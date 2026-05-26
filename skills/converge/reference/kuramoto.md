<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# The lock-in (the Kuramoto model)

**Tiny words:** nudge the ideas in each trio until they agree; the agree-meter tells you how locked-in they are.

## What it is

Picture each idea as a spinner with a phase (an angle). The **Kuramoto model** couples spinners so they pull on each other. Ideas that agree pull into the same phase; ideas that clash push apart. Run it for a bit and the spinners settle.

The **order parameter** `r` is the agree-meter:

```
r = | average of e^(i·phase) over the points |      # 0 = scattered, 1 = all aligned
```

You read `r` two ways:
- **global r** — how aligned the whole set is.
- **per-trio r** — how aligned one line's 3 ideas are. A trio is **locked** when its own `r` passes the threshold (default 0.85).

## How agreement becomes a force

You give the engine a coherence number `c` in `[0,1]` for each pair. It becomes a coupling:

```
K = 2c − 1        # c>0.5 attracts (agree), c<0.5 repels (clash), c=0.5 neutral
```

So a pair that genuinely agrees pulls together; a pair that clashes pushes apart and **keeps its trio from locking**. That's why the result is honest: you can't force a clashing trio to lock just by wanting it to.

## Why a short run is enough

The spinners have no drift of their own (zero natural frequency) — the only motion is the pull/push of coupling. That makes the system settle to a **fixed point** (a Banach-style attractor) rather than wandering forever, so a finite, bounded run reads the true answer. The settling-to-one-attractor behavior is validated empirically in the published work over thousands of trials.

## Source

From the published work — *Material Reality* (doi:10.5281/zenodo.18993958) for Kuramoto convergence + the Banach fixed-point guarantee, and *Bounded Informational Time Crystals* (doi:10.5281/zenodo.18906944) for the bounded, halting recurrence.
