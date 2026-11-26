---
title: Corporate Default & Distress Prediction
summary: Predicting next-year corporate default from firm fundamentals and market signals, with calibrated probabilities of default.
headline: "Top decile captures 39% of defaults"
tags: [Credit Risk, Classification, Calibration]
featured: true
order: 3
thumb: /assets/img/projects/default-prediction/thumb.png
repo: https://github.com/harpreetanandsingh/corporate-default-prediction
results:
  - value: "0.740"
    label: Test ROC-AUC (LASSO logit), KS 0.404
  - value: "38.7%"
    label: Defaults captured in riskiest 10% of firms
  - value: "0.77%"
    label: Base default rate, 78,682 firm-years (simulated panel)
  - value: "6"
    label: Models compared, from logit to gradient boosting
---

## Question

Which firms will default next year, and how well can firm ratios and market signals rank and price that risk when defaults are rare?

## Data

An anonymized panel of 8,262 firms and 78,682 firm-years, **simulated to reproduce the structure of a corporate-bankruptcy prediction problem** (ratios, market signals, rare defaults and stress years) rather than raw Compustat or CRSP data. It contains 609 next-year defaults (0.77%). The data were split in time: training on fiscal 1999–2011, model choices on 2012–2014 validation, and a single final evaluation on 2015–2018 (12,282 firm-years, 119 defaults).

## Method

- Models: logit, LASSO and Ridge logits, a decision tree, a random forest and gradient boosting, with hyperparameters chosen on validation only.
- Class imbalance: compared weighting and resampling strategies; cutoffs chosen to maximize validation F1.
- Metrics: ROC-AUC, PR-AUC, KS statistic, decile capture, and calibration of predicted PDs.
- Calibration: Platt scaling on validation, because raw predicted PDs were too low.

## Findings

- Regularized logits ranked firms best on validation and test: LASSO reaches test ROC-AUC 0.740 and KS 0.404, and puts 38.7% of all defaults in the riskiest 10% of firms. The random forest is close (0.736); a single tree is clearly weakest.
- Gradient boosting had the best validation PR-AUC but fell back on test, which shows how noisy model rankings are with only 87 validation defaults.
- Leverage, retained earnings and the prior-year stock return drive predictions in both linear and tree models.
- Raw PDs under-predict defaults (about 0.57% vs a realized 0.97%), so calibration is needed before using them. Recommendation: LASSO logit with Platt calibration, with the random forest as a challenger.

<figure>
  <img src="{{ '/assets/img/projects/default-prediction/roc-pr.png' | relative_url }}" alt="ROC and precision-recall curves for all models on the test sample">
  <figcaption>Test-sample ROC and precision–recall curves.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/projects/default-prediction/calibration.png' | relative_url }}" alt="Calibration of LASSO predicted default probabilities: raw, isotonic and Platt">
  <figcaption>Reliability of LASSO PDs: raw vs. isotonic and Platt calibration.</figcaption>
</figure>
