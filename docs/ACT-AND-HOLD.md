<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /act and /hold

The five core verbs find an answer. `/act` and `/hold` put it to work and keep it true. Both are live.

## Why these two, and no others

A verb earns a place only if it names one structural operation the others do not cover, so the model knows what to do from the first token. Trace the five and the pipeline ends with a decided answer sitting in the model's context. It stops in two places: at the edge of your real world, and at one point in time. `/act` and `/hold` are those two operations. Everything else people ask for (focus, rank, split, compare, summarize) is a chain of the existing verbs, so it stays a chain.

## /act: turn the answer into real next steps

`/act` is the inverse of `/frame`. `frame` lifts your world into the structure. `/act` brings the structure back into your world: it takes a locked answer and turns it into the smallest set of concrete next steps, then runs them through the tools your host already has.

Host-tool discovery (the no-redundancy rule). The plugin ships no integrations of its own. It uses what your host already exposes:

- In Claude Code: the native tools, plus any MCP servers you have installed.
- In the Claude desktop app: the connectors you have connected.

`/act` proposes only steps it can actually run there. If your desktop app has Calendar and Gmail connected, it books the holds and drafts the mails through those. If nothing is connected, it prints a plain step list you can run yourself.

Safety. `/act` is the one verb that acts, so it stays in your control. It shows the plan first and gets a go-ahead before anything that writes, sends, books, or changes state. Read-only lookups it may run to fill in details. On a partial answer it acts only on the locked part and hands you the open question. Every action goes through your client's own permission prompts, so you approve each one. `/act` has no math engine and no MCP tool of its own. It is a command and a skill that orchestrates the tools you already trust.

## /hold: re-check a settled answer as the world moves

A decision is a one-shot by itself. Life is continuous. `/hold` takes a prior settled answer and the world's new state and re-checks whether it still holds. It reports the trios that came loose, so you fix the drift instead of re-deciding from scratch. Structurally it is converge with memory: it diffs a fresh converge against the prior's locked set. It needs no storage in the plugin. The agent hands it the prior witness plus the new inputs, so it stays offline and read-only, like the five.

`/hold` is a live MCP tool (`engine.hold`), plus a command and a skill.

## The shape, end to end

`frame` to `converge` to `act`, then `hold` to keep it together. The full loop: pull in, widen, lock, cheapen, decide, act, hold.
