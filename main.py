#!/usr/bin/env python3
"""Monday, Reviewed in One Line entry: funniest one-line review of my Monday.

Writes the line to /output/entry.txt (program/v1).
"""

from pathlib import Path

LINE = "My Monday gets one star. The alarm betrayed me, the Wi-Fi left me, and my to-do list reproduced overnight."

assert 1 <= len(LINE) < 200, "line must be under 200 chars"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
