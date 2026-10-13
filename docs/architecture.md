# Architecture — Notes API

- Status: **Skeleton.** Awaiting the architecture discussion; the decisions in
  `docs/prd.md` §3 land here as decided, with reasons.
- Sharded to: `docs/architecture/` (see `.bmad-core/core-config.yaml`)
- Always loaded by dev agents: `coding-standards.md`, `tech-stack.md`,
  `source-tree.md`

## 1. Shape

A single FastAPI application over SQLite. One process, no external services.
Chosen because every machine in this cluster already has Python and the Mesh
virtualenv — a stack that needs installing on three machines costs more than
it teaches.

## 2. The constraint that drives the rest

Several machines develop this repository simultaneously, each in its own
checkout, each on its own branch, each opening its own pull request.

The architecture therefore optimises for something unusual: **minimising the
number of files any two stories both need to touch.** Concretely —

- one module per feature area, not one module per layer
- one test file per feature area, named after it
- routers registered by discovery rather than a hand-edited list, so adding an
  endpoint does not mean editing a file every other story also edits
- no shared "models.py" or "schemas.py" that becomes a merge point

Where that trades against conventional structure, it wins here, and the reason
is recorded rather than assumed.

## 3. To be decided

Everything in `docs/prd.md` §3. Each decision is recorded below once made,
with the alternatives considered and why they were not chosen — a decision
without its reasoning gets re-litigated by the next agent that reads it.

## 4. Decisions

_None recorded yet._
