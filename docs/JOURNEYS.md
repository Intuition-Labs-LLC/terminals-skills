<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# What people use terminals for

Try this. Each row is a real call someone has to make. Type the prompt, watch for the thing in the middle column, and read what the model hands back.

| You type | What to look for | What comes back |
|---|---|---|
| `/recommend` your two term sheets and a bridge, 9 months of cash, you want to keep control | Does it pick a path and say what it refuses to touch? | Raise with the bridge or the priced round. Both keep you in control. It sets revenue-based financing aside because it fights the rest. Bridge versus priced is the call left to you. |
| `/explore` then `/converge` on build the billing system, buy it, or partner | Do all the reasons point one way, or do they fight? | Buy the category leader. Speed, focus, cost, and what customers need all agree. Settled. |
| `/frame` your org notes then `/converge` on cut 15 percent of cost | Will it admit a real trade-off, or force a clean answer? | Only the cut itself holds. Protecting your best people, keeping speed, and morale all pull against the number. You can hit 15 percent or you can hold the team. That trade-off is the decision. |
| `/explore` then `/converge` on price by seats or by usage | Does it land on one model and say which ones it dropped? | Lean to the hybrid, a platform fee plus usage. It keeps revenue predictable and comp simple. It drops pure usage and plain seats. |
| `/frame` the data room on a deal | Does it split what holds from what is risky? | The fundamentals hold. Two things stay open: the customer concentration and the missing head of sales. Price those before you say yes. |
| `/recommend` on a VP Eng hire who is 15 percent over band | Will it commit when the case is strong? | Extend the offer. Track record, culture, the gap she fills, and timing all line up. Settled. |
| `/recommend` to turn a pile of discovery notes into one client plan | One clean plan, or a pile of options? | Wedge into mid-market, partner-led, priced for adoption, with a 12-month proof gate before scaling. One plan. Settled. |

Settled means every reason agreed. When it does not all agree, it gives you the lean plus the one question still left to you, and it never says settled unless it is.

Every answer here is a real run. The cases live in [`mcp/tests/journeys.json`](../mcp/tests/journeys.json), and you can run them yourself with `pytest mcp/tests/test_journeys.py`.
