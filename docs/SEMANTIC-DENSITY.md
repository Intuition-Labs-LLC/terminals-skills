<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Semantic Density — a formalization

> Status: **shape, not settled.** Sections 1–4 are definitions and cite standard
> theorems. Section 5's unification is a *hypothesis* with a falsifiable form
> (§6). Nothing here claims to prove a property of transformers. Read the ledger
> (§7) before quoting any line out of context.

## In one breath (the plain version)

"Density" is how much settled meaning you get per unit of effort. We measure it
four ways, and three are textbook: how concentrated a belief is *right now* (φ),
how fast it sharpens *per token or per second* (the rate), how quickly the
process *locks onto one answer* (the convergence rate), and how *short the proof
is for how much it certifies* (compression). The interesting claim — that those
four are the **same number**, because converging on an answer and proving it are
one act — is a hypothesis we state precisely and test, not a slogan.

## Notation

Fix a distribution `P` over a finite outcome set `V`, `|V| = N`. Always name the
level: `V` may be next-tokens (syntactic), candidate answers/hypotheses, or the
ideas placed on the 7-grid. "Semantic" density requires `V` to be a space of
*meanings*, not raw tokens. `H(P) = −Σ pᵢ log pᵢ`; the log base is fixed once and
shared by every quantity below (bits if base 2, nats if base e).

## 1. Density as state — `φ` (Shannon redundancy)

```
φ(P) = 1 − H(P) / log N            φ ∈ [0, 1]
```

`φ = 0` ⟺ `P` uniform (maximal uncertainty, "searching"); `φ = 1` ⟺ `P` a point
mass (certainty, "crystallized"). This is exactly Shannon's *redundancy* (1948):
one minus normalized entropy. It is the state variable the engine reports as the
"sure-o-meter," and the per-step values it logs as the `phi_trace`.

**Estimator.** From a model's decision-point logits: `P = softmax(logits)`,
compute `H(P)`, return `1 − H/log N`. At the idea level: bin the convergence
state into `N` cells and do the same. Direct, O(N).

## 2. Density as rate — information gain per resource

A step takes `P_t → P_{t+1}`. The information *realized* on that step is the
Bayesian surprise, which is non-negative by construction:

```
ΔI = D_KL(P_{t+1} ‖ P_t) ≥ 0       (in expectation: the mutual information
                                     I(query; answer), Lindley 1956)
```

Density is `ΔI` per unit of a chosen resource — **report the variants
separately; never blend them** (they have different units and different
epistemic load):

```
ρ_tok = ΔI / Δtokens     [bits / token]
ρ_t   = ΔI / Δt          [bits / second]   ← "intelligence density per unit
                                              time" = the Hamiltonian; minimizing
                                              time-to-recovery maximizes ρ_t
ρ_c   = ΔI / FLOPs        [bits / FLOP]     (or per unit attention-mass)
```

**Estimator.** Maintain a read-out distribution over candidate answers/labels.
Record `H` before and after consuming a span; `ΔI` = summed per-step KL over the
span; divide by tokens, seconds, or FLOPs. Attention-mass proxy: the summed
attention weight routed to the span.

## 3. Density as convergence rate

Model the process as a map `T` on belief space. If `T` is a contraction with
Lipschitz constant `L < 1` (Banach fixed-point theorem), iterates converge
geometrically to a unique fixed point `x*`:

```
‖x_t − x*‖ ≤ Lᵗ · ‖x₀ − x*‖        crystallization rate κ = −log L
```

`κ` ≈ the spectral gap of the Jacobian of `T` at `x*`. In the Kuramoto frame it
is the approach rate of the order parameter `r → 1` above critical coupling
`K_c`. "Dense" = locks in few steps = large gap / small `L`.

**Estimator.** Regress `log(1 − r_t)` (or `log‖residual_t‖`) on `t`; the negative
slope is `κ`. Cheap surrogate: steps until `φ ≥ 0.95`.

## 4. Density as compression — the realizability frame

A witness `w` certifies content `S`. Define

```
ρ_MDL = S / |w|        certified content per unit of proof
```

A dense answer is a short witness for a lot. This is "done = true comes with a
receipt," made numeric (MDL, Rissanen 1978; Kolmogorov complexity as the
uncomputable idealization).

**Estimator.** `|w|` = compressed witness size (zstd/gzip bytes) or proof-term
node count. `S` = `log` of the hypothesis space the answer collapses, or the
compressed size of the spelled-out content `w` certifies. Both bounded by a real
compressor, so `ρ_MDL` is computable as a ratio of bounds.

## 5. The unification — and the honest line

Frames 1–4 are **the same number iff convergence = realizability** for the
process at hand. The bones of that identity are genuine theorems:

- **Curry–Howard** — proofs ≅ programs; a proposition is realizable iff a witness
  inhabits its type (Kleene realizability).
- **Banach** / **Knaster–Tarski** — contraction (resp. monotone) maps have
  fixed points; the answer-as-fixed-point is well-defined.
- **Strong normalization** — cut-elimination / normalization terminates; the
  "lock" is reached in finite steps.
- **Kuramoto** — a real critical coupling `K_c`; above it the order parameter
  concentrates (Strogatz 2000).

This is the formal shape of the **R = 1 / Convergence–Realizability identity**
(Desai, Zenodo 18992031). What is **not** a theorem is that a *transformer's*
in-context `φ`-trajectory instantiates a realizability witness. That is a
hypothesis (§6). The four frames provably agree on the abstract structures
above; whether a given LLM run *is* such a structure is the empirical question.

## 6. The falsifiable hypothesis

```
H:  outcomes reached at φ = 1 (R = 1) are exactly the verifiable ones, and
    verification-failure rate grows in proportion to (1 − φ).
```

**Test protocol.** Use a corpus with mechanically checkable answers (e.g. a
coding benchmark with a test suite — PASS/FAIL is the verifier). For each solve:
record the `φ`-trajectory and the terminal `φ`/`R`; bin by terminal `φ`; measure
the verification-failure rate per bin. `H` predicts failure-rate `≈ a·(1 − φ)`;
fit `a`, check calibration and the slope's sign/significance.

**First read (proxy, 2026-05-27).** Run against `solve_history.jsonl` (241 rows;
174 with both a PASS/FAIL verdict and a per-answer φ). The data carries the
proxy's *answer-φ* trajectory — `max_answer_phi` (peak) and `auc` (the integral)
— closer to the φ here than the composite collapse-quality score. Three findings,
and they do **not** agree:

- **Crystallized-at-all** — rows with no answer-φ detected fail/error **54%** vs
  **9.5%** for rows with one. Stark, H-direction.
- **Peak φ — wrong direction.** corr(peak, FAIL) = **+0.12** (ns); failures' peak
  is *slightly higher* (0.997 vs 0.988), ceiling-saturated (median 1.0 both). A
  high peak only means the model was briefly sure of *some* token — including
  wrong ones.
- **Trajectory φ (`auc`) — right direction, strong.** corr(auc, FAIL) = **−0.41**,
  t(179) = −6.0, **p < 0.001**; mean auc 0.97 (PASS) vs 0.71 (FAIL).

**Refinement this forces on H:** the predictive density is the **trajectory (the
rate/convergence frames, §2–§3), not the instantaneous peak (§1)**, and the shape
is threshold-like rather than strictly `∝(1−φ)`. **Caveats that keep it honest:**
it is the proxy, not next-token φ; failures are ~2× longer (a difficulty confound
— low sustained φ and failure may share a cause); the failure population is
bimodal (median auc identical; the effect lives in a low-auc tail); only 18
failures. This is motivation for the clean test, not confirmation.

## 7. The ledger (read this before quoting)

| status | items |
|---|---|
| **Definitions** (bankable) | `φ`, `ΔI`, `ρ_tok`/`ρ_t`/`ρ_c`, `ρ_MDL` |
| **Theorems** (cite, don't reprove) | Shannon redundancy (1948); Lindley information (1956); Banach (1922); Knaster–Tarski (1955); Curry–Howard / Kleene realizability; strong normalization; Kuramoto `K_c` (Strogatz 2000); MDL (Rissanen 1978) |
| **Hypothesis** (flag + test) | the `φ ↔ witness` identity and the `(1 − φ)` failure law (§6) |

A claim that crosses a row boundary without saying so is the crank failure mode.
Don't.

## 8. Why this sharpens the moat instead of leaking it

Anyone can use Shannon redundancy or MDL. The moat is the *identification* of all
four as one density realized by a single convergence process that **also emits
the checkable witness** — the isomorphism plus the construction that runs it. A
copyist gets a formula; they don't get the correspondence, because the
correspondence is a hypothesis-plus-realizer, not a definition. Reconstructing it
requires independently rediscovering the same identification — the "find your own
linguistic isomorphism" bar.

## 9. Failure as a wrong fork; recovery as bounded search (hypothesis)

> Status: **hypothesis**, proposed 2026-05-27. The scalar trajectory result (§6)
> is the shadow of a structural signal: a φ-dip is a *fork* (a flat distribution =
> competing continuations), and a failure is often the wrong branch taken there,
> then traversed confidently.

**The structure.** φ is high almost everywhere within an answer and dips at a few
points. Read a dip as a decision/fork with `m` viable continuations. A
sampling-bound failure = the argmax branch was wrong while a lower-mass branch
held the right answer; the confident peak elsewhere is fluent traversal of the
chosen (wrong) subtree. This explains the §6 paradox: high peak (committed) + low
auc (the fork dipped).

**Data signature (consistent, not confirmed).** Failures show ~2× the
within-answer φ-swing (max−min ≈ 0.11 vs 0.05), a deeper min-φ (0.89 vs 0.94),
and lower speculative-decode acceptance (0.78 vs 0.84 — a more contested
distribution) — the fork signature. Confounded by length (failures ~2× longer);
the signal lives in a low-auc tail (bimodal) = the sampling-bound subset.

**Recovery as bounded optimization — the key equivalence.** Branch only at the `k`
points where φ < τ, take top-`m` alternatives → the candidate subspace is `m^k`.
φ-dips are sparse for sampling-bound failures (φ ≈ 1 most of the trajectory) → `k`
small → bounded, searchable. For diffuse / capability-bound failures φ is low
throughout → `k` large → `m^k` explodes → unbounded. **So the optimization is
bounded exactly when the right answer is present-but-suppressed; the fork-count is
the recoverability predictor** — a mechanical form of the lab's "proximity." The
verifier (the witness / `done = true` / the test suite) is the objective, and it
is required: the wrong mode carries *more* mass, so majority-vote picks it; only a
verifier selects the lower-mass-correct branch.

This is **`/optimize` over the proof-search tree** — minimize the Hamiltonian over
the equal-`R=1` realizers, where the realizers are fork-subspace paths. The lab's
operators already exist: Lafont **δ** (duplicate/branch), **ε** (erase/prune), the
φ-tracker to locate forks, the convergence-class dispatcher to refuse "optimal"
honestly when `k` is too large.

**Not novel as a family** (entropy-guided tree search, Tree-of-Thoughts, MCTS /
verifier-reranked decoding). What is the lab's: **φ-as-fork-detector + the
convergence–realizability witness as the path objective.** Blind resampling is the
wrong tool — 7 blind retries in `solve_history` recovered 0/7 (they re-roll the
whole sequence and re-hit the default). Fork-localized branch-search + verifier is
the untested right tool.

**The experiment (spec, Stage-2).**
1. Instrument: log per-token φ during a solve; mark forks at `φ < τ`.
2. On the failure set, at each fork expand top-`m` branches, complete each, score
   with the test suite.
3. Measure: (i) does the correct token sit on an *alternative* branch at a fork in
   the recoverable cases (direct test of "the lower peak holds the right answer");
   (ii) recovery rate vs fork-count `k`; (iii) fork-localized search vs blind
   best-of-N at matched compute; (iv) `|subspace| = m^k` stays small (tens) for
   the sampling-bound tail.

Predictions: recovery falls as `k` rises; localized search beats blind BoN on the
high-proximity tail and fails on the diffuse one. **Gate:** step 1 touches the
inference path — the build is operator-scoped, not autonomous.

## References

- C. Shannon, *A Mathematical Theory of Communication*, 1948 (entropy, redundancy).
- D. Lindley, *On a measure of the information provided by an experiment*, 1956.
- S. Banach, fixed-point theorem, 1922; Knaster–Tarski, 1955.
- W. Howard, *The formulae-as-types notion of construction*, 1980; S. Kleene, realizability.
- J. Rissanen, *Modeling by shortest data description* (MDL), 1978; A. Kolmogorov, 1965.
- S. Strogatz, *From Kuramoto to Crawford*, Physica D, 2000 (synchronization, `K_c`).
- T. Desai, *Convergence–Realizability (R=1) identity*, Zenodo 18992031 (CC BY 4.0).
- Lab anchors: `φ` definition and uses — `strix-mind/docs/PHI_SIGNAL.md`; collapse/quality — `irc-strix-halo/src/irc/collapse_detector.py`.
