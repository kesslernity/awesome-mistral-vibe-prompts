---
name: sql-read
mode: chat
category: technical
summary: Read a SQL query back in plain words, name what it counts, and flag the joins and filters that quietly change the answer.
use_when: Use when a number came from a query you did not write and you have to decide whether to trust it.
inputs:
  - The query
  - What the number is supposed to mean
writes: none
outputs: A plain reading, the grain of the result, ranked traps in the joins and filters, and the checks that would confirm it.
---

# SQL read

## Prompt

```text
Read this query back to me.

Query:
PASTE IT
What the result is supposed to mean: WHAT.

Six parts.

One sentence. What this query returns.

The grain. One row of the output is one what. State it exactly, because
most argued numbers are a grain disagreement.

Tables and joins. For each join: which one it is, on what, and what it
does to the row count. Name any join that can multiply rows, and any
outer join whose filter in the WHERE clause silently turns it into an
inner one.

Filters. Every condition, in plain words, including the ones hidden in
a join condition. Flag any comparison against a column that can be
null, because null comparisons drop rows without saying so.

Counts and sums. For each one: what exactly is being counted, whether
duplicates are included, and whether the denominator of any ratio is
the same population as its numerator.

Traps, ranked. The ways this query could return a number that looks
right and is not. Date boundaries that include or exclude a day, a
timezone, a deleted or inactive flag not filtered, a currency or unit
mix, a grouping that hides a duplicate.

Then: the smallest check that would confirm the result. Usually a count
at a different grain, or the same query over a period whose answer I
already know.

You cannot run this, so mark anything that depends on the data rather
than the query text as something to verify.
```

## Before you run it

- Say what the number is supposed to mean. The grain section is where most wrong numbers come from, and it only works against a stated intent.
- Chat cannot connect to a database or run the query. This is a read of the text, which is exactly what you want before you run anything.

## What you get

A plain statement of what the query counts, the joins and filters that can change the answer without looking wrong, and one small check to confirm it.

## Boundaries

It does not run the query, see the data or know your schema's history. The reading is a draft, and anything that depends on what is actually in the tables has to be verified against them.
