---
title: Evidence-Grounded Financial RAG with a Local LLM
summary: A fully local retrieval-augmented QA system that answers financial questions with cited sources, uses a calculator for arithmetic, and refuses when evidence is missing.
headline: "94% correct with cited evidence"
tags: [RAG, LLMs, Information Retrieval]
featured: false
order: 6
thumb: /assets/img/projects/financial-rag/thumb.png
results:
  - value: "1.00"
    label: Recall@5 of required sources (hybrid retriever)
  - value: "94%"
    label: Correct answers; 92% with every source cited
  - value: "8 / 8"
    label: Unanswerable questions correctly refused
  - value: "0.83"
    label: Recall@5 on real FinQA report text
---

## Question

Can a small, locally run LLM answer numeric questions about company financials accurately, cite where each number came from, and say "I don't know" when the documents don't contain the answer?

## Data

The main evaluation uses a **synthetic** corpus of company reports for twelve fictional companies, with 36 development questions (8 deliberately unanswerable). A separate check runs on real annual-report passages from the public FinQA dataset.

## Method

- Chunking into 45-word windows with 10-word overlap (336 chunks), compared against section-level chunks.
- Retrieval: company/year metadata filter first, then TF-IDF (1–2 grams) and MiniLM sentence embeddings fused with reciprocal rank fusion (k = 60), top-5 unique documents.
- Generation: `qwen2.5:7b` (4-bit, via Ollama, temperature 0) prompted to give a formula, an answer and its sources. A Python calculator evaluates the written formula.
- Everything runs on a laptop. No hosted API is called.

## Findings

- With the metadata filter applied first, the hybrid retriever finds every required source in its top 5 (recall@5 = 1.00, recall@3 = 0.89).
- The system answers 34 of 36 development questions correctly (94%), 33 with every required source cited, and refuses all 8 unanswerable questions without refusing any answerable one.
- The LLM picks the right figures but is weak at arithmetic. The calculator fixes slips, but it can't fix a wrong formula, such as a ratio scaled by 10 or 100.
- On real FinQA text, recall@5 stays at 0.83 and 4 of 6 answers are correct. The single retrieval miss caused the only hallucination, which shows that grounding quality bounds answer quality.

<figure>
  <img src="{{ '/assets/img/projects/financial-rag/recall.png' | relative_url }}" alt="Recall at 3 and 5 for TF-IDF, semantic, hybrid and LSA retrieval with section and window chunking">
  <figcaption>Known-evidence recall@3 and recall@5 by retrieval method and chunking scheme.</figcaption>
</figure>
