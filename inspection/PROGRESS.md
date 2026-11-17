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
