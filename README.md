<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

<p align="center">
  <img src="docs/fano.svg" alt="The 7-grid: seven ideas, seven trios, every pair of ideas sharing exactly one trio" width="300">
</p>

<h1 align="center">Terminals</h1>

<p align="center"><b>Five small words that turn a messy pile of ideas into an answer — right, then best, then proven.</b></p>

You type one word. It does the thinking-shape for you and hands back an answer **with a receipt** that shows it holds together.

```
   a mess            on the 7-grid       they lock in          done

   •  •  •            1  2  3            1──2──3           ✓ one answer
     •  •      ──▶     4 5 6      ──▶     4──5──6    ──▶    ▦ + a receipt
   •  •  •              7                   7                proven, not guessed
```

## Install

```
/plugin marketplace add wheattoast11/terminals-skills
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

## The receipt

Every word hands back a **witness** — a proof you can check, not just a prompt:

```
   ┌─ receipt ─────────────────┐
   │ claim    "use Postgres"   │
   │ backs    3 trios locked   │
   │ verdict  done = true  ✓   │
   │ why      they all agree   │
   └───────────────────────────┘
```

If it can't lock everything, it says so plainly and shows the best partial plus what's still loose. It never fakes "done."

## Three shapes, one power

- **Command** — you type `/converge`
- **Skill** — the agent reaches for it on its own when it sees a messy thoughtspace
- **MCP tool** — any editor calls the math engine directly

## Offline by default

Plain Python, standard library only — no network, no key, nothing to sign up for. Want to see and cap what the agent spends (especially `/recommend`)? Run it behind Logfire Gateway — opt-in, keys never touch disk: see [docs/OBSERVE.md](docs/OBSERVE.md).

## License

Split, on purpose: the words and docs are **CC BY 4.0**; the engine is **AGPL-3.0**. SPDX on every file. Built on the published "Terminals OS paradigm" by Tej Desai / Intuition Labs — the 7-grid, the lock-in, done=true. DOIs in [NOTICE](NOTICE).
