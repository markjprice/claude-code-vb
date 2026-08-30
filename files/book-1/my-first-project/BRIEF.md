# Photo Renamer

## User and problem

Someone who imports **hundreds** of vacation photos and can never find
a specific one later.

## Smallest useful version

Rename each photo to include the date it was taken.

## Acceptance criteria

- Given a folder of `.jpg` files, renames each one to `YYYY-MM-DD-original-name.jpg` based on the date it was taken
- Leaves files that already match this pattern *unchanged*

## Non-goals

- Sorting photos into folders
- Handling file types other than `.jpg`
