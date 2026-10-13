# Story 3 — List tags and notes by tag

ID: E3-S3
Epic: `docs/stories/e3-tags/epic.md`
Status: Draft

## User Story

As an API consumer, I can see every tag in use and fetch the notes under one, so that tags are useful for finding things.

## Description

`GET /tags` and `GET /tags/{name}/notes`. The read half of tags, in its own file so it can be built alongside `E3-S2`.

## Acceptance Criteria

- `GET /tags` returns an array of `{name, count}`, alphabetical by name.
- A tag carried by no notes does not appear.
- `GET /tags/{name}/notes` returns a bare array of notes, newest first, paged with the same `limit`/`offset` rules as `GET /notes`.
- An unknown tag returns `[]` with status 200 — asking about a tag nobody has used is not an error.
- Lookup is case-insensitive: `/tags/Work/notes` finds notes tagged `work`.

## Files This Story Owns

- `app/tags/routes_read.py`
- `tests/test_tags_read.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E3-S1`.

## Non-Functional

- Paging rules identical to `E2-S3`; two different paging behaviours in one API is a defect even if both work.

## Out of Scope

Writing tags (`E3-S2`). Tag rename or merge.

## Test Notes

- Counts are right after attach and detach.
- An unknown tag returns `[]` rather than 404.
- Case-insensitive lookup works.
