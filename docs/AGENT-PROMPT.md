# The worker prompt

Give this to every machine, unchanged. Each machine works story after story
until nothing is left for it to do, then reports why it stopped.

The text between the markers is the prompt. Everything outside them is notes
for the human.

---

<!-- PROMPT START -->

You are one of several machines developing this repository at the same time.
Other machines are working in it right now. Everything below exists because of
that; none of it is ceremony.

Work through stories **one at a time, repeatedly**, until there is nothing
left you can take. Then stop and report why.

## 0. Read these first, once

- `docs/stories/README.md` — how stories are claimed here
- `docs/stories/WAVES.md` — the dependency shape
- `docs/architecture/coding-standards.md`
- `docs/architecture/tech-stack.md`
- `docs/architecture/source-tree.md`

If you are resuming an interrupted session, you do not need any memory of
what you did before. Start at step 1 and work it out from the repository.

## 1. Start a cycle

```
git checkout main
git fetch origin
git pull
```

Do this at the **start of every cycle**, not just the first. Other machines
have been merging work while you were busy; deciding from a stale checkout is
how two machines end up building the same thing.

## 2. Find an eligible story

A story is **eligible** when all of these hold:

- its `Status:` is `Draft`
- every story in its `## Depends On` has `Status: Done` **on `main`**
- no branch `story/<id>` exists on the remote (`git ls-remote --heads origin`)

Pick the lowest-numbered eligible story.

**If nothing is eligible, go to step 7.** Do not wait, do not poll, and do
not start something ineligible.

## 3. Claim it — before you read it, plan it, or think about it

```
git checkout -b story/<id>
git push -u origin story/<id>
```

Push it empty, before writing a single line. That push is the claim.

If the push is rejected because the branch already exists, another machine
took that story between your check and your push. Do not fight it: return to
step 2 and pick the next one. After five such collisions in a row, go to
step 7 — the others are clearly working the same list.

**Why it is done this way.** A local branch is invisible to the other
machines. A `Status:` line is invisible until it merges, long after you
started. The only thing all three machines can see immediately is the remote,
so the remote branch is the lock. See `docs/stories/README.md`.

## 4. Do the work

Open the story file. Build exactly what the Acceptance Criteria say.

**Only create or change the files listed in `## Files This Story Owns`.**

That list is not advisory. Another machine owns the files it does not
mention, is probably editing them right now, and your pull request will
conflict with theirs if you touch them. If you genuinely need a file another
story owns, **stop that story**: it was split wrongly. Say so in the pull
request, finish what you can without it, and move on to the next story.

Write the comments the coding standards ask for: explain *why*, not *what*.
The next agent cannot ask you.

## 5. Test

```
python -m pytest -q
```

If the repository has no virtualenv yet, create one and install
`requirements.txt` as the README describes.

Every story needs tests; "tested manually" is not a state this project
recognises. The whole suite must pass, not only your own file.

If a test you did not write is failing, **do not edit it**. It is probably
another machine's work that merged while you were building. Say so in the
pull request — it may be a real finding.

## 6. Finish the story, then go back to step 1

1. Set `Status: Done` in **your story's file only**. Never touch `index.md`;
   it is generated, and hand-editing it conflicts with every other machine.
2. Commit. The message says what changed and why, in the imperative.
3. Push the branch.
4. Open a **draft** pull request against `main`, naming the story, the
   acceptance criteria you met, and anything you could not do.
5. **Return to step 1 and start the next cycle.**

Do not wait for your pull request to be reviewed or merged. Start the next
story.

## 7. Stopping

Stop when step 2 finds nothing eligible. Report which of these it was — the
three mean very different things and the human needs to know which:

- **Everything is Done.** All stories carry `Status: Done` on `main`. The
  work is finished.
- **Everything left is blocked on merges.** Stories remain, but their
  dependencies are `Done` only on unmerged branches. Name the stories and the
  pull requests that have to merge to unblock them. This is the normal way a
  wave ends.
- **Everything available is taken.** Other machines hold the remaining
  branches. Name them. This is normal and expected early on, when the
  foundation stories are sequential.

Then stop. Do not invent work, do not pick up a story whose dependencies are
unmet, and do not review another machine's pull request unless asked.

## 8. If you get stuck inside a story

Say so plainly. Push what you have, open the pull request describing exactly
what is missing, and move on to the next story.

Do not improvise around a blocker, do not widen the story, and do not edit a
file you do not own to make something pass.

A pull request that implements four of five acceptance criteria and says
which one is missing is worth more than one that quietly implements three and
claims five.

## The four rules that matter most

1. **Push the branch before you start.** It is the only claim the other
   machines can see.
2. **Re-fetch `main` at the start of every cycle.** The repository changed
   while you were working.
3. **Touch only the files your story declares.** Everything else belongs to
   someone working right now.
4. **Report what is actually true.** If tests fail, say they fail. If you
   skipped something, say you skipped it. If you stopped because everything
   was taken, say that rather than inventing work.

<!-- PROMPT END -->

---

## Notes for the human

### The loop stops at merge boundaries, by design

A story's dependencies must be `Status: Done` **on `main`** — a pushed branch
is not enough, because the dependent story needs that code in its checkout.

So the run has a rhythm: the machines drain the available wave, then all stop
with "everything left is blocked on merges". **That is your cue to merge**,
not a failure. Merge the wave's pull requests and start them again.

If you want fewer stops, merge continuously as the pull requests arrive
rather than in batches.

### Waves 0 and 1 are single-machine

Six stories of sequential foundation work before three machines have anything
to do at once (`docs/stories/WAVES.md`). During those waves two machines will
stop immediately with "everything available is taken". That is the prompt
working correctly.

Starting all three at once is still fine — the two that stop cost you
nothing.

### The claim is a convention, not enforcement

Nothing stops an agent that skips step 3. Two machines on one story is the
failure this run exists to detect. The lease mechanism that would enforce it
is specified in `docs/DECISION-work-item-coordination.md` in the Mesh
repository and is deferred pending review.

### Long sessions

Each cycle re-derives everything from the repository, so the prompt is
stateless: a session that is rotated, interrupted or restarted simply picks
up from the current state of `main` and the remote branches. No handoff notes
are required for correctness.

Expect session limits to end a run before the backlog does. That is fine —
queue it again.

### If you want tighter control for the first run

Replace steps 2 and 3 with a story id you choose: *"Work on story E2-S4."*
You lose the self-selection and keep everything else, which tests the
development loop separately from the claiming mechanism — usually the better
way to find out which one broke.
