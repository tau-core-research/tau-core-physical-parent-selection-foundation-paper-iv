#!/usr/bin/env python3
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "paperIV_submission_source"
OUT = ROOT / "arxiv_submission_source.zip"

with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(SRC.rglob("*")):
        if path.is_file() and path.suffix not in {".pdf", ".aux", ".log"}:
            zf.write(path, path.relative_to(SRC))
    for path in sorted((SRC / "figures").glob("*.pdf")):
        zf.write(path, path.relative_to(SRC))
print("WROTE", OUT)

