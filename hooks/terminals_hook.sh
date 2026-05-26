#!/usr/bin/env bash
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
#
# Terminals lifecycle hook -- SHIPPED INERT.
#
# By default this does nothing: it exits 0 immediately. It exists to *codify* the
# Claude Code lifecycle chain (see the project's dag.md) as a runnable map, wired
# but off. Turn on observation-only logging with one env var:
#
#     export TERMINALS_HOOKS=1
#
# Even when on it ONLY appends a one-line note per event. It never blocks a tool,
# never modifies input, never injects context, and always exits 0.

event="${1:-unknown}"

# Inert by default. One env var turns on observation.
if [ "${TERMINALS_HOOKS:-0}" != "1" ]; then
  exit 0
fi

# Drain stdin (the event JSON) so the writer never blocks; no jq dependency.
payload="$(cat 2>/dev/null || true)"

log_dir="${TERMINALS_HOOK_LOG_DIR:-$HOME/.terminals}"
mkdir -p "$log_dir" 2>/dev/null || exit 0
ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo now)"
printf '%s\t%s\t%s bytes\n' "$ts" "$event" "${#payload}" >> "$log_dir/lifecycle.log" 2>/dev/null || true

# Observational only: never block, never emit stdout.
exit 0
