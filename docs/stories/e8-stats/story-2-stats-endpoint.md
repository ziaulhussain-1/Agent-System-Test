# Story 2 — Statistics endpoint

ID: E8-S2
Epic: `docs/stories/e8-stats/epic.md`
Status: Draft

## User Story

As an operator, I can read statistics endpoint over HTTP, so that I can see usage without a database client.

## Description

`GET /stats`, in its own module.

## Acceptance Criteria

- Returns note count, tag count and the most recent note time.
- An empty database returns zeroes with 200, not 404.

## Files This Story Owns

- `app/stats/routes_stats-endpoint.py`
- `tests/test_stats_stats-endpoint.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E8-S1`.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Responses are bare objects; no envelope (`docs/architecture.md` §4.2).
- Errors use FastAPI's `{"detail": ...}` shape (§4.3).

## Out of Scope

The other stats endpoints. Charts or dashboards.

## Test Notes

- Shape is stable and documented.
- Empty database returns zeroes.
