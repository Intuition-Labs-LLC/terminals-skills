<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# The cost-meter (the Hamiltonian)

**Tiny words:** how much an answer costs. Lower is better.

## What it is

Once an answer is sound (done = true / R=1: every trio of ideas locked together), there's usually more than one version of it that holds. "Sound" here means the ideas cohere under the coherence you supplied; it certifies internal consistency, not real-world correctness. The **cost-meter** scores each version so you can pick the cheapest. In the lab this is the **Hamiltonian**, the quantity you minimize. Its headline reading is *time-to-recovery*: how fast you get to a working answer. Cheaper means fewer moving parts, less effort, less noise.

## How the engine scores it

For a converged arrangement the cost is:

```
cost = sum over trios of (1 − trio_agree)      # how hard each trio had to work
     + a small term for how long the trios took to lock   # less effort = cheaper
```

A tighter, faster-locking arrangement scores lower. `/optimize` searches the equally-sound arrangements for the minimum and reports `cost_before → cost_after`.

## The rule it never breaks

The cost-meter only ranks arrangements that are **already** done = true. `/optimize` will not accept a cheaper arrangement if it drops a trio that was locked. **Correct first, cheap second.** Soundness is held fixed while cost drops.

## Source

The Hamiltonian (minimize time-to-recovery = maximize useful work per unit time) is the lab's core optimization target; `/optimize` applies it to the set of sound arrangements the realizability identity proves exist.
