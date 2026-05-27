<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Roadmap: /act and /hold (designed, shipped inert)

The live surface is the five verbs. Two more are designed and wired dormant. They close the loop from a settled answer into the world, and keep it closed as the world moves. Default off. What follows is the spec, not a live feature.

## Why these two, and no others

A verb earns a place only if it names one structural operation the others do not cover, so the model knows what to do from the first token. Trace the five and the pipeline ends with a decided answer sitting in the model's context. It stops in two places: at the edge of your real world, and at one point in time. `/act` and `/hold` are those two operations. Everything else people ask for (focus, rank, split, compare, summarize) is a chain of the existing verbs, so it stays a chain.

## /act: turn the answer into real next steps

`/act` is the inverse of `/frame`. `frame` lifts your world into the structure. `/act` brings the structure back into your world: it takes a locked answer and turns it into the smallest set of concrete next steps, then runs them through the tools your host already has.

Host-tool discovery (the no-redundancy rule). The plugin ships no integrations of its own. On load it asks the host what it can already do:

- In Claude Code: the native tools, plus any MCP servers you have installed.
- In the Claude desktop app: the connectors you have connected.

`/act` proposes only steps it can actually run there. If your desktop app has Calendar and Gmail connected, it books the holds and drafts the mails through those. If nothing is connected, it prints a plain step list you can run yourself.

Safety. `/act` is the one verb that writes, so it stays opt-in and permissioned, and it shows the receipt for each step before it touches anything. On a partial answer it executes only the locked part and hands you the open question. No connector means no failure: it falls back to the step list.

## /hold: re-check a settled answer as the world moves

A decision is one-shot today. Life is continuous. `/hold` takes a prior settled answer and the world's new state and re-checks whether it still holds. It reports the trios that came loose, so you fix the drift instead of re-deciding from scratch. Structurally it is converge with memory: it diffs a fresh converge against the prior's locked set. It needs no storage in the plugin. The agent hands it the prior witness plus the new inputs, so it stays offline.

The dormant engine hook for `/hold` already exists (`engine.hold`), is tested, and is intentionally left out of the live MCP tool list. Turning it on is a one-line registration once the host-tool surface and the safety review for `/act` land together.

## The shape, end to end

`frame` to `converge` to `act`, then `hold` to keep it together. With the five, the loop is complete: pull in, widen, lock, cheapen, decide, act, hold.
