#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/rank_one_lorentz_typing.json").read_text())

def E(i, j):
    m = sp.zeros(4)
    m[i, j] = 1
    return m

# Standard real generators: three spatial rotations and three boosts.
generators = [
    E(1, 2) - E(2, 1),
    E(2, 3) - E(3, 2),
    E(3, 1) - E(1, 3),
    E(0, 1) + E(1, 0),
    E(0, 2) + E(2, 0),
    E(0, 3) + E(3, 0),
]
commutators = []
for a in generators:
    for b in generators:
        c = a * b - b * a
        commutators.append(sp.Matrix(c).reshape(16, 1))

commutator_rank = sp.Matrix.hstack(*commutators).rank()
generator_rank = sp.Matrix.hstack(
    *[sp.Matrix(g).reshape(16, 1) for g in generators]
).rank()
assert generator_rank == 6
assert commutator_rank == 6
assert data["connected_group_type"] == "Lorentz_scalar"
print("RANK_ONE_LORENTZ_TYPING_PASS lie_rank=6 commutator_rank=6 type=scalar")
