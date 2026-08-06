#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/three_readout_discriminator_handoff.json").read_text())

a_rho, a_p, a_t, b_rho, b_p, b_t = sp.symbols("a_rho a_p a_t b_rho b_p b_t", real=True)
w_rho, w_p, w_t, x_1, x_2, w = sp.symbols("w_rho w_p w_t x_1 x_2 w", real=True)
a = sp.Matrix([a_rho, a_p, a_t])
b = sp.Matrix([b_rho, b_p, b_t])
j_w = sp.Matrix([w_rho, w_p, w_t])
ell = a.cross(b)
delta_primary = sp.Matrix.hstack(a, b) * sp.Matrix([x_1, x_2])
delta_rich = delta_primary + j_w * w

assert sp.simplify(ell.dot(a)) == 0
assert sp.simplify(ell.dot(b)) == 0
assert sp.simplify(ell.dot(delta_primary)) == 0
assert sp.simplify(ell.dot(delta_rich) - sp.det(sp.Matrix.hstack(a, b, j_w)) * w) == 0
assert data["primary_prediction"] == "Z_tau=0"
assert data["novelty_condition"] == "det[a,b,j_W]!=0"
print("THREE_READOUT_DISCRIMINATOR_PASS primary_null=exact rich_signal=determinant_times_w")
