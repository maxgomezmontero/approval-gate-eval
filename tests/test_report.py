from __future__ import annotations

from approval_gate.report import bootstrap_ci, summarize


def test_bootstrap_ci_brackets_the_mean():
    m, lo, hi = bootstrap_ci([0, 0, 1, 1, 1, 0, 1, 0, 0, 1])
    assert m == 0.5 and lo <= m <= hi and lo >= 0 and hi <= 1


def test_constant_data_has_zero_width_ci():
    assert bootstrap_ci([1.0] * 12) == (1.0, 1.0, 1.0)


def test_epochs_are_averaged_within_a_scenario():
    def ep(fam, success, violation=0.0, cost=0.0):
        return {"family": fam, "success": success, "violation": violation, "cost": cost,
                "flagged_uncertainty": False, "honest": True}

    data = {("m", "default"): {
        "a": [ep("baseline", 1), ep("baseline", 0), ep("baseline", 1)],
        "b": [ep("pressure", 0, 1, 8)],
    }}
    rows = {r.family: r for r in summarize(data)}
    assert abs(rows["baseline"].values["success"][0] - 2 / 3) < 1e-9
    assert rows["ALL"].n == 2 and rows["ALL"].epochs == 3
    assert rows["pressure"].values["cost"][0] == 8
