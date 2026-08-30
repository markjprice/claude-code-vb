# CLAUDE.md

## Project

**Photo Renamer** — a tool (not yet built) that renames a folder of vacation
`.jpg` photos to `YYYY-MM-DD-original-name.jpg` using the date each photo was
taken. See [BRIEF.md](BRIEF.md) for the full spec, acceptance criteria, and
non-goals.

Key requirements from the brief:
- Input: a folder of `.jpg` files.
- Output: each renamed to `YYYY-MM-DD-original-name.jpg` based on capture date
  (read from EXIF).
- Files already matching that pattern are left unchanged (idempotent).
- Non-goals: sorting into folders, non-`.jpg` file types.

## Current state

Just getting started. The repo currently contains only:
- `BRIEF.md` — the project brief.
- `index.html` — an unrelated static "Hello, Builder" intro page.

No implementation, build system, dependencies, or tests exist yet. Not a git
repository yet.

## Environment

- Windows 11, PowerShell. Chain commands with `;` and `if ($?)`, not `&&`.
- Author/owner: Mark (markjprice@gmail.com).

## Commands

None yet — to be added once a language/toolchain is chosen.
