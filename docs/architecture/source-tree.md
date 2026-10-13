# Source tree

```
app/
  main.py            application factory, router discovery, nothing feature-specific
  db.py              connection + schema bootstrap
  notes/             one folder per feature area
    router.py
    models.py
    store.py
  tags/
  search/
  export/
  health/
tests/
  test_notes.py      one test file per feature area, named for it
  test_tags.py
  ...
docs/                PRD, architecture, stories (BMAD)
```

## Why it is shaped this way

Grouped **by feature, not by layer**. A layered tree (`routers/`, `models/`,
`services/`) means a single story edits four files that three other stories
also edit, and every pull request conflicts. Grouped by feature, a story owns
a folder.

`main.py` discovers routers rather than importing them one by one. A
hand-maintained list of routers would be a file every new-endpoint story has
to edit — the exact merge point this layout exists to avoid.

## Rules

- A new feature area is a new folder plus its test file. Nothing else changes.
- If a change needs `main.py` or `db.py`, it is infrastructure work and belongs
  in its own story, not folded into a feature story.
