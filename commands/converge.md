---
description: Bring a messy pile of ideas together into one right answer — with a receipt that proves it holds (done = true / R=1).
argument-hint: <the messy ideas, or a question to settle>
allowed-tools: mcp__terminals__converge, Read, Grep, Glob
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /converge

Bring it together. Take the noisy thoughtspace and collapse it to one answer that **provably hangs together** — and hand back the receipt.

The thoughtspace: **$ARGUMENTS**
(If that's empty, use the ideas already on the table in this conversation.)

Run this protocol. Keep every word small.

1. **Pick the points.** Pull out the distinct ideas in play. Keep the 7 strongest. If there are more than 7, cluster the rest into those 7 and say so. If fewer, use what's there.
2. **Judge agreement.** For every pair of ideas, rate 0..1 how well they fit together — do they support each other (→1), sit fine side by side (→0.5), or clash (→0)? This is your coherence matrix. Be honest; this is the only judgment that matters.
3. **Run the lock-in.** Call the `converge` tool with `{ ideas, coherence }`. It lays them on the 7-grid and runs the math. (No tool? Reason it through using `skills/converge/reference/` — same protocol, you do the arithmetic.)
4. **Read the result.**
   - **done = true (R=1):** every trio locked. Give the answer — the synthesis of the locked trios — in plain words. Then the receipt: which trios locked, the agree-meter `r`, the sure-o-meter `phi`.
   - **partial:** not everything locked. Say so plainly. Give the best partial, name the loose trios and *why* they're loose, and the one next move that would tighten them (or split the problem).
5. **Always show the receipt.** End with the witness: what the answer claims, which trios back it, the verdict, and the one-line why. Never fake "done."

Output shape: the **answer** first (plain English), then **the receipt** as a card:

```
  ╭───────────────────────  terminals · converge  ──╮
  │  answer  →  <one plain line>                      │
  │  locked  ▸ <trio> ▸ <trio> ▸ <trio>               │
  │  loose   ▸ <trio> — <what would tighten it>       │
  │  r <0..1>   ·   phi <0..1>   ·   done = true ✓     │
  ╰───────────────────────────────────────────────────╯
```

Use the user's own plain words inside the card — no jargon, whatever their domain. Drop the `loose` line when nothing is loose; show `partial` instead of `done = true ✓` when it didn't fully lock.
