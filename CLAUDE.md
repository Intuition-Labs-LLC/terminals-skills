<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# CLAUDE.md — terminals-skills

A Claude Code plugin: the terminals verbs that turn a messy idea-pile into a
coherent answer with a checkable receipt. Public: github.com/Intuition-Labs-LLC/terminals-skills.

## Layout
- `commands/<verb>.md` — slash command (frontmatter: description / argument-hint /
  allowed-tools, then SPDX, then a small-words protocol + a box-drawing receipt card).
- `skills/<verb>/SKILL.md` — the same verb as an auto-reach skill; deep refs in
  `skills/converge/reference/`.
- `agents/{explorer,referee}.md`, `hooks/`, `mcp/`, `.claude-plugin/{plugin,marketplace}.json`.
- `docs/` — CONCEPTS (glossary) · WORKBENCH (tools→trinkets) · FINDINGS (what a run
  emits) · SECURITY · JOURNEYS.

## Adding a verb
New `commands/<verb>.md` + `skills/<verb>/SKILL.md`, matching `commands/converge.md`
exactly (frontmatter, protocol, the card footer `r … · phi … · done = true ✓`).
Auto-discovered; no manifest edit. New verbs orchestrate the base verbs — no new MCP tool.

## House rules (load-bearing)
- Voice: plain, small words, one idea per sentence; no "not X but Y"; no fixed counts
  in copy (the 7-grid invariant is exempt).
- Names straight: sematon = trinket, gluon, the gate, the lens. No "earn it" caveats.
- Honesty is the product: never fake `done = true`; say `partial` out loud; a witness
  rides every answer and proves coherence, not world-truth.
- Two doors: README is "For humans" (operator's voice) + "For AI". Metaphysics stays
  in deep docs as labeled analogy, never a literal physics claim.

## Search with ix (optional floor)
`ix "<query>" <path> --json` → R-scored hits (ast-grep·grep·meaning agree); high-R
solid, low-R weak; feed R into the coherence judgment. Offline
(`pip install git+https://github.com/Intuition-Labs-LLC/ix-search`); fall back to
Grep/Glob so the plugin stays no-dep.

## Ship flow
Commit, then push to a branch (not master) for operator PR + squash review. `gh` is
authed (wheattoast11, https). Engine = AGPL-3.0, docs/words = CC-BY-4.0, SPDX on every
file. Git identity: Tej Desai <29216465+wheattoast11@users.noreply.github.com>.
