---
name: regulation-diff-watch
mode: scheduled
category: governance
summary: A weekly check of named regulator and standards pages for changes, quoted and linked, with no interpretation.
use_when: Use when a small set of official sources governs your work and you need the change before the newsletter tells you.
inputs:
  - The named list of official pages to watch
writes: none
outputs: Changed pages with quoted before and after where available, a No change list, and a Could not check list.
---

# Regulation diff watch

## Prompt

```text
Check the official pages below for changes since this task last ran.
Read only.

Pages:
  NAME, URL.
  NAME, URL.

Only these pages. Do not substitute a law firm summary, a news article
or a vendor blog for a source you could not reach. If a page failed, it
belongs in Could not check.

For each page that changed.

What changed, quoted. Give the new text, and the old text where the
page or its own version history shows it. If you have the new
text only, say so plainly rather than describing a difference you did
not see.
The link, as specific as the site allows.
The date the page states. If the page states none, write NO DATE ON
PAGE.
Whether the change carries a date on which it takes effect, quoted.

Then two lists.

No change. Pages read and unchanged, with the date you read them.
Could not check. Pages that failed, timed out, need a login, or now
redirect elsewhere. Include the status you got.

Rules. Quote, do not paraphrase. Do not say what a change means for us,
whether it applies to us, or what we should do. Those are for a
qualified human.
```

## Before you run it

- Keep the list to official sources you can name. The value of this watch is that everything in it is quoted from the page that governs, not from someone's reading of it.
- The Could not check list matters most here. A regulator page that quietly moved looks identical to a regulator page that did not change.

## What you get

A weekly note where every entry is a quotation with a link and a date, and where the pages you failed to read are listed rather than assumed quiet.

## Boundaries

It does not interpret a rule, decide whether it applies to you, assess compliance or give legal advice. The watch is a draft evidence list, and a qualified human decides what any of it means.
