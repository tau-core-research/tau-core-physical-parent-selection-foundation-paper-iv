#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data/derived/mvp_source_signature.json").read_text())
blocks = data["source_blocks"]
ids = [block["id"] for block in blocks]
assert len(ids) == len(set(ids)), "duplicate source block id"
known = set(ids)
graph = {block["id"]: block["depends_on"] for block in blocks}
for block in blocks:
    assert set(block["depends_on"]) <= known, f"unknown dependency in {block['id']}"

visiting, visited = set(), set()
def visit(node):
    assert node not in visiting, "cyclic source dependency"
    if node in visited:
        return
    visiting.add(node)
    for parent in graph[node]:
        visit(parent)
    visiting.remove(node)
    visited.add(node)
for node in ids:
    visit(node)

owned = {}
for block in blocks:
    for item in block["owns"]:
        assert item not in owned, f"independent ownership duplicated: {item}"
        owned[item] = block["id"]
assert len(blocks) == 8
assert "tau_hold" in data["operational_not_parent_selection"]
assert "physical_ownership_of_S6_METRIC" in data["open_selection_core"]
print(f"MVP_SOURCE_SIGNATURE_PASS blocks={len(blocks)} owned={len(owned)}")
