# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The lock-in: coupled phase oscillators on the 7-grid (the Kuramoto model).

Each idea is an oscillator. Ideas that agree pull together; ideas that clash
push apart. The order parameter r is the agree-meter: 0 = all over the place,
1 = fully locked in. A trio is 'locked' when its own r passes the threshold.

Natural frequencies are zero, so the only motion is the pull/push of coupling;
the system settles to a fixed point (a Banach-style attractor), which is why a
finite, bounded run is enough to read done=true.
"""
from __future__ import annotations

import cmath
import math

from .fano import lines
from .phi import phi_from_phases


def order_parameter(phases):
    """Global agree-meter r = | mean(e^{i*theta}) | over all points, in [0,1]."""
    z = sum(cmath.exp(1j * t) for t in phases) / len(phases)
    return abs(z)


def line_order(phases, line):
    """Agree-meter over just the 3 points of one trio."""
    z = sum(cmath.exp(1j * phases[p]) for p in line) / len(line)
    return abs(z)


def coupling_matrix(coherence):
    """Map pairwise coherence c in [0,1] to coupling K = 2c - 1 in [-1,1].

    c > 0.5 attracts (the pair agrees and pulls together); c < 0.5 repels (the
    pair clashes and pushes apart); c = 0.5 is neutral. Diagonal is 0.
    """
    n = len(coherence)
    K = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                K[i][j] = 2.0 * coherence[i][j] - 1.0
    return K


def integrate(phases, K, *, dt=0.05, steps=220, threshold=0.85, record=True):
    """Run the lock-in to a fixed point.

    Returns the final phases, the global agree-meter, each trio's agree-meter,
    the order trios locked in, and (if recording) the r and phi traces.
    """
    phases = list(phases)
    n = len(phases)
    ls = lines()
    lock_step: "dict[int, int | None]" = {k: None for k in range(len(ls))}
    trace = []
    phi_trace = []
    for s in range(steps):
        new = phases[:]
        for i in range(n):
            pi = phases[i]
            acc = 0.0
            for j in range(n):
                if i != j:
                    acc += K[i][j] * math.sin(phases[j] - pi)
            new[i] = pi + dt * (acc / n)
        phases = new
        for k, ln in enumerate(ls):
            if lock_step[k] is None and line_order(phases, ln) >= threshold:
                lock_step[k] = s
        if record:
            trace.append(round(order_parameter(phases), 4))
            phi_trace.append(round(phi_from_phases(phases), 4))
    line_r = {k: line_order(phases, ln) for k, ln in enumerate(ls)}
    locked_steps = {k: st for k, st in lock_step.items() if st is not None}
    lock_order = sorted(locked_steps, key=lambda k: locked_steps[k])
    return {
        "phases": phases,
        "r_global": order_parameter(phases),
        "line_r": line_r,
        "lock_step": lock_step,
        "lock_order": lock_order,
        "trace": trace,
        "phi_trace": phi_trace,
    }
