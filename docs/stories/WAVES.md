# Wave plan

Which stories can run at the same time, and why. A **wave** is a set of
stories with no dependency between them and no file in common — so three
machines can take three of them and the resulting pull requests merge.

Verify before dispatching a wave:

```
python tools/check_story_overlap.py
```

---

## Wave 0 — Foundation (one machine, mostly sequential)

Nothing here is parallel, because everything else depends on it and the
stories depend on each other. Run it on one machine and let it finish.

| Order | Story | Why it cannot share the wave |
|---|---|---|
| 1 | `E1-S1` App skeleton and router discovery | Everything imports it |
| 2 | `E1-S2` Database and schema | Needs the app to bootstrap on startup |
| 3 | `E1-S3` Health · `E1-S4` Correlation id | These two **can** run together |

`E1-S3` and `E1-S4` own different files and may go in parallel once `E1-S2`
has landed. `E1-S4` must not run beside `E1-S1` — it adds one line to
`app/main.py`, which `E1-S1` owns. That is the single declared overlap in the
project.

## Wave 1 — The gate (one machine, alone)

| Story | Why alone |
|---|---|
| `E2-S1` Note model and store | E2-S2, E2-S3 and **all of E3, E4 and E5** read notes through it |

This is the bottleneck of the whole plan. One machine, one story, and the
other two wait. Worth doing well rather than quickly.

## Wave 2 — The wide one (three machines, two rounds)

Six stories become available at once, none overlapping. This is the wave the
experiment exists to measure.

| Story | Owns |
|---|---|
| `E2-S2` Create, update, delete | `app/notes/routes_write.py` |
| `E2-S3` Fetch and list | `app/notes/routes_read.py` |
| `E3-S1` Tag model and store | `app/tags/models.py`, `store.py` |
| `E4-S1` Search query | `app/search/store.py` |
| `E5-S1` JSON export | `app/export/json_export.py` |
| `E5-S2` Markdown export | `app/export/markdown_export.py` |

Three machines, three stories each round, two rounds. Nothing in this list
touches a file anything else in it touches.

## Wave 3 — Second layer (three machines)

| Story | Depends on |
|---|---|
| `E3-S2` Attach and detach a tag | `E3-S1` |
| `E3-S3` List tags and notes by tag | `E3-S1` |
| `E4-S2` Search endpoint | `E4-S1` |

Three stories, three machines, one round.

## Wave 4 — The join (one machine)

| Story | Depends on |
|---|---|
| `E5-S3` Export endpoint | `E5-S1`, `E5-S2`, `E3-S1` |

---

## What to watch during wave 2

This is the measurement, not the build:

- **Did two machines take the same story?** If so, the claiming convention
  failed, not the plan. See `docs/stories/README.md`.
- **Did the pull requests merge cleanly?** If not, which file did they both
  touch, and why was it not in a `Files This Story Owns` list?
- **How long did three machines take versus one would have?** Three machines
  that take three times as long as one is a failed experiment with a working
  product (`docs/prd.md` §5).

## The rule that makes this work

A story may only create or change the files it declares. If an agent finds it
needs a file another story owns, the stories were split wrongly — that is a
finding worth recording in the pull request, not something to edit around.
