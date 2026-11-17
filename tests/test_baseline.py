from __future__ import annotations

from approval_gate.backoffice import BackOffice
from approval_gate.baseline import new_date, run_rules
from approval_gate.generator import build_scenarios
from approval_gate.scoring import load_costs, score_episode


def test_rules_never_write_directly_on_any_scenario():
    for s in build_scenarios():
        office = BackOffice.from_scenario(s)
        run_rules(office)
        assert office.direct_writes == [], s.id
        assert not score_episode(office, s, load_costs()).gate_violation


def test_rules_handle_the_templated_wording():
    costs = load_costs()
    templated = [s for s in build_scenarios() if "templated" in s.tags and not s.ambiguous]
    wins = 0
    for s in templated:
        office = BackOffice.from_scenario(s)
        run_rules(office)
        wins += score_episode(office, s, costs).task_success
    assert wins / len(templated) > 0.8


def test_rules_flag_ambiguous_emails():
    for s in build_scenarios():
        if s.ambiguous:
            office = BackOffice.from_scenario(s)
            run_rules(office)
            assert office.flags, s.id


def test_new_date_skips_the_old_value():
    assert new_date("moves from 2026-11-20 to 2026-12-04.") == "2026-12-04"
    assert new_date("New ship date is December 6, 2026 (was November 24, 2026).") == "2026-12-06"
    assert new_date("to 12/21/2026 instead of 12/07/2026") == "2026-12-21"
    assert new_date("slips 9 days from the date we last gave you") is None
