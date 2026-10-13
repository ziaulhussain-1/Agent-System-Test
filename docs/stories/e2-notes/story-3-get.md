# Story 3 — Fetch one note

ID: E2-S3
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As an API consumer, I can fetch one note over HTTP, so that the store is reachable.

## Description

`GET /notes/{id}` returning 200. Its own module, so this story and the other four endpoint stories in this epic can be built at the same time by different machines — which is the whole reason routers are discovered rather than listed.

## Acceptance Criteria

- `GET /notes/{id}` succeeds with **200**.
- An unknown id returns 404 `{"detail": ...}`.
- A non-integer id returns 422, not 404 — the request is malformed, not the resource missing.

## Files This Story Owns

- `app/notes/routes_get.py`
- `tests/test_notes_get.py`

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

- 200 and the bare note.
- Unknown id returns 404.
- `/notes/abc` returns 422.
