# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""Regression tests for the 2026-05-27 security audit findings.

HIGH  : a deeply-nested JSON frame must not crash the stdio server.
MED   : caller-supplied optimize max_steps must be clamped (no unbounded hang).
LOW   : non-finite / out-of-range threshold must be sanitized (no NaN/Infinity leak).
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

from terminals_core import engine  # noqa: E402

HIGH = [[0.95 if i != j else 1.0 for j in range(7)] for i in range(7)]
IDEAS = [f"i{i}" for i in range(7)]


def test_recursion_bomb_does_not_crash_server():
    """A 100k-deep nested-array line raises RecursionError in json.loads; the
    server must skip it and still answer the next request."""
    bomb = "[" * 100000 + "]" * 100000
    ping = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "ping"})
    proc = subprocess.run(
        [sys.executable, SERVER], input=bomb + "\n" + ping + "\n",
        capture_output=True, text=True, timeout=60,
    )
    out = [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]
    ids = [m.get("id") for m in out if "id" in m]
    assert 1 in ids, "server did not survive a recursion-bomb frame"
    assert proc.returncode == 0


def test_optimize_clamps_max_steps():
    """max_steps=1e9 would run effectively forever unclamped; clamped it returns
    promptly. If this test hangs to the suite timeout, the clamp regressed."""
    conv = engine.converge(IDEAS, HIGH)
    res = engine.optimize(conv, max_steps=10 ** 9)
    assert "R_held" in res  # returned a real result instead of hanging


def test_nonfinite_and_out_of_range_threshold_sanitized():
    for bad in [float("nan"), float("inf"), -float("inf"), 1e999, 50, -9, "x", None]:
        res = engine.converge(IDEAS, HIGH, threshold=bad)
        t = res["threshold"]
        assert isinstance(t, float) and math.isfinite(t) and 0.0 < t <= 1.0, (bad, t)
        dumped = json.dumps(res)
        assert "NaN" not in dumped and "Infinity" not in dumped, bad


def test_optimize_normalizes_short_coherence_no_indexerror():
    """LOW audit finding: a hand-crafted converged object with a ragged/short
    coherence must not raise IndexError. optimize normalizes any matrix to 7x7
    before annealing."""
    bad = {"points": ["a"] * 7, "coherence": [[1.0]], "witness": {"verdict": "R=1"}}
    res = engine.optimize(bad)
    assert "R_held" in res  # a real result, not an IndexError


def test_hold_detects_drift_and_is_live():
    """engine.hold re-checks a prior answer against new state and reports drift.
    hold is now a live MCP tool; act stays a command/skill (host orchestration)."""
    from terminals_core import server

    prior = engine.converge(IDEAS, HIGH)  # all trios locked
    low = [[1.0 if i == j else 0.15 for j in range(7)] for i in range(7)]
    fell_apart = engine.hold(prior, IDEAS, low)
    assert fell_apart["still_holds"] is False
    assert len(fell_apart["drifted"]) > 0
    unchanged = engine.hold(prior, IDEAS, HIGH)
    assert unchanged["still_holds"] is True
    live = {t["name"] for t in server.TOOLS}
    assert live == {"explore", "converge", "optimize", "recommend", "frame", "hold"}
    assert "act" not in live  # act has no MCP tool by design
