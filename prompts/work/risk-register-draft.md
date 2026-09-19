---
name: risk-register-draft
mode: work
category: planning
summary: Turn your material into a draft risk register where every risk carries the evidence it was inferred from.
use_when: Use when you need a first risk register for a project and want it built from what people actually wrote rather than from a generic list.
inputs:
  - Project documents, plans, threads or notes
writes: none
outputs: One row per risk with its evidence quoted, its owner blank, and blank likelihood and impact cells for a human to score.
---

# Risk register draft

## Prompt

```text
Draft a risk register for PROJECT NAME from the material I am giving
you.

One row per risk:

  ID. Sequential.
  Risk. Written as a condition and a consequence: if CONDITION then
  CONSEQUENCE. Not a one word topic.
  Evidence. The quote from my material that this came from, with its
  source and date. A risk with no quote goes in a separate list at the
  end called Inferred, not in this table.
  Category. Delivery, technical, supplier, people, regulatory,
  financial, or operational.
  Early signal. What would be visible first if this started happening,
  and where someone would see it.
  Existing mitigation. Only what the material says is already in place,
  quoted. NONE STATED where there is nothing.
  Likelihood. Leave blank.
  Impact. Leave blank.
  Owner. Leave blank.

Then two sections.

Inferred. Risks that are plainly there but that nobody wrote down,
each with the reasoning. Clearly separated from the table above,
because the table is evidence and this is not.

Where the material is quiet. Areas a project like this usually carries
risk in, where my material says nothing at all. Name the area and the
question rather than inventing the risk.

Rules. Leave likelihood, impact and owner blank. Scoring a risk is a
judgement with consequences, and it belongs to the people who own the
project. Do not merge two risks with different consequences.
```

## Before you run it

- Give it the messy material as well as the plan. Threads carry the risks that documents smooth over.
- The blank scoring columns are deliberate. Fill them in a room with the owners rather than accepting a number that arrived pre filled.

## What you get

A register where every row can be traced to a sentence someone wrote, a clearly separate list of inferred risks, and a map of where your material is silent.

## Boundaries

It does not score, rank or accept risk, and it is not a safety assessment of any kind. Nothing in it authorises work, clears a hazard or signs anything off. The register is a draft for the people accountable for the project.
