# Story 4 — Export endpoint

ID: E5-S4
Epic: `docs/stories/e5-export/epic.md`
Status: Draft

## User Story

As an API consumer, I can download my notes in any supported format, optionally limited to one tag, so that I can take what I need.

## Description

`GET /export?format=json|markdown|csv&tag=`, wiring the three formatters to the notes and tags stores.

## Acceptance Criteria

- Each format returns its own content type: `application/json`, `text/markdown`, `text/csv`.
- `format` defaults to `json` when omitted.
- An unknown `format` returns 422 naming the accepted values.
- `tag=work` restricts the export, matched case-insensitively.
- An unknown tag exports zero notes with 200, not 404.

## Files This Story Owns

- `app/export/router.py`
- `tests/test_export_router.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E5-S1`, `E5-S2`, `E5-S3`, and `E3-S1` for the tag filter.

## Non-Functional

- Errors carry no SQL, path or traceback.
- Responses are bare objects; no envelope (`docs/architecture.md` §4.2).
- Errors use FastAPI's `{"detail": ...}` shape (§4.3).
- Content types are set explicitly; Markdown served as JSON is a defect.
- Export reads; it never writes.

## Out of Scope

Streaming or chunked export. Scheduled or emailed exports. Import (`E7`).

## Test Notes

- All three formats return the right content type.
- Default is JSON.
- Unknown format returns 422 naming the accepted values.
- The tag filter restricts; an unknown tag yields an empty export, not a 404.
