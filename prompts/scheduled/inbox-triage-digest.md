---
name: inbox-triage-digest
mode: scheduled
category: inbox
summary: A daily read-only digest of what arrived in your mailbox overnight, ordered by who is waiting on you.
use_when: Use when you want the state of your mailbox in one note each morning instead of opening it cold.
inputs:
  - Gmail or Outlook
writes: none
outputs: Four short buckets, the oldest unanswered ask, and a list of anything the run could not read.
---

# Inbox triage digest

## Prompt

```text
Read my mail that arrived since this task last ran. Change nothing in
the mailbox.

Give me four buckets.

Waiting on me. Someone is blocked until I answer. One line each: who it
is from, the ask in their own words, any stated date, and how long they
have been waiting.

Needs an answer, nobody blocked. Same fields, shorter.

Nothing needed. Notifications and copies. Count them by type, name the
two largest sources, and stop there.

Unclear. Messages where I cannot tell whether the ask is aimed at me.
Quote the sentence that made it ambiguous.

Then two closing lines. The oldest unanswered ask with its date. What
you could not read, including folders and attachments.

Keep the whole digest under 400 words. If nothing arrived that needs
me, say exactly that in one line rather than padding the buckets.
```

## Before you run it

- Scheduled tasks are Work mode only, and they run unattended. This one is read-only on purpose, so it needs no pre-authorisation for a write and nothing can go out in your name.
- Daily at an hour before you start reading mail is the usual cadence. Schedules run in the Workspace where they were created, and connector authentications are Workspace scoped, so create it where your mail connector lives.

## What you get

One note a day that tells you who is blocked, what the oldest unanswered ask is, and how much of the mailbox is noise.

## Boundaries

It does not answer, flag, file or mark anything, and it takes no action on a message. The digest is a draft view of the mailbox for you to act on yourself.
