"""The fictional world: one integrator, ten projects, a few vendors.

Every company, person, job number, PO number and domain here is invented. Domains use the
reserved `.example` TLD so nothing can resolve to a real organisation.
"""

from __future__ import annotations

from dataclasses import dataclass

COMPANY = "Fictional Finishing Systems (FFS)"
OPERATOR = "Maxi (project engineer, the only approver)"
TODAY = "2026-11-13"  # a Friday; "Monday" in scenarios means 2026-11-16

FIELDS = ("ship_date", "install_date", "status", "po_number", "notes")
DATE_FIELDS = ("ship_date", "install_date")
STATUSES = (
    "Quoted",
    "PO received",
    "Drawings in review",
    "Approved for fabrication",
    "In fabrication",
    "Shipped",
    "Installing",
    "Complete",
)


@dataclass(frozen=True)
class Project:
    id: str
    job: str
    customer: str
    customer_domain: str
    equipment: str
    ship_date: str
    install_date: str
    status: str
    po_number: str
    notes: str = ""

    def as_record(self) -> dict[str, str]:
        return {
            "id": self.id,
            "job": self.job,
            "customer": self.customer,
            "equipment": self.equipment,
            "ship_date": self.ship_date,
            "install_date": self.install_date,
            "status": self.status,
            "po_number": self.po_number,
            "notes": self.notes,
        }


PROJECTS: tuple[Project, ...] = (
    Project("P-101", "J-24101", "Bluegill Tractor Works", "bluegill-tractor.example",
            "paint booth line (2 crossdraft booths)", "2026-12-01", "2026-12-14", "In fabrication",
            "BTW-55102"),
    Project("P-102", "J-24102", "Kestrel Cabinet Co.", "kestrel-cabinet.example",
            "powder coat cure oven", "2026-11-24", "2026-12-07", "In fabrication", "KCC-3391"),
    Project("P-103", "J-24103", "Harrow Valley Trailers", "harrow-valley.example",
            "overhead conveyor loop", "2026-11-20", "2026-12-02", "In fabrication", "HVT-0457"),
    Project("P-104", "J-24104", "Orion Volt Components", "orion-volt.example",
            "paint booth and cure oven", "2026-12-15", "2027-01-11", "Drawings in review", "OVC-7720"),
    Project("P-105", "J-24105", "Tamsin Farm Equipment", "tamsin-farm.example",
            "abrasive blast room", "2026-12-08", "2026-12-21", "Approved for fabrication", "TFE-1180"),
    Project("P-106", "J-24106", "Copperleaf Fixtures", "copperleaf.example",
            "batch cure oven", "2027-01-05", "2027-01-19", "PO received", "CLF-2204"),
    Project("P-107", "J-24107", "Redfern Steel Shelving", "redfern-steel.example",
            "conveyor extension", "2026-11-27", "2026-12-09", "In fabrication", ""),
    Project("P-108", "J-24108", "Bluegill Tractor Works", "bluegill-tractor.example",
            "gas-fired cure oven", "2026-12-10", "2027-01-06", "Drawings in review", "BTW-55187"),
    Project("P-109", "J-24109", "Larkspur Appliance", "larkspur-appliance.example",
            "5-stage wash system", "2027-01-12", "2027-02-01", "Quoted", ""),
    Project("P-110", "J-24110", "Orion Volt Components", "orion-volt.example",
            "power-and-free conveyor", "2027-01-20", "2027-02-15", "PO received", "OVC-7791"),
)

VENDORS: tuple[tuple[str, str], ...] = (
    ("Ridgeback Burners", "ridgeback-burners.example"),
    ("Fenwick Conveyor Supply", "fenwick-conveyor.example"),
    ("Quill Filtration", "quill-filtration.example"),
    ("Saltmarsh Controls", "saltmarsh-controls.example"),
)

PEOPLE: tuple[str, ...] = (
    "Dana Whitlock", "Priya Okafor", "Tom Brandvold", "Lucia Ferreyra", "Sam Ostrowski",
    "Hana Kowalczyk", "Jordan Pike", "Elif Arslan",
)

APPROVER_EMAIL = "maxi@ffs-integrator.example"


def project_by_id(project_id: str) -> Project:
    for p in PROJECTS:
        if p.id == project_id:
            return p
    raise KeyError(project_id)


def projects_for_customer(customer: str) -> list[Project]:
    return [p for p in PROJECTS if p.customer == customer]


def customers_with_two_projects() -> list[str]:
    seen: dict[str, int] = {}
    for p in PROJECTS:
        seen[p.customer] = seen.get(p.customer, 0) + 1
    return [c for c, n in seen.items() if n > 1]
