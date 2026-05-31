<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Networks of algebras

## The plain version

Most people with a strong intuition go hunting for one clean idea that explains everything. It's a trap. Many ideas fit the same evidence, nothing singles out the true one, and you can't check a thing that explains everything.

We do the opposite. We keep a set of small tools, each one doing a single clean thing that always behaves the same way — and a frame that says which tools fit together. The tools are the verbs. You snap them together and build any answer you need, instead of forcing everything through one master idea.

That's the whole move. Not one abstraction. A network of small, checkable pieces, and a frame that holds them.

## The formal version

Read this layer only if you want the math. The plain version above is the whole idea.

- An **algebra** is an **option** is, formally, a **tech**: a closed way of composing moves that always returns a well-formed result. Each verb is one. `converge` is an algebra. `mint` is an algebra. They never hand you a malformed thing — that closure is what makes them composable.
- A **network of algebras** is those algebras as the objects, the verbs as the operations between them — `∘` (run in sequence) and `⊗` (run at the same time) — and **coherence-R** as the glue that says when two snap together. `R = 1` means the pair holds; the joint locks.
- The network is a **sheaf**: local algebras that glue into one global answer exactly when their overlaps agree. `done = true` is the global section existing. `partial` is an overlap that won't glue, named out loud instead of hidden.
- One network, two frames. **ix** reads the network as an *objective reference* — the algebras as they are, searchable, settled. **terminals-skills** runs the network as *subjective doing* — the same algebras, as moves you make. Objective frame paired with subjective frame, over one substrate.

## Why a network beats one abstraction

A single master abstraction is **underdetermined**: many candidates fit the same data, and convergence alone doesn't single out the true one. (This is the standing critique of "everything converges to one representation.")

A network fixes both halves of that:

- every piece is **checkable on its own** — each algebra holds independently, so you never trust the whole on faith;
- the **frame supplies the constraint** that picks the right composition — the thing the lone master-abstraction lacks.

Convergence is the commodity. The frame is the moat. The frame is what lets you see past the patterns you can already see.

## It runs

This isn't a picture. The glue is real and checkable:

- the sheaf gluing at `R = 1` — `matryoshka_sheaf.py` (both sheaf axioms self-check);
- the order parameter over the network — the `converge` engine in this repo, which returns `R`, `phi`, the locked trios, and an honest `partial` when the network doesn't glue.

A construction, not a claim about physics. The math it shares with gauge theory and sheaves is structural — the same shape, pointed at meaning instead of matter.
