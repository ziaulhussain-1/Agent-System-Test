# Story 1 — Tag model and store

ID: E3-S1
Epic: `docs/stories/e3-tags/epic.md`
Status: Draft

## User Story

As a developer agent, I can attach tags to notes through one module, so that the join table has exactly one owner.

## Description

The tag model and every statement touching `tags` and `note_tags`. Tag names are normalised — trimmed and lowercased — so that `Work`, `work` and ` work ` are one tag rather than three. Deciding this here, once, is the difference between a clean tag list and a mess no later story can fix.

## Acceptance Criteria

- `attach(note_id, name)` creates the tag if new and links it, and is idempotent: attaching twice leaves one link.
- `detach(note_id, name)` removes the link and reports whether one went.
- `list_tags()` returns every tag in use with the number of notes carrying it.
- `notes_for(name, limit, offset)` returns notes carrying the tag, newest first.
- Names are trimmed and lowercased on the way in; an empty name is rejected.
- A tag with no notes left does not appear in `list_tags()`.

## Files This Story Owns

- `app/tags/__init__.py`
- `app/tags/models.py`
- `app/tags/store.py`
- `tests/test_tags_store.py`

A story may only create or change the files listed here. Needing another story's file means these two stories were split wrongly — say so in the pull request rather than editing around it.

## Depends On

`E2-S1`.

## Non-Functional

- Parameterised SQL only.
- Attaching a tag to a missing note is an error the store reports, not a silent orphan row.

## Out of Scope

No HTTP layer. No renaming or merging of tags.

## Test Notes

- `Work`, `work` and ` work ` all resolve to one tag.
- Attaching twice yields one link.
- Counts in `list_tags()` match reality after attach and detach.
- Deleting a note removes its links (the cascade from `E1-S2`).
