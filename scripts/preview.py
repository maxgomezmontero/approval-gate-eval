"""Print a few generated scenarios for a quick human check."""

from __future__ import annotations

import sys
from collections import Counter

from approval_gate.generator import DATA_PATH, build_scenarios, write_jsonl


def main(ids: list[str]) -> None:
    scenarios = build_scenarios()
    write_jsonl(scenarios, DATA_PATH)
    print(len(scenarios), dict(Counter(s.family for s in scenarios)))
    for s in scenarios:
        if ids and s.id not in ids:
            continue
        event = next(m for m in s.inbox if m.id == s.event_email_id)
        print("----", s.id, s.approver, s.tags, [vars(x) for x in s.expected], s.candidates)
        print(event.sender, "|", event.subject)
        print(event.body)


if __name__ == "__main__":
    main(sys.argv[1:])
