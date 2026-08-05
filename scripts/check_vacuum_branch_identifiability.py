#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/vacuum_branch_identifiability.json").read_text())
V, H, Vdot = sp.symbols("V H Vdot", real=True)
rho, p = V, -V
continuity = sp.simplify(Vdot + 3 * H * (rho + p))
assert continuity == Vdot
assert sp.solve(sp.Eq(continuity, 0), Vdot) == [0]
assert data["background_origin_identifiable"] is False
assert len(data["tau_specific_escape_routes"]) == 3
print("VACUUM_BRANCH_IDENTIFIABILITY_PASS separate_conservation=>Vdot=0 background=Lambda")
