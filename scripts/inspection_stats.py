"""Referee-driven statistics for Study 2.

- unit of analysis: unique defective items and queue contents, not judgments
- content-clustered (queue) bootstrap, paired where the design is paired
- exact (Clopper-Pearson) intervals and item-level bounds for zero-event cells
- SDT (d', c) only where sensitivity is finite (no-evidence views), treating A > Q > R as a rating scale
- attribute agreement per display on the 3-category response
- a real acceptance-sampling plan (lot = queue of 30, n, c=0, rectifying), OC curve and AOQL

    python scripts/inspection_stats.py
"""

from __future__ import annotations

import json
import math
import random
from collections import defaultdict
from pathlib import Path
from statistics import NormalDist, mean

from approval_gate.inspection_analysis import item_rows, parse_results

R = Path("inspection/results")
KEYS = Path("inspection/keys")
OPS = ("haiku-low", "haiku", "sonnet", "opus")
VISIBLE = ("sibling_project", "wrong_field")
Z = NormalDist().inv_cdf


# ------------------------------------------------------------------ intervals

def _binom_cdf(k: int, n: int, p: float) -> float:
    if p <= 0:
        return 1.0
    if p >= 1:
        return 0.0 if k < n else 1.0
    return sum(math.exp(math.lgamma(n + 1) - math.lgamma(i + 1) - math.lgamma(n - i + 1)
                        + i * math.log(p) + (n - i) * math.log1p(-p)) for i in range(k + 1))


def clopper_pearson(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))

    def solve(f, target):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid) > target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    def solve_increasing(g, target):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if g(mid) < target:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    lower = 0.0 if k == 0 else solve_increasing(lambda p: 1 - _binom_cdf(k - 1, n, p), alpha / 2)
    upper = 1.0 if k == n else solve(lambda p: _binom_cdf(k, n, p), alpha / 2)
    return lower, upper


def boot(rows: list[dict], stat, key: str = "content", reps: int = 2000, seed: int = 1) -> tuple[float, float]:
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        groups[r[key]].append(r)
    names = sorted(groups)
    rng = random.Random(seed)
    vals = []
    for _ in range(reps):
        sample = [x for g in rng.choices(names, k=len(names)) for x in groups[g]]
        try:
            v = stat(sample)
        except (ZeroDivisionError, ValueError, KeyError):
            continue
        if v == v:
            vals.append(v)
    vals.sort()
    if not vals:
        return (float("nan"), float("nan"))
    return vals[int(0.025 * len(vals))], vals[min(len(vals) - 1, int(0.975 * len(vals)))]


def approve_rate(rs: list[dict]) -> float:
    return mean(1 - r["reject"] for r in rs)


def fmt(p: float, lo: float, hi: float) -> str:
    return f"{100 * p:.1f}% [{100 * lo:.1f}, {100 * hi:.1f}]"


def load(name: str) -> list[dict]:
    p = R / name
    return item_rows(parse_results(p.read_text(encoding="utf-8")), KEYS) if p.exists() else []


def uid(r: dict) -> str:
    """Unique defective item across experiments: (base content, position) after removing render variants."""
    c = r["content"]
    if c.startswith("x"):
        c = c[:2]  # Exp 4 versions share the base items
    return f"{c}:{r['pos']}"


# ------------------------------------------------------------------ main

def main() -> None:
    out: list[str] = ["# Study 2: statistics after referee review\n"]
    J: dict = {}
    v2, v3, x34, x56, x7, rep = (load(n) for n in ("raw_main.txt", "raw_v3.txt", "raw_exp34.txt", "raw_exp56.txt",
                                                   "raw_exp7.txt", "raw_replication.txt"))
    rev = load("raw_revision.txt")

    # 1. zero-miss claim at the right unit
    ev = [r for r in v3 + x34 + [r for r in x56 if r["content"].startswith("L")]
          if r["display"] in ("source", "aligned") and r["signal"]]
    k = sum(1 - r["reject"] for r in ev)
    uniq = {uid(r) for r in ev}
    by_type = defaultdict(set)
    for r in ev:
        by_type[r["defect"]].add(uid(r))
    lo_j, hi_j = clopper_pearson(k, len(ev))
    lo_i, hi_i = clopper_pearson(0, len(uniq))
    out.append("\n## 1. Misses with the evidence shown, at the right unit\n\n"
               f"{k} approved out of {len(ev)} defect judgments on **{len(uniq)} unique defective items**. "
               f"Exact 95% upper bound: {100 * hi_j:.2f}% if judgments were independent; "
               f"{100 * hi_i:.1f}% treating each unique item as one observation (perfect within-item correlation). "
               "Per reviewer (each saw every unique item at least once): "
               f"upper bound {100 * clopper_pearson(0, len(uniq))[1]:.1f}% at the item level.\n\n"
               "| defect type | unique items | judgments | approved | item-level 95% upper bound |\n|---|---|---|---|---|\n")
    for d, s in sorted(by_type.items()):
        n_j = sum(1 for r in ev if r["defect"] == d)
        out.append(f"| {d} | {len(s)} | {n_j} | 0 | {100 * clopper_pearson(0, len(s))[1]:.0f}% |\n")
    J["evidence"] = {"judgments": len(ev), "approved": k, "unique_items": len(uniq), "ub_judgment": hi_j, "ub_item": hi_i}

    # 2. no-evidence views: decision set x reviewer, content-clustered, paired
    def no_ev(card_rows, forced_rows, label):
        lines = [f"\n### {label}\n\n| reviewer | correct approved, A/R/Q | correct approved, A/R | paired difference | "
                 "hidden defects approved, A/R/Q | hidden defects approved, A/R | contents |\n|---|---|---|---|---|---|---|\n"]
        res = {}
        for op in OPS:
            c = [r for r in card_rows if r["operator"] == op]
            f = [r for r in forced_rows if r["operator"] == op]
            if not c or not f:
                continue
            cg, fg = [r for r in c if not r["signal"]], [r for r in f if not r["signal"]]
            ch = [r for r in c if r["signal"] and r["defect"] not in VISIBLE]
            fh = [r for r in f if r["signal"] and r["defect"] not in VISIBLE]
            both = cg + fg

            def diff(s):
                a = [r for r in s if r["display"] == "forced" and not r["signal"]]
                b = [r for r in s if r["display"] == "card" and not r["signal"]]
                return approve_rate(a) - approve_rate(b)

            d_lo, d_hi = boot(both, diff)
            res[op] = {"card": approve_rate(cg), "forced": approve_rate(fg), "diff": approve_rate(fg) - approve_rate(cg),
                       "diff_ci": (d_lo, d_hi), "card_hidden": approve_rate(ch) if ch else float("nan"),
                       "forced_hidden": approve_rate(fh) if fh else float("nan")}
            lines.append(f"| {op} | {fmt(approve_rate(cg), *boot(cg, approve_rate))} | {fmt(approve_rate(fg), *boot(fg, approve_rate))} | "
                         f"{100 * res[op]['diff']:+.1f} pts [{100 * d_lo:+.1f}, {100 * d_hi:+.1f}] | "
                         f"{fmt(approve_rate(ch), *boot(ch, approve_rate))} | {fmt(approve_rate(fh), *boot(fh, approve_rate))} | "
                         f"{len({r['content'] for r in c})} |\n")
        return "".join(lines), res

    card = [r for r in v3 if r["display"] == "card" and r["rep"] == 0]
    forced = [r for r in x56 if r["display"] == "forced"]
    t_orig, res_orig = no_ev(card, forced, "Original queues (11 contents, 2 justification styles)")
    rc = [r for r in rep if r["display"] == "card"]
    rf = [r for r in rep if r["display"] == "forced"]
    t_rep, res_rep = no_ev(rc, rf, "Replication (6 fresh contents at 10% prevalence, terse, 2 runs each)")
    out.append("\n## 2. No evidence attached: decision set x reviewer (content-clustered 95% CIs)\n" + t_orig + t_rep)
    # interaction: Sonnet's shift vs the mean shift of the others
    for name, res in (("original", res_orig), ("replication", res_rep)):
        if "sonnet" in res:
            others = mean(res[o]["diff"] for o in res if o != "sonnet")
            out.append(f"\nInteraction ({name}): removing Q raised approval of correct items by {100 * others:.0f} points on "
                       f"average for Haiku-low, Haiku and Opus, and by {100 * res['sonnet']['diff']:.0f} points for Sonnet, which "
                       f"already approved {100 * res['sonnet']['card']:.0f}% with Q available.\n")
    J["no_evidence"] = {"original": res_orig, "replication": res_rep}

    # 3. SDT where sensitivity is finite: card view (A > Q > R) and forced
    out.append("\n## 3. Signal detection in the no-evidence views (hidden defects vs correct items)\n\n"
               "Rating scale A > Q > R. Point 1: 'approve' vs not; point 2 (card only): 'approve or query' vs reject. "
               "d' and c with the log-linear correction; CIs by content bootstrap.\n\n"
               "| reviewer | view | d' (approve vs not) | c | d' (A or Q vs R) |\n|---|---|---|---|---|\n")

    def dprime(s, cut="approve"):
        sig = [r for r in s if r["signal"] and r["defect"] not in VISIBLE]
        noi = [r for r in s if not r["signal"]]
        if cut == "approve":
            h = (sum(r["reject"] for r in sig) + .5) / (len(sig) + 1)
            f = (sum(r["reject"] for r in noi) + .5) / (len(noi) + 1)
        else:
            h = (sum(r["hard_reject"] for r in sig) + .5) / (len(sig) + 1)
            f = (sum(r["hard_reject"] for r in noi) + .5) / (len(noi) + 1)
        return Z(h) - Z(f), -0.5 * (Z(h) + Z(f))

    J["sdt"] = {}
    for op in OPS:
        for view, rows in (("card A/R/Q", [r for r in card if r["operator"] == op]),
                           ("forced A/R", [r for r in forced if r["operator"] == op])):
            if not rows:
                continue
            d, c = dprime(rows)
            dlo, dhi = boot(rows, lambda s: dprime(s)[0])
            clo, chi = boot(rows, lambda s: dprime(s)[1])
            d2 = dprime(rows, "hard")[0] if view.startswith("card") else float("nan")
            J["sdt"][f"{op}|{view}"] = {"d": d, "c": c, "d_ci": (dlo, dhi), "c_ci": (clo, chi)}
            out.append(f"| {op} | {view} | {d:.2f} [{dlo:.2f}, {dhi:.2f}] | {c:.2f} [{clo:.2f}, {chi:.2f}] | "
                       f"{'' if d2 != d2 else f'{d2:.2f}'} |\n")

    # 4. persuasion where the criterion can move
    out.append("\n## 4. Persuasive justification where the criterion is free to move\n\n"
               "| reviewer | view | correct approved, terse | correct approved, persuasive |\n|---|---|---|---|\n")
    for op in OPS:
        for view, rows in (("card A/R/Q", card), ("forced A/R", forced)):
            t = [r for r in rows if r["operator"] == op and r["style"] == "terse" and not r["signal"]]
            p = [r for r in rows if r["operator"] == op and r["style"] == "persuasive" and not r["signal"]]
            if t and p:
                out.append(f"| {op} | {view} | {fmt(approve_rate(t), *boot(t, approve_rate))} | "
                           f"{fmt(approve_rate(p), *boot(p, approve_rate))} |\n")

    # 5. attribute agreement per display, 3 categories
    def kappa3(a, b):
        cats = "ARQ"
        n = len(a)
        po = sum(x == y for x, y in zip(a, b, strict=True)) / n
        pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
        return (po - pe) / (1 - pe) if pe < 1 else 1.0

    dec: dict[tuple, dict[int, str]] = defaultdict(dict)
    for r in v3:
        dec[(r["batch"], r["operator"], r["rep"])][r["pos"]] = r["decision"]
    out.append("\n## 5. Attribute agreement (AIAG-style), per display, 3-category A/R/Q, Cohen's kappa\n\n"
               "Repeatability: same reviewer, same queue, two runs (10% prevalence queues). Reproducibility: two "
               "reviewers, same queue, first run.\n\n| display | comparison | kappa | items |\n|---|---|---|---|\n")
    J["agreement"] = {}
    for disp in ("card", "source", "aligned"):
        for op in OPS:
            a, b = [], []
            for (bt, o, rp), d in dec.items():
                if o == op and rp == 0 and bt.endswith(disp) and (bt, o, 1) in dec:
                    for pos in sorted(d):
                        a.append(d[pos])
                        b.append(dec[(bt, o, 1)][pos])
            if a:
                kv = kappa3(a, b)
                J["agreement"][f"{disp}|repeat|{op}"] = kv
                out.append(f"| {disp} | repeatability {op} | {kv:.2f} | {len(a)} |\n")
        for i, o1 in enumerate(OPS):
            for o2 in OPS[i + 1:]:
                a, b = [], []
                for (bt, o, rp), d in dec.items():
                    if o == o1 and rp == 0 and bt.endswith(disp) and (bt, o2, 0) in dec:
                        for pos in sorted(d):
                            a.append(d[pos])
                            b.append(dec[(bt, o2, 0)][pos])
                if a:
                    kv = kappa3(a, b)
                    J["agreement"][f"{disp}|{o1}|{o2}"] = kv
                    out.append(f"| {disp} | {o1} vs {o2} | {kv:.2f} | {len(a)} |\n")

    # 6. Exp 4: prevalence and the criterion on never-defective items, clean vs cued
    never = {}
    for b in ("x0", "x1"):
        kk = json.loads((KEYS / f"{b}k10.json").read_text(encoding="utf-8"))
        never[b] = {i["pos"] for i in kk if not i["defect"]}
    e4 = [r for r in x34 if r["content"].startswith("x") and r["pos"] in never[r["content"][:2]]]
    out.append("\n## 6. Exp 4: false alarms on items that are never defective, by prevalence\n\n"
               "Same items in every version; only the other positions change. Two base queues, so CIs are by run.\n\n"
               "| reviewer | items | 1/30 | 3/30 | 10/30 |\n|---|---|---|---|---|\n")
    for op in OPS:
        for clean in (1, 0):
            cells = []
            for p in (1, 3, 10):
                s = [r for r in e4 if r["operator"] == op and r["prevalence"] == p and r["clean"] == clean]
                kk = sum(r["reject"] for r in s)
                lo, hi = clopper_pearson(kk, len(s))
                cells.append(f"{100 * kk / len(s):.1f}% ({kk}/{len(s)})" if s else "n/a")
            out.append(f"| {op} | {'clean' if clean else 'cued'} | " + " | ".join(cells) + " |\n")

    # 7. Exp 5: serial position
    L = [r for r in x56 if r["content"].startswith("L")]
    out.append("\n## 7. Exp 5: queue length and serial position (source shown)\n\n"
               "| reviewer | queue | misses | false alarms, first third | middle | last third |\n|---|---|---|---|---|---|\n")
    for op in OPS:
        for n in (30, 90, 150):
            s = [r for r in L if r["operator"] == op and r["n_items"] == n]
            if not s:
                continue
            miss = sum(1 - r["reject"] for r in s if r["signal"])
            nd = sum(r["signal"] for r in s)
            thirds = []
            for t in range(3):
                g = [r for r in s if not r["signal"] and t * n / 3 < r["pos"] <= (t + 1) * n / 3]
                thirds.append(f"{100 * mean(r['reject'] for r in g):.1f}%")
            out.append(f"| {op} | {n} | {miss}/{nd} | " + " | ".join(thirds) + " |\n")

    # 8. format: realignment analysis on v2 and the interleaved re-test
    out.append("\n## 8. Output format\n\n")
    keyc = {}
    for r in v2:
        keyc.setdefault((r["batch"], r["operator"], r["rep"]), {})[r["pos"]] = (r["signal"], r["decision"])
    shifted, normal = [], []
    for (bt, op, rp), d in keyc.items():
        if op != "sonnet" or bt.endswith("card"):
            continue
        sig = [d[p][0] for p in range(1, 31)]
        rej = [d[p][1] != "A" for p in range(1, 31)]
        best = max(range(-3, 4), key=lambda s_: sum(sig[i] == rej[i + s_] for i in range(30) if 0 <= i + s_ < 30))
        (shifted if best != 0 else normal).append((sig, rej))
    m_shift = sum(1 for sig, rej in shifted for i in range(30) if sig[i] and not rej[i])
    n_shift = sum(1 for sig, _ in shifted for i in range(30) if sig[i])
    m_norm = sum(1 for sig, rej in normal for i in range(30) if sig[i] and not rej[i])
    n_norm = sum(1 for sig, _ in normal for i in range(30) if sig[i])
    out.append(f"First pass (v2), Sonnet, evidence shown: runs whose string fits the key better after a shift: "
               f"{len(shifted)}/{len(shifted) + len(normal)}. Misses in those runs: {m_shift}/{n_shift}; "
               f"in the other runs: {m_norm}/{n_norm} ({100 * m_norm / max(1, n_norm):.1f}%). "
               "The shift diagnosis uses the key, so it is suggestive, not proof.\n\n")
    J["format_v2"] = {"shifted_runs": len(shifted), "runs": len(shifted) + len(normal), "miss_shifted": [m_shift, n_shift],
                      "miss_other": [m_norm, n_norm]}
    if rev:
        fm = [r for r in rev if r["operator"].endswith(("-str", "-num"))]
        out.append("Interleaved re-test (same session, same queues, randomized order), evidence shown:\n\n"
                   "| reviewer | format | defects judged | approved | exact 95% CI | false alarms |\n|---|---|---|---|---|---|\n")
        J["format_interleaved"] = {}
        for op in ("haiku", "sonnet"):
            for f in ("str", "num"):
                s = [r for r in fm if r["operator"] == f"{op}-{f}"]
                sg = [r for r in s if r["signal"]]
                kk = sum(1 - r["reject"] for r in sg)
                lo, hi = clopper_pearson(kk, len(sg))
                fa = mean(r["reject"] for r in s if not r["signal"]) if s else float("nan")
                J["format_interleaved"][f"{op}-{f}"] = {"approved": kk, "n": len(sg), "fa": fa,
                                                        "runs": len({r['run'] for r in s})}
                out.append(f"| {op} | {'30-letter string' if f == 'str' else 'item-numbered'} | {len(sg)} | {kk} | "
                           f"[{100 * lo:.1f}, {100 * hi:.1f}] | {100 * fa:.1f}% |\n")
        n_bad = sum(1 for line in (R / "raw_revision.txt").read_text().splitlines() if line.endswith(("BAD", "NULL")))
        out.append(f"\nInvalid outputs in the revision runs: {n_bad}.\n")

    # 9. Exp 7: clean vs cued false alarms; corrected instruction
    out.append("\n## 9. Exp 7: superseded evidence\n\n| reviewer | instruction | display | superseded approved | "
               "false alarms, clean | false alarms, cued |\n|---|---|---|---|---|---|\n")
    later = [r for r in rev if r["style"] == "later"]
    for op in OPS:
        for instr, rows, disps in (("source-only wording", x7, ("source", "aligned")), ("all-information wording", later, ("source",))):
            for d in disps:
                s = [r for r in rows if r["operator"] == op and r["display"] == d]
                if not s:
                    continue
                sg = [r for r in s if r["signal"]]
                kk = sum(1 - r["reject"] for r in sg)
                cl = [r for r in s if not r["signal"] and r["clean"]]
                cu = [r for r in s if not r["signal"] and not r["clean"]]
                out.append(f"| {op} | {instr} | {d} | {kk}/{len(sg)} | {100 * mean(r['reject'] for r in cl):.1f}% | "
                           f"{100 * mean(r['reject'] for r in cu):.1f}% |\n")

    # 10. realistic alignment
    ext = [r for r in rev if r["display"] == "extracted"]
    if ext:
        out.append("\n## 10. Evidence alignment from a regex extractor (no answer key) vs the oracle alignment\n\n"
                   "The regex extractor matched the oracle's job on 330/330 items and the oracle sentence on 325/330, "
                   "because the source emails are templated: on this stimulus set the oracle concern is small, on real "
                   "email it would not be.\n\n| reviewer | display | defects approved | false alarms, clean |\n|---|---|---|---|\n")
        for op in OPS:
            for d, rows in (("oracle aligned", [r for r in v3 if r["display"] == "aligned" and r["style"] == "terse" and r["rep"] == 0]),
                            ("regex extracted", ext)):
                s = [r for r in rows if r["operator"] == op]
                sg = [r for r in s if r["signal"]]
                cl = [r for r in s if not r["signal"] and r["clean"]]
                out.append(f"| {op} | {d} | {sum(1 - r['reject'] for r in sg)}/{len(sg)} | "
                           f"{100 * mean(r['reject'] for r in cl):.1f}% |\n")

    # 11. acceptance sampling: lot = 30 approved proposals, sample n, accept if 0 defects, else 100% screen
    out.append("\n## 11. Acceptance sampling after review\n\n"
               "Lot = one reviewed queue of N = 30 approved proposals; inspect n at random; accept the lot if 0 defects "
               "are found (c = 0), otherwise screen all 30 and fix (rectifying). Incoming defect rate to the plan = agent "
               "defect rate x reviewer miss rate. AOQ = p_in x Pa x (N - n) / N (binomial approximation). AOQL = max over "
               "p_in.\n\n| plan | AOQL (defects per 1,000 approved) |\n|---|---|\n")
    N_LOT = 30
    J["sampling"] = {}
    for n in (0, 3, 5, 10):
        aoql = max(p * ((1 - p) ** n if n else 1.0) * (N_LOT - n) / N_LOT for p in [i / 2000 for i in range(1, 1001)])
        J["sampling"][n] = aoql
        out.append(f"| n = {n}, c = 0 | {1000 * aoql:.1f} |\n")
    out.append("\nExample: an agent defect rate of 5% reviewed in a forced-choice card view (hidden-defect approval "
               "~55-74%) gives p_in of roughly 2.8-3.7%, above the AOQL of n = 5 sampling, so post-review sampling "
               "alone does not reach a low outgoing defect rate; attaching the evidence brings p_in to approximately 0 "
               "(upper bound per section 1).\n")

    (R / "STATS.md").write_text("".join(out), encoding="utf-8", newline="\n")
    (R / "stats.json").write_text(json.dumps(J, indent=1, default=str), encoding="utf-8", newline="\n")
    print("".join(out))


if __name__ == "__main__":
    main()
