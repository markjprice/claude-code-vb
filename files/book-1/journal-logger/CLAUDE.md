# CLAUDE.md

## Project

**Journal Logger** — a tiny command-line tool for appending quick, dated notes to a single
journal file. See [BRIEF.md](BRIEF.md) for the full product brief.

## Layout

- [journal.py](journal.py) — the CLI. `add_entry(message, journal_path)` does the work;
  `main(argv)` handles argument parsing and exit codes.
- [test_journal.py](test_journal.py) — `unittest` tests (stdlib only), each in a temp dir.
- `journal.txt` — the journal itself, created on first use. Git-ignored (personal data).

## Behaviour (from BRIEF.md)

- Run with a message → appends `YYYY-MM-DD HH:MM — <message>` as a new line to `journal.txt`.
- Creates `journal.txt` automatically on first use (open mode `"a"`).
- Append-only: a second run the same day adds another entry; past entries are never modified.
- No message → prints usage to stderr, exits 1.
- `journal.txt` is resolved relative to the script, so it works from any working directory.

### Non-goals

Editing/deleting past entries, searching/filtering, any GUI.

## Environment

- Windows 11, PowerShell. Python 3.14 via the **`py`** launcher — bare `python` is not on PATH
  (it hits the Microsoft Store alias).

## Commands

- Run: `py journal.py "your note here"`
- Test: `py -m unittest`

## Not a git repo

Run `git init` if version control is wanted.
