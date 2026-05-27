---
description: Bring a messy pile of ideas together into one coherent answer, with a receipt you can check (done = true).
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /converge (OpenCode)

Collapse the noisy thoughtspace to one answer that holds together under your judgments, and hand back the receipt.

Thoughtspace: **$ARGUMENTS** (if empty, use the ideas already on the table).

1. **Pick the points.** The distinct ideas in play; keep the 7 strongest (cluster if more, use what's there if fewer).
2. **Judge agreement.** Rate every pair 0..1 (support goes to 1, coexist to 0.5, clash to 0). That is the coherence matrix.
3. **Run the lock-in.** Call the `terminals` MCP tool `converge` with `{ ideas, coherence }`.
4. **Read it.** done = true (R=1) means every trio agrees under the coherence you scored. Give the synthesized answer plus the receipt (locked trios, agree-meter r, sure-o-meter phi). The receipt certifies coherence given your judgments. It does not prove the decision is correct in the world. Partial: best partial plus the loose trios plus the next move.
5. **Always show the receipt.** Never fake done. Never hide a loose trio.

Answer first (plain words), receipt second.
