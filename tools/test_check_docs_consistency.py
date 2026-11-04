#!/usr/bin/env python3
"""Tests for the spelling scan in check_docs_consistency.py.

Run from the repository root:
    python3 -m unittest discover -s tools -p 'test_*.py'

Standard library only. The old spelling is built from parts so this file does not contain it.
"""
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_docs_consistency as cdc  # noqa: E402

BAD = "tu" + "che"


def run_git(root, *args):
    subprocess.run(["git", *args], cwd=root, check=True, capture_output=True)


class TempRepoCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name
        run_git(self.root, "init", "-q")
        self._old_root = cdc.ROOT
        cdc.ROOT = self.root

    def tearDown(self):
        cdc.ROOT = self._old_root
        self._tmp.cleanup()

    def put(self, rel, text, track=False):
        full = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(text)
        if track:
            run_git(self.root, "add", rel)



class SpellingScan(TempRepoCase):
    def failures(self):
        out = []
        cdc.check_spelling(out.append)
        return out

    def test_untracked_file_with_old_spelling_fails(self):
        self.put("docs/note.md", f"Partner {BAD} wrote back.\n")
        fails = self.failures()
        self.assertEqual(len(fails), 1, fails)
        self.assertIn("docs/note.md:1", fails[0])

    def test_tracked_file_with_old_spelling_fails(self):
        self.put("docs/note.md", f"{BAD}\n", track=True)
        self.assertEqual(len(self.failures()), 1)

    def test_untracked_path_with_old_spelling_fails(self):
        self.put(f"docs/{BAD}-notes.md", "clean text\n")
        self.assertIn("path contains", self.failures()[0])

    def test_gitignored_file_is_not_scanned(self):
        self.put(".gitignore", "scratch/\n")
        self.put("scratch/note.md", f"{BAD}\n")
        self.assertEqual(self.failures(), [])

    def test_frozen_file_is_exempt(self):
        self.put("docs/record.md", f"quoted old spelling: {BAD}\n")
        self.put(cdc.FROZEN_LIST, "0" * 64 + "  docs/record.md\n")
        self.assertEqual(self.failures(), [])

    def test_unfrozen_neighbour_of_a_frozen_file_still_fails(self):
        self.put("docs/record.md", f"{BAD}\n")
        self.put("docs/other.md", f"{BAD}\n")
        self.put(cdc.FROZEN_LIST, "0" * 64 + "  docs/record.md\n")
        fails = self.failures()
        self.assertEqual(len(fails), 1)
        self.assertIn("docs/other.md", fails[0])

    def test_partner_source_directory_is_exempt(self):
        self.put(cdc.FROZEN_SOURCE_DIR + "spec.md", f"{BAD}\n")
        self.assertEqual(self.failures(), [])

    def test_correct_spelling_passes(self):
        self.put("docs/note.md", "Tushe wrote back.\n")
        self.assertEqual(self.failures(), [])


class RetiredOrgLinks(TempRepoCase):
    URL = "https://github.com/" + "noema" + "-org/docs/pull/1"

    def failures(self):
        out = []
        cdc.check_links_to_retired_org(out.append)
        return out

    def test_url_to_retired_org_fails(self):
        self.put("docs/note.md", f"See {self.URL}\n")
        fails = self.failures()
        self.assertEqual(len(fails), 1, fails)
        self.assertIn("docs/note.md:1", fails[0])

    def test_url_to_canonical_org_passes(self):
        self.put("docs/note.md", "See https://github.com/Noemai-org/docs/pull/1\n")
        self.assertEqual(self.failures(), [])

    def test_frozen_file_may_keep_the_old_url(self):
        self.put("docs/record.md", f"{self.URL}\n")
        self.put(cdc.FROZEN_LIST, "0" * 64 + "  docs/record.md\n")
        self.assertEqual(self.failures(), [])

    def test_untracked_file_is_scanned(self):
        self.put("docs/new.md", f"{self.URL}\n")
        self.assertEqual(len(self.failures()), 1)


class NoCodeInDocs(TempRepoCase):
    def failures(self):
        out = []
        cdc.check_no_code(out.append)
        return out

    def test_contracts_and_packs_directories_fail(self):
        self.put("contracts/schema.json", "{}\n")
        self.put("packs/fintech_v1.json", "{}\n")
        self.assertEqual(len(self.failures()), 2)

    def test_source_code_outside_the_exempt_places_fails(self):
        self.put("docs/example.py", "print('x')\n")
        self.put("services/core/main.go", "package main\n")
        self.assertEqual(len(self.failures()), 2)

    def test_untracked_code_is_found(self):
        self.put("tools/packcheck.py", "x = 1\n")
        self.assertIn("tools/packcheck.py", self.failures()[0])

    def test_own_checkers_and_their_tests_are_exempt(self):
        for name in sorted(cdc.OWN_CHECKERS):
            self.put(name, "x = 1\n")
        self.assertEqual(self.failures(), [])

    def test_infrastructure_code_is_allowed_in_the_two_directories(self):
        self.put(".github/scripts/main-merge-audit.js", "x = 1\n")
        self.put(".github/scripts/another_helper.py", "x = 1\n")
        self.put(".github/tests/main-merge-audit.test.js", "x = 1\n")
        self.put(".github/tests/fixtures/sample.json", "{}\n")
        self.assertEqual(self.failures(), [])

    def test_a_code_file_anywhere_else_still_fails(self):
        for where in (".github/workflows/helper.js", ".github/helper.js", ".githubx/scripts/a.js", "scripts/a.js",
                      "tools/new_tool.py", "docs/tool.js", "main.go", ".github/scriptsx/a.js"):
            self.put(where, "x = 1\n")
        failures = self.failures()
        self.assertEqual(len(failures), 8, failures)

    def test_archive_is_exempt(self):
        self.put("docs/archive/2026-10-pre-poc-drafts/example.py", "x = 1\n")
        self.put("docs/archive/2026-10-pre-poc-drafts/contracts/schema.yaml", "a: 1\n")
        self.assertEqual(self.failures(), [])

    def test_documents_pass(self):
        self.put("docs/README.md", "text\n")
        self.put("tools/frozen-files.sha256", "")
        self.put(".github/workflows/docs-consistency.yml", "name: x\n")
        self.assertEqual(self.failures(), [])


if __name__ == "__main__":
    unittest.main()


class NamedVersions(TempRepoCase):
    """OPS-09: a README names the highest plan and PERD on disk, compared as numbers."""

    def disk(self, plan, perd):
        for v in plan:
            self.put(f"docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v{v}.md", "x")
        for v in perd:
            self.put(f"docs/poc/perd/NOEMA_POC_PERD_v{v}.md", "x")

    def readme(self, plan, perd):
        text = f"[four-week implementation plan](docs/poc/execution/README.md) v{plan}\n[POC PERD](docs/poc/perd/README.md) v{perd}\n"
        self.put("README.md", text)
        self.put("docs/README.md", f"execution/ four-week plan v{plan} (current)\nperd/ POC PERD v{perd} (current)\n")

    def failures(self):
        out = []
        cdc.check_named_versions(out.append)
        return out

    def test_the_highest_version_on_disk_passes(self):
        self.disk(["1.9", "1.10"], ["1.19", "1.9"])
        self.readme("1.10", "1.19")
        self.assertEqual(self.failures(), [])

    def test_v1_10_beats_v1_9_as_a_number(self):
        self.disk(["1.9", "1.10"], ["1.9"])
        self.readme("1.9", "1.9")
        out = self.failures()
        self.assertTrue(any("names plan v1.9" in m and "v1.10" in m for m in out), out)

    def test_a_stale_perd_fails_in_both_readmes(self):
        self.disk(["1.10"], ["1.5", "1.19"])
        self.readme("1.10", "1.5")
        out = self.failures()
        self.assertEqual(sum("names PERD v1.5" in m for m in out), 2, out)

    def test_a_readme_that_names_no_version_fails(self):
        self.disk(["1.10"], ["1.19"])
        self.put("README.md", "nothing\n")
        self.put("docs/README.md", "nothing\n")
        out = self.failures()
        self.assertTrue(any("does not name the plan version" in m for m in out), out)
        self.assertTrue(any("does not name the PERD version" in m for m in out), out)
