# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""Terminals convergence engine — the math behind the five verbs.

The agent supplies the meaning (ideas, and how much each pair agrees). This
package supplies the math (the 7-grid, the lock-in, the order parameter, the
done=true test, the polish). Pure standard library. Offline. No API key.
"""
from __future__ import annotations

from .engine import (
    DEFAULT_THRESHOLD,
    converge,
    explore,
    optimize,
    recommend,
    frame,
)

__all__ = [
    "DEFAULT_THRESHOLD",
    "converge",
    "explore",
    "optimize",
    "recommend",
    "frame",
]

__version__ = "0.1.0"
