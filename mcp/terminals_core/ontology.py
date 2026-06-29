# SPDX-License-Identifier: CC-BY-4.0
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""ontology — the Terminals ontology surface for the MCP (one atom, many projections).

Reads the canonical machine-readable manifest (terminals-skills/ontology/terminals-ontology.json)
and serves it whole or filtered. The SAME ontology the /ontology site renders and the skills
reference — one source, many projections. Zero-dependency, degrade-closed.
"""
from __future__ import annotations

import json
import os
from typing import Any, Dict, Optional

_HERE = os.path.dirname(os.path.abspath(__file__))
# mcp/terminals_core/ -> mcp/ -> terminals-skills/ -> ontology/terminals-ontology.json
_MANIFEST = os.path.normpath(os.path.join(_HERE, "..", "..", "ontology", "terminals-ontology.json"))


def _load() -> Dict[str, Any]:
    try:
        with open(_MANIFEST, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:  # noqa: BLE001 — total: a missing manifest never raises
        return {"error": "ontology manifest unavailable", "detail": str(e), "path": _MANIFEST}


def read(query: Optional[str] = None) -> Dict[str, Any]:
    """The ontology, optionally filtered by `query`: a SECTION (atom | ladder | functions |
    objects) or a named object/function (e.g. 'Recipe', 'leap'). No query → the whole manifest."""
    onto = _load()
    if "error" in onto or not query:
        return onto
    q = str(query).strip().lower()
    if q in ("atom", "ladder", "functions", "constructed_objects", "objects"):
        key = "constructed_objects" if q == "objects" else q
        return {key: onto.get(key)}
    for o in onto.get("constructed_objects", []):
        if str(o.get("object", "")).lower() == q:
            return {"object": o}
    for fn in onto.get("functions", []):
        if str(fn.get("name", "")).lower() == q:
            return {"function": fn}
    return {"one_line": onto.get("one_line"), "atom": onto.get("atom"),
            "hint": f"no match for {query!r}; try a section (atom|ladder|functions|objects) or a name"}
