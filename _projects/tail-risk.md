---
title: Extreme Equity Returns, Tail Risk & Market Regimes
summary: Defining, clustering and predicting extreme stock moves in a 240-firm panel built to match the statistical features of US equity returns.
headline: "2.6× jump rate in recessions"
tags: [Tail Risk, Extreme Value Theory, Anomaly Detection]
featured: true
order: 2
thumb: /assets/img/projects/tail-risk/thumb.png
repo: https://github.com/harpreetanandsingh/equity-tail-risk-regimes
results:
  - value: "77K+"
    label: Firm-months, 240 anonymized firms (simulated panel)
  - value: "ξ = 0.14"
    label: GPD tail shape; excess kurtosis 6.5
  - value: "2.6×"
    label: Extreme-event frequency in recessions
  - value: "0.66"
    label: Best next-month jump ROC-AUC (out of sample)
---

## Question

On a panel built to behave like monthly US equity returns: how heavy are the tails, what should count as an "extreme" move, and can extreme moves be detected in the same month or predicted a month ahead?

## Data

An anonymized panel of 240 firms and 77,520 firm-months (1997–2023), **simulated to reproduce the statistical features of US equity returns** (heavy tails, volatility clustering, stress-period clustering and cross-sectional differences) rather than raw CRSP data. It comes with matching market and macro regime proxies, including stress windows modelled on the dot-com bust, 2008, COVID and 2022. The data were split in time into training, validation and a 2019–2023 test period. Because the panel is simulated, the findings below describe the methods' behaviour on realistic data, not new facts about the US market.

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
- In the COVID-style stress window, extreme moves were a synchronized downside crash (8 negative jumps per positive one), and every backward-looking forecast ranked those months the wrong way. That is a useful stress test for any jump model.

<figure>
  <img src="{{ '/assets/img/projects/tail-risk/tails.png' | relative_url }}" alt="Return distribution tails compared with a Normal distribution and the fitted GPD">
  <figcaption>Empirical tails vs. Normal and the fitted Generalized Pareto Distribution.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/projects/tail-risk/clustering.png' | relative_url }}" alt="Autocorrelation of the monthly jump fraction, next-month jump rate by intensity quintile, and test gain curves">
  <figcaption>Clustering of extreme events and next-month prediction.</figcaption>
</figure>
