---
name: vendor-renewal-lookahead
mode: scheduled
category: finance
summary: A monthly look at contracts reaching a notice window, with the dates counted and the missing documents named.
use_when: Use when auto-renewal has already cost you once and nobody owns the calendar.
inputs:
  - Google Drive, SharePoint or Notion, and the contract folder or register
writes: none
outputs: Contracts ordered by notice deadline, the arithmetic behind each date, and lists for missing terms and missing owners.
---

# Vendor renewal lookahead

## Prompt

```text
Read the contract records below and give me the renewals reaching a
decision window in the next MONTHS months. Read only. Change nothing.

Source: WHERE.
Today's date: read it from the run, and state it at the top.

One block per contract, ordered by the earliest date at which action
is required.

Vendor, and the document link.
Renewal date, quoted from the contract with its clause or page.
Notice period, quoted the same way. If the document does not state one,
write NOTICE PERIOD NOT FOUND and treat the contract as urgent.
Notice deadline. Renewal date minus notice period. Show the
subtraction, both dates and the day count from today.
Automatic renewal: yes, no, or NOT STATED, with the quoted clause.
Annual value as recorded, with its currency.
Owner as recorded, or NO OWNER RECORDED.

Then three lists.

Inside the notice window already. The decision is live now.
Missing a notice period or a renewal date. These cannot be scheduled
and are the real risk in the set.
No owner recorded.

Rules. Every date comes with the quoted text it came from. Do not
interpret a clause, do not judge whether a contract is good value, and
do not draft anything to a vendor.
```

## Before you run it

- Monthly is the right cadence. Weekly repeats the same list; quarterly misses a ninety day notice period.
- The Missing list matters more than the ordered one. A contract with no recorded notice period cannot be watched by any calendar, including this one.

## What you get

A monthly list ordered by the date something has to happen, with each date traceable to a quoted clause, and the contracts that cannot be tracked separated out.

## Boundaries

It does not interpret contract terms, give legal advice, contact a vendor or start a cancellation. The lookahead is a draft calendar built from the documents, and a qualified human reads the clause before acting on it.
