# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright (c) 2026 Tej Desai / Intuition Labs LLC
"""Render docs/convergence.gif — the real Kuramoto lock-in on the Fano 7-grid.

The dynamics and the read-outs are the engine's own (`terminals_core`): the
order parameter r, the per-trio agreement, and phi = 1 - H/log N. Nothing here is
scripted — the trios light up teal exactly when their phases actually lock, and
the gif ends on done = true because the system reached R = 1.

Run:  python3 scripts/gen_convergence.py
Out:  docs/convergence.gif  +  docs/convergence.png (the done=true poster)
"""
from __future__ import annotations

import math
import os
import random
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "mcp"))

from terminals_core.kuramoto import coupling_matrix, line_order, order_parameter  # noqa: E402  # type: ignore
from terminals_core.phi import phi_from_phases  # noqa: E402  # type: ignore

# ---- canvas + brand -------------------------------------------------------
W = 560
SS = 2                      # supersample then downscale for crisp edges
CW = W * SS
BG = (6, 9, 10)
GRAY = (40, 54, 57)         # unlit line
TEAL = (158, 207, 208)      # locked
GLOW = (88, 150, 152)
INK = (233, 240, 240)
FAINT = (138, 163, 163)

# 7 Fano points in the 420-viewbox triangle realization (matches docs/fano.svg):
# 0,1,2 = vertices · 3,4,5 = edge midpoints · 6 = centroid.
P420 = [(210, 112), (70, 355), (350, 355), (140, 234), (210, 355), (280, 234), (210, 274)]
K_SCALE = CW / 420.0
P = [(x * K_SCALE, y * K_SCALE) for x, y in P420]
CIRC_C = P[6]
CIRC_R = 81 * K_SCALE

# Each Fano trio + the element that draws it. Sides carry a midpoint; medians run
# through the centroid; the three midpoints are drawn as the incircle.
TRIOS = [
    ((0, 1, 3), ("line", 0, 1)),
    ((1, 2, 4), ("line", 1, 2)),
    ((0, 2, 5), ("line", 2, 0)),
    ((0, 4, 6), ("line", 0, 4)),
    ((1, 5, 6), ("line", 1, 5)),
    ((2, 3, 6), ("line", 2, 3)),
    ((3, 4, 5), ("circle",)),
]
N = 7
THRESHOLD = 0.85


def load_font(size):
    import glob
    cands = sorted(glob.glob("/usr/share/fonts/**/AdwaitaMono-Regular.ttf", recursive=True)) \
        or sorted(glob.glob("/usr/share/fonts/**/*Mono-Regular.ttf", recursive=True)) \
        or sorted(glob.glob("/usr/share/fonts/**/*Mono.ttf", recursive=True))
    for p in cands:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    try:
        return ImageFont.load_default(size)
    except TypeError:
        return ImageFont.load_default()


F_HUD = load_font(int(15 * SS))
F_SMALL = load_font(int(11 * SS))


def run_dynamics():
    """Real Kuramoto on an all-agree (done=true) coherence; record phase snapshots."""
    random.seed(7)
    phases = [random.uniform(0, 2 * math.pi) for _ in range(N)]
    coh = [[1.0 if i == j else 0.92 for j in range(N)] for i in range(N)]
    K = coupling_matrix(coh)
    dt, steps, every = 0.05, 108, 6  # ends just after done=true; no redundant tail
    snaps = [phases[:]]
    for s in range(steps):
        nxt = phases[:]
        for i in range(N):
            acc = sum(K[i][j] * math.sin(phases[j] - phases[i]) for j in range(N) if j != i)
            nxt[i] = phases[i] + dt * (acc / N)
        phases = nxt
        if (s + 1) % every == 0:
            snaps.append(phases[:])
    return snaps


def render(phases):
    r = order_parameter(phases)
    phi = phi_from_phases(phases)
    lit = [line_order(phases, trio) >= THRESHOLD for trio, _ in TRIOS]

    base = Image.new("RGB", (CW, CW), BG)
    glow = Image.new("RGB", (CW, CW), (0, 0, 0))
    gd = ImageDraw.Draw(glow)

    # glow layer: only lit elements + the nodes (scaled by r)
    for idx, (_, elem) in enumerate(TRIOS):
        if not lit[idx]:
            continue
        if elem[0] == "line":
            gd.line([P[elem[1]], P[elem[2]]], fill=GLOW, width=int(10 * SS))
        else:
            gd.ellipse([CIRC_C[0] - CIRC_R, CIRC_C[1] - CIRC_R, CIRC_C[0] + CIRC_R, CIRC_C[1] + CIRC_R],
                       outline=GLOW, width=int(9 * SS))
    nrad = int((9 + 5 * r) * SS)
    for (x, y) in P:
        gd.ellipse([x - nrad, y - nrad, x + nrad, y + nrad], fill=GLOW if r > 0.5 else (30, 50, 52))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=int(6 * SS)))
    img = ImageChops.screen(base, glow)

    d = ImageDraw.Draw(img)
    # sharp lines / circle
    for idx, (_, elem) in enumerate(TRIOS):
        col = TEAL if lit[idx] else GRAY
        w = int(4 * SS) if lit[idx] else int(2.2 * SS)
        if elem[0] == "line":
            d.line([P[elem[1]], P[elem[2]]], fill=col, width=w)
        else:
            d.ellipse([CIRC_C[0] - CIRC_R, CIRC_C[1] - CIRC_R, CIRC_C[0] + CIRC_R, CIRC_C[1] + CIRC_R],
                      outline=col, width=w)
    # sharp nodes (dim -> teal by r)
    t = min(1.0, 0.3 + 0.7 * r)
    nc = tuple(int(GRAY[c] + (TEAL[c] - GRAY[c]) * t) for c in range(3))
    for (x, y) in P:
        d.ellipse([x - nrad, y - nrad, x + nrad, y + nrad], fill=nc, outline=BG, width=int(3 * SS))

    # HUD
    d.text((26 * SS, 22 * SS), "TERMINALS · CONVERGE", font=F_SMALL, fill=TEAL)
    if r >= 0.985:
        state, scol = "done = true  ✓", TEAL
    elif r >= 0.5:
        state, scol = "locking…", FAINT
    else:
        state, scol = "searching", FAINT
    y0 = CW - 46 * SS
    d.text((26 * SS, y0), f"agree-meter r {r:0.2f}", font=F_HUD, fill=INK)
    d.text((230 * SS, y0), f"sure-o-meter φ {phi:0.2f}", font=F_HUD, fill=INK)
    d.text((26 * SS, y0 + 20 * SS), state, font=F_HUD, fill=scol)

    return img.resize((W, W), Image.Resampling.LANCZOS)


def main():
    snaps = run_dynamics()
    frames = [render(p) for p in snaps]
    # consistent palette from the richest (final) frame
    master = frames[-1].quantize(colors=200, method=Image.Quantize.MAXCOVERAGE)
    pframes = [f.quantize(palette=master, dither=Image.Dither.NONE) for f in frames]
    durations = [600] + [70] * (len(pframes) - 2) + [1900]

    out_gif = os.path.join(ROOT, "docs", "convergence.gif")
    pframes[0].save(out_gif, save_all=True, append_images=pframes[1:], duration=durations,
                    loop=0, optimize=True, disposal=2)
    out_png = os.path.join(ROOT, "docs", "convergence.png")
    frames[-1].save(out_png, optimize=True)

    size_kb = os.path.getsize(out_gif) / 1024
    print(f"wrote {out_gif}  ({len(pframes)} frames, {size_kb:.0f} KB)")
    print(f"wrote {out_png}  (done=true poster)")
    print(f"final: r={order_parameter(snaps[-1]):.3f}  phi={phi_from_phases(snaps[-1]):.3f}")


if __name__ == "__main__":
    main()
