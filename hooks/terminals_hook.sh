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

# Always drain stdin (the event JSON) first, even when inert, so the host's
# write to our stdin can never hit a closed pipe. No jq dependency.
payload="$(cat 2>/dev/null || true)"

# Inert by default. One env var turns on observation.
if [ "${TERMINALS_HOOKS:-0}" != "1" ]; then
  exit 0
fi

log_dir="${TERMINALS_HOOK_LOG_DIR:-$HOME/.terminals}"
mkdir -p "$log_dir" 2>/dev/null || exit 0
ts="$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || echo now)"
printf '%s\t%s\t%s bytes\n' "$ts" "$event" "${#payload}" >> "$log_dir/lifecycle.log" 2>/dev/null || true

# Observational only: never block, never emit stdout.
exit 0
