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
        "data/derived/w3_once_counted_ledger_import.json",
        "data/derived/w4_candidate_selection_decision.json",
        "data/derived/carrier_category_decision.json",
        "data/derived/terminal_witness_handoff.json",
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
    assert ledger["results"]["frozen_mvp_carrier_category_selects_primary_completion"] == "proved"
    assert ledger["results"]["nature_selects_minimum_over_rank_novel_carrier_categories"] == "open"


def test_manuscript_markers():
    tex = (ROOT / "paperIV_submission_source/main.tex").read_text()
    assert "Physical Parent Selection for a Common Tau Completion" in tex
    assert "Nature-level selection remains open" in tex
    assert "fig_parent_selection_fork.pdf" in tex
    assert "fig_signature_spine.pdf" in tex
    assert "Carrier-category dichotomy" in tex
    assert "Complete-terminal witness" in tex


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


def test_w3_ledger_import():
    data = json.loads(
        (ROOT / "data/derived/w3_once_counted_ledger_import.json").read_text()
    )
    assert data["rerun_checks"]["gamma_mvp_once_counted_ledger"] == "10/10"
    assert data["single_remaining_physical_gap"] == (
        "one_base_seed_parent_fills_and_occupies_the_complete_ledger"
    )


def test_w4_candidate_decision():
    data = json.loads(
        (ROOT / "data/derived/w4_candidate_selection_decision.json").read_text()
    )
    assert data["w4_verdict"] == "closed_as_current_reduct_no_go"
    assert data["selected_working_candidate"] == "C_PRIMARY"
    assert len(data["same_reduct_pair"]) == 2


def test_carrier_category_decision():
    data = json.loads(
        (ROOT / "data/derived/carrier_category_decision.json").read_text()
    )
    assert data["descriptor_blocks"] == 8
    assert data["mvp_verdict"].startswith("primary_source_irredundant")
    assert data["energy_sharing_status"] == (
        "excluded_inside_mvp_but_admissible_as_rank_novel_enrichment"
    )


def test_terminal_witness_handoff():
    data = json.loads(
        (ROOT / "data/derived/terminal_witness_handoff.json").read_text()
    )
    assert data["redundant_rich_increment"] == 0
    assert data["novel_rich_increment"] == 1
    assert len(data["preferred_terminal_stack"]) == 4


def test_arxiv_archive_is_source_only():
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as zf:
        names = zf.namelist()
    assert "main.tex" in names
    assert "figures/fig_parent_selection_fork.pdf" in names
    assert "main.pdf" not in names
