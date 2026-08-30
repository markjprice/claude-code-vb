# CLAUDE.md

## Project

Unit Converter — a small CLI tool to convert a number from one unit to another
within a category the user uses often. See [BRIEF.md](BRIEF.md) for the product
brief and [README.md](README.md) for user-facing usage.

## Status

Working first version. Two categories supported: **volume** (US cooking measures,
base unit millilitre) and **currency** (base unit USD, static hand-entered rates).
Python 3, standard library only. Not a git repository.

## Structure

- [convert.py](convert.py) — everything: category data tables (`VOLUME`,
  `CURRENCY`, `CATEGORIES`), pure core (`normalize_unit`, `convert`,
  `ConversionError`), and the `argparse` CLI (`main`).
- [tests/test_convert.py](tests/test_convert.py) — pytest; covers core + CLI
  (`main([...])` and a `subprocess` run).

## Commands

- Run: `py convert.py <value> <from> <to>` (e.g. `py convert.py 1 cup ml`)
- List units: `py convert.py --list`
- Tests: `py -m pytest -q`

Note: on this machine the `python` command is not installed — use the `py`
launcher (Python 3.14, pytest 9.x).

## Conventions

- A new category = a new dict in `CATEGORIES` with `base`, `decimals`, `units`
  (canonical → factor-to-base), and `aliases` (alias → canonical). No other code
  changes needed.
- Category is inferred from the units given; both must belong to the same one.
  `--category` forces it.
- Currency rates in `CURRENCY["units"]` are static approximations (USD per unit),
  not live — edit by hand.

## Acceptance criteria (from BRIEF.md)

- Given number + from + to in a supported category, return the converted value.
- Unsupported unit → clear message naming supported units, exit code 1, never a wrong number.
- Round to a sensible number of decimals (currently 2 for both categories).

## Non-goals

- Unit/category coverage beyond volume + currency.
- Live currency exchange rates.
- A GUI.

## Environment

- Platform: Windows 11, PowerShell (Bash tool also available).
- Working directory: `c:\claude\unit-converter`.
