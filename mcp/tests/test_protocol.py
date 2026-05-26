# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""The server speaks MCP over stdio: initialize -> tools/list -> tools/call.

Drives the real server.py as a subprocess with newline-delimited JSON-RPC.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SERVER = os.path.join(os.path.dirname(HERE), "server.py")

HIGH = [[0.95 if i != j else 1.0 for j in range(7)] for i in range(7)]


def _run(messages):
    proc = subprocess.run(
        [sys.executable, SERVER],
        input="\n".join(json.dumps(m) for m in messages) + "\n",
        capture_output=True,
        text=True,
        timeout=90,
    )
    out = [json.loads(line) for line in proc.stdout.splitlines() if line.strip()]
    return out, proc.stderr


def test_initialize_list_and_call_converge():
    msgs = [
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": "2025-06-18", "capabilities": {},
                    "clientInfo": {"name": "test", "version": "1"}}},
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 3, "method": "tools/call",
         "params": {"name": "converge",
                    "arguments": {"ideas": [f"i{i}" for i in range(7)], "coherence": HIGH}}},
    ]
    out, err = _run(msgs)
    by_id = {m.get("id"): m for m in out if "id" in m}

    assert by_id[1]["result"]["serverInfo"]["name"] == "terminals"
    assert by_id[1]["result"]["protocolVersion"] == "2025-06-18"

    names = {t["name"] for t in by_id[2]["result"]["tools"]}
    assert names == {"explore", "converge", "optimize", "recommend", "frame"}

    payload = json.loads(by_id[3]["result"]["content"][0]["text"])
    assert payload["witness"]["verdict"] == "R=1"


def test_unknown_method_returns_jsonrpc_error():
    out, err = _run([{"jsonrpc": "2.0", "id": 9, "method": "does/notexist"}])
    assert out[0]["error"]["code"] == -32601


def test_tool_error_is_reported_as_iserror():
    # converge with no ideas -> KeyError in dispatch -> isError result, not a crash
    out, err = _run([
        {"jsonrpc": "2.0", "id": 5, "method": "tools/call",
         "params": {"name": "converge", "arguments": {}}},
    ])
    by_id = {m.get("id"): m for m in out if "id" in m}
    assert by_id[5]["result"]["isError"] is True


def test_notification_method_gets_no_reply_and_never_id_null():
    # a request-method sent without an id is a notification -> no response, ever.
    out, err = _run([
        {"jsonrpc": "2.0", "method": "ping"},  # notification (no id)
        {"jsonrpc": "2.0", "id": 1, "method": "initialize",
         "params": {"protocolVersion": "2025-06-18", "capabilities": {}}},
    ])
    assert all(("id" not in m) or (m["id"] is not None) for m in out)  # no "id": null frame
    assert [m.get("id") for m in out if "id" in m] == [1]  # only initialize replied


def test_tools_call_missing_name_is_invalid_params():
    out, err = _run([{"jsonrpc": "2.0", "id": 7, "method": "tools/call", "params": {}}])
    by_id = {m.get("id"): m for m in out if "id" in m}
    assert by_id[7]["error"]["code"] == -32602
