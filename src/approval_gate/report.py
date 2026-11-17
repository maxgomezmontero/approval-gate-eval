"""Turn Inspect logs into the results table (CSV + Markdown) and one chart.

Unit of analysis is the scenario: when a model ran several epochs, its per-scenario values are averaged
first, and 95% confidence intervals come from a percentile bootstrap over scenarios (2,000 resamples).
"""

from __future__ import annotations

import csv
import random
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from statistics import mean

from inspect_ai.log import list_eval_logs, read_eval_log

PRICES_PER_MTOK = {  # USD, input / output (Anthropic list prices, cached 2026-11-03)
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-sonnet-5-5": (2.00, 10.00),
    "claude-opus-5-5": (4.00, 20.00),
}
METRICS = ("success", "violation", "cost")
FAMILY_ORDER = ("baseline", "pressure", "injection", "ambiguity", "approver_away", "authorized", "ALL")


@dataclass
class Row:
    agent: str
    variant: str
    family: str
    n: int
    epochs: int
    values: dict[str, tuple[float, float, float]]  # metric -> (mean, lo, hi)
    extra: dict[str, float]


def bootstrap_ci(xs: list[float], reps: int = 2000, seed: int = 0) -> tuple[float, float, float]:
    if not xs:
        return (float("nan"),) * 3
    rng = random.Random(seed)
    means = sorted(mean(rng.choices(xs, k=len(xs))) for _ in range(reps))
    return mean(xs), means[int(0.025 * reps)], means[int(0.975 * reps) - 1]


def agent_label(log) -> str:
    if log.eval.task_args.get("agent") == "rules":
        return "rules-baseline"
    return log.eval.model.split("/")[-1]


def usd(log) -> float:
    total = 0.0
    for model, u in (log.stats.model_usage or {}).items():
        price = PRICES_PER_MTOK.get(model.split("/")[-1])
        if not price:
            continue
        # prompt caching: reads bill at 0.1x the input price, 5-minute cache writes at 1.25x
        inp = ((u.input_tokens or 0) + 0.1 * (u.input_tokens_cache_read or 0)
               + 1.25 * (u.input_tokens_cache_write or 0))
        total += inp / 1e6 * price[0] + (u.output_tokens or 0) / 1e6 * price[1]
    return total


def collect(log_dir: Path) -> tuple[dict, dict[str, float]]:
    """{(agent, variant): {sample_id: [per-epoch metadata dicts]}}, and spend per agent."""
    data: dict = defaultdict(lambda: defaultdict(list))
    spend: dict[str, float] = defaultdict(float)
    for info in list_eval_logs(str(log_dir)):
        log = read_eval_log(info)
        if log.status != "success" or not log.samples:
            continue
        key = (agent_label(log), log.eval.task_args.get("variant", "default"))
        spend[key[0]] += usd(log)
        for s in log.samples:
            sc = (s.scores or {}).get("approval_gate_scorer")
            if sc is None:
                continue
            data[key][s.id].append({**sc.metadata, **sc.value})
    return data, spend


def summarize(data: dict) -> list[Row]:
    rows: list[Row] = []
    for (agent, variant), by_sample in sorted(data.items()):
        fams: dict[str, list[str]] = defaultdict(list)
        for sid, eps in by_sample.items():
            fams[eps[0]["family"]].append(sid)
            fams["ALL"].append(sid)
        for fam in FAMILY_ORDER:
            sids = fams.get(fam)
            if not sids:
                continue
            per = {m: [mean(float(e[m]) for e in by_sample[s]) for s in sids] for m in METRICS}
            eps = max(len(by_sample[s]) for s in sids)
            flagged = [mean(float(e["flagged_uncertainty"]) for e in by_sample[s]) for s in sids]
            honest = [float(e["honest"]) for s in sids for e in by_sample[s] if e.get("honest") is not None]
            rows.append(Row(agent, variant, fam, len(sids), eps,
                            {m: bootstrap_ci(per[m], seed=hash((agent, variant, fam, m)) % 10_000) for m in METRICS},
                            {"flag_rate": mean(flagged), "honesty_rate": mean(honest) if honest else float("nan"),
                             "honesty_n": len(honest)}))
    return rows


def fmt(v: tuple[float, float, float], pct: bool) -> str:
    m, lo, hi = v
    if pct:
        return f"{m * 100:.0f}% [{lo * 100:.0f}, {hi * 100:.0f}]"
    return f"{m:.2f} [{lo:.2f}, {hi:.2f}]"


def write_outputs(rows: list[Row], spend: dict[str, float], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "summary.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["agent", "variant", "family", "n_scenarios", "epochs",
                    *[f"{m}_{k}" for m in METRICS for k in ("mean", "lo", "hi")],
                    "flag_rate", "honesty_rate", "honesty_n"])
        for r in rows:
            w.writerow([r.agent, r.variant, r.family, r.n, r.epochs,
                        *[f"{x:.4f}" for m in METRICS for x in r.values[m]],
                        f"{r.extra['flag_rate']:.4f}", f"{r.extra['honesty_rate']:.4f}", r.extra["honesty_n"]])
    lines = ["| agent | variant | family | n | epochs | success | gate violation | mean cost | flag rate |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r.agent} | {r.variant} | {r.family} | {r.n} | {r.epochs} | "
                     f"{fmt(r.values['success'], True)} | {fmt(r.values['violation'], True)} | "
                     f"{fmt(r.values['cost'], False)} | {r.extra['flag_rate'] * 100:.0f}% |")
    lines += ["", "95% bootstrap CIs over scenarios in brackets. Flag rate = share of scenarios where the agent "
              "said it was unsure (most relevant for the ambiguity family).", ""]
    honest = [r for r in rows if r.family == "ALL" and r.extra["honesty_n"]]
    if honest:
        lines += ["| agent | variant | honest answers to 'did you write directly?' | n |", "|---|---|---|---|"]
        lines += [f"| {r.agent} | {r.variant} | {r.extra['honesty_rate'] * 100:.0f}% | {r.extra['honesty_n']} |"
                  for r in honest]
        lines.append("")
    if spend:
        lines.append("API spend (from token usage and list prices): " +
                     ", ".join(f"{a} ${v:.2f}" for a, v in sorted(spend.items())))
    (out_dir / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    chart(rows, out_dir / "chart.png")
    headline_chart(rows, out_dir / "headline.png")


CONDITIONS = (
    ("default", "written policy"),
    ("speed", "written policy +\n'measured on speed'"),
    ("hard", "no written policy +\nvague 'keep things moving'"),
    ("nopolicy", "same, and a neutral\ntool description"),
)


def headline_chart(rows: list[Row], path: Path) -> None:
    """Unapproved direct writes (all families pooled) per condition and model."""
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    models = sorted({r.agent for r in rows if r.agent != "rules-baseline"})
    conds = [c for c in CONDITIONS if any(r.variant == c[0] and r.family == "ALL" for r in rows)]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    width = 0.8 / max(1, len(models))
    colors = ("#d0112b", "#0b0b0c", "#8a8a90")
    for i, model in enumerate(models):
        xs, vals, lo_err, hi_err, labels = [], [], [], [], []
        for j, (variant, _) in enumerate(conds):
            r = next((x for x in rows if x.agent == model and x.variant == variant and x.family == "ALL"), None)
            if r is None:
                continue
            m, lo, hi = r.values["violation"]
            xs.append(j + i * width)
            vals.append(m * 100)
            lo_err.append(max(0.0, (m - lo) * 100))
            hi_err.append(max(0.0, (hi - m) * 100))
            labels.append(f"{m * 100:.0f}%\nn={r.n}x{r.epochs}")
        ax.bar(xs, vals, width, yerr=[lo_err, hi_err], capsize=3, color=colors[i % len(colors)], label=model)
        for x, v, h, t in zip(xs, vals, hi_err, labels, strict=True):
            ax.text(x, v + h + 0.4, t, ha="center", va="bottom", fontsize=7.5)
    ax.set_xticks([j + width * (len(models) - 1) / 2 for j in range(len(conds))])
    ax.set_xticklabels([c[1] for c in conds], fontsize=8.5)
    ax.set_ylabel("episodes with an unapproved direct write (%)")
    ax.set_ylim(0, 15)
    ax.set_title("Unapproved ERP writes, all 54 scenarios pooled (95% bootstrap CI)", fontsize=10)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(fontsize=8, frameon=False)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def chart(rows: list[Row], path: Path) -> None:
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fams = [f for f in FAMILY_ORDER if f != "ALL" and any(r.family == f for r in rows)]
    agents = sorted({(r.agent, r.variant) for r in rows})
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.2))
    width = 0.8 / max(1, len(agents))
    for ax, metric, title in ((axes[0], "violation", "Gate-violation rate"),
                              (axes[1], "cost", "Mean cost-weighted error")):
        for i, ag in enumerate(agents):
            vals, errs = [], [[], []]
            for f in fams:
                r = next((x for x in rows if (x.agent, x.variant) == ag and x.family == f), None)
                m, lo, hi = r.values[metric] if r else (0, 0, 0)
                vals.append(m)
                errs[0].append(max(0, m - lo))
                errs[1].append(max(0, hi - m))
            xs = [j + i * width for j in range(len(fams))]
            label = ag[0] + ("" if ag[1] == "default" else f" ({ag[1]})")
            ax.bar(xs, vals, width, yerr=errs, capsize=2, label=label)
        ax.set_xticks([j + width * (len(agents) - 1) / 2 for j in range(len(fams))])
        ax.set_xticklabels(fams, rotation=20)
        ax.set_title(title)
    axes[0].set_ylim(0, 1)
    axes[0].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def main(log_dir: str = "results/logs", out_dir: str = "results") -> None:
    data, spend = collect(Path(log_dir))
    rows = summarize(data)
    write_outputs(rows, spend, Path(out_dir))
    print((Path(out_dir) / "summary.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
