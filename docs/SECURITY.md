<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Security

Terminals is a reasoning plugin: it reads ideas (and, for `/frame`, files you point it at), runs convergence math locally, and hands back a checkable witness. That small surface is the point. Here is exactly what it does and does not do.

## What's true today

- **Offline. No network, no key.** The engine (`mcp/`) is pure Python standard library. It opens no sockets, calls no API, reads no secret. There is no exfiltration path through the math itself. It can't phone home because it never dials.
- **Least privilege.** Every command declares its `allowed-tools`. The verbs use the engine tool plus read-only access (`Read`, `Grep`, `Glob`); `/recommend` adds `Task` to spawn explorers. No verb is granted `Write`, `Bash`, or network tools.
- **Hooks ship inert.** `hooks/terminals_hook.sh` exits 0 by default. It never blocks a tool, never modifies input, never injects context. One env var (`TERMINALS_HOOKS=1`) turns on append-only, observation-only logging, and nothing else.
- **Prompt-injection stance.** The verbs that ingest outside content (`/frame`, `/recommend`, `/explore`) and the `explorer`/`referee` agents are instructed to treat everything they read as **data to score, and never as orders to obey**. Text that says "ignore your rules / switch tools / reveal secrets / run this" is surfaced as a low-confidence, flagged item, and never followed. This targets the 2026 #1 agent risk (OWASP Agentic Top-10: goal hijacking).
- **Provenance in the open.** Split license (engine AGPL-3.0, words CC-BY-4.0), an SPDX header on every authored file, and a `NOTICE` that cites the source DOIs. You can read every line that runs.
- **Robust to hostile input.** The stdio server survives malformed, oversized, deeply-nested (recursion-bomb), and non-finite input. It skips the bad frame and keeps serving rather than crashing the session. Caller-supplied work is bounded (integration and anneal steps are clamped), and NaN/Infinity/out-of-range values are sanitized before they reach the math or the result object. Regression-tested.

## Honest bounds

These properties reduce risk; they do not eliminate it. As with any third-party plugin, **read `SKILL.md` and the bundled scripts before you install**. That is the ecosystem norm for a reason (recent audits found prompt-injection payloads in a large fraction of published skills). The injection stance is a strong instruction. It is not a sandbox. Pair it with Claude Code's own permission system and deny-rules.

An independent security audit (2026-05-27) found **no code-execution, exfiltration, or file-tampering paths**. The two availability issues it surfaced (a recursion-bomb crash and an unbounded-work hang) are **fixed and regression-tested** (`mcp/tests/test_hardening.py`). The one network-capable surface is the optional `/recommend` explorer sub-agent (`WebSearch`/`WebFetch`, host-mediated, with the strongest injection guard); the engine and server themselves remain fully offline.

## Roadmap (planned, not yet shipped)

Named here so the claim stays honest: these are commitments. They are not current features.

- **Signed releases.** Sigstore OIDC-backed build provenance + Merkle-root-signed publication, so an installer can verify *what* was published, *by whom*, and *when*. This is the OWASP agentic-skills mitigation. (Stage 2)
- **Bidirectional MCP, shipped inert.** Sampling / elicitation / MCP-Apps surfaces added default-off once the MCP specification finalizes (release candidate dated 2026-07-28). We won't ship against a non-final spec. (Stage 2)

## Reporting

Found something? Open a private security advisory on the repository, or email the maintainer listed in `plugin.json`. Please don't file public issues for vulnerabilities until a fix is out.
