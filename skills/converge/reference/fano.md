<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# The 7-grid (the Fano plane)

**Tiny words:** 7 ideas, 7 trios, every pair of ideas shares exactly one trio.

## What it is

The 7-grid is the **Fano plane** — the smallest projective plane, `PG(2,2)`. It has 7 points and 7 lines. Each line holds exactly 3 points, each point sits on exactly 3 lines, and **every pair of points lies on exactly one line**. In design terms it's the Steiner triple system `S(2,3,7)`.

That last property is the whole point: it is the most efficient way to cover every pair of 7 ideas once — **no pair is missed, no pair is counted twice.** When you check whether a set of ideas "hangs together," you only ever have to check 7 trios instead of all 21 pairs, and you're guaranteed full coverage.

## How the engine builds it

The 7 lines are the cyclic translates of the difference set `{0, 1, 3}`:

```
line k = { k, k+1, k+3 }  (mod 7)
```

Because `{0,1,3}` hits every nonzero remainder mod 7 exactly once as a difference, the 7 translates form a valid Steiner system. The engine asserts this in a test (`incidence_ok`): 7 lines, size 3, all 21 pairs covered once.

## Why exactly 7

The Fano plane is fixed at 7 points — that's what makes the geometry exact. So the engine maps your thoughtspace onto 7 points:

- **More than 7 ideas?** Cluster them into the 7 strongest and say so. We never pretend 30 ideas *are* 7.
- **Fewer than 7?** The extra grid slots stay empty and the coverage report shows it.

## The picture (the wiring / Heawood graph)

Draw the 7 points and the 7 lines as two rows of nodes, and connect each point to the lines it sits on. You get the **Heawood graph**: 14 nodes, every node degree 3, 21 edges. It's the bipartite "which idea sits in which trio" map.

## Source

From the published work — *Interactive Research Environments* (doi:10.5281/zenodo.18906942), where the Fano plane carries 7 reasoning trajectories and its 7 lines are the coherence constraints.
