---
name: inbox-triage-plan
mode: work
category: inbox
summary: Sort an unread mailbox into what needs you, what needs a decision and what can wait, without touching a single message.
use_when: Use when you are behind on mail and need a plan for the next hour instead of a folder full of unread items.
inputs:
  - Gmail or Outlook
writes: none
outputs: Four buckets with one line per message, its ask, its deadline, and a separate list of what was unclear.
---

# Inbox triage plan

## Prompt

```text
Triage my unread mail from DATE to now. Read it. Change nothing.

Four buckets, in this order.

Needs a decision from me. Someone is blocked until I answer. One line
each: who, the ask in their words, the deadline if stated, and how long
they have been waiting.

Needs a reply but not a decision. Acknowledgements, scheduling,
questions someone else could answer. Same fields.

Needs nothing from me. Notifications, copies, threads where someone
else already answered. Count them by type rather than listing them all,
and name the two largest sources.

Unclear. Messages where I cannot tell whether an ask is aimed at me.
List these individually with the sentence that made it ambiguous. This
bucket is more useful than the first one.

Then two lines at the end.

Oldest unanswered ask, with its date.
What I could not read: folders, threads or attachments you could not
open.

Rules. Order the first two buckets by deadline, then by how long the
sender has waited. Do not draft replies. Do not archive, label, flag,
mark as read, or move anything.
```

## Before you run it

- Enable the mail connector and give a start date. Without one, triage runs over everything and the useful buckets get buried.
- This prompt deliberately writes nothing. If you want drafts as well, use `reply-drafts-for-review`, which asks for approval before it creates anything.

## What you get

A plan for the next hour, ordered by who is actually blocked, and an Unclear bucket that usually holds the message you would have missed.

## Boundaries

It reads and sorts. It does not reply, archive, flag or mark anything, and it does not decide what deserves your time. The plan is a draft view of your mailbox, not an action taken on it.
