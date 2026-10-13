# Story 3 — Import endpoint

ID: E7-S3
Epic: `docs/stories/e7-import/epic.md`
Status: Draft

## User Story

As an API consumer, I can upload an export and have it loaded, so that moving data takes one request.

## Description

`POST /import?format=json|markdown`, parsing with the right parser and writing accepted candidates through the notes store.

## Acceptance Criteria

- Returns 200 with counts: imported, skipped, and the problems found.
- Partial success is the normal case: good notes import, bad ones are reported, and the response says exactly which.
- An unknown `format` returns 422 naming the accepted values.
- An empty or unparseable body returns 422.
- Import never overwrites an existing note.

## Files This Story Owns

- `app/import_notes/router.py`
- `tests/test_import_router.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E7-S1`, `E7-S2`, `E2-S1`.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Responses are bare objects; no envelope (`docs/architecture.md` §4.2).
- Errors use FastAPI's `{"detail": ...}` shape (§4.3).

## Out of Scope

Dry run (`E7-S4`). Merge strategies. Import of tags.

## Test Notes

- A mixed payload imports the good notes and reports the bad ones.
- Nothing is overwritten.
- Unknown format returns 422.
