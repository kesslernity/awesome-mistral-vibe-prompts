---
name: regulation-change-watch
mode: work
category: research
summary: Establish what a named regulation currently says on the points you care about, with the official text quoted and dated.
use_when: Use when you need the current state of a specific regulation on specific questions, and secondhand summaries are not good enough.
inputs:
  - Web search, pointed at the official publisher
  - Any internal note stating what you currently believe
writes: none
outputs: A question by question table quoting the official text with its identifier and date, plus Amended, Disputed and Not established.
---

# Regulation change watch

## Prompt

```text
Establish what REGULATION NAME currently says on these questions:
QUESTION, QUESTION, QUESTION.

Use the official publisher first: the legislature, the regulator, or
the official journal. Secondary sources are allowed only to find the
official text, and never as the source of a statement.

One row per question:

  Question. As I wrote it.
  Answer. What the official text says, quoted, with the article or
  section number.
  Instrument. The full identifier of the document you quoted, with its
  publication date.
  Status. In force, in force from a stated date, adopted and not yet in
  force, or proposed. Take this from the document, not from a summary.

Then three sections.

Amended. Where the article you quoted has been changed, replaced or
repealed by a later instrument, with that instrument's identifier and
date. An article quoted without checking for an amendment is the most
common way this goes wrong.

Disputed or unclear. Where official sources or official guidance point
different ways. Show both.

Not established. Questions the official text does not answer, and what
you would have to read or ask instead.

Rules. Quote, do not paraphrase. Every quote carries its instrument
identifier and date. Say clearly that you cannot verify anything
published after the pages you opened. Do not tell me what we should do.
```

## Before you run it

- Paste what you currently believe to be true, as a separate block, and ask for it to be checked against what is found. A belief you have carried for a year is the thing this run is for.
- Name the jurisdiction. The same regulation name often exists in two of them.

## What you get

Answers with article numbers and instrument identifiers, and an Amended section that catches the case where the text you have been quoting was replaced.

## Boundaries

This is not legal advice and it is not a compliance position. It does not decide whether a rule applies to you, and it does not assess compliance. It reports what a published document says on a day, the output is a draft with its sources attached, and a qualified adviser decides what any of it means for you.
