# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The polish: shake a *correct* answer toward its cheapest equal-but-better form.

The papers prove realizers are not unique -- many idea->point arrangements reach
done=true. /optimize searches them for the lowest-cost one (the cost-meter, a
Hamiltonian), never dropping a trio that was already locked, on a bounded,
log-cooled schedule so it always halts.
"""
from __future__ import annotations

import math
import random

from .fano import N_POINTS
from .kuramoto import coupling_matrix, integrate


def hamiltonian(result):
    """Cost-meter: lower = tighter and cleaner. Sum over trios of (1 - agree),
    plus a small term for how long the trios took to lock (less effort = cheaper)."""
    line_r = result["line_r"]
    tightness = sum(1.0 - line_r[k] for k in line_r)
    lock_step = result["lock_step"]
    effort = sum((s or 0) for s in lock_step.values()) / (len(lock_step) * 1000.0)
    return tightness + effort


def _reindex(perm, coherence):
    """Re-place the coherence matrix under an idea->point permutation."""
    n = len(perm)
    c = [[0.0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            c[perm[a]][perm[b]] = coherence[a][b]
    return c


def anneal(coherence, *, threshold=0.85, max_steps=200, dt=0.05, steps=160, seed=0):
    """Search idea->point permutations for the min-cost done=true arrangement.

    A fixed (seeded) set of start phases is reused for every candidate so the
    cost is a deterministic function of the arrangement. Returns the best
    permutation, the cost before/after, how many trios stay locked, and whether
    done=true was held throughout.
    """
    rng = random.Random(seed)
    n = N_POINTS
    ph0 = [rng.uniform(0, 2 * math.pi) for _ in range(n)]

    def evaluate(perm):
        K = coupling_matrix(_reindex(perm, coherence))
        res = integrate(ph0, K, dt=dt, steps=steps, threshold=threshold, record=False)
        locked = sum(1 for k in res["line_r"] if res["line_r"][k] >= threshold)
        return res, locked, hamiltonian(res)

    cur = list(range(n))
    _, cur_locked, cur_cost = evaluate(cur)
    start_locked, cost_before = cur_locked, cur_cost
    best, best_cost, best_locked = cur[:], cur_cost, cur_locked

    for k in range(max_steps):
        T = 1.0 / math.log(k + 2)  # log cooling -> bounded, guaranteed halt
        cand = cur[:]
        i, j = rng.randrange(n), rng.randrange(n)
        cand[i], cand[j] = cand[j], cand[i]
        _, cand_locked, cand_cost = evaluate(cand)
        if cand_locked < start_locked:
            continue  # hard constraint: never give up a trio we started with
        d = cand_cost - cur_cost
        if d < 0 or rng.random() < math.exp(-d / max(T, 1e-9)):
            cur, cur_cost, cur_locked = cand, cand_cost, cand_locked
            if cand_locked > best_locked or (cand_locked == best_locked and cand_cost < best_cost):
                best, best_cost, best_locked = cand[:], cand_cost, cand_locked

    return {
        "best_perm": best,
        "cost_before": round(cost_before, 4),
        "cost_after": round(best_cost, 4),
        "locked_lines": best_locked,
        "start_locked": start_locked,
        "R_held": best_locked >= start_locked,
        "steps_used": max_steps,
    }
