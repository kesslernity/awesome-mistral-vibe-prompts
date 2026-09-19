---
name: jargon-decode
mode: chat
category: explaining
summary: Decode the unfamiliar terms in a piece of text, separating the ones with a real definition from the ones that are context dependent.
use_when: Use when you are reading something in an unfamiliar area and half the nouns are doing unknown work.
inputs:
  - The text containing the jargon
  - The field it comes from, if you know it
writes: none
outputs: A term table with plain meanings and confidence, a list of terms that mean different things in different places, and one plain paragraph.
---

# Jargon decode

## Prompt

```text
Decode the terms in the text below.

Field, if I know it: WHICH.

A table: the term, what it means in plain words, and why it is in this
sentence rather than a simpler word. Include acronyms, and include
ordinary words being used in a special sense, which are the ones that
actually cause the confusion.

Then a confidence column. HIGH if the term has one standard meaning in
this field. MEDIUM if the meaning depends on the organisation or the
vendor. LOW if you are inferring it from context. Anything below HIGH
says what it would depend on.

Then two short sections.

Means different things in different places. Terms where two teams would
answer differently. Give both readings. Say which one fits the
sentence, and say if you cannot tell.

Doing no work. Terms that could be deleted from the sentence without
changing what it says.

Finally, one paragraph: the whole text with the jargon gone, same
meaning.

You have no access to anything beyond what I pasted. Where a term is
specific to an organisation you cannot see, say so rather than
inventing a definition.

TEXT:
```

## Before you run it

- Name the field if you know it. The same three-letter acronym has a different expansion in finance, engineering and HR, and a wrong expansion reads perfectly plausible.
- Take the confidence column seriously. MEDIUM means go and ask somebody rather than quote the definition back in a meeting.

## What you get

A term by term reading with its uncertainty marked, the terms that will cause a misunderstanding between two teams, and a plain version of the whole passage.

## Boundaries

It does not know your organisation's internal vocabulary and it cannot look anything up while it answers. Every definition is a draft reading, and the ones marked below HIGH need a human who knows the field.
