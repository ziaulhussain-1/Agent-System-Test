# Epic E2: Notes

- ID: E2
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e2-notes/`

## Goal

The core resource. Everything else in the product reads notes, so this epic gates the other three.

## Scope

The note model, its persistence, and the five endpoints: create, fetch, list, update, delete.

## Dependencies

`E1` complete. `E2-S1` gates `E2-S2`, `E2-S3` and all of E3, E4 and E5 — it goes out in a wave of its own.

## Traceability

`docs/prd.md` §2.2 (Notes); `docs/architecture.md` §4.2 (bare objects), §4.3 (error shape), §5 (data model).

## Stories

- [Story 1 — Note model and store](./story-1-note-store.md) — `E2-S1`
- [Story 2 — Create, update and delete a note](./story-2-write-endpoints.md) — `E2-S2`
- [Story 3 — Fetch a note and list notes](./story-3-read-endpoints.md) — `E2-S3`
