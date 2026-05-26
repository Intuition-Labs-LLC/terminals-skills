---
description: Take an answer that's already right and make it the best one — same answer, cheapest and cleanest form, without breaking done = true.
argument-hint: (run after /converge) — what to make cheaper/cleaner
allowed-tools: mcp__terminals__optimize, mcp__terminals__converge, Read, Grep, Glob
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /optimize

Make it the best one. The answer is already right (`/converge` said done = true). Now find the cheapest, cleanest version of that **same** answer.

Focus: **$ARGUMENTS**
(If empty, optimize the answer just converged in this conversation.)

The papers prove there are many equally-right versions of a sound answer. This picks the one that costs the least — fewest moving parts, least effort, lowest noise — while keeping the receipt valid.

Run this protocol.

1. **Start from a done answer.** You need a converged result (done = true). If there isn't one yet, run `/converge` first, then come back.
2. **Polish it.** Call the `optimize` tool with the whole converged object. It searches the equal-but-cheaper arrangements on a bounded schedule, so it always stops, and it **refuses any move that breaks done = true**.
3. **Read the cost.** It returns `cost_before`, `cost_after`, and `R_held`. If `R_held` is true and `cost_after ≤ cost_before`, the polish held — same answer, lower cost.
4. **Hand it back.** Give the cleaned-up answer in plain words. Then one line: "still done = true · cost X → Y." If nothing got cheaper, say so honestly — the first form was already best.

Never trade away done = true for a lower cost. Correct first, cheap second.
