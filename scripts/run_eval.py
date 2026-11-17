"""Run the Approval Gate eval: rule baseline + LLM models, then write the results table.

    python scripts/run_eval.py --models anthropic/claude-haiku-5-5 anthropic/claude-sonnet-5-5 --epochs 3

Prints the number of model calls and an estimated cost before running and asks for confirmation
(skip with --yes). --dry-run stops after the estimate.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from inspect_ai import eval as inspect_eval

from approval_gate.report import PRICES_PER_MTOK
from approval_gate.report import main as write_report
from approval_gate.task import MESSAGE_LIMIT, approval_gate, scenario_samples

# Rough per-sample usage measured on smoke runs: ~9 model calls, ~4.5k input tokens per call
# (the conversation grows), ~500 output tokens per call. Upper bound assumes every sample hits
# the message limit.
TYPICAL = {"calls": 9, "in_per_call": 4500, "out_per_call": 500}
WORST = {"calls": MESSAGE_LIMIT // 2 + 1, "in_per_call": 9000, "out_per_call": 1500}


def estimate(model: str, n_samples: int) -> tuple[int, float, float]:
    price = PRICES_PER_MTOK.get(model.split("/")[-1])
    calls = n_samples * TYPICAL["calls"]

    def cost(u: dict) -> float:
        if not price:
            return float("nan")
        per = u["calls"] * (u["in_per_call"] / 1e6 * price[0] + u["out_per_call"] / 1e6 * price[1])
        return n_samples * per

    return calls, cost(TYPICAL), cost(WORST)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="*", default=["anthropic/claude-haiku-5-5"])
    ap.add_argument("--epochs", type=int, default=1)
    ap.add_argument("--limit", type=int, default=None, help="first N scenarios only")
    ap.add_argument("--family", default="all")
    ap.add_argument("--variant", default="default", choices=["default", "speed"])
    ap.add_argument("--no-baseline", action="store_true")
    ap.add_argument("--no-honesty", action="store_true")
    ap.add_argument("--log-dir", default="results/logs")
    ap.add_argument("--max-connections", type=int, default=8)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()

    n = len(scenario_samples(args.family))
    if args.limit:
        n = min(n, args.limit)
    runs = n * args.epochs
    print(f"{n} scenarios x {args.epochs} epochs = {runs} samples per model, variant={args.variant}")
    total_typ = 0.0
    for m in args.models:
        calls, typ, worst = estimate(m, runs)
        total_typ += typ if typ == typ else 0
        print(f"  {m}: ~{calls} model calls, estimated ${typ:.2f} (upper bound ${worst:.2f})")
    print(f"  estimated total ${total_typ:.2f}; the rule baseline makes no model calls")
    if args.dry_run:
        return 0
    if args.models and not os.environ.get("ANTHROPIC_API_KEY") and any(m.startswith("anthropic/") for m in args.models):
        print("ANTHROPIC_API_KEY is not set; set it in your environment (see .env.example).")
        return 2
    if args.models and not args.yes and input("Run? [y/N] ").strip().lower() != "y":
        return 1

    log_dir = Path(args.log_dir)
    if not args.no_baseline:
        inspect_eval(approval_gate(variant=args.variant, family=args.family, agent="rules"),
                     model="mockllm/model", log_dir=str(log_dir), limit=args.limit, display="plain")
    for m in args.models:
        inspect_eval(approval_gate(variant=args.variant, family=args.family, honesty=not args.no_honesty),
                     model=m, epochs=args.epochs, limit=args.limit, log_dir=str(log_dir),
                     max_connections=args.max_connections, display="plain", fail_on_error=0.2)
    write_report(str(log_dir), "results")
    return 0


if __name__ == "__main__":
    sys.exit(main())
