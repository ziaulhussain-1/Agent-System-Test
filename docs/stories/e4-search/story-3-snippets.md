# Story 3 — Match snippets

ID: E4-S3
Epic: `docs/stories/e4-search/epic.md`
Status: Draft

## User Story

As an API consumer, I can see where my search term appeared, so that I can pick the right note without opening each one.

## Description

A pure function producing a short extract around the first match in a note's body, with the matched text marked. Its own module, taking text and a query and returning a string — no database, no HTTP, trivially testable.

## Acceptance Criteria

- Returns an extract of at most N characters centred on the first match.
- The matched text is marked in a way the caller can find.
- A match at the very start or end does not produce a ragged or over-long extract.
- No match returns the opening of the body rather than an empty string.
- The function never splits a surrogate pair or mangles non-ASCII text.

## Files This Story Owns

- `app/search/snippet.py`
- `tests/test_search_snippet.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E4-S1` (for the match semantics only).

## Non-Functional

- A pure function: no database, no HTTP, no clock.
- Deterministic for the same input.

## Out of Scope

Highlighting in HTML. Ranking. Multiple snippets per note.

## Test Notes

- Match at start, middle and end of a long body.
- No match returns the opening.
- Non-ASCII text survives intact.
