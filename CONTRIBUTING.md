# Contributing

Short version: **a prompt here has to be honest about the mode it runs in.**
This library makes one claim, that nothing in `prompts/scheduled/` asks to act
while nobody is watching and nothing in `prompts/chat/` reaches for a connector
or for retrieval, both of which Mistral documents under Work. Every contribution either keeps that claim true or
it does not land.

## The loop

```bash
python3 tools/verify.py --house      # format rules, mode rules, house rules
python3 tools/selftest.py            # proves each rule fires on a broken file
python3 tools/manifest.py            # regenerates MANIFEST.json and the tables
python3 tools/manifest.py --check    # what CI runs
```

Standard library only, any `python3`. The front matter parser lives in
`tools/verify.py` precisely so the repository has no dependency and no minimum
version to argue about.

## Adding a prompt

1. **Pick the mode honestly.** If it needs a connector it is not Chat. If it
   needs a person to approve something it is not scheduled. The folder is the
   claim, and the checker holds you to it.
2. **Write the file** to the shape in [`docs/WRITING-PROMPTS.md`](docs/WRITING-PROMPTS.md).
   Wrap the prompt block at 78 columns.
3. **Run it.** Actually run it, in the mode it claims, against real material.
   A prompt nobody has run is a piece of writing about a prompt.
4. **Write "Before you run it" from what went wrong the first time.** That
   section exists because these prompts have preconditions, and the precondition
   is usually what you got wrong on the first attempt.
5. **Write Boundaries last, and make it true.** A sentence starting "It does
   not", and the word draft. If you cannot write an honest one, the prompt is
   claiming more than it does.
6. `python3 tools/manifest.py`, then the full loop, then commit.

## Changing a rule

Rules live in `tools/verify.py` and each one has an identifier, F1 to F13, M1
to M7, H1 to H3, W1 to W3. If you add or change one:

**Add its case to `tools/selftest.py` in the same commit.** One deliberately
broken file that the rule catches. The selftest also asserts the three clean
baselines stay clean, which is the half that catches a rule that is too eager.

If your rule looks for a word, add a negative control in the same commit: a
case whose expected rule is `None`, using the same word in the harmless way.
The write rule has four, because "create a table" and "create a Linear issue"
are the same verb and only one of them is a write. A rule with no negative
control is a rule nobody can safely tighten later.

The WARN doctrine: a WARN never fails the build, and **if a WARN fires on a
file that is right, the rule is wrong.** Fix the rule rather than bending the
file to it. The three warnings today are prompt block length, `use_when`
length and prompt line width, and all three are guides rather than limits.

The FAIL doctrine is the opposite: a FAIL means the file makes a claim it
cannot keep. The temptation when a file fails M2 is to reword the prompt until
the write verb is gone. That is only correct if the prompt genuinely does not
write. If it does, it belongs in `prompts/work/` with its write declared.

## Who owns what

| File | Owns | Edited by hand |
|---|---|---|
| `prompts/**/*.md` | the prompts, and the front matter that describes them | yes |
| `tools/verify.py` | every rule, and the front matter parser | yes |
| `tools/selftest.py` | one broken case per rule, plus three clean baselines and the negative controls | yes |
| `tools/manifest.py` | `MANIFEST.json` and the generated README tables | yes |
| `MANIFEST.json` | nothing, it is output | **no** |
| `README.md` tables and counts | nothing, they are output | **no**, the prose around them yes |

Anything between `<!-- BEGIN:... -->` and `<!-- END:... -->`, or between a
`<!-- n-something:start -->` pair, is generated. `tools/manifest.py --check`
fails if a hand edit is sitting in one.

## House rules

Four, and they are not negotiable in a pull request.

1. **AI prepares, humans decide.** No prompt advises using an agent for safety
   authorisation: permit to work, isolation and lockout, confined space entry,
   job safety analysis, incident classification, inspection sign off. Rule H2
   greps for the language, but the rule is broader than the grep, so use
   judgement as well.
2. **A scheduled task reads.** See above. This is the repository's argument, so
   a pull request that weakens it needs to make the case for the whole library,
   not for one file.
3. **Missing information is named.** Every prompt that gathers anything asks
   the model for the list of what it could not establish, in words the model is
   allowed to use. A prompt with no such escape hatch produces its most
   confident sentence exactly where it knows least.
4. **No em dashes**, and no en dashes. Rule H1.

## Versions

Product behaviour described in the README and in `docs/` was read from
Mistral's documentation on **19 September 2026**, when scheduled tasks were in
Public Preview and Work shipped twelve built-in Skills. If you find any of it
has moved, change the text and say when you checked. A dated claim that is
wrong is fixable. An undated one is not.
