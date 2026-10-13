# Epic E5: Export

- ID: E5
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e5-export/` (4)

## Goal

Getting data out. Three pure formatters and one endpoint, reading notes and tags and owning neither — the most self-contained epic in the project.

## Scope

JSON, Markdown and CSV formatters, and the endpoint serving all three with an optional tag filter.

## Dependencies

`E2-S1`. The three formatters are independent of each other and of everything else; `E5-S4` joins them.

## Traceability

`docs/prd.md` §2.2.

## Stories

- [Story 1 — JSON export](./story-1-json-export.md) — `E5-S1`
- [Story 2 — Markdown export](./story-2-markdown-export.md) — `E5-S2`
- [Story 3 — CSV export](./story-3-csv-export.md) — `E5-S3`
- [Story 4 — Export endpoint](./story-4-export-endpoint.md) — `E5-S4`
