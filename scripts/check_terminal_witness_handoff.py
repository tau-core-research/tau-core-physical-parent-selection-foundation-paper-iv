#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads(
    (ROOT / "data/derived/terminal_witness_handoff.json").read_text()
)

j_primary = sp.Matrix([[1, 0], [0, 1], [0, 0]])
p_primary = j_primary * (j_primary.T * j_primary).inv() * j_primary.T
j_redundant = sp.Matrix([1, 1, 0])
j_novel = sp.Matrix([0, 0, 1])
d_redundant = (sp.eye(3) - p_primary) * j_redundant
d_novel = (sp.eye(3) - p_primary) * j_novel
ell = sp.Matrix([[0, 0, 1]])

assert d_redundant == sp.zeros(3, 1)
assert d_novel == j_novel
assert ell * j_primary == sp.zeros(1, 2)
assert ell.dot(j_novel) == 1
assert data["redundant_rich_increment"] == 0
assert data["novel_rich_increment"] == 1
print("TERMINAL_WITNESS_HANDOFF_PASS primary_rank=2 redundant_increment=0 novel_increment=1")
