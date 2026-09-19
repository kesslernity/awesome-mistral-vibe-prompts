---
name: reply-drafts-for-review
mode: work
category: inbox
summary: Create unsent reply drafts for a named set of messages, one at a time, with a stated reason for each.
use_when: Use when you have triaged your mail and want the routine replies written but not sent.
inputs:
  - Gmail, where drafting is the documented ceiling
writes:
  - Creates draft messages in the mail client. Work asks for approval before each write.
outputs: One unsent draft per message, plus a table of what each draft commits you to and which ones were left for you to write.
---

# Reply drafts for review

## Prompt

```text
For the messages I list below, create a reply DRAFT for each. Do not
send anything. Do not mark anything as read.

Messages: LIST, by sender and subject.

For each one, before you create the draft, show me:
  Who it is to, and the subject.
  The ask, quoted from their message.
  The reply in full.
  What it commits me to: a date, a decision, an opinion, or nothing.

Then create the draft and tell me it exists and where.

Write the replies short. Answer the ask, confirm the next step and its
date, and stop. No pleasantries I did not ask for.

Three things you never do in a draft. You never agree to a date that
is not already in my calendar or my message. You never state a position
on a decision I have not told you I have taken. You never apologise on
my behalf.

If a message needs any of those three, do not draft it. Put it in a
list at the end called For me to write, with the reason.

At the end, a table: recipient, what the draft commits me to, and
whether I have to check a fact before sending it.
```

## Before you run it

- This prompt writes. Work asks before a connector acts on your behalf and offers Continue, Always allow and Decline. Choose Continue each time, and do not switch this one to Always allow, because the approval is the control here.
- Run it on Gmail. Mistral asks Gmail for the `gmail.compose` scope rather than `gmail.send`, and says so in as many words: drafting is the ceiling, and you send from Gmail yourself. Outlook is the other shape. Its connector is documented as "Read and send emails", and drafting is not on that list, so on Outlook the nearest documented action to the one this prompt asks for is the irreversible one. Read every approval prompt before you answer it.
- Name the messages. Pointing at a whole folder is how a mailbox fills with drafts you did not read.

## What you get

Drafts sitting in your mail client unsent, each with the ask it answers and what it would commit you to, plus a short list of the ones that were not safe to write for you.

## Boundaries

It creates drafts and never sends. It does not mark a message as read, file it or act on it in any other way, and every write it makes waits for your approval first. A draft is not a sent message, so nothing here commits you to anything until you press send yourself. Read each one, because the commitment table is a claim about the draft rather than a guarantee.
