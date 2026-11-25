#!/usr/bin/env python3
"""Midnight Fridge Roast - make.fun entry (program/v1).

Writes a single one-line roast of a smart fridge that refuses to open
after midnight to <MAKEFUN_OUTPUT_DIR>/entry.txt.

Contract (from the competition kit):
- Output goes ONLY to the grader's output directory, read from the
  MAKEFUN_OUTPUT_DIR environment variable ("/output" in the grader).
  Nothing is ever written into the repository directory: the grader
  mounts the repo read-only and a write there fails run_completes.
- The entry must be UTF-8 text, 1-200 characters, not only whitespace.
- Deterministic: no network, no randomness, no clock. The same bytes
  come out on every run.

The roast (chosen against the judge brief, most important first):
1. It is a one-line roast of a smart fridge that refuses to open
   after midnight - the refusal itself is the target, not smart
   homes in general.
2. It lands a real joke with a turn: the fridge treats its owner
   like a burglar, and the owner answers that he bought the milk -
   the "thief" owns the loot. The line was tightened once (a longer
   draft naming "my own kitchen" was cut) so no word is wasted.
3. It is one tight line that reads cleanly aloud, with a single joke.
4. It sounds like something a person would actually say out loud at
   the fridge door at midnight.
"""

import os
import sys

ENTRY = (
    "My fridge locks at midnight and treats me like a burglar "
    "\u2014 I bought the milk, I'm not stealing it."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > MAX_CHARS:
        print("entry invalid: %d chars" % len(text), file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
