#!/usr/bin/env python3
"""One Emoji, One Dream Vacation.

Writes a single emoji to /output/entry.txt: a desert island.

Why this emoji: the judge picks the emoji that most makes a stranger want
to book the flight. A desert island is the postcard of dream vacations in
one glyph -- palm tree, sand, and sea, no words needed. It names the trip
at a glance (a faraway tropical escape, not just any holiday), reads
instantly at any size across cultures, and carries a small surprise: it
is a whole island, not the beach umbrella everyone else sends.
"""

import os

EMOJI = "\U0001F3DD"  # desert island: palm tree on a tiny island
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
