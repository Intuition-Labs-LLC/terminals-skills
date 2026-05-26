<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Recording the demo

Goal: a 60–90s clip that shows **the full runtime in action** and proves the same five words work on *anything* — not just code. Branded slightly (Terminals dark × Intuition Labs teal), elegant, never loud.

## The look (one theme, used everywhere)

Terminals' dark canvas + Intuition Labs' signature teal + Geist Mono.

| role | hex | used for |
|---|---|---|
| background | `#0f0f12` | the canvas |
| foreground | `#e7e3da` | normal text (IL paper, on dark) |
| accent (teal) | `#9ecfd0` | prompts · the Lock · R=1 |
| success | `#22c55e` | `done = true ✓` |
| amber | `#f59e0b` | partial · the loose trio |
| dim | `#6b7177` | comments · dividers |

Font: **Geist Mono** (`brew install --cask font-geist-mono`, or Google Fonts). Fallback `ui-monospace`.

## Tools

- **asciinema + agg** — the *live* agentic run (you can't script an LLM; record real, theme at render).
- **VHS** (`charmbracelet/vhs`) — the *deterministic* clips (engine, install). See `terminals.tape`.
- **freeze** (`charmbracelet/freeze`) — a still PNG of the final witness card for the thumbnail/social.

## Setup (once)

```bash
# you have access; the repo is private
/plugin marketplace add wheattoast11/terminals-skills
/plugin install terminals@terminals
```

Make the runtime *visible* — a second pane that shows the lifecycle chain firing:
```bash
export TERMINALS_HOOKS=1            # observational lifecycle log, on for the demo
tail -f ~/.terminals/lifecycle.log  # pane 2
```
You'll see: `SessionStart → UserPromptSubmit → PreToolUse (×7 Task + mcp) → PostToolUse → Stop`.

## Beat 1 — cold open (deterministic, ~8s) · "the math is real, offline"

```bash
vhs demo/terminals.tape    # renders demo/engine.gif — pure-stdlib tests, no network, no key
```

## Beat 2 — the flagship (live, ~50s) · a job offer, decided with a receipt

Record with asciinema:
```bash
asciinema rec recommend.cast
```
Then, in Claude Code, one prompt:
```
/recommend Two offers. A: $185k senior IC at a 2,000-person public co — strong team,
30-min commute, stable. B: $150k + 0.4% equity at a 25-person seed startup — mission I
care about, fully remote, higher risk. I'm 31, ~10 months runway saved, want to grow into
leadership. You decide — go deep.
```
It spawns 7 explorers in parallel, the referee judges coherence, the engine locks + trims, and it ends on the witness card — leaning B, honest that *the equity's worth is the one thing only you can settle.*

Render themed:
```bash
agg --font-family "Geist Mono" --font-size 22 --line-height 1.4 \
  --theme '0f0f12,e7e3da,1a1b1e,ef4444,22c55e,f59e0b,9ecfd0,c9a3d4,9ecfd0,e7e3da,6b7177,f87171,4ade80,fbbf24,bfe3e4,d8bfe4,bfe3e4,f9f6ee' \
  recommend.cast recommend.gif
```

## Beat 3 — the range (fast cuts, ~20s) · "same five words, any life"

Record each as a 3–4s cut; c2 of them are enough to land it.
```
/converge   my 14 to-dos this week — which 3 actually matter?
/frame      read my /research folder and give me the thesis (+ what's still contested)
/recommend  three apartments [trade-offs pasted] — pick one for me
/converge   does the argument in my talk actually hold together?
/optimize   this 8-step launch plan — cheapest version that still works
```

## Cards (title + end)

`titlecard.svg` — the 7-grid mark + `terminals · intuition labs` + *"the answer, and the proof it holds."* Use as the open and the close (export to PNG with `freeze` or any SVG→PNG).

## Notes

- The agentic run is **non-deterministic** — do one dry take, then record. "go deep" nudges the 7-explorer society on for the camera.
- Keep pane 2 (the lifecycle log) narrow on the right — it reads as "the full runtime," not clutter.
- After recording, `unset TERMINALS_HOOKS` to return the hook to inert.
