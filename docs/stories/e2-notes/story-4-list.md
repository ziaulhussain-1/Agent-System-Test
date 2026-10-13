# Story 4 — List notes with paging

ID: E2-S4
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As an API consumer, I can list notes with paging over HTTP, so that the store is reachable.

## Description

`GET /notes` returning 200. Its own module, so this story and the other four endpoint stories in this epic can be built at the same time by different machines — which is the whole reason routers are discovered rather than listed.

## Acceptance Criteria

- `GET /notes` succeeds with **200**.
- Returns a JSON **array**, newest first, with no envelope.
- An empty database returns `[]` with 200, not 404.
- `limit` defaults to 20, caps at 100, over-cap is clamped not rejected.
- Negative `limit` or `offset` returns 422.
- Ordering is deterministic (newest first, id descending as tiebreak) or paging repeats rows across pages.

## Files This Story Owns

- `app/notes/routes_list.py`
- `tests/test_notes_list.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1`.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Responses are bare objects; no envelope (`docs/architecture.md` §4.2).
- Errors use FastAPI's `{"detail": ...}` shape (§4.3).

## Out of Scope

The other notes endpoints — each is its own story. Tags, search, export.

## Test Notes

- Paging across a known set returns each note exactly once, with no duplicate at the page boundary.
- Over-cap limit is clamped.
- Empty database returns `[]`.
