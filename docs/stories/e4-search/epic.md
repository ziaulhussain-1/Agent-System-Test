# Epic E4: Search

- ID: E4
- Source: `docs/prd.md` → §2.2
- Stories: `docs/stories/e4-search/`

## Goal

Finding notes by their text. Reads the notes table and owns nothing in it, so it runs alongside E3 and E5 without contention.

## Scope

A case-insensitive substring query over titles and bodies, and the endpoint that exposes it with paging.

## Dependencies

`E2-S1` (the notes table must exist and be populated by tests).

## Traceability

`docs/prd.md` §2.2 (Search); `docs/architecture.md` §4.4 (why `LIKE`, not FTS5).

## Stories

- [Story 1 — Search query](./story-1-search-store.md) — `E4-S1`
- [Story 2 — Search endpoint](./story-2-search-endpoint.md) — `E4-S2`
