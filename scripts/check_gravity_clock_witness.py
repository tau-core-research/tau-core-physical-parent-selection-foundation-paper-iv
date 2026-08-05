#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/gravity_clock_witness.json").read_text())

g_b, t_b, g_w, t_w, x, w = sp.symbols("g_B t_B g_W t_W x w")
j = sp.Matrix([[g_b, g_w], [t_b, t_w]])
delta = sp.factor(j.det())
delta_g = g_b * x + g_w * w
delta_t = t_b * x + t_w * w
z = sp.factor(t_b * delta_g - g_b * delta_t)

assert delta == g_b * t_w - t_b * g_w
assert sp.simplify(z + delta * w) == 0
assert sp.factor(z.subs(w, 0)) == 0
assert data["novelty_determinant"] == "Delta_GT=g_B*t_W-t_B*g_W"
print("GRAVITY_CLOCK_WITNESS_PASS primary_rank=1 rich_rank=2_iff_Delta_GT_nonzero")
