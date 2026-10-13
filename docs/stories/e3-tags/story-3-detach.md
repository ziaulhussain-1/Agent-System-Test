# Story 3 — Detach a tag

ID: E3-S3
Epic: `docs/stories/e3-tags/epic.md`
Status: Draft

## User Story

As an API consumer, I can detach a tag over HTTP, so that tags are useful for organising and finding notes.

## Description

`DELETE /notes/{id}/tags/{name}`, in its own module so the four tag endpoints can be built concurrently.

## Acceptance Criteria

- Returns **204** with no body.
- Detaching a tag the note does not have returns 404.
- Matching is case-insensitive: attaching `Work` then detaching `work` succeeds.
- A tag left on no notes disappears from `GET /tags`.

## Files This Story Owns

- `app/tags/routes_detach.py`
- `tests/test_tags_detach.py`

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

- 204 on success; 404 when the link does not exist.
- Case-insensitive detach works.
- The orphaned tag is gone from the list.
