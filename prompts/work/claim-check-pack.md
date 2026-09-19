---
name: claim-check-pack
mode: work
category: research
summary: Check the factual claims in a piece of writing one by one and return supported, contradicted, mixed or not found with sources.
use_when: Use when something is about to be published or sent and you need each factual claim checked against a source rather than read for tone.
inputs:
  - The draft text, document or post
  - Web search
writes: none
outputs: One row per claim with a verdict, the source URL, the date on that page, and a separate list of claims that cannot be checked.
---

# Claim check pack

## Prompt

```text
Check the factual claims in the text I am giving you.

First, list the claims. A claim is a statement that could be shown
false: a number, a date, a version, a price, an attribution, a
statement about what a product or an organisation does. Opinions,
predictions and recommendations are not claims, and you list those
separately under Not checkable so I can see you saw them.

Then, one row per claim:

  Claim. Quoted from my text.
  Verdict. SUPPORTED, CONTRADICTED, MIXED or NOT FOUND.
  Source. The URL you opened, and the date printed on that page. NO
  DATE if the page shows none.
  What the source actually says. A short quote, not a paraphrase.
  Distance. If the source supports something narrower or broader than
  my claim, say exactly how it differs. This is where most bad claims
  are, not in the ones that are flatly wrong.

Then two sections.

Not checkable. Opinions, predictions, and claims about private or
internal facts no public source can settle.

What I would need. For each NOT FOUND, the specific source that would
settle it.

Rules. One source is not a check for a contested claim, so say when a
verdict rests on a single page. Never mark SUPPORTED from memory. You
cannot verify how current a page is beyond the date it prints, so do
not write that something is the latest or still true today.
```

## Before you run it

- Paste the whole piece, not the claims you already doubt. The claims you did not doubt are the ones worth the run.
- Expect the Distance column to be the useful one. Most claims that fail do so by being slightly wider than their source.

## What you get

A checkable row per claim, a list of what no source can settle, and a short list of exactly which sources you would need to close the gaps.

## Boundaries

It does not rewrite your text and it does not decide whether to publish. A SUPPORTED verdict is a statement about one page on one day, and the output is a draft that a human reads before anything ships.
