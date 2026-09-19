---
name: analogy-check
mode: chat
category: explaining
summary: Test an analogy you are about to use by finding where it holds, where it breaks, and what a listener would wrongly conclude.
use_when: Use when you are about to build an explanation or a pitch on a comparison.
inputs:
  - The analogy, stated as X is like Y
  - Who will hear it and what you want them to conclude
writes: none
outputs: Where it holds, where it breaks, the wrong conclusions it invites, and two alternatives.
---

# Analogy check

## Prompt

```text
Test this analogy before I use it.

Analogy: X IS LIKE Y.
Audience: WHO.
What I want them to take away: THE POINT.

Four sections.

Where it holds. The specific mappings that are true: this part of X
corresponds to that part of Y, and the relationship between them is the
same in both.

Where it breaks. The mappings that fail. Be specific about which
property does not carry over.

What they will wrongly conclude. Given the break points, the
conclusions a reasonable listener will draw that are false. This is the
section that decides whether to use the analogy at all.

Does it carry my point. Yes or no, and which part of the analogy is
doing the work. If the analogy is decorative, say so, because a
decorative analogy costs attention and returns nothing.

Then give me two alternatives from domains this audience knows better,
each with its own single strongest break point so I can compare
honestly.
```

## Before you run it

- Name the audience. An analogy from cooking works differently in a room of engineers than in a room of lawyers, and the break points that matter depend on what the room knows well.
- If the wrong conclusions section is longer than the holds section, use the plain explanation instead.

## What you get

A map of where your comparison is doing real work, where it misleads, and two alternatives with their own weaknesses stated.

## Boundaries

It does not know how your audience thinks or what comparisons they have heard before. The check is a draft, and the wrong conclusions list is a prediction rather than a finding.
