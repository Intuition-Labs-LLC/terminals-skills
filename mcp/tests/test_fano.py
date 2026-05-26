# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The 7-grid must be a valid Fano plane: parity against finite geometry."""
from collections import Counter

from terminals_core import fano


def test_seven_lines_each_size_three():
    ls = fano.lines()
    assert len(ls) == 7
    assert all(len(set(l)) == 3 for l in ls)


def test_every_pair_on_exactly_one_line():
    assert fano.incidence_ok()


def test_each_point_on_three_lines():
    for p in range(7):
        assert len(fano.point_lines(p)) == 3


def test_heawood_is_bipartite_degree_three():
    edges = fano.heawood_edges()
    assert len(edges) == 21
    deg = Counter()
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    assert len(deg) == 14  # 7 point-nodes + 7 line-nodes
    assert all(d == 3 for d in deg.values())
