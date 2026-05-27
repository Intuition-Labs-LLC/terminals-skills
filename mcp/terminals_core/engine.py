# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The five verbs as one organism.

`converge` is the core: lay ideas on the 7-grid, run the lock-in, read done=true,
return the answer plus the receipt (the witness). `explore`, `optimize`,
`recommend`, and `frame` are the same core with different before/after steps.

Split of labor: the agent supplies the *meaning* (the ideas, and how much each
pair agrees, as a coherence matrix). This engine supplies the *math*. Everything
here is deterministic given its inputs, offline, and uses no API key.
"""
from __future__ import annotations

import hashlib
import math
import random

from .anneal import anneal
from .fano import N_POINTS, lines
from .kuramoto import coupling_matrix, integrate, order_parameter
from .phi import phi_from_phases
from .steiner import coverage_report

DEFAULT_THRESHOLD = 0.85
MAX_OPTIMIZE_STEPS = 2000   # clamp caller-supplied max_steps (single-stdio DoS guard)
MAX_INTEGRATE_STEPS = 2000  # clamp caller-supplied integration steps


def _seed(*parts):
    h = hashlib.sha256(repr(parts).encode("utf-8")).hexdigest()
    return int(h[:16], 16)


def _to_points(ideas):
    """Map ideas onto exactly 7 points. Fewer than 7 pads with empty slots; more
    than 7 keeps the first 7 (the agent is asked to cluster first) and reports
    the compression honestly."""
    ideas = [str(x).strip() for x in (ideas or []) if str(x).strip()]
    n_real = len(ideas)
    if n_real >= N_POINTS:
        points = ideas[:N_POINTS]
        note = (
            "kept the first 7; cluster your ideas to 7 before converging for the cleanest result"
            if n_real > N_POINTS
            else "exactly 7 ideas mapped to the 7-grid"
        )
        compression = {"given": n_real, "used": N_POINTS, "note": note}
    else:
        points = ideas + [f"(empty {i})" for i in range(n_real, N_POINTS)]
        compression = {
            "given": n_real,
            "used": n_real,
            "note": f"only {n_real} ideas given; {N_POINTS - n_real} grid slots are empty",
        }
    return points, n_real, compression


def _default_coherence(n_real):
    """Neutral prior when the agent passes no coherence: real ideas weakly agree
    (0.55), anything touching an empty slot is neutral (0.5)."""
    c = [[1.0 if i == j else 0.5 for j in range(N_POINTS)] for i in range(N_POINTS)]
    for i in range(N_POINTS):
        for j in range(N_POINTS):
            if i != j and i < n_real and j < n_real:
                c[i][j] = 0.55
    return c


def _is_matrix(coherence):
    """True only for a real 2-D matrix (a list/tuple of row lists). A scalar,
    string, dict, or empty value is NOT a matrix and must not be silently
    treated as coherence (it would discard the signal while claiming success)."""
    if not isinstance(coherence, (list, tuple)) or len(coherence) == 0:
        return False
    return all(isinstance(row, (list, tuple)) for row in coherence)


def _normalize_coherence(coherence):
    """Coerce any input into a 7x7 symmetric matrix in [0,1] with unit diagonal."""
    c = [[0.0] * N_POINTS for _ in range(N_POINTS)]
    for i in range(N_POINTS):
        for j in range(N_POINTS):
            if i == j:
                c[i][j] = 1.0
            else:
                try:
                    v = float(coherence[i][j])
                except (IndexError, TypeError, ValueError, KeyError):
                    v = 0.5
                c[i][j] = min(1.0, max(0.0, v))
    for i in range(N_POINTS):
        for j in range(i + 1, N_POINTS):
            m = (c[i][j] + c[j][i]) / 2.0
            c[i][j] = c[j][i] = m
    return c


def _label_line(points, k):
    ln = lines()[k]
    return {"line": k, "points": list(ln), "ideas": [points[p] for p in ln]}


def _clean_threshold(t):
    """Coerce a caller-supplied threshold to a finite fraction in [0.01, 1.0].

    Guards the result object (and the math) against NaN/Infinity/out-of-range
    threshold values reaching the witness or json.dumps.
    """
    try:
        t = float(t)
    except (TypeError, ValueError):
        return DEFAULT_THRESHOLD
    return min(1.0, max(0.01, t)) if math.isfinite(t) else DEFAULT_THRESHOLD


def converge(ideas, coherence=None, threshold=DEFAULT_THRESHOLD, *, steps=220, dt=0.05, seed=None):
    """Bring a messy set of ideas together into one right answer with a receipt.

    Returns the engine-contract object: points, lines, order_parameter, R, phi,
    kept (locked trios in lock order), witness, phi_trace, and the coherence used.
    """
    threshold = _clean_threshold(threshold)
    steps = max(1, min(int(steps), MAX_INTEGRATE_STEPS))
    points, n_real, compression = _to_points(ideas)
    coherence_provided = coherence is not None and _is_matrix(coherence)
    c = _normalize_coherence(coherence) if coherence_provided else _default_coherence(n_real)
    if seed is None:
        seed = _seed(points, c, threshold)
    rng = random.Random(seed)
    K = coupling_matrix(c)
    ph0 = [rng.uniform(0, 2 * math.pi) for _ in range(N_POINTS)]
    res = integrate(ph0, K, dt=dt, steps=steps, threshold=threshold, record=True)

    line_r = res["line_r"]
    # A trio only counts if all three of its points are real ideas — empty
    # padding slots are never reportable as locked.
    real = set(range(min(n_real, N_POINTS)))
    real_lines = [k for k in range(N_POINTS) if all(p in real for p in lines()[k])]
    # Coherence is read from the FINAL state, never from "ever crossed", so the
    # locked set the user sees always matches the verdict. lock_order only orders.
    coherent = [k for k in real_lines if line_r[k] >= threshold]
    incoherent = [k for k in real_lines if line_r[k] < threshold]
    lock_pos = {k: i for i, k in enumerate(res["lock_order"])}
    kept = sorted(coherent, key=lambda k: lock_pos.get(k, len(line_r)))
    phi_final = phi_from_phases(res["phases"])
    n_lines = len(real_lines)
    verdict = "R=1" if n_lines and len(coherent) == n_lines else "partial"
    R = 1.0 if verdict == "R=1" else (round(len(coherent) / n_lines, 4) if n_lines else 0.0)

    if verdict == "R=1":
        rationale = "every trio locked in — the answer hangs together (done = true)."
    elif n_lines == 0:
        rationale = (
            "these ideas don't share a checkable trio on the grid yet — add one or two "
            "more (it works best with about 7)."
        )
    else:
        rationale = (
            f"{len(coherent)}/{n_lines} trios locked; {len(incoherent)} still loose. "
            "Best partial returned — tighten the loose pairs or split the problem."
        )
    if not coherence_provided:
        rationale += (
            " (No coherence matrix was given, so a neutral prior was used — it rarely "
            "reaches done = true; pass pairwise coherence 0..1 for a real verdict.)"
        )

    witness = {
        "coherent_lines": [_label_line(points, k) for k in kept],
        "incoherent": [
            {"line": k, "ideas": [points[p] for p in lines()[k]], "agree": round(line_r[k], 3)}
            for k in incoherent
        ],
        "verdict": verdict,
        "rationale": rationale,
        "coverage": coverage_report(n_real),
    }
    return {
        "points": points,
        "lines": [list(l) for l in lines()],
        "order_parameter": round(res["r_global"], 4),
        "R": R,
        "phi": round(phi_final, 4),
        "kept": [_label_line(points, k) for k in kept],
        "witness": witness,
        "phi_trace": res["phi_trace"],
        "coherence": c,
        "coherence_provided": coherence_provided,
        "compression": compression,
        "threshold": threshold,
        "seed": seed,
    }


def explore(ideas=None, question=None, k=7, seed=None):
    """Open a question into its full fan of distinct angles (high entropy).

    With ideas, lays them out spread wide and scores the divergence. Without
    ideas, returns 7 empty slots as a template for the agent to fill.
    """
    if ideas:
        points, _n_real, compression = _to_points(ideas)
    else:
        points = [f"(angle {i})" for i in range(N_POINTS)]
        compression = {"given": 0, "used": 0, "note": "template — fill the 7 angles, then /converge"}
    if seed is None:
        seed = _seed(points, question, "explore")
    rng = random.Random(seed)
    # spread phases evenly around the circle with jitter: deliberately high entropy
    phases = [(2 * math.pi * i / N_POINTS) + rng.uniform(-0.25, 0.25) for i in range(N_POINTS)]
    r = order_parameter(phases)
    return {
        "points": points,
        "lines": [list(l) for l in lines()],
        "divergence": round(1.0 - r, 4),
        "order_parameter": round(r, 4),
        "phi": round(phi_from_phases(phases), 4),
        "guidance": (
            "these are your angles, spread wide. Fill any (angle i) slots, judge how much "
            "each pair agrees (0..1), then /converge."
        ),
        "compression": compression,
        "seed": seed,
    }


def optimize(converged, cost_fn="hamiltonian", max_steps=200, threshold=None, seed=None, steps=220):
    """Take an already-converged result and find its cheapest, cleanest equal
    form without breaking done=true."""
    if threshold is None:
        threshold = converged.get("threshold", DEFAULT_THRESHOLD)
    threshold = _clean_threshold(threshold)
    max_steps = max(1, min(int(max_steps), MAX_OPTIMIZE_STEPS))
    steps = max(1, min(int(steps), MAX_INTEGRATE_STEPS))
    points = list(converged["points"])
    coherence = converged.get("coherence")
    was_done = converged.get("witness", {}).get("verdict") == "R=1"
    if coherence is None:
        return {
            "best": converged,
            "cost_before": None,
            "cost_after": None,
            "R_held": True,
            "note": "no coherence matrix on the converged result; nothing to optimize.",
        }
    if seed is None:
        seed = _seed(points, "optimize", threshold)
    a = anneal(coherence, threshold=threshold, max_steps=max_steps, steps=steps, seed=seed)
    perm = a["best_perm"]
    new_points = [None] * N_POINTS
    new_coh = [[0.0] * N_POINTS for _ in range(N_POINTS)]
    for i in range(N_POINTS):
        new_points[perm[i]] = points[i]
        for j in range(N_POINTS):
            new_coh[perm[i]][perm[j]] = coherence[i][j]
    best = converge(new_points, new_coh, threshold=threshold, seed=seed, steps=steps)
    still_done = best["witness"]["verdict"] == "R=1"
    return {
        "best": best,
        "cost_before": a["cost_before"],
        "cost_after": a["cost_after"],
        "R_held": (still_done if was_done else True),
        "arrangement": {"perm": perm, "points": new_points},
        "cost_fn": cost_fn,
        "steps_used": a["steps_used"],
    }


def recommend(ideas, coherence=None, threshold=DEFAULT_THRESHOLD, seed=None):
    """Run the whole loop for the user: converge, then (if done) optimize, then
    hand back a pick plus the witness and the alternatives."""
    conv = converge(ideas, coherence, threshold=threshold, seed=seed)
    result = conv
    optimized = False
    if conv["witness"]["verdict"] == "R=1":
        opt = optimize(conv, seed=seed)
        result = opt["best"]
        optimized = True
    locked = result["kept"] or result["witness"]["coherent_lines"]
    pick = locked[0] if locked else None
    alternatives = locked[1:4]
    return {
        "pick": pick,
        "alternatives": alternatives,
        "witness": result["witness"],
        "R": result["R"],
        "phi": result["phi"],
        "order_parameter": result["order_parameter"],
        "optimized": optimized,
        "detail": result,
    }


def frame(items, coherence=None, threshold=DEFAULT_THRESHOLD, seed=None):
    """Translate the user's own context onto the 7-grid, then converge.

    `items` is whatever the agent pulled from the working folder/notes; each
    item becomes a point. Returns a short reading of how the context was mapped,
    then the full converge result.
    """
    items = [str(x).strip() for x in (items or []) if str(x).strip()]
    points, _n_real, compression = _to_points(items)
    conv = converge(items, coherence, threshold=threshold, seed=seed)
    framing = {
        "read_as_points": points,
        "note": "here is how I read your stuff: each item became a point on the 7-grid; "
        + compression["note"],
    }
    return {"framing": framing, **conv}
