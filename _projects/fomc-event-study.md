---
title: Market Reaction to Monetary Policy Surprises
summary: An event study of how stocks react to the current-policy and forward-guidance parts of FOMC surprises, 1995–2022.
headline: "221 FOMC announcements"
tags: [Event Study, Monetary Policy, Empirical Finance]
featured: false
order: 4
thumb: /assets/img/projects/fomc-event-study/thumb.png
repo: https://github.com/harpreetanandsingh/fomc-policy-surprise-event-study
results:
  - value: "221"
    label: FOMC announcements, 1995–2022
  - value: "Day 0"
    label: Reaction concentrated on announcement day
  - value: "≈ −0.0008"
    label: CAR effect per unit surprise, stable across beta specs
  - value: "1.16 → 0.56"
    label: Drop in target-surprise s.d. at the zero lower bound
---

## Question

How do stocks react to monetary policy surprises, and do the *target* (current rate) and *path* (forward guidance) components of a surprise behave differently?

## Data

Target and path surprise series from Acosta (2022) for 221 FOMC announcements (1995–2022), matched to daily stock returns, the market index and firm size and industry.

## Method

- Raw-return regressions of daily returns on target and path surprises the day before, the day of, and the day after each announcement, for the aggregate market, individual firms and size-sorted portfolios.
- Cumulative abnormal returns (CARs) from a market model, with beta estimated two ways: full-sample per firm and a rolling 252-day window before each event.
- Cross-sectional tests: size, industry and beta interactions with each surprise component.

## Findings

- At the zero lower bound the target surprise's volatility falls by more than half (s.d. 1.16 → 0.56) while path barely changes (1.10 → 0.77). With rates pinned at zero, the Fed relies on forward guidance.
- The reaction is fast. Nothing shows up the day before, there's a significant reaction on the day, and only weak continuation the day after. Hawkish surprises of both kinds push returns down.
- Effects on CARs are nearly identical under both beta specifications (≈ −0.0007 to −0.0009), so the result isn't an artifact of how expected returns were estimated.
- Two surprises: Construction and Mining react most, while Finance is only middling (likely diversification inside a broad group), and higher-beta firms are *less* sensitive to hawkish path surprises.

<figure>
  <img src="{{ '/assets/img/projects/fomc-event-study/surprises.png' | relative_url }}" alt="Time series of target and path monetary policy surprises with zero-lower-bound periods shaded">
  <figcaption>Target and path surprises across FOMC announcements; grey marks the zero lower bound.</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/img/projects/fomc-event-study/coef-by-day.png' | relative_url }}" alt="Aggregate market-return sensitivity to target and path surprises the day before, of, and after announcements">
  <figcaption>Aggregate market-return sensitivity by event day, with 95% confidence intervals.</figcaption>
</figure>
