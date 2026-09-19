---
name: rollout-plan-draft
mode: work
category: planning
summary: Draft a staged rollout plan with entry and exit criteria per stage, and a named list of what is not yet decided.
use_when: Use when a change has to reach a population in stages and you need a first plan that makes the unknowns visible.
inputs:
  - What is being rolled out, to whom, and by when
  - Any constraint document: change windows, approvals, training, licences
writes: none
outputs: A stage table with entry and exit criteria, a rollback line per stage, and separate Assumptions, Dependencies and Open decisions lists.
---

# Rollout plan draft

## Prompt

```text
Draft a staged rollout plan.

What: WHAT IS CHANGING.
Who: POPULATION, and its size if I gave you one.
By: DATE.
Constraints: LIST, or none stated.

Return a stage table. Suggest the stages rather than assuming mine:

  Stage. Name and the slice of the population it covers.
  Entry criteria. What must be true before this stage starts. Testable
  conditions, not intentions.
  What happens. The actions, in order.
  Exit criteria. What must be true before the next stage starts, with
  the measure and who reads it.
  Rollback. What undoes this stage, how long it takes, and what cannot
  be undone. Every stage has this row, and "not possible" is a valid
  and important answer.
  Duration. Your estimate, with the basis for it. An estimate with no
  basis is written as UNKNOWN.

Then three lists.

Assumptions. Everything you had to assume because I did not say it.
Number them.

Dependencies. What has to come from somebody else, who, and by when.

Open decisions. Choices in this plan that are mine to make, stated as
questions with the options. Do not resolve them.

Rules. Do not compress the plan to fit the date. If the stages do not
fit, say which stage the date breaks and by how much. Do not schedule
a stage over a stated constraint.
```

## Before you run it

- Give the constraints as text, including the ones that feel obvious. Change windows and approval lead times are what make a plan real.
- Expect the Assumptions list to be long on the first run. Answering three of them and running again beats editing the plan by hand.

## What you get

A plan where each stage has a testable exit criterion and a rollback line, and three lists that tell you what the plan is standing on.

## Boundaries

It does not approve the change, schedule anything, or decide the risk appetite. Nothing here authorises work of any kind, and a rollback line is a draft plan rather than a tested procedure. A human owns the plan and the decisions in it.
