---
name: hold
description: Use when a decision was settled earlier and something has changed, and the user wants to know if it still holds rather than redo it from scratch ("does this still work now that X happened", "did the plan survive", "re-check our call"). Re-converges with memory and reports which parts drifted. Use hold to re-check an existing answer against new facts; use converge for a fresh decision, and recommend when you should make the call yourself.
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Hold

A decision was settled earlier and the world moved. Re-check whether it still holds and point at the one thing that drifted, so the user fixes the drift instead of re-deciding.

## The protocol

1. **Recall the prior answer.** You need the earlier settled result and its locked trios. If you don't have it, re-converge the original ideas first.
2. **Fold in what changed.** Update the ideas and the pairwise coherence to reflect the new state. Keep the same 7 points where you can, so the comparison stays clean.
3. **Re-check with memory.** Call the `hold` tool with `{ prior, ideas, coherence }`. It re-converges and diffs against the prior locked set.
4. **Read the drift.** `still_holds`, `drifted` (were locked, now loose), `held`, and any `new` locks.
5. **Report the one thing.** If it holds, one line. If something drifted, name that trio and the single move that re-locks it. If most of it drifted, treat it as a fresh decision and point back to converge.

Re-check rather than re-decide. Name the trio that drifted and the move that re-locks it.

## Going deeper (load only if needed)

- What "locked" means, and what it does and doesn't establish: `../converge/reference/realizability.md`
