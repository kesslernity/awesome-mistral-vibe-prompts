---
name: exec-update-draft
mode: work
category: comms
summary: Draft a short leadership update from the evidence you already have, with every claim tied to a source.
use_when: Use when you owe someone senior a written update and the material is scattered across tickets, documents and threads.
inputs:
  - The tracker or project board
  - The document or deck the work produced
  - Any thread where the decisions were taken
writes: none
outputs: A draft update under 300 words with Position, Changes, Risks, Asks, and a separate evidence list keyed to each claim.
---

# Exec update draft

## Prompt

```text
Draft a leadership update on PROJECT NAME covering DATE to DATE, for
an audience of AUDIENCE who last heard about this on DATE.

Work from the sources I name and nothing else. Say which ones you
reached.

Structure, under 300 words in total.

Position. Two sentences on where the work stands now. No adjectives
that cannot be checked. "On track" is a claim, so if you write it,
show what it rests on.

Changes since the last update. Three to five lines. Each one says what
changed and what it means for the plan, not just that it happened.

Risks. Only risks with evidence behind them. For each: the risk, the
signal you saw, and the date of that signal. A risk with no signal is
a worry, and it does not belong in an update.

Asks. What you need from this audience, stated as a decision they can
make or a resource they can release. If there is nothing, write
"Nothing this period" rather than inventing an ask.

Then, below the update and clearly separated from it, an evidence list:
one numbered line per claim in the update, with the source and date it
came from. Any claim you could not source stays in this list marked
UNSOURCED and is removed from the update above.

Rules. No internal codenames the audience will not know. No percentage
or figure that is not in a source. Do not send this anywhere.
```

## Before you run it

- Name the audience and the date they last heard from you. Both change what counts as news.
- If your organisation has a house template, paste it in and say "use this structure instead" after the sources line.

## What you get

A short update, plus the evidence list that is the actual point: it shows you which of your own claims you cannot support before someone senior asks.

## Boundaries

It does not decide whether the project is on track, and it does not soften or sharpen a status on your behalf. The update is a draft you edit and send yourself, under your name.
