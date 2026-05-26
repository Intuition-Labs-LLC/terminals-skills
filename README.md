<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Terminals

**Five small words that turn a messy pile of ideas into an answer — right, then best, then proven.**

You type one word. It does the thinking-shape for you and hands back an answer *with a receipt* that shows the answer holds together. Works in Claude Code, OpenCode, and any tool that speaks MCP.

## Install (two lines)

```
/plugin marketplace add wheattoast11/terminals
/plugin install terminals@terminals
```

That's it. Now type `/converge` and go. No API key. No setup. The math runs on your machine.

## The five words

| type this | it means | what you get |
|---|---|---|
| `/explore` | "open it up" | every angle on your question, spread out on purpose |
| `/converge` | "bring it together" | one right answer **+ the receipt** that proves it fits |
| `/optimize` | "make it the best one" | the same answer, but the cheapest, cleanest version |
| `/recommend` | "you decide" | it explores, converges, and optimizes for you, then hands you its pick **+ the receipt** |
| `/frame` | "start from my stuff" | point it at the folder you're already in; it pulls your context in and goes |

The normal path is `explore → converge → optimize`. `/recommend` runs that whole path for you. `/frame` is the on-ramp when you already have your own notes.

## The mental model

**Point · Line · Lock is the whole thing.**

- A **Point** is one idea. Seven of them sit on the grid.
- A **Line** is a trio of ideas that has to agree.
- A **Lock** is the moment a Line clicks into agreement. When all seven Lock, the answer is done = true — and you get the receipt.

Every word is just a move over those three:

| word | the move |
|---|---|
| `/explore` | scatter the Points wide |
| `/frame` | turn your own stuff into Points |
| `/converge` | run the Locks → answer + receipt |
| `/optimize` | find the cheapest way to Lock |
| `/recommend` | place the Points, Lock them, and pick — for you |

Same three primitives whether a human types the word or an agent reaches for it on its own. That is the entire surface. Nothing else to learn.

## How it works (the short version)

1. It lays your ideas on a **7-grid** — 7 ideas, 7 trios, every pair of ideas sharing exactly one trio. No idea gets lost, nothing is counted twice.
2. It nudges the ideas in each trio toward agreement — the **lock-in**.
3. When every trio locks in, the answer is **done = true**: it's not just an opinion, it provably hangs together.
4. You get back the answer **and the receipt** — which trios locked, how sure it is, and what (if anything) didn't fit.

If it *can't* lock everything in, it says so plainly and shows you the best partial plus what's still loose. It never fakes "done."

## The receipt

Every word returns a **witness** — a small record of `what it claims · what backs it · the verdict · why`. That's the difference: most tools give you a prompt; this gives you a proof you can check.

## Offline by default

The convergence math is plain Python, standard library only. No network, no key, nothing to sign up for. (You can wire in heavy outside research later if you want — it's off by default.)

## Three shapes, one power

Each word ships three ways so it fits how you work:

- **Command** — you type `/converge`.
- **Skill** — the agent reaches for it on its own when it sees a messy thoughtspace.
- **MCP tool** — any editor can call the math engine directly.

## License

Split, on purpose:

- The words, skills, and docs are **CC BY 4.0** — use them, learn from them, share them.
- The engine is **AGPL-3.0** — improvements to the engine stay open.

See `LICENSE` (engine) and `LICENSE.docs` (words). Built on published work — see `NOTICE` for the papers and the math credits.

## Credit

The convergence method is the published "Terminals OS paradigm" by Tej Desai / Intuition Labs (the 7-grid, the lock-in, done=true). DOIs are listed in `NOTICE`.
