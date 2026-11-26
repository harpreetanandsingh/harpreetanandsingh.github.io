---
layout: page
title: Research
permalink: /research/
intro: NLP and LLM research on long financial documents and low-resource machine translation.
---

## Publications

{% for pub in site.data.publications %}{% include publication.html pub=pub %}
{% endfor %}

## Research experience

### Georgia Tech Financial Services Innovation Lab · May 2024 – Apr 2025
Built a long-context benchmark of 20,139 QA pairs from 170 SEC credit agreements using RDF knowledge graphs and SPARQL, and evaluated 16 LLMs on it. This work became the ACL 2026 paper. [Project details →]({{ '/projects/kg-qa/' | relative_url }})

### Machine translation for Indic languages, BITS Pilani · 2023 – 2024
Fine-tuned NLLB and related multilingual models for low-resource pairs (Odia–Hindi in governance and healthcare; Bhojpuri–Hindi and Marathi–Hindi speech translation), leading to the FIRE 2023 and IWSLT 2024 papers. [Code](https://github.com/harpreetanandsingh/MTIL_FIRE_BITSP)

### North Eastern Space Applications Centre · May 2023 – Jul 2023
Multi-class semantic segmentation of UAV and Sentinel-2 imagery with zero-shot learning, using Meta's Segment Anything Model and merging per-class masks into one segmented map. [Code](https://github.com/harpreetanandsingh/NESAC_Project)
