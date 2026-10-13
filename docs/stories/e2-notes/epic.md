# Epic E2: Notes

- ID: E2
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e2-notes/` (6)

## Goal

The core resource. Everything else in the product reads notes, so this epic gates the other six.

## Scope

The notes table and model, and five endpoints — each in its own module so five machines could in principle build them at once.

## Dependencies

`E1` complete. `E2-S1` gates everything else in the project and goes out alone.

## Traceability

`docs/prd.md` §2.2; `docs/architecture.md` §4.2, §4.3, §5.

## Stories

- [Story 1 — Note model, schema and store](./story-1-note-store.md) — `E2-S1`
- [Story 2 — Create a note](./story-2-create.md) — `E2-S2`
- [Story 3 — Fetch one note](./story-3-get.md) — `E2-S3`
- [Story 4 — List notes with paging](./story-4-list.md) — `E2-S4`
- [Story 5 — Update a note](./story-5-update.md) — `E2-S5`
- [Story 6 — Delete a note](./story-6-delete.md) — `E2-S6`
