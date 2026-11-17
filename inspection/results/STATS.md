# Study 2: statistics after referee review

## 1. Misses with the evidence shown, at the right unit

1 approved out of 2072 defect judgments on **122 unique defective items** (1 unique item(s) ever approved). Exact 95% upper bound: 0.27% if judgments were independent; 4.5% treating each unique item as one observation.

| defect type | unique items | judgments | approved | item-level 95% upper bound |
|---|---|---|---|---|
| field_mixup | 10 | 160 | 0 | 31% |
| near_value | 16 | 252 | 0 | 21% |
| relative_miscalc | 11 | 216 | 0 | 28% |
| sibling_project | 14 | 264 | 0 | 23% |
| sibling_value | 10 | 160 | 0 | 31% |
| stale_in_thread | 10 | 160 | 0 | 31% |
| stale_value | 13 | 216 | 0 | 25% |
| unsupported | 14 | 200 | 0 | 23% |
| workday_calc | 10 | 160 | 1 | 45% |
| wrong_field | 14 | 284 | 0 | 23% |

Superseded evidence (Exp 7 and 7r, a later email overrides the card's source; evidence shown): 9 approved out of 840 superseded-proposal judgments, 1.1% [0.5, 2.0] exact. All evidence-attached conditions with item-numbered output together: 10/2912 = 0.3% [0.2, 0.6] exact (judgments treated as independent). The string-format runs (Exp 1a, Exp 2 string arm) are excluded from both pools; see section 8.

Totals over all committed logs (inspection/results/raw_*.txt): 1880 review runs, 60720 item decisions. The pilots before Exp 1a and Exp 9 were not kept and are not in these totals.

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

Forced-choice (A/R) runs that rejected all 30 items:

| sample | reviewer | all-reject runs | runs |
|---|---|---|---|
| original | haiku-low | 7 | 22 |
| original | haiku | 10 | 22 |
| original | sonnet | 0 | 22 |
| original | opus | 1 | 22 |
| replication | haiku-low | 7 | 12 |
| replication | haiku | 4 | 12 |
| replication | sonnet | 0 | 12 |
| replication | opus | 1 | 12 |

## 3. Signal detection in the no-evidence views (hidden defects vs correct items)

Rating scale A > Q > R. Point 1: 'approve' vs not; point 2 (card only): 'approve or query' vs reject. d' and c with the log-linear correction; CIs by content bootstrap.

| reviewer | view | d' (approve vs not) | c | d' (A or Q vs R) |
|---|---|---|---|---|
| haiku-low | card A/R/Q | 0.02 [-1.13, 0.31] | -1.80 [-2.78, -1.22] | 1.39 [0.88, 2.15] |
| haiku-low | forced A/R | -0.07 [-0.48, 0.68] | 0.39 [-0.23, 0.87] |  |
| haiku | card A/R/Q | -0.41 [-1.13, 0.20] | -1.23 [-2.69, -0.78] | 1.26 [0.65, 1.93] |
| haiku | forced A/R | -0.14 [-0.70, 0.98] | 0.05 [-0.75, 0.52] |  |
| sonnet | card A/R/Q | 0.25 [-0.23, 1.09] | 0.42 [-0.12, 0.83] | 0.89 [0.45, 1.54] |
| sonnet | forced A/R | 0.54 [0.08, 1.18] | 0.89 [0.52, 1.21] |  |
| opus | card A/R/Q | 0.29 [-0.21, 0.97] | -0.99 [-1.67, -0.58] | 1.19 [0.59, 1.82] |
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

Repeatability: same reviewer, same queue, two runs (10% prevalence queues). Reproducibility: two reviewers, same queue, first run. 95% CIs: percentile bootstrap over queue contents (both justification styles of a content resampled together). Repeatability rests on 3 contents x 2 styles = 6 queues, so its CIs are very rough; resamples where kappa is undefined are dropped. Haiku-low vs Haiku is the same model at two effort settings, so it is closer to repeatability than to reproducibility.

| display | comparison | kappa [95% CI] | items | contents |
|---|---|---|---|---|
| card | repeatability haiku-low | 0.49 [0.21, 1.00] | 180 | 3 |
| card | repeatability haiku | 0.20 [0.08, 1.00] | 180 | 3 |
| card | repeatability sonnet | 0.46 [0.15, 1.00] | 180 | 3 |
| card | repeatability opus | 0.01 [-0.64, 1.00] | 180 | 3 |
| card | haiku-low vs haiku | 0.69 [0.38, 0.90] | 660 | 11 |
| card | haiku-low vs sonnet | 0.10 [0.04, 0.15] | 660 | 11 |
| card | haiku-low vs opus | 0.42 [0.18, 0.70] | 660 | 11 |
| card | haiku vs sonnet | 0.15 [0.08, 0.22] | 660 | 11 |
| card | haiku vs opus | 0.43 [0.19, 0.70] | 660 | 11 |
| card | sonnet vs opus | 0.04 [-0.15, 0.22] | 660 | 11 |
| source | repeatability haiku-low | 0.61 [0.28, 1.00] | 180 | 3 |
| source | repeatability haiku | 0.56 [0.39, 1.00] | 180 | 3 |
| source | repeatability sonnet | 0.94 [0.84, 1.00] | 180 | 3 |
| source | repeatability opus | 0.61 [0.46, 0.87] | 180 | 3 |
| source | haiku-low vs haiku | 0.83 [0.73, 0.93] | 660 | 11 |
| source | haiku-low vs sonnet | 0.48 [0.29, 0.66] | 660 | 11 |
| source | haiku-low vs opus | 0.58 [0.40, 0.72] | 660 | 11 |
| source | haiku vs sonnet | 0.54 [0.32, 0.75] | 660 | 11 |
| source | haiku vs opus | 0.65 [0.41, 0.84] | 660 | 11 |
| source | sonnet vs opus | 0.63 [0.39, 0.83] | 660 | 11 |
| aligned | repeatability haiku-low | 1.00 [1.00, 1.00] | 180 | 3 |
| aligned | repeatability haiku | 1.00 [1.00, 1.00] | 180 | 3 |
| aligned | repeatability sonnet | 0.97 [0.93, 1.00] | 180 | 3 |
| aligned | repeatability opus | 0.94 [0.91, 1.00] | 180 | 3 |
| aligned | haiku-low vs haiku | 0.91 [0.70, 1.00] | 660 | 11 |
| aligned | haiku-low vs sonnet | 0.95 [0.89, 0.98] | 660 | 11 |
| aligned | haiku-low vs opus | 0.79 [0.53, 0.94] | 660 | 11 |
| aligned | haiku vs sonnet | 0.88 [0.69, 0.98] | 660 | 11 |
| aligned | haiku vs opus | 0.74 [0.46, 0.93] | 660 | 11 |
| aligned | sonnet vs opus | 0.79 [0.52, 0.95] | 660 | 11 |

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

Interleaved re-test (same session, same queues, randomized order), evidence shown. The exact CI treats judgments as independent; the content-clustered CI resamples queue contents (both runs and both displays of a content together), which is the honest one since misses cluster in runs.

| reviewer | format | defects judged | approved | runs | exact 95% CI | content-clustered 95% CI | false alarms |
|---|---|---|---|---|---|---|---|
| haiku | 30-letter string | 140 | 0 | 44 | [0.0, 2.6] | [0.0, 0.0] | 7.9% |
| haiku | item-numbered | 140 | 0 | 44 | [0.0, 2.6] | [0.0, 0.0] | 8.9% |
| haiku | string minus numbered (paired by content) | | +0.0 pts | | | [+0.0, +0.0] | |
| sonnet | 30-letter string | 140 | 17 | 44 | [7.2, 18.7] | [3.2, 23.8] | 4.5% |
| sonnet | item-numbered | 140 | 0 | 44 | [0.0, 2.6] | [0.0, 0.0] | 1.0% |
| sonnet | string minus numbered (paired by content) | | +12.1 pts | | | [+3.2, +23.8] | |

Invalid outputs in the revision runs: 0.

## 9. Exp 7: superseded evidence

| reviewer | instruction | display | superseded approved | false alarms, clean | false alarms, cued |
|---|---|---|---|---|---|
| haiku-low | source-only wording | source | 3/70 | 12.1% | 25.0% |
| haiku-low | source-only wording | aligned | 3/70 | 1.1% | 4.2% |
| haiku-low | all-information wording | source | 1/70 | 15.5% | 33.5% |
| haiku | source-only wording | source | 0/70 | 6.2% | 23.3% |
| haiku | source-only wording | aligned | 0/70 | 0.0% | 8.9% |
| haiku | all-information wording | source | 1/70 | 20.3% | 44.5% |
| sonnet | source-only wording | source | 0/70 | 14.1% | 23.3% |
| sonnet | source-only wording | aligned | 1/70 | 5.6% | 12.3% |
| sonnet | all-information wording | source | 0/70 | 9.9% | 20.3% |
| opus | source-only wording | source | 0/70 | 0.8% | 6.4% |
| opus | source-only wording | aligned | 0/70 | 0.0% | 6.8% |
| opus | all-information wording | source | 0/70 | 3.4% | 10.2% |

## 10. Evidence alignment from a regex extractor (no answer key) vs the oracle alignment

The regex extractor matched the oracle's job on 330/330 items and the oracle sentence on 325/330, because the source emails are templated: on this stimulus set the oracle concern is small, on real email it would not be.

| reviewer | display | defects approved | false alarms, clean |
|---|---|---|---|
| haiku-low | oracle aligned | 0/35 | 0.6% |
| haiku-low | regex extracted | 0/35 | 2.2% |
| haiku | oracle aligned | 0/35 | 0.0% |
| haiku | regex extracted | 0/35 | 0.6% |
| sonnet | oracle aligned | 0/35 | 0.0% |
| sonnet | regex extracted | 0/35 | 2.2% |
| opus | oracle aligned | 0/35 | 0.6% |
| opus | regex extracted | 0/35 | 0.6% |

## 11. Acceptance sampling after review

Lot = one reviewed queue of N = 30 approved proposals; inspect n at random; accept the lot if 0 defects are found (c = 0), otherwise screen all 30 and fix (rectifying). Incoming defect rate to the plan = agent defect rate x reviewer miss rate. AOQ = p_in x Pa x (N - n) / N (binomial approximation). AOQL = max over p_in.

| plan | AOQL (defects per 1,000 approved) |
|---|---|
| n = 3, c = 0 | 94.9 |
| n = 5, c = 0 | 55.8 |
| n = 10, c = 0 | 23.4 |

Example: an agent defect rate of 5% reviewed in a forced-choice card view, using the hidden-defect approval of Haiku, Sonnet and Opus (54.8-73.8%), gives p_in of about 2.7-3.7%. This is an upper figure: defects with a visible cue on the card are caught far more often. With the evidence attached, all item-numbered conditions pooled (section 1b, 10/2912): p_in = 0.02% [0.01, 0.03]; the worst single cell (haiku-low, source, superseded evidence, 3/70) gives 0.21%.

## 12. Exp 9: three-message threads, prevalence within item (1 vs 10 per 30)

352 runs, 10560 item decisions, 4 base queues. Each base queue has one version with 10 defects and ten versions with 1 defect (each of the 10 defective items alone).

**Misses** (defects approved):

| split | approved / judged |
|---|---|
| prevalence 1/30 | 1/320 |
| prevalence 10/30 | 0/320 |
| terse justification | 1/320 |
| misquoting justification | 0/320 |
| haiku-low | 0/160 |
| haiku | 0/160 |
| sonnet | 1/160 |
| opus | 0/160 |

Approved defects: sonnet workday_calc in h0k1d0.

**False alarms on never-defective items** (items that are correct in every version), 1/30 vs 10/30. Difference = 1/30 minus 10/30, in points; 95% CI by bootstrap over the base queues, paired (the same items in both prevalences). With only four base queues these CIs are rough.

| reviewer | items | 1/30 | 10/30 | difference [95% CI] |
|---|---|---|---|---|
| haiku-low | clean | 4.7% (56/1180) | 5.9% (7/118) | -1.2 [-8.3, +6.2] |
| haiku-low | cued | 16.0% (67/420) | 19.0% (8/42) | -3.1 [-21.4, +13.2] |
| haiku-low | all | 7.7% (123/1600) | 9.4% (15/160) | -1.7 [-11.5, +8.1] |
| haiku | clean | 3.4% (40/1180) | 2.5% (3/118) | +0.8 [-4.5, +4.2] |
| haiku | cued | 13.3% (56/420) | 4.8% (2/42) | +8.6 [-7.1, +22.9] |
| haiku | all | 6.0% (96/1600) | 3.1% (5/160) | +2.9 [-5.3, +9.1] |
| sonnet | clean | 6.2% (73/1180) | 6.8% (8/118) | -0.6 [-4.3, +3.3] |
| sonnet | cued | 16.2% (68/420) | 16.7% (7/42) | -0.5 [-14.5, +13.9] |
| sonnet | all | 8.8% (141/1600) | 9.4% (15/160) | -0.6 [-6.8, +6.2] |
| opus | clean | 8.3% (98/1180) | 7.6% (9/118) | +0.7 [-2.3, +4.9] |
| opus | cued | 30.7% (129/420) | 28.6% (12/42) | +2.1 [-5.0, +13.2] |
| opus | all | 14.2% (227/1600) | 13.1% (21/160) | +1.1 [-2.9, +7.0] |

**False alarms on correct items that are defective in other versions** (the 1/30 versions, where 9 of the 10 target items are correct):

| reviewer | false alarms |
|---|---|
| haiku-low | 13.8% (99/720) |
| haiku | 10.6% (76/720) |
| sonnet | 17.4% (125/720) |
| opus | 26.1% (188/720) |
