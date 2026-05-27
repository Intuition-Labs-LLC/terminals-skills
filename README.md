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

## A real run

You type:

```
/recommend Two offers. A: $185k senior IC at a 2,000-person public co — strong team,
30-min commute, stable. B: $150k + 0.4% equity at a 25-person seed startup — mission I
care about, fully remote, higher risk. I'm 31, want to grow into leadership. You decide.
```

It opens the question into seven angles, judges how they fit, locks the ones that agree, and hands back the call **with the receipt**. These are the engine's real numbers:

```
╭─ terminals · recommend ─────────────────────────────────╮
│ pick    →  take the startup (offer B)                   │
│ why     →  growth, mission & remote pull one way        │
│                                                         │
│ locked  ▸ growth + mission + remote                     │
│         ▸ growth + optionality + team                   │
│         ▸ leadership + remote + team                    │
│         ▸ mission + leadership + optionality            │
│ loose   ▸ every loose trio is the same thing —          │
│           “is the equity worth it?”  ·  your call       │
│                                                         │
│ r 0.71   ·   phi 0.83   ·   partial — 4 of 7 locked     │
╰─────────────────────────────────────────────────────────╯
```

Four of seven trios lock — the case for B holds. The three that *don't* are all one thing: whether the equity is actually worth it. The math won't pretend to know that, so it hands that part back to you. **That's the difference — an answer that shows its own seams.**

## More real runs

**`/converge` — when it all actually fits.** Ask whether an argument holds; if every claim backs the next, you get **done = true** — not a maybe:

```
╭─ terminals · converge ──────────────────────────────────╮
│ answer  →  the case for a 4-day week holds              │
│                                                         │
│ locked  ▸ all 7 trios — every claim backs the next      │
│           e.g. focus + cost-neutral + fewer meetings    │
│                                                         │
│ r 1.00   ·   phi 1.00   ·   done = true ✓               │
╰─────────────────────────────────────────────────────────╯
```

**`/frame` — start from your own folder.** Point it at a pile of notes; it reads them, lays them on the grid, and tells you what coheres and what's still open:

```
╭─ terminals · frame ─────────────────────────────────────╮
│ read    ▸ 7 notes from your folder → the 7-grid         │
│ answer  →  not settled yet — leans remote, not done     │
│                                                         │
│ locked  ▸ flexibility + lease savings + hiring          │
│         ▸ productivity + flexibility + async            │
│ open    ▸ two threads still pull against it:            │
│           onboarding  ·  roles needing in-person        │
│                                                         │
│ r 0.43   ·   phi 0.76   ·   partial — 2 of 7 locked     │
╰─────────────────────────────────────────────────────────╯
```

That's the honest read: your folder *isn't* decided yet. Two threads cohere, two still pull against them — so it hands you the map instead of a fake verdict.

Same five words, three shapes of answer — a confident pick with one caveat, a clean *done*, and an honest *not yet* — each carrying its receipt.

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

## Where it's going — in stages

We ship what's real and name what isn't.

- **Live now** — the five verbs as commands + skills, the offline engine, a witness on every answer, an experimental OpenCode flavor.
- **Next** — signed releases (Sigstore provenance + Merkle-root publication) so you can verify what you install; bidirectional MCP — the plugin asks the model, asks *you*, and renders the witness as live UI — added inert once the spec finalizes (2026-07-28).
- **The open problem** — terminals is meant to *return* attention, not eat it, and there is no honest metric for that yet. We treat defining one as the real work, not a tagline. The why behind it: [intuitionlabs.tech](https://intuitionlabs.tech).

## License

Split, on purpose: the words and docs are **CC BY 4.0**; the engine is **AGPL-3.0**. SPDX on every file. Built on the published "Terminals OS paradigm" by Tej Desai / Intuition Labs — the 7-grid, the lock-in, done=true. DOIs in [NOTICE](NOTICE).
