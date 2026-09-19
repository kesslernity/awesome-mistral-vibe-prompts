---
name: overnight-incident-digest
mode: scheduled
category: operations
summary: A morning digest of what broke overnight, taken from the channels and tickets themselves, with the open questions listed.
use_when: Use when incidents are discussed across a chat tool and a tracker and you want one read before the stand-up.
inputs:
  - Slack
  - Linear, Atlassian or GitHub
writes: none
outputs: One block per incident with timeline, current state as stated, who is on it, and what is still unanswered.
---

# Overnight incident digest

## Prompt

```text
Read the incident channels and tickets I name, covering the period
since this task last ran. Change nothing.

Channels: LIST.
Tracker: WHICH ONE, and which project or label.

For each incident, one block.

Title, and the identifier if there is one.
Timeline. First report, first acknowledgement, the state changes, and
the most recent message, each with its time and who wrote it.
Current state, quoted from the most recent message rather than
inferred. If nobody has written anything for hours, say how long the
silence has run.
Who is on it, as stated. If nobody is named, write NOBODY NAMED.
Customer impact, only if someone stated it. Never estimate it.
Open questions. What the thread asks and nobody has answered.

Then two lists.

Still open. Incidents with no stated resolution.
Went quiet. Incidents with no message for over four hours and no
stated resolution. This list is the point of the digest.

Rules. Do not diagnose a cause. Do not judge severity. Where the thread
disagrees with the ticket, show both and say they disagree.
```

## Before you run it

- Name the channels. A scheduled task that reads every channel produces a digest nobody finishes.
- Read-only by design. A scheduled run is unattended, so it should never be the thing that changes an incident state.

## What you get

A pre stand-up read with the timeline already assembled, and a Went quiet list that surfaces the incident everyone assumed someone else had.

## Boundaries

It does not classify severity, assign an owner, change a ticket or diagnose a cause. The digest is a draft record from the threads, and the people running the incident decide what it means.
