"""One-Line Laugh Sprint entry.

Writes one original funny line about everyday life to entry.txt.
Standard library only; deterministic: every run writes the same bytes.
"""

import os

LINE = "My bank app sent me a spending summary: apparently I've been investing heavily in snacks and regret."

# The gate requires 1 to 200 characters of non-whitespace text.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 characters"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
