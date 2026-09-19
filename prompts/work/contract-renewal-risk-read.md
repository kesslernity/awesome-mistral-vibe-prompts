---
name: contract-renewal-risk-read
mode: work
category: documents
summary: Read a contract before a renewal and return the dates, the money, the exits and the clauses that move without you.
use_when: Use when a contract is coming up for renewal and you need the mechanical terms in front of you before any conversation with the vendor.
inputs:
  - The contract, and any amendment or order form attached to it
writes: none
outputs: A table of the mechanical terms with clause references, plus Automatic behaviour, Questions for the vendor, and Not in this document.
builtin_overlap: document-review
---

# Contract renewal risk read

## Prompt

```text
Read the attached contract and its amendments. Today is DATE and the
renewal is on or around DATE.

Return four parts.

Mechanical terms. A table, one row per term, with the value and the
clause number it came from. Cover at least: term start and end, notice
period and how notice must be served, automatic renewal and its length,
price and any uplift formula, minimum commitment, termination for
convenience, termination for cause and its cure period, liability cap,
data location and deletion on exit, assignment on change of control.
Where the contract is silent, write NOT PRESENT. Where an amendment
changes a clause, show the amended value and cite both documents.

Automatic behaviour. What happens if nobody does anything: the dates
that pass, the notice window that closes, the price that changes. Give
the actual calendar dates, computed from the dates in the document, and
show the computation.

Questions for the vendor. Specific questions raised by what you read,
each tied to its clause. Not general advice.

Not in this document. Terms you looked for and did not find, and
anything that refers to a document you were not given.

Rules. Quote the clause wording where the meaning turns on it. Do not
tell me whether the terms are good or standard. Do not draft a message
to the vendor.
```

## Before you run it

- Vibe Work ships a built-in `document-review` skill. Use `/document-review` for a general read of a document; this prompt is the narrower one, aimed at the dates and the clauses that move money.
- Attach every amendment and order form. A renewal clause amended once and then amended again is the usual source of a wrong date.
- State today's date in the prompt. The automatic behaviour section is only useful if the arithmetic starts from the right day.

## What you get

The mechanical terms in one table with clause references, and a set of calendar dates that tell you how long you actually have.

## Boundaries

This is not legal advice. It does not tell you whether to renew, and it does not negotiate. It reads what the document says and names what the document does not, and the result is a draft read for a qualified reviewer to check before you rely on any of it.
