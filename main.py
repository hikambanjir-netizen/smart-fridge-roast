"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Entry for the make.fun bounty
"u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9".

The entry is a single roast line (at most 160 characters) about a smart
fridge. The winning angle: a fridge so "smart" it cannot open without
Wi-Fi, which turns the leftovers inside it into a cloud service.
Running this program prints the line and writes it to entry.txt.
Pure standard library, deterministic output.
"""

LINE = "My fridge won't open without Wi-Fi, so my leftovers are now cloud-based."

MAX_CHARS = 160


def main() -> None:
    """Print the roast line and write it to entry.txt (one line)."""
    assert len(LINE) <= MAX_CHARS, "roast line exceeds 160 characters"
    assert "\n" not in LINE, "roast line must be a single line"
    print(LINE)
    with open("entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
