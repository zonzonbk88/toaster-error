#!/usr/bin/env python3
"""The Funniest Toaster Error Message - make.fun entry.

Writes a single deadpan toaster error message (<=120 chars) to /output/entry.txt.
Standard library only.
"""

import os

LINE = "ERROR E07: Bread refused. I respect its decision."

def main() -> None:
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"
    assert "\n" not in LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
