#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/stress_type_branch_decision.json").read_text())

q, J, W, rho_b, rho_w = sp.symbols("q J W rho_B rho_W", positive=True)
action = sp.Rational(1, 2) * q * W**2 - J * W
w_star = sp.solve(sp.diff(action, W), W)[0]
hessian = sp.diff(action, W, 2)

assert sp.simplify(w_star - J / q) == 0
assert sp.simplify(hessian - q) == 0
delta_dust_volume = sp.factor(rho_b * (-rho_w) - 0 * rho_w)
assert sp.simplify(delta_dust_volume + rho_b * rho_w) == 0
assert data["covariant_controls"]["minimal_volume_lift"]["w_W"] == -1
assert data["covariant_controls"]["conserved_flow_lift"]["w_W"] == 0
assert data["verdict"].startswith("stress_type_not_selected")
print("STRESS_TYPE_BRANCH_PASS same_fiber_law_distinct_EOS conditional_Delta=-rhoB*rhoW")
