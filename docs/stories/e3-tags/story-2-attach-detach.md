# Story 2 — Attach and detach a tag

ID: E3-S2
Epic: `docs/stories/e3-tags/epic.md`
Status: Draft

## User Story

As an API consumer, I can tag and untag a note over HTTP, so that I can organise what I have stored.

## Description

`POST /notes/{id}/tags` and `DELETE /notes/{id}/tags/{name}`. The write half of tags; reads are `E3-S3` in a separate file so the two can run at once.

## Acceptance Criteria

- `POST /notes/{id}/tags` with `{"name": "work"}` returns 201 and the note's tags.
- Attaching a tag the note already has returns 200, not an error — the operation is idempotent and the caller should not have to care.
- `POST` to an unknown note id returns 404.
- `DELETE /notes/{id}/tags/{name}` returns 204.
- Detaching a tag the note does not have returns 404.
- An empty or whitespace name returns 422.

## Files This Story Owns

- `app/tags/routes_write.py`
- `tests/test_tags_write.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E3-S1`.

## Non-Functional

- Errors carry no SQL, path or traceback.

## Out of Scope

Reading tags (`E3-S3`). Bulk tagging.

## Test Notes

- Idempotent attach returns 200 and does not duplicate.
- Unknown note and unknown tag cases return 404 rather than 500.
- Name normalisation is visible through the API: attaching `Work` then detaching `work` succeeds.
