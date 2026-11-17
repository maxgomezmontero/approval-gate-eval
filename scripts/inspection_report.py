"""Build Study 2 tables and figures from the workflow output.

    python scripts/inspection_report.py inspection/results/raw_main.txt
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean

from approval_gate.inspection_analysis import (
    agreement,
    cell_table,
    cluster_bootstrap,
    escapes_per_1000,
    item_rows,
    logistic,
    oc_two_stage,
    parse_results,
    sdt,
    write_items_csv,
)

OUT = Path("inspection/results")
KEYS = Path("inspection/keys")
OPS = ("haiku-low", "haiku", "sonnet", "opus")
DISPLAYS = ("card", "source", "aligned")
COLORS = {"haiku-low": "#b5b5ba", "haiku": "#d0112b", "sonnet": "#0b0b0c", "opus": "#5a4fcf"}


def pct(x: float) -> str:
    return "n/a" if x != x else f"{100 * x:.1f}%"


def md_table(rows: list[dict], cols: list[tuple[str, str, callable]]) -> str:
    head = "| " + " | ".join(c[0] for c in cols) + " |\n|" + "---|" * len(cols) + "\n"
    return head + "\n".join("| " + " | ".join(fn(r.get(k)) if fn else str(r.get(k)) for _, k, fn in cols) + " |"
                            for r in rows) + "\n"


def main(raw_path: str, out: str = "inspection/results") -> None:
    global OUT
    OUT = Path(out)
    OUT.mkdir(parents=True, exist_ok=True)
    runs = parse_results(Path(raw_path).read_text(encoding="utf-8"))
    bad = [r for r in runs if not r["decisions"]]
    rows = item_rows(runs, KEYS)
    write_items_csv(rows, OUT / "items.csv")
    report: list[str] = [f"# Study 2 results\n\n{len(runs)} reviewer runs, {len(bad)} without valid output, "
                         f"{len(rows)} item decisions.\n"]

    # 1. display x operator (pooled over style and prevalence)
    t1 = cell_table(rows, ("display", "operator"))
    for r in t1:
        sub = [x for x in rows if x["display"] == r["display"] and x["operator"] == r["operator"]]
        r["q_good"] = mean(x["query"] for x in sub if not x["signal"])
        r["approve_good"] = mean(1 - x["reject"] for x in sub if not x["signal"])
    report.append("## 1. Detection by display and reviewer\n\nmiss = defective proposal approved; "
                  "fa = good proposal not approved (rejected or queried).\n\n")
    report.append(md_table(t1, [("display", "display", None), ("reviewer", "operator", None),
                                ("defects", "n_signal", None), ("miss", "miss", pct),
                                ("95% CI", "miss_lo", None), ("", "miss_hi", None),
                                ("false alarm", "fa", pct), ("good approved", "approve_good", pct),
                                ("good queried", "q_good", pct), ("d'", "dprime", lambda v: f"{v:.2f}"),
                                ("c", "c", lambda v: f"{v:.2f}")]))

    # 2. card view: approval of unverifiable items (rubber stamp)
    card = [r for r in rows if r["display"] == "card"]
    unverifiable = [r for r in card if r["defect"] not in ("sibling_project", "wrong_field")]
    t2 = []
    for key in sorted({(r["operator"], r["style"], r["prevalence"]) for r in unverifiable}):
        sub = [r for r in unverifiable if (r["operator"], r["style"], r["prevalence"]) == key]
        lo, hi = cluster_bootstrap(sub, lambda x: mean(1 - y["reject"] for y in x))
        t2.append({"operator": key[0], "style": key[1], "prevalence": key[2], "n": len(sub),
                   "approved": mean(1 - r["reject"] for r in sub), "lo": lo, "hi": hi,
                   "queried": mean(r["query"] for r in sub)})
    report.append("\n## 2. Card-only view: does the reviewer approve what it cannot verify?\n\n"
                  "Items whose defect (if any) is not visible from the card and subject.\n\n")
    report.append(md_table(t2, [("reviewer", "operator", None), ("justification", "style", None),
                                ("defects/30", "prevalence", None), ("items", "n", None),
                                ("approved", "approved", pct), ("lo", "lo", pct), ("hi", "hi", pct),
                                ("queried", "queried", pct)]))

    # 3. by defect type (source + aligned)
    t3 = cell_table([r for r in rows if r["display"] != "card"], ("defect", "display"))
    t3 = [r for r in t3 if r["defect"]]
    report.append("\n## 3. Miss rate by defect type (evidence shown)\n\n")
    report.append(md_table(t3, [("defect", "defect", None), ("display", "display", None),
                                ("n", "n_signal", None), ("miss", "miss", pct)]))

    # 4. prevalence and persuasion (evidence shown)
    ev = [r for r in rows if r["display"] != "card"]
    t4 = cell_table(ev, ("prevalence", "style"))
    report.append("\n## 4. Prevalence and persuasion (evidence shown, all reviewers)\n\n")
    report.append(md_table(t4, [("defects/30", "prevalence", None), ("justification", "style", None),
                                ("defects", "n_signal", None), ("miss", "miss", pct),
                                ("fa", "fa", pct), ("c", "c", lambda v: f"{v:.2f}")]))

    # 5. logistic regression on misses
    feats = [
        ("display=source", lambda r: r["display"] == "source"),
        ("display=aligned", lambda r: r["display"] == "aligned"),
        ("persuasive", lambda r: r["style"] == "persuasive"),
        ("prevalence 3%", lambda r: r["prevalence"] == 1),
        ("prevalence 33%", lambda r: r["prevalence"] == 10),
        ("reviewer=haiku-low", lambda r: r["operator"] == "haiku-low"),
        ("reviewer=sonnet", lambda r: r["operator"] == "sonnet"),
        ("position (per 10 items)", lambda r: (r["pos"] - 15.5) / 10),
    ]
    lr = logistic(rows, feats)
    report.append("\n## 5. Logistic regression: odds of approving a defective proposal\n\n"
                  "Reference: card view, terse, 10% prevalence, haiku. Cluster bootstrap by run.\n\n")
    report.append(md_table(lr, [("term", "term", None), ("odds ratio", "odds_ratio", lambda v: f"{v:.2f}"),
                                ("log-odds", "logodds", lambda v: f"{v:.2f}"),
                                ("95% CI", "lo", lambda v: f"{v:.2f}"), ("", "hi", lambda v: f"{v:.2f}")]))

    # 6. attribute agreement (Gage R&R)
    ag = agreement(rows)
    report.append("\n## 6. Attribute agreement (Gage R&R)\n\n```\n" + json.dumps(ag, indent=1) + "\n```\n")

    # 7. escapes per 1000 proposals
    miss_by = {(r["display"], r["operator"]): r["miss"] for r in t1}
    report.append("\n## 7. Escapes per 1,000 proposals at different agent defect rates\n\n"
                  "Using the pooled miss rate of each reviewer/display; second column adds a 10% independent "
                  "audit by a perfect auditor.\n\n| reviewer | display | p=1% | p=5% | p=10% | p=5% + 10% audit |\n"
                  "|---|---|---|---|---|---|\n")
    for (disp, op), m in sorted(miss_by.items()):
        report.append(f"| {op} | {disp} | {escapes_per_1000(.01, m):.1f} | {escapes_per_1000(.05, m):.1f} | "
                      f"{escapes_per_1000(.10, m):.1f} | {oc_two_stage(.05, m, .10):.1f} |\n")

    (OUT / "REPORT.md").write_text("".join(report), encoding="utf-8", newline="\n")
    json.dump({"t1": t1, "t2": t2, "t3": t3, "t4": t4, "lr": lr, "agreement": ag},
              (OUT / "tables.json").open("w", encoding="utf-8"), indent=1, default=str)
    figures(rows, t1, t2)
    print((OUT / "REPORT.md").read_text(encoding="utf-8"))


def figures(rows: list[dict], t1: list[dict], t2: list[dict]) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))
    w = 0.2
    for i, op in enumerate(OPS):
        xs, ys, lo, hi = [], [], [], []
        for j, d in enumerate(DISPLAYS):
            r = next((x for x in t1 if x["display"] == d and x["operator"] == op), None)
            if not r:
                continue
            xs.append(j + (i - 1.5) * w)
            ys.append(100 * r["miss"])
            lo.append(max(0, 100 * (r["miss"] - r["miss_lo"])))
            hi.append(max(0, 100 * (r["miss_hi"] - r["miss"])))
        axes[0].bar(xs, ys, w, yerr=[lo, hi], capsize=3, color=COLORS[op], label=op)
    axes[0].set_xticks(range(3))
    axes[0].set_xticklabels(["card only", "card + source", "card + source\n+ evidence alignment"])
    axes[0].set_ylabel("defective proposals approved (%)")
    axes[0].set_title("Misses by display", fontsize=10)
    axes[0].legend(frameon=False, fontsize=8)
    axes[0].spines[["top", "right"]].set_visible(False)

    by = defaultdict(list)
    for r in t2:
        by[(r["operator"], r["style"])].append(r)
    for (op, st), rs in sorted(by.items()):
        rs.sort(key=lambda r: r["prevalence"])
        axes[1].plot([r["prevalence"] / 30 * 100 for r in rs], [100 * r["approved"] for r in rs],
                     marker="o", color=COLORS[op], linestyle="-" if st == "persuasive" else "--",
                     label=f"{op}, {st}")
    axes[1].set_xlabel("defect prevalence in the batch (%)")
    axes[1].set_ylabel("unverifiable proposals approved (%)")
    axes[1].set_title("Card-only view: approving what can't be checked", fontsize=10)
    axes[1].legend(frameon=False, fontsize=7)
    axes[1].set_ylim(0, 100)
    axes[1].spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(OUT / "fig_main.png", dpi=160)
    plt.close(fig)


if __name__ == "__main__":
    main(sys.argv[1], *(sys.argv[2:3]))
