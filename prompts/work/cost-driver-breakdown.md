---
name: cost-driver-breakdown
mode: work
category: analysis
summary: Break a cost line into its drivers from the data you supply, showing the arithmetic and refusing to guess at missing pieces.
use_when: Use when a cost has moved and you need to know which components moved, before anyone explains it in a meeting.
inputs:
  - The cost export, invoice detail or billing report for both periods
writes: none
outputs: A driver table with both periods, the delta, the share of the total move, the arithmetic shown, and an Unexplained residual line.
---

# Cost driver breakdown

## Prompt

```text
Break down the change in COST LINE between PERIOD A and PERIOD B, using
only the data I have attached.

First, state the two totals and the difference, in the currency of the
file. Show the arithmetic.

Then a table, one row per driver, ordered by the size of the move:

  Driver. The component, named as the data names it.
  Period A. The figure.
  Period B. The figure.
  Change. Absolute and as a share of the total move. Show the division.
  Direction. Whether this driver increased or decreased the total.

The shares must sum to the total move. If they do not, add a final row
called Unexplained residual with the amount and say what it is made of:
rows you could not classify, currency effects, a period boundary, a
changed tag. Never distribute a residual across the drivers to make the
table balance.

Then two sections.

What changed in the data rather than in reality. Renamed components, a
new account, a reclassification, a period of different length, a rate
change. Each with the evidence you saw in the file.

What I cannot see from here. What a driver is made of, why a rate
changed, who owns a component, anything that needs a source outside
this export.

Rules. Every figure comes from the attached data. Show every division
and every subtraction. Do not attribute a cause to a driver.
```

## Before you run it

- Attach both periods at the same granularity. A summary for one period and detail for the other produces a confident and wrong table.
- Say whether the figures are gross or net of credits, and whether the periods are the same length.

## What you get

A driver table that adds up, or an explicit residual line where it does not, with the arithmetic visible so someone can check it in a meeting.

## Boundaries

It reports what moved, not why. It does not name a cause, judge a cost or recommend a cut. The breakdown is a draft for the person who owns the budget to read against the source figures.
