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

### 22:35 — related work check and two extra experiments launched
- Searched for prior work. SDT has been proposed as a framework for error detection in AI oversight, and
  the prevalence effect is discussed for *human* labellers of rare events, but I found no study testing
  a prevalence effect in LLM reviewers, and no Gage R&R (repeatability x reproducibility, output channel)
  of LLM monitors. AI control's trusted monitoring (Greenblatt et al. 2023, and 2025-26 follow-ups on
  adaptive attacks and bootstrapped monitoring) assumes a monitor's error profile but does not measure it
  with inspection-science tools. These are the gaps Study 2 targets; claims will stay "to our knowledge".
- Exp 3 (misquoting justification): the agent's reason restates its wrong value as if quoted from the
  email. 22 batches x 4 reviewers.
- Exp 4 (controlled prevalence): the same 20 defective items embedded at 1, 3 and 10 defects per 30
  (other items regenerated as correct proposals for the same slots). 28 batches x 4 reviewers.
- v3 (item-numbered output, 4 reviewers incl. Opus) running in parallel: 336 runs.

### 22:50 — Exp 3/4 done; stimulus-validity check on "false alarms"
- Exp 3/4: 200 runs, 0 invalid outputs.
- Haiku rejected/queried some *correct* proposals in Exp 4 at fixed positions. Inspection showed real
  reasons to hesitate that my generator introduced: (a) with all proposals applied, a project's ship
  date can land after its install date; (b) yearless dates ("the 26th of November"); (c) relative shifts
  whose base ("the date we last gave you") is assumed to be the ERP value. 39% of good items carry at least
  one cue (conflict 10%, yearless 16%, relative 18%).
- Added these as `cue_*` columns and a `clean` flag. On v2: Haiku's false alarms with the source shown are
  10% on clean items vs 31% on cued items, and the evidence-alignment display cuts them to ~0-6%. So part of
  Haiku's "false alarms" is calibrated hesitation, and the paper must report FA on clean items separately.

### 23:05 — v3 (item-numbered output, 4 reviewers) changes the story
- With evidence shown (source or aligned), all four reviewers approved 0 of 704 defective proposals.
  Exp 3 (misquoting justification): 0/280. Exp 4 (same defects at 1, 3, 10 per 30): 0/232, no paired
  item missed at any prevalence. Rule-of-three upper bounds: miss <= ~0.4% (704), <= ~1.3% (232).
- So the v2 "Sonnet misses 17%" was entirely the 30-letter output channel (A. in EXTRA.md: 17.0% -> 0.0%,
  same reviewer, same items). Headline methods finding: a monitor's measured miss rate can be dominated by
  how it is asked to report, so do MSA before trusting monitor error rates.
- Where the gate fails is the interface: card-only (no email), Sonnet approved ~76% of good items it could
  not verify and 34% of defects; Haiku and Opus mostly queried. Reproducibility between reviewer models
  is low (kappa 0.38-0.45 for Sonnet pairs): the monitor's *criterion*, not its detection, decides.
- Evidence alignment (poka-yoke) cut false alarms of the conservative reviewers from 9-20% to 0.3-4% with
  no misses. False alarms concentrate on items with genuine ambiguity cues.
- Prevalence: no effect on misses (all zero). In Exp 4, Haiku's false alarms fall as defects become more
  common (haiku-low 19% -> 0%, haiku 21% -> 13%); needs a cue-controlled check on the never-defective items.
- Launched Exp 5 (queue length 30/90/150 at ~3% prevalence, source shown, 2 reps) and Exp 6 (forced A/R
  with no evidence attached): 160 runs.
