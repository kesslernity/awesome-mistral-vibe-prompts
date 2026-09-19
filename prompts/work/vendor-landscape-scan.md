---
name: vendor-landscape-scan
mode: work
category: research
summary: Scan a vendor category against criteria you set, with every claim quoted from a dated page and the gaps named.
use_when: Use when you need a first pass at who is in a market and what they claim, before anyone books a demo.
inputs:
  - Web search
  - Any vendor documents or pricing pages you already hold
writes: none
outputs: A vendor by criterion table where every cell carries a quote, a URL and a page date, plus Could not establish and Contradictions.
builtin_overlap: deep-research
---

# Vendor landscape scan

## Prompt

```text
Scan the market for CATEGORY, for a buyer who is SHORT CONTEXT: size,
sector, constraint that matters.

My criteria, in priority order: CRITERION, CRITERION, CRITERION.

Return a table, one row per vendor, one column per criterion. In every
cell, put the claim, a short quote, the URL you took it from, and the
date printed on that page. Where a page carries no date, write NO DATE
rather than guessing from the content. Where you cannot find a vendor's
position on a criterion, write NOT FOUND. Never fill a cell from
general knowledge.

Then three sections.

Contradictions. Places where a vendor's own pages disagree, or where a
vendor and a third party state different things. Show both, with both
URLs.

Could not establish. Criteria where the public material does not answer
the question for anybody, and what you would have to ask a vendor
instead.

Recency limit. State plainly that you cannot verify how current any of
this is beyond the dates printed on the pages, and name the oldest date
in the table.

Rules. No URL you did not open. No pricing figure without a page that
shows it. Do not rank the vendors and do not recommend one.
```

## Before you run it

- Vibe Work ships a built-in `deep-research` skill, and in Chat the Deep Research feature now redirects to Work. If you want breadth, start with `/deep-research`; use this prompt when you want a fixed table with a source in every cell.
- Write the criteria before you run it. Criteria invented after seeing the vendors are criteria fitted to the vendors.

## What you get

A comparison table where every cell can be clicked back to its source, and two sections telling you what the public web cannot answer, which is the list you take into a vendor call.

## Boundaries

It does not rank, score or recommend, and a vendor's claim quoted accurately is still a vendor's claim. Nothing here is a procurement decision or a security assessment. Treat the table as a draft that a human checks before it reaches a shortlist.
