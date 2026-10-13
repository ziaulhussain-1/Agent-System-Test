# Story 2 — Markdown export

ID: E5-S2
Epic: `docs/stories/e5-export/epic.md`
Status: Draft

## User Story

As an API consumer, I can get my notes as Markdown, so that another tool or person can read them.

## Description

A pure function turning notes into one Markdown document, a section per note.

The thing to get right: a note's body may itself contain Markdown, including headings. Without care, a body starting `# Shopping` becomes a top-level heading and the document's structure collapses.

## Acceptance Criteria

- Each note becomes a section with its title as a heading.
- Each section shows created and updated times.
- A body containing `#` headings does not break the structure.
- An empty list produces a valid document saying there is nothing to export, not an empty string.
- Output ends with exactly one trailing newline.

## Files This Story Owns

- `app/export/markdown_export.py`
- `tests/test_export_markdown.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1` (for the note shape), and `E5-S1` for the package file only — this story does not use its code.

## Non-Functional

- A pure function: no database, no HTTP, and the export time is injectable so tests do not depend on the wall clock (`docs/prd.md` §4).

## Out of Scope

The endpoint (`E5-S4`). The other formats.

## Test Notes

- A body containing `# Heading` does not corrupt the document — the test that justifies whatever escaping is chosen.
- Empty input produces a valid document.
- Output is byte-identical across runs.
