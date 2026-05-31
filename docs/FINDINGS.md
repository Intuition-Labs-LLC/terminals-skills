<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Findings: where your work is still open

When you point the bench at a body of work, the useful thing is not only what holds. It is what does not. The places that will not lock are the open spots, and they are worth keeping. This page says how the bench hands those back, as small honest objects you can keep, publish, or work next.

## Two things it makes

**A finding.** A condition the bench should have handled but did not, or a constraint your work keeps running into. It carries: what happened, the smallest repro (the ideas and the coherence scores that misbehaved), the receipt (`r`, `phi`, what locked, what stayed loose), and the general fix it points at, if you see one. A finding is honest about being a report, not a fix.

**A hypothesis.** A void in the work turned into a falsifiable claim. It carries: the claim in one line; its phase, which is a **hunch** by construction; the void it fills; and the **test** — the one thing that would move it from hunch to real, or kill it. No test, no hypothesis. That is the contract.

Both are siblings of the trinket. A trinket says whether it holds. A finding says where it did not. A hypothesis says what to test next.

## The emit step

Meaning is signal that has differentiated into *how to respond*. Noise is the default: still a thing, still read as something, just signal you have not differentiated yet. The bench emits when a run crosses from noise into meaning:

- `converge` comes back **partial** and names a loose trio. That loose trio is a void.
- a constraint trips a check. That is a finding.
- a void is sharp enough to state as a claim with a test. That is a hypothesis.

So the step is plain: after any pass, read the receipt for the holes, not only the wall. If a hole is worth carrying, emit it as a finding or a hypothesis, show it to the user, and offer to publish it in one shot.

## The contract (why these stay honest)

A finding and a hypothesis are phase-tagged and carry their own check: the repro for a finding, the test for a hypothesis. They never wear a "done" badge. This is the same spine as the engine. It does not fake `done = true`, and neither does anything it emits. A finding you cannot reproduce, or a hypothesis you cannot test, does not ship. That is what keeps this a research instrument and not a fortune-cookie machine.

## The loop (how the bench gets better from you)

A published finding is an edge case for the next update's convergence checks. A published hypothesis is a void someone can go close. The people using the bench find the conditions the maintainers did not, and each one becomes a check the next version carries. The tool improves from its use, in the open.

Publish in one shot: [open an edge-case report](https://github.com/Intuition-Labs-LLC/terminals-skills/issues/new?template=edge-case.yml). Your agent already holds the failing case from the session, so it can fill the form for you. Strip anything private first — everything in the report is data you mean to share.
