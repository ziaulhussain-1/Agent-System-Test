# Story 4 — List all tags

ID: E3-S4
Epic: `docs/stories/e3-tags/epic.md`
Status: Draft

## User Story

As an API consumer, I can list all tags over HTTP, so that tags are useful for organising and finding notes.

## Description

`GET /tags`, in its own module so the four tag endpoints can be built concurrently.

## Acceptance Criteria

- Returns an array of `{name, count}`, alphabetical by name.
- A tag carried by no notes does not appear.
- An empty database returns `[]` with 200.

## Files This Story Owns

- `app/tags/routes_list-tags.py`
- `tests/test_tags_list-tags.py`

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

- Counts are right after attach and detach.
- Alphabetical order.
- Empty database returns `[]`.
