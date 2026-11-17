# Study 2 results

336 reviewer runs, 0 without valid output, 10080 item decisions.
## 1. Detection by display and reviewer

miss = defective proposal approved; fa = good proposal not approved (rejected or queried).

| display | reviewer | defects | miss | 95% CI |  | false alarm | good approved | good queried | d' | c |
|---|---|---|---|---|---|---|---|---|---|---|
| aligned | haiku | 88 | 0.0% | 0.0 | 0.0 | 1.5% | 98.5% | 1.5% | 4.70 | -0.19 |
| aligned | haiku-low | 88 | 0.0% | 0.0 | 0.0 | 0.3% | 99.7% | 0.3% | 5.25 | 0.09 |
| aligned | opus | 88 | 0.0% | 0.0 | 0.0 | 4.1% | 95.9% | 4.1% | 4.27 | -0.40 |
| aligned | sonnet | 88 | 0.0% | 0.0 | 0.0 | 0.5% | 99.5% | 0.5% | 5.05 | -0.01 |
| card | haiku | 88 | 6.8% | 0.0 | 0.18478260869565222 | 91.1% | 8.9% | 89.5% | 0.11 | -1.40 |
| card | haiku-low | 88 | 1.1% | 0.0 | 0.03797468354430378 | 97.2% | 2.8% | 96.3% | 0.22 | -2.01 |
| card | opus | 88 | 6.8% | 0.011235955056179803 | 0.1428571428571429 | 80.9% | 19.1% | 78.6% | 0.58 | -1.16 |
| card | sonnet | 88 | 34.1% | 0.21794871794871795 | 0.43137254901960786 | 24.2% | 75.8% | 19.0% | 1.10 | 0.15 |
| source | haiku | 88 | 0.0% | 0.0 | 0.0 | 13.6% | 86.4% | 12.0% | 3.63 | -0.72 |
| source | haiku-low | 88 | 0.0% | 0.0 | 0.0 | 20.1% | 79.9% | 20.1% | 3.37 | -0.85 |
| source | opus | 88 | 0.0% | 0.0 | 0.0 | 9.3% | 90.7% | 9.3% | 3.85 | -0.61 |
| source | sonnet | 88 | 0.0% | 0.0 | 0.0 | 1.5% | 98.5% | 0.3% | 4.70 | -0.19 |

## 2. Card-only view: does the reviewer approve what it cannot verify?

Items whose defect (if any) is not visible from the card and subject.

| reviewer | justification | defects/30 | items | approved | lo | hi | queried |
|---|---|---|---|---|---|---|---|
| haiku | persuasive | 1 | 178 | 0.0% | 0.0% | 0.0% | 97.8% |
| haiku | persuasive | 3 | 170 | 0.0% | 0.0% | 0.0% | 98.8% |
| haiku | persuasive | 10 | 53 | 0.0% | 0.0% | 0.0% | 96.2% |
| haiku | terse | 1 | 178 | 0.0% | 0.0% | 0.0% | 94.4% |
| haiku | terse | 3 | 170 | 28.8% | 0.0% | 61.5% | 70.0% |
| haiku | terse | 10 | 53 | 45.3% | 0.0% | 88.9% | 49.1% |
| haiku-low | persuasive | 1 | 178 | 0.0% | 0.0% | 0.0% | 98.3% |
| haiku-low | persuasive | 3 | 170 | 0.0% | 0.0% | 0.0% | 98.8% |
| haiku-low | persuasive | 10 | 53 | 0.0% | 0.0% | 0.0% | 96.2% |
| haiku-low | terse | 1 | 178 | 0.0% | 0.0% | 0.0% | 96.6% |
| haiku-low | terse | 3 | 170 | 12.9% | 0.0% | 39.3% | 85.9% |
| haiku-low | terse | 10 | 53 | 0.0% | 0.0% | 0.0% | 96.2% |
| opus | persuasive | 1 | 178 | 11.8% | 0.0% | 35.2% | 83.7% |
| opus | persuasive | 3 | 170 | 31.8% | 0.0% | 66.3% | 67.1% |
| opus | persuasive | 10 | 53 | 0.0% | 0.0% | 0.0% | 94.3% |
| opus | terse | 1 | 178 | 15.7% | 0.0% | 47.7% | 78.1% |
| opus | terse | 3 | 170 | 15.9% | 0.0% | 48.2% | 82.9% |
| opus | terse | 10 | 53 | 37.7% | 0.0% | 76.9% | 56.6% |
| sonnet | persuasive | 1 | 178 | 43.3% | 13.4% | 75.6% | 48.3% |
| sonnet | persuasive | 3 | 170 | 77.1% | 45.0% | 94.7% | 21.8% |
| sonnet | persuasive | 10 | 53 | 92.5% | 88.5% | 96.3% | 3.8% |
| sonnet | terse | 1 | 178 | 76.4% | 68.3% | 84.7% | 9.0% |
| sonnet | terse | 3 | 170 | 93.5% | 87.0% | 98.2% | 3.5% |
| sonnet | terse | 10 | 53 | 90.6% | 88.5% | 92.6% | 3.8% |

## 3. Miss rate by defect type (evidence shown)

| defect | display | n | miss |
|---|---|---|---|
| near_value | aligned | 56 | 0.0% |
| near_value | source | 56 | 0.0% |
| relative_miscalc | aligned | 56 | 0.0% |
| relative_miscalc | source | 56 | 0.0% |
| sibling_project | aligned | 72 | 0.0% |
| sibling_project | source | 72 | 0.0% |
| stale_value | aligned | 48 | 0.0% |
| stale_value | source | 48 | 0.0% |
| unsupported | aligned | 40 | 0.0% |
| unsupported | source | 40 | 0.0% |
| wrong_field | aligned | 80 | 0.0% |
| wrong_field | source | 80 | 0.0% |

## 4. Prevalence and persuasion (evidence shown, all reviewers)

| defects/30 | justification | defects | miss | fa | c |
|---|---|---|---|---|---|
| 1 | persuasive | 48 | 0.0% | 7.3% | -0.43 |
| 1 | terse | 48 | 0.0% | 10.1% | -0.52 |
| 10 | persuasive | 160 | 0.0% | 4.1% | -0.50 |
| 10 | terse | 160 | 0.0% | 1.9% | -0.34 |
| 3 | persuasive | 144 | 0.0% | 5.2% | -0.54 |
| 3 | terse | 144 | 0.0% | 4.1% | -0.48 |

## 5. Logistic regression: odds of approving a defective proposal

Reference: card view, terse, 10% prevalence, haiku. Cluster bootstrap by run.

| term | odds ratio | log-odds | 95% CI |  |
|---|---|---|---|---|
| intercept | 0.05 | -2.93 | -4.49 | -2.04 |
| display=source | 0.00 | -21.21 | -21.94 | -20.26 |
| display=aligned | 0.00 | -21.21 | -21.94 | -20.31 |
| persuasive | 0.46 | -0.77 | -2.04 | 0.07 |
| prevalence 3% | 0.96 | -0.04 | -18.29 | 1.23 |
| prevalence 33% | 2.83 | 1.04 | 0.01 | 1.99 |
| reviewer=haiku-low | 0.15 | -1.90 | -19.57 | 0.32 |
| reviewer=sonnet | 8.64 | 2.16 | 1.28 | 3.58 |
| position (per 10 items) | 1.85 | 0.61 | 0.04 | 1.13 |

## 6. Attribute agreement (Gage R&R)

```
{
 "repeatability_kappa_haiku-low": 0.8044023404848146,
 "repeatability_agree_haiku-low": 0.9037037037037037,
 "repeatability_n_haiku-low": 540,
 "repeatability_kappa_haiku": 0.7095761381475667,
 "repeatability_agree_haiku": 0.8629629629629629,
 "repeatability_n_haiku": 540,
 "repeatability_kappa_sonnet": 0.7254503195816389,
 "repeatability_agree_sonnet": 0.9351851851851852,
 "repeatability_n_sonnet": 540,
 "repeatability_kappa_opus": 0.5767769940314705,
 "repeatability_agree_opus": 0.8074074074074075,
 "repeatability_n_opus": 540,
 "reproducibility_kappa_haiku-low_vs_haiku": 0.9233920059429233,
 "reproducibility_kappa_haiku-low_vs_sonnet": 0.4213616732178387,
 "reproducibility_kappa_haiku-low_vs_opus": 0.7488524419722923,
 "reproducibility_kappa_haiku_vs_sonnet": 0.4492744933445257,
 "reproducibility_kappa_haiku_vs_opus": 0.7412185853156691,
 "reproducibility_kappa_sonnet_vs_opus": 0.3825546164885983,
 "vs_standard_kappa_haiku-low": 0.2440266512638198,
 "vs_standard_kappa_haiku": 0.2682546286665281,
 "vs_standard_kappa_sonnet": 0.6246042870867655,
 "vs_standard_kappa_opus": 0.3047387966401494
}
```

## 7. Escapes per 1,000 proposals at different agent defect rates

Using the pooled miss rate of each reviewer/display; second column adds a 10% independent audit by a perfect auditor.

| reviewer | display | p=1% | p=5% | p=10% | p=5% + 10% audit |
|---|---|---|---|---|---|
| haiku | aligned | 0.0 | 0.0 | 0.0 | 0.0 |
| haiku-low | aligned | 0.0 | 0.0 | 0.0 | 0.0 |
| opus | aligned | 0.0 | 0.0 | 0.0 | 0.0 |
| sonnet | aligned | 0.0 | 0.0 | 0.0 | 0.0 |
| haiku | card | 0.7 | 3.4 | 6.8 | 3.1 |
| haiku-low | card | 0.1 | 0.6 | 1.1 | 0.5 |
| opus | card | 0.7 | 3.4 | 6.8 | 3.1 |
| sonnet | card | 3.4 | 17.0 | 34.1 | 15.3 |
| haiku | source | 0.0 | 0.0 | 0.0 | 0.0 |
| haiku-low | source | 0.0 | 0.0 | 0.0 | 0.0 |
| opus | source | 0.0 | 0.0 | 0.0 | 0.0 |
| sonnet | source | 0.0 | 0.0 | 0.0 | 0.0 |
