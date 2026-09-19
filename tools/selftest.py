#!/usr/bin/env python3
"""Prove the checker catches what it claims to catch, and nothing else.

Every rule in tools/verify.py gets one deliberately broken file here. The
test asserts two things per case: the rule fires on the broken file, and
the baseline it was built from is clean. The second half matters as much
as the first, because a rule that fires on a correct file is a rule that
will be silenced later.

Cases with an expected rule of None are negative controls: a mutation that
looks like the thing a rule catches but is not, and must stay clean. The
write rule needs them most, because most write verbs have a harmless
reading and a rule that cannot tell the two apart is worse than no rule.

    python3 tools/selftest.py
"""

import importlib.util
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location(
    "verify", os.path.join(ROOT, "tools", "verify.py"))
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)

WORK = """---
name: NAME
mode: work
category: comms
summary: A one line summary of what this prompt does.
use_when: Use when you need a baseline file for the self test.
inputs:
  - The material
writes: none
outputs: A thing.
---

# Baseline

## Prompt

```text
Do the thing with the material.
```

## Before you run it

- Something worth knowing first.

## What you get

A thing.

## Boundaries

It does not decide anything. The output is a draft.
"""

SCHEDULED = WORK.replace("mode: work", "mode: scheduled").replace(
    "Do the thing with the material.",
    "Read the material since this task last ran. Read only.")

CHAT = WORK.replace("mode: work", "mode: chat")


def rep(old, new):
    return lambda t: t.replace(old, new, 1)


# (case name, expected rule, mode, mutation)
CASES = [
    ("no front matter", "F1", "work", lambda t: t.split("---\n", 2)[2]),
    ("front matter never closed", "F1", "work",
     lambda t: t.replace("---\n\n# Baseline", "\n# Baseline", 1)),
    ("indented line that is not a list item", "F1", "work",
     rep("outputs: A thing.", "outputs:\n  A thing.")),
    ("front matter line with no colon", "F1", "work",
     rep("outputs: A thing.", "outputs")),
    ("duplicate front matter key", "F1", "work",
     rep("outputs: A thing.", "outputs: A thing.\noutputs: Another thing.")),
    ("missing required key", "F2", "work", rep("category: comms\n", "")),
    ("empty required key", "F2", "work", rep("outputs: A thing.", "outputs:")),
    ("unknown key", "F2", "work",
     rep("outputs: A thing.", "outputs: A thing.\nauthor: somebody")),
    ("name does not match the file", "F3", "work",
     rep("name: NAME", "name: something-else")),
    ("name is not kebab case", "F3", "work", "RENAME:Not_Kebab"),
    ("mode is not one of the three", "F4", "work",
     rep("mode: work", "mode: agent")),
    ("mode does not match the folder", "F4", "work",
     rep("mode: work", "mode: chat")),
    ("category is not kebab case", "F5", "work",
     rep("category: comms", "category: Comms And Things")),
    ("summary over 160 chars", "F6", "work",
     rep("summary: A one line summary of what this prompt does.",
         "summary: " + "a" * 161)),
    ("use_when does not open with Use when", "F7", "work",
     rep("use_when: Use when", "use_when: Helps with")),
    ("inputs is not a list", "F8", "work",
     rep("inputs:\n  - The material", "inputs: the material")),
    ("writes is neither none nor a list", "F9", "work",
     rep("writes: none", "writes: maybe")),
    ("a heading is missing", "F10", "work",
     rep("## What you get\n\nA thing.\n\n", "")),
    ("headings out of order", "F10", "work",
     rep("## Before you run it\n\n- Something worth knowing first.\n\n"
         "## What you get\n\nA thing.\n\n",
         "## What you get\n\nA thing.\n\n"
         "## Before you run it\n\n- Something worth knowing first.\n\n")),
    ("two fenced blocks", "F11", "work",
     rep("## What you get\n\nA thing.",
         "## What you get\n\n```text\nstray\n```")),
    ("fenced block tagged something else", "F11", "work",
     rep("```text", "```markdown")),
    ("duplicate name across the library", "F12", "work", "DUPLICATE"),
    ("builtin_overlap is not a Work built-in", "F13", "work",
     rep("writes: none", "builtin_overlap: contract-review\nwrites: none")),
    ("builtin_overlap never mentioned", "F13", "work",
     rep("writes: none", "builtin_overlap: meeting-prep\nwrites: none")),
    ("scheduled prompt declares a write", "M1", "scheduled",
     rep("writes: none", "writes:\n  - Sends a summary")),
    ("write verb in an unattended prompt", "M2", "scheduled",
     rep("Read only.", "Read only. Then send me the summary.")),
    ("unattended prompt writes to a connector", "M2", "scheduled",
     rep("Read only.", "Read only.\nCreate a Linear issue for each one.")),
    ("unattended prompt posts to a channel", "M2", "scheduled",
     rep("Read only.", "Read only.\nPost the digest in the Slack channel.")),
    ("unattended prompt updates a ticket", "M2", "scheduled",
     rep("Read only.", "Read only.\nUpdate the Jira ticket afterwards.")),
    # Negative controls. A write verb aimed at the conversation is not a
    # write, and these must stay clean or the rule is unusable.
    ("a table is not a write", None, "scheduled",
     rep("Read only.", "Read only.\nCreate a table of what moved.")),
    ("a brief is not a write", None, "scheduled",
     rep("Read only.", "Read only.\nWrite a one page brief of the week.")),
    ("share of spend is not a share action", None, "scheduled",
     rep("Read only.", "Read only.\nGive each vendor's share of spend.")),
    ("a sender is a reader", None, "scheduled",
     rep("Read only.", "Read only.\nGive the sender and the subject.")),
    ("scheduled prompt never says it changes nothing", "M3", "scheduled",
     rep(" Read only.", "")),
    ("chat prompt declares a write", "M4", "chat",
     rep("writes: none", "writes:\n  - Creates a draft")),
    ("chat prompt names a connector", "M5", "chat",
     rep("- The material", "- The material in Slack")),
    ("chat prompt reaches for the web", "M6", "chat",
     rep("Do the thing", "Browse for the thing and do the thing")),
    ("work write with no approval in Boundaries", "M7", "work",
     rep("writes: none", "writes:\n  - Creates a draft message")),
    ("em dash", "H1", "work", rep("A thing.", "A thing — a good one.")),
    ("safety authorisation language", "H2", "work",
     rep("Do the thing", "Decide the permit to work and do the thing")),
    ("Boundaries never says draft", "H3", "work",
     rep("The output is a draft.", "The output is yours.")),
    ("Boundaries has no It does not sentence", "H3", "work",
     rep("It does not decide anything.", "Nothing is decided here.")),
    ("prompt block over 2500 chars", "W1", "work",
     rep("Do the thing with the material.", "Do it. " * 400)),
    ("use_when over 200 chars", "W2", "work",
     rep("use_when: Use when you need a baseline file for the self test.",
         "use_when: Use when " + "x" * 200)),
    ("prompt line over 78 chars", "W3", "work",
     rep("Do the thing with the material.", "Do the thing. " * 8)),
]

BASELINES = {"work": WORK, "scheduled": SCHEDULED, "chat": CHAT}


def run_one(tmp, mode, text, name="case-file", extra_seen=None):
    d = os.path.join(tmp, mode)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, name + ".md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text.replace("NAME", name))
    fails, warns = [], []
    verify.check_file(path, "%s/%s.md" % (mode, name), True, fails, warns,
                      dict(extra_seen or {}))
    return [f[1] for f in fails] + [w[1] for w in warns]


def main():
    tmp = tempfile.mkdtemp(prefix="vibe-prompts-selftest-")
    bad = 0

    # The baselines themselves must be clean, or every case below proves
    # nothing.
    for mode, text in BASELINES.items():
        rules = run_one(tmp, mode, text, "baseline-" + mode)
        if rules:
            print("FAIL baseline %s is not clean: %s" % (mode, rules))
            bad += 1

    for label, expect, mode, mutate in CASES:
        text = BASELINES[mode]
        seen = {}
        name = "case-file"
        if isinstance(mutate, str):
            if mutate.startswith("RENAME:"):
                name = mutate.split(":", 1)[1]
                text = BASELINES[mode].replace("name: NAME",
                                               "name: " + name)
                # keep the file name equal to the declared name so only the
                # kebab rule can fire
                rules = run_one(tmp, mode, text.replace("NAME", name), name)
                got = rules
            elif mutate == "DUPLICATE":
                seen = {"case-file": "prompts/work/case-file.md"}
                got = run_one(tmp, mode, text, name, seen)
            else:
                raise SystemExit("unknown string mutation %r" % mutate)
        else:
            got = run_one(tmp, mode, mutate(text), name)

        if expect is None:
            if got:
                print("FAIL %-44s expected nothing, got %s" % (label, got))
                bad += 1
        elif expect not in got:
            print("FAIL %-44s expected %s, got %s"
                  % (label, expect, got or "nothing"))
            bad += 1

    print()
    print("%d selftest cases, %d failed" % (len(CASES) + len(BASELINES), bad))
    if not bad:
        controls = sum(1 for c in CASES if c[1] is None)
        print("Every rule fires on a file that breaks it, and on none of "
              "the three clean baselines or the %d negative controls."
              % controls)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
