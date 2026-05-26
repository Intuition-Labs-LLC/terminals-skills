# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""Zero-install entry point: `python3 server.py` runs the Terminals MCP server.

This shim puts its own directory on the import path so `terminals_core` resolves
without installation, then hands off to the in-package server. No dependencies,
no API key, no network.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from terminals_core.server import main  # noqa: E402

if __name__ == "__main__":
    main()
