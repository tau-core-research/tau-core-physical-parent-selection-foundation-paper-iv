#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/algebraic_exchange_absorption.json").read_text())
M, W, a, b, q = sp.symbols("M W a b q", nonzero=True, real=True)
potential = sp.Rational(1, 2) * a * M**2 + b * M * W + sp.Rational(1, 2) * q * W**2
w_star = sp.solve(sp.diff(potential, W), W)[0]
v_eff = sp.factor(potential.subs(W, w_star))
h_eff = sp.factor(sp.diff(v_eff, M, 2))
assert sp.simplify(w_star + b * M / q) == 0
assert sp.simplify(v_eff - sp.Rational(1, 2) * (a - b**2 / q) * M**2) == 0
assert sp.simplify(h_eff - (a - b**2 / q)) == 0
assert len(data["independent_rich_terminal_requires"]) == 3
print("ALGEBRAIC_EXCHANGE_ABSORPTION_PASS Wstar=-bM/q Heff=a-b^2/q novelty=0")
