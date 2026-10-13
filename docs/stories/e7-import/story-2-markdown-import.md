# Story 2 — Markdown import parser

ID: E7-S2
Epic: `docs/stories/e7-import/epic.md`
Status: Draft

## User Story

As a person, I can bring in a Markdown document and get one note per section, so that notes written elsewhere can be loaded.

## Description

A pure function splitting a Markdown document into note candidates, one per top-level heading.

The inverse of `E5-S2`, and it inherits the same difficulty: a body containing its own `#` headings must not be split into extra notes.

## Acceptance Criteria

- Each top-level heading starts a new note; its text becomes the title.
- Content before the first heading is reported as a problem, not silently lost.
- Headings *inside* a note's body do not split it further.
- A document with no headings is reported as a problem.
- An empty document yields no candidates and no crash.

## Files This Story Owns

- `app/import_notes/markdown_import.py`
- `tests/test_import_markdown.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E5-S2` (the document shape it must read).

## Non-Functional

- A pure function.
- Never raises on malformed input.

## Out of Scope

The HTTP layer. JSON import. Front-matter or metadata parsing.

## Test Notes

- A document exported by `E5-S2` round-trips to the same notes.
- A body containing `## Sub` does not become a second note.
- Content before the first heading is reported.
