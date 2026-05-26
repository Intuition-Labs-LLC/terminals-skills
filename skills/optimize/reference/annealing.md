<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# The polish (bounded annealing)

**Tiny words:** shake the answer toward a cheaper equal form, then stop.

## What it is

**Simulated annealing** is a search that starts willing to try worse moves and slowly gets pickier, so it can climb out of a local rut before settling. Here it shuffles which idea sits on which grid point, looking for an arrangement that's still sound but costs less on the cost-meter.

The "get pickier over time" is a cooling schedule. We use **log cooling**:

```
temperature T(k) = 1 / log(k + 2)
```

It cools slowly enough to explore, and the step budget is **bounded** — a fixed `max_steps` — so the polish **always halts**. That bounded-recurrence guarantee comes straight from the published *Bounded Informational Time Crystals* work: the loop recurs, but within fixed bounds, so it can't run forever.

## The hard rule

Every candidate arrangement is re-checked for done = true. **Any move that would unlock a trio is rejected outright** — annealing only ever wanders among sound arrangements. So `R_held` comes back true: the answer you started with is still the answer, just cheaper.

## What you get back

```
{ best, cost_before, cost_after, R_held }
```

If `cost_after < cost_before` and `R_held` is true, the polish worked. If nothing got cheaper, the first form was already best, and it says so.

## Source

*Bounded Informational Time Crystals* (doi:10.5281/zenodo.18906944) for the bounded, halting recurrence; the cost-meter it minimizes is in `hamiltonian.md`.
