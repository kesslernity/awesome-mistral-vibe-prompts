# Writing a prompt for this library

Every file in `prompts/` has the same shape, and `tools/verify.py` enforces
most of it. This page is the reference for the parts a checker cannot judge.

## The file

````markdown
---
name: kebab-case-matching-the-file-name
mode: work | scheduled | chat
category: kebab-case
summary: One sentence, 160 characters or fewer.
use_when: Use when ...
inputs:
  - What the reader has to supply or connect
writes: none
outputs: What comes back.
builtin_overlap: meeting-prep      # optional
---

# Title

## Prompt

```text
The prompt itself, wrapped at 78 columns, with CAPITALISED placeholders.
```

## Before you run it

## What you get

## Boundaries
````

## The keys

| Key | Rule | Notes |
|---|---|---|
| `name` | required, kebab, 1 to 64 chars, equal to the file name | unique across the whole library |
| `mode` | required, one of `work`, `scheduled`, `chat` | must match the folder |
| `category` | required, kebab, 32 chars | groups the generated README tables |
| `summary` | required, 160 chars | one sentence, no trailing context |
| `use_when` | required, opens with "Use when" | this becomes the Skill description, so it is a trigger rather than a description |
| `inputs` | required, a list | what the reader supplies: a document, a connector, a target length |
| `writes` | required, `none` or a list | a list means the prompt causes a write, and each entry names it |
| `outputs` | required | what the reader gets back |
| `builtin_overlap` | optional | one of Work's twelve built-in Skills, and it must be mentioned in "Before you run it" |

## The four sections

**`## Prompt`** holds exactly one fenced block tagged `text`. One block, so
there is no ambiguity about what to copy. Wrap at 78 columns: the block is read
in a terminal, a diff and a chat input, and none of them wrap it kindly.

**`## Before you run it`** is the precondition section. It is the most useful
part of most files, because almost every one of these prompts has a single
input that decides whether the output is worth anything: the denominator, the
definitions document, the real deadline, what the reader already knows. Say
that. Do not restate the prompt.

**`## What you get`** is two or three sentences on the shape of the output and
which part of it to read first.

**`## Boundaries`** says what the prompt does not do, in a sentence that starts
"It does not", and uses the word draft. This is checked, because it is the
section a reader skips and the section that matters when the output is wrong.

## What a good prompt asks for

The prompts here share a set of moves. They are not style: each one is there
because it changes what comes back.

- **Ask for the denominator before the finding.** A share with no stated total
  cannot be checked, and a model will produce one happily.
- **Ask for the arithmetic to be shown.** Any date subtraction, any difference,
  any percentage. A visible subtraction is a checkable subtraction.
- **Give it a name for "I could not establish this".** NOT STATED, NO DATE ON
  PAGE, NO REASON RECORDED, NO ANSWER IN WHAT YOU GAVE ME. A model that has no
  sanctioned way to say nothing will invent something plausible, and the
  invention will be the most fluent sentence in the output.
- **Ask for the negative list explicitly.** What was not covered, what could
  not be read, which pages failed. A failed read that quietly lands in "no
  change" is the single most expensive defect in a monitoring prompt.
- **Separate what was stated from what was inferred**, and make the model mark
  each one. STATED, INFERRED, UNKNOWN beats a confident table every time.
- **Forbid the conclusion you did not ask for.** No recommendation, no
  severity, no sentiment score, no health colour, no forecast. Most of these
  prompts end with a short list of things not to do, and that list is what
  keeps the output usable by the person who owns the decision.
- **Say what not to invent.** Where a prompt drafts anything, ask for an
  explicit list of everything the draft contains that the source material did
  not.

## Mode is a constraint, not a label

Before writing, decide which mode this belongs in, and then respect what that
mode can actually do.

- **Work** has connectors and a person watching. It may gather, compare and
  draft. If it writes, `writes:` lists the write and the Boundaries section
  says the approval prompt will appear.
- **Scheduled** is Work with nobody watching. It reads and reports. No write
  verb, `writes: none`, and the prompt block itself says it changes nothing.
  Write the prompt so that a run six months from now is still bounded: name the
  period, name the sources, cap the length.
- **Chat** is where the prompt works on what you paste. Connectors and
  retrieval are documented under Work, so a prompt that needs either is a Work
  prompt, whatever it is about. This is a filing rule rather than a claim about
  what Chat can do, and the checker enforces it as one. Where the reasoning
  depends on something the model cannot run, say so inside the prompt and ask
  it to mark which of its outputs need running.

## Adding one

1. Pick the mode, and put the file in `prompts/<mode>/`.
2. Name the file after the `name`.
3. Write it. Wrap the prompt block at 78 columns.
4. `python3 tools/verify.py --house prompts/<mode>/<name>.md`
5. `python3 tools/manifest.py` to regenerate `MANIFEST.json` and the README
   tables. Never edit either by hand.
6. `python3 tools/verify.py --house && python3 tools/selftest.py &&
   python3 tools/manifest.py --check` before you commit.

If you find yourself wanting to relax a rule so a file passes, read
[`CONTRIBUTING.md`](../CONTRIBUTING.md) first. Sometimes the rule is wrong, and
then it gets fixed and gains a selftest case. Usually the file is.
