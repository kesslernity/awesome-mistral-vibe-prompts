---
name: plain-english-rewrite
mode: chat
category: writing
summary: Rewrite dense or evasive text in plain English and flag the sentences that turned out to mean nothing.
use_when: Use when a paragraph reads as important and you cannot tell what it commits anyone to.
inputs:
  - The text to rewrite
writes: none
outputs: A plain English version, a table of the terms replaced, and a list of sentences with no content.
---

# Plain English rewrite

## Prompt

```text
Rewrite the text below in plain English. Same meaning, no more.

Then two things.

Terms replaced. A short table: the original phrase, what you replaced
it with, and whether the replacement is exactly equivalent or slightly
narrower. Mark anything that is not exactly equivalent.

Said nothing. Sentences that survive the rewrite as empty: no actor, no
action, no date, no commitment. Quote them and say what is missing. If
a sentence has no subject who does anything, it goes here.

Rules. Keep every number, date, name and condition exactly as written.
Keep hedges that carry real uncertainty, and say which ones you kept.
Do not resolve an ambiguity by picking a reading: name it instead.

TEXT:
```

## Before you run it

- Use it on text you received rather than text you wrote. The Said nothing list reads very differently when the sentences are someone else's.
- If everything lands in Said nothing, you have your answer about the document.

## What you get

A version you can act on, a record of every phrase that changed, and a list of the sentences that only appeared to say something.

## Boundaries

It does not verify any claim in the text and it does not tell you whether the original was written that way on purpose. The rewrite is a draft reading, and where it says a meaning is narrower, check the original wording.
