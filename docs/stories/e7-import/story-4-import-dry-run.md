# Story 4 — Import dry run

ID: E7-S4
Epic: `docs/stories/e7-import/epic.md`
Status: Draft

## User Story

As an API consumer, I can check what an import would do before it does it, so that I am not guessing with my own data.

## Description

`POST /import/preview?format=` — the same parsing and validation as `E7-S3`, reporting what would happen, writing nothing.

## Acceptance Criteria

- Returns the same counts and problems as a real import would.
- **Writes nothing.** The database is byte-identical afterwards.
- Accepts the same formats and returns the same 422s as `E7-S3`.

## Files This Story Owns

- `app/import_notes/routes_preview.py`
- `tests/test_import_preview.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E7-S1`, `E7-S2`.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Responses are bare objects; no envelope (`docs/architecture.md` §4.2).
- Errors use FastAPI's `{"detail": ...}` shape (§4.3).

## Out of Scope

Actually importing. Saving a preview for later execution.

## Test Notes

- Counts match what a real import produces for the same payload.
- The note count is unchanged afterwards — the test that proves 'writes nothing'.
