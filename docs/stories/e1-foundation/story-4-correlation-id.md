# Story 4 — Correlation id and structured logging

ID: E1-S4
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As an operator, I can follow one request through the logs, so that I can tell which of three machines produced which line.

## Description

Middleware assigning each request a correlation id, returning it as `X-Request-ID`, and logging one structured line per request.

**Declared exception to file ownership:** registering middleware needs one line in `app/main.py`, owned by `E1-S1`. This story runs after E1-S1 and never beside it. Written down here rather than discovered in a merge conflict.

## Acceptance Criteria

- Every response carries `X-Request-ID`.
- A caller-supplied `X-Request-ID` is preserved rather than replaced.
- Exactly one structured line per request: method, path, status, duration, id.
- Note titles and bodies never appear in a log line.

## Files This Story Owns

- `app/middleware.py`
- `tests/test_middleware.py`
- `app/main.py` — **one line only** (declared exception)

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1-S1`. Must not run concurrently with it.

## Non-Functional

- Structured logging, not free text.
- No note content in logs.

## Out of Scope

Log shipping, metrics, tracing backends.

## Test Notes

- Header present; supplied id preserved.
- One line per request with every field.
- A request body containing a distinctive string: it does not appear in the logs.
