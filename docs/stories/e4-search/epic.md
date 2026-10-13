# Epic E4: Search

- ID: E4
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e4-search/` (3)

## Goal

Finding notes by their text. Reads the notes table and owns nothing in it, so it runs alongside E3 and E5 through E8 without contention.

## Scope

A case-insensitive substring query, the endpoint exposing it, and match snippets.

## Dependencies

`E2-S1`.

## Traceability

`docs/prd.md` §2.2; `docs/architecture.md` §4.4.

## Stories

- [Story 1 — Search query](./story-1-search-store.md) — `E4-S1`
- [Story 2 — Search endpoint](./story-2-search-endpoint.md) — `E4-S2`
- [Story 3 — Match snippets](./story-3-snippets.md) — `E4-S3`
