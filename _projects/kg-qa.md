---
title: Knowledge-Graph QA on Financial Documents
summary: A benchmark of 20,139 question–answer pairs built from SEC credit agreements with knowledge graphs, used to test how well LLMs handle long financial documents.
headline: "ACL 2026 main conference"
tags: [LLM Evaluation, Knowledge Graphs, Financial NLP]
featured: true
order: 5
tile: { value: "20,139", label: "QA pairs · 170 SEC credit agreements" }
paper: https://aclanthology.org/2026.acl-long.151/
results:
  - value: "20,139"
    label: QA pairs across 170 SEC credit agreements
  - value: "14.2M+"
    label: Tokens of long-context financial text
  - value: "16"
    label: LLMs benchmarked
  - value: "κ = 80.76%"
    label: Inter-annotator agreement
---

## Question

Can LLMs answer multi-step questions over very long financial contracts, and where do they break down as questions get harder?

## Data

170 SEC credit agreements (14.2M+ tokens). Annotators labelled economic entities and relations over multiple stages; agreement reached Cohen's κ = 80.76%.

## Method

- Built RDF knowledge graphs from the annotations and generated questions at increasing levels of complexity with SPARQL, giving 20,139 QA pairs with verified answers.
- Benchmarked 16 LLMs, including GPT-4o, Gemini, DeepSeek-V3, Qwen2 and Llama 3.1, under full-document, standard RAG and oracle-retrieval settings.
- Scored with F1, edit distance, cosine similarity and LLM-as-a-judge, and validated the automatic metrics against 100 human ratings (Pearson, Kendall's τ).

Research at the Georgia Tech Financial Services Innovation Lab, May 2024 – Apr 2025, published as *KG-MuLQA* at ACL 2026 (main conference). An earlier version appeared on arXiv as KG-QAGen (2505.12495).

## Findings

- Performance falls sharply with complexity: "Not Found" answers rise from 15.0% to 77.4% as questions need more hops and conditions.
- Standard RAG does substantially worse than full-document and oracle retrieval, so retrieval is a key bottleneck for long contracts.
- The automatic metrics, including LLM-as-a-judge, were validated against 100 human evaluations with Pearson correlation and Kendall's τ.
