# Story 1 — Search query

ID: E4-S1
Epic: `docs/stories/e4-search/epic.md`
Status: Draft

## User Story

As a developer agent, I can run one query to find notes matching text, so that the endpoint has nothing to think about.

## Description

`search(q, limit, offset)` over `notes`, matching title or body case-insensitively. `LIKE`, not FTS5 — the reason is in `docs/architecture.md` §4.4: FTS5 needs a second table kept in sync on every write, coupling this epic to the notes epic.

The real trap: `%` and `_` are wildcards in `LIKE`. Someone searching for `100%` must not match everything.

## Acceptance Criteria

- Matches `foo` in title or body, in any case.
- Newest first, same ordering rule as `list`.
- `%` and `_` in the query match literally.
- A query matching nothing returns an empty list, not an error.
- `limit` defaults to 20, caps at 100, over-cap is clamped not rejected.
- Negative `limit` or `offset` returns 422.
- Ordering is deterministic (newest first, id descending as tiebreak) or paging repeats rows across pages.

## Files This Story Owns

- `app/search/__init__.py`
- `app/search/store.py`
- `tests/test_search_store.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1`.

## Non-Functional

- Parameterised SQL only — a search endpoint is the obvious injection target.
- No second table, no index to keep in sync.

## Out of Scope

Ranking, stemming, fuzzy matching. The HTTP layer.

## Test Notes

- Case-insensitive match in both title and body.
- A literal `%` search does not return everything — the test that justifies the escaping.
- Paging matches the notes store.
