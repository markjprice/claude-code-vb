"""Journal Logger — append a quick, dated note to journal.txt."""

import sys
from datetime import datetime
from pathlib import Path

DEFAULT_JOURNAL = Path(__file__).parent / "journal.txt"


def add_entry(message, journal_path=DEFAULT_JOURNAL):
    """Append a timestamped entry for ``message`` to ``journal_path``.

    The file is created if it does not exist; existing content is never
    overwritten.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(journal_path, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} — {message}\n")
    return timestamp


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    message = " ".join(argv).strip()
    if not message:
        print('usage: py journal.py "your note here"', file=sys.stderr)
        return 1
    add_entry(message)
    print(f"Added entry to {DEFAULT_JOURNAL.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
