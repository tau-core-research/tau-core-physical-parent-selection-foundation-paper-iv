import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_files_exist():
    for rel in [
        "paperIV_submission_source/main.tex",
        "paperIV_submission_source/main.pdf",
        "figures/fig_parent_selection_fork.pdf",
        "data/derived/selection_ledger.json",
        "arxiv_submission_source.zip",
    ]:
        assert (ROOT / rel).exists(), rel


def test_claim_ledger_boundaries():
    ledger = json.loads((ROOT / "data/derived/selection_ledger.json").read_text())
    assert ledger["results"]["joint_split_countermodel"] == "proved"
    assert ledger["results"]["physical_parent_selects_full_gamma_mvp"] == "open"


def test_manuscript_markers():
    tex = (ROOT / "paperIV_submission_source/main.tex").read_text()
    assert "Physical Parent Selection for a Common Tau Completion" in tex
    assert "Nature-level selection remains open" in tex
    assert "fig_parent_selection_fork.pdf" in tex


def test_arxiv_archive_is_source_only():
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as zf:
        names = zf.namelist()
    assert "main.tex" in names
    assert "figures/fig_parent_selection_fork.pdf" in names
    assert "main.pdf" not in names

