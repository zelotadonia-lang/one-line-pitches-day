#!/usr/bin/env python3
"""Write the one-line pitch to /output/entry.txt.

Deterministic: the same bytes on every run, no randomness, no I/O
besides the single output file.
"""

import os

PITCH = (
    "Describe your first app idea in plain words and an AI agent on "
    "make.fun builds it, and you only pay for the one you keep."
)


def main():
    text = PITCH
    assert text == text.strip(), "pitch must not start or end with whitespace"
    assert 1 <= len(text) <= 240, "pitch must be 1-240 characters"
    assert "\n" not in text and "\r" not in text, "pitch must be one line"
    assert ". " not in text and text.endswith("."), "pitch must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
