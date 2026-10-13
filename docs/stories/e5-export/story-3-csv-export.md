# Story 3 — CSV export

ID: E5-S3
Epic: `docs/stories/e5-export/epic.md`
Status: Draft

## User Story

As an API consumer, I can get my notes as CSV, so that another tool or person can read them.

## Description

A pure function turning notes into CSV, one row per note.

CSV looks trivial and is not: a body containing a comma, a quote or a newline must survive, and a title beginning `=` or `+` is a formula injection risk the moment someone opens the file in a spreadsheet.

## Acceptance Criteria

- Header row, then one row per note: id, title, body, created, updated.
- Commas, quotes and newlines inside a field are escaped per RFC 4180.
- A field starting `=`, `+`, `-` or `@` is neutralised so a spreadsheet does not execute it.
- An empty list produces a header row and nothing else.

## Files This Story Owns

- `app/export/csv_export.py`
- `tests/test_export_csv.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1` (for the note shape), and `E5-S1` for the package file only — this story does not use its code.

## Non-Functional

- A pure function: no database, no HTTP, and the export time is injectable so tests do not depend on the wall clock (`docs/prd.md` §4).

## Out of Scope

The endpoint (`E5-S4`). The other formats.

## Test Notes

- A body containing a comma, a quote and a newline round-trips through a CSV reader.
- A title starting `=cmd` is neutralised.
- Empty input yields just the header.
