# Story 1 — Tag model, schema and store

ID: E3-S1
Epic: `docs/stories/e3-tags/epic.md`
Status: Draft

## User Story

As a developer agent, I can attach tags to notes through one module, so that the join table has exactly one owner.

## Description

The `tags` and `note_tags` tables and every statement touching them. Names are normalised — trimmed and lowercased — so `Work`, `work` and ` work ` are one tag rather than three. Deciding this once, here, is the difference between a clean tag list and a mess no later story can fix.

## Acceptance Criteria

- `attach(note_id, name)` creates the tag if new, links it, and is idempotent.
- `detach(note_id, name)` removes the link and reports whether one went.
- `list_tags()` returns tags in use with a count of notes carrying each.
- `notes_for(name, limit, offset)` returns notes carrying the tag, newest first.
- Names are trimmed and lowercased; an empty name is rejected.
- A tag with no notes left does not appear in `list_tags()`.
- Deleting a note removes its links (cascade).

## Files This Story Owns

- `app/tags/__init__.py`
- `app/tags/models.py`
- `app/tags/store.py`
- `app/tags/schema.sql`
- `tests/test_tags_store.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1`.

## Non-Functional

- Parameterised SQL only.
- Attaching to a missing note is a reported error, not a silent orphan row.

## Out of Scope

Any HTTP layer. Renaming or merging tags.

## Test Notes

- `Work`, `work` and ` work ` resolve to one tag.
- Attaching twice yields one link.
- Counts match reality after attach and detach.
- The cascade works.
