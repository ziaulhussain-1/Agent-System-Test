# Story 1 — JSON export

ID: E5-S1
Epic: `docs/stories/e5-export/epic.md`
Status: Draft

## User Story

As an API consumer, I can get my notes as JSON, so that another tool or person can read them.

## Description

A pure function turning a list of notes into the JSON export payload. No HTTP, no database — it takes notes and returns a structure, which makes it impossible to couple to anything.

## Acceptance Criteria

- Carries every note with id, title, body and both timestamps.
- Timestamps are ISO 8601 strings, not raw floats — an export is read by other tools and by people.
- Records the export time and the note count.
- An empty list exports successfully with a count of zero.

## Files This Story Owns

- `app/export/__init__.py`
- `app/export/json_export.py`
- `tests/test_export_json.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1` (for the note shape).

## Non-Functional

- A pure function: no database, no HTTP, and the export time is injectable so tests do not depend on the wall clock (`docs/prd.md` §4).

## Out of Scope

The endpoint (`E5-S4`). The other formats.

## Test Notes

- Every field of every note survives the round trip.
- Empty input exports cleanly.
- Timestamps are ISO strings.
