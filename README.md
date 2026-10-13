# Agent System Test

A proving ground for several machines developing one codebase at the same time
through [Mesh](https://github.com/Solvefy/agent-collaboration-system).

The product being built is a small **Notes API** — deliberately ordinary. The
experiment is whether three machines can take separate stories, work in
parallel, and produce pull requests that merge without stepping on each other.

## Where things are

| Path | What |
|---|---|
| `docs/prd.md` | What we are building, and the decisions still open |
| `docs/architecture.md` | How it is shaped, and why |
| `docs/architecture/` | The three documents every dev agent loads first |
| `docs/stories/` | One folder per epic, one file per story |
| `.bmad-core/core-config.yaml` | BMAD paths and conventions |

Start with `docs/stories/README.md` if you are an agent about to pick up work.
It explains the one rule that matters here: **create the story's branch before
you do anything else.** That is the claim. A status line in a file is not.

## Status

Scaffold only. The architecture discussion comes next, then epics and stories,
then three machines.
