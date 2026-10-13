# Story 3 — Fetch a note and list notes

ID: E2-S3
Epic: `docs/stories/e2-notes/epic.md`
Status: Draft

## User Story

As an API consumer, I can fetch one note and page through all of them, so that I can read what I have stored.

## Description

The read half: `GET /notes/{id}` and `GET /notes?limit=&offset=`. A separate file from the write routes so this story and `E2-S2` can run concurrently.

## Acceptance Criteria

- `GET /notes/{id}` returns 200 and the bare note.
- `GET /notes/{id}` for an unknown id returns 404 `{"detail": "..."}`.
- `GET /notes` returns a JSON **array**, newest first, with no envelope.
- `limit` defaults to 20, caps at 100, and a value over the cap is clamped rather than rejected.
- A negative `limit` or `offset` returns 422.
- An empty database returns `[]` with status 200, not 404.

## Files This Story Owns

- `app/notes/routes_read.py`
- `tests/test_notes_read.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1`.

## Non-Functional

- Ordering is deterministic: newest first, id descending as the tiebreak, or paging repeats rows across pages.

## Out of Scope

Writing (`E2-S2`). Search (`E4`). Filtering by tag (`E3`).

## Test Notes

- Paging across a known set returns every note exactly once, with no duplicates at the page boundary.
- The cap is clamped, not rejected.
- An empty database returns `[]`.
