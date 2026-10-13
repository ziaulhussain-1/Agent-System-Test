# Epic E6: Archive

- ID: E6
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e6-archive/` (4)

## Goal

Recoverable removal. Owns its own table so that archiving never edits the notes schema or any notes endpoint.

## Scope

An archive store with its own schema, and three endpoints.

## Dependencies

`E2-S1`. Independent of E3, E4, E5, E7 and E8.

## Traceability

`docs/architecture.md` §2 (why a separate table, not a column).

## Stories

- [Story 1 — Archive store and schema](./story-1-archive-store.md) — `E6-S1`
- [Story 2 — Archive a note](./story-2-archive-endpoint.md) — `E6-S2`
- [Story 3 — Restore a note](./story-3-restore-endpoint.md) — `E6-S3`
- [Story 4 — List archived notes](./story-4-list-archived.md) — `E6-S4`
