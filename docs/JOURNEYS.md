<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# What people use terminals for

A hard call. One word. A straight answer — and when it isn't fully settled, it tells you the one thing still open instead of faking it.

The answer comes back one of two ways:

- **settled** — everything lines up. Here's the call.
- **a lean + one open thing** — most of it lines up. Here's where it points, and the one question still pulling against it. That part stays yours.

---

### The founder — "how should I raise?"
9 months of cash. A $4M priced seed, a cheaper $2M bridge, a strategic round from a partner. You want to keep control and hit the Series A.
Type **`/recommend`** with the three options.
→ Raise with the **bridge or the priced round** — both keep you in control. Skip revenue-based financing; it fights everything else. Bridge vs priced is the one call left to you.

### The CEO — "build it or buy it?"
You need usage billing now. Building it ties up six engineers for three quarters.
Type **`/explore`** the options, then **`/converge`**.
→ **Settled: buy the category leader.** Speed, focus, cost, and what customers need all point the same way.

### The VP — "how do I cut 15% without breaking the team?"
Merge two teams, cut a weak product line, offshore support — while protecting your best people and keeping the roadmap moving.
Type **`/frame`** your org notes, then **`/converge`**.
→ Only the cut itself holds. Protecting your top people, keeping speed, and morale all pull against the number. It won't pretend that away: you can hit 15%, or hold the team — not both this deep. **That trade-off is the decision.**

### The GTM lead — "how should we price?"
Move from seats to usage. The board wants predictable revenue, sales comp has to stay simple, and competitors already moved.
Type **`/explore`**, then **`/converge`**.
→ Lean to the **hybrid** — a platform fee plus usage. It keeps revenue predictable and comp simple. Pure usage and plain seats are the two you're choosing not to take.

### The investor — "is this deal a yes?"
A data room: great retention, healthy margins — but the top three customers are 41% of revenue and there's no head of sales yet.
Type **`/frame`** the data room.
→ The fundamentals hold. Two things stay open: the **customer concentration** and the **missing sales leader**. Price those, or get conviction, before you say yes.

### The hiring lead — "should I make this hire?"
A VP of Engineering who's scaled a team before, ships on time, great references — but asking 15% over band.
Type **`/recommend`**.
→ **Settled: extend the offer.** Track record, culture, the gap she fills, and timing all line up.

### The consultant — "what do I tell the client?"
A pile of discovery notes; the client needs one clear plan to enter the market.
Type **`/recommend`** and let it take the wheel.
→ **Settled:** wedge into mid-market, partner-led, priced for adoption, with a 12-month proof gate before scaling up. One clean plan.

---

## All seven at a glance

<p align="center">
  <img src="journeys.svg" alt="Seven decisions: who decides, where they start, the words they run, and whether the answer came back settled or with an open question" width="760">
</p>

*(In the picture, "done = true" is just **settled**, and "partial" is **a lean + an open question**. `r` is how tightly the parts agree.)*

Three come back settled; four come back with an open question — because most real calls carry a live trade-off, and a tool that always says "settled" is lying.

Every answer here is a **real run** — same answer every time, and it never says settled unless it is. The cases are in [`mcp/tests/journeys.json`](../mcp/tests/journeys.json); run them with `pytest mcp/tests/test_journeys.py`.
