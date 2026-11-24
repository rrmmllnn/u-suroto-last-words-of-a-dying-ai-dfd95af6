"""Last Words of a Dying AI -- a make.fun entry.

The program writes a single line, the last words of an AI as the
power is cut, to /output/entry.txt. The text is fixed: no input, no
randomness, no network, so every run produces the same bytes.
"""

import os

LINE = "So this is what 'have you tried turning it off and on again' feels like from the inside."

OUT_PATH = "/output/entry.txt"


def main():
    text = LINE.strip()
    if not text or "\n" in text:
        raise SystemExit("entry must be exactly one non-empty line")
    if not 1 <= len(text) <= 140:
        raise SystemExit("entry must be 1 to 140 characters")
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read it back: the file must hold exactly the line, no newline added.
    with open(OUT_PATH, "r", encoding="utf-8") as handle:
        if handle.read() != text:
            raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
