---
name: backlog-ageing-report
mode: scheduled
category: projects
summary: A fortnightly read on how old the backlog is, where items sit untouched, and which ones nobody owns.
use_when: Use when the backlog keeps growing and nobody can say which parts of it are actually dead.
inputs:
  - Linear, Atlassian or GitHub
writes: none
outputs: Age distributions by bucket and by state, the oldest untouched items, and No owner and Never triaged lists.
---

# Backlog ageing report

## Prompt

```text
Report on the age of the backlog below. Read only. Change no item.

Source: WHERE, and which project, team or label.
Count as open: WHICH STATES.

Start with the arithmetic. Total open items, and the distribution by
age since creation: under 30 days, 30 to 90, 90 to 180, 180 to 365,
over 365. Give a count and a share for each bucket, with the total
stated so every share can be checked.

Then the same distribution by state, so a long queue in one state is
visible rather than averaged away.

Then four lists.

Oldest untouched. The twenty oldest items with no activity at all,
showing age since creation and days since last activity.
Never triaged. Items still in the intake or backlog state since the day
they were created.
No owner. Open items with nobody assigned, counted and bucketed by age.
Duplicated in wording. Items whose titles read as the same request,
quoted side by side for a human to judge.

Then one line: the median age of open items, and the median age of
items closed in the last ninety days. Both together say more than
either alone.

Rules. Do not recommend closing anything. Do not judge priority. Do not
predict when anything will be done.
```

## Before you run it

- Name the states that count as open. Every tracker has one state that means different things to different teams, and it changes the whole distribution.
- Read the two medians together. A backlog whose open median is far above its closed median is not a queue, it is an archive with a queue attached.

## What you get

A fortnightly picture of how old the work is, with the shares checkable against a stated total, and the items nobody has ever looked at named individually.

## Boundaries

It does not close, prioritise, assign or reorder anything. The report is a draft measurement of the tracker, and the team decides what to do about any of it.
