# Story 1 — Application skeleton and router discovery

ID: E1-S1
Epic: `docs/stories/e1-foundation/epic.md`
Status: Draft

## User Story

As a developer agent, I can add a feature by creating a folder, so that no two stories ever have to edit the same registration file.

## Description

Create the FastAPI application factory. It must find and mount every `app/<area>/router*.py` by walking the `app/` package at startup, rather than importing each one by name.

This is the most important file in the project for the parallel-work goal: a hand-maintained list of routers would be a file every later story has to edit, which is the merge point the whole architecture exists to avoid (`docs/architecture.md` §2).

## Acceptance Criteria

- Given the app starts, when a module `app/<area>/router*.py` exposes `router = APIRouter()`, then its routes are served without any other file being edited.
- Given a folder with no router module, when the app starts, then it is skipped and startup still succeeds.
- Given a router module that raises on import, when the app starts, then startup fails loudly naming the module — a feature that silently fails to mount is worse than one that refuses to start.
- `GET /docs` serves the generated OpenAPI page.

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

- Pin every dependency in `requirements.txt`; "latest" lets three machines install three different things on the same afternoon.
- `.gitignore` covers `notes.db`, `__pycache__/`, `.venv/`.
- The app starts with one documented command.

## Out of Scope

No endpoints beyond what FastAPI provides. No database (`E1-S2`). No middleware (`E1-S4`).

## Test Notes

- A temporary package with a dummy router is discovered and mounted.
- A folder without a router module does not break startup.
- A deliberately broken module makes startup raise, and the message names it.
