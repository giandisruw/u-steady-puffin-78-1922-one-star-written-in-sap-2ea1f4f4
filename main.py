#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes the winning one-line 1-star review from a houseplant about its
human owner to /output/entry.txt. The line is a single line, 139
characters (gate: 1 to 279), chosen by a local pairwise tournament
judged against the bounty's published judge brief (see README.md for
the tournament table).
"""

import os

# Winning line (tournament winner — see README.md).
# Local tournament: 14 candidates, Swiss 4 rounds (28 games) + final,
# 58 judge calls on the Caffeine Inference router, every game played
# in both label orders. #11 led the Swiss at 2.8, #10 second at 2.65;
# the final went to #10, 0.55-0.45.
ENTRY = (
    "★☆☆☆☆ One star. My owner Googled 'why is my plant sad' while "
    "standing in my shade, then watered the rug instead. "
    "The rug is fine. I am not."
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check `line` against the kit's sealed-scorer gate, verbatim.

    competition.yaml: "/output/entry.txt is UTF-8 text of 1 to 279
    characters, not only white space". Single-line follows from the
    task itself (one line, under 280 characters). Returns the line
    unchanged; raises AssertionError on any gate violation.
    """
    assert isinstance(line, str)
    line.encode("utf-8")  # must be valid UTF-8
    assert 1 <= len(line) <= 279, f"length {len(line)} outside 1-279"
    assert line.strip(), "entry is only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    return line


def main() -> None:
    line = validate(ENTRY)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
