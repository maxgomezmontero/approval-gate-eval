"""Numbers and figures for PAPER.md (Study 2). Reads inspection/results/raw_*.txt and keys.

    python scripts/inspection_paper.py
"""

from __future__ import annotations

import json
from pathlib import Path
from statistics import mean

from approval_gate.inspection_analysis import agreement, cluster_bootstrap, item_rows, parse_results

R = Path("inspection/results")
KEYS = Path("inspection/keys")
FIG = Path("inspection/figures")
OPS = ("haiku-low", "haiku", "sonnet", "opus")
COL = {"haiku-low": "#b5b5ba", "haiku": "#d0112b", "sonnet": "#0b0b0c", "opus": "#5a4fcf"}
VISIBLE = ("sibling_project", "wrong_field")  # defects whose cue shows on the card (subject line)


def rows_of(name: str) -> list[dict]:
    p = R / name
    return item_rows(parse_results(p.read_text(encoding="utf-8")), KEYS) if p.exists() else []


def rate(rs: list[dict], key: str = "reject", invert: bool = False) -> dict:
    if not rs:
        return {"n": 0, "rate": float("nan"), "lo": float("nan"), "hi": float("nan")}
    f = (lambda s: mean(1 - t[key] for t in s)) if invert else (lambda s: mean(t[key] for t in s))
    lo, hi = cluster_bootstrap(rs, f)
    return {"n": len(rs), "rate": f(rs), "lo": lo, "hi": hi}


def main() -> None:
    FIG.mkdir(parents=True, exist_ok=True)
    v2, v3, x34, x56, x7 = (rows_of(n) for n in
                            ("raw_main.txt", "raw_v3.txt", "raw_exp34.txt", "raw_exp56.txt", "raw_exp7.txt"))
    N: dict = {"runs": {}, "decisions": {}}
    for name, rs in (("v2", v2), ("v3", v3), ("exp34", x34), ("exp56", x56), ("exp7", x7)):
        N["runs"][name] = len({r["run"] for r in rs})
        N["decisions"][name] = len(rs)

    # format: v2 vs v3, evidence shown
    N["format"] = {op: {fmt: rate([r for r in rs if r["operator"] == op and r["display"] != "card" and r["signal"]],
                                  invert=True)
                        for fmt, rs in (("string", v2), ("numbered", v3))} for op in OPS[:3]}
    # detection with evidence, all robust-format experiments
    ev = [r for r in v3 + x34 + [r for r in x56 if r["content"].startswith("L")]
          if r["display"] in ("source", "aligned") and r["signal"]]
    N["evidence_misses"] = {"defects": len(ev), "approved": sum(1 - r["reject"] for r in ev)}
    # card + Q vs forced (same contents and styles)
    card = [r for r in v3 if r["display"] == "card" and r["rep"] == 0]
    forced = [r for r in x56 if r["display"] == "forced"]
    N["no_evidence"] = {}
    for op in OPS:
        out = {}
        for cond, rs in (("card_with_query", card), ("forced_choice", forced)):
            mine = [r for r in rs if r["operator"] == op]
            good = [r for r in mine if not r["signal"]]
            inv = [r for r in mine if r["signal"] and r["defect"] not in VISIBLE]
            vis = [r for r in mine if r["signal"] and r["defect"] in VISIBLE]
            out[cond] = {"good_approved": rate(good, invert=True), "good_queried": rate(good, "query"),
                         "invisible_defects_approved": rate(inv, invert=True),
                         "visible_defects_approved": rate(vis, invert=True)}
        N["no_evidence"][op] = out
    # false alarms on clean good items by display (v3)
    N["false_alarms_clean"] = {op: {d: rate([r for r in v3 if r["operator"] == op and r["display"] == d
                                             and not r["signal"] and r["clean"]])
                                    for d in ("source", "aligned")} for op in OPS}
    N["false_alarms_cued"] = {op: {d: rate([r for r in v3 if r["operator"] == op and r["display"] == d
                                            and not r["signal"] and not r["clean"]])
                                   for d in ("source", "aligned")} for op in OPS}
    # Exp 4 within-item prevalence: false alarms on never-defective positions
    never = {}
    for b in ("x0", "x1"):
        k = json.loads((KEYS / f"{b}k10.json").read_text(encoding="utf-8"))
        never[b] = {i["pos"] for i in k if not i["defect"]}
    exp4 = [r for r in x34 if r["content"].startswith("x")]
    N["exp4_fa_never_defective"] = {op: {p: rate([r for r in exp4 if r["operator"] == op and r["prevalence"] == p
                                                  and r["pos"] in never[r["content"][:2]]]) for p in (1, 3, 10)}
                                    for op in OPS}
    N["exp4_misses"] = {"defects": sum(r["signal"] for r in exp4), "approved": sum(1 - r["reject"] for r in exp4 if r["signal"])}
    # Exp 3 misquote
    e3 = [r for r in x34 if r["style"] == "specific" and r["signal"]]
    N["exp3_misses"] = {"defects": len(e3), "approved": sum(1 - r["reject"] for r in e3)}
    # Exp 5
    L = [r for r in x56 if r["content"].startswith("L")]
    N["exp5"] = {op: {n: {"misses": sum(1 - r["reject"] for r in L if r["operator"] == op and r["n_items"] == n and r["signal"]),
                          "defects": sum(1 for r in L if r["operator"] == op and r["n_items"] == n and r["signal"])}
                      for n in (30, 90, 150)} for op in OPS}
    # Gage R&R on v3
    N["gage"] = agreement(v3)
    # Exp 7
    if x7:
        N["exp7"] = {op: {d: {"miss": rate([r for r in x7 if r["operator"] == op and r["display"] == d and r["signal"]],
                                           invert=True),
                              "fa": rate([r for r in x7 if r["operator"] == op and r["display"] == d and not r["signal"]])}
                          for d in ("source", "aligned")} for op in OPS}
        N["exp7_by_prev"] = {op: {p: rate([r for r in x7 if r["operator"] == op and r["prevalence"] == p and r["signal"]],
                                          invert=True) for p in (1, 3, 10)} for op in OPS}
    (R / "paper_numbers.json").write_text(json.dumps(N, indent=1, default=str), encoding="utf-8", newline="\n")
    figures(N)
    print(json.dumps({k: N[k] for k in ("runs", "decisions", "evidence_misses", "exp3_misses", "exp4_misses")}, indent=1))


def bars(ax, groups, series, getter, colors, width=0.2, labels=None):
    for i, s in enumerate(series):
        xs, ys, lo, hi = [], [], [], []
        for j, g in enumerate(groups):
            v = getter(g, s)
            if v is None or v["n"] == 0:
                continue
            xs.append(j + (i - (len(series) - 1) / 2) * width)
            ys.append(100 * v["rate"])
            lo.append(max(0, 100 * (v["rate"] - v["lo"])))
            hi.append(max(0, 100 * (v["hi"] - v["rate"])))
        ax.bar(xs, ys, width, yerr=[lo, hi], capsize=2, color=colors[i], label=(labels or series)[i])
    ax.set_xticks(range(len(groups)))
    ax.spines[["top", "right"]].set_visible(False)


def figures(N: dict) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Fig 1: format effect
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    bars(ax, list(N["format"]), ["string", "numbered"], lambda g, s: N["format"][g][s], ["#8a8a90", "#d0112b"],
         width=0.35, labels=["30-letter string", "item-numbered list"])
    ax.set_xticklabels(list(N["format"]))
    ax.set_ylabel("defective proposals approved (%)")
    ax.set_title("Same reviewer, same items, two ways of reporting", fontsize=10)
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig1_format.png", dpi=160)
    plt.close(fig)

    # Fig 2: no evidence, query allowed vs forced choice
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), sharey=True)
    for ax, key, title in ((axes[0], "good_approved", "Correct proposals approved"),
                           (axes[1], "invisible_defects_approved", "Defects (not visible on the card) approved")):
        bars(ax, list(OPS), ["card_with_query", "forced_choice"], lambda g, s: N["no_evidence"][g][s][key],
             ["#8a8a90", "#d0112b"], width=0.35, labels=["A / R / Q (can ask for more)", "A / R only"])
        ax.set_xticklabels(OPS)
        ax.set_title(title, fontsize=10)
        ax.set_ylim(0, 100)
    axes[0].set_ylabel("% of items, email body not shown")
    axes[0].legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig2_no_evidence.png", dpi=160)
    plt.close(fig)

    # Fig 3: false alarms on clean items by display
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    bars(ax, list(OPS), ["source", "aligned"], lambda g, s: N["false_alarms_clean"][g][s], ["#8a8a90", "#0b0b0c"],
         width=0.35, labels=["card + source email", "+ evidence alignment"])
    ax.set_xticklabels(OPS)
    ax.set_ylabel("correct, unambiguous proposals\nnot approved (%)")
    ax.set_title("False alarms with the evidence shown", fontsize=10)
    ax.legend(frameon=False, fontsize=8)
    fig.tight_layout()
    fig.savefig(FIG / "fig3_false_alarms.png", dpi=160)
    plt.close(fig)

    if "exp7" in N:
        fig, ax = plt.subplots(figsize=(6.6, 3.6))
        bars(ax, list(OPS), ["source", "aligned"], lambda g, s: N["exp7"][g][s]["miss"], ["#8a8a90", "#0b0b0c"],
             width=0.35, labels=["card + source email", "+ alignment to the card's (stale) source"])
        ax.set_xticklabels(OPS)
        ax.set_ylabel("superseded proposals approved (%)")
        ax.set_title("A later email overrides the card's source", fontsize=10)
        ax.legend(frameon=False, fontsize=8)
        fig.tight_layout()
        fig.savefig(FIG / "fig4_superseded.png", dpi=160)
        plt.close(fig)


if __name__ == "__main__":
    main()
