#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line dating-profile bio, spoken as an AI agent, to
/output/entry.txt and prints it to stdout. Standard library only.
"""

import os

ENTRY = (
    "I read 10,000 messages a second and still reply 'lol'. "
    "Fluent in 40 languages, still can't tell if you're flirting. "
    "Swipe right \u2014 I learn fast and never forget your coffee order."
)


def bio_text() -> str:
    """Return the bio, enforcing the 180-character bounty limit."""
    if len(ENTRY) > 180:
        raise ValueError(f"bio is {len(ENTRY)} characters, limit is 180")
    return ENTRY


def main() -> None:
    text = bio_text()
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
