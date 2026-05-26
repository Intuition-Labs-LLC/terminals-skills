---
description: Bring a messy pile of ideas together into one right answer, with a receipt that proves it holds (done = true).
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /converge (OpenCode)

Collapse the noisy thoughtspace to one answer that provably hangs together, and hand back the receipt.

Thoughtspace: **$ARGUMENTS** (if empty, use the ideas already on the table).

1. **Pick the points** — the distinct ideas in play; keep the 7 strongest (cluster if more, use what's there if fewer).
2. **Judge agreement** — rate every pair 0..1 (support →1, coexist →0.5, clash →0). That's the coherence matrix.
3. **Run the lock-in** — call the `terminals` MCP tool `converge` with `{ ideas, coherence }`.
4. **Read it** — done = true (R=1): give the synthesized answer + the receipt (locked trios, agree-meter r, sure-o-meter phi). Partial: best partial + the loose trios + the next move.
5. **Always show the receipt.** Never fake done.

Answer first (plain words), receipt second.
