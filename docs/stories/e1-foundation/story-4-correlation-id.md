# Story 4 — Correlation id and structured logging

ID: E1-S4
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As an operator, I can follow one request through the logs, so that I can tell which of three machines produced which line.

## Description

Middleware that assigns each request a correlation id, returns it as `X-Request-ID`, and logs one structured line per request: method, path, status, duration, id.

**Honest exception to the ownership rule:** registering middleware needs one line in `app/main.py`, which `E1-S1` owns. This story therefore runs after E1-S1 and never at the same time as it. It is written down here rather than discovered in a merge conflict.

## Acceptance Criteria

- Given any request, when it completes, then the response carries an `X-Request-ID` header.
- Given the caller already sent `X-Request-ID`, then that value is used rather than a new one.
- Given a request completes, then exactly one structured log line is emitted with method, path, status, duration and id.
- Note titles and bodies never appear in a log line.

## Files This Story Owns

- `app/middleware.py`
- `tests/test_middleware.py`
- `app/main.py` — **one line only**, to register the middleware (declared exception; see Description)

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1-S1`. Must not run concurrently with it.

## Non-Functional

- Logging is structured, not free text.
- No note content in logs (`docs/prd.md` §4).

## Out of Scope

No log shipping, metrics or tracing backend.

## Test Notes

- The header is present, and a supplied id is preserved.
- One line per request, carrying the required fields.
- A request whose body contains a distinctive string: that string does not appear in the captured logs.
