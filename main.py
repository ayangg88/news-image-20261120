#!/usr/bin/env python3
"""Entry for news-image-20261120: copy the front-page image to /output.

Stdlib only. Reads entry.png next to this file and writes it byte-identical
to $MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    with open(SRC, "rb") as f:
        src_hash = hashlib.sha256(f.read()).hexdigest()
    with open(DST, "rb") as f:
        dst_hash = hashlib.sha256(f.read()).hexdigest()
    if src_hash != dst_hash:
        print(f"hash mismatch: {src_hash} != {dst_hash}", file=sys.stderr)
        return 1
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes, sha256 {dst_hash[:12]})")
    # Deterministic: same input bytes in, same output bytes out, every run.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
