# Story 2 — Attach a tag

ID: E3-S2
Epic: `docs/stories/e3-tags/epic.md`
Status: Draft

## User Story

As an API consumer, I can attach a tag over HTTP, so that tags are useful for organising and finding notes.

## Description

`POST /notes/{id}/tags`, in its own module so the four tag endpoints can be built concurrently.

## Acceptance Criteria

- `POST /notes/{id}/tags` with `{"name": "work"}` returns 201 and the note's tags.
- Attaching a tag the note already has returns **200, not an error** — the operation is idempotent and the caller should not have to care.
- An unknown note id returns 404.
- An empty or whitespace name returns 422.

## Files This Story Owns

- `app/tags/routes_attach.py`
- `tests/test_tags_attach.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E3-S1`.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Responses are bare objects; no envelope (`docs/architecture.md` §4.2).
- Errors use FastAPI's `{"detail": ...}` shape (§4.3).

## Out of Scope

The other tag endpoints. Tag rename or merge.

## Test Notes

- Idempotent attach returns 200 and does not duplicate.
- Unknown note returns 404, not 500.
- `Work` and `work` attach to the same tag.
