# Story 1 — Statistics queries

ID: E8-S1
Epic: `docs/stories/e8-stats/epic.md`
Status: Draft

## User Story

As an operator, I can see how much is stored, so that I know whether the service is being used.

## Description

Aggregate queries over notes and tags, in their own module. Reads only; owns no table.

## Acceptance Criteria

- `totals()` returns note count, tag count and the time of the most recent note.
- `notes_per_day(days)` returns a count per day for the last N days, including days with zero — a gap in a chart is a different claim from a zero.
- `top_tags(n)` returns the n most-used tags with counts.
- An empty database returns zeroes, not an error.

## Files This Story Owns

- `app/stats/__init__.py`
- `app/stats/store.py`
- `tests/test_stats_store.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1`; `top_tags` also needs `E3-S1`.

## Non-Functional

- Read-only; no writes, no schema.
- Aggregates are computed in SQL, not by loading every note into memory.

## Out of Scope

Any HTTP layer. Charts. Retention or historical snapshots.

## Test Notes

- Counts are right after adding and deleting notes.
- A day with no notes appears as zero, not as a missing key.
- An empty database returns zeroes.
