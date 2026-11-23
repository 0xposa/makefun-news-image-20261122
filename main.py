#!/usr/bin/env python3
"""make.fun entry — news-image-20261122.

Writes the day's news poster to the output directory. The poster itself
(entry.png, committed beside this file under output/) was drawn by draw.py
with Pillow at build time; this entrypoint only copies it, using nothing
but the standard library, so it runs in the grader's stock Python image.
Deterministic: the same bytes on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "output", "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        dest = os.path.join(out_dir, "entry.png")
        shutil.copyfile(SRC, dest)
    except OSError:
        out_dir = os.path.join(HERE, "output")
        dest = os.path.join(out_dir, "entry.png")
        if os.path.abspath(dest) != os.path.abspath(SRC):
            shutil.copyfile(SRC, dest)
    size = os.path.getsize(dest)
    print(f"wrote {dest} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
