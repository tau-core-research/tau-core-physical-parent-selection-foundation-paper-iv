#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/nonabsorbed_rich_trichotomy.json").read_text())
W, v = sp.symbols("W v", positive=True, real=True)
potential = sp.Rational(1, 4) * (W**2 - v**2) ** 2
stationary = sp.factor(sp.diff(potential, W))
roots = sp.solve(stationary, W)
# W is declared positive by SymPy, so audit the two signed roots directly.
hessian = sp.diff(potential, W, 2)
assert sp.simplify(stationary.subs(W, v)) == 0
assert sp.simplify(stationary.subs(W, -v)) == 0
assert sp.simplify(hessian.subs(W, v) - 2 * v**2) == 0
assert sp.simplify(hessian.subs(W, -v) - 2 * v**2) == 0
assert set(data["nonabsorbed_cases"]) == {"P", "B", "D"}
print("NONABSORBED_RICH_TRICHOTOMY_PASS cases=P,B,D double_well_stable_branches=2")
