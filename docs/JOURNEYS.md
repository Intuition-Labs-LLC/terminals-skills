<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Real-world journeys — terminals for high-stakes business calls

terminals is not just for code. It is for the call you make when the stakes are real and the answer isn't obvious — a fundraise, a build-vs-buy, a reorg, a price change, a deal, a senior hire. This page maps **seven of those calls** to the person making them, the verb-chain they run, and the **receipt** they get back.

<p align="center">
  <img src="journeys.svg" alt="Seven decisions mapped to who decides, where they enter, the chain they run, and the receipt each one yields" width="760">
</p>

## How to read one journey

```
   who decides   →   where they enter   →   the chain (the loop)   →   the receipt
   ───────────       ─────────────────      ────────────────────       ──────────
   a persona         blank? own folder?     frame ▸ explore ▸           done = true,
                     just decide?           converge ▸ optimize ▸       or a lean +
                                            recommend                   the open question
```

- **enter** — you don't have to start at the beginning. Blank page → `/explore`. A folder of notes, a data room, a deck → `/frame`. Just want the call → `/recommend`.
- **the chain** — the "abstractive loop." One verb is rarely the whole job; a real decision threads two or three. The same chain serves many people, so the chain is an *attribute* of the journey, not the way the journeys are filed.
- **the receipt** — the witness. **done = true** means every angle locked and the answer holds. **partial** means it didn't all lock — you get the lean plus the one open question, never a faked "done."

## The seven journeys

| who decides | the call | enter | the chain | receipt |
|---|---|---|---|---|
| **The Founder** | which financing path, 9 mo runway | `/frame` | frame ▸ converge ▸ recommend | **partial** · r .81 |
| **The CEO / Board** | build, buy, or partner a core system | `/explore` | explore ▸ converge ▸ optimize | **done = true** · r 1.0 |
| **The Operating VP** | reorg to cut 15% opex | `/frame` | frame ▸ converge | **partial** · r .16 |
| **The GTM Leader** | re-price seats → usage | `/explore` | explore ▸ converge ▸ optimize | **partial** · r .44 |
| **The Investor** | Series B go / no-go from the data room | `/frame` | frame ▸ converge | **partial** · r .75 |
| **The Hiring Lead** | extend the VP Eng offer? | `/recommend` | recommend | **done = true** · r 1.0 |
| **The Consultant** | one staged market-entry rec for a client | `/recommend` | recommend | **done = true** · r 1.0 |

These are the engine's real numbers, reproduced on every test run. Below, each one in plain words.

### 1 · The Founder — the fundraise → **partial** (r .81)
Priced seed, a SAFE bridge, a strategic round, RBF, or cut burn — under "keep control, hit the A." Four of seven trios lock toward the **priced seed**: it funds the milestones and keeps control. What stays loose is the **strategic round** — partner distribution against the control you'd give up. The tool hands you the lean and leaves that one call where it belongs: with you.

### 2 · The CEO / Board — build-vs-buy → **done = true** (r 1.0)
Usage metering needed now, capital discipline on, six engineers better spent on the core. Every angle — speed, focus, cost, customer pull — points the same way. All seven trios lock: **buy the category leader**, integrate by API. An overdetermined call, and the receipt says so.

### 3 · The Operating VP — the reorg → **partial** (r .16)
Cut 15% of opex without stalling the roadmap or losing the top ICs. Only the cut itself locks. Protecting ICs, holding velocity, and morale all stay loose — because they genuinely fight the number at this depth. This is the honest one: the tool will **not** pretend a trilemma is solved. You can hit the number, or hold velocity and morale — not both here. That trade-off *is* the decision.

### 4 · The GTM Leader — the re-price → **partial** (r .44)
Pure usage, hybrid, or seats-plus-a-tier, under predictable-revenue + simple-comp + a market that already moved. The **hybrid** leads — it threads predictability, comp, and the land-and-expand motion (two trios lock there). Pure usage stays loose against predictability; seats stay loose against the market. The pick is clear; the loose trios are the alternatives you're consciously not taking.

### 5 · The Investor — the data room → **partial** (r .75)
NRR 128%, Rule-of-40 at 52, 78% margin, burn 1.4 — and two flags: logo concentration at 41%, founder-led sales with no VP yet. The fundamentals lock; the two risks stay loose. That's the read a good partner writes: thesis holds **except** concentration and the missing GTM leader — price those or get conviction before the IC. `/frame` reads the room and surfaces exactly the two things to underwrite.

### 6 · The Hiring Lead — the senior offer → **done = true** (r 1.0)
Scaled eng 20→150 at stage, shipped two rewrites on time, low-ego mentor on references, comp 15% over band but reasonable, fills a real gap, strong backchannels, starts in four weeks. Capability, culture, fit, and timing all line up. Clean call: **extend the offer.**

### 7 · The Consultant — the synthesis → **done = true** (r 1.0)
You take the wheel: wedge into mid-market, partner-led distribution, price for adoption, defer enterprise until SOC2, a small first team, a 12-month traction gate. One coherent staged motion — `/recommend` lands a confident pick and `/optimize` trims it to its cheapest equal form.

## The spread is the point

Three calls lock clean. Four come back partial. That ratio is **deliberate and honest** — most real business decisions carry a live trade-off, and the only useful tool is one that shows the seam instead of papering over it. A coherence tool that always returned "done = true" would be lying, and the test suite below would catch it.

```
   done = true  ███                         ceo · hiring · consultant   (it holds)
   partial      ████                        founder · vp · gtm · investor   (lean + open question)
```

## Run them yourself

Every journey is a runnable fixture, not a screenshot.

- **`mcp/tests/journeys.json`** — the seven cases: persona, entry, chain, the prompt, the seven ideas, and the coherence judgment given compactly (every pair starts at `base`; `align` groups agree; `clash` pairs disagree).
- **`mcp/tests/test_journeys.py`** — drives the **real engine** for each case and checks the **honesty contract**, not a memorized answer:
  1. a coherent decision returns `done = true`; a real trade-off returns `partial`;
  2. the clash that makes it partial **surfaces as a loose trio** (the seam is never hidden — this check is load-bearing: a strongly-coherent field can otherwise drag a lone clash into global lock and bury it);
  3. the locked set always equals the coherent set (no stale locks);
  4. no empty grid slot is ever locked;
  5. the chain never upgrades a `partial` into a fake `done`;
  6. every run is deterministic.

```
python -m pytest mcp/tests/test_journeys.py -v     # 45 checks, all green
```

## We chose this shape with the tool itself

The honest move: before writing this page, we ran `/converge` on the seven ways we *could* structure it — by persona, by verb-chain, by entry point, by expected receipt, by runnable fixtures, by contract tests, by one visual map. The real witness:

```
  ╭───────────────────────  terminals · converge  ──────────────────────╮
  │  answer  →  structure it persona-first, entry-routed, backed by      │
  │             runnable contract tests, with one visual map             │
  │  locked  ▸ persona + fixtures + honesty-tests                        │
  │          ▸ entry-point + expected-receipt + honesty-tests            │
  │          ▸ persona + entry-point + one visual                        │
  │  loose   ▸ "organize by verb-chain" — it sits in 3 of the 4 loose    │
  │            trios; the chain is a per-journey attribute, not the axis  │
  │  loose   ▸ runnable-fixtures vs the prose map — keep them in sync     │
  │  r 0.85   ·   phi 0.62   ·   partial — 3 of 7 locked                  │
  ╰──────────────────────────────────────────────────────────────────────╯
```

It came back **partial**, and we did **not** fake a `done = true` on our own framework. We followed the locked spine — this page is filed by **persona**, routed by **entry point**, backed by the **runnable contract tests**, with **one visual**. We followed the loose read too: the verb-chain is shown as an attribute of each journey, not as the way they're organized; and the fixtures and this prose map are cross-linked so the one maintenance seam stays closed. The tool told us how to represent itself, including where it doesn't fully cohere. That is the whole product in one move.
