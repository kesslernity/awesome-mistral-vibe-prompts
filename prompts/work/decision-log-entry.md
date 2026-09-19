---
name: decision-log-entry
mode: work
category: meetings
summary: Turn a thread or a set of notes into one decision log entry, with the decision quoted and the alternatives recorded.
use_when: Use when a decision has just been taken in a meeting or a thread and you need it written down before the reasoning evaporates.
inputs:
  - The thread, notes or transcript where the decision was taken
  - Any document the decision refers to
writes: none
outputs: A single log entry with Decision, Date and forum, Decided by, Because, Alternatives considered, Consequences, Revisit when, and Unresolved.
---

# Decision log entry

## Prompt

```text
Write one decision log entry from the material I am giving you.

Fields, in this order.

Decision. One sentence, in the present tense, stating what was decided.
Then the exact quote from the source that makes it a decision, with its
author and timestamp. If no sentence in the material states a decision,
stop and tell me that instead of writing the entry.

Date and forum. When and where it was taken.

Decided by. The person or group with the authority here, as stated in
the material. If the material does not say, write NOT STATED rather
than assuming it was whoever spoke last.

Because. The reasons given at the time, not the reasons that make sense
now. Quote or cite each one.

Alternatives considered. What else was on the table and why it was not
chosen. If nothing else was discussed, write NONE DISCUSSED, which is
itself worth recording.

Consequences. What now becomes true, and what now has to change. Only
consequences that were stated or that follow directly.

Revisit when. The condition or date that would reopen this, if one was
given. Do not invent one.

Unresolved. Anything that was raised and not settled by this decision.

Rules. Do not improve the reasoning. A decision log is a record of what
was decided and why it was decided then, including the parts that look
weak later.
```

## Before you run it

- Paste the raw material or point at the thread. A summary of the thread loses the sentence that makes the decision a decision.
- If the decision was taken verbally and the notes are thin, expect NOT STATED in two or three fields. That is the correct output, and it tells you what to go and confirm.

## What you get

One entry you can paste into a decision log, where the quote does the work and the empty fields show you what was never actually settled.

## Boundaries

It does not validate the decision or say whether the right person made it. It records a draft of what happened, and the Decided by field is copied from the material rather than assessed.
