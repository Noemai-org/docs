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
