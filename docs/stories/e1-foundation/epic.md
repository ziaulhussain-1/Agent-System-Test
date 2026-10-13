# Epic E1: Foundation

- ID: E1
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e1-foundation/` (5)

## Goal

Everything the other epics stand on: an app that starts, a database that bootstraps itself by discovery, and test fixtures every later story reuses.

## Scope

Application factory, router discovery, connection and schema discovery, health, request logging, shared fixtures. No product features.

## Dependencies

None. **E1 runs alone** — its stories are mostly sequential and there is nothing to parallelise against yet.

## Traceability

`docs/architecture.md` §1, §3, §5.

## Stories

- [Story 1 — Application skeleton and router discovery](./story-1-app-skeleton.md) — `E1-S1`
- [Story 2 — Database connection and schema discovery](./story-2-database.md) — `E1-S2`
- [Story 3 — Health endpoint](./story-3-health.md) — `E1-S3`
- [Story 4 — Correlation id and structured logging](./story-4-correlation-id.md) — `E1-S4`
- [Story 5 — Shared test fixtures](./story-5-test-fixtures.md) — `E1-S5`
