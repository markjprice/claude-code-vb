#!/usr/bin/env python3
"""Report word, sentence, and character counts for a .txt file."""

import argparse
import re
import sys
from pathlib import Path

_SENTENCE_END = re.compile(r"[.!?]+")


def count_characters(text: str) -> int:
    """Every character in the text, including whitespace."""
    return len(text)


def count_words(text: str) -> int:
    """Whitespace-separated tokens."""
    return len(text.split())


def count_sentences(text: str) -> int:
    """Runs of sentence-ending punctuation.

    A non-empty text with no such punctuation still counts as one sentence.
    Empty (or whitespace-only) text counts as zero.
    """
    if not text.strip():
        return 0
    count = len(_SENTENCE_END.findall(text))
    return count if count > 0 else 1


def analyze(text: str) -> dict[str, int]:
    return {
        "words": count_words(text),
        "sentences": count_sentences(text),
        "characters": count_characters(text),
    }


def read_text_file(path: Path) -> str:
    if path.suffix.lower() != ".txt":
        raise ValueError(f"not a .txt file: {path}")
    if not path.is_file():
        raise FileNotFoundError(f"no such file: {path}")
    return path.read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="path to a .txt file")
    args = parser.parse_args(argv)

    try:
        text = read_text_file(args.path)
    except (ValueError, FileNotFoundError, OSError) as err:
        print(f"error: {err}", file=sys.stderr)
        return 1

    counts = analyze(text)
    print(f"words:      {counts['words']}")
    print(f"sentences:  {counts['sentences']}")
    print(f"characters: {counts['characters']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
