---
name: change-announcement-draft
mode: work
category: comms
summary: Draft an internal announcement for a change, with the questions people will ask answered or explicitly listed as unanswered.
use_when: Use when a change is about to affect colleagues and you need an announcement that survives the first ten replies.
inputs:
  - The change description, dates and affected population
  - Any support, training or FAQ material that already exists
writes: none
outputs: A draft announcement plus an Anticipated questions list split into answered and unanswered, and a What I invented check.
builtin_overlap: internal-comms
---

# Change announcement draft

## Prompt

```text
Draft an internal announcement.

Change: WHAT IS CHANGING.
Who it affects: POPULATION.
When: DATE, and any window.
What people have to do: ACTION, or nothing.
Where help comes from: CHANNEL.

The announcement, under 250 words, in this order: what is changing,
when, what it means for the reader specifically, what they have to do
and by when, and where to get help. Lead with the effect on the reader,
not with the project name.

Then Anticipated questions, split in two.

Answered. Questions the material I gave you does answer, with the
answer and where it came from.

Unanswered. Questions people will certainly ask that my material does
not answer. Write the question, not a guess at the answer. This list is
the point of the exercise, so do not pad the answered list to shorten
it.

Then What I invented. Every detail in the draft that did not come from
my material: a date you smoothed, a reassurance you added, a benefit
you asserted. Each one quoted from your own draft. If the list is
empty, say so explicitly.

Rules. No benefits that are not in my material. No apology and no
enthusiasm that I did not ask for. Do not send or post this anywhere.
```

## Before you run it

- Vibe Work ships a built-in `internal-comms` skill covering status reports, leadership updates, FAQs and incident notes. Try `/internal-comms` first for the general case; this prompt is for the specific one where the unanswered questions matter more than the prose.
- Give it the support channel and its actual hours. Announcements fail on the help line more often than on the wording.

## What you get

A short draft, the questions it will trigger, and an explicit list of everything the model added that you never said, which is the paragraph to delete before sending.

## Boundaries

It does not send or post anything, and it does not decide whether the change is ready to announce. The announcement is a draft that you own and put your name on.
