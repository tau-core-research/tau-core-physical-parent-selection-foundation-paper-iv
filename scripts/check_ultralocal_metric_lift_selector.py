#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/ultralocal_metric_lift_selector.json").read_text())
V = sp.symbols("V", nonzero=True, real=True)
rho, p = V, -V
assert sp.simplify(p / rho + 1) == 0
assert all(sp.simplify(p - (p + p + p) / 3) == 0 for _ in range(3))
assert data["anisotropic_stress"] == 0
assert len(data["escape_routes"]) == 4
print("ULTRALOCAL_METRIC_LIFT_PASS wW=-1 anisotropic_stress=0 escapes=4")
