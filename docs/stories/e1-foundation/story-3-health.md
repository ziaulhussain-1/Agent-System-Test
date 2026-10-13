# Story 3 — Health endpoint

ID: E1-S3
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As an operator, I can call one endpoint to learn whether the service and its database work, so that I am not guessing from logs.

## Description

`GET /health`, reporting service status and whether the database answers a trivial query. The first consumer of router discovery, and the proof it works.

## Acceptance Criteria

- Database reachable: 200, status `ok`, database `ok`.
- Database unreachable: 503, the database field reports failure — with no exception text, path or SQL fragment.
- No parameters, no authentication.

## Files This Story Owns

- `app/health/__init__.py`
- `app/health/router.py`
- `tests/test_health.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1-S1`, `E1-S2`.

## Non-Functional

- Answers well under a second; it is polled.
- Never leaks internals.

## Out of Scope

Dependency checks beyond the database. Metrics.

## Test Notes

- Healthy case returns 200 and the expected shape.
- A broken connection returns 503 with no path, SQL or traceback in the body.
