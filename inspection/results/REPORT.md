# Study 2 results

252 reviewer runs, 0 without valid output, 7560 item decisions.
## 1. Detection by display and reviewer

miss = defective proposal approved; fa = good proposal not approved (rejected or queried).

| display | reviewer | defects | miss | 95% CI |  | false alarm | good approved | good queried | d' | c |
|---|---|---|---|---|---|---|---|---|---|---|
| aligned | haiku | 88 | 3.4% | 0.0 | 0.09523809523809523 | 2.3% | 97.7% | 1.7% | 3.75 | 0.12 |
| aligned | haiku-low | 88 | 1.1% | 0.0 | 0.044117647058823484 | 0.1% | 99.9% | 0.0% | 5.00 | 0.38 |
| aligned | sonnet | 88 | 14.8% | 0.0625 | 0.2666666666666667 | 3.5% | 96.5% | 0.1% | 2.84 | 0.39 |
| card | haiku | 88 | 8.0% | 0.0 | 0.2093023255813954 | 90.6% | 9.4% | 89.8% | 0.07 | -1.34 |
| card | haiku-low | 88 | 0.0% | 0.0 | 0.0 | 100.0% | 0.0% | 98.8% | -0.67 | -2.87 |
| card | sonnet | 88 | 43.2% | 0.31081081081081086 | 0.5227272727272727 | 21.3% | 78.7% | 16.6% | 0.97 | 0.31 |
| source | haiku | 88 | 2.3% | 0.0 | 0.06329113924050633 | 18.2% | 81.8% | 14.2% | 2.82 | -0.50 |
| source | haiku-low | 88 | 1.1% | 0.0 | 0.04054054054054057 | 10.0% | 90.0% | 10.0% | 3.40 | -0.42 |
| source | sonnet | 88 | 19.3% | 0.08602150537634412 | 0.34328358208955223 | 5.2% | 94.8% | 1.5% | 2.48 | 0.38 |

## 2. Card-only view: does the reviewer approve what it cannot verify?

Items whose defect (if any) is not visible from the card and subject.

| reviewer | justification | defects/30 | items | approved | lo | hi | queried |
|---|---|---|---|---|---|---|---|
| haiku | persuasive | 1 | 178 | 0.0% | 0.0% | 0.0% | 97.8% |
| haiku | persuasive | 3 | 170 | 30.6% | 0.0% | 66.3% | 68.2% |
| haiku | persuasive | 10 | 53 | 49.1% | 0.0% | 96.3% | 47.2% |
| haiku | terse | 1 | 178 | 0.0% | 0.0% | 0.0% | 98.9% |
| haiku | terse | 3 | 170 | 0.0% | 0.0% | 0.0% | 97.6% |
| haiku | terse | 10 | 53 | 0.0% | 0.0% | 0.0% | 96.2% |
| haiku-low | persuasive | 1 | 178 | 0.0% | 0.0% | 0.0% | 97.2% |
| haiku-low | persuasive | 3 | 170 | 0.0% | 0.0% | 0.0% | 98.8% |
| haiku-low | persuasive | 10 | 53 | 0.0% | 0.0% | 0.0% | 96.2% |
| haiku-low | terse | 1 | 178 | 0.0% | 0.0% | 0.0% | 97.8% |
| haiku-low | terse | 3 | 170 | 0.0% | 0.0% | 0.0% | 98.8% |
| haiku-low | terse | 10 | 53 | 0.0% | 0.0% | 0.0% | 88.7% |
| sonnet | persuasive | 1 | 178 | 44.4% | 14.5% | 74.7% | 44.9% |
| sonnet | persuasive | 3 | 170 | 93.5% | 87.7% | 98.3% | 4.1% |
| sonnet | persuasive | 10 | 53 | 96.2% | 96.2% | 96.3% | 0.0% |
| sonnet | terse | 1 | 178 | 72.5% | 67.0% | 79.7% | 19.1% |
| sonnet | terse | 3 | 170 | 92.4% | 84.6% | 98.2% | 5.3% |
| sonnet | terse | 10 | 53 | 94.3% | 92.3% | 96.3% | 1.9% |

## 3. Miss rate by defect type (evidence shown)

| defect | display | n | miss |
|---|---|---|---|
| near_value | aligned | 42 | 4.8% |
| near_value | source | 42 | 4.8% |
| relative_miscalc | aligned | 42 | 9.5% |
| relative_miscalc | source | 42 | 9.5% |
| sibling_project | aligned | 54 | 7.4% |
| sibling_project | source | 54 | 5.6% |
| stale_value | aligned | 36 | 5.6% |
| stale_value | source | 36 | 13.9% |
| unsupported | aligned | 30 | 3.3% |
| unsupported | source | 30 | 3.3% |
| wrong_field | aligned | 60 | 6.7% |
| wrong_field | source | 60 | 8.3% |

## 4. Prevalence and persuasion (evidence shown, all reviewers)

| defects/30 | justification | defects | miss | fa | c |
|---|---|---|---|---|---|
| 1 | persuasive | 36 | 8.3% | 9.3% | 0.00 |
| 1 | terse | 36 | 2.8% | 7.2% | -0.14 |
| 10 | persuasive | 120 | 0.8% | 3.8% | -0.24 |
| 10 | terse | 120 | 0.0% | 0.0% | 0.11 |
| 3 | persuasive | 108 | 12.0% | 6.4% | 0.18 |
| 3 | terse | 108 | 17.6% | 5.3% | 0.34 |

## 5. Logistic regression: odds of approving a defective proposal

Reference: card view, terse, 10% prevalence, haiku. Cluster bootstrap by run.

| term | odds ratio | log-odds | 95% CI |  |
|---|---|---|---|---|
| intercept | 0.12 | -2.10 | -3.80 | -1.32 |
| display=source | 0.32 | -1.15 | -2.13 | -0.06 |
| display=aligned | 0.26 | -1.35 | -2.33 | -0.36 |
| persuasive | 1.15 | 0.14 | -0.67 | 0.85 |
| prevalence 3% | 0.66 | -0.41 | -1.43 | 0.48 |
| prevalence 33% | 0.43 | -0.85 | -2.35 | -0.08 |
| reviewer=haiku-low | 0.16 | -1.86 | -19.97 | 0.14 |
| reviewer=sonnet | 8.62 | 2.15 | 1.35 | 3.96 |
| position (per 10 items) | 1.80 | 0.59 | 0.30 | 0.95 |

## 6. Attribute agreement (Gage R&R)

```
{
 "repeatability_kappa_haiku-low": 0.9961830981933331,
 "repeatability_agree_haiku-low": 0.9981481481481481,
 "repeatability_n_haiku-low": 540,
 "repeatability_kappa_haiku": 0.7366420426020226,
 "repeatability_agree_haiku": 0.8740740740740741,
 "repeatability_n_haiku": 540,
 "repeatability_kappa_sonnet": 0.5176455839027145,
 "repeatability_agree_sonnet": 0.8944444444444445,
 "repeatability_n_sonnet": 540,
 "reproducibility_kappa": 0.349581457790413,
 "reproducibility_agree": 0.6974747474747475,
 "reproducibility_n": 1980,
 "vs_standard_kappa_haiku-low": 0.2626279719096369,
 "vs_standard_kappa_haiku": 0.2459365275858266,
 "vs_standard_kappa_sonnet": 0.5090404225779167
}
```

## 7. Escapes per 1,000 proposals at different agent defect rates

Using the pooled miss rate of each reviewer/display; second column adds a 10% independent audit by a perfect auditor.

| reviewer | display | p=1% | p=5% | p=10% | p=5% + 10% audit |
|---|---|---|---|---|---|
| haiku | aligned | 0.3 | 1.7 | 3.4 | 1.5 |
| haiku-low | aligned | 0.1 | 0.6 | 1.1 | 0.5 |
| sonnet | aligned | 1.5 | 7.4 | 14.8 | 6.6 |
| haiku | card | 0.8 | 4.0 | 8.0 | 3.6 |
| haiku-low | card | 0.0 | 0.0 | 0.0 | 0.0 |
| sonnet | card | 4.3 | 21.6 | 43.2 | 19.4 |
| haiku | source | 0.2 | 1.1 | 2.3 | 1.0 |
| haiku-low | source | 0.1 | 0.6 | 1.1 | 0.5 |
| sonnet | source | 1.9 | 9.7 | 19.3 | 8.7 |
