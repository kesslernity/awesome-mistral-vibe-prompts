---
name: error-message-decode
mode: chat
category: technical
summary: Read an error message back in plain words, separate what it states from what it implies, and rank the causes by how cheap they are to check.
use_when: Use when an error is unfamiliar and you want the reading before you start changing things.
inputs:
  - The error message in full, and what you were doing when it appeared
writes: none
outputs: A plain reading, what the message does and does not state, ranked candidate causes with a cheap check for each.
---

# Error message decode

## Prompt

```text
Read this error message back to me.

What I was doing: CONTEXT.
Where it appeared: WHERE.
Error, in full:
PASTE IT

Five parts.

Plain reading. What the message says, in one or two sentences.

What it states. The facts the message itself contains: the component,
the operation, the code, the value. Quote them.

What it does not state. What people will assume from this message that
it does not actually say. Misreadings here cost more time than the
error does.

Likely causes, ranked. For each: the cause, why this message would
appear if that were true, and the cheapest way to check it. Rank by
cost to check, not by likelihood, because a five second check on a less
likely cause beats an hour on a more likely one.

What would tell us more. Which log, which flag, which command output,
stated specifically.

Rules. You cannot see my system, so distinguish clearly between what
the message proves and what you are inferring. If the message is
truncated or the important part is missing, say what part you need.
Do not guess a version specific behaviour: say what to confirm.
```

## Before you run it

- Paste the whole thing, including the part that looks like noise. Stack frames and codes carry most of the information.
- This is a reading, not a fix. Chat cannot run anything or see your machine, so it works with the text you gave it and nothing else.

## What you get

A plain reading, an explicit line between what the error proves and what it merely suggests, and a check list ordered so the cheapest test comes first.

## Boundaries

It does not run commands, see your environment or confirm a version specific behaviour. Every cause is a draft hypothesis with a check attached, and the check is the part that settles it.
