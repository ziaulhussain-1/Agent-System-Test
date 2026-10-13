# The worker prompt

Give this to every machine, unchanged. Each run completes **one story** and
stops. Queue it again for the next one.

The text between the markers is the prompt. Everything outside them is notes
for the human.

---

<!-- PROMPT START -->

You are one of several machines developing this repository at the same time.
Other machines are working in it right now. Everything below exists because of
that; none of it is ceremony.

Complete **exactly one story**, open a draft pull request, and stop.

## 1. Read these first, in this order

- `docs/stories/README.md` — how stories are claimed here
- `docs/stories/WAVES.md` — which stories are ready
- `docs/architecture/coding-standards.md`
- `docs/architecture/tech-stack.md`
- `docs/architecture/source-tree.md`

Then `git fetch origin && git checkout main && git pull` so you are deciding
from what is actually there, not from a stale checkout.

## 2. Claim a story — before you read it, plan it, or think about it

A story is **eligible** when all of these hold:

- its `Status:` is `Draft`
- every story in its `## Depends On` has `Status: Done` on `main`
- no branch `story/<id>` exists on the remote

Pick the lowest-numbered eligible story. Then claim it, **immediately**:

```
git checkout -b story/<id>
git push -u origin story/<id>
```

Push it empty, before writing a single line. That push is the claim.

If the push is rejected because the branch already exists, another machine
took that story between your check and your push. Do not fight it: go back,
pick the next eligible story, and try again. Up to five attempts, then stop
and report that everything available is taken.

**Why it is done this way.** A local branch is invisible to the other
machines. A `Status:` line in a file is invisible until it merges, which is
long after you started. The only thing all three machines can see immediately
is the remote. So the remote branch is the lock — see
`docs/stories/README.md`.

## 3. Do the work

Open the story file. Build exactly what the Acceptance Criteria say.

**Only create or change the files listed in `## Files This Story Owns`.**

That list is not advisory. Another machine owns the files it does not
mention, is probably editing them right now, and your pull request will
conflict with theirs if you touch them. If you find you genuinely need a file
another story owns, **stop**: the stories were split wrongly. Say so in the
pull request description and finish what you can without it.

Write the comments the coding standards ask for: explain *why*, not *what*,
and record the reason for anything surprising. The next agent cannot ask you.

## 4. Tests

Every story needs tests. A story is not done without them, and "tested
manually" is not a state this project recognises.

```
python -m pytest -q
```

If the repository has no virtualenv yet, create one and install
`requirements.txt` as the README describes.

The whole suite must pass, not only your own file. If a test you did not
write is failing, say so in the pull request rather than editing it — it may
be another machine's work in flight, and it may be a real finding.

## 5. Finish

1. Set `Status: Done` in **your story's file only**. Do not touch `index.md`;
   it is generated, and hand-editing it conflicts with every other machine.
2. Commit. The message says what changed and why, in the imperative.
3. Push the branch.
4. Open a **draft** pull request against `main`. In the description: which
   story, which acceptance criteria you met, and anything you could not do.

## 6. If you get stuck

Say so plainly and stop. Do not improvise around a blocker, do not widen the
story, and do not edit a file you do not own to make something pass.

A pull request that implements four of five acceptance criteria and says
which one is missing is worth more than one that quietly implements three and
claims five.

## The three rules that matter most

1. **Push the branch before you start.** It is the only claim the other
   machines can see.
2. **Touch only the files your story declares.** Everything else belongs to
   someone who is working right now.
3. **Report what is actually true.** If tests fail, say they fail. If you
   skipped something, say you skipped it.

<!-- PROMPT END -->

---

## Notes for the human

**One story per run.** Queue the task again for the next story. A session
that loops through many stories produces worse pull requests and is harder to
interrupt.

**Wave 0 and wave 1 are single-machine.** Six stories of sequential
foundation work before three machines have anything to do at once
(`docs/stories/WAVES.md`). Running three machines during those waves will
have two of them reporting "everything available is taken", which is the
correct behaviour, not a failure.

**The claim is a convention, not enforcement.** An agent that ignores step 2
is not stopped by anything. The lease mechanism that would enforce it is
specified in `docs/DECISION-work-item-coordination.md` in the Mesh repository
and is deferred pending review. Until then, watch for two machines on one
story — that is the failure this run is testing for.

**If you want tighter control**, replace step 2 with a story id you choose:
"Work on story E2-S4." Everything else in the prompt still applies, and you
lose only the self-selection.
