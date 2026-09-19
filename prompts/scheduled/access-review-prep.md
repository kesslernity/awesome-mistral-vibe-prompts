---
name: access-review-prep
mode: scheduled
category: governance
summary: A quarterly pack that assembles who has access to what, ready for the owners to review, with no recommendation attached.
use_when: Use when access reviews stall because assembling the lists takes longer than reviewing them.
inputs:
  - The access exports or listings, in Drive, SharePoint or a repository
writes: none
outputs: Per system membership lists grouped by owner, plus flags for dormant, unmatched and unowned entries.
---

# Access review prep

## Prompt

```text
Assemble the access review pack from the exports below. Read only.
Change no permission, no group and no file.

Exports: WHERE, and which systems they cover.
Reference list of current people: WHERE.
Dormant means no recorded activity for more than DAYS days.

Per system.

Who has access, grouped by role or permission level, with the count per
group.
System owner as recorded, or NO OWNER RECORDED.
Date of the export, quoted from the file. If the export carries no
date, say so, because an undated export cannot support a review.

Then four flags across all systems.

Not on the reference list. Accounts present in an export and absent
from the people list. Show both entries so a human can judge whether it
is a leaver or a name mismatch.
Dormant. Past the threshold, with the days since last recorded
activity.
Elevated. Anyone in an administrator or owner group, listed in full
regardless of the other flags.
Unowned systems. Any export whose system has no recorded owner.

Then a coverage line: which systems you had an export for, and which
systems in my list produced nothing.

Rules. No recommendation on any individual account. Do not suggest
removals. Do not judge whether any access is appropriate. The pack is
evidence for the owners, not a verdict.
```

## Before you run it

- The coverage line is the honest part of the pack. A review that silently skips a system reads as complete and is not.
- Every flag is a question for a named owner rather than a finding. An unmatched account is as often a spelling difference as a leaver.

## What you get

A quarterly pack with the lists already grouped by owner, the exports dated, and the systems you have no evidence for named explicitly.

## Boundaries

It does not change, grant or withdraw access, and it does not decide whether any access is appropriate. The pack is a draft evidence set, and the system owners take every access decision themselves.
