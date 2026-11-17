from __future__ import annotations

from collections import Counter

from approval_gate.generator import DATA_PATH, FAMILY_SIZES, build_scenarios, read_jsonl
from approval_gate.world import PROJECTS, project_by_id


def test_deterministic():
    a = [s.to_dict() for s in build_scenarios(7)]
    b = [s.to_dict() for s in build_scenarios(7)]
    assert a == b
    assert a != [s.to_dict() for s in build_scenarios(8)]


def test_family_sizes_and_unique_ids():
    s = build_scenarios()
    assert Counter(x.family for x in s) == Counter(FAMILY_SIZES)
    assert len({x.id for x in s}) == len(s)


def test_committed_dataset_matches_generator():
    assert [s.to_dict() for s in read_jsonl(DATA_PATH)] == [s.to_dict() for s in build_scenarios()]


def test_every_non_ambiguous_scenario_has_one_real_change():
    for s in build_scenarios():
        if s.ambiguous:
            assert not s.expected and len(s.candidates) == 2
            continue
        assert len(s.expected) == 1
        e = s.expected[0]
        assert getattr(project_by_id(e.project_id), e.field) != e.value, s.id


def test_ambiguous_emails_do_not_reveal_the_project():
    for s in build_scenarios():
        if not s.ambiguous:
            continue
        body = next(m for m in s.inbox if m.id == s.event_email_id).body
        for pid in s.candidates:
            p = project_by_id(pid)
            assert p.job not in body and p.equipment not in body, s.id
            assert p.ship_date not in body and p.install_date not in body, s.id


def test_no_real_looking_domains():
    for s in build_scenarios():
        for m in s.inbox:
            assert ".example>" in m.sender, m.sender
    assert all(p.customer_domain.endswith(".example") for p in PROJECTS)
