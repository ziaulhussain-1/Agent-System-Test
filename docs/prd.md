# Product Requirements — Notes API

- Status: **Draft skeleton.** Product framing is settled; the marked decisions
  are open and are the subject of the next architecture discussion.
- Sharded to: `docs/prd/` (see `.bmad-core/core-config.yaml`)

## 1. Why this exists

This repository is the proving ground for several machines developing one
codebase at the same time through Mesh. The product is deliberately small and
deliberately ordinary: the interesting part is whether three agents can take
separate stories, work in parallel, and produce pull requests that merge
without stepping on each other.

That constraint shapes the requirements. Features are chosen so that each
story owns its own module and its own test file. A feature that would force
two stories to edit the same file is the wrong feature for this project, no
matter how sensible it looks on its own.

## 2. The product

A small REST API for notes.

- Create, read, update, delete a note
- Tag notes and list by tag
- Full-text search across titles and bodies
- Export a selection of notes
- An operational health endpoint

### 2.1 Users

| User | Needs |
|---|---|
| API consumer | Predictable REST semantics, clear errors, stable response shapes |
| Operator | A health endpoint, structured logs, a way to see what the service is doing |

### 2.2 Out of scope for the MVP

No user interface. No multi-tenancy. No sharing or collaboration between
users. No attachments or binary content. These are excluded to keep stories
independent, not because they are uninteresting.

## 3. Open decisions

These are the architecture discussion, not conclusions. Nothing below is
settled, and the epics are not written until they are.

1. **Authentication.** None, a static API key, or per-user tokens? This decides
   whether every later story carries auth work or none of them do.
2. **Storage.** SQLite is the obvious default. Does anything here need more?
3. **Search.** A `LIKE` query, SQLite FTS5, or something else? This is the one
   place where the simple answer may not survive contact with the requirement.
4. **Response envelope.** Bare objects, or a wrapper with metadata? Changing
   this later touches every endpoint, which is exactly the sort of change
   three parallel agents handle badly.
5. **Error model.** Problem Details (RFC 9457), or a project-specific shape?
6. **Versioning.** Is `/v1` in the path from the start?

## 4. Non-functional requirements

- Every endpoint has tests; a story is not done without them
- Errors never leak stack traces or internal paths
- Structured logs with a correlation id per request
- The service starts from a clean checkout with one documented command

## 5. Success for this experiment

Measured on the process, not only the product:

- Three machines complete stories from the same epic concurrently
- No two machines take the same story
- The resulting pull requests merge without conflicts
- The stories index never conflicts, because nothing hand-edits it
