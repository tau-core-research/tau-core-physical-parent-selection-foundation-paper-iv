#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
signature = json.loads((ROOT / "data/derived/mvp_source_signature.json").read_text())
audit = json.loads((ROOT / "data/derived/pbd_source_signature_audit.json").read_text())

blocks = signature["source_blocks"]
owned = [item for block in blocks for item in block["owns"]]
for forbidden in [
    "W_derivative_principal_symbol",
    "W_branch_label",
    "W_topological_label",
    "W_terminal_separator",
]:
    assert forbidden not in owned
assert len(blocks) == audit["frozen_blocks"] == 8
assert len(owned) == audit["owned_items"] == 35
assert set(audit["audit"]) == {"P_propagating_W", "B_branch_W", "D_descriptor_witness"}
print("PBD_SOURCE_SIGNATURE_AUDIT_PASS blocks=8 owned=35 P=absent B=absent D=absent")
