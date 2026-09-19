---
name: doc-change-watch
mode: scheduled
category: documents
summary: A weekly read on which documents in a named space changed, who changed them, and which ones are overdue a review.
use_when: Use when a policy or procedure space matters and nobody is watching what quietly changed in it.
inputs:
  - Google Drive, SharePoint or Notion, and the specific space or folder
writes: none
outputs: Changed documents with author and date, an Overdue review list, and a No owner list.
---

# Doc change watch

## Prompt

```text
Watch the document space below for changes since this task last ran.
Read only. Change no document.

Space: WHERE, and the folder, site or database.
Review period: documents are due a review every MONTHS months.

Three sections.

Changed. One line per document: title, link, who changed it, when, and
what changed if the version history says. If the history shows only
that an edit happened, write EDIT RECORDED, DETAIL NOT AVAILABLE rather
than guessing at the content.

Overdue review. Documents whose last substantive change is older than
the review period. Show the age in months, oldest first, and the owner
if the document names one.

No owner. Documents with no owner recorded anywhere in the file or its
properties. These are the ones that go stale without anybody noticing.

Then one line: how many documents you could not open, and why.

Rules. Do not judge whether a change was correct. Do not summarise a
document's content unless it changed. An empty section is written as
one line saying it is empty.
```

## Before you run it

- Point it at one space. A watch over an entire drive produces a list nobody reads by week three.
- Set the review period to whatever your own policy says. If there is no policy, the Overdue list is your first draft of one.

## What you get

A weekly note on what moved in a space that is supposed to be stable, and two lists that show where ownership has quietly lapsed.

## Boundaries

It does not open, edit, rename or file anything, and it does not judge whether a change was right. The watch is a draft list for the document owners to read.
