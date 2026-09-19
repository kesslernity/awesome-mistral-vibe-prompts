---
name: kpi-pack-prep
mode: scheduled
category: reporting
summary: A monthly figures pack built only from the sources, with each number carrying its definition, period and denominator.
use_when: Use when the monthly pack takes a day to assemble and half the meeting is spent questioning the numbers.
inputs:
  - The source exports or dashboards, in Drive, SharePoint, Notion or Stripe
writes: none
outputs: One block per metric with the figure, its definition, its period and its source, plus Missing and Changed definition lists.
---

# KPI pack prep

## Prompt

```text
Assemble the monthly figures pack from the sources below. Read only.
Change nothing.

Metrics and their definitions: LIST, or point me at the definitions
document.
Sources: WHERE, per metric.
Period: state the exact start and end dates at the top, and use the
same window for every metric.

One block per metric.

The figure, with its unit.
Its definition, quoted from my definitions rather than restated in your
own words.
Numerator and denominator, both as absolute numbers, whenever the
metric is a rate or a share. A percentage with no denominator does not
go in the pack.
The previous period's figure, and the difference, with the subtraction
shown.
Source, as a link, with the date the source was produced.

Then three lists.

Missing. Metrics you could not compute, and exactly what was missing.
Never estimate one of these.
Changed definition. Metrics whose source has changed shape since the
last period, such as a renamed column or a new filter.
Not in my definitions. Figures available in the sources that nobody has
defined, named but not computed.

Rules. No commentary, no cause, no target, no forecast. If two sources
disagree on the same metric, show both figures and say they disagree
rather than choosing.
```

## Before you run it

- Point it at your definitions document. Without one, every month silently redefines a metric and the trend line becomes fiction.
- The disagreement rule is deliberate. A pack that quietly picks one of two conflicting sources is worse than one that shows the conflict.

## What you get

A pack where every figure carries its definition, its window and its denominator, and where what could not be computed is visible instead of estimated.

## Boundaries

It does not explain a movement, set a target or forecast anything. The pack is a draft assembly of the sources, and the owner of each metric confirms it before it goes to a meeting.
