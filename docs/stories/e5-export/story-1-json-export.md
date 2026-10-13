# Story 1 — JSON export

ID: E5-S1
Epic: `docs/stories/e5-export/epic.md`
Status: Draft

## User Story

As an API consumer, I can get my notes as JSON, so that another tool can read them.

## Description

A pure function turning a list of notes into the JSON export payload. No HTTP, no database — it takes notes and returns a structure, which makes it trivial to test and impossible to couple to anything.

## Acceptance Criteria

- Given a list of notes, the result carries every note with id, title, body and both timestamps.
- Timestamps are ISO 8601 strings, not raw floats — an export is read by other tools and by people.
- The payload records the export time and the number of notes.
- An empty list exports successfully with a count of zero, rather than failing.

## Files This Story Owns

- `app/export/__init__.py`
- `app/export/json_export.py`
- `tests/test_export_json.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1` (for the note shape).

## Non-Functional

- A pure function: no database access, no HTTP, no clock except the recorded export time, which is injectable so tests do not depend on wall-clock time (`docs/prd.md` §4).

## Out of Scope

The endpoint (`E5-S3`). Markdown (`E5-S2`).

## Test Notes

- Round trip: the exported structure contains every field of every note.
- Empty input exports cleanly.
- Timestamps are ISO strings.
