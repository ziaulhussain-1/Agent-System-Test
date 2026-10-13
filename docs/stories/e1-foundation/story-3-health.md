# Story 3 — Health endpoint

ID: E1-S3
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As an operator, I can call one endpoint to learn whether the service and its database are working, so that I am not guessing from logs.

## Description

A `GET /health` returning service status and whether the database answers a trivial query. The first consumer of router discovery, and therefore the proof that it works.

## Acceptance Criteria

- Given the database is reachable, when `GET /health` is called, then it returns 200 with status `ok` and a database field of `ok`.
- Given the database cannot be reached, then it returns 503 with the database field reporting the failure — and no exception text, path or SQL fragment.
- The endpoint takes no parameters and needs no authentication.

## Files This Story Owns

- `app/health/__init__.py`
- `app/health/router.py`
- `tests/test_health.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1-S1`, `E1-S2`.

## Non-Functional

- Answers well under a second; it is polled.
- Never leaks internals on failure (`docs/prd.md` §4).

## Out of Scope

No dependency checks beyond the database. No metrics endpoint.

## Test Notes

- Healthy case returns 200 and the expected shape.
- A broken connection returns 503 and the body contains no path, no SQL and no traceback.
