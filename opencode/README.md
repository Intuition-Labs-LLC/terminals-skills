<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright (c) 2026 Tej Desai / Intuition Labs LLC -->

# Terminals in OpenCode (experimental)

The engine is standard MCP, so it works in OpenCode the same way it works anywhere. The slash commands are a best-effort port and are marked **experimental**, because OpenCode's command spec is still moving.

## 1. Wire the engine (the part that just works)

Add the Terminals MCP server to your OpenCode config (`opencode.json`, project or global). See `opencode.json` here for the shape:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "terminals": {
      "type": "local",
      "command": ["python3", "/ABSOLUTE/PATH/TO/terminals/mcp/server.py"],
      "enabled": true
    }
  }
}
```

Set the path to where you cloned this repo. No API key, no extra installs: the server is pure Python standard library. Now any OpenCode agent can call the `converge`, `explore`, `optimize`, `recommend`, `frame`, and `hold` tools.

## 2. The slash commands (experimental)

Copy `opencode/command/*.md` into your OpenCode commands directory (project `.opencode/command/` or global `~/.config/opencode/command/`). Then `/converge`, `/explore`, `/optimize`, `/recommend`, `/frame`, `/act`, and `/hold` are available. They carry the same protocol as the Claude Code versions. The first six call the `terminals` MCP tools; `/act` orchestrates the tools your OpenCode host already has and asks before anything that writes.

If a command flavor lags an OpenCode change, the MCP path in step 1 still gives you the full engine. Call the tools directly.
