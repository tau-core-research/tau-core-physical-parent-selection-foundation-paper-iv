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
        "data/derived/three_readout_discriminator_handoff.json",
        "data/derived/gravity_clock_witness.json",
        "data/derived/ward_pressure_witness.json",
        "data/derived/stress_type_branch_decision.json",
        "data/derived/ultralocal_metric_lift_selector.json",
        "data/derived/rank_one_lorentz_typing.json",
        "data/derived/vacuum_branch_identifiability.json",
        "data/derived/algebraic_exchange_absorption.json",
        "data/derived/nonabsorbed_rich_trichotomy.json",
        "data/derived/pbd_source_signature_audit.json",
        "data/derived/nature_packet_stop_theorem.json",
        "data/derived/finite_local_occupied_support.json",
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
    assert "Physical Parent-Law Realization for a Common Tau Completion" in tex
    assert "Atemporal parent-realization terminology" in tex
    assert "Unrestricted parent-law realization and physical occupation remain open" in tex
    assert "fig_parent_selection_fork.pdf" in tex
    assert "fig_signature_spine.pdf" in tex
    assert "Carrier-category dichotomy" in tex
    assert "Complete-terminal witness" in tex
    assert "Three-readout determinant handoff" in tex
    assert "Gravity--clock contrast" in tex
    assert "Ward-aligned no-go" in tex
    assert "Stress-type nonselection" in tex
    assert "Ultralocal scalar lift selector" in tex
    assert "Rank-one Lorentz typing" in tex
    assert "Vacuum-branch identifiability no-go" in tex
    assert "Algebraic exchange absorption" in tex
    assert "Nonabsorbed rich trichotomy" in tex
    assert "P/B/D source-signature audit" in tex
    assert "Ambient-source exhaustivity stop theorem" in tex
    assert "Common-source primitive-readout assembly" in tex
    assert "eq:mopr-source-assembly" in tex
    assert "Cyclic-source occupation" in tex
    assert "eq:full-source-occupation" in tex
    assert "eq:mvp-actual-occupation" in tex
    assert "projective/body connector" in tex
    assert "eq:projective-body-scale-import" in tex


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


def test_gravity_clock_witness():
    data = json.loads(
        (ROOT / "data/derived/gravity_clock_witness.json").read_text()
    )
    assert data["primary_response"] == "Z_GT=0"
    assert data["rich_response"] == "Z_GT=-Delta_GT*w"


def test_three_readout_discriminator_handoff():
    data = json.loads(
        (ROOT / "data/derived/three_readout_discriminator_handoff.json").read_text()
    )
    assert data["primary_prediction"] == "Z_tau=0"
    assert data["novelty_condition"] == "det[a,b,j_W]!=0"
    assert len(data["terminal_stack"]) == 3


def test_ward_pressure_witness():
    data = json.loads(
        (ROOT / "data/derived/ward_pressure_witness.json").read_text()
    )
    assert data["ward_aligned_pair"]["verdict"] == "Delta_GT_identically_zero"
    assert data["first_viable_pair"] == ["energy_density_rho", "spatial_pressure_p"]


def test_stress_type_branch_decision():
    data = json.loads(
        (ROOT / "data/derived/stress_type_branch_decision.json").read_text()
    )
    assert data["covariant_controls"]["minimal_volume_lift"]["w_W"] == -1
    assert data["covariant_controls"]["conserved_flow_lift"]["w_W"] == 0
    assert data["verdict"].startswith("stress_type_not_selected")


def test_ultralocal_metric_lift_selector():
    data = json.loads(
        (ROOT / "data/derived/ultralocal_metric_lift_selector.json").read_text()
    )
    assert data["equation_of_state_on_constant_occupied_branch"] == "w_W=-1"
    assert data["anisotropic_stress"] == 0
    assert len(data["escape_routes"]) == 4


def test_rank_one_lorentz_typing():
    data = json.loads(
        (ROOT / "data/derived/rank_one_lorentz_typing.json").read_text()
    )
    assert data["connected_group_type"] == "Lorentz_scalar"
    assert data["stress_consequence_with_ultralocal_selector"].startswith("w_W=-1")


def test_vacuum_branch_identifiability():
    data = json.loads(
        (ROOT / "data/derived/vacuum_branch_identifiability.json").read_text()
    )
    assert data["background_origin_identifiable"] is False
    assert data["flrw_equivalent"].endswith("dot_V=0")
    assert len(data["tau_specific_escape_routes"]) == 3


def test_algebraic_exchange_absorption():
    data = json.loads(
        (ROOT / "data/derived/algebraic_exchange_absorption.json").read_text()
    )
    assert data["effective_body_hessian"] == "a-b^2/q"
    assert data["terminal_status_without_independent_W_access"] == "absorbed_into_complete_body"
    assert len(data["independent_rich_terminal_requires"]) == 3


def test_nonabsorbed_rich_trichotomy():
    data = json.loads(
        (ROOT / "data/derived/nonabsorbed_rich_trichotomy.json").read_text()
    )
    assert set(data["nonabsorbed_cases"]) == {"P", "B", "D"}
    assert data["all_cases_enlarge"].startswith("complete_body")


def test_pbd_source_signature_audit():
    data = json.loads((ROOT / "data/derived/pbd_source_signature_audit.json").read_text())
    assert data["frozen_blocks"] == 8
    assert data["owned_items"] == 35
    assert all(value.startswith("absent") for value in data["audit"].values())


def test_nature_packet_stop_theorem():
    data = json.loads((ROOT / "data/derived/nature_packet_stop_theorem.json").read_text())
    assert data["declared_terminal_change"] == 0
    assert set(data["dichotomy"]) == {"true_null", "incomplete_descriptor"}
    assert len(data["required_reopening"]) == 3


def test_finite_local_occupied_support():
    data = json.loads((ROOT / "data/derived/finite_local_occupied_support.json").read_text())
    assert data["split"]["e_star"] == 0.0
    assert abs(data["coupled"]["e_star"] + 4.0 / 15.0) < 1e-12
    assert data["status"] == "finite_C2_local_occupied_support_closed"


def test_arxiv_archive_is_source_only():
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as zf:
        names = zf.namelist()
    assert "main.tex" in names
    assert "figures/fig_parent_selection_fork.pdf" in names
    assert "main.pdf" not in names


def test_m4_metrological_boundary():
    text = (ROOT / "paperIV_submission_source/main.tex").read_text()
    normalized = " ".join(text.split())
    assert "eq:paperiv-m4-metrological-orbit" in text
    assert "does not need to select that representative" in normalized
    assert "dimensionless coupling normalizations remain" in normalized
