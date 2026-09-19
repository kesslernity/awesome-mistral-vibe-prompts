---
name: pipeline-hygiene-check
mode: scheduled
category: revenue
summary: A weekly read on the records in your pipeline that are stale, incomplete or internally inconsistent.
use_when: Use when pipeline reviews keep turning into arguments about whether the data is right.
inputs:
  - The pipeline source: Notion, Linear, Atlassian or an exported sheet in Drive or SharePoint
writes: none
outputs: Grouped exception lists with record links and counts, plus the totals with and without the exceptions.
---

# Pipeline hygiene check

## Prompt

```text
Check my pipeline records for hygiene problems since this task last
ran. Read only. Change no record.

Source: WHERE, and which view or database.
Fields that must be filled: LIST.
Stale means no activity for more than DAYS days.

Group the exceptions.

Stale. Past the staleness threshold and still open. Show the days since
last activity, highest first.
Missing fields. Records with a required field empty, naming the field.
Date in the past. Records with a close date already gone by that are
still open.
Stage and activity disagree. Late-stage records with no recent
activity, and early-stage records with a close date inside the month.
Duplicates. Records that look like the same opportunity, quoted side by
side so a human can judge.
No owner.

Per group: the count, and up to ten records with a link each. If a
group is empty, say so in one line.

Then the arithmetic. Total value of open records, total value of the
records flagged above, and the first number minus the second. Show the
subtraction. State the currency and say whether values are as recorded,
because you have no way to check them.

No forecast. No probability. No comment on any individual deal.
```

## Before you run it

- Set the staleness threshold and the required field list explicitly. Without them the run invents a standard and the exception counts mean nothing week to week.
- The subtraction at the end is the number worth showing in a review, because it separates the pipeline from the part of it that nobody has touched.

## What you get

A weekly exception list with links, and one arithmetic line that shows how much of the pipeline rests on records nobody has maintained.

## Boundaries

It does not forecast, score or close anything, and it changes no record. The check is a draft exception list, and the owner of each record decides what is actually wrong.
