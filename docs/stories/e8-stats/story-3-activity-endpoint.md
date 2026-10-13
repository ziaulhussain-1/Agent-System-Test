# Story 3 — Activity endpoint

ID: E8-S3
Epic: `docs/stories/e8-stats/epic.md`
Status: Draft

## User Story

As an operator, I can read activity endpoint over HTTP, so that I can see usage without a database client.

## Description

`GET /stats/activity`, in its own module.

## Acceptance Criteria

- `?days=` returns a count per day, defaulting to 30, capped at 365.
- Days with no notes appear with a count of zero.
- `days=0` or a negative value returns 422.

## Files This Story Owns

- `app/stats/routes_activity-endpoint.py`
- `tests/test_stats_activity-endpoint.py`

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

- Every day in the range is present, including empty ones.
- Over-cap is clamped; zero and negative return 422.
