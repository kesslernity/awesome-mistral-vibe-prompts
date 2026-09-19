---
name: options-table
mode: chat
category: thinking
summary: Lay out the options against criteria you name, with an evidence column that shows which cells are actually known.
use_when: Use when a choice has drifted into a conversation and nobody has written the options next to each other.
inputs:
  - The options
  - The criteria that matter and what the decision is
writes: none
outputs: A comparison table with an evidence basis per cell, what would change the answer, and the option that was not listed.
---

# Options table

## Prompt

```text
Lay these options out against these criteria.

Decision: WHAT IS BEING DECIDED, and by when.
Options: LIST.
Criteria that matter: LIST, in rough order of importance.
What I know: ANY FACTS, COSTS, DATES OR CONSTRAINTS.

The table: options as rows, criteria as columns.

Every cell carries two things: the assessment, and its basis. Basis is
STATED if it came from what I gave you, INFERRED if you reasoned it
from something I gave you, or UNKNOWN. Do not fill an UNKNOWN cell with
a plausible value, and do not quietly drop a criterion because the
table is thin there. A column full of UNKNOWN is the most useful thing
this table can show me.

Then four short sections.

What would change the answer. The one or two facts that, if known,
would shift the choice. Ordered by how cheap they are to find out.
Not comparable. Where a criterion means something different for
different options, so the column is misleading.
Reversibility. For each option, how hard it is to undo and roughly how
long you would have to notice.
The option not on my list. If there is an obvious one I did not name,
including doing nothing for now, add it as a row and say why.

Do not recommend one. Do not score or weight them into a total. A
single number hides exactly the judgement I am here to make.
```

## Before you run it

- List your criteria yourself. Letting the model choose them is how a decision quietly gets made before you see the table.
- Read the UNKNOWN cells before the assessments. They tell you whether this is a decision or a research task.

## What you get

The options side by side, with every cell marked as known, inferred or unknown, and the cheap facts that would settle it named.

## Boundaries

It does not recommend, score or decide, and an INFERRED cell is the model's reasoning rather than a fact. The table is a draft frame for a decision that stays yours.
