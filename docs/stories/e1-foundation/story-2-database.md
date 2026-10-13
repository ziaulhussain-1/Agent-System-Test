# Story 2 — Database connection and schema

ID: E1-S2
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As a developer agent, I can get a working SQLite connection with the schema already in place, so that no feature story writes DDL.

## Description

Create `app/db.py`: a connection helper and the schema bootstrap for the three tables in `docs/architecture.md` §5. The application uses a file (`./notes.db`, gitignored); tests get their own in-memory database through a fixture, so three machines running the suite at once cannot collide (`docs/architecture.md` §4.6).

Foreign keys must be ON. SQLite disables them per connection by default, which makes the `note_tags` cascade silently do nothing — a bug that surfaces much later, in the tags epic, looking like someone else's fault.

## Acceptance Criteria

- Given a fresh database, when the app starts, then `notes`, `tags` and `note_tags` exist with the columns in the architecture.
- Given the app starts twice against the same file, then the second start succeeds and no data is lost.
- Given a connection from the helper, then `PRAGMA foreign_keys` is on.
- Given a note is deleted, then its `note_tags` rows go with it.
- A fixture yields an isolated in-memory database per test file.

## Files This Story Owns

- `app/db.py`
- `tests/test_db.py`
- `tests/conftest.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1-S1` (the app must exist to bootstrap on startup).

## Non-Functional

- No ORM. The data model is three tables; an ORM would add a shared mapping file for every story to touch.
- Schema creation is idempotent.

## Out of Scope

No migration framework. No seed data.

## Test Notes

- Schema is created on a fresh database, and re-running is safe.
- Foreign keys are enforced: deleting a note removes its tag links.
- Two tests in the same file get independent databases.
