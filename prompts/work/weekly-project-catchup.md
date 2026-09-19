---
name: weekly-project-catchup
mode: work
category: status
summary: Catch up on one project across mail, chat and the tracker, and separate what moved from what is stuck.
use_when: Use when you have been away from a project and need what changed, what is blocked and what needs you, before you walk into a meeting.
inputs:
  - Gmail or Outlook
  - Slack
  - Linear, Atlassian or the tracker you use
writes: none
outputs: A dated brief with What moved, What is stuck, Decisions taken, What needs you, and Not covered.
---

# Weekly project catchup

## Prompt

```text
Catch me up on PROJECT NAME for the period DATE to DATE.

Read only these sources, and say which ones you actually reached:
mail, the project channel in Slack, and the issue tracker.

Return five sections, in this order.

What moved. One line per item, each with the date and the source it
came from. An item is something that changed state, not something
that was discussed.

What is stuck. Anything that has not changed state in the period but
was expected to. Say how long it has been still, and who last touched it.

Decisions taken. Only decisions that were stated as decided. Quote the
sentence that makes it a decision, with its author and date. If people
discussed an option and never closed it, it belongs in What is stuck,
not here.

What needs you. Items where my name appears with an ask attached.
Quote the ask.

Not covered. Sources you could not reach, threads you could not read,
and anything the period cut in half. An empty list here is almost
always wrong, so look before you write it.

Rules. Every claim carries its source and date. Where two sources
disagree, show both rather than picking one. Where you cannot find
something, write NOT FOUND rather than inferring it. Do not send,
reply to, archive or modify anything.
```

## Before you run it

- Enable the connectors you name, from the `+` icon or by typing `/` and choosing Tools. Work will use what it can reach and stay quiet about what it cannot, so naming them makes the gap visible.
- Replace the project name and both dates. A period with no end date makes the Not covered section meaningless.
- Work may ask a clarifying question about scope. Answer it before it starts rather than correcting it later.

## What you get

Five sections you can read in two minutes, where every line names the message or ticket it came from. The Not covered section is the one that tells you whether to trust the other four.

## Boundaries

It does not decide what to do about anything it found, and it does not rank the items by importance, because importance is a judgement about your week rather than a property of the data. The output is a draft brief for you to read, not a status report to forward.
