# Story 2 — Database connection and schema discovery

ID: E1-S2
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As a developer agent, I can add a table by adding a file to my own feature folder, so that no epic edits a shared bootstrap.

## Description

`app/db.py`: a connection helper, and schema bootstrap by **discovery** — it applies every `app/<area>/schema.sql` it finds at startup.

Discovery rather than a hardcoded list for the same reason routers are discovered: a central `CREATE TABLE` block would be a file that grows with every epic and conflicts on every wave. Each feature owns its own schema.

Foreign keys must be ON. SQLite disables them per connection by default, which makes cascades silently do nothing — a bug that surfaces later, in someone else's epic, looking like their fault.

## Acceptance Criteria

- Every `app/<area>/schema.sql` is applied at startup, in a stable order.
- Schema files must be idempotent (`CREATE TABLE IF NOT EXISTS`); applying twice is safe and loses no data.
- `PRAGMA foreign_keys` is ON for every connection the helper returns.
- A malformed schema file fails startup loudly, naming the file.
- The app uses `./notes.db`; the path is overridable for tests.

## Files This Story Owns

- `app/db.py`
- `tests/test_db.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1-S1`.

## Non-Functional

- No ORM; an ORM adds a shared mapping file for every story to touch.
- Parameterised SQL only, everywhere, forever.

## Out of Scope

Migrations. Seed data. Any feature's actual tables — those belong to their epics.

## Test Notes

- A temp feature folder with a `schema.sql` has its table created.
- Running the bootstrap twice is safe.
- Foreign keys are enforced.
- A malformed schema file fails loudly and names itself.
