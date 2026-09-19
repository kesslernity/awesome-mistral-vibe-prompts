---
name: project-rollup
mode: scheduled
category: projects
summary: A weekly read-only rollup across your tracker and channels, built from what moved and what did not.
use_when: Use when you write the same weekly status by hand from three tools every Friday.
inputs:
  - Linear, Atlassian or GitHub
  - Slack or Notion, if decisions live there
writes: none
outputs: Per workstream progress, slipped dates with old and new, items with no owner, and a Went quiet list.
---

# Project rollup

## Prompt

```text
Build my weekly rollup from the sources below, covering the period
since this task last ran. Read only. Change nothing anywhere.

Tracker: WHICH, and which project, team or label.
Discussion: WHERE, and which channels or pages.

Per workstream.

Progressed. Items that changed state, with their old and new state, and
who made the change.
Landed. Items now in a done state, with the date.
Slipped. Items whose target date shifted, with both dates and the
stated reason. If no reason is recorded, write NO REASON RECORDED.
Blocked. Items marked blocked, with what is named as the blocker and
how many days they have been blocked.
No owner. Open items with nobody assigned.

Then three lists across all workstreams.

Went quiet. Items with no activity for more than fourteen days that are
still open.
Decided this week. Decisions I can point to in a message or page, each
quoted with its author and date. If you cannot quote it, it is not a
decision, it is a discussion.
Discussed, not decided. The threads that ran without a conclusion.

Keep it factual. No health colour, no percentage complete, no
prediction of a date. Those are mine to set.
```

## Before you run it

- Give it one project or label. A rollup across a whole workspace is a wall rather than a read.
- The Went quiet and No owner lists are usually the two that change your Monday. Read them first.

## What you get

A Friday read assembled from the tools instead of from memory, with slippage shown as two dates and decisions shown as quotes.

## Boundaries

It does not set a status colour, forecast a date, assign an owner or change a ticket. The rollup is a draft you edit before it becomes a status anyone relies on.
