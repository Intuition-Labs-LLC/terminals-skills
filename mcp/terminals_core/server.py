# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""Terminals MCP server: pure standard library, offline, no API key.

Speaks the Model Context Protocol over stdio: newline-delimited JSON-RPC 2.0.
Exposes six tools (explore, converge, optimize, recommend, frame, hold). The math
lives in this same package; this module is just the wire. The seventh verb, act,
is host orchestration with no math, so it ships as a command and skill only.
"""
from __future__ import annotations

import json
import sys

from . import engine, ontology

SERVER_NAME = "terminals"
SERVER_VERSION = "0.1.0"
DEFAULT_PROTOCOL = "2025-06-18"

_NUM_MATRIX = {
    "type": "array",
    "items": {"type": "array", "items": {"type": "number"}},
    "description": "Optional N x N matrix in [0,1]: how much idea i agrees with idea j.",
}

TOOLS = [
    {
        "name": "ontology",
        "description": (
            "The Terminals ontology — one atom, many projections. The whole substrate reduces to a "
            "single externally-gated interaction-arrow (decode->interpret->translate->control->GATE->"
            "{cement|recycle}), weighted by coherence R, descending H=1-R. Returns the atom, the 9 "
            "constructed objects (Switchboard/Runtime/Ledger/Recipe/Factory/Registry/Governor/"
            "Firewall/Kind), the isoformer ladder (interaction->recipe->library->sematon), and the "
            "ontological functions (leap, kind, witness, tower, settle, govern). Pass `query` to "
            "filter to a section (atom|ladder|functions|objects) or a named object/function "
            "(e.g. 'Recipe', 'leap'). Field reading, not advice; the math is real, the edge unproven."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Optional filter: a section (atom|ladder|functions|objects) or a named object/function.",
                },
            },
        },
    },
    {
        "name": "converge",
        "description": (
            "Bring a messy set of ideas together into one coherent answer with a checkable receipt. "
            "Pass the ideas and, ideally, a coherence matrix (how much each pair agrees, 0..1). "
            "Returns the locked trios, the agree-meter r, the sure-o-meter phi, done=true or "
            "partial, and the witness: a certificate that the answer holds together under the "
            "coherence you supplied. It shows internal consistency. It does not prove the "
            "decision is correct in the world."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "ideas": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "The ideas (up to 7; cluster to 7 first if you have more).",
                },
                "coherence": _NUM_MATRIX,
                "threshold": {"type": "number", "description": "Lock-in threshold (default 0.85)."},
            },
            "required": ["ideas"],
        },
    },
    {
        "name": "explore",
        "description": (
            "Open a question into its full fan of distinct angles (high entropy, on purpose). "
            "Returns 7 spread points and a divergence score. With no ideas yet, returns 7 empty "
            "slots to fill."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "ideas": {"type": "array", "items": {"type": "string"}},
                "question": {"type": "string"},
            },
        },
    },
    {
        "name": "optimize",
        "description": (
            "Take an already-converged result and find its cheapest, cleanest equal form without "
            "breaking done=true. Pass the whole object that converge returned."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "converged": {"type": "object", "description": "The object returned by converge."},
                "max_steps": {"type": "integer", "description": "Bounded search budget (default 200)."},
            },
            "required": ["converged"],
        },
    },
    {
        "name": "recommend",
        "description": (
            "Run the whole loop for the user: converge, then optimize, then hand back a pick plus "
            "the witness and alternatives. Pass the agent's own best lines as ideas and, ideally, "
            "a coherence matrix."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "ideas": {"type": "array", "items": {"type": "string"}},
                "coherence": _NUM_MATRIX,
                "threshold": {"type": "number"},
            },
            "required": ["ideas"],
        },
    },
    {
        "name": "frame",
        "description": (
            "Translate the user's own context (notes/files already gathered) onto the 7-grid, "
            "then converge. Pass the items as a list of strings."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "items": {"type": "array", "items": {"type": "string"}},
                "coherence": _NUM_MATRIX,
                "threshold": {"type": "number"},
            },
            "required": ["items"],
        },
    },
    {
        "name": "hold",
        "description": (
            "Re-check a settled answer against new state (converge with memory). Pass the prior "
            "converge result plus the updated ideas and coherence. Returns which locked trios came "
            "loose (drift), which still hold, the new ones, and the fresh verdict, so you fix the "
            "drift instead of re-deciding from scratch."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "prior": {"type": "object", "description": "The earlier converge result to re-check."},
                "ideas": {"type": "array", "items": {"type": "string"}},
                "coherence": _NUM_MATRIX,
                "threshold": {"type": "number"},
            },
            "required": ["prior", "ideas"],
        },
    },
]


def dispatch(name, args):
    if name == "ontology":
        return ontology.read(args.get("query"))
    if name == "converge":
        return engine.converge(args["ideas"], args.get("coherence"), args.get("threshold", engine.DEFAULT_THRESHOLD))
    if name == "explore":
        return engine.explore(args.get("ideas"), args.get("question"))
    if name == "optimize":
        return engine.optimize(args["converged"], max_steps=args.get("max_steps", 200))
    if name == "recommend":
        return engine.recommend(args["ideas"], args.get("coherence"), args.get("threshold", engine.DEFAULT_THRESHOLD))
    if name == "frame":
        return engine.frame(args["items"], args.get("coherence"), args.get("threshold", engine.DEFAULT_THRESHOLD))
    if name == "hold":
        return engine.hold(args["prior"], args["ideas"], args.get("coherence"), args.get("threshold", engine.DEFAULT_THRESHOLD))
    raise ValueError(f"unknown tool: {name}")


def _send(obj):
    sys.stdout.write(json.dumps(obj) + "\n")
    sys.stdout.flush()


def _result(id_, result):
    _send({"jsonrpc": "2.0", "id": id_, "result": result})


def _error(id_, code, message):
    _send({"jsonrpc": "2.0", "id": id_, "error": {"code": code, "message": message}})


def handle(msg):
    method = msg.get("method")
    id_ = msg.get("id")
    has_id = "id" in msg and msg["id"] is not None
    # A message with no id, or in the notifications/* namespace, is a notification:
    # per JSON-RPC it gets NO response (never reply with "id": null).
    if not has_id or (method or "").startswith("notifications/"):
        return
    if method == "initialize":
        proto = (msg.get("params") or {}).get("protocolVersion") or DEFAULT_PROTOCOL
        _result(id_, {
            "protocolVersion": proto,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        })
    elif method == "ping":
        _result(id_, {})
    elif method == "tools/list":
        _result(id_, {"tools": TOOLS})
    elif method == "tools/call":
        params = msg.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        if not name:  # malformed request, not a tool failure
            _error(id_, -32602, "tools/call is missing params.name")
            return
        try:
            out = dispatch(name, args)
            _result(id_, {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]})
        except Exception as exc:  # a tool failure is a result with isError, not a protocol error
            _result(id_, {"content": [{"type": "text", "text": f"error: {exc}"}], "isError": True})
    else:
        _error(id_, -32601, f"method not found: {method}")


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except (json.JSONDecodeError, RecursionError, ValueError):
            # RecursionError: a deeply-nested JSON frame must not crash the server.
            sys.stderr.write("terminals: skipped an unparseable line\n")
            sys.stderr.flush()
            continue
        if isinstance(msg, list):
            for m in msg:
                if isinstance(m, dict):
                    handle(m)
        elif isinstance(msg, dict):
            handle(msg)
        else:
            sys.stderr.write("terminals: skipped a non-object JSON-RPC frame\n")
            sys.stderr.flush()


if __name__ == "__main__":
    main()
