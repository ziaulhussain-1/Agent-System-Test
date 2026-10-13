# Stories

One folder per epic. One file per story. Nothing in this tree is hand-edited
by more than one agent at a time, and that is the whole point.

```
docs/stories/
  e1-foundation/
    epic.md          the epic: goal, scope, dependencies, traceability
    index.md         GENERATED from the story files — never hand-edit
    story-1-....md   one story, one file, owned by one agent at a time
    story-2-....md
  e2-notes-crud/
    ...
```

## Why one file per story

Several machines develop this repository at the same time. A single shared
story list that every agent ticks off would put a conflict in every pull
request, every time — and the conflict would be in the one file that records
what everybody is doing.

So: a story's status lives **in its own file**. The index is generated from
those files. If you find yourself editing `index.md` by hand, stop: the
generator is the thing to fix.

## Status is not a lock

Marking a story `Done` in its file records what happened. It does **not**
stop another machine picking the same story up, because the other machines
have their own checkouts and will not see your edit until it merges.

Claiming is a separate mechanism. Until it exists, the working convention is:

> Pick a story, **immediately create its branch** `story/<id>` before reading
> further or planning anything. If the branch is refused because another agent
> owns it, move to the next story.

Creating the branch is the claim, because the hub's branch registry is atomic
and shared; a status line in a file is neither. See
`docs/DECISION-work-item-coordination.md` in the Mesh repository for the three
options and why this is the interim one.

## Story file shape

Mirrors the house format:

```
# Story N — <title>

ID: E<e>-S<n>
Epic: docs/stories/<epic-folder>/epic.md
Status: Draft | Ready | In progress | Done

## User Story
## Description
## Acceptance Criteria
## Files This Story Owns      <- the parallel-work contract
## Non-Functional
## Out of Scope
## Test Notes
```

`Files This Story Owns` is not decoration. It is how we tell, before any work
starts, whether two stories can safely run at the same time. Two stories whose
file lists overlap do not go out in the same wave.
