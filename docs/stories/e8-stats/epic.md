# Epic E8: Statistics

- ID: E8
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e8-stats/` (3)

## Goal

Visibility into what is stored. Read-only, owns no table, depends on nothing but the stores — the easiest epic to run in parallel with anything.

## Scope

Aggregate queries and two endpoints.

## Dependencies

`E2-S1`, and `E3-S1` for tag statistics.

## Traceability

`docs/prd.md` §2.1 (the operator).

## Stories

- [Story 1 — Statistics queries](./story-1-stats-store.md) — `E8-S1`
- [Story 2 — Statistics endpoint](./story-2-stats-endpoint.md) — `E8-S2`
- [Story 3 — Activity endpoint](./story-3-activity-endpoint.md) — `E8-S3`
