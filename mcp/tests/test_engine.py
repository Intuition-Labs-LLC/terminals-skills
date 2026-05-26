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


# --- regression: the locked set must match the verdict, and never include padding ---

def _all_repel():
    return [[1.0 if i == j else 0.0 for j in range(7)] for i in range(7)]


def test_kept_equals_coherent_no_stale_locks():
    # All pairs repel: any transient threshold-cross at the start must not survive
    # into the reported locks. kept (shown to the user) must equal coherent_lines.
    out = engine.converge(SEVEN, _all_repel(), seed=2)
    assert out["witness"]["verdict"] == "partial"
    kept = {tuple(w["points"]) for w in out["kept"]}
    coherent = {tuple(w["points"]) for w in out["witness"]["coherent_lines"]}
    assert kept == coherent


def test_no_empty_slot_is_ever_locked_or_picked():
    for s in range(40):
        out = engine.converge(["ship it", "hold off"], seed=s)
        for w in out["kept"]:
            assert not any(str(x).startswith("(empty") for x in w["ideas"])
        rec = engine.recommend(["ship it", "hold off"], seed=s)
        if rec["pick"]:
            assert not any(str(x).startswith("(empty") for x in rec["pick"]["ideas"])


def test_five_ideas_lock_only_real_trios():
    five = [f"idea{i}" for i in range(5)]
    c = [[0.95 if i != j else 1.0 for j in range(5)] for i in range(5)]
    out = engine.converge(five, c)
    for w in out["kept"]:
        assert all(p < 5 for p in w["points"])
        assert not any(str(x).startswith("(empty") for x in w["ideas"])


def test_coherence_provided_is_honest():
    assert engine.converge(SEVEN, HIGH)["coherence_provided"] is True
    assert engine.converge(SEVEN, 0.9)["coherence_provided"] is False  # a scalar is not a matrix
    assert engine.converge(SEVEN, None)["coherence_provided"] is False


def test_no_coherence_adds_a_note():
    out = engine.converge(SEVEN, None)
    assert "neutral prior" in out["witness"]["rationale"]


def test_phi_nbins_one_is_guarded():
    from terminals_core import phi
    assert isinstance(phi.phi_from_phases([0.0, 1.0, 2.0], nbins=1), float)  # no ZeroDivisionError
