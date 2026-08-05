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


def main():
    OUT.mkdir(parents=True, exist_ok=True); SRC.mkdir(parents=True, exist_ok=True)
    path = OUT / "fig_parent_selection_fork.pdf"
    selection_fork(path)
    shutil.copy2(path, SRC / path.name)
    print("WROTE", path)


if __name__ == "__main__":
    main()

