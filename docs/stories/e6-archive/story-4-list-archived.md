# Story 4 — List archived notes

ID: E6-S4
Epic: `docs/stories/e6-archive/epic.md`
Status: Draft

## User Story

As an API consumer, I can list archived notes, so that removing a note is recoverable.

## Description

`GET /archive`, in its own module.

## Acceptance Criteria

- Returns a bare array of notes, most recently archived first.
- An empty archive returns `[]` with 200.
- `limit` defaults to 20, caps at 100, over-cap is clamped not rejected.
- Negative `limit` or `offset` returns 422.
- Ordering is deterministic (newest first, id descending as tiebreak) or paging repeats rows across pages.

## Files This Story Owns

- `app/archive/routes_list-archived.py`
- `tests/test_archive_list-archived.py`

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

- Order is by archive time, not note time.
- Empty archive returns `[]`.
