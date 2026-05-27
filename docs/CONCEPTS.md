<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Concepts — the whole thing in small words

Everything Terminals does sits on three words. If you only read one page, read this.

## Point · Line · Lock

- a **Point** is one idea — seven sit on a grid
- a **Line** is a trio of ideas that has to agree
- a **Lock** is the moment a trio snaps into agreement

When all seven trios Lock, the answer is **done = true** — sound, not guessed.
Nothing else to learn. That's the entire surface, whether *you* type the word or
the *agent* reaches for it.

## The two meters

- **agree-meter `r`** — 0 = the ideas are all over the place, 1 = fully locked in.
- **sure-o-meter `φ`** — how concentrated the answer is. 0 = still searching, 1 = crystallized.

When `r` reaches 1, every trio agrees — that's **R = 1**, done = true.

## The five words

| word | tiny meaning | what you get |
|---|---|---|
| `/explore` | open it up | every angle, spread out on purpose — before you pick |
| `/converge` | bring it together | one right answer **+ the receipt** |
| `/optimize` | make it the best one | same answer, the cheapest and cleanest version |
| `/recommend` | you decide | it runs the whole path and hands you its pick + the receipt |
| `/frame` | start from my stuff | point it at your folder; it pulls your context in and goes |

## The receipt (the witness)

Every word hands back a **witness** — a proof you can check, not just a prompt:
the answer, the trios that back it, how sure it is (`r`, `φ`), and what (if
anything) is still loose. If it can't lock everything, it says so plainly and
shows the best partial. **It never fakes "done."** That honesty is the product.

## The smallest-word glossary

The hard name on the left is real math; the tiny word is what we show you. Never
needs the hard name to *use* it — that stays in the receipts and the papers.

| the real thing | tiny word | one-line plain version |
|---|---|---|
| Fano plane (PG(2,2)) | **the 7-grid** | 7 ideas, 7 trios; every pair of ideas shares exactly one trio |
| Steiner triple system S(2,3,7) | **the trios** | the 7 trios that cover every pair once — max coverage, zero waste |
| Kuramoto synchronization | **the lock-in** | nudge ideas in the same trio until they agree |
| order parameter `r` | **the agree-meter** | 0 = scattered, 1 = locked in |
| R = 1 (Convergence–Realizability identity) | **done = true** | when everything locks, the answer is automatically sound |
| φ = 1 − H/log\|V\| | **the sure-o-meter** | how sure the model is of the next step (0 lost … 1 knows) |
| collapse / crystallization | **the click** | the moment "searching" flips to "knowing" |
| realizability witness (Curry–Howard) | **the receipt** | the answer comes with proof it hangs together |
| interaction combinators (γ/δ/ε) | **build / split / drop** | combine ideas, fan them out, throw out the dead ones |
| J-operator | **the translator** | turns "what you want" into "what to actually run" (that's `/frame`) |
| the Hamiltonian (min time-to-recovery) | **the cost-meter** | how much an answer costs in time/tokens/mess — lower is better |
| bounded log-cooled annealing | **the polish** | shake the answer toward its cheapest equal-but-better form, then stop |

## Searching → knowing

The whole motion is one flip: a question starts **searching** (low `φ`, ideas
scattered) and ends **knowing** (high `φ`, trios locked). The lock-in is that flip,
made visible — see the animation in the [README](../README.md), where the meters
are the engine's real numbers.

## Going deeper

- Why "everything locked" means the answer is sound, and the math that backs each
  meter: [`SEMANTIC-DENSITY.md`](SEMANTIC-DENSITY.md).
- What the plugin can and can't do, and the safety posture: [`SECURITY.md`](SECURITY.md).
