# Epic E5: Export

- ID: E5
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e5-export/`

## Goal

Getting data out. The most self-contained epic: two pure formatters and one endpoint, reading notes and tags and owning neither.

## Scope

A JSON formatter, a Markdown formatter, and the endpoint that serves both with an optional tag filter.

## Dependencies

`E2-S1`. `E5-S3` depends on both formatters; `E5-S1` and `E5-S2` are independent of each other and run in parallel.

## Traceability

`docs/prd.md` §2.2 (Export).

## Stories

- [Story 1 — JSON export](./story-1-json-export.md) — `E5-S1`
- [Story 2 — Markdown export](./story-2-markdown-export.md) — `E5-S2`
- [Story 3 — Export endpoint](./story-3-export-endpoint.md) — `E5-S3`
