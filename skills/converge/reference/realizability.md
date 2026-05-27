<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# done = true (R=1) and the receipt

**Tiny words:** when every trio locks in, the ideas you gave all agree with each other, and you get a receipt that shows it.

## The done-condition

`R` is the done-flag. `R = 1` means every one of the 7 trios locked in. It is a structural fact about the coherence you supplied: once all the pairwise agreements are high enough at the same time, the set of ideas is mutually consistent.

Read that boundary carefully. The coherence scores are your input. `R=1` certifies that those scores hold together. It does not certify that your scores were right, and it does not prove the decision is correct in the world. That part stays with you.

The published *Convergence-Realizability Identity* states the structural half sharply: convergence under a closed witness loop is constructive, so the certificate travels with the answer. Reaching `R=1` is the consistency check on the coherence you gave. It is one check on one input. Whether your coherence judgments match reality is the separate, upstream question the receipt cannot see.

## The receipt (the witness)

Every verb returns a witness:

```
{ predicate, evidence, verdict, rationale }
```

- **coherent_lines:** the trios that locked (the evidence the answer holds together under your scores).
- **incoherent:** any trio that did not, with how loose it was.
- **verdict:** `R=1` or `partial`.
- **rationale:** the one-line why.

This is the **Curry-Howard** idea in practice: the answer and the certificate that it is internally consistent are the same object. Most tools hand you a conclusion. This hands you a conclusion plus the structure that shows it holds together, given what you fed it.

## Realizers are not unique

Many different idea-arrangements can reach `R=1`. There is no single proof. That is what `/optimize` exploits: among all the equally-coherent arrangements, pick the cheapest.

## The translator (the J-operator)

`/frame` uses the same identity in reverse. The user's own words and your structural form are the same object in different coordinates. The translator (the J-operator, `[terminals] ⊗ [techs] ⊗ [techs′]` in the lab) carries one to the other, so "what you want" becomes "what to actually run" without losing meaning.

## Honest note

The convergence papers are published draft preprints. The abstractions here (the done-condition, the witness, non-unique realizers) are taken from that work and cited by DOI. We do not claim the internal proofs are beyond review. And to keep the core claim precise: `R=1` proves the consistency of your coherence scores, not the real-world correctness of the decision.

## Source

*Semantic Realizability: the Convergence-Realizability Identity* (doi:10.5281/zenodo.18992031) and *Interactive Research Environments* (doi:10.5281/zenodo.18906942).
