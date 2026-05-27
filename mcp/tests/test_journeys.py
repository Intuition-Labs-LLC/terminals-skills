# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The business-decision journeys, run against the real engine.

Each journey in journeys.json is a persona + an entry point + a verb-chain + an
honest coherence judgment. These tests do NOT check that the engine produces a
particular *answer* (that is the agent's semantic job). They check the engine's
**honesty contract** on realistic, high-stakes inputs:

  - a decision that genuinely hangs together returns done = true (R=1);
  - a decision with a real trade-off returns partial, and the clashing pair
    SURFACES as a loose trio (the seam is never hidden);
  - the locked set always equals the coherent set (no stale locks);
  - no empty grid slot is ever locked;
  - the chain never upgrades a partial into a fake done;
  - everything is deterministic.

If a journey's verdict here ever drifts, either the matrix or the engine moved —
both are findings.
"""
import json
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
MCP = os.path.dirname(HERE)
SERVER = os.path.join(MCP, "server.py")
sys.path.insert(0, MCP)

from terminals_core import engine, fano  # noqa: E402

with open(os.path.join(HERE, "journeys.json"), encoding="utf-8") as fh:
    JOURNEYS = json.load(fh)["journeys"]

ALIGN, CLASH, N = 0.92, 0.12, 7


def build_coherence(spec):
    """Compact spec -> honest 7x7 matrix. base everywhere, then align groups
    strongly agree, then clash pairs strongly disagree (clash wins on overlap)."""
    base = spec.get("base", 0.6)
    c = [[1.0 if i == j else base for j in range(N)] for i in range(N)]
    for group in spec.get("align", []):
        for a in group:
            for b in group:
                if a != b:
                    c[a][b] = c[b][a] = ALIGN
    for a, b in spec.get("clash", []):
        c[a][b] = c[b][a] = CLASH
    return c


def line_containing(a, b):
    """The single Fano trio that holds both points (every pair shares exactly one)."""
    for k, ln in enumerate(fano.lines()):
        if a in ln and b in ln:
            return k
    raise AssertionError(f"no Fano line holds both {a} and {b}")


def _ids(j):
    return j["id"]


# --- per-journey: the verdict is what the honest matrix says it is ---

import pytest  # noqa: E402


@pytest.mark.parametrize("j", JOURNEYS, ids=[_ids(x) for x in JOURNEYS])
def test_journey_verdict_matches_honest_expectation(j):
    out = engine.converge(j["ideas"], build_coherence(j["coherence"]))
    assert out["witness"]["verdict"] == j["expect"], (
        f"{j['id']}: expected {j['expect']}, engine said {out['witness']['verdict']}"
    )
    if j["expect"] == "R=1":
        assert out["R"] == 1.0
        assert len(out["witness"]["incoherent"]) == 0
    else:
        assert out["R"] < 1.0
        assert len(out["witness"]["incoherent"]) > 0


@pytest.mark.parametrize("j", JOURNEYS, ids=[_ids(x) for x in JOURNEYS])
def test_journey_seam_is_surfaced_not_hidden(j):
    """For a partial decision, the clash that makes it partial MUST appear as a
    loose trio. A tool that buried the trade-off would be lying."""
    if j["expect"] != "partial" or not j.get("seam"):
        return
    out = engine.converge(j["ideas"], build_coherence(j["coherence"]))
    loose = {w["line"] for w in out["witness"]["incoherent"]}
    a, b = j["seam"]
    assert line_containing(a, b) in loose, (
        f"{j['id']}: the seam {j['ideas'][a]!r} vs {j['ideas'][b]!r} was not surfaced"
    )


@pytest.mark.parametrize("j", JOURNEYS, ids=[_ids(x) for x in JOURNEYS])
def test_journey_locked_equals_coherent_and_no_empty(j):
    out = engine.converge(j["ideas"], build_coherence(j["coherence"]))
    kept = {tuple(w["points"]) for w in out["kept"]}
    coherent = {tuple(w["points"]) for w in out["witness"]["coherent_lines"]}
    assert kept == coherent  # the shown locks are exactly the verdict's locks
    for w in out["kept"]:
        assert not any(str(x).startswith("(empty") for x in w["ideas"])


@pytest.mark.parametrize("j", JOURNEYS, ids=[_ids(x) for x in JOURNEYS])
def test_journey_readouts_are_sane(j):
    out = engine.converge(j["ideas"], build_coherence(j["coherence"]))
    assert 0.0 <= out["R"] <= 1.0
    assert 0.0 <= out["phi"] <= 1.0 and math.isfinite(out["phi"])
    assert 0.0 <= out["order_parameter"] <= 1.0


@pytest.mark.parametrize("j", JOURNEYS, ids=[_ids(x) for x in JOURNEYS])
def test_journey_is_deterministic(j):
    c = build_coherence(j["coherence"])
    a = engine.converge(j["ideas"], c)
    b = engine.converge(j["ideas"], c)
    assert a["phi_trace"] == b["phi_trace"]
    assert a["witness"]["verdict"] == b["witness"]["verdict"]


# --- the chain (abstractive loop): recommend must never fake done ---

@pytest.mark.parametrize("j", JOURNEYS, ids=[_ids(x) for x in JOURNEYS])
def test_chain_recommend_never_upgrades_partial(j):
    """recommend chains converge -> optimize. On a partial decision it must come
    back partial (and only optimize when it genuinely locked)."""
    rec = engine.recommend(j["ideas"], build_coherence(j["coherence"]))
    assert rec["witness"]["verdict"] == j["expect"]
    if j["expect"] == "partial":
        assert rec["optimized"] is False
        assert len(rec["witness"]["incoherent"]) > 0
    else:
        assert rec["optimized"] is True
        assert rec["pick"] is not None


# --- the spread is honest: not all-done, not all-partial ---

def test_journey_set_spans_both_verdicts():
    verdicts = [j["expect"] for j in JOURNEYS]
    assert "R=1" in verdicts and "partial" in verdicts
    assert all(v in ("R=1", "partial") for v in verdicts)


def test_every_journey_is_well_formed():
    for j in JOURNEYS:
        assert len(j["ideas"]) == 7, f"{j['id']} must lay 7 points on the grid"
        assert j["entry"] in {"explore", "converge", "optimize", "recommend", "frame"}
        assert j["chain"][-1] in {"converge", "optimize", "recommend"}
        assert j["entry"] == j["chain"][0]


# --- the product surface (MCP server) carries a full journey end-to-end ---

def _run_server(messages):
    proc = subprocess.run(
        [sys.executable, SERVER],
        input="\n".join(json.dumps(m) for m in messages) + "\n",
        capture_output=True, text=True, timeout=90,
    )
    out = [json.loads(line) for line in proc.stdout.splitlines() if line.strip()]
    return {m.get("id"): m for m in out if "id" in m}


def test_frame_journey_runs_through_the_real_server():
    """The investor data-room journey, driven through server.py over stdio: frame
    the room, get the honest partial back as a real MCP tool result."""
    inv = next(j for j in JOURNEYS if j["id"] == "investor-dataroom")
    by_id = _run_server([
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                    "clientInfo": {"name": "test", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/call",
         "params": {"name": "frame",
                    "arguments": {"items": inv["ideas"],
                                  "coherence": build_coherence(inv["coherence"])}}},
    ])
    payload = json.loads(by_id[2]["result"]["content"][0]["text"])
    assert "framing" in payload
    assert payload["witness"]["verdict"] == "partial"
    assert len(payload["witness"]["incoherent"]) > 0
