# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The 7-grid: the Fano plane PG(2,2), a.k.a. the Steiner triple system S(2,3,7).

7 points, 7 lines (trios). Every pair of points lies on exactly one line. No
idea gets lost, nothing is counted twice. This is the fixed structure every
verb reduces a thoughtspace onto.
"""
from __future__ import annotations

N_POINTS = 7

# The (7,3,1) cyclic difference set {0,1,3}: line k is its translate mod 7.
# Differences of {0,1,3} cover every nonzero residue mod 7 exactly once, so the
# 7 translates form a valid Steiner triple system (every pair once).
_BASE = (0, 1, 3)


def lines():
    """The 7 trios, each a sorted (a, b, c). Line k = {k, k+1, k+3} mod 7."""
    out = []
    for k in range(N_POINTS):
        out.append(tuple(sorted((k + d) % N_POINTS for d in _BASE)))
    return out


def point_lines(p):
    """Indices of the 3 lines that pass through point p."""
    return [i for i, ln in enumerate(lines()) if p in ln]


def incidence_ok():
    """True iff the structure is a valid Fano plane: 7 lines of size 3, and
    every one of the 21 point-pairs lies on exactly one line."""
    ls = lines()
    if len(ls) != N_POINTS or any(len(set(l)) != 3 for l in ls):
        return False
    seen = {}
    for l in ls:
        pts = sorted(l)
        for a in range(3):
            for b in range(a + 1, 3):
                pair = (pts[a], pts[b])
                seen[pair] = seen.get(pair, 0) + 1
    if len(seen) != 21:
        return False
    return all(v == 1 for v in seen.values())


def heawood_edges():
    """The wiring: bipartite incidence as the Heawood graph.

    7 point-nodes ('P0'..'P6') + 7 line-nodes ('L0'..'L6'), 21 edges, every
    node degree 3. The picture of which idea sits in which trio.
    """
    edges = []
    for k, ln in enumerate(lines()):
        for p in sorted(ln):
            edges.append((f"P{p}", f"L{k}"))
    return edges
