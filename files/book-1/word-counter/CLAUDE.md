# CLAUDE.md

## What this is

Word Counter — a CLI tool that, given a `.txt` file, reports its word count,
sentence count, and character count. See [BRIEF.md](BRIEF.md) for the full
problem statement and [README.md](README.md) for usage.

## Structure

- [wordcount.py](wordcount.py) — the whole tool. Pure counting functions
  (`count_words`, `count_sentences`, `count_characters`), `read_text_file` for
  validation/IO, `analyze` to combine, `main` for the argparse CLI.
- [tests/test_wordcount.py](tests/test_wordcount.py) — pytest suite.
- [tests/conftest.py](tests/conftest.py) — puts the repo root on `sys.path`.

Stdlib only; `pytest` is the sole dependency, for tests.

## Commands

Python is not on PATH as `python`; use the `py` launcher.

- Run: `py -3 wordcount.py <file.txt>`
- Test: `py -3 -m pytest`
- Install pytest (once): `py -3 -m pip install pytest`

## Counting rules

- words: whitespace-separated tokens.
- sentences: runs of `.` `!` `?`; non-empty text with none → 1; empty/whitespace → 0.
- characters: raw length, whitespace included.
- Non-`.txt` path or missing file → exit 1, message on stderr.

## Notes

- Platform: Windows 11, PowerShell primary shell.
- Local pip installs may fail intermittently (network resets observed).
