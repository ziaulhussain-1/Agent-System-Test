# Epic E3: Tags

- ID: E3
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e3-tags/`

## Goal

Labelling and retrieval by label. Owns the `tags` and `note_tags` tables entirely — the notes epic never reads them.

## Scope

The tag model and store, attaching and detaching tags, listing all tags with counts, and listing the notes carrying a tag.

## Dependencies

`E2-S1` (the notes table must exist). Independent of E4 and E5, so it runs alongside them.

## Traceability

`docs/prd.md` §2.2 (Tags); `docs/architecture.md` §5 (`note_tags` ownership).

## Stories

- [Story 1 — Tag model and store](./story-1-tag-store.md) — `E3-S1`
- [Story 2 — Attach and detach a tag](./story-2-attach-detach.md) — `E3-S2`
- [Story 3 — List tags and notes by tag](./story-3-tag-reads.md) — `E3-S3`
