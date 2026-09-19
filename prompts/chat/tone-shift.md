---
name: tone-shift
mode: chat
category: writing
summary: Move a message along one named axis of tone and show exactly which words did the work.
use_when: Use when a message is right in substance and wrong in temperature.
inputs:
  - The text
  - The direction, named as an axis
writes: none
outputs: The shifted version, a table of the words that changed, and a warning on any change that altered the meaning.
---

# Tone shift

## Prompt

```text
Shift the tone of the text below. Keep the content identical.

Direction: NAME THE AXIS, for example warmer, firmer, more neutral,
less apologetic, less certain.
Keep: anything I want untouched.

Return three things.

The shifted version.

What moved the tone. A table of before and after word or phrase pairs,
with one word on why each one changes the temperature. This is the part
worth reading, because it tells you what you were doing without
noticing.

Meaning changes. Anywhere the shift altered what the text commits to, a
deadline, a degree of certainty, an acceptance of fault. Quote both
versions and flag it. Firmer must not become a promise I did not make,
and softer must not become an apology I did not offer.

Rules. Same facts, same dates, same names. No new pleasantries. If the
requested direction cannot be reached without a meaning change, say so
and show the furthest safe version.

TEXT:
```

## Before you run it

- Name the axis. "Better" produces a generic business voice and deletes whatever made the message yours.
- Watch the third section on anything sensitive. Softening an email is the most common accidental route to admitting fault.

## What you get

The same message at a different temperature, plus the word level record of how it got there and a flag wherever the tone change moved the substance.

## Boundaries

It does not judge whether the tone is right for the person receiving it. The shifted text is a draft, and any change flagged under meaning changes is yours to accept deliberately or reverse.
