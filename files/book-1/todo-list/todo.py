#!/usr/bin/env python3
"""A tiny terminal to-do list: add tasks, list them, mark them done.

Storage is a JSON file (tasks.json) next to this script. Task numbers are
1-based positions in the list and stay stable because tasks are never deleted.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

TASKS_FILE = Path(__file__).resolve().parent / "tasks.json"


def load_tasks(path: Path = TASKS_FILE) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks: list[dict], path: Path = TASKS_FILE) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
        f.write("\n")


def cmd_add(args: argparse.Namespace, path: Path = TASKS_FILE) -> int:
    text = args.description.strip()
    if not text:
        print("Task description cannot be empty.", file=sys.stderr)
        return 1
    tasks = load_tasks(path)
    tasks.append({"text": text, "done": False})
    save_tasks(tasks, path)
    print(f"Added task {len(tasks)}: {text}")
    return 0


def cmd_list(args: argparse.Namespace, path: Path = TASKS_FILE) -> int:
    tasks = load_tasks(path)
    if not tasks:
        print("No tasks yet. Add one with: todo.py add \"<description>\"")
        return 0
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['text']}")
    return 0


def cmd_done(args: argparse.Namespace, path: Path = TASKS_FILE) -> int:
    tasks = load_tasks(path)
    n = args.number
    if n < 1 or n > len(tasks):
        print(f"No task numbered {n}. Run 'list' to see task numbers.", file=sys.stderr)
        return 1
    task = tasks[n - 1]
    if task["done"]:
        print(f"Task {n} was already done: {task['text']}")
        return 0
    task["done"] = True
    save_tasks(tasks, path)
    print(f"Marked task {n} done: {task['text']}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="todo.py", description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="add a new task")
    p_add.add_argument("description", help="what the task is")
    p_add.set_defaults(func=cmd_add)

    p_list = sub.add_parser("list", help="show every task and its status")
    p_list.set_defaults(func=cmd_list)

    p_done = sub.add_parser("done", help="mark a task complete by its number")
    p_done.add_argument("number", type=int, help="the task number shown by 'list'")
    p_done.set_defaults(func=cmd_done)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
