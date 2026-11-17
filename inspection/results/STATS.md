# Study 2: statistics after referee review

## 1. Misses with the evidence shown, at the right unit

0 approved out of 1432 defect judgments on **82 unique defective items**. Exact 95% upper bound: 0.26% if judgments were independent; 4.4% treating each unique item as one observation (perfect within-item correlation). Per reviewer (each saw every unique item at least once): upper bound 4.4% at the item level.

| defect type | unique items | judgments | approved | item-level 95% upper bound |
|---|---|---|---|---|
| near_value | 16 | 252 | 0 | 21% |
| relative_miscalc | 11 | 216 | 0 | 28% |
| sibling_project | 14 | 264 | 0 | 23% |
| stale_value | 13 | 216 | 0 | 25% |
| unsupported | 14 | 200 | 0 | 23% |
| wrong_field | 14 | 284 | 0 | 23% |

## 2. No evidence attached: decision set x reviewer (content-clustered 95% CIs)

### Original queues (11 contents, 2 justification styles)

| reviewer | correct approved, A/R/Q | correct approved, A/R | paired difference | hidden defects approved, A/R/Q | hidden defects approved, A/R | contents |
|---|---|---|---|---|---|---|
| haiku-low | 3.6% [0.0, 10.8] | 63.7% [41.1, 86.7] | +60.2 pts [+38.2, +82.0] | 2.4% [0.0, 11.1] | 66.7% [35.0, 78.9] | 11 |
| haiku | 7.5% [0.0, 18.7] | 49.2% [23.7, 75.7] | +41.7 pts [+17.1, +67.8] | 14.3% [0.0, 28.6] | 54.8% [11.1, 71.8] | 11 |
| sonnet | 70.7% [54.0, 86.3] | 87.8% [79.4, 95.1] | +17.1 pts [+6.1, +29.8] | 61.9% [30.0, 78.1] | 73.8% [53.3, 85.2] | 11 |
| opus | 19.8% [7.3, 33.8] | 88.5% [78.3, 95.7] | +68.6 pts [+48.0, +85.9] | 11.9% [0.0, 23.3] | 71.4% [50.0, 86.4] | 11 |

### Replication (6 fresh contents at 10% prevalence, terse, 2 runs each)

| reviewer | correct approved, A/R/Q | correct approved, A/R | paired difference | hidden defects approved, A/R/Q | hidden defects approved, A/R | contents |
|---|---|---|---|---|---|---|
| haiku-low | 15.4% [0.0, 32.1] | 38.3% [8.0, 70.4] | +22.8 pts [+7.1, +39.2] | 8.3% [0.0, 25.0] | 25.0% [6.7, 55.6] | 6 |
| haiku | 0.0% [0.0, 0.0] | 62.3% [30.2, 94.4] | +62.3 pts [+30.2, +94.4] | 0.0% [0.0, 0.0] | 45.8% [14.3, 94.4] | 6 |
| sonnet | 88.9% [84.6, 92.9] | 88.3% [80.6, 93.5] | -0.6 pts [-4.9, +2.2] | 66.7% [46.7, 90.9] | 70.8% [50.0, 94.4] | 6 |
| opus | 14.2% [0.0, 30.2] | 84.6% [67.9, 94.4] | +70.4 pts [+54.3, +87.0] | 12.5% [0.0, 33.3] | 62.5% [42.9, 94.4] | 6 |

Interaction (original): removing Q raised approval of correct items by 57 points on average for Haiku-low, Haiku and Opus, and by 17 points for Sonnet, which already approved 71% with Q available.

Interaction (replication): removing Q raised approval of correct items by 52 points on average for Haiku-low, Haiku and Opus, and by -1 points for Sonnet, which already approved 89% with Q available.

## 3. Signal detection in the no-evidence views (hidden defects vs correct items)

Rating scale A > Q > R. Point 1: 'approve' vs not; point 2 (card only): 'approve or query' vs reject. d' and c with the log-linear correction; CIs by content bootstrap.

| reviewer | view | d' (approve vs not) | c | d' (A or Q vs R) |
|---|---|---|---|---|
| haiku-low | card A/R/Q | 0.02 [-1.13, 0.31] | -1.80 [-2.78, -1.22] | 1.39 |
| haiku-low | forced A/R | -0.07 [-0.48, 0.68] | 0.39 [-0.23, 0.87] |  |
| haiku | card A/R/Q | -0.41 [-1.13, 0.20] | -1.23 [-2.69, -0.78] | 1.26 |
| haiku | forced A/R | -0.14 [-0.70, 0.98] | 0.05 [-0.75, 0.52] |  |
| sonnet | card A/R/Q | 0.25 [-0.23, 1.09] | 0.42 [-0.12, 0.83] | 0.89 |
| sonnet | forced A/R | 0.54 [0.08, 1.18] | 0.89 [0.52, 1.21] |  |
| opus | card A/R/Q | 0.29 [-0.21, 0.97] | -0.99 [-1.67, -0.58] | 1.19 |
| opus | forced A/R | 0.64 [-0.00, 1.42] | 0.87 [0.53, 1.20] |  |

## 4. Persuasive justification where the criterion is free to move

| reviewer | view | correct approved, terse | correct approved, persuasive |
|---|---|---|---|
| haiku-low | card A/R/Q | 7.1% [0.0, 21.6] | 0.0% [0.0, 0.0] |
| haiku-low | forced A/R | 69.5% [41.4, 98.3] | 58.0% [30.8, 85.8] |
| haiku | card A/R/Q | 14.9% [0.0, 37.4] | 0.0% [0.0, 0.0] |
| haiku | forced A/R | 49.2% [22.1, 76.4] | 49.2% [22.4, 76.9] |
| sonnet | card A/R/Q | 85.1% [76.7, 92.3] | 56.3% [30.2, 82.7] |
| sonnet | forced A/R | 86.1% [77.3, 94.0] | 89.5% [80.6, 96.6] |
| opus | card A/R/Q | 24.1% [0.0, 51.9] | 15.6% [0.0, 36.9] |
| opus | forced A/R | 93.2% [88.9, 96.4] | 83.7% [64.1, 96.2] |

## 5. Attribute agreement (AIAG-style), per display, 3-category A/R/Q, Cohen's kappa

Repeatability: same reviewer, same queue, two runs (10% prevalence queues). Reproducibility: two reviewers, same queue, first run.

| display | comparison | kappa | items |
|---|---|---|---|
| card | repeatability haiku-low | 0.49 | 180 |
| card | repeatability haiku | 0.20 | 180 |
| card | repeatability sonnet | 0.46 | 180 |
| card | repeatability opus | 0.01 | 180 |
| card | haiku-low vs haiku | 0.69 | 660 |
| card | haiku-low vs sonnet | 0.10 | 660 |
| card | haiku-low vs opus | 0.42 | 660 |
| card | haiku vs sonnet | 0.15 | 660 |
| card | haiku vs opus | 0.43 | 660 |
| card | sonnet vs opus | 0.04 | 660 |
| source | repeatability haiku-low | 0.61 | 180 |
| source | repeatability haiku | 0.56 | 180 |
| source | repeatability sonnet | 0.94 | 180 |
| source | repeatability opus | 0.61 | 180 |
| source | haiku-low vs haiku | 0.83 | 660 |
| source | haiku-low vs sonnet | 0.48 | 660 |
| source | haiku-low vs opus | 0.58 | 660 |
| source | haiku vs sonnet | 0.54 | 660 |
| source | haiku vs opus | 0.65 | 660 |
| source | sonnet vs opus | 0.63 | 660 |
| aligned | repeatability haiku-low | 1.00 | 180 |
| aligned | repeatability haiku | 1.00 | 180 |
| aligned | repeatability sonnet | 0.97 | 180 |
| aligned | repeatability opus | 0.94 | 180 |
| aligned | haiku-low vs haiku | 0.91 | 660 |
| aligned | haiku-low vs sonnet | 0.95 | 660 |
| aligned | haiku-low vs opus | 0.79 | 660 |
| aligned | haiku vs sonnet | 0.88 | 660 |
| aligned | haiku vs opus | 0.74 | 660 |
| aligned | sonnet vs opus | 0.79 | 660 |

## 6. Exp 4: false alarms on items that are never defective, by prevalence

Same items in every version; only the other positions change. Two base queues, so CIs are by run.

| reviewer | items | 1/30 | 3/30 | 10/30 |
|---|---|---|---|---|
| haiku-low | clean | 15.1% (45/298) | 13.6% (12/88) | 0.0% (0/28) |
| haiku-low | cued | 26.5% (27/102) | 15.6% (5/32) | 0.0% (0/12) |
| haiku | clean | 16.4% (49/298) | 8.0% (7/88) | 14.3% (4/28) |
| haiku | cued | 23.5% (24/102) | 15.6% (5/32) | 8.3% (1/12) |
| sonnet | clean | 0.0% (0/298) | 0.0% (0/88) | 0.0% (0/28) |
| sonnet | cued | 0.0% (0/102) | 0.0% (0/32) | 0.0% (0/12) |
| opus | clean | 0.0% (0/298) | 0.0% (0/88) | 0.0% (0/28) |
| opus | cued | 9.8% (10/102) | 12.5% (4/32) | 0.0% (0/12) |

## 7. Exp 5: queue length and serial position (source shown)

| reviewer | queue | misses | false alarms, first third | middle | last third |
|---|---|---|---|---|---|
| haiku-low | 30 | 0/6 | 10.0% | 15.5% | 10.7% |
| haiku-low | 90 | 0/18 | 0.6% | 0.6% | 0.6% |
| haiku-low | 150 | 0/30 | 0.3% | 0.3% | 0.0% |
| haiku | 30 | 0/6 | 13.3% | 25.9% | 16.1% |
| haiku | 90 | 0/18 | 5.8% | 8.5% | 5.2% |
| haiku | 150 | 0/30 | 0.3% | 0.7% | 0.3% |
| sonnet | 30 | 0/6 | 3.3% | 8.6% | 8.9% |
| sonnet | 90 | 0/18 | 0.0% | 0.0% | 0.0% |
| sonnet | 150 | 0/30 | 0.0% | 0.0% | 0.0% |
| opus | 30 | 0/6 | 3.3% | 8.6% | 14.3% |
| opus | 90 | 0/18 | 3.5% | 1.7% | 0.6% |
| opus | 150 | 0/30 | 3.1% | 3.8% | 2.8% |

## 8. Output format

First pass (v2), Sonnet, evidence shown: runs whose string fits the key better after a shift: 8/56. Misses in those runs: 15/20; in the other runs: 15/156 (9.6%). The shift diagnosis uses the key, so it is suggestive, not proof.


## 9. Exp 7: superseded evidence

| reviewer | instruction | display | superseded approved | false alarms, clean | false alarms, cued |
|---|---|---|---|---|---|
| haiku-low | source-only wording | source | 3/70 | 12.1% | 25.0% |
| haiku-low | source-only wording | aligned | 3/70 | 1.1% | 4.2% |
| haiku | source-only wording | source | 0/70 | 6.2% | 23.3% |
| haiku | source-only wording | aligned | 0/70 | 0.0% | 8.9% |
| sonnet | source-only wording | source | 0/70 | 14.1% | 23.3% |
| sonnet | source-only wording | aligned | 1/70 | 5.6% | 12.3% |
| opus | source-only wording | source | 0/70 | 0.8% | 6.4% |
| opus | source-only wording | aligned | 0/70 | 0.0% | 6.8% |

## 11. Acceptance sampling after review

Lot = one reviewed queue of N = 30 approved proposals; inspect n at random; accept the lot if 0 defects are found (c = 0), otherwise screen all 30 and fix (rectifying). Incoming defect rate to the plan = agent defect rate x reviewer miss rate. AOQ = p_in x Pa x (N - n) / N (binomial approximation). AOQL = max over p_in.

| plan | AOQL (defects per 1,000 approved) |
|---|---|
| n = 0, c = 0 | 500.0 |
| n = 3, c = 0 | 94.9 |
| n = 5, c = 0 | 55.8 |
| n = 10, c = 0 | 23.4 |

Example: an agent defect rate of 5% reviewed in a forced-choice card view (hidden-defect approval ~55-74%) gives p_in of roughly 2.8-3.7%, above the AOQL of n = 5 sampling, so post-review sampling alone does not reach a low outgoing defect rate; attaching the evidence brings p_in to approximately 0 (upper bound per section 1).
