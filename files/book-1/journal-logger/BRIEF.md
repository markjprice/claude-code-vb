# Journal Logger

## User and problem

You, when you want to jot a quick, dated note about your day, without opening a separate notes app or journal to do it.

## Smallest useful version

Running the tool with a short message appends a new, dated entry to a single journal file.

## Acceptance criteria

- Running the tool with a message appends a new line to `journal.txt`, including today's date and the message
- Creates `journal.txt` automatically the first time it's needed, if the file doesn't already exist
- Running the tool a second time on the same day adds a new dated entry, rather than overwriting the previous one

## Non-goals

- Editing or deleting a past entry
- Searching or filtering past entries
- A graphical interface

