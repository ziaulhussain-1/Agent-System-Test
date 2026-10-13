# Story 2 — Search endpoint

ID: E4-S2
Epic: `docs/stories/e4-search/epic.md`
Status: Draft

## User Story

As an API consumer, I can search my notes over HTTP, so that I can find one without paging through all of them.

## Description

`GET /search?q=&limit=&offset=`, returning a bare array of notes.

## Acceptance Criteria

- `GET /search?q=foo` returns 200 and a bare array of matching notes.
- A missing `q` returns 422.
- An empty or whitespace-only `q` returns **422, not an empty array** — asking for nothing is a client mistake, and silently returning everything or nothing hides it (`docs/prd.md` §2.2).
- `limit` and `offset` follow the same rules as `GET /notes`.
- A query matching nothing returns `[]` with status 200.

## Files This Story Owns

- `app/search/router.py`
- `tests/test_search.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E4-S1`.

## Non-Functional

- Paging rules identical to `E2-S3`.
- The query string never reaches the response unescaped.

## Out of Scope

Ranking or highlighting. Searching tags (that is `GET /tags/{name}/notes`).

## Test Notes

- Missing, empty and whitespace `q` all return 422.
- A match returns the note; a non-match returns `[]`.
- Paging across a known result set returns each note exactly once.
