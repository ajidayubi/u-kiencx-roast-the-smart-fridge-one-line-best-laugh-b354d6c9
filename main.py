#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

The line roasts the smart fridge as a snitch with a gym habit: it catches
the owner's midnight ice-cream raid, reports it to the owner's trainer,
then locks the freezer until the owner does ten squats in front of its
built-in camera. The sting lands on the last phrase - the fridge is not
just judging, it is enforcing a workout, and the owner cannot eat until
the fridge is satisfied.
"""

import os
import sys

LINE = (
    "My smart fridge ratted my midnight ice cream out to my trainer, "
    "then locked the freezer until I did ten squats in front of its camera."
)


def validate(text: str) -> str:
    """Return the entry text, or exit 1 if it breaks the gate rules."""
    if not 1 <= len(text) <= 160:
        print(f"entry is {len(text)} chars, must be 1-160", file=sys.stderr)
        sys.exit(1)
    if text.strip() != text:
        print("entry must not start or end with whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("entry must be one line", file=sys.stderr)
        sys.exit(1)
    return text


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    entry = validate(LINE)
    with open(out, "w", encoding="utf-8") as f:
        f.write(entry)
    print(f"wrote {len(entry)} chars to {out}: {entry}")


if __name__ == "__main__":
    main()
