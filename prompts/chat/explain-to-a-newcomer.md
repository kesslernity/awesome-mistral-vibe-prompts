---
name: explain-to-a-newcomer
mode: chat
category: explaining
summary: Explain something to a named level of prior knowledge, with the terms that have to be learned separated from the ones that can wait.
use_when: Use when you have to bring somebody up to speed and you have stopped being able to tell what is obvious.
inputs:
  - The thing to explain
  - Who the newcomer is and what they already know
writes: none
outputs: A layered explanation, a must-know terms list, a can-wait list, and the questions they will ask next.
---

# Explain to a newcomer

## Prompt

```text
Explain the thing below to someone new.

Thing: WHAT.
Who they are: ROLE, and what they already know well.
Why they need it: THE TASK in front of them.

Four parts.

One sentence. What it is and what it is for. No analogy yet.

The shape. Five or six sentences: the parts, how they relate, and where
this person's work touches it.

Must know now. Terms they cannot get through a meeting without, each in
one line. Keep this list short, because a long one is a glossary and
nobody reads a glossary.

Can wait. Terms they will hear and can safely ignore for a month, with
one line on why they can wait. This list does more for a newcomer than
the first one.

Then: the three questions they will ask next, with a one line answer
each.

Pitch it at what they already know. Do not explain their own field back
to them, and do not use an analogy unless the plain version failed
first, in which case say why.

THING:
```

## Before you run it

- Name what they already know well. An explanation aimed at nobody in particular ends up aimed at a beginner, which insults an experienced person joining from elsewhere.
- Read the Can wait list yourself. It is a decent test of whether you still know which parts of your own area actually matter.

## What you get

An explanation sized to a real person, with the vocabulary split into what they need this week and what they can leave alone.

## Boundaries

It does not know your organisation's version of any of this, so local naming and local exceptions will be missing. Treat it as a draft briefing to correct, not an onboarding document.
