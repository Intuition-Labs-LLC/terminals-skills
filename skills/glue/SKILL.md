---
name: glue
description: Use when two or more things that each already hold need to become one, and the real question is whether they hold together ("do these two plans fit", "merge these answers", "can we run both", "join these"). Treats each as its own cluster and converges across the seam, returning one combined answer (done = true / R=1) or the honest seam that won't take plus the best partial. Use glue to join pieces that already stand; use converge for one fresh pile of ideas, and recommend when you should make the call yourself.
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Glue

You have a few things that each already hold: two earlier answers, two plans, two reads of one mess. The new question is whether they hold **together**. Join them into one, and show the receipt. If they clash, name the seam straight.

This is the gluon verb. It reuses the lock-in you already trust and runs it across the seam where the pieces meet. It adds no new check.

## The protocol

1. **Name the pieces.** List what you are joining. Each is its own cluster, a thing that already holds. Pull the key ideas inside each, so the seam has something to grip.
2. **Pool to the 7-grid.** Put the key ideas from all pieces onto one grid, up to 7. A shared idea is one point, not two. Over 7 means cluster the rest in and say so. This pool is the union you test.
3. **Judge agreement across the seam.** Rate every pair 0..1: support (toward 1), coexist (toward 0.5), clash (toward 0). The cross-seam pairs, an idea from one piece against one from another, are where a join lives or dies. If `ix` is on PATH, search the user's context per cross-seam pair (`ix "<A> <B>" <path> --json`); each hit's `R` is how much structure, text, and meaning agree on it, so high `R` backs a high score and low `R` scores the join down. Feed that `R` in. No `ix`? Use Grep and Glob. It works offline.
4. **Run the lock-in on the union.** Call the `converge` tool with `{ ideas, coherence }` for the pooled set. Same engine, now testing the pieces as one.
5. **Read it.** `R=1` (every trio locked across the seam) means give the one combined trinket plus the receipt. `partial` means the pieces do not fully glue: name the seam (the gluon that will not take), give the best partial (the largest group that holds, and what stays outside), and the one move that would make the join take, or the call to keep them as two.
6. **Always show the receipt** (the witness): the joined claim, the trios that back it, the verdict, the one-line why. Never fake done = true.

Remember what done = true means: the pieces you pooled all agree with each other under your scores. It is a check on your coherence judgments across the seam. It does not prove the combined thing is right in the world.

A join is only as honest as the seam. Two good trinkets that will not hold together is a real finding. Say it straight.

Joined answer first, in plain words. Receipt second.

## Going deeper (load only if needed)

- The lock-in this verb reuses (how agreement becomes one answer): `../converge/reference/kuramoto.md`
- The 7-grid you pool onto (why 7, and "nothing lost"): `../converge/reference/fano.md`
- What "everything locked" does and doesn't establish: `../converge/reference/realizability.md`
- The bench picture: a gluon is the join between two tools' trinkets: `../../docs/WORKBENCH.md`
