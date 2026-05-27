---
description: Take an answer that already holds together and make it the cheapest, cleanest form of itself, without breaking done = true.
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /optimize (OpenCode)

The answer already holds together. Find the cheapest, cleanest version of that same answer.

Focus: **$ARGUMENTS** (if empty, optimize the answer just converged).

1. **Start from a done answer.** You need a converged result (done = true). If none, run `/converge` first.
2. **Polish it.** Call the `terminals` MCP tool `optimize` with the whole converged object. Bounded search, so it always stops; it refuses any move that breaks done = true.
3. **Read the cost.** `cost_before`, `cost_after`, `R_held`. Held and cheaper means it worked.
4. **Hand back** the cleaned-up answer, then "still done = true, cost X to Y." If nothing got cheaper, say so.

Coherence first, cheap second. Never trade away done = true for cost.
