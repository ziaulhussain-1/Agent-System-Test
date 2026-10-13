# Product Requirements — Notes API

- Status: **Complete.** Decisions settled 2026-10-13; see
  `docs/architecture.md` §4 for the technical reasoning behind each.
- Sharded to: `docs/prd/` (see `.bmad-core/core-config.yaml`)

## 1. Why this exists

This repository is the proving ground for several machines developing one
codebase at the same time through Mesh. The product is deliberately small and
deliberately ordinary: the interesting part is whether three agents can take
separate stories, work in parallel, and produce pull requests that merge
without stepping on each other.

That constraint shapes the requirements. Features are chosen so that each
story owns its own module and its own test file. **A feature that would force
two stories to edit the same file is the wrong feature for this project**, no
matter how sensible it looks on its own.

## 2. The product

A small REST API for notes. No user interface.

### 2.1 Users

| User | Needs |
|---|---|
| API consumer | Predictable REST semantics, clear errors, stable response shapes |
| Operator | A health endpoint, structured logs, a documented way to start it |

### 2.2 Functional scope

**Notes** — the core resource.

- Create a note with a title and a body
- Fetch a note by id
- List notes, newest first, with limit/offset paging
- Update a note's title or body
- Delete a note

**Tags** — labelling and retrieval.

- Add a tag to a note
- Remove a tag from a note
- List every tag in use, with how many notes carry each
- List the notes carrying a given tag

**Search** — finding things.

- Case-insensitive substring search across titles and bodies
- Paged results, newest first
- An empty query is a client error, not an empty result

**Export** — getting data out.

- Export notes as JSON
- Export notes as Markdown, one document with a section per note
- Export everything, or restrict to a tag

**Health** — operations.

- A `GET /health` that reports whether the database is reachable

### 2.3 Out of scope for the MVP

No user interface. **No authentication** — see §3.1. No multi-tenancy, sharing
or collaboration. No attachments or binary content. No soft delete or revision
history. No rate limiting.

These are excluded to keep stories independent, not because they are
uninteresting. Authentication in particular is a good *later* epic: adding a
cross-cutting concern to a codebase three machines already share is a sharper
test than building it in from the start.

## 3. Decisions

Settled. Each is recorded with its reasoning in `docs/architecture.md` §4.

### 3.1 No authentication in the MVP

The API is unauthenticated. This is a local experiment with no exposure, and
auth would make every endpoint story carry auth work — destroying the story
independence the whole project exists to test.

### 3.2 Bare response objects

`GET /notes/{id}` returns the note. `GET /notes` returns a JSON array. No
envelope, no `data` wrapper. Paging information is conveyed by the request
parameters the caller already sent.

### 3.3 FastAPI's default error shape

Errors are `{"detail": "..."}` with an appropriate status code — what
`HTTPException` already produces and what FastAPI's own validation failures
use. We do not invent a second error vocabulary that the framework's own
errors would not follow.

### 3.4 Search by SQL `LIKE`

Case-insensitive substring matching over `title` and `body`. No FTS5, no
second table to keep in sync with notes, therefore no coupling between the
search stories and the notes stories.

### 3.5 No version prefix in paths

Routes are `/notes`, `/tags`, `/search`. There is no external consumer to
break, and a prefix can be added in one line later if that changes.

### 3.6 SQLite: a file for the app, in memory for tests

The running service uses a gitignored file. Every test file gets its own
in-memory database from a fixture, so three machines running the suite at the
same time cannot interfere with each other.

## 4. Non-functional requirements

- **Tests.** Every endpoint has them. A story is not done without them, and
  "tested manually" is not a state this project recognises.
- **No leakage.** Errors never return a stack trace, a filesystem path, or a
  SQL fragment.
- **Logging.** Structured, one correlation id per request, no note content in
  the logs.
- **Startup.** The service runs from a clean checkout with one documented
  command and no external services.
- **Isolation.** The test suite touches no network and depends on no
  wall-clock time.

## 5. Success criteria

Measured on the process as much as the product.

**The product works:**
- Every endpoint in §2.2 exists, behaves as described, and is tested
- The suite passes from a clean checkout on all three machines

**The experiment works:**
- Three machines complete stories from the same epic concurrently
- No two machines take the same story
- The resulting pull requests merge without conflicts
- The stories index never conflicts, because nothing hand-edits it

The second list is the one that matters. A working Notes API that took three
machines three times as long as one would be a failed experiment with a
successful product.
