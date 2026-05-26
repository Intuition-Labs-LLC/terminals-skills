<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# done = true (R=1) and the receipt

**Tiny words:** when every trio locks in, the answer is automatically sound — and it comes with proof.

## The done-condition

`R` is the done-flag. **`R = 1` means every one of the 7 trios locked in.** It's not a vote or a vibe; it's a structural fact: once all the coherence constraints hold at the same time, the set of ideas is mutually consistent.

The published *Convergence-Realizability Identity* states this sharply: **convergence under a closed witness loop is the same thing as being constructive** — i.e., type-safe — so you don't need a second checker to bless the answer. Reaching `R=1` *is* the check.

## The receipt (the witness)

Because the answer is constructive, it carries its own proof. Every verb returns a **witness**:

```
{ predicate, evidence, verdict, rationale }
```

- **coherent_lines** — the trios that locked (the evidence the answer holds).
- **incoherent** — any trio that didn't, with how loose it was.
- **verdict** — `R=1` or `partial`.
- **rationale** — the one-line why.

This is the **Curry–Howard** idea in practice: the answer (the program) and the proof (that it type-checks) are the same object. Most tools hand you a conclusion; this hands you a conclusion *plus* the structure that makes it sound.

## Realizers are not unique

Many different idea-arrangements can reach `R=1` — there's no single "the" proof. That's not a weakness; it's what `/optimize` exploits: among all the equally-sound arrangements, pick the cheapest one.

## The translator (the J-operator)

`/frame` uses the same identity in reverse. The user's own words and your structural form are **the same object in different coordinates**. The translator (the J-operator, `[terminals] ⊗ [techs] ⊗ [techs′]` in the lab) carries one to the other, so "what you want" becomes "what to actually run" without losing meaning.

## Honest note

The convergence papers are published draft preprints. The *abstractions* here — the done-condition, the witness, non-unique realizers — are taken from that work and cited by DOI; we don't claim the internal proofs are beyond review.

## Source

*Semantic Realizability: the Convergence-Realizability Identity* (doi:10.5281/zenodo.18992031) and *Interactive Research Environments* (doi:10.5281/zenodo.18906942).
