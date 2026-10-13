# Story 1 — Note model, schema and store

ID: E2-S1
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As a developer agent, I can persist and retrieve notes through one module, so that no endpoint story writes SQL.

## Description

The `notes` table, the note's models, and every statement touching it. Owns its own `schema.sql`, applied by the discovery in `E1-S2`.

**This story gates most of the project** — five endpoint stories here plus all of E3 through E8 read notes through it. It goes out in a wave of its own.

## Acceptance Criteria

- `create(title, body)` returns the stored note with id and both timestamps.
- `get(id)` returns the note or `None`; the store never raises HTTP errors.
- `list(limit, offset)` returns notes newest first.
- `update(id, title=None, body=None)` changes only what is given, moves `updated_at`, leaves `created_at` alone.
- `delete(id)` reports whether a row went.
- Empty or whitespace-only title or body is rejected by the model.

## Files This Story Owns

- `app/notes/__init__.py`
- `app/notes/models.py`
- `app/notes/store.py`
- `app/notes/schema.sql`
- `tests/test_notes_store.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1` complete.

## Non-Functional

- Parameterised SQL only.
- `created_at` never changes after creation.

## Out of Scope

Any HTTP layer. Tags, search, export.

## Test Notes

- Round trip through every store function.
- Partial update leaves the untouched field alone and moves `updated_at`.
- `get` of a missing id returns `None`.
- Whitespace-only titles rejected.
