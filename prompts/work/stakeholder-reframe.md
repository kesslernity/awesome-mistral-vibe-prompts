---
name: stakeholder-reframe
mode: work
category: comms
summary: Reframe the same material for a named audience, showing what was cut and what claim each audience is being asked to accept.
use_when: Use when one piece of work has to be told to a second audience and you want the translation visible rather than invisible.
inputs:
  - The original material
  - Who the new audience is and what decision they face
writes: none
outputs: The reframed piece, a table of what was cut, added or softened, and the single claim the audience must accept for it to work.
builtin_overlap: stakeholder-translator
---

# Stakeholder reframe

## Prompt

```text
Reframe the material I am giving you for a different audience.

New audience: WHO THEY ARE, what they are responsible for, what they
already know, and what decision is in front of them.
Length: LIMIT.

Return three things.

The reframed piece. Written for that audience, at that length.

The translation table. One row per change you made:
  What you cut, and why that audience does not need it.
  What you added, and where it came from. If it came from nowhere, say
  ADDED WITHOUT SOURCE, which is a flag rather than a confession.
  What you softened or sharpened, with the original wording and the new
  wording side by side.

The load bearing claim. The one thing this audience has to accept for
the piece to work, stated in a single sentence. Then say whether my
original material actually supports it, and quote the part that does.
If nothing supports it, say that plainly.

Rules. Technical detail can be cut. Certainty cannot be added. If the
original says a result is provisional, the reframe says it too, no
matter how senior the audience is.
```

## Before you run it

- Vibe Work ships a built-in `stakeholder-translator` skill for audience reframing. Use `/stakeholder-translator` when you want the rewrite; use this when you want to see what the rewrite quietly changed.
- Name the decision the audience faces, not just their job title. A reframe without a decision is a summary.

## What you get

The rewrite, an explicit diff of what happened to the meaning, and the one claim the whole piece rests on, checked against your source material.

## Boundaries

It does not decide what an audience should be told, and it does not send anything. The reframe is a draft, and the load bearing claim is there so a human can check it before standing behind it.
