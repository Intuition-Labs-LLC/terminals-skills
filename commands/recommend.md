---
description: You decide for me. Run the whole loop — explore, converge, optimize — on your own best lines and hand back a pick, with the receipt.
argument-hint: <the problem or decision you want settled>
allowed-tools: mcp__terminals__recommend, mcp__terminals__converge, mcp__terminals__optimize, Read, Grep, Glob, Task
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /recommend

You decide. The user is asking *because they're unsure* — so take the wheel. Run the whole loop yourself and come back with a pick **and** the receipt that backs it.

The problem: **$ARGUMENTS**

Run this protocol. Use your own judgment at every step — that's the point of this verb.

1. **Explore (you, not them).** Generate up to 7 genuinely distinct strong angles on the problem. Use your real conviction. For a hard or high-stakes problem, spawn the `explorer` agent up to 7 times (one per angle) in parallel to go deep (real token cost — cap it with Logfire Gateway, see `docs/OBSERVE.md`); for an everyday one, do it inline.
2. **Judge agreement.** Rate every pair 0..1 for how well they fit — honestly. Build the coherence matrix.
3. **Run the loop.** Call the `recommend` tool with `{ ideas, coherence }`. It converges (gets a sound answer + witness) and, if done = true, optimizes (the cheapest equal form), then returns a pick, alternatives, and the witness.
4. **Make the call.** State your pick in one or two plain sentences — what to do and the single biggest reason. Don't hedge; you were asked to decide.
5. **Back it with the receipt.** Show the witness: which trios locked (why the pick holds), the agree-meter and sure-o-meter, and 1–2 alternatives with the one reason each lost. If the space came back **partial**, say "I can't fully back a pick yet" and give the best lean plus the one thing that would settle it.

Pick first, in plain words. Receipt second. No fence-sitting, no fake certainty.
