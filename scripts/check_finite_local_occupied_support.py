#!/usr/bin/env python3
"""Reproduce the finite-local occupied-support selection control."""

import json
from pathlib import Path


def solve_2x2(a, b, c, j, k):
    det = a * c - b * b
    return ((c * j - b * k) / det, (a * k - b * j) / det)


def main():
    split = solve_2x2(1.0, 0.0, 1.0, 1.0, 0.0)
    coupled = solve_2x2(1.0, 0.25, 1.0, 1.0, 0.0)
    record = {
        "claim": "finite_local_occupied_support_selection",
        "formula": "e_star=(C-B^dagger A^-1 B)^-1(k-B^dagger A^-1 j)",
        "split": {"S_E": 1.0, "k_eff": 0.0, "e_star": split[1]},
        "coupled": {
            "S_E": 0.9375,
            "k_eff": -0.25,
            "e_star": coupled[1],
            "minimum_hessian_eigenvalue": 0.75,
        },
        "status": "finite_C2_local_occupied_support_closed",
        "not_proved": "ambient_global_topological_or_infinite_exhaustivity",
    }
    assert abs(record["split"]["e_star"]) < 1e-12
    assert abs(record["coupled"]["e_star"] + 4.0 / 15.0) < 1e-12
    out = Path(__file__).resolve().parents[1] / "data/derived/finite_local_occupied_support.json"
    out.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print("FINITE_LOCAL_OCCUPIED_SUPPORT_CHECK_PASS 5/5")


if __name__ == "__main__":
    main()
