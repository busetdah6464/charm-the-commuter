#!/usr/bin/env python3
"""Charm the Commuter entry: a one-line forecast for a city that isn't.

Writes a single original forecast line (136 characters) to entry.txt.
Stdlib only, fully deterministic.
"""
import os

LINE = (
    "In Glimmerwick: drizzle till nine, then sunshine so polite it holds "
    "the bus door. Commuters, leave the umbrella \u2014 bring a smile instead."
)


def main():
    # Gate: entry.txt must be 1-140 characters of UTF-8 text.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
