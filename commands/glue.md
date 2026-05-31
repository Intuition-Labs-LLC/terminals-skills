---
description: Join two or more things that already hold into one. Check they hold together, and hand back the combined trinket, or name the seam that won't take.
argument-hint: <the things to join, or two prior /converge answers>
allowed-tools: mcp__terminals__converge, Read, Grep, Glob, Bash
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /glue

Join the trinkets. You have a few things that each already hold on their own: two earlier `/converge` answers, or two piles you point at. `/glue` asks the one new question: do they hold **together**? If yes, one combined trinket and the receipt. If they clash, the honest seam, the gluon that will not take, and the best partial.

What to join: **$ARGUMENTS**
(If empty, join the answers already settled in this conversation.)

This is the gluon verb. It does not invent a new check. It takes the same lock-in you already trust and runs it across the seam where two trinkets meet.

Run this protocol. Keep every word small.

1. **Name the pieces.** List the things you are joining. Each one is its own cluster, a thing that already holds: two prior answers, two plans, two reads of the same mess. Keep the strongest few. Pull out the key ideas inside each, so the seam has something to grip.
2. **Pool to the 7-grid.** Put the key ideas from all pieces onto one grid, up to 7. If two pieces overlap, that shared idea is one point, not two. If the pool runs over 7, cluster the rest in and say so. This pooled set is the union you are testing.
3. **Judge agreement across the seam.** For every pair, rate 0..1 how well they fit: support each other (toward 1), sit fine side by side (toward 0.5), or clash (toward 0). The pairs that matter are the cross-seam ones, an idea from one piece against an idea from another. That is where a join lives or dies. Be honest there. If `ix` is on PATH, search the user's context for each cross-seam pair (`ix "<idea A> <idea B>" <path> --json`). Each hit carries an `R`, how much structure, text, and meaning agree on it. High `R` is solid ground for a high score; low `R` means the join is weak or contested, so score it down. Feed that `R` into your judgment. No `ix`? Use `Grep` and `Glob`. The verb works offline.
4. **Run the lock-in on the union.** Call the `converge` tool with `{ ideas, coherence }` for the pooled set. Same engine, now testing whether the pieces hold as one. (No tool? Reason it through using `skills/converge/reference/`, same protocol, you do the arithmetic.)
5. **Read the result.**
   - **done = true (R=1):** the pieces glue. Every trio locked across the seam. Give the one combined trinket in plain words, the thing all the pieces become together. Then the receipt: which trios locked, the agree-meter `r`, the sure-o-meter `phi`.
   - **partial:** the pieces do not fully glue. Say so plainly. Name the seam, the one cross-piece pair that clashes, the gluon that will not take. Give the best partial: the largest group that does hold together, and what is left outside it. Then the one move that would make the join take: change one piece, drop the clashing idea, or keep them as two.
6. **Always show the receipt.** End with the witness: what the joined trinket claims, which trios back it, the verdict, and the one-line why. Never fake "done."

Keep the meaning of done = true precise: it says the pieces you pooled all agree with each other under the scores you gave. It checks your coherence judgments across the seam. It does not prove the combined thing is right in the world.

A join is only as honest as the seam. If two good trinkets will not hold together, that is a real finding, not a failure. Say it straight.

Output shape: the **joined answer** first (plain English), then **the receipt** as a card:

```
  ╭───────────────────────  terminals · glue  ──────╮
  │  joined  →  <the one combined thing, plain line>  │
  │  pieces  ▸ <piece> ▸ <piece> ▸ <piece>            │
  │  locked  ▸ <trio> ▸ <trio> ▸ <trio>               │
  │  seam    ▸ <the cross-piece pair that won't take> │
  │  r <0..1>   ·   phi <0..1>   ·   done = true ✓     │
  ╰───────────────────────────────────────────────────╯
```

Use the user's own plain words inside the card, no jargon, whatever their domain. Drop the `seam` line when the pieces fully glue. Show `partial` in place of `done = true ✓`, and let `seam` carry the gluon that would not take, when they don't.
