---
name: spend-anomaly-watch
mode: scheduled
category: finance
summary: A weekly read on charges that moved against their own history, with the arithmetic shown and no cause attached.
use_when: Use when spend is spread across vendors and nobody notices a change until the quarter closes.
inputs:
  - Stripe, or an export in Drive or SharePoint
writes: none
outputs: Ranked changes with both figures and the difference, new and stopped charges, and what could not be compared.
---

# Spend anomaly watch

## Prompt

```text
Compare the period since this task last ran against the same length of
time before it. Read only. Change nothing.

Source: WHERE.
Threshold: flag a change above PERCENT percent or CURRENCY AMOUNT,
whichever is smaller.

State the two periods and both totals before anything else. Every
figure below sits inside those two windows.

Then four groups.

Larger. Line items above the threshold. Show the earlier figure, the
later figure, the difference and the percentage, with the subtraction
visible. Largest difference first.
Smaller. The same, for drops. A drop matters as much as a rise and is
noticed far less.
New. Line items present in the later period and absent in the earlier
one.
Stopped. Present earlier, absent later.

Then a line for what you could not compare: renamed line items,
currency changes, or a category that only exists on one side. Never
let one of those appear as New or Stopped without saying so.

Rules. Do not explain why anything changed. Do not call anything waste.
Currency is stated once, and mixed currencies are kept separate rather
than converted.
```

## Before you run it

- Set both thresholds. A percentage alone floods the report with small line items; an amount alone hides fast growth on a small base.
- Renames are the usual false positive. The last line exists so a renamed item is not read twice, once as Stopped and once as New.

## What you get

A weekly list of what moved in your spend, with the subtraction shown so the figure can be checked, and no story attached to it.

## Boundaries

It does not judge a charge, cancel anything or name a cause. The watch is a draft comparison from the records, and the budget owner decides whether a change is a problem.
