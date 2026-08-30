# Word Counter

A tiny CLI that reports the word, sentence, and character counts of a `.txt` file.

## Usage

```
py -3 wordcount.py path/to/file.txt
```

Output:

```
words:      6
sentences:  2
characters: 30
```

## Counting rules

- **words** — whitespace-separated tokens
- **sentences** — runs of `.`, `!`, or `?`; a non-empty file with none still counts as 1
- **characters** — every character, whitespace included
- empty file → `0` for all three

Only `.txt` files are accepted; other extensions and missing files exit with
status `1` and an error on stderr.

## Tests

```
py -3 -m pytest
```

Requires `pytest` (`py -3 -m pip install pytest`).
