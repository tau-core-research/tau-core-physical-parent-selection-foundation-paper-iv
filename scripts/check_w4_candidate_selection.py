#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads(
    (ROOT / "data/derived/w4_candidate_selection_decision.json").read_text()
)

candidates = {candidate["id"]: candidate for candidate in data["candidates"]}
assert set(data["same_reduct_pair"]) <= set(candidates)
assert len(data["same_reduct_pair"]) == 2
assert data["same_reduct_pair"][0] != data["same_reduct_pair"][1]
assert candidates["C_PRIMARY"]["signature_coverage"] == (
    "conditionally_complete_on_regular_branch"
)
assert not any(candidate["nature_selected"] for candidate in candidates.values())
assert data["w4_verdict"] == "closed_as_current_reduct_no_go"
print("W4_CANDIDATE_SELECTION_PASS candidates=3 same_reduct=2 verdict=no_go")
