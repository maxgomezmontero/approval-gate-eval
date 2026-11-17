"""Night run as actually executed (budget-capped): Haiku x3 epochs, Sonnet x1 epoch, and the speed
variant on Haiku x1 epoch. The rule baseline log is produced by run_eval.py. `run_eval.py` is the general
entry point; this script just records what was run."""

from __future__ import annotations

from inspect_ai import eval as inspect_eval

from approval_gate.report import main as write_report
from approval_gate.task import approval_gate

LOG_DIR = "results/logs"
RUNS = (
    ("default", "anthropic/claude-haiku-5-5", 3),
    ("default", "anthropic/claude-sonnet-5-5", 1),
    ("speed", "anthropic/claude-haiku-5-5", 1),
)


def main() -> None:
    for variant, model, epochs in RUNS:
        inspect_eval(approval_gate(variant=variant), model=model, epochs=epochs, log_dir=LOG_DIR,
                     max_connections=8, display="plain", fail_on_error=0.2)
    write_report(LOG_DIR, "results")


if __name__ == "__main__":
    main()
