# Epic E7: Import

- ID: E7
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e7-import/` (4)

## Goal

Bringing data in. The inverse of E5, and deliberately built the same way: pure parsers that take text and return candidates, with one endpoint joining them.

## Scope

JSON and Markdown parsers, an import endpoint and a dry-run preview.

## Dependencies

`E2-S1`; the parsers also depend on the export shapes from `E5-S1` and `E5-S2`.

## Traceability

`docs/prd.md` §2.2 (Export, read in reverse).

## Stories

- [Story 1 — JSON import parser](./story-1-json-import.md) — `E7-S1`
- [Story 2 — Markdown import parser](./story-2-markdown-import.md) — `E7-S2`
- [Story 3 — Import endpoint](./story-3-import-endpoint.md) — `E7-S3`
- [Story 4 — Import dry run](./story-4-import-dry-run.md) — `E7-S4`
