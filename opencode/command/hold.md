---
description: Re-check a settled answer as the world moves. Reports which parts came loose so you fix the drift instead of re-deciding the whole thing.
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /hold (OpenCode)

Keep it together. You settled an answer earlier (`/converge` or `/recommend`). The world has moved. `/hold` re-checks whether the answer still holds and points at the one thing that drifted.

What changed: **$ARGUMENTS** (if empty, use the new information already in this conversation).

1. **Recall the prior answer.** You need the earlier settled result and its locked trios. If you don't have it, re-run `/converge` on the original ideas first.
2. **Fold in what changed.** Update the ideas and your pairwise coherence to reflect the new state. Keep the same 7 points where you can, so the comparison stays clean.
3. **Re-check with memory.** Call the `terminals` MCP tool `hold` with `{ prior, ideas, coherence }`. It re-converges and diffs against the prior locked set.
4. **Read the drift.** It returns `still_holds`, the trios that `drifted` (were locked, now loose), the ones that `held`, and any `new` locks. The re-check certifies coherence given your updated judgments. It does not prove the answer is correct in the world.
5. **Report the one thing.** If it still holds, say so in a line. If something drifted, name that trio and the single move that re-locks it. If most of it drifted, treat it as a fresh decision and point back to `/converge`.

End with a short receipt:

```
  ╭───────────────────────  terminals · hold  ──────╮
  │  still holds  →  yes / no                         │
  │  drifted      ▸ <trio that came loose>            │
  │  held         ▸ <what still stands>               │
  │  fix          ▸ <the one move to re-lock>         │
  │  r <0..1>   ·   phi <0..1>                         │
  ╰───────────────────────────────────────────────────╯
```

Re-check, then fix the drift. Do not re-decide what still stands.
