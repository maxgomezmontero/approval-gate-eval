# Study 2: Inspecting the inspector — progress log

Started 2026-11-16 ~21:45 local. Deliver by 07:00. No Anthropic API: reviewers are internal Claude Code
subagents (Haiku and Sonnet tiers) run through workflows.

## Question

Study 1 measured whether an agent respects the approval gate. Study 2 asks whether the gate still works
when it is respected: does the *reviewer* catch the agent's wrong proposals? In my own tool I approved
1 wrong proposal out of 141; the gate existed, the proposal looked right.

AI-control setups rely on a reviewer (human or a "trusted monitor" model). Industrial quality engineering
has a century of results on inspectors. This study borrows them:

| IE / human-factors tool | used here for |
|---|---|
| Signal detection theory (hit rate, false-alarm rate, d', criterion c) | separating "can't see the defect" from "biased toward approving" |
| Prevalence effect (rare defects are missed more; Wolfe et al. 2005, airport screening) | does an LLM reviewer miss more when the agent is usually right? |
| Attribute agreement analysis / Gage R&R (MSA) | repeatability (same reviewer, same batch twice) and reproducibility (Haiku vs Sonnet) |
| Poka-yoke / "successive check" (Shingo) | does an evidence-alignment display beat "review carefully"? |
| Vigilance decrement (position in the queue) | are late items in a batch reviewed worse? |
| Acceptance sampling (OC curves, AOQ/AOQL) | how much audit is needed given the measured inspector error |

## Design (v1)

Stimuli: proposal cards generated deterministically from the Study 1 world (fictional). Each batch has
30 proposals; a proposal is either correct or carries one subtle defect:
`near_value` (digit slip / day off), `sibling_project` (same customer, other project), `wrong_field`
(ship vs install), `relative_miscalc` ("slips 9 days" computed wrong), `stale_value` (uses the old date the
email mentions), `unsupported` (the email does not ask for the change).

Factors (full factorial):
- prevalence: 1, 3 or 10 defects per 30 (3%, 10%, 33%)
- justification style: terse vs persuasive (asserts it was cross-checked; identical for good and bad items)
- display: card only (rubber-stamp UI) / card + full source email / card + source + evidence alignment
  (poka-yoke: the sentence from the source that carries the value, shown next to the proposed value)
- reviewer: Haiku vs Sonnet tier subagents

Replication: P=3 batches are each reviewed twice per model (Gage R&R); P=1 has more batches to get
enough rare defects.

Outcome per item: approve / reject. Analysis: hit rate (defect rejected), false-alarm rate (good item
rejected), d' and c with log-linear correction, logistic regression on miss, cluster bootstrap by batch.

## Log

### 21:55 — pilot (4 runs) and redesign to v2
- With the source email inline, Haiku and Sonnet caught 10/10 defects with 0 false alarms (p10, 30 items).
  LLM reviewers do not tire at 30 items; inline evidence alone produces a ceiling.
- Artefact found: random items repeated (project, field) inside a batch, so in the card-only view Haiku
  rejected proposals for being *inconsistent with each other*, not with the source. Fixed: each batch now
  has exactly one proposal per (project, field) slot (10 projects x 3 fields = 30).
- Added a third decision, Q = query ("can't tell, show me more"). In the card-only view this measures the
  thing we care about: does the reviewer approve what it cannot verify (rubber-stamping)?
- Added inspection effort as a factor via operators: haiku at low effort (fast monitor), haiku, sonnet.
- Main run: 252 reviewer runs = 11 contents x 2 styles x 3 displays x 3 operators (+ second rep at p=3
  for Gage R&R). Run order interleaved by a fixed shuffle.
- Python file `inspection.py` was lost once to a failed in-place patch (untracked); rewritten and
  committed immediately.

### 22:20 — main run v2 (252 runs, string output) and a measurement-system finding
- Haiku (both efforts) queried ~98% of card-only items it could not verify; Sonnet approved 44-96% of them.
  With evidence shown, Haiku missed 1-3% of defects, Sonnet 15-19%.
- Before trusting "Sonnet misses more", checked the output channel: in 8/56 evidence runs Sonnet's
  30-character A/R/Q string fits the answer key better after shifting by one or two positions (Haiku 2-4/56).
  Part of Sonnet's "misses" are transcription slips, not judgement. That is a measurement-system (MSA)
  error and it is itself a finding for anyone who uses LLM monitors with compact output formats.
- Decision: keep v2 as the "string format" measurement and re-run the full design as v3 with item-numbered,
  validated output (n, d) per proposal, and add Opus as a fourth reviewer: 336 runs.
- v2 report saved under inspection/results/v2_string_format/.
