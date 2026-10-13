# Story 1 — Application skeleton and router discovery

ID: E1-S1
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As a developer agent, I can add an endpoint by creating a module, so that no two stories ever edit the same registration file.

## Description

The FastAPI application factory. It walks `app/` at startup and mounts every module matching `app/<area>/routes_*.py` or `app/<area>/router.py` that exposes `router = APIRouter()`.

This is the most important file in the project for the parallel-work goal. A hand-maintained list of routers would be a file every later story edits — the merge point the architecture exists to avoid (`docs/architecture.md` §2). With discovery, 20 endpoint stories touch 20 different files.

## Acceptance Criteria

- A module exposing `router` under `app/<area>/` is served without any other file being edited.
- A folder with no router module is skipped; startup still succeeds.
- A router module that raises on import makes startup fail loudly, naming the module — silently failing to mount is worse than refusing to start.
- `GET /docs` serves the OpenAPI page.

## Files This Story Owns

- `app/__init__.py`
- `app/main.py`
- `tests/test_app.py`
- `requirements.txt`
- `.gitignore`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

Nothing. This story is first.

## Non-Functional

- Pin every dependency; "latest" lets three machines install three different things on one afternoon.
- `.gitignore` covers `notes.db`, `__pycache__/`, `.venv/`.

## Out of Scope

Database (`E1-S2`), middleware (`E1-S4`), test fixtures (`E1-S5`).

## Test Notes

- A dummy router in a temp package is discovered and mounted.
- A folder without a router module does not break startup.
- A broken module makes startup raise, and the message names it.
