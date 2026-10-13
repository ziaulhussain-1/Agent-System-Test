# Story 1 — JSON import parser

ID: E7-S1
Epic: `docs/stories/e7-import/epic.md`
Status: Draft

## User Story

As an API consumer, I can bring notes in from a JSON export, so that data can move between instances.

## Description

A pure function turning an export payload into validated note candidates. No database, no HTTP: it takes a structure and returns notes plus a list of problems.

## Acceptance Criteria

- A valid payload yields one candidate per note.
- A note missing a title or body is reported as a problem rather than silently dropped or silently imported blank.
- Ids in the payload are **ignored** — importing must not overwrite an existing note by id collision.
- ISO timestamps are parsed; unparseable ones are reported, not guessed.
- A payload that is not an export at all is reported clearly.

## Files This Story Owns

- `app/import_notes/__init__.py`
- `app/import_notes/json_import.py`
- `tests/test_import_json.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E5-S1` (the payload shape it must read).

## Non-Functional

- A pure function; no database writes here.
- Never raises on bad input — it reports.

## Out of Scope

The HTTP layer (`E7-S3`). Markdown (`E7-S2`). Merge or conflict resolution.

## Test Notes

- A round trip from the E5-S1 export shape produces identical candidates.
- A note missing a title is reported, not dropped.
- Ids in the payload do not reach the candidate.
