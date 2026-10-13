# Epic E1: Foundation

- ID: E1
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e1-foundation/`

## Goal

Everything the other four epics stand on: an application that starts, a database that exists, and the discovery mechanism that lets a new feature be a new folder rather than an edit to a shared file.

## Scope

The application factory, router discovery, the SQLite connection and schema, a health endpoint and request logging. No product features.

## Dependencies

None. Every other epic depends on this one, so **E1 runs alone** — its stories are mostly sequential and there is nothing to parallelise against yet.

## Traceability

`docs/architecture.md` §1 (shape), §3 (request flow), §5 (data model).

## Stories

- [Story 1 — Application skeleton and router discovery](./story-1-app-skeleton.md) — `E1-S1`
- [Story 2 — Database connection and schema](./story-2-database.md) — `E1-S2`
- [Story 3 — Health endpoint](./story-3-health.md) — `E1-S3`
- [Story 4 — Correlation id and structured logging](./story-4-correlation-id.md) — `E1-S4`
