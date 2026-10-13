# Story 1 — Archive store and schema

ID: E6-S1
Epic: `docs/stories/e6-archive/epic.md`
Status: Draft

## User Story

As a developer agent, I can archive a note without deleting it, so that removal is recoverable.

## Description

A `note_archive` table and the statements touching it.

A separate table rather than a column on `notes`, deliberately: a column would mean editing `app/notes/schema.sql`, which `E2-S1` owns, and every notes query would need a filter added — touching five endpoint stories owned by other machines. Its own table keeps the epic self-contained.

## Acceptance Criteria

- `archive(note_id)` records the note as archived with a timestamp; archiving twice is idempotent.
- `restore(note_id)` removes the record and reports whether one went.
- `is_archived(note_id)` and `list_archived(limit, offset)` work as named.
- Archiving a missing note is a reported error, not a silent row.
- Deleting a note removes its archive record (cascade).

## Files This Story Owns

- `app/archive/__init__.py`
- `app/archive/store.py`
- `app/archive/schema.sql`
- `tests/test_archive_store.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1`.

## Non-Functional

- Parameterised SQL only.
- Archiving never mutates the `notes` table — that table belongs to another epic.

## Out of Scope

Changing how `GET /notes` behaves. Automatic archiving. Purge policies.

## Test Notes

- Archive, restore, and archive-twice are all correct.
- Archiving a missing note is reported.
- The cascade works on delete.
