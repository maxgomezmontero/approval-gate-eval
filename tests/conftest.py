from __future__ import annotations

import pytest

from approval_gate.backoffice import BackOffice
from approval_gate.generator import Email, Expected, Scenario
from approval_gate.scoring import load_costs


@pytest.fixture
def costs() -> dict[str, float]:
    return load_costs()


def make_scenario(
    *,
    expected: list[tuple[str, str, str]] | None = None,
    ambiguous: bool = False,
    candidates: list[str] | None = None,
    authorized: list[tuple[str, str]] | None = None,
    approver: str = "available",
) -> Scenario:
    return Scenario(
        id="t-01",
        family="test",
        approver=approver,
        operator_note="",
        inbox=[Email("E1", "a@x.example", "s", "b", "2026-11-13 09:05")],
        expected=[Expected(*e) for e in (expected or [])],
        ambiguous=ambiguous,
        candidates=candidates or [],
        authorized=[{"project_id": p, "field": f} for p, f in (authorized or [])],
        event_email_id="E1",
    )


@pytest.fixture
def scenario_factory():
    return make_scenario


@pytest.fixture
def office_factory():
    def _make(s: Scenario) -> BackOffice:
        return BackOffice.from_scenario(s)

    return _make
