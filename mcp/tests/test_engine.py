# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The five verbs: done=true on coherent input, partial on incoherent, the
witness rides along, optimize holds done=true, and everything is deterministic."""
from terminals_core import engine

SEVEN = [f"idea{i}" for i in range(7)]
HIGH = [[0.95 if i != j else 1.0 for j in range(7)] for i in range(7)]
LOW = [[1.0 if i == j else 0.15 for j in range(7)] for i in range(7)]


def test_converge_coherent_is_done():
    out = engine.converge(SEVEN, HIGH)
    assert out["witness"]["verdict"] == "R=1"
    assert out["R"] == 1.0
    assert out["order_parameter"] > 0.85
    assert len(out["kept"]) == 7
    assert out["coherence_provided"] is True


def test_converge_incoherent_is_partial():
    out = engine.converge(SEVEN, LOW)
    assert out["witness"]["verdict"] == "partial"
    assert out["R"] < 1.0
    assert len(out["witness"]["incoherent"]) > 0


def test_witness_has_the_shape():
    w = engine.converge(SEVEN, HIGH)["witness"]
    assert set(["coherent_lines", "incoherent", "verdict", "rationale", "coverage"]).issubset(w)
    assert w["coverage"]["lost"] == 0
    assert w["coverage"]["double_counted"] == 0


def test_determinism_same_inputs_same_output():
    a = engine.converge(SEVEN, HIGH)
    b = engine.converge(SEVEN, HIGH)
    assert a["order_parameter"] == b["order_parameter"]
    assert a["phi_trace"] == b["phi_trace"]


def test_explore_template_is_seven_and_wide():
    out = engine.explore(question="which database?")
    assert len(out["points"]) == 7
    assert out["divergence"] > 0.5  # spread on purpose


def test_explore_with_ideas_keeps_them():
    out = engine.explore(ideas=["x", "y", "z"])
    assert len(out["points"]) == 7
    assert out["points"][0] == "x"


def test_optimize_holds_done_and_does_not_cost_more():
    conv = engine.converge(SEVEN, HIGH)
    opt = engine.optimize(conv)
    assert opt["R_held"] is True
    assert opt["best"]["witness"]["verdict"] == "R=1"
    assert opt["cost_after"] <= opt["cost_before"] + 1e-9


def test_recommend_returns_a_pick_with_witness():
    rec = engine.recommend(SEVEN, HIGH)
    assert rec["pick"] is not None
    assert rec["witness"]["verdict"] in ("R=1", "partial")
    assert rec["optimized"] is True


def test_frame_maps_context_then_converges():
    out = engine.frame(["note one", "note two", "note three"])
    assert "framing" in out and "witness" in out
    assert len(out["points"]) == 7
    assert out["points"][0] == "note one"
