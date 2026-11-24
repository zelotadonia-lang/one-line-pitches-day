#!/usr/bin/env python3
"""Write the one-line pitch to /output/entry.txt.

The pitch asks a friend to say their idea out loud once, then watch
make.fun build their first app from it — the only step is speaking,
not learning to code.

Deterministic: the same bytes on every run, no randomness, no I/O
besides the single output file.
"""

import os

PITCH = (
    "Say your idea out loud once and make.fun builds your first app "
    "while you watch it take shape."
)


MIN_LEN = 1
MAX_LEN = 240


def validate_pitch(text):
    """Check the pitch against the competition gate (RULES.txt).

    Returns the text unchanged when every check passes, so the
    written bytes are exactly the PITCH constant.
    """
    assert text == text.strip(), "pitch must not start or end with whitespace"
    assert MIN_LEN <= len(text) <= MAX_LEN, "pitch must be 1-240 characters"
    assert "\n" not in text and "\r" not in text, "pitch must be one line"
    assert ". " not in text and text.endswith("."), "pitch must be one sentence"
    assert text.encode("utf-8").decode("utf-8") == text, "pitch must be valid UTF-8"
    return text


def main():
    text = validate_pitch(PITCH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
