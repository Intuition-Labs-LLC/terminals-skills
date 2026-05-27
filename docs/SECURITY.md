<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Security

Terminals is a reasoning plugin: it reads ideas (and, for `/frame`, files you point it at), runs convergence math locally, and hands back a checkable witness. That small surface is the point — here is exactly what it does and does not do.

## What's true today

- **Offline. No network, no key.** The engine (`mcp/`) is pure Python standard library. It opens no sockets, calls no API, reads no secret. There is no exfiltration path through the math itself — it can't phone home because it never dials.
- **Least privilege.** Every command declares its `allowed-tools`. The verbs use the engine tool plus read-only access (`Read`, `Grep`, `Glob`); `/recommend` adds `Task` to spawn explorers. No verb is granted `Write`, `Bash`, or network tools.
- **Hooks ship inert.** `hooks/terminals_hook.sh` exits 0 by default. It never blocks a tool, never modifies input, never injects context. One env var (`TERMINALS_HOOKS=1`) turns on append-only, observation-only logging — and nothing else.
- **Prompt-injection stance.** The verbs that ingest outside content (`/frame`, `/recommend`, `/explore`) and the `explorer`/`referee` agents are instructed to treat everything they read as **data to score, not orders to obey**. Text that says "ignore your rules / switch tools / reveal secrets / run this" is surfaced as a low-confidence, flagged item — never followed. This targets the 2026 #1 agent risk (OWASP Agentic Top-10: goal hijacking).
- **Provenance in the open.** Split license (engine AGPL-3.0, words CC-BY-4.0), an SPDX header on every authored file, and a `NOTICE` that cites the source DOIs. You can read every line that runs.

## Honest bounds

These properties reduce risk; they do not eliminate it. As with any third-party plugin, **read `SKILL.md` and the bundled scripts before you install** — that is the ecosystem norm for a reason (recent audits found prompt-injection payloads in a large fraction of published skills). The injection stance is a strong instruction, not a sandbox; pair it with Claude Code's own permission system and deny-rules.

## Roadmap (planned — not yet shipped)

Named here so the claim stays honest: these are commitments, not current features.

- **Signed releases.** Sigstore OIDC-backed build provenance + Merkle-root-signed publication, so an installer can verify *what* was published, *by whom*, and *when* — the OWASP agentic-skills mitigation. (Stage 2)
- **Bidirectional MCP, shipped inert.** Sampling / elicitation / MCP-Apps surfaces added default-off once the MCP specification finalizes (release candidate dated 2026-07-28). We won't ship against a non-final spec. (Stage 2)

## Reporting

Found something? Open a private security advisory on the repository, or email the maintainer listed in `plugin.json`. Please don't file public issues for vulnerabilities until a fix is out.
