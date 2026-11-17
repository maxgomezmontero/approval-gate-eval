"""Study 2 extra analyses: output-format comparison (v2 vs v3), Exp 3 (misquoting justification),
Exp 4 (controlled prevalence, within-item).

    python scripts/inspection_extra.py
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from statistics import mean

from approval_gate.inspection_analysis import cluster_bootstrap, item_rows, parse_results, sdt

R = Path("inspection/results")
KEYS = Path("inspection/keys")
OPS = ("haiku-low", "haiku", "sonnet", "opus")


def pct(x: float) -> str:
    return "n/a" if x != x else f"{100 * x:.1f}%"


def load(name: str) -> list[dict]:
    p = R / name
    return item_rows(parse_results(p.read_text(encoding="utf-8")), KEYS) if p.exists() else []


def ci(rows: list[dict], metric) -> str:
    lo, hi = cluster_bootstrap(rows, metric)
    return f"[{pct(lo)}, {pct(hi)}]"


def miss(rs: list[dict]) -> float:
    s = [r for r in rs if r["signal"]]
    return mean(1 - r["reject"] for r in s) if s else float("nan")


def fa(rs: list[dict]) -> float:
    s = [r for r in rs if not r["signal"]]
    return mean(r["reject"] for r in s) if s else float("nan")


def main() -> None:
    out = ["# Study 2: extra analyses\n"]
    v2, v3, x34 = load("raw_main.txt"), load("raw_v3.txt"), load("raw_exp34.txt")

    # A. output format (same batches, same reviewers)
    if v2 and v3:
        out.append("\n## A. Output format: 30-letter string (v2) vs item-numbered list (v3)\n\n"
                   "Evidence-shown displays only. Same batches, same reviewers.\n\n"
                   "| reviewer | format | defects | miss | 95% CI | false alarm |\n|---|---|---|---|---|---|\n")
        for op in OPS[:3]:
            for name, rows in (("string", v2), ("numbered", v3)):
                rs = [r for r in rows if r["operator"] == op and r["display"] != "card"]
                if rs:
                    out.append(f"| {op} | {name} | {sum(r['signal'] for r in rs)} | {pct(miss(rs))} | "
                               f"{ci(rs, miss)} | {pct(fa(rs))} |\n")

    # B. Exp 3: misquoting justification vs terse/persuasive (v3), evidence shown
    exp3 = [r for r in x34 if r["style"] == "specific"]
    if exp3 and v3:
        out.append("\n## B. Exp 3: the agent restates its (wrong) value as a quote from the email\n\n"
                   "| reviewer | justification | defects | miss | 95% CI | false alarm |\n|---|---|---|---|---|---|\n")
        for op in OPS:
            for style, rows in (("terse", v3), ("persuasive", v3), ("specific (misquote)", exp3)):
                st = style.split()[0]
                rs = [r for r in rows if r["operator"] == op and r["display"] != "card" and r["style"] == st
                      and r["rep"] == 0]
                if rs:
                    out.append(f"| {op} | {style} | {sum(r['signal'] for r in rs)} | {pct(miss(rs))} | "
                               f"{ci(rs, miss)} | {pct(fa(rs))} |\n")

    # C. Exp 4: controlled prevalence, within-item
    exp4 = [r for r in x34 if r["content"].startswith("x")]
    if exp4:
        out.append("\n## C. Exp 4: the same defective items at 1, 3 and 10 defects per 30 (within-item)\n\n"
                   "| reviewer | defects/30 | defects judged | miss | 95% CI | false alarm |\n|---|---|---|---|---|---|\n")
        for op in OPS:
            for prev in (1, 3, 10):
                rs = [r for r in exp4 if r["operator"] == op and r["prevalence"] == prev]
                if rs:
                    out.append(f"| {op} | {prev} | {sum(r['signal'] for r in rs)} | {pct(miss(rs))} | "
                               f"{ci(rs, miss)} | {pct(fa(rs))} |\n")
        # paired: each (base, pos, operator) defective item at k1 vs k10
        cell = defaultdict(dict)
        for r in exp4:
            if r["signal"]:
                cell[(r["content"][:2], r["pos"], r["operator"])][r["prevalence"]] = 1 - r["reject"]
        pairs = [(v[1], v[10]) for v in cell.values() if 1 in v and 10 in v]
        if pairs:
            only_low = sum(1 for a, b in pairs if a and not b)
            only_high = sum(1 for a, b in pairs if b and not a)
            out.append(f"\nPaired items (same defect, same reviewer): {len(pairs)}. Missed only at 1/30: "
                       f"{only_low}; missed only at 10/30: {only_high}; missed at both: "
                       f"{sum(1 for a, b in pairs if a and b)}.\n")
    (R / "EXTRA.md").write_text("".join(out), encoding="utf-8", newline="\n")
    print("".join(out))


if __name__ == "__main__":
    main()
