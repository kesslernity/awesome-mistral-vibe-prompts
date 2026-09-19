---
name: pre-mortem-quick
mode: chat
category: thinking
summary: Assume the thing failed, then work backwards to the causes, the earliest visible signal and what to do now.
use_when: Use when a plan is agreed, the deadline is real, and nobody wants to reopen it.
inputs:
  - The plan and its deadline
  - What success is supposed to look like
writes: none
outputs: Ranked failure stories with their earliest signal, the cheapest action now, and the failure nobody is watching.
---

# Pre-mortem quick

## Prompt

```text
It is DATE. The plan below failed. Not partially, it failed.

Plan: WHAT IT IS.
Success was supposed to be: WHAT.

Write the five most likely stories of how that happened. One paragraph
each, in the past tense, as if reporting it afterwards.

Order them by likelihood, and say what makes each one likely rather
than merely possible.

Then for each story, three lines.

Earliest visible signal. The first thing anyone could have noticed, and
roughly when relative to the deadline.
Who would have seen it first. A role, not a name.
Cheapest action today. What I could do this week that makes this story
less likely or easier to catch.

Then close with one section: the failure nobody is watching. Of the
five, which one has no owner, no signal in any existing report, and no
regular meeting where it would come up.

Realistic causes only. Ordinary ones. A key person leaves, an agreement
was assumed rather than confirmed, the data was worse than anyone
looked at, two teams read the same sentence differently.
```

## Before you run it

- Give it the real deadline. A pre-mortem with no date produces vague causes and no signals.
- Fifteen minutes on this is worth more than another hour of planning, because the output is a watch list rather than more plan.

## What you get

Five concrete failure stories ranked by likelihood, each with the first observable signal and a cheap action, plus the one failure your current reporting would never surface.

## Boundaries

It does not know your organisation, so the stories are drafts to test against people who do. The value is in the signals and the unwatched failure, not in the ranking.
