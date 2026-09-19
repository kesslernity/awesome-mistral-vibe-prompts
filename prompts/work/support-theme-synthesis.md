---
name: support-theme-synthesis
mode: work
category: customer
summary: Theme a batch of support tickets or feedback with counts, quoted evidence and an explicit list of what cannot be concluded.
use_when: Use when you have a pile of tickets, reviews or survey answers and need the themes with numbers rather than an impression.
inputs:
  - The ticket export, review set or survey responses
writes: none
outputs: Themed groups with record counts and shares, anonymised quotes keyed to record ids, plus Contradictions and Cannot conclude.
---

# Support theme synthesis

## Prompt

```text
Theme the records I am giving you.

First, count. How many records, over what period, from what source, and
how many you had to exclude and why. Every share you quote later is
against this denominator, stated once here.

Then the themes. Build them from the text rather than from a list you
already have. For each theme:

  Theme. A sentence describing what the customer is experiencing, not a
  one word label.
  Count and share. The share carries the denominator with it.
  Evidence. Two or three short quotes, each keyed to a record id. Strip
  names, addresses, order numbers and anything else identifying.
  Boundary. What is in this theme and what is deliberately not, so it
  does not quietly absorb its neighbours.

Then three sections.

Contradictions. Records that say the opposite of a theme. Every real
theme has some. If you found none, say you found none and treat that as
a reason for doubt rather than a strong result.

Cannot conclude. Questions these records cannot answer: how common this
is among people who did not write in, whether it is getting worse,
whether it costs anything.

Unthemed. The records that did not fit anywhere, with a count. A high
number here is information, not failure.

Rules. No sentiment score and no percentage positive. Ratings appear
as distributions with an n or not at all. Do not recommend a fix.
```

## Before you run it

- Say what the set is and how it was selected. People who write in are not a sample of your customers, and the Cannot conclude section depends on you saying so.
- Strip or mask personal data before the run if your policy requires it. The prompt asks for anonymised quotes, but the input is yours to control.

## What you get

Themes with counts against a stated denominator, quotes you can use without exposing a customer, and a section that says what this pile of records genuinely cannot tell you.

## Boundaries

It does not prioritise, size or recommend anything, and a theme is not a root cause. The synthesis is a draft for the people who own the product to read against the raw records.
