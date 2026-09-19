---
name: meeting-prep-brief
mode: work
category: meetings
summary: Build a one page brief for a specific meeting from the invite, the thread history and the last decisions taken.
use_when: Use when you are walking into a meeting you did not organise and need the history, the open questions and the likely asks.
inputs:
  - The calendar invite
  - Mail or chat threads with the attendees
  - Any document attached to the invite
writes: none
outputs: A brief with Purpose, Who is in the room, What happened last time, Open questions, Likely asks, and What I could not find.
builtin_overlap: meeting-prep
---

# Meeting prep brief

## Prompt

```text
Prepare me for the meeting titled TITLE on DATE.

Read the invite, the attached documents, and any thread with these
attendees from the last 60 days. Say which sources you reached.

Return six sections.

Purpose. What this meeting is for, in one sentence, taken from the
invite or the thread rather than from the title. If the purpose is not
stated anywhere, say so instead of guessing it.

Who is in the room. One line per attendee: their role if you can find
it, what they last said about this topic, and the date. Where you have
nothing on someone, write NO HISTORY rather than leaving them out.

What happened last time. The previous meeting or thread on this topic,
what was decided, and what was left open. Quote the decision.

Open questions. Things that were raised and never answered, each with
who raised it and when.

Likely asks. What someone in this room is probably going to want from
me, based on what they have asked for before. Mark each one as either
stated in a source or inferred, and never blur the two.

What I could not find. Threads you could not read, attendees with no
history, documents you could not open.

Rules. Quote rather than paraphrase when the wording matters. Every
line carries a date. Do not accept, decline or reply to the invite.
```

## Before you run it

- Vibe Work ships a built-in `meeting-prep` skill. Type `/meeting-prep` first and see whether it covers your case; this prompt exists for when you want the evidence and the gap list in a fixed shape.
- Give the exact meeting title and date. Two meetings with similar names in one week is the common failure.

## What you get

A brief you can read in the corridor, where the Likely asks section separates what people actually said from what the model inferred, and the last section tells you where the history is thin.

## Boundaries

It does not tell you what position to take, and an inferred ask is a guess with a label on it, not intelligence. The brief is a draft for your own use, not a document to circulate.
