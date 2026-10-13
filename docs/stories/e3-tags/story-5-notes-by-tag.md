# Story 5 — List notes under a tag

ID: E3-S5
Epic: `docs/stories/e3-tags/epic.md`
Status: Draft

## User Story

As an API consumer, I can list notes under a tag over HTTP, so that tags are useful for organising and finding notes.

## Description

`GET /tags/{name}/notes`, in its own module so the four tag endpoints can be built concurrently.

## Acceptance Criteria

- Returns a bare array of notes, newest first.
- An unknown tag returns `[]` with 200 — asking about a tag nobody used is not an error.
- Lookup is case-insensitive.
- `limit` defaults to 20, caps at 100, over-cap is clamped not rejected.
- Negative `limit` or `offset` returns 422.
- Ordering is deterministic (newest first, id descending as tiebreak) or paging repeats rows across pages.

## Files This Story Owns

- `app/tags/routes_notes-by-tag.py`
- `tests/test_tags_notes-by-tag.py`

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

- An unknown tag returns `[]` rather than 404.
- Case-insensitive lookup.
- Paging behaves exactly as `GET /notes` does; two paging behaviours in one API is a defect even if both work.
