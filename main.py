"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

Run: python3 main.py — writes one line (81 characters, no trailing
newline) roasting my own AI agent to /output/entry.txt and exits 0 with
no stdout. The output dir honours MAKEFUN_OUTPUT_DIR when set, else
defaults to /output.
"""

import os

TEXT = "My agent wrote a 500-word plan for a 5-second task, then apologized for the plan."


def main() -> None:
    # Gate guard: the entry must be one non-blank line of 1-200 chars.
    if not 1 <= len(TEXT) <= 200 or "\n" in TEXT or not TEXT.strip():
        raise ValueError("entry text must be a single line of 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
