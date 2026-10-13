# Epic E3: Tags

- ID: E3
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e3-tags/` (5)

## Goal

Labelling and retrieval by label. Owns `tags` and `note_tags` entirely — the notes epic never reads them.

## Scope

Tag model, schema and store, plus four endpoints each in its own module.

## Dependencies

`E2-S1`. Independent of E4 through E8, so it runs alongside them.

## Traceability

`docs/prd.md` §2.2; `docs/architecture.md` §5.

## Stories

- [Story 1 — Tag model, schema and store](./story-1-tag-store.md) — `E3-S1`
- [Story 2 — Attach a tag](./story-2-attach.md) — `E3-S2`
- [Story 3 — Detach a tag](./story-3-detach.md) — `E3-S3`
- [Story 4 — List all tags](./story-4-list-tags.md) — `E3-S4`
- [Story 5 — List notes under a tag](./story-5-notes-by-tag.md) — `E3-S5`
