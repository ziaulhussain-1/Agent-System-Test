# Story 2 — Search endpoint

ID: E4-S2
Epic: `docs/stories/e4-search/epic.md`
Status: Draft

## User Story

As an API consumer, I can search my notes over HTTP, so that I can find one without paging through all of them.

## Description

`GET /search?q=&limit=&offset=`, returning a bare array of notes.

## Acceptance Criteria

- `GET /search?q=foo` returns 200 and a bare array.
- A missing `q` returns 422.
- An empty or whitespace-only `q` returns **422, not an empty array** — asking for nothing is a client mistake, and silently returning everything or nothing hides it.
- A query matching nothing returns `[]` with 200.
- `limit` defaults to 20, caps at 100, over-cap is clamped not rejected.
- Negative `limit` or `offset` returns 422.
- Ordering is deterministic (newest first, id descending as tiebreak) or paging repeats rows across pages.

## Files This Story Owns

- `app/search/router.py`
- `tests/test_search.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E4-S1`.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Responses are bare objects; no envelope (`docs/architecture.md` §4.2).
- Errors use FastAPI's `{"detail": ...}` shape (§4.3).

## Out of Scope

Ranking or highlighting (`E4-S3`). Searching tags.

## Test Notes

- Missing, empty and whitespace `q` all return 422.
- A match returns the note; a non-match returns `[]`.
