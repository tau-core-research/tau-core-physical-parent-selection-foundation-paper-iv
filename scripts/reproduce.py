#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(*args):
    print("$", " ".join(map(str, args)))
    subprocess.run(args, cwd=ROOT, check=True)


run(sys.executable, "scripts/build_figures.py")
run(sys.executable, "scripts/check_selection_signature.py")
run(sys.executable, "scripts/check_w2_variational_certificate.py")
run(sys.executable, "scripts/check_w3_once_counted_ledger.py")
run(sys.executable, "scripts/check_w4_candidate_selection.py")
run("tectonic", "paperIV_submission_source/main.tex")
run(sys.executable, "scripts/build_arxiv_source.py")
run(sys.executable, "-m", "pytest", "-q")
print("FOUNDATION_PAPER_IV_PREPARATION_REPRODUCTION_COMPLETE")
