# Architecture — Notes API

- Status: **Complete.** Decisions settled 2026-10-13.
- Sharded to: `docs/architecture/` (see `.bmad-core/core-config.yaml`)
- Always loaded by dev agents: `coding-standards.md`, `tech-stack.md`,
  `source-tree.md`

## 1. Shape

A single FastAPI application over SQLite. One process, no external services,
no network at test time.

Chosen because every machine in this cluster already has Python and the Mesh
virtualenv. A stack that needs installing on three machines costs more than it
teaches, and a failed install on machine three is indistinguishable from a bug
until someone looks.

## 2. The constraint that drives the rest

Several machines develop this repository simultaneously, each in its own
checkout, each on its own branch, each opening its own pull request.

The architecture therefore optimises for something unusual: **minimising the
number of files any two stories both need to touch.**

- One module per feature area, not one module per layer
- One test file per feature area, named after it
- Routers registered by **discovery**, not a hand-edited list
- **No shared `models.py`, `schemas.py` or `utils.py`** — they become the file
  every story edits and therefore the file every pull request conflicts on
- A feature's request/response models live beside the feature

Where this trades against conventional structure, it wins here. The reason is
recorded so the next agent does not "fix" it.

## 3. Request flow

```
client → uvicorn → FastAPI app (main.py)
                     ├ correlation-id middleware     (adds X-Request-ID, logs)
                     └ router discovery → app/<area>/router.py
                                            → store.py → sqlite3 connection
```

`db.py` owns the connection and the schema bootstrap. A feature's `store.py`
owns its own SQL. No ORM: the data model is four tables and an ORM would add a
shared mapping file for every story to touch.

## 4. Decisions

Each records what was chosen, what else was considered, and why the
alternatives lost. A decision without its reasoning gets re-litigated by the
next agent that reads it.

### 4.1 No authentication in the MVP

**Chosen:** no auth of any kind.

**Considered:** a static API key in a header; per-user tokens with note
ownership.

**Why:** auth is cross-cutting. With it, every endpoint story inherits auth
work and a shared middleware file, and the stories stop being independent —
which is the one property this project exists to test. The static key was
close, but it still puts one shared file in every story's path. Per-user
tokens would need an owner column from story one and roughly double the work
per endpoint.

Auth is a good *later* epic: adding a cross-cutting concern to a codebase
three machines already share tests something the MVP cannot.

### 4.2 Bare response objects

**Chosen:** resources returned as themselves; collections as JSON arrays.

**Considered:** a `{"data": ..., "meta": ...}` envelope; bare singles with
wrapped collections.

**Why:** the envelope buys a home for pagination metadata we do not need —
the caller already knows the `limit` and `offset` it sent. It costs a wrapper
type every story must use correctly and noise in every test. The hybrid is
worse than either: it is the option three different agents are most likely to
apply inconsistently.

This decision is cheap now and expensive later. Changing it once five
endpoints exist means editing all of them, in five branches, at once.

### 4.3 FastAPI's default error shape

**Chosen:** `{"detail": "..."}`, the shape `HTTPException` already produces.

**Considered:** RFC 9457 Problem Details; a project-specific
`{"error": {"code", "message"}}`.

**Why:** Problem Details is the better standard and what a public API should
use. Here it would need a shared error module *and* a handler rewriting
FastAPI's own validation errors to match — a file every story depends on, to
solve a problem no consumer has. A custom shape has the same cost plus an
invented vocabulary, and FastAPI's built-in validation errors still would not
follow it.

Using the framework's own shape means our errors and the framework's errors
are the same shape, for free.

### 4.4 Search by SQL `LIKE`

**Chosen:** `WHERE lower(title) LIKE ? OR lower(body) LIKE ?`.

**Considered:** SQLite FTS5.

**Why:** FTS5 gives real ranking and tokenisation, and is the right answer for
a real corpus. It also adds a virtual table that must be kept in sync with
`notes` on every write — which couples the search stories to the notes
stories, the exact coupling this architecture is built to avoid. `LIKE` has no
ranking and scales badly; neither will ever be observed at this size.

If we want FTS5, it belongs in a later story that swaps the implementation
behind the same endpoint — a useful test of whether one story can change
another's internals without a merge war.

### 4.5 No version prefix

**Chosen:** `/notes`, `/tags`, `/search`, `/export`, `/health`.

**Considered:** `/v1/...`.

**Why:** no external consumer exists to break. A prefix is one line in
`main.py` whenever that changes, and until then it is ceremony repeated in
every route and every test.

### 4.6 SQLite: a file for the app, in memory for tests

**Chosen:** the service writes `./notes.db` (gitignored); each test file gets
its own in-memory database from a fixture.

**Considered:** a temp file per test; in-memory everywhere.

**Why:** three machines run this suite at the same time. A shared database
file would let one machine's test run corrupt another's, and the failure would
look like a flaky test rather than a collision. In-memory everywhere was
rejected because the running service would forget everything on restart, which
makes any live demo confusing.

## 5. Data model

Four tables, created by `db.py` at startup.

```
notes(id INTEGER PK, title TEXT NOT NULL, body TEXT NOT NULL,
      created_at REAL NOT NULL, updated_at REAL NOT NULL)

tags(id INTEGER PK, name TEXT NOT NULL UNIQUE)

note_tags(note_id INTEGER, tag_id INTEGER, PRIMARY KEY (note_id, tag_id))
```

`note_tags` is owned by the tags epic. The notes epic does not read it, so
deleting a note cascades through a foreign key rather than through code the
notes stories would have to know about.

## 6. Conventions that keep stories parallel

1. **A story declares the files it owns.** Two stories whose file lists
   overlap do not go out in the same wave.
2. **A new feature area is a new folder plus its test file.** Nothing else
   changes.
3. **Infrastructure changes are their own story.** If a change needs
   `main.py` or `db.py`, it is not a feature story.
4. **The story index is generated.** Nothing hand-edits it, so nothing
   conflicts on it.
