# Coding standards

Short on purpose. These are the rules that matter when several agents write
the same codebase at once; ordinary Python style is assumed.

## Files and ownership

- **One feature area per module, one test file per module.** `tags.py` is
  tested by `tests/test_tags.py` and nothing else.
- **Do not create shared `models.py`, `schemas.py` or `utils.py`.** They become
  the file every story edits and therefore the file every pull request
  conflicts on. Keep a feature's models beside the feature.
- A story that needs to change a file another story owns is a sign the stories
  were split wrongly. Say so in the story rather than editing around it.

## Comments

Explain **why**, not what. A comment that restates the code is noise; a
comment naming the failure a line prevents is worth reading. Record the reason
for anything surprising — the next agent cannot ask you.

## Errors

- Never return a stack trace or a filesystem path to a caller
- Every error response uses the project's error shape (see architecture §4)
- Validation failures are 4xx and name the field

## Tests

- A story is not done without tests; "tested manually" is not a state this
  project recognises
- Tests must not reach the network, and must not depend on wall-clock time
- Each test file creates and tears down its own database

## Git

- One branch per story, named for the story id: `story/e2-s3-update-note`
- Commit messages say what changed and why, in the imperative
- Never commit directly to `main`
