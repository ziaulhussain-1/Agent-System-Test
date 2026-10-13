"""Which stories can safely run at the same time?

Several machines develop this repository concurrently. Two stories that both
change the same file will produce two pull requests that conflict, and the
conflict surfaces at merge time — long after the work was done, when it is
most expensive to unpick.

Every story declares a `## Files This Story Owns` section. This reads those
declarations and reports any pair that overlaps. A pair that overlaps must not
go out in the same wave.

    python tools/check_story_overlap.py            # report overlaps
    python tools/check_story_overlap.py --waves    # also print a wave plan

Exit code is 1 if an *undeclared* overlap exists, so this can gate CI. One
overlap is expected and declared: E1-S1 and E1-S4 both touch app/main.py,
because registering middleware needs a line there. It is listed in ALLOWED
below rather than left to be rediscovered.
"""
from __future__ import annotations

import itertools
import pathlib
import re
import sys

# Declared, deliberate overlaps: (story a, story b) -> why.
ALLOWED = {
    ("E1-S1", "E1-S4"): "middleware registration needs one line in main.py; "
                        "E1-S4 runs after E1-S1 and never beside it",
}

ROOT = pathlib.Path(__file__).resolve().parent.parent
STORIES = ROOT / "docs" / "stories"


def load():
    """story id -> (owned files, dependency line)."""
    out = {}
    for p in sorted(STORIES.glob("e*/story-*.md")):
        text = p.read_text(encoding="utf-8")
        sid = re.search(r"^ID: (\S+)", text, re.M)
        if not sid:
            print(f"  ! {p} has no ID line", file=sys.stderr)
            continue
        owns = text.split("## Files This Story Owns", 1)[1].split("##", 1)[0]
        deps = text.split("## Depends On", 1)[1].split("##", 1)[0].strip()
        # only backticked paths count; prose in the section is ignored
        files = set(re.findall(r"^- `([^`]+)`", owns, re.M))
        out[sid.group(1)] = (files, deps.splitlines()[0] if deps else "")
    return out


def main() -> int:
    stories = load()
    print(f"{len(stories)} stories\n")

    undeclared = 0
    for a, b in itertools.combinations(sorted(stories), 2):
        shared = stories[a][0] & stories[b][0]
        if not shared:
            continue
        why = ALLOWED.get((a, b)) or ALLOWED.get((b, a))
        if why:
            print(f"  declared  {a} / {b}: {sorted(shared)}\n            {why}")
        else:
            undeclared += 1
            print(f"  OVERLAP   {a} / {b}: {sorted(shared)}")

    print(f"\nundeclared overlaps: {undeclared}")
    if "--waves" in sys.argv:
        print("\nWave plan: docs/stories/WAVES.md")
    return 1 if undeclared else 0


if __name__ == "__main__":
    raise SystemExit(main())
