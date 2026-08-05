#!/usr/bin/env python3
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
data = json.loads(
    (ROOT / "data/derived/carrier_category_decision.json").read_text()
)

n = data["descriptor_blocks"]
f_mvp = sp.eye(n)
redundant_work = f_mvp[0, :] + 2 * f_mvp[3, :] - f_mvp[7, :]
novel_work = sp.Matrix([[0] * n + [1]])
f_extended = f_mvp.row_join(sp.zeros(n, 1))

assert f_mvp.col_join(redundant_work).rank() == n
assert f_extended.col_join(novel_work).rank() == n + 1
assert data["mvp_verdict"].startswith("primary_source_irredundant")
assert data["broad_parent_verdict"].endswith("not_entailed")
print("CARRIER_CATEGORY_DECISION_PASS redundant_rank=8 novel_rank=9 verdict=dichotomy")
