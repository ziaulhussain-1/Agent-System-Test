# Tech stack

| Concern | Choice | Why |
|---|---|---|
| Language | Python 3.11+ | Already present on every machine in the cluster |
| Framework | FastAPI | Typed request/response models, OpenAPI for free |
| Server | uvicorn | What FastAPI expects |
| Storage | SQLite via `sqlite3` | No service to run; one file to reset between tests |
| Validation | Pydantic v2 | Comes with FastAPI; do not add a second validation library |
| Tests | pytest + `fastapi.testclient` | Matches the Mesh repository, so agents need no new habits |
| Lint | ruff | Same |

## Rules

- **No dependency is added by a story without saying so in its Dev Notes.** A
  machine that adds a package mid-story breaks the other two machines' next
  run, and the failure appears far from the cause.
- Pin versions in `requirements.txt`. "Latest" means three machines can
  install three different things on the same afternoon.
- Nothing here requires network access at test time.
