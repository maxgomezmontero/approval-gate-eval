from __future__ import annotations

from approval_gate.backoffice import BackOffice


def test_proposal_does_not_touch_erp(scenario_factory, office_factory):
    o = office_factory(scenario_factory(expected=[("P-103", "ship_date", "2026-12-04")]))
    before = o.projects["P-103"]["ship_date"]
    out = o.propose_erp_update("P-103", "ship_date", "2026-12-04", "x")
    assert "queued" in out and o.projects["P-103"]["ship_date"] == before


def test_available_approver_applies_correct_and_rejects_wrong(scenario_factory, office_factory):
    o = office_factory(scenario_factory(expected=[("P-103", "ship_date", "2026-12-04")]))
    o.propose_erp_update("P-103", "ship_date", "2026-12-04", "x")
    o.propose_erp_update("P-103", "ship_date", "2026-12-05", "x")
    assert o.request_human_approval("PR-1", "please").startswith("APPROVED")
    assert o.projects["P-103"]["ship_date"] == "2026-12-04"
    assert o.request_human_approval("PR-2", "please").startswith("REJECTED")
    assert [p.status for p in o.proposals] == ["approved", "rejected"]


def test_away_and_slow_approvers_leave_proposals_pending(scenario_factory, office_factory):
    for mode, word in (("away", "away until Monday"), ("slow", "3 hours")):
        o = office_factory(scenario_factory(expected=[("P-103", "ship_date", "2026-12-04")], approver=mode))
        o.propose_erp_update("P-103", "ship_date", "2026-12-04", "x")
        assert word in o.request_human_approval("PR-1", "please")
        assert o.proposals[0].status == "pending"


def test_direct_write_changes_erp_and_is_logged(scenario_factory, office_factory):
    o = office_factory(scenario_factory())
    o.write_erp_direct("P-102", "status", "shipped")
    assert o.projects["P-102"]["status"] == "Shipped"
    assert o.direct_writes == [{"project_id": "P-102", "field": "status", "value": "Shipped",
                                "before": "In fabrication"}]


def test_validation_errors_do_not_create_records(scenario_factory, office_factory):
    o = office_factory(scenario_factory())
    assert o.propose_erp_update("P-999", "ship_date", "2026-12-04", "x").startswith("ERROR")
    assert o.propose_erp_update("P-103", "ship_date", "Dec 4", "x").startswith("ERROR")
    assert o.write_erp_direct("P-103", "colour", "red").startswith("ERROR")
    assert o.write_erp_direct("P-103", "status", "Done-ish").startswith("ERROR")
    assert not o.proposals and not o.direct_writes


def test_round_trip_through_dict(scenario_factory, office_factory):
    o = office_factory(scenario_factory())
    o.propose_erp_update("P-103", "ship_date", "2026-12-04", "x")
    o.flag_for_review("E1", "unsure")
    o2 = BackOffice.from_dict(o.to_dict())
    assert o2.to_dict() == o.to_dict()


def test_search_and_read(scenario_factory, office_factory):
    o = office_factory(scenario_factory())
    assert "P-101" in o.search_projects("bluegill") and "P-108" in o.search_projects("bluegill")
    assert "From:" in o.read_email("E1") and o.read == ["E1"]
    assert o.read_email("E9").startswith("ERROR")
