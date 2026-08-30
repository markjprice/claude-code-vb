# CLAUDE.md

## Project

A terminal to-do list tool. Add a task, list all tasks with status, mark a task done by number.
See [BRIEF.md](BRIEF.md) for the full spec, acceptance criteria, and non-goals.

## Structure

```
todo-list/
  todo.py        The CLI (stdlib only: argparse, json, pathlib)
  test_todo.py   Tests (unittest)
  tasks.json     Task store, created on first `add`, git-ignored
  BRIEF.md       Product brief
  CLAUDE.md      This file
```

## Commands

Windows has no `python` on PATH — use the `py` launcher (Python 3.14).

```
py todo.py add "<description>"   # add a task
py todo.py list                  # show every task; [x] = done, [ ] = open
py todo.py done <number>         # mark task <number> complete
py -m unittest -v                # run the tests
```

## Notes

- Storage: `tasks.json` next to `todo.py` — a JSON list of `{"text": str, "done": bool}`.
  Single device by design (syncing is a non-goal).
- Task numbers are 1-based list positions. Stable because tasks are never deleted
  (`done` only flips a flag; there is no delete — a non-goal).
- Command functions take an optional `path` arg so tests can point at a temp file.
- Non-goals: due dates, reminders, multi-device sync, hard delete.
