# Wave plan

Which stories can run at the same time, and why. A **wave** is a set of
stories with no dependency between them and no file in common — so three
machines can take three of them and the resulting pull requests merge.

Verify before dispatching a wave:

```
python tools/check_story_overlap.py
```

**34 stories across 8 epics.** The number that matters is not 34 but the
width of wave 2: once the foundation and the note store exist, **18 stories
are available at once**, which is six rounds of work for three machines with
nothing waiting on anything.

---

## Wave 0 — Foundation (one machine, mostly sequential)

Nothing here is parallel. Everything else depends on it and the stories
depend on each other. Run it on one machine and let it finish.

| Order | Story | Note |
|---|---|---|
| 1 | `E1-S1` App skeleton and router discovery | Everything imports it |
| 2 | `E1-S2` Database and schema discovery | Needs the app to bootstrap on startup |
| 3 | `E1-S3` Health · `E1-S4` Correlation id · `E1-S5` Test fixtures | These three can run together |

`E1-S4` must not run beside `E1-S1` — it adds one line to `app/main.py`,
which `E1-S1` owns. That is the only declared overlap in the project.

**Why discovery matters here.** `E1-S1` discovers routers and `E1-S2`
discovers `app/*/schema.sql`. Without both, every later epic would have to
edit a central registration file and a central `CREATE TABLE` block — two
files that grow with every epic and conflict on every wave. These two stories
are what make the other 29 independent.

## Wave 1 — The gate (one machine, alone)

| Story | Why alone |
|---|---|
| `E2-S1` Note model, schema and store | Five endpoint stories here plus **all of E3–E8** read notes through it |

The bottleneck of the whole plan: one machine, one story, two machines idle.
Worth doing well rather than quickly.

## Wave 2 — The wide one (three machines, six rounds)

Eighteen stories become available at once, none overlapping.

| Epic | Stories |
|---|---|
| E2 Notes | `S2` create · `S3` get · `S4` list · `S5` update · `S6` delete |
| E3 Tags | `S1` store |
| E4 Search | `S1` query |
| E5 Export | `S1` JSON · `S2` Markdown · `S3` CSV |
| E6 Archive | `S1` store |
| E7 Import | `S1` JSON parser · `S2` Markdown parser |
| E8 Stats | `S1` queries |

Strictly, `E5-S2` and `E5-S3` want `E5-S1` to have created
`app/export/__init__.py` first — the package file, not its code. Give E5-S1
a short head start, or let the second machine create the file if it is
missing.

**This is the wave the experiment exists to measure.**

## Wave 3 — Second layer (three machines, three rounds)

| Story | Depends on |
|---|---|
| `E3-S2` Attach · `E3-S3` Detach · `E3-S4` List tags · `E3-S5` Notes by tag | `E3-S1` |
| `E4-S2` Search endpoint · `E4-S3` Snippets | `E4-S1` |
| `E6-S2` Archive · `E6-S3` Restore · `E6-S4` List archived | `E6-S1` |
| `E8-S2` Stats · `E8-S3` Activity | `E8-S1` |

Eleven stories, no overlaps.

## Wave 4 — The joins (two machines)

| Story | Depends on |
|---|---|
| `E5-S4` Export endpoint | `E5-S1`, `E5-S2`, `E5-S3`, `E3-S1` |
| `E7-S3` Import endpoint | `E7-S1`, `E7-S2`, `E2-S1` |

## Wave 5 — Last (one machine)

| Story | Depends on |
|---|---|
| `E7-S4` Import dry run | `E7-S1`, `E7-S2` |

---

## Shape of the run

| Wave | Stories | Machines usefully busy |
|---|---|---|
| 0 | 5 | 1, then 3 for the last three |
| 1 | 1 | 1 — the bottleneck |
| 2 | 18 | 3, six rounds |
| 3 | 11 | 3, nearly four rounds |
| 4 | 2 | 2 |
| 5 | 1 | 1 |

Six stories of mostly-sequential work at the start, then 29 that parallelise
well. That shape is inherent to building from nothing, not a flaw in the
plan — but it means the interesting measurement does not begin immediately.

## What to watch during wave 2

This is the measurement, not the build:

- **Did two machines take the same story?** Then the claiming convention
  failed, not the plan. See `docs/stories/README.md`.
- **Did the pull requests merge cleanly?** If not, which file did two
  stories both touch, and why was it not in a `Files This Story Owns` list?
- **How long did three machines take versus one would have?** Three machines
  taking three times as long as one is a failed experiment with a working
  product (`docs/prd.md` §5).

## The rule that makes this work

A story may only create or change the files it declares. If an agent finds it
needs a file another story owns, the stories were split wrongly — that is a
finding worth recording in the pull request, not something to edit around.
