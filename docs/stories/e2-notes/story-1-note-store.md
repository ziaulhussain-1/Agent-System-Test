# Story 1 — Note model and store

ID: E2-S1
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As a developer agent, I can create, read, update, delete and list notes through one module, so that no endpoint story writes SQL.

## Description

The note's request/response models and every SQL statement touching the `notes` table. Models live beside the feature, not in a shared `models.py` (`docs/architecture.md` §2).

This story gates most of the project: E2-S2, E2-S3 and all of E3, E4 and E5 read notes. It should go out alone.

## Acceptance Criteria

- `create(title, body)` returns the stored note with id and both timestamps.
- `get(id)` returns the note or `None` — the store does not raise HTTP errors; that is the router's job.
- `list(limit, offset)` returns notes newest first.
- `update(id, title=None, body=None)` changes only what is given and moves `updated_at`.
- `delete(id)` reports whether a row went.
- An empty or whitespace-only title or body is rejected by the model.

## Files This Story Owns

- `app/notes/__init__.py`
- `app/notes/models.py`
- `app/notes/store.py`
- `tests/test_notes_store.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1` complete.

## Non-Functional

- Parameterised SQL only — never string interpolation.
- `created_at` never changes after creation.

## Out of Scope

No HTTP layer; no tags, search or export.

## Test Notes

- Round trip through every store function.
- Partial update leaves the untouched field alone and moves `updated_at`.
- `get` of a missing id returns `None` rather than raising.
- Empty and whitespace-only titles are rejected.
