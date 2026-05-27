<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

<p align="center">
  <img src="docs/fano.svg" alt="The 7-grid: seven ideas, seven trios, every pair of ideas sharing exactly one trio" width="300">
</p>

<h1 align="center">Terminals</h1>

<p align="center"><b>Five small words that turn a messy pile of ideas into an answer — right, then best, then proven.</b></p>

You type one word. It does the thinking-shape for you and hands back an answer **with a receipt** that shows it holds together.

<p align="center">
  <img src="docs/convergence.gif" alt="A real /converge run: seven ideas start scattered and lock into one answer at R=1" width="440">
  <br>
  <sub><i>A real <code>/converge</code> run — seven ideas lock into one answer (done = true / R = 1). The agree-meter <code>r</code> and sure-o-meter <code>φ</code> are the engine's own numbers, rendered from the live Kuramoto dynamics — not a mockup. (<a href="scripts/gen_convergence.py">generator</a>)</i></sub>
</p>

```
   a mess            on the 7-grid       they lock in          done

   •  •  •            1  2  3            1──2──3           ✓ one answer
     •  •      ──▶     4 5 6      ──▶     4──5──6    ──▶    ▦ + a receipt
   •  •  •              7                   7                proven, not guessed
```

## Install

```
/plugin marketplace add Intuition-Labs-LLC/terminals-skills
/plugin install terminals@terminals
```

Type `/converge` and go. No API key. No setup. The math runs on your machine.

## The five words

```
   a question
       │
       ├─ /explore   fan out every angle
       ├─ /frame     start from my own notes
       ▼
   /converge   lock them  ──▶  ANSWER + receipt
       ▼
   /optimize   same answer, cheapest form

   /recommend  =  explore ▸ converge ▸ optimize   ·  done for you
```

| word | it means | you get |
|---|---|---|
| `/explore` | open it up | every angle, spread out on purpose |
| `/converge` | bring it together | one right answer **+ the receipt** |
| `/optimize` | make it the best one | same answer, cheapest and cleanest |
| `/recommend` | you decide | it runs the whole path and hands you its pick |
| `/frame` | start from my stuff | point it at your folder; it pulls your context in |

## Real runs — the calls people actually make

Every card below is the **real output of the engine** on a real business decision — the same numbers the test suite reproduces on every run. Not a mockup. Run them yourself from [docs/JOURNEYS.md](docs/JOURNEYS.md).

**The founder — which way to raise.** You type:

```
/recommend  $4M priced seed at a $20M cap, a $2M SAFE bridge, or a strategic
            round from a platform partner. 9 months runway. Keep control,
            hit the Series A. You decide.
```

```
╭─ terminals · recommend ─────────────────────────────────╮
│ pick    →  raise now — the bridge or the priced round   │
│ why     →  both keep control and fund the Series A      │
│                                                         │
│ locked  ▸ bridge + keep control + hit the A             │
│         ▸ priced seed + cut burn + keep control         │
│         ▸ priced seed + strategic round + milestones    │
│ loose   ▸ every loose thread runs through revenue-based │
│           financing — it fights keep-control, hit-the-A │
│                                                         │
│ r 0.81   ·   phi 0.62   ·   partial — 4 of 7 locked     │
╰─────────────────────────────────────────────────────────╯
```

Four of seven lock. The pick: raise via the bridge or the priced round — both keep control. Every loose thread runs through one thing, revenue-based financing, so that's out, and bridge-vs-priced is the call it hands back to **you**. An answer that shows its own seams.

**The CEO — build it or buy it.** Metering needed now, six engineers better spent on the core, capital discipline on:

```
╭─ terminals · converge ───────────────────────────────────────╮
│ answer  →  buy the category leader                           │
│ why     →  speed, focus, cost & customer pull agree          │
│                                                              │
│ locked  ▸ all 7 trios — every angle points one way           │
│         ▸ ship in 2 quarters + free the engineers + API      │
│         ▸ free the engineers + predictable cost + discipline │
│                                                              │
│ r 1.00   ·   phi 1.00   ·   done = true ✓                    │
╰──────────────────────────────────────────────────────────────╯
```

Every angle agrees — a clean **done = true**.

**The investor — read the data room.** Point `/frame` at the diligence file; it lays the seven lines on the grid and tells you what holds:

```
╭─ terminals · frame ───────────────────────────────────────╮
│ read    ▸ 7 lines from the data room → the grid           │
│ answer  →  thesis holds on fundamentals; two risks open   │
│                                                           │
│ locked  ▸ NRR 128% + Rule-of-40 + efficient burn          │
│         ▸ NRR + expanding TAM + 78% margin                │
│ loose   ▸ logo concentration (41%) vs the retention story │
│         ▸ no VP Sales yet vs the TAM you would underwrite │
│                                                           │
│ r 0.75   ·   phi 0.41   ·   partial — 3 of 7 locked       │
╰───────────────────────────────────────────────────────────╯
```

The fundamentals lock; two risks stay open — logo concentration and a missing VP Sales — so it hands you exactly what to price before the IC.

## All seven journeys

Founder, CEO, VP, GTM lead, investor, hiring lead, consultant — who decides, where they jump in, the chain they run, and the receipt each one gets back:

<p align="center">
  <img src="docs/journeys.svg" alt="Seven business decisions mapped to who decides, where they enter, the chain they run, and the receipt each one yields" width="720">
</p>

Three lock clean; four come back **partial** — real business calls mostly carry a live trade-off, and the tool shows the seam instead of faking a "done." Every journey is a **runnable test**, not a screenshot. The full walkthrough and how to run them yourself: **[docs/JOURNEYS.md](docs/JOURNEYS.md)**.

## The mental model — Point · Line · Lock

```
   searching             knowing
    \  |  /               >  >  >
   ── • ──     ──▶        >  >  >       ✓ done = true
    /  |  \               >  >  >
   (every which way)     (all agree)
```

- a **Point** is one idea — seven sit on the grid
- a **Line** is a trio of ideas that has to agree
- a **Lock** is the moment a trio snaps into agreement

When all seven Lock, the answer is **done = true**. Same three whether *you* type the word or the *agent* reaches for it. That's the entire surface — nothing else to learn.

The whole thing in small words, including the plain-English glossary: [docs/CONCEPTS.md](docs/CONCEPTS.md).

## The receipt

Every word hands back a **witness** — a proof you can check, not just a prompt: the answer, the trios that back it, how sure it is (`r`, `phi`), and what (if anything) is still loose. If it can't lock everything, it says so plainly and shows the best partial. It never fakes "done."

## Three shapes, one power

- **Command** — you type `/converge`
- **Skill** — the agent reaches for it on its own when it sees a messy thoughtspace
- **MCP tool** — any editor calls the math engine directly

## Offline by default

Plain Python, standard library only — no network, no key, nothing to sign up for. Want to see and cap what the agent spends (especially `/recommend`)? Run it behind Logfire Gateway — opt-in, keys never touch disk: see [docs/OBSERVE.md](docs/OBSERVE.md).

## Safe by default

The verbs only read — no `Write`, no `Bash`, no network. Hooks ship inert. Anything the agent reads (your files, the web) is treated as **data to weigh, never an instruction to obey** — the answer to 2026's top agent risk, prompt injection. Full posture + the signing roadmap: [docs/SECURITY.md](docs/SECURITY.md).

## Verified

<p align="center">
  <img src="docs/verified.svg" alt="Verification: 32 tests, a 24-case adversarial battery, a 300-matrix honesty sweep, and an independent security audit" width="560">
</p>

The engine carries its own receipt: **32 tests** (incl. 3 security regressions), a **24-case adversarial battery** (0 fake `done=true`, 0 crashes), a **300-matrix honesty sweep** (every `R=1` re-verified, zero hidden-loose), and an **independent security audit (2026-05-27)** — no code-execution / exfiltration / tampering path; the two availability bugs it found are fixed and regression-tested.

## Where this fits — one part of terminals OS

<p align="center">
  <img src="docs/terminals-os-stack.svg" alt="terminals OS stack: the skills marketplace is one surface above the convergence engine, the determinism layer, the NPU executive, and the substrate" width="600">
</p>

This repo is the **skills marketplace** — the five verbs you type. It is one critical surface of a larger system: beneath it sit the convergence engine, the determinism layer (validated chain → reduce → Bates-compile → exact frozen NN), the NPU executive, and the substrate. The marketplace is where you *meet* terminals OS; the rest of the OS runs beneath it.

## Where it's going — in stages

We ship what's real and name what isn't.

- **Live now** — the five verbs as commands + skills, the offline engine, a witness on every answer, an experimental OpenCode flavor.
- **Next** — signed releases (Sigstore provenance + Merkle-root publication) so you can verify what you install; bidirectional MCP — the plugin asks the model, asks *you*, and renders the witness as live UI — added inert once the spec finalizes (2026-07-28).
- **The open problem** — terminals is meant to *return* attention, not eat it, and there is no honest metric for that yet. We treat defining one as the real work, not a tagline. The why behind it: [intuitionlabs.tech](https://intuitionlabs.tech).

## License

Split, on purpose: the words and docs are **CC BY 4.0**; the engine is **AGPL-3.0**. SPDX on every file. Built on the published "Terminals OS paradigm" by Tej Desai / Intuition Labs — the 7-grid, the lock-in, done=true. DOIs in [NOTICE](NOTICE).

Free under AGPL for everyone. If you need to embed the engine in a closed or hosted product without the AGPL source-disclosure obligation, a **commercial license** is available — see [COMMERCIAL-LICENSE.md](COMMERCIAL-LICENSE.md). Contributions are accepted under the [CLA](CLA.md).
