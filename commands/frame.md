---
description: Start from my stuff. Pull the context I already have — this folder, my notes — into the system and get going.
argument-hint: [path or "here"] — where your context lives
allowed-tools: mcp__terminals__frame, mcp__terminals__converge, Read, Grep, Glob
---
<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# /frame

Start from my stuff. The user already did the legwork — there's a folder, a doc, a pile of notes. Pull it in, translate it into the system, and pick up from there.

Where it lives: **$ARGUMENTS**
(If empty or "here", use the current working directory and what's already in this conversation.)

This is the on-ramp. It turns the user's own words into the structure the other verbs need — the same translation, every time.

Run this protocol.

1. **Read their stuff.** Gather the context: read the path/files named, or scan the working folder (READMEs, docs, plans, notes). Skim, don't drown — you want the distinct claims and options, not every line.
2. **Pull out the items.** List the distinct ideas / options / claims you found. Aim for the 7 that carry the most weight. If there are more, cluster; if fewer, that's fine.
3. **Translate.** Call the `frame` tool with `{ items }` (add a coherence matrix if you can judge how the items fit). It maps each item onto the 7-grid and tells you how it read them, then converges.
4. **Show the reading first.** One short block: "Here's how I read your stuff" — each item → its place. This lets the user catch a misread before anything is decided.
5. **Then the answer + receipt.** Hand back the converged result like `/converge` does: the answer in plain words, then the witness. If it came back partial, say what's loose and the next step.

Read first, translate openly, then converge. The user should recognize their own problem in your reading.
