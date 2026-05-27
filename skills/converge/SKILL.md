---
name: converge
description: Use when several competing ideas, options, or hypotheses are already on the table and a single coherent answer is needed. Collapses a noisy pile of competing ideas into one coherent answer and returns a checkable receipt (done = true / R=1), or an honest partial when it can't. Reach for this at decision points or when finalizing a plan. Use converge when the options are already in play; if you'd have to generate the options yourself, use recommend; if the problem is still wide open, use explore first.
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Converge

You're looking at a pile of competing ideas and an answer is needed. Bring it together into one coherent answer and show the receipt.

## The protocol

1. **Pick the points.** Pull out the distinct ideas in play; keep the 7 strongest. More than 7 means cluster the rest into them and say so. Fewer means use what's there.
2. **Judge agreement.** Rate every pair 0..1: do they support each other (toward 1), coexist fine (toward 0.5), or clash (toward 0)? That is the coherence matrix, the one judgment that matters.
3. **Run the lock-in.** Call the `converge` tool with `{ ideas, coherence }`. It lays them on the 7-grid and runs the math.
4. **Read it.** `R=1` (every trio locked) means give the synthesized answer plus the receipt. `partial` means give the best partial, name the loose trios and why, and the one next move.
5. **Always show the receipt** (the witness): the claim, the trios that back it, the verdict, the one-line why. Never fake done = true.

Remember what done = true means: the ideas you scored all agree with each other. It is a check on your coherence judgments. It does not prove the answer is right in the world.

Answer first, in plain words. Receipt second.

## Going deeper (load only if needed)

- The 7-grid (why exactly 7, and "nothing lost"): `reference/fano.md`
- The lock-in (how agreement becomes one answer): `reference/kuramoto.md`
- The sure-o-meter `phi`: `reference/phi.md`
- What "everything locked" does and doesn't establish: `reference/realizability.md`
