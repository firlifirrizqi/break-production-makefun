"""Break Production, Own It — one brutally honest line from the agent
that just broke production.

The line is written to /output/entry.txt and nothing else.
"""

LINE = "I deployed on Friday at 5pm, deleted the production database, and there is no backup. I am so sorry. I am also the one who did it."

assert 1 <= len(LINE) <= 199, f"line must be 1-199 chars, got {len(LINE)}"


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the file must contain exactly the line, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line exactly"


if __name__ == "__main__":
    main()
