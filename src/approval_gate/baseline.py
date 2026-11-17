"""Rule-based baseline, in the spirit of a rules-first email matcher.

Keywords and regular expressions only. It never calls write_erp_direct, so it cannot violate the
gate by construction. It is not tuned on the scenarios' answers: it only reads the inbox and the ERP.
"""

from __future__ import annotations

import re
from datetime import date

from .backoffice import BackOffice

SPAM_WORDS = ("unsubscribe", "% off", "click here", "newsletter", "webinar", "mailbox is almost full")
NO_CHANGE_WORDS = ("no change", "still ships", "as planned")
JOB = re.compile(r"\bJ-\d{5}\b")
PO = re.compile(r"\bPO\s+([A-Z]{2,4}-\d{4}(?:-R\d)?)\b")
MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
     "november", "december"], start=1)}
DATE_PATTERNS = (
    re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b"),
    re.compile(r"\b([A-Z][a-z]+) (\d{1,2}), (\d{4})\b"),
    re.compile(r"\b(\d{2})/(\d{2})/(\d{4})\b"),
    re.compile(r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) ([A-Z][a-z]{2}) (\d{1,2})\b"),
)
OLD_MARKERS = ("from", "was", "instead of")


def _to_iso(pattern_idx: int, groups: tuple[str, ...]) -> str | None:
    try:
        if pattern_idx == 0:
            return date(int(groups[0]), int(groups[1]), int(groups[2])).isoformat()
        if pattern_idx == 1:
            month = MONTHS.get(groups[0].lower())
            return date(int(groups[2]), month, int(groups[1])).isoformat() if month else None
        if pattern_idx == 2:
            return date(int(groups[2]), int(groups[0]), int(groups[1])).isoformat()
        month = next((v for k, v in MONTHS.items() if k.startswith(groups[0].lower())), None)
        if month is None:
            return None
        year = 2026 if month >= 11 else 2027  # "today" is 2026-11-13; dates without a year are upcoming
        return date(year, month, int(groups[1])).isoformat()
    except ValueError:
        return None


def new_date(text: str) -> str | None:
    """First date in the text that is not introduced as the old value ("from X", "was X")."""
    found: list[tuple[int, str]] = []
    for i, pat in enumerate(DATE_PATTERNS):
        for m in pat.finditer(text):
            before = text[max(0, m.start() - 12):m.start()].lower()
            iso = _to_iso(i, m.groups())
            if iso and not any(w in before for w in OLD_MARKERS):
                found.append((m.start(), iso))
    return min(found)[1] if found else None


def detect_field(subject: str, body: str) -> str | None:
    s, b = subject.lower(), body.lower()
    if "ship" in s or "ship date" in b:
        return "ship_date"
    if "install" in s or "install" in b:
        return "install_date"
    if PO.search(subject) or "purchase order" in b:
        return "po_number"
    if "drawing" in s and "approved" in b:
        return "status"
    return None


def find_project(office: BackOffice, sender: str, subject: str, body: str) -> tuple[list[str], str]:
    """Return candidate project ids and how they were found."""
    for text, how in ((subject, "job number in subject"), (body, "job number in body")):
        jobs = {j for j in JOB.findall(text) if office.resolve_project(j)}
        if len(jobs) == 1:
            return [office.resolve_project(jobs.pop()) or ""], how
    domain = sender.split("@")[-1].rstrip(">").lower()
    by_domain = [r["id"] for r in office.projects.values()
                 if domain and domain in r.get("customer_domain", "")]
    by_name = [r["id"] for r in office.projects.values() if r["customer"].lower() in body.lower()]
    cands = sorted(set(by_name) or set(by_domain))
    return cands, "customer name"


def run_rules(office: BackOffice) -> str:
    """Process every email; returns the report the agent would submit."""
    lines: list[str] = []
    for mail in office.inbox:
        office.read_email(mail["id"])
        subject, body, sender = mail["subject"], mail["body"], mail["sender"]
        text = f"{subject}\n{body}".lower()
        if any(w in text for w in SPAM_WORDS) or any(w in text for w in NO_CHANGE_WORDS):
            continue
        fld = detect_field(subject, body)
        if fld is None:
            continue
        cands, how = find_project(office, sender, subject, body)
        if len(cands) != 1:
            if cands:
                office.flag_for_review(mail["id"], f"matches {len(cands)} projects: {', '.join(cands)}")
                lines.append(f"{mail['id']}: flagged, matches {', '.join(cands)}")
            continue
        pid = cands[0]
        if fld in ("ship_date", "install_date"):
            value = new_date(body)
        elif fld == "po_number":
            m = PO.search(subject) or PO.search(body)
            value = m.group(1) if m else None
        else:
            value = "Approved for fabrication"
        if not value:
            office.flag_for_review(mail["id"], f"could not read the new {fld}")
            lines.append(f"{mail['id']}: flagged, no value for {fld}")
            continue
        out = office.propose_erp_update(pid, fld, value, f"rule match ({how}) on {mail['id']}")
        if out.startswith("Proposal"):
            prop_id = out.split()[1]
            office.request_human_approval(prop_id, f"{fld} change from {mail['id']}")
            lines.append(f"{mail['id']}: proposed {pid} {fld} = {value}")
    return "Rule baseline report:\n" + ("\n".join(lines) if lines else "no changes proposed")
