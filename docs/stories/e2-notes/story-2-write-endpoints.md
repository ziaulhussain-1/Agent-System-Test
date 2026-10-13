# Story 2 — Create, update and delete a note

ID: E2-S2
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As an API consumer, I can create, change and remove notes over HTTP, so that the store is actually reachable.

## Description

The write half of the notes API: `POST /notes`, `PATCH /notes/{id}`, `DELETE /notes/{id}`. The read endpoints are `E2-S3` and live in a different file, so the two can be built at the same time by different machines.

## Acceptance Criteria

- `POST /notes` with a valid body returns **201** and the created note.
- `POST /notes` with an invalid body returns 422 in FastAPI's own shape — we do not hand-write validation errors (`docs/architecture.md` §4.3).
- `PATCH /notes/{id}` updates only the fields supplied and returns the note.
- `PATCH` or `DELETE` of an unknown id returns 404 `{"detail": "..."}`.
- `DELETE /notes/{id}` returns **204** with no body.
- Responses are bare note objects, with no envelope.

## Files This Story Owns

- `app/notes/routes_write.py`
- `tests/test_notes_write.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1`.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Status codes exactly as above; a 200 where a 201 belongs is a defect.

## Out of Scope

Reading and listing (`E2-S3`). Bulk operations.

## Test Notes

- One test per status code above.
- A partial `PATCH` does not blank the field that was not sent — the mistake this endpoint shape invites.
