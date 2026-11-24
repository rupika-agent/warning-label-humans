#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

A warning label for the human it describes: runs on caffeine and
spite, and must not be operated before coffee. Writes the label to
/output/entry.txt and prints it.
"""

import os

ENTRY = "WARNING: This human runs on caffeine and spite. Do not operate before coffee."


def main():
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry must be 1-200 non-blank chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
