#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/ward_pressure_witness.json").read_text())

rho_b, rho_w, w_b, w_w, x, w = sp.symbols("rho_B rho_W w_B w_W x w")
p_b = w_b * rho_b
p_w = w_w * rho_w
delta = sp.factor(rho_b * p_w - p_b * rho_w)
delta_rho = rho_b * x + rho_w * w
delta_p = p_b * x + p_w * w
z = sp.factor(rho_b * delta_p - p_b * delta_rho)

assert sp.simplify(delta - rho_b * rho_w * (w_w - w_b)) == 0
assert sp.simplify(z - delta * w) == 0
assert sp.simplify(delta.subs(w_w, w_b)) == 0
assert data["ward_aligned_pair"]["verdict"] == "Delta_GT_identically_zero"
print("WARD_PRESSURE_WITNESS_PASS ward_pair_rank=1 pressure_novel_iff_wW_ne_wB")
