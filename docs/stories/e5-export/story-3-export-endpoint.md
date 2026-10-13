# Story 3 — Export endpoint

ID: E5-S3
Epic: `docs/stories/e5-export/epic.md`
Status: Draft

## User Story

As an API consumer, I can download my notes in either format, optionally limited to one tag, so that I can take what I need.

## Description

`GET /export?format=json|markdown&tag=`, wiring the two formatters to the notes and tags stores.

## Acceptance Criteria

- `GET /export?format=json` returns the JSON payload with content type `application/json`.
- `GET /export?format=markdown` returns the document with content type `text/markdown`.
- `format` defaults to `json` when omitted.
- An unknown `format` returns 422 naming the accepted values.
- `tag=work` restricts the export to notes carrying that tag, matched case-insensitively.
- An unknown tag exports zero notes with status 200, not 404.

## Files This Story Owns

- `app/export/router.py`
- `tests/test_export_router.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E5-S1`, `E5-S2`, and `E3-S1` for the tag filter.

## Non-Functional

- Content types are set explicitly; a Markdown export served as JSON is a defect.
- Export reads; it never writes.

## Out of Scope

Streaming or chunked export. Scheduled or emailed exports. Import.

## Test Notes

- Both formats return the right content type.
- Default format is JSON.
- An unknown format returns 422 and names the accepted values.
- The tag filter restricts results, and an unknown tag yields an empty export rather than a 404.
