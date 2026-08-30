import tempfile
import unittest
from datetime import datetime
from pathlib import Path

import journal


class AddEntryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / "journal.txt"
        self.addCleanup(self.tmp.cleanup)

    def test_appends_dated_message(self):
        journal.add_entry("hello world", self.path)
        text = self.path.read_text(encoding="utf-8")
        self.assertIn(datetime.now().strftime("%Y-%m-%d"), text)
        self.assertIn("hello world", text)
        self.assertTrue(text.endswith("\n"))

    def test_creates_file_when_missing(self):
        self.assertFalse(self.path.exists())
        journal.add_entry("first", self.path)
        self.assertTrue(self.path.exists())

    def test_second_entry_same_day_is_appended(self):
        journal.add_entry("first", self.path)
        journal.add_entry("second", self.path)
        lines = self.path.read_text(encoding="utf-8").splitlines()
        self.assertEqual(len(lines), 2)
        self.assertIn("first", lines[0])
        self.assertIn("second", lines[1])

    def test_main_without_message_returns_nonzero(self):
        self.assertNotEqual(journal.main([]), 0)
        self.assertNotEqual(journal.main(["   "]), 0)


if __name__ == "__main__":
    unittest.main()
