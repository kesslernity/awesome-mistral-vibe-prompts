---
name: policy-gap-questions
mode: work
category: documents
summary: Compare a policy against a framework or standard you supply and return the gaps as questions rather than as findings.
use_when: Use when you have to review an internal policy against a framework and want the gaps in a form you can take to the owner.
inputs:
  - The policy document
  - The framework, standard or control set you are comparing against
writes: none
outputs: A control by control table with Addressed, Partly addressed, Not found, plus quoted evidence and one question per gap.
---

# Policy gap questions

## Prompt

```text
Compare the attached policy against the framework I am also attaching.

Work control by control, in the framework's order. One row each:

  Control. The identifier and its wording, from the framework.
  Status. Addressed, Partly addressed, or Not found in this document.
  Evidence. The passage from the policy that supports the status, quoted,
  with its section. Every Addressed and Partly addressed row needs a
  quote. A row with no quote is Not found.
  Question. One specific question for the policy owner. For Not found,
  the question asks where this lives if not here. For Partly addressed,
  the question names the missing part.

Then two sections.

Outside this policy. Controls that are plainly handled somewhere else,
where the policy says so and names the other document. Quote that.

What I could not assess. Controls where the framework wording is too
general to test against a document, or where the policy language is
too vague to match either way. Say which of the two it is.

Rules. Not found means not found in this document, which is not the
same as not done anywhere. Never write the word compliant. You are
comparing two documents, and that is the whole claim.
```

## Before you run it

- Attach the framework text rather than naming it. A framework recalled from memory is a framework from some other version.
- Give the policy's scope statement if it is in a separate document. Half of what looks like a gap is a scope boundary.

## What you get

A table where every positive finding carries its quote, and a question list you can send to the policy owner without rewriting it.

## Boundaries

It compares two documents and nothing else. It does not audit, it does not certify, and Not found is a statement about a file rather than about your organisation. The output is a draft for a reviewer who knows the estate.
