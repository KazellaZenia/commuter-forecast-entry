"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast for the invented city of
Mizzlewick to /output/entry.txt. Pure stdlib, no network.
"""

import os

ENTRY = (
    "Mizzlewick: light rain, heavy sighs, and the 7:52 to Nowhere "
    "Central delayed by leaves, as it has been every autumn since 1987."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
