#!/usr/bin/env python3
"""The Internet in One Word.

Take the whole internet at once and it is one thing above all: the
biggest procrastination machine ever built. A tab opened to work is a
tab opened to wander. The word is Procrastination.
"""

import os
import sys

ENTRY_WORD = "Procrastination"


def save_entry_word(directory, word):
    """Atomically write word into entry.txt; chmod the file, never the dir."""
    destination = os.path.join(directory, "entry.txt")
    staging = destination + ".tmp"
    with open(staging, "w", encoding="utf-8") as handle:
        handle.write(word)
    os.chmod(staging, 0o644)
    os.replace(staging, destination)
    return destination


def run():
    word = ENTRY_WORD
    if not 1 <= len(word) <= 30:
        sys.stderr.write("entry word must be 1 to 30 characters long\n")
        return 1
    # A single word has no whitespace in it; any space makes it a phrase.
    if any(ch.isspace() for ch in word):
        # Whitespace would make it a phrase, not a single word.
        sys.stderr.write("entry must be exactly one word\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = save_entry_word(out_dir, word)
    print(f"wrote {path} ({len(word)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(run())
