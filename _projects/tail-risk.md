---
title: Extreme Equity Returns, Tail Risk & Market Regimes
summary: How often stocks make extreme moves, how those moves cluster across firms and regimes, and whether they can be detected or predicted.
headline: "2.6× jump rate in recessions"
tags: [Tail Risk, Extreme Value Theory, Anomaly Detection]
featured: true
order: 2
thumb: /assets/img/projects/tail-risk/thumb.png
results:
  - value: "77K+"
    label: Firm-months across 240 firms
  - value: "ξ = 0.14"
    label: GPD tail shape; excess kurtosis 6.5
  - value: "2.6×"
    label: Extreme-event frequency in recessions
  - value: "0.66"
    label: Best next-month jump ROC-AUC (out of sample)
---

## Question

How heavy are the tails of monthly equity returns, what counts as an "extreme" move, and can extreme moves be detected in the same month or predicted a month ahead?

## Data

Monthly returns for 240 firms (77K+ firm-months) with market returns and macro regime labels. Data were split in time into training, validation and a 2019–2023 test period that includes COVID and the 2022 rate shock.

## Method

- Tail modelling: kurtosis, Normal comparison, and a Generalized Pareto Distribution fitted above the training 95th percentile (Extreme Value Theory).
- Four definitions of an extreme event: fixed ±10%, firm-relative 95th percentile, volatility-scaled 3σ and market-adjusted. Each was compared across industries and stress periods.
- Clustering: jump rates by regime, persistence after a jump, and cross-firm synchronization.
- Detection and prediction: Isolation Forest, a logistic model on event-intensity signals, and their combination, scored by ROC-AUC and top-decile capture.

## Findings

- Returns are strongly heavy-tailed: excess kurtosis 6.5, a 30% move is 18× more likely than under a Normal, and the GPD shape is ξ = 0.14.
- The definition matters: the fixed 10% rule mostly flags volatile industries and market-wide months. Firm-relative and volatility-scaled rules give similar rates across industries.
- Extreme events cluster: 2.6× the normal rate in recessions, 1.4× more likely after a firm's own jump, and the market-wide jump fraction stays autocorrelated for six months.
- Isolation Forest is an excellent *same-month* detector (ROC-AUC 0.93) but the weakest *next-month* forecaster (0.58). The best forward model, a small logistic regression, reaches 0.66 and captures 19% of next-month jumps in its top decile.
- COVID was a synchronized downside crash (8 negative jumps per positive one) in which every backward-looking forecast ranked months the wrong way.

<figure>
  <img src="{{ '/assets/img/projects/tail-risk/tails.png' | relative_url }}" alt="Return distribution tails compared with a Normal distribution and the fitted GPD">
  <figcaption>Empirical tails vs. Normal and the fitted Generalized Pareto Distribution.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/projects/tail-risk/clustering.png' | relative_url }}" alt="Autocorrelation of the monthly jump fraction, next-month jump rate by intensity quintile, and test gain curves">
  <figcaption>Clustering of extreme events and next-month prediction.</figcaption>
</figure>
