# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The lock-in: order parameter math + agree-locks / clash-breaks behavior."""
import math

from terminals_core import kuramoto


def test_order_parameter_identical_is_one():
    assert abs(kuramoto.order_parameter([1.0] * 7) - 1.0) < 1e-9


def test_order_parameter_evenly_spread_is_near_zero():
    phases = [2 * math.pi * i / 7 for i in range(7)]
    assert kuramoto.order_parameter(phases) < 1e-6


def test_coupling_maps_coherence_to_attract_and_repel():
    K = kuramoto.coupling_matrix([[1.0, 0.9], [0.1, 1.0]])
    assert abs(K[0][1] - 0.8) < 1e-9     # 2*0.9 - 1  (attract)
    assert abs(K[1][0] - (-0.8)) < 1e-9  # 2*0.1 - 1  (repel)
    assert K[0][0] == 0.0


def test_all_agree_locks_every_trio():
    c = [[0.95 if i != j else 1.0 for j in range(7)] for i in range(7)]
    res = kuramoto.integrate([0.1 * i for i in range(7)], kuramoto.coupling_matrix(c),
                             steps=320, threshold=0.85)
    assert res["r_global"] > 0.85
    assert all(v >= 0.85 for v in res["line_r"].values())


def test_all_clash_locks_nothing():
    c = [[1.0 if i == j else 0.15 for j in range(7)] for i in range(7)]
    res = kuramoto.integrate([0.1 * i for i in range(7)], kuramoto.coupling_matrix(c),
                             steps=320, threshold=0.85)
    locked = sum(1 for v in res["line_r"].values() if v >= 0.85)
    assert locked < 7
