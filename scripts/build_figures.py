#!/usr/bin/env python3
from pathlib import Path
import shutil

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
SRC = ROOT / "paperIV_submission_source" / "figures"


def box(ax, x, y, w, h, text, color):
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h, boxstyle="round,pad=0.015,rounding_size=0.015",
        linewidth=1.2, edgecolor="#263238", facecolor=color
    ))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=8.3)


def arrow(ax, a, b, label=""):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12,
                                 linewidth=1.2, color="#263238"))
    if label:
        ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + .035,
                label, ha="center", fontsize=7.4)


def selection_fork(path):
    fig, ax = plt.subplots(figsize=(8.4, 3.8))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    box(ax, .03, .40, .20, .22, "current separate\nsource reduct", "#eaf2ff")
    box(ax, .36, .66, .24, .19, "joint potential\nnonzero mixed Hessian", "#dff3e4")
    box(ax, .36, .16, .24, .19, "split potential\nzero mixed Hessian", "#f7dfdf")
    box(ax, .72, .66, .24, .19, "minimal selected law\nif certificate semantics", "#eef6d8")
    box(ax, .72, .16, .24, .19, "exact control\nunder current laws", "#fde5d6")
    arrow(ax, (.23, .54), (.36, .75), "same pure-axis data")
    arrow(ax, (.23, .46), (.36, .25), "same pure-axis data")
    arrow(ax, (.60, .75), (.72, .75), "complete mediation")
    arrow(ax, (.60, .25), (.72, .25), "no joint role")
    ax.text(.5, .96, "Physical parent-selection fork", ha="center",
            va="top", fontsize=12, fontweight="bold")
    ax.text(.5, .04,
            "Seed occupation fixes support in both branches; it does not choose the mixed Hessian.",
            ha="center", fontsize=8.2)
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close(fig)


def signature_spine(path):
    fig, ax = plt.subplots(figsize=(9.0, 4.2))
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    nodes = [
        (.03,.66,"S0\nbase + seed + body","#eaf4ea",.16),
        (.27,.66,"S1\nonce-counted ledger","#eaf2ff",.16),
        (.51,.66,"S2\njoint incidence","#f3efff",.16),
        (.75,.66,"S3\nstandard-limit class","#fff1e1",.16),
        (.15,.27,"S4\nstate/effect packet","#eef6d8",.16),
        (.39,.27,"S5\nrecord occupation","#dff3e4",.16),
        (.63,.27,"S6\nfinite metric law","#fde5d6",.16),
        (.83,.27,"S7\naction unit","#f7dfdf",.14),
    ]
    for x, y, text_, color, width in nodes:
        box(ax, x, y, width, .17, text_, color)
    for a, b in [((.19,.745),(.27,.745)),((.43,.745),(.51,.745)),
                 ((.67,.745),(.75,.745)),((.59,.66),(.23,.44)),
                 ((.59,.66),(.47,.44)),((.55,.355),(.63,.355)),
                 ((.79,.355),(.83,.355))]:
        arrow(ax, a, b)
    ax.text(.5,.95,"Deduplicated physical-selection signature",ha="center",fontsize=12,fontweight="bold")
    ax.text(.5,.08,"Hold, detector error and timing endpoints are validation data, not parent-selection blocks.",ha="center",fontsize=8.1)
    fig.tight_layout(); fig.savefig(path,bbox_inches="tight"); plt.close(fig)


def main():
    OUT.mkdir(parents=True, exist_ok=True); SRC.mkdir(parents=True, exist_ok=True)
    paths = [OUT / "fig_parent_selection_fork.pdf", OUT / "fig_signature_spine.pdf"]
    selection_fork(paths[0]); signature_spine(paths[1])
    for path in paths:
        shutil.copy2(path, SRC / path.name)
    print("WROTE", *paths)


if __name__ == "__main__":
    main()
