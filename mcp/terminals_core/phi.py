# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The sure-o-meter: phi = 1 - H(P) / log|V|.

The lab's phi measures how peaked a distribution is (0 = lost, 1 = knows the
next step). Here the distribution P is the spread of the 7 phases around the
circle: when they bunch up, entropy H falls and phi rises toward 1. This is the
circle analog of the decode-time phi signal.
"""
from __future__ import annotations

import math


def phi_from_phases(phases, nbins=12):
    """phi in [0,1] from how concentrated the phases are on the unit circle.

    All phases in one bin -> H=0 -> phi=1 (locked, sure). Phases spread evenly
    -> H high -> phi low (searching).
    """
    if not phases or nbins <= 1:
        return 0.0
    counts = [0.0] * nbins
    two_pi = 2.0 * math.pi
    for t in phases:
        b = int((t % two_pi) / two_pi * nbins) % nbins
        counts[b] += 1.0
    total = sum(counts)
    if total == 0:
        return 0.0
    H = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            H -= p * math.log(p)
    return max(0.0, min(1.0, 1.0 - H / math.log(nbins)))
