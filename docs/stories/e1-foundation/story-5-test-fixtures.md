# Story 5 — Shared test fixtures

ID: E1-S5
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As a developer agent, I can get an isolated database and a test client from a fixture, so that every test file does not invent its own.

## Description

`tests/conftest.py`: a fixture giving each test file its own in-memory SQLite with the discovered schema applied, and a FastAPI `TestClient` bound to it.

Three machines run this suite at the same time. Shared state between test files would make one machine's run fail because of another's, and the failure would look like a flaky test rather than a collision (`docs/architecture.md` §4.6).

## Acceptance Criteria

- Each test gets a fresh in-memory database; nothing leaks between tests.
- The schema is applied by the same discovery path the app uses, so tests cannot pass against a schema production does not have.
- A `client` fixture returns a `TestClient` bound to that database.
- No test touches `./notes.db`.

## Files This Story Owns

- `tests/conftest.py`
- `tests/test_fixtures.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E1-S1`, `E1-S2`.

## Non-Functional

- No network, no wall-clock dependence (`docs/prd.md` §4).
- Fixtures are function-scoped unless a test says otherwise.

## Out of Scope

Factories or fake data generators. Those belong with the features that need them.

## Test Notes

- Two tests in one file get independent databases.
- The client fixture reaches a discovered route.
- The real `notes.db` is never created by the suite.
