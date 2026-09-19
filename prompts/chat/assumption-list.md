---
name: assumption-list
mode: chat
category: thinking
summary: Surface the assumptions a plan or argument rests on, ranked by what happens if each one is wrong.
use_when: Use when a plan feels solid and you want the things nobody stated written down.
inputs:
  - The plan, argument or proposal
writes: none
outputs: Stated and unstated assumptions, each with its consequence if false, ranked by damage and cheapest check.
---

# Assumption list

## Prompt

```text
List the assumptions the text below rests on.

Two groups.

Stated. Assumptions the text names as assumptions. Quote them.

Unstated. Things that must be true for this to work but that the text
never mentions. This group is the reason for the exercise. Look
specifically at: who will do the work and whether they have time, what
a named other team will agree to, what the data shows, how long
something takes, what stays the same while this runs, and what a
customer or regulator will accept.

For each assumption, three fields.

If it is false. The concrete consequence, in one sentence. Not
"risk to the timeline", but what actually happens.
How to check it. The cheapest real test: a conversation with a named
role, a query, a document to read, a week of observation.
Already knowable. Whether someone could find this out today, or whether
only time answers it.

Rank the whole list by damage if false, worst first. Then give me one
line: the assumption to check first, chosen by damage divided by cost
to check.

Do not assess the plan itself.

TEXT:
```

## Before you run it

- Works on a proposal you received as well as one you wrote, and the unstated list is usually longer on the ones you wrote.
- The last line is the deliverable. An assumption that is cheap to check and expensive to get wrong is this afternoon's work.

## What you get

The load bearing beliefs under a plan, written down, each with a concrete failure and a cheap way to find out.

## Boundaries

It does not know your organisation, so some of what it calls unstated will be obvious to you and some real assumptions will be missing. The list is a draft to argue with, not an audit of the plan.
