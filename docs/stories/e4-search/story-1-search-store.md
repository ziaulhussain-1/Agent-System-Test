# Story 1 — Search query

ID: E4-S1
Epic: `docs/stories/e4-search/epic.md`
Status: Draft

## User Story

As a developer agent, I can run one query to find notes matching text, so that the endpoint has nothing to think about.

## Description

`search(q, limit, offset)` over `notes`, matching `title` or `body` case-insensitively. `LIKE`, not FTS5, and the reason is recorded in `docs/architecture.md` §4.4: FTS5 needs a second table kept in sync with notes on every write, which would couple this epic to the notes epic.

The one real trap: `%` and `_` are wildcards in `LIKE`. A user searching for `100%` must not match everything.

## Acceptance Criteria

- `search("foo")` returns notes whose title or body contains `foo`, in any case.
- Results are newest first, with the same ordering rule as `list`.
- `limit` and `offset` behave exactly as in the notes store.
- A query containing `%` or `_` matches those characters literally.
- A query matching nothing returns an empty list, not an error.

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

Ranking, stemming, fuzzy matching. The HTTP layer (`E4-S2`).

## Test Notes

- Case-insensitive matching in both title and body.
- A literal `%` search does not return everything — the test that justifies the escaping.
- Paging matches the notes store's behaviour.
