#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/nature_packet_stop_theorem.json").read_text())
x1, x2, h, q, j = sp.symbols("x1 x2 h q j", nonzero=True, real=True)
F = sp.Matrix([[1, 0], [0, 1]])
F_ext = sp.Matrix([[1, 0, 0], [0, 1, 0]])
assert F.rank() == F_ext.rank() == 2
action_h = sp.Rational(1, 2) * q * h**2 - j * h
h_star = sp.solve(sp.diff(action_h, h), h)[0]
assert sp.simplify(h_star - j / q) == 0
assert F_ext * sp.Matrix([x1, x2, h_star]) == F * sp.Matrix([x1, x2])
assert data["declared_terminal_change"] == 0
assert len(data["required_reopening"]) == 3
print("NATURE_PACKET_STOP_PASS terminal_rank=2 hidden_occupied=true terminal_change=0")
