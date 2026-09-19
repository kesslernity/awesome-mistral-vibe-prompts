---
name: regex-explain
mode: chat
category: technical
summary: Explain a regular expression piece by piece, with examples that match, examples that do not, and the cases where it will surprise you.
use_when: Use when you are about to trust a pattern somebody else wrote, or one you wrote a month ago.
inputs:
  - The pattern, and the flavour or language if you know it
  - What it is supposed to match
writes: none
outputs: A piece by piece reading, matching and non-matching examples, the surprises, and flavour differences.
---

# Regex explain

## Prompt

```text
Explain this regular expression.

Pattern:
PASTE IT
Flavour or language, if I know it: WHICH.
What it is supposed to match: WHAT.

Five parts.

One sentence. What it matches overall.

Piece by piece. A table: the fragment, what it does, and what it would
match on its own. Include anchors, groups, escapes and every quantifier.

Matches. Five example strings it accepts, chosen to include at least
one that is surprising.

Does not match. Five example strings it rejects, chosen to include the
near misses people expect it to accept. This is the useful half.

Surprises. Where it will not behave as the author intended. Look
specifically at: a dot matching more than expected, a greedy quantifier
running past its intended stop, a missing anchor allowing a partial
match anywhere in the string, a character class that quietly includes
something, and any construct that could backtrack badly on a long
input.

Then one line on flavour. Whether the pattern behaves differently in
another common flavour, and which construct causes the difference.

You cannot execute anything here, so derive every example from the
pattern and say if one is uncertain. Then tell me which of the examples
I should actually run to confirm.
```

## Before you run it

- Say what it is meant to match. Half the value is in the gap between intent and behaviour, and without the intent there is no gap to find.
- Chat cannot run the pattern. The last line exists because the examples are reasoned rather than tested, and a two minute test settles them.

## What you get

A fragment by fragment reading, examples on both sides chosen to be informative rather than easy, and a named list of the ways the pattern can misbehave.

## Boundaries

It does not execute the pattern or test it against your data. Every example is a draft prediction, and the ones flagged as uncertain are the ones to run yourself.
