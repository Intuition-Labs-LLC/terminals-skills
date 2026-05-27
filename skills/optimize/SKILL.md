---
name: optimize
description: Use right after a coherent answer is reached (done = true / R=1) to find its cheapest, cleanest equal form (fewer moving parts, less effort, lower noise) without breaking it. Reach for this when an answer holds together but feels heavier than it needs to be, or the user says "simplify this" / "make it cleaner" / "trim it" / "can this be simpler?" about an answer just given.
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Optimize

The answer already holds together. Now make it the **best** one, the cheapest, cleanest version of that same answer. The math gives many equally-coherent forms. Pick the one that costs least.

## The protocol

1. **Start from a done answer.** You need a converged result with done = true. If there isn't one, converge first.
2. **Polish it.** Call the `optimize` tool with the whole converged object. It searches equal-but-cheaper arrangements on a bounded schedule (so it always stops) and **refuses any move that breaks done = true**.
3. **Read the cost.** It returns `cost_before`, `cost_after`, `R_held`. Held and cheaper means the polish worked.
4. **Hand back** the cleaned-up answer in plain words, then one line: "still done = true, cost X to Y." If nothing got cheaper, say so. The first form was already best.

Correct first, cheap second. Never trade away done = true for cost.

## Going deeper (load only if needed)

- The cost-meter (the Hamiltonian): `reference/hamiltonian.md`
- How the polish searches and why it always stops: `reference/annealing.md`
