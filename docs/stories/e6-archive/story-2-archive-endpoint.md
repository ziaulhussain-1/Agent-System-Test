# Story 2 — Archive a note

ID: E6-S2
Epic: `docs/stories/e6-archive/epic.md`
Status: Draft

## User Story

As an API consumer, I can archive a note, so that removing a note is recoverable.

## Description

`POST /notes/{id}/archive`, in its own module.

## Acceptance Criteria

- Returns 200 and the archive record.
- Archiving an already-archived note returns 200, not an error.
- An unknown note id returns 404.

## Files This Story Owns

- `app/archive/routes_archive-endpoint.py`
- `tests/test_archive_archive-endpoint.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E6-S1`.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Responses are bare objects; no envelope (`docs/architecture.md` §4.2).
- Errors use FastAPI's `{"detail": ...}` shape (§4.3).

## Out of Scope

The other archive endpoints.

## Test Notes

- Idempotent archive returns 200.
- Unknown id returns 404.
