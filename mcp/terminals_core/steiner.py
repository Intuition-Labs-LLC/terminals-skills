# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""Coverage: did any pair of ideas get lost or double-counted?

The 7-grid promises every pair of points sits on exactly one trio. This reports
that promise against the real ideas mapped onto the points (the rest are empty
padding).
"""
from __future__ import annotations

from .fano import lines, N_POINTS


def coverage_report(n_real):
    """How the 7-grid covers `n_real` real ideas (points beyond that are empty).

    For a valid Steiner system every real pair is covered exactly once, so a
    healthy report shows lost=0 and double_counted=0.
    """
    real = set(range(min(n_real, N_POINTS)))
    pair_count = {}
    for ln in lines():
        pts = sorted(ln)
        for a in range(3):
            for b in range(a + 1, 3):
                pair = (pts[a], pts[b])
                pair_count[pair] = pair_count.get(pair, 0) + 1
    real_covered = [pr for pr in pair_count if pr[0] in real and pr[1] in real]
    total_real_pairs = n_real * (n_real - 1) // 2 if n_real >= 2 else 0
    # within the 7 grid points, every real pair is covered, so capped at C(7,2)
    capped_total = min(total_real_pairs, len(real) * (len(real) - 1) // 2)
    return {
        "real_ideas": min(n_real, N_POINTS),
        "real_pairs_total": total_real_pairs,
        "real_pairs_covered": len(real_covered),
        "max_times_a_pair_is_counted": max(pair_count.values()) if pair_count else 0,
        "lost": max(0, capped_total - len(real_covered)),
        "double_counted": sum(1 for v in pair_count.values() if v > 1),
    }
