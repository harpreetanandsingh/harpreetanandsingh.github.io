---
title: Forecasting Market Betas with Neural Networks
summary: A neural network that forecasts each stock's next-year market beta from historical risk, return and size signals, tested out of sample on 2018–2022.
headline: "−30% MSE vs. trailing daily beta"
tags: [Asset Pricing, Deep Learning, Forecasting]
featured: true
order: 1
thumb: /assets/img/projects/neural-beta/thumb.png
repo: https://github.com/harpreetanandsingh/neural-beta-forecasting
results:
  - value: "−30%"
    label: MSE vs. trailing daily beta (Newey–West t = 9.4)
  - value: "0.76"
    label: Out-of-sample R² vs. 36-month rolling beta
  - value: "0.63 → 1.53"
    label: Realized beta, lowest to highest forecast quintile
  - value: "9 / 10"
    label: Industry betas where one multi-output net beats separate nets
---

## Question

Can a stock's future market beta be forecast better than by the usual rolling-window estimates? Beta drives cost-of-capital estimates, hedging and risk models, but historical betas are noisy and too extreme.

## Data

CRSP stocks, 1996–2023. At the end of each month, the target is the daily-return beta over the next 12 months. Predictors are twelve historical risk, return and size variables plus the firm's industry. Training, validation and test periods are strictly separated in time; the test period (2018–2022) was never used for training or model selection.

## Method

- Benchmarks: rolling 12-, 24- and 36-month monthly betas, the trailing 12-month daily beta, and a constant beta of 1.
- Model: a small feed-forward network (MLP) with early stopping, compared against a linear regression on the same inputs to isolate the non-linear gain.
- Evaluation: test RMSE, out-of-sample R², Newey–West t-statistics on monthly loss differences, bias by firm size, and quintile sorts on the forecast.
- Extension: one network with ten outputs (industry betas) against ten separate networks, across three random seeds.

## Findings

- The network beats every benchmark. Against the most demanding one, the trailing daily beta, it lowers MSE by 30% (RMSE 0.443 vs 0.530) and its monthly error is lower in every one of the 60 test months.
- Most of the gain comes from **shrinkage**: one unit of historical daily beta is followed by only 0.51 units of realized beta. Firm size and idiosyncratic volatility decide how far each estimate is pulled toward the mean. A linear model recovers most of the gain; the non-linear part adds a smaller but reliable improvement (t = 3.9), mainly among the largest firms.
- Sorting stocks on the forecast separates future risk cleanly (realized beta 0.63 → 1.53, monotone in all 60 test months) but not returns: the high-minus-low return is −0.48% per month (t = −1.1), a flat security market line.
- Limits: the model ranks firms well within a month but doesn't time market-wide beta swings (e.g. around COVID), and it under-predicts the smallest firms.

<figure>
  <img src="{{ '/assets/img/projects/neural-beta/quintiles.png' | relative_url }}" alt="Realized beta, next-month return and the empirical security market line by forecast quintile in the test period">
  <figcaption>Realized beta, next-month return and the empirical security market line by forecast quintile, 2018–2022 test period.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/projects/neural-beta/test-error.png' | relative_url }}" alt="Average beta and cross-sectional RMSE by forecast month for the network and benchmarks">
  <figcaption>Average beta and cross-sectional RMSE by forecast month: network vs. rolling-beta benchmarks.</figcaption>
</figure>
