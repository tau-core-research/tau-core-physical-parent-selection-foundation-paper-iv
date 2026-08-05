#!/usr/bin/env python3
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
data = json.loads(
    (ROOT / "data/derived/w3_once_counted_ledger_import.json").read_text()
)

assert data["rerun_checks"] == {
    "gamma_mvp_once_counted_ledger": "10/10",
    "stagewise_joint_postbody_relation": "33/33",
    "cross_lane_source_inventory": "37/37",
    "primitive_hessian_construction": "26/26",
}

# A zero-residual squared relation has Hessian J^T J.
J = np.array([[1.0, -2.0], [0.5, 3.0]])
H = J.T @ J
assert np.allclose(H, np.array([[1.25, -0.5], [-0.5, 13.0]]))

# Exact elimination of the second block gives the Schur complement.
kx, ky, mix = 5.0, 4.0, 1.5
schur = kx - mix**2 / ky
assert np.isclose(schur, 4.4375)

# A positive-semidefinite additive block with zero diagonals cannot carry a
# nonzero pure cross term: [[0,c],[c,0]] has eigenvalues +/-|c|.
c = 0.75
assert np.allclose(np.linalg.eigvalsh(np.array([[0.0, c], [c, 0.0]])), [-c, c])

assert data["w3_verdict"] == (
    "closed_as_structural_audit_not_as_microscopic_nature_selection"
)
print("W3_ONCE_COUNTED_LEDGER_PASS imported=106 structural=10")
