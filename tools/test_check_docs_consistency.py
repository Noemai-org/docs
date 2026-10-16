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


class SpellingScan(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
