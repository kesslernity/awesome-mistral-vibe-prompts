---
name: rfp-requirement-extract
mode: work
category: documents
summary: Turn a tender or RFP document into a numbered requirement table with page references and an explicit list of ambiguities.
use_when: Use when a tender, RFP or statement of work arrives and you need every requirement as a row before anyone starts writing answers.
inputs:
  - The RFP, tender or statement of work, including annexes
writes: none
outputs: A numbered requirement table with page and clause references, plus Ambiguous, Conflicting, and Not a requirement.
builtin_overlap: structured-extraction
---

# RFP requirement extract

## Prompt

```text
Extract every requirement from the attached document and its annexes.

A requirement is anything the document obliges a bidder to do, provide,
meet or evidence. Wording like "shall", "must", "is required to" and
"the bidder will" signals one. "May", "should" and "is encouraged to"
signal something weaker, and you keep them with their strength recorded
rather than promoting them.

Return a table, one row per requirement:

  ID. Number them in document order.
  Requirement. The obligation, in the document's own words where the
  wording matters.
  Strength. Mandatory, recommended or optional, taken from the verb.
  Source. Document name, section and page.
  Response type. What the bidder has to produce: a narrative, a figure,
  a certificate, a named person, a sample, a price.
  Owner. Leave blank. A human fills this in.

Then three lists.

Ambiguous. Requirements where the obligation could be read two ways.
Give both readings and say which part of the sentence causes it.

Conflicting. Places where two sections require different things. Cite
both.

Not a requirement. Sentences that read like requirements but are
context, background or vendor marketing. This list stops the table
growing by a third.

Rules. Do not merge two requirements into one row because they are
adjacent. Do not answer any of them. Do not assess whether we can meet
them.
```

## Before you run it

- Attach the annexes. Evaluation criteria and pricing schedules carry requirements the main body never mentions.
- Vibe Work ships a built-in `structured-extraction` skill. For a quick table it is enough; this prompt adds the strength column and the ambiguity list, which is where tender arguments actually happen.

## What you get

A numbered table you can split across owners, and two lists that give you your clarification questions before the deadline for asking them closes.

## Boundaries

It does not decide whether to bid and it does not judge whether a requirement is achievable. The extract is a draft that a human reads against the source before anybody commits to anything.
