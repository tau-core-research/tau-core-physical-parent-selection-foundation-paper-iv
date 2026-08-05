import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_files_exist():
    for rel in [
        "paperIV_submission_source/main.tex",
        "paperIV_submission_source/main.pdf",
        "figures/fig_parent_selection_fork.pdf",
        "figures/fig_signature_spine.pdf",
        "data/derived/selection_ledger.json",
        "data/derived/mvp_source_signature.json",
        "data/derived/w2_variational_certificate_audit.json",
        "arxiv_submission_source.zip",
    ]:
        assert (ROOT / rel).exists(), rel


def test_claim_ledger_boundaries():
    ledger = json.loads((ROOT / "data/derived/selection_ledger.json").read_text())
    assert ledger["results"]["joint_split_countermodel"] == "proved"
    assert ledger["results"]["deduplicated_mvp_source_signature"] == "frozen_audit"
    assert (
        ledger["results"]["operational_validation_separated_from_parent_selection"]
        == "frozen_type_separation"
    )
    assert ledger["results"]["physical_parent_selects_full_gamma_mvp"] == "open"


def test_manuscript_markers():
    tex = (ROOT / "paperIV_submission_source/main.tex").read_text()
    assert "Physical Parent Selection for a Common Tau Completion" in tex
    assert "Nature-level selection remains open" in tex
    assert "fig_parent_selection_fork.pdf" in tex
    assert "fig_signature_spine.pdf" in tex


def test_deduplicated_signature():
    data = json.loads((ROOT / "data/derived/mvp_source_signature.json").read_text())
    assert len(data["source_blocks"]) == 8
    assert "tau_hold" in data["operational_not_parent_selection"]
    owned = [item for block in data["source_blocks"] for item in block["owns"]]
    assert len(owned) == len(set(owned))


def test_w2_certificate_audit():
    data = json.loads(
        (ROOT / "data/derived/w2_variational_certificate_audit.json").read_text()
    )
    assert data["w2_verdict"] == "closed_conditionally_not_nature_selected"
    assert "certificate_equals_body_action_derivative" in data["derived"]
    assert "nature_selects_gamma_mvp" in data["not_derived"]


def test_arxiv_archive_is_source_only():
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as zf:
        names = zf.namelist()
    assert "main.tex" in names
    assert "figures/fig_parent_selection_fork.pdf" in names
    assert "main.pdf" not in names
