---
title: SEC 10-K Filings Analyzer
summary: Pulls key sections from a company's 10-K filing, classifies each sentence as bullish or bearish, and summarizes both sides.
headline: "RoBERTa + T5 on SEC filings"
tags: [Financial NLP, Transformers, Sentiment]
featured: false
order: 7
tile: { value: "RoBERTa + T5", label: "sentence sentiment · section summaries" }
repo: https://github.com/harpreetanandsingh/10K-Analyser
results:
  - value: "RoBERTa"
    label: Financial-sentiment classifier, per sentence
  - value: "T5-base"
    label: Summarizer for bullish and bearish content
  - value: "Per section"
    label: Analysis by 10-K section
---

## Question

Can an investor get a quick, balanced read of a long 10-K filing: what sounds positive, what sounds negative, and why?

## Data

Company 10-K filings from SEC EDGAR, split into their standard sections.

## Method

- Extracted text section by section from each filing.
- Classified every sentence as bullish or bearish with a RoBERTa model fine-tuned for financial sentiment.
- Summarized the bullish and bearish sentences separately with T5-base, giving a short two-sided view of each section.

## Findings

- For each section of a filing, the tool outputs the bullish and bearish sentences and a short summary of each side.
- This gives a two-sided reading of a long filing without reading it end to end.
