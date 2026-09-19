---
name: metric-definition-audit
mode: work
category: analysis
summary: Collect every definition of a metric in use across your documents and show where they disagree.
use_when: Use when two teams report the same metric with different numbers and you need to find out whether they are measuring the same thing.
inputs:
  - The reports, dashboards specs, documents or threads where the metric appears
writes: none
outputs: One row per definition found with its source and date, a disagreement matrix, and a list of the questions the documents cannot answer.
---

# Metric definition audit

## Prompt

```text
Find every definition of METRIC NAME in the material I am pointing you
at, and show where they disagree.

One row per definition you find:

  Source. Document, dashboard or thread, with its date and owner if
  stated.
  Definition. Quoted. If a document uses the metric without defining
  it, that is a row too, with the definition column marked USED BUT NOT
  DEFINED.
  Numerator. What is counted.
  Denominator. What it is counted against, if anything.
  Population. Who or what is included, and who is excluded.
  Window. The period, and whether it is calendar or rolling.
  Filters. Anything excluded: test accounts, internal users, cancelled
  rows, a region.

Then the disagreements. For each pair of definitions that differ, one
line naming the field they differ on and what the difference would do
to the number. Bigger or smaller, and roughly by how much if the
material lets you say.

Then Questions the documents cannot answer. Things only the owner of
each definition can settle, one question per owner, named.

Rules. Do not pick a correct definition. Do not write a new one. Where
a document implies a definition without stating it, mark it INFERRED
and show the sentence you inferred from.
```

## Before you run it

- Point at the places the metric is actually used, including the thread where someone first asked for it. The oldest definition is usually the one still in a query somewhere.
- Do not supply your own definition first. It becomes the anchor everything else is judged against.

## What you get

Every definition in one view, the specific field each pair disagrees on, and a named question for each owner, which is what turns a reporting argument into a short meeting.

## Boundaries

It does not choose a definition, and it has no authority to. The audit is a draft that the metric owners resolve between them.
