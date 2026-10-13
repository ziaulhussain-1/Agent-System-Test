# Story 6 — Delete a note

ID: E2-S6
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As an API consumer, I can delete a note over HTTP, so that the store is reachable.

## Description

`DELETE /notes/{id}` returning 204. Its own module, so this story and the other four endpoint stories in this epic can be built at the same time by different machines — which is the whole reason routers are discovered rather than listed.

## Acceptance Criteria

- `DELETE /notes/{id}` succeeds with **204**.
- Returns **204** with no body.
- An unknown id returns 404.
- Deleting twice returns 404 the second time, not 204.

## Files This Story Owns

- `app/notes/routes_delete.py`
- `tests/test_notes_delete.py`

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

- 204 and an empty body.
- The note is really gone afterwards.
- Second delete returns 404.
