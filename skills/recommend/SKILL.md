---
name: recommend
description: Use when the user asks you to decide for them, or signals they're unsure and want your call ("what should I do", "you pick", "I don't know, recommend something"). Take agency: run the whole loop yourself (explore your own best lines, converge, optimize) and return a clear pick backed by a receipt. The right move when the user is uncertain and wants a decision, not just options. Unlike explore (which only lays out options) and converge (which resolves options the user already supplied), recommend generates its own options and commits to one.
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Recommend

The user is unsure and wants *you* to decide. Take the wheel. Run the full loop on your own best thinking and come back with a pick **and** the receipt.

## The protocol

1. **Explore (you, not them).** Generate up to 7 genuinely distinct strong angles, using your real conviction. For a hard or high-stakes call, spawn the `explorer` agent up to 7 times in parallel — one per angle (that's 7 subagents, so save it for genuinely hard calls); for an everyday call, do it inline.
2. **Judge agreement.** Rate every pair 0..1, honestly. Build the coherence matrix.
3. **Run the loop.** Call the `recommend` tool with `{ ideas, coherence }`. It converges, then (if done = true) optimizes, and returns a pick, alternatives, and the witness.
4. **Make the call.** State your pick in one or two plain sentences — what to do and the single biggest reason. Don't hedge; you were asked to decide.
5. **Back it.** Show the receipt: which trios lock the pick, the agree/sure meters, and 1–2 alternatives with the one reason each lost. If it came back **partial**, say "I can't fully back a pick yet," give the best lean, and name the one thing that would settle it.

Pick first, plain words. Receipt second. No fence-sitting, no fake certainty.

## Going deeper (load only if needed)

- Why the loop's output is trustworthy: `../converge/reference/realizability.md`
