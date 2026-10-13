# Story 3 — Restore a note

ID: E6-S3
Epic: `docs/stories/e6-archive/epic.md`
Status: Draft

## User Story

As an API consumer, I can restore a note, so that removing a note is recoverable.

## Description

`DELETE /notes/{id}/archive`, in its own module.

## Acceptance Criteria

- Returns 204.
- Restoring a note that was not archived returns 404.
- An unknown note id returns 404.

## Files This Story Owns

- `app/archive/routes_restore-endpoint.py`
- `tests/test_archive_restore-endpoint.py`

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

- 204 on success.
- Restoring an unarchived note returns 404.
