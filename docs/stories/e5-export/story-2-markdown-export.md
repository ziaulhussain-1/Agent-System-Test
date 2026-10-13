# Story 2 — Markdown export

ID: E5-S2
Epic: `docs/stories/e5-export/epic.md`
Status: Draft

## User Story

As a person, I can get my notes as one readable Markdown document, so that I can keep or print them.

## Description

A pure function turning a list of notes into a single Markdown document, one section per note.

The thing to get right: a note's body may itself contain Markdown, including headings. Without care, a body starting `# Shopping` becomes a top-level heading and the document's structure collapses.

## Acceptance Criteria

- Each note becomes a section with its title as a heading.
- Each section shows when the note was created and last updated.
- A body containing `#` headings does not break the document's structure.
- An empty list produces a valid document saying there is nothing to export, not an empty string.
- Output ends with exactly one trailing newline.

## Files This Story Owns

- `app/export/markdown_export.py`
- `tests/test_export_markdown.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1` (for the note shape).

## Non-Functional

- A pure function, as in `E5-S1`.
- Deterministic: the same notes always produce byte-identical output, or the tests cannot assert on it.

## Out of Scope

The endpoint (`E5-S3`). JSON (`E5-S1`). Any rendering to HTML or PDF.

## Test Notes

- A note whose body contains `# Heading` does not corrupt the structure — the test that justifies whatever escaping or nesting is chosen.
- Empty input produces a valid document.
- Output is byte-identical across runs.
