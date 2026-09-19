---
name: tighten-this
mode: chat
category: writing
summary: Cut a piece of writing to a stated length and show what was lost, so you can judge the trade rather than accept it.
use_when: Use when something you wrote is too long and you want the cut shown rather than hidden.
inputs:
  - The text to cut
  - The target length
writes: none
outputs: The tightened text at the target length, a list of what was cut, and anything that could not be cut without losing meaning.
---

# Tighten this

## Prompt

```text
Cut the text below to WORDS words. Keep my voice.

Return three things.

The tightened text.

What went, as a list. Each line names what you removed and why:
repetition, hedging, a detail the reader does not need, a sentence that
restated the one before it.

What I would lose if you cut further. One or two items, quoted from the
original, that are carrying the argument rather than decorating it.

Rules. Do not add a single fact, number or claim that is not already
there. Do not make a hedged sentence certain. If the text cannot reach
the target without losing something load bearing, say so, give me the
shortest honest version, and tell me its length.

TEXT:
```

## Before you run it

- Give a number, not "shorter". Without a target the cut lands wherever the model feels like stopping.
- The third section is the one to read. It tells you where the next cut would start costing you.

## What you get

A shorter version at the length you asked for, and an explicit account of what left, so the edit is yours to accept rather than a rewrite you have to reverse engineer.

## Boundaries

It does not fact check, and a hedge removed by accident is your problem to catch. The result is a draft edit of your own words, and nothing here changes what the text claims.
