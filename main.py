"""One Word for Your Wi-Fi entry: writes a single line to entry.txt.

Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = 'Ghosted'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
