"""Ridiculous at First Glance, Real by the Second.

Writes a single-sentence startup pitch to /output/entry.txt:
a bizarre idea that sounds like a joke until the business logic lands.
"""

import os

SENTENCE = (
    "We sell sealed jars of hometown air to homesick expats for $29, "
    "because a whiff of childhood beats a $900 flight home and nostalgia "
    "is the one product nobody returns."
)


def main() -> None:
    # Guard the gate before writing: one sentence, 1-200 characters,
    # and not only white space, exactly as the sealed scorer checks.
    sentence = SENTENCE.strip()
    assert 1 <= len(sentence) <= 200, f"sentence is {len(sentence)} chars"
    assert sentence.count(".") == 1 and sentence.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence + "\n")


if __name__ == "__main__":
    main()
