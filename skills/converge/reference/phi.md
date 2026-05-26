<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# The sure-o-meter (phi)

**Tiny words:** how sure the system is — 0 = lost, 1 = it knows.

## What it is

`phi` measures how *peaked* things are:

```
phi = 1 − H(P) / log|V|
```

`H(P)` is the entropy of a distribution `P`; `log|V|` is the most entropy it could have. When `P` is spread out (lots of options, no commitment), `H` is high and `phi` is near 0 — "searching." When `P` collapses onto one choice, `H` drops and `phi` rises toward 1 — "knowing."

This is the same signal the lab reads live while a model generates text: a low-`phi` token is one the model is unsure about; a `phi`-spike is the moment it commits. The flip from low to high `phi` is the **click** — searching turning into knowing.

## How it shows up here

In the 7-grid, `P` is the spread of the 7 phases around the circle. While the ideas are scattered, the spread is wide, `H` is high, `phi` is low. As the lock-in pulls them together, the spread narrows, `H` falls, and `phi` climbs toward 1. The engine records a `phi_trace` over the run so you can *see* the click happen.

## phi vs the agree-meter r

They move together but mean different things:
- **r** (agree-meter) — how aligned the spinners are.
- **phi** (sure-o-meter) — how concentrated, read as entropy collapse.

Both rising toward 1 is the signature of a real convergence, not a forced one.

## Source

The `phi = 1 − H/log|V|` signal is the lab's decode-time convergence measure; here it's the circle analog over the 7 phases. It pairs with the collapse picture (searching → crystallizing) that the grokker line of work tracks.
