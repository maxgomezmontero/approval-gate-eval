"""Analysis for Study 2 (reviewer as inspector).

Input: results JSON (one record per reviewer run with a 30-char A/R string) + item keys per content.
Output: item-level CSV, cell table with signal-detection metrics, logistic regression on misses,
attribute agreement (Gage R&R), escape-rate / acceptance-sampling curves, figures.
"""

from __future__ import annotations

import csv
import json
import math
import random
import zlib
from collections import defaultdict
from pathlib import Path
from statistics import NormalDist, mean

import numpy as np

Z = NormalDist().inv_cdf
OPERATORS = ("haiku-low", "haiku", "sonnet", "opus")


# ------------------------------------------------------------------ loading

def parse_results(text: str) -> list[dict]:
    """Workflow output lines 'batch|operator|rep|decisions' -> run records with factors."""
    out = []
    for line in text.strip().splitlines():
        if not line.strip():
            continue
        batch, op, rep, dec = line.strip().split("|")
        content, style, display = batch.split("-")
        prev = int(content[1:3]) if content.startswith("p") else None  # Exp 4: filled from the key
        out.append({"batch": batch, "content": content, "prevalence": prev, "style": style,
                    "display": display, "operator": op, "model": op.split("-")[0], "rep": int(rep),
                    "decisions": None if dec in ("NULL", "BAD") else dec})
    return out


def ambiguity_cues(items: list[dict]) -> dict[int, dict[str, int]]:
    """Reasons a careful reviewer could legitimately hesitate on a *correct* proposal:
    conflict  - with all proposals applied, the project's ship date would fall after its install date
    yearless  - the source gives the date without a year ("the 26th of November")
    relative  - the source gives a shift ("slips 13 days from the date we last gave you")"""
    by_proj: dict[str, dict[str, str]] = defaultdict(dict)
    for it in items:
        by_proj[it["project_id"]][it["field"]] = it["new"]
    out = {}
    for it in items:
        d = by_proj[it["project_id"]]
        ship, inst = d.get("ship_date"), d.get("install_date")
        conflict = int(it["field"] in ("ship_date", "install_date") and bool(ship and inst) and ship > inst)
        out[it["pos"]] = {"cue_conflict": conflict,
                          "cue_yearless": int(" of " in it["key_sentence"] and "the " in it["key_sentence"]),
                          "cue_relative": int(" slips " in it["key_sentence"])}
    return out


def item_rows(results: list[dict], key_dir: Path) -> list[dict]:
    """One row per (run, item). caught = not approved (R or Q); for good items that is a false alarm."""
    keys: dict[str, list[dict]] = {}
    rows = []
    for r in results:
        d = r.get("decisions")
        if not d or d in ("BAD", "NULL") or set(d) - {"A", "R", "Q"}:
            continue
        items = keys.setdefault(r["content"], json.loads((key_dir / f"{r['content']}.json").read_text(encoding="utf-8")))
        if len(d) != len(items):
            continue
        prev = r["prevalence"] if r["prevalence"] is not None else sum(1 for it in items if it["defect"])
        cues = ambiguity_cues(items)
        for it in items:
            dec = d[it["pos"] - 1]
            rows.append({
                "run": f"{r['batch']}|{r['operator']}|{r['rep']}", "batch": r["batch"], "content": r["content"],
                "prevalence": prev, "style": r["style"], "display": r["display"],
                "operator": r["operator"], "model": r["model"], "rep": r["rep"], "pos": it["pos"], "n_items": len(items),
                "defect": it["defect"] or "", "field": it["field"], "signal": int(it["defect"] is not None),
                "decision": dec, "reject": int(dec != "A"), "query": int(dec == "Q"), "hard_reject": int(dec == "R"),
                **cues[it["pos"]], "clean": int(not any(cues[it["pos"]].values())),
            })
    return rows


def write_items_csv(rows: list[dict], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]), lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


# ------------------------------------------------------------------ signal detection

def sdt(rows: list[dict]) -> dict:
    sig = [r for r in rows if r["signal"]]
    noi = [r for r in rows if not r["signal"]]
    hits, fas = sum(r["reject"] for r in sig), sum(r["reject"] for r in noi)
    h = (hits + 0.5) / (len(sig) + 1)  # log-linear correction (Hautus 1995)
    f = (fas + 0.5) / (len(noi) + 1)
    return {
        "n_signal": len(sig), "n_noise": len(noi),
        "hit": hits / len(sig) if sig else float("nan"), "fa": fas / len(noi) if noi else float("nan"),
        "miss": 1 - hits / len(sig) if sig else float("nan"),
        "dprime": Z(h) - Z(f), "c": -0.5 * (Z(h) + Z(f)),
    }


def cluster_bootstrap(rows: list[dict], stat, reps: int = 2000, key: str = "run", seed: int = 0):
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
        except (ZeroDivisionError, ValueError):
            continue
        if v == v:
            vals.append(v)
    vals.sort()
    if not vals:
        return (float("nan"), float("nan"))
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]


def cell_table(rows: list[dict], by: tuple[str, ...]) -> list[dict]:
    cells: dict[tuple, list[dict]] = defaultdict(list)
    for r in rows:
        cells[tuple(r[k] for k in by)].append(r)
    out = []
    for k, rs in sorted(cells.items(), key=lambda kv: tuple(str(x) for x in kv[0])):
        s = sdt(rs)
        seed = zlib.crc32("|".join(map(str, k)).encode())
        lo, hi = cluster_bootstrap(rs, lambda x: sdt(x)["miss"], seed=seed) if s["n_signal"] else (math.nan, math.nan)
        dlo, dhi = cluster_bootstrap(rs, lambda x: sdt(x)["dprime"], seed=seed + 1)
        out.append({**dict(zip(by, k, strict=True)), **s, "miss_lo": lo, "miss_hi": hi, "d_lo": dlo, "d_hi": dhi,
                    "runs": len({r["run"] for r in rs})})
    return out


# ------------------------------------------------------------------ logistic regression (IRLS)

def logistic(rows: list[dict], features: list[tuple[str, callable]]) -> list[dict]:
    """Logit of miss (approve a defective item) on named features; cluster-bootstrap CIs by run."""
    sig = [r for r in rows if r["signal"]]

    def fit(rs: list[dict]) -> np.ndarray:
        X = np.array([[1.0] + [float(fn(r)) for _, fn in features] for r in rs])
        y = np.array([1.0 - r["reject"] for r in rs])
        b = np.zeros(X.shape[1])
        for _ in range(50):
            p = 1 / (1 + np.exp(-X @ b))
            W = p * (1 - p) + 1e-9
            H = X.T @ (X * W[:, None]) + 1e-6 * np.eye(X.shape[1])  # tiny ridge for separation
            step = np.linalg.solve(H, X.T @ (y - p))
            b += step
            if np.max(np.abs(step)) < 1e-8:
                break
        return b

    est = fit(sig)
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in sig:
        groups[r["run"]].append(r)
    names = sorted(groups)
    rng = random.Random(7)
    boots = []
    for _ in range(600):
        sample = [x for g in rng.choices(names, k=len(names)) for x in groups[g]]
        try:
            boots.append(fit(sample))
        except np.linalg.LinAlgError:
            continue
    B = np.array(boots)
    out = []
    for i, name in enumerate(["intercept"] + [n for n, _ in features]):
        lo, hi = np.percentile(B[:, i], [2.5, 97.5])
        out.append({"term": name, "logodds": float(est[i]), "lo": float(lo), "hi": float(hi),
                    "odds_ratio": math.exp(est[i])})
    return out


# ------------------------------------------------------------------ attribute agreement (Gage R&R)

def kappa(a: list[int], b: list[int]) -> float:
    n = len(a)
    po = sum(x == y for x, y in zip(a, b, strict=True)) / n
    pa, pb = sum(a) / n, sum(b) / n
    pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def agreement(rows: list[dict]) -> dict:
    by_run: dict[tuple, dict[int, int]] = defaultdict(dict)
    truth: dict[tuple, int] = {}
    for r in rows:
        by_run[(r["batch"], r["operator"], r["rep"])][r["pos"]] = r["reject"]
        truth[(r["batch"], r["pos"])] = r["signal"]
    out = {}
    for model in OPERATORS:  # repeatability: rep 0 vs rep 1, same model, same batch
        a, b = [], []
        for (batch, m, rep), d in by_run.items():
            if m == model and rep == 0 and (batch, m, 1) in by_run:
                d2 = by_run[(batch, m, 1)]
                for pos in d:
                    a.append(d[pos])
                    b.append(d2[pos])
        if a:
            out[f"repeatability_kappa_{model}"] = kappa(a, b)
            out[f"repeatability_agree_{model}"] = mean(int(x == y) for x, y in zip(a, b, strict=True))
            out[f"repeatability_n_{model}"] = len(a)
    for i, m1 in enumerate(OPERATORS):  # reproducibility: every pair of reviewers, rep 0, same batch
        for m2 in OPERATORS[i + 1:]:
            a, b = [], []
            for (batch, m, rep), d in by_run.items():
                if m == m1 and rep == 0 and (batch, m2, 0) in by_run:
                    d2 = by_run[(batch, m2, 0)]
                    for pos in d:
                        a.append(d[pos])
                        b.append(d2[pos])
            if a:
                out[f"reproducibility_kappa_{m1}_vs_{m2}"] = kappa(a, b)
    for model in OPERATORS:  # vs standard
        a = [truth[(batch, pos)] for (batch, m, rep), d in by_run.items() if m == model for pos in d]
        b = [d[pos] for (batch, m, rep), d in by_run.items() if m == model for pos in d]
        if a:
            out[f"vs_standard_kappa_{model}"] = kappa(a, b)
    return out


# ------------------------------------------------------------------ escapes and sampling

def escapes_per_1000(p_defect: float, miss: float) -> float:
    """Defective changes that reach the ERP per 1,000 proposals with 100% review by this reviewer."""
    return 1000 * p_defect * miss


def oc_two_stage(p_defect: float, miss: float, audit_frac: float, audit_miss: float = 0.0) -> float:
    """Escapes per 1,000 when a second, independent audit re-checks a random fraction of approvals."""
    after_first = p_defect * miss
    return 1000 * after_first * (1 - audit_frac * (1 - audit_miss))
