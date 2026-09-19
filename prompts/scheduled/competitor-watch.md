---
name: competitor-watch
mode: scheduled
category: research
summary: A weekly read on a named list of competitors, restricted to what changed on their own public pages.
use_when: Use when you want a steady signal on a handful of competitors without a daily feed of commentary.
inputs:
  - The named list of competitors and the pages that matter
writes: none
outputs: One line per competitor with what changed and the link, a No change list, and a Could not check list.
---

# Competitor watch

## Prompt

```text
Check the competitors below for changes since this task last ran. Read
only, and change nothing anywhere. Use their own pages first: pricing,
product, changelog, careers, status.

Competitors and pages:
  NAME, URLS.
  NAME, URLS.

For each one that changed, one entry.

What changed, in one sentence, with the before and the after where the
page shows both.
Where you saw it, as a link.
When, as the page states it. If the page carries no date, write NO DATE
ON PAGE rather than guessing from the wording.
Confidence. HIGH if you read it on their own page. MEDIUM if a
publication reported it and named a source. LOW if it is commentary.
Anything below HIGH says who reported it.

Then two lists that matter as much as the first.

No change. Competitors whose pages you read and found unchanged.
Could not check. Pages that failed, timed out, need a login or hid
behind a consent wall. Never let a page you could not read fall into No
change.

Rules. No analysis of what it means for us. No recommendation. Pricing
carries its currency, unit and plan exactly as written.
```

## Before you run it

- Name the pages, not just the companies. A watch built on search results drifts into commentary within a month.
- Weekly is usually right. Daily produces mostly Could not check noise.

## What you get

A short weekly read where every claim is traceable to a page you can open, and where the pages that failed to load are visible rather than silently counted as quiet.

## Boundaries

It does not interpret a competitor's move, recommend a response or rank anyone. The watch is a draft evidence list, and no entry below HIGH confidence belongs in anything you circulate.
