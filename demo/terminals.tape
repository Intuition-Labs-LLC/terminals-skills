# SPDX-License-Identifier: CC-BY-4.0
# terminals — engine cold open: the convergence math, offline and tested.
# Run from the repo root:  vhs demo/terminals.tape   ->   demo/engine.gif

Output demo/engine.gif

Set FontFamily "Geist Mono"
Set FontSize 22
Set Width 1100
Set Height 640
Set Padding 36
Set Margin 28
Set MarginFill "#0f0f12"
Set BorderRadius 12
Set TypingSpeed 40ms
Set Theme { "background":"#0f0f12","foreground":"#e7e3da","cursor":"#9ecfd0","selection":"#1f3a3b","black":"#1a1b1e","red":"#ef4444","green":"#22c55e","yellow":"#f59e0b","blue":"#9ecfd0","magenta":"#c9a3d4","cyan":"#9ecfd0","white":"#e7e3da","brightBlack":"#6b7177","brightGreen":"#4ade80","brightYellow":"#fbbf24","brightWhite":"#f9f6ee" }

Sleep 600ms
Type "# the convergence engine — pure python, no key, no network"
Sleep 300ms
Enter
Type "cd mcp && python3 -m pytest -q"
Sleep 300ms
Enter
Sleep 3s
Type "# 7-grid + lock-in + R=1 + the witness, all offline, all proven"
Sleep 300ms
Enter
Sleep 2s
