#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads(
    (ROOT / "data/derived/w2_variational_certificate_audit.json").read_text()
)

premises = set(data["premises"])
required = {
    "body_first_freeze",
    "differentiable_body_action",
    "nondegenerate_quotient_pairing",
    "complete_variational_response_identity",
    "no_hidden_response_covector",
}
assert required <= premises
assert data["w2_verdict"] == "closed_conditionally_not_nature_selected"
assert "nature_selects_gamma_mvp" in data["not_derived"]
assert data["necessity_countermodel"]["hidden_covector"] == "b_nonzero"
print("W2_VARIATIONAL_CERTIFICATE_PASS premises=5 verdict=conditional")
