"""Tests for todo.py. Run: python -m pytest  (or: python -m unittest)."""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import todo


class TodoTests(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.path = Path(self._tmp.name) / "tasks.json"

    def run_cmd(self, *argv):
        args = todo.build_parser().parse_args(list(argv))
        return args.func(args, self.path)

    def test_load_missing_file_returns_empty(self):
        self.assertEqual(todo.load_tasks(self.path), [])

    def test_save_load_round_trip(self):
        tasks = [{"text": "buy milk", "done": False}, {"text": "call mum", "done": True}]
        todo.save_tasks(tasks, self.path)
        self.assertEqual(todo.load_tasks(self.path), tasks)

    def test_add_appends_task(self):
        self.assertEqual(self.run_cmd("add", "write report"), 0)
        self.assertEqual(todo.load_tasks(self.path), [{"text": "write report", "done": False}])

    def test_add_rejects_empty_description(self):
        self.assertEqual(self.run_cmd("add", "   "), 1)
        self.assertEqual(todo.load_tasks(self.path), [])

    def test_done_marks_only_target_task(self):
        self.run_cmd("add", "one")
        self.run_cmd("add", "two")
        self.assertEqual(self.run_cmd("done", "1"), 0)
        tasks = todo.load_tasks(self.path)
        self.assertTrue(tasks[0]["done"])
        self.assertFalse(tasks[1]["done"])

    def test_done_rejects_out_of_range(self):
        self.run_cmd("add", "only task")
        self.assertEqual(self.run_cmd("done", "5"), 1)
        self.assertEqual(self.run_cmd("done", "0"), 1)
        self.assertFalse(todo.load_tasks(self.path)[0]["done"])

    def test_done_is_idempotent(self):
        self.run_cmd("add", "task")
        self.assertEqual(self.run_cmd("done", "1"), 0)
        self.assertEqual(self.run_cmd("done", "1"), 0)

    def test_list_empty_and_populated(self):
        self.assertEqual(self.run_cmd("list"), 0)
        self.run_cmd("add", "task")
        self.assertEqual(self.run_cmd("list"), 0)


if __name__ == "__main__":
    unittest.main()
