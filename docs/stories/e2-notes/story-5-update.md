# Story 5 — Update a note

ID: E2-S5
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As an API consumer, I can update a note over HTTP, so that the store is reachable.

## Description

`PATCH /notes/{id}` returning 200. Its own module, so this story and the other four endpoint stories in this epic can be built at the same time by different machines — which is the whole reason routers are discovered rather than listed.

## Acceptance Criteria

- `PATCH /notes/{id}` succeeds with **200**.
- Only the fields supplied change; omitted fields keep their values.
- An unknown id returns 404.
- An empty body is a no-op returning the note unchanged, not a 422.

## Files This Story Owns

- `app/notes/routes_update.py`
- `tests/test_notes_update.py`

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

- A partial PATCH does not blank the field that was not sent — the mistake this endpoint shape invites.
- `updated_at` moves; `created_at` does not.
