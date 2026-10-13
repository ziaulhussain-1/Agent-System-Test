# Story 2 — Create a note

ID: E2-S2
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As an API consumer, I can create a note over HTTP, so that the store is reachable.

## Description

`POST /notes` returning 201. Its own module, so this story and the other four endpoint stories in this epic can be built at the same time by different machines — which is the whole reason routers are discovered rather than listed.

## Acceptance Criteria

- `POST /notes` succeeds with **201**.
- An invalid body returns 422 in FastAPI's own shape — we do not hand-write validation errors.
- The response carries the created note, including its new id.

## Files This Story Owns

- `app/notes/routes_create.py`
- `tests/test_notes_create.py`

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

- 201 and the note body.
- Missing title returns 422.
- Whitespace-only title returns 422, not a note with a blank title.
