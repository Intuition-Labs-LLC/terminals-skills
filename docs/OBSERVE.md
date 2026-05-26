<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Watch the cost (optional)

Terminals has two halves, and only one of them ever costs anything.

- **The engine** — the `converge` math — is offline. Plain Python, no key, no network, free. Nothing to watch.
- **The agent** that drives the verbs — the model reading your folder, generating angles, judging agreement, spawning explorers — makes LLM calls. Those cost tokens. `/recommend` is the heavy one: on a hard call it can spawn up to 7 explorer subagents at once.

If you want to **see** and **cap** that spend, run the agent behind **Logfire Gateway** — a local proxy in front of your model provider that traces every call and enforces cost limits, without storing API keys on your laptop.

## Turn it on

For Claude Code (first-class):

```bash
uvx --with 'logfire[gateway]' logfire gateway launch claude
```

It opens a browser for a one-time login (OAuth, PKCE), runs a proxy on `127.0.0.1` with a short-lived token, and starts your tool pointed at it. No API key touches disk.

For any other MCP client or tool:

```bash
uvx --with 'logfire[gateway]' logfire gateway serve
# prints a base URL — point your tool's model endpoint at it
```

Now every verb you run is traced in your Logfire project: the LLM calls, the token cost, the tool calls (including each `converge` / `recommend`), latency, and errors. Set hierarchical limits — org → project → user → session — so a runaway `/recommend` can't surprise you.

## The two receipts

This pairs cleanly with what Terminals already returns:

- **The witness** (from every verb) tells you *what* the answer is and *why* it holds — the reasoning receipt.
- **The Logfire trace** tells you *what it cost* to get there — the spend receipt.

Together: a sound answer, the proof it's sound, and the bill. Both are opt-in to read; neither is required to run.

> Terminals does not bundle or require Logfire. This is an optional environment recipe — you turn it on, not us. The engine stays offline and free with or without it.

Logfire is from Pydantic — built on OpenTelemetry. Launch announcement: <https://pydantic.dev/articles/logfire-gateway-launch>
