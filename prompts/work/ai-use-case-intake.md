---
name: ai-use-case-intake
mode: work
category: governance
summary: Turn a proposed AI use case into a structured intake record, with the unanswered governance questions listed as questions.
use_when: Use when someone proposes an AI use case and you need it written down in a comparable shape before anyone assesses it.
inputs:
  - The proposal, thread or meeting note describing the use case
  - Your own intake template, if you have one
writes: none
outputs: An intake record with purpose, data, decision impact, human role and reversibility, plus Unanswered questions routed to named owners.
---

# AI use case intake

## Prompt

```text
Turn the proposal I am giving you into an intake record.

Fields. Where the material does not say, write NOT STATED and add the
question to the list at the end. Never fill a field with a plausible
answer.

  Use case, in one sentence: who does what, with what, to achieve what.
  Requested by, and the date.
  The job today. How this is done now, and what it costs in time or
  money, as stated.
  Data it would read. Sources, and whether any of it is personal,
  confidential or customer data, as stated in the material.
  Data it would produce or change.
  Who or what the output affects. A person, a customer, a supplier, a
  system, a document.
  The decision. What decision the output feeds, who takes that decision
  today, and whether that stays true.
  Human role. Where a person reads the output before anything happens,
  and what they would be checking.
  Reversibility. What happens if the output is wrong, how it would be
  noticed, and how long it would take to undo.
  Volume. How often this would run.
  Success. How anyone would know it worked, as stated.

Then Unanswered questions. One line each, with the field it belongs to
and the named person who can answer it. Group them by that person.

Then Out of scope for this form. Anything in the proposal that is a
different use case wearing the same name.

Rules. Do not assess, score or approve. Do not suggest a tool. If the
proposal describes a person's judgement being replaced rather than
prepared, quote that sentence under the Human role field rather than
resolving it.
```

## Before you run it

- Paste your own intake template after the fields list and say "map to this instead" if you already have one. The point is comparability across records, and an existing form beats a new one.
- Expect NOT STATED across several fields on a first proposal. That list is the intake's output, not a failure of the run.

## What you get

A record in a fixed shape that can sit next to every other one, and a grouped question list you can send to three people instead of scheduling a workshop.

## Boundaries

It records and routes. It does not assess risk, approve a use case or classify anything, and no output of this prompt authorises a system to be built or used. The record is a draft intake for the people who assess, and nothing produced here is a safety, legal or regulatory determination: a qualified human decides all of those.
