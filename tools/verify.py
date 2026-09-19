#!/usr/bin/env python3
"""Check every prompt file in this library.

Runs on any python3 with the standard library only. No YAML parser, no
tomllib, no 3.11 requirement: the front matter is parsed here, in about
forty lines, because the format is deliberately small enough for that.

    python3 tools/verify.py            format rules and mode rules
    python3 tools/verify.py --house    the above plus the house rules
    python3 tools/verify.py --quiet    only the summary and any findings

A FAIL exits 1. A WARN never does. If a WARN fires on a file that is
right, the rule is wrong: fix the rule, not the file.
"""

import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS = os.path.join(ROOT, "prompts")

MODES = ("work", "scheduled", "chat")

REQUIRED_KEYS = ("name", "mode", "category", "summary", "use_when",
                 "inputs", "writes", "outputs")
OPTIONAL_KEYS = ("builtin_overlap",)
ALLOWED_KEYS = REQUIRED_KEYS + OPTIONAL_KEYS

HEADINGS = ("## Prompt", "## Before you run it", "## What you get",
            "## Boundaries")

KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

# Vibe Work ships twelve built-in skills. A builtin_overlap value has to be
# one of them, because the point of the field is to send the reader to the
# thing that already exists.
BUILTIN_WORK_SKILLS = (
    "challenge-my-thinking", "data-analysis", "deep-research",
    "doc-coauthoring", "document-review", "internal-comms", "meeting-prep",
    "research-synthesis", "skill-creator", "stakeholder-translator",
    "structured-extraction", "vibe-work-onboarding",
)

# The ruler for "is this a write" is Mistral's own, from the Vibe Work
# safety-and-approvals page: an interactive tool is one that "creates,
# updates, deletes, sends, or posts data", and a read-only tool is one that
# "retrieves information (get, list, search)".
#
# A verb alone is not enough, because most of these verbs have a harmless
# reading. "Create a table of the five biggest movers" writes into the
# conversation. "Create a Linear issue" writes into Linear. So there are two
# lists. ALWAYS_WRITE fires on the verb. TARGETED_WRITE fires only when the
# verb is aimed at something that lives outside the conversation.
#
# Word boundaries are the ruler for both: "sender" is a reader and passes,
# "send" does not.
ALWAYS_WRITE = ("send", "reply", "delete", "archive", "pay", "approve",
                "merge", "revoke", "unsubscribe")
TARGETED_WRITE = ("create", "update", "modify", "post", "move", "assign",
                  "schedule", "upload", "submit", "publish", "rename",
                  "transfer", "invite", "grant", "share", "write")

# Connectors, from the Vibe Work connectors page. The mode-routing page also
# names Google Drive, which that table does not list, so both are here.
CONNECTORS = ("gmail", "outlook", "slack", "notion", "linear", "github",
              "atlassian", "jira", "confluence", "google drive",
              "google calendar", "outlook calendar", "sharepoint", "stripe",
              "box")

# Things that only exist outside the conversation. A write verb pointed at
# one of these is a write to somebody else's system.
EXTERNAL_OBJECTS = CONNECTORS + (
    "issue", "ticket", "pull request", "merge request", "email", "e-mail",
    "draft", "calendar event", "meeting invite", "channel", "canvas",
    "wiki page", "invoice", "payment", "commit", "branch", "repository",
)

def _verb_re(verbs):
    return re.compile(
        r"\b(" + "|".join(
            v + r"(s|es|ing|ed|d|ies|ied)?" for v in verbs
        ) + r")\b", re.I)

ALWAYS_WRITE_RE = _verb_re(ALWAYS_WRITE)
TARGETED_WRITE_RE = _verb_re(TARGETED_WRITE)
OBJECT_RE = re.compile(
    r"\b(" + "|".join(re.escape(o) for o in EXTERNAL_OBJECTS) + r")s?\b",
    re.I)

# How far after the verb the object may sit and still be its object.
OBJECT_WINDOW = 40


def find_write(text):
    """Return (verb, why) for the first write this text asks for, or None."""
    hit = ALWAYS_WRITE_RE.search(text)
    if hit:
        return hit.group(0), "a write verb"
    for hit in TARGETED_WRITE_RE.finditer(text):
        tail = text[hit.end():hit.end() + OBJECT_WINDOW]
        obj = OBJECT_RE.search(tail)
        if obj:
            return ("%s ... %s" % (hit.group(0), obj.group(0)),
                    "a write verb aimed outside the conversation")
    return None


READ_ONLY_RE = re.compile(r"read only|read-only|change nothing|change no ",
                          re.I)

# Mistral documents Connectors, approvals and Skills under Work. The Chat
# page names none of them. These two rules are therefore filing rules for
# this library, not claims about what Chat can do: a prompt that reaches for
# a connector or for retrieval belongs in Work, where both are documented.
WEB_PHRASES = ("search the web", "web search", "browse", "the internet",
               "online", "look it up")

# Hard rule: AI prepares, humans decide. Nothing in this library may put an
# agent anywhere near a safety authorisation.
SAFETY_RE = re.compile(
    r"\b(permit[ -]to[ -]work|lockout|loto|tagout|confined space|"
    r"job safety analysis|jsa|incident classification|"
    r"inspection sign[ -]?off|safety authorisation|safety authorization|"
    r"method statement approval)\b", re.I)

DASHES = {"—": "em dash", "–": "en dash"}


def parse_front_matter(text, rel, fails):
    """Return (dict, body) or (None, None). Scalars and simple lists only."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        fails.append((rel, "F1", "no front matter: first line is not ---"))
        return None, None
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        fails.append((rel, "F1", "front matter is never closed with ---"))
        return None, None

    data = {}
    key = None
    for n in range(1, end):
        raw = lines[n]
        if not raw.strip():
            continue
        if raw.startswith("  - "):
            if key is None:
                fails.append((rel, "F1",
                              "line %d: list item before any key" % (n + 1)))
                return None, None
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(raw[4:].strip())
            continue
        if raw[0] in " \t":
            fails.append((rel, "F1",
                          "line %d: indented line that is not a list item"
                          % (n + 1)))
            return None, None
        if ":" not in raw:
            fails.append((rel, "F1", "line %d: no colon" % (n + 1)))
            return None, None
        key, _, value = raw.partition(":")
        key = key.strip()
        value = value.strip()
        if key in data:
            fails.append((rel, "F1", "duplicate key %r" % key))
            return None, None
        data[key] = value if value else None
    return data, "\n".join(lines[end + 1:])


def sections(body):
    """Split the body on its ## headings. Returns (h1, {heading: text})."""
    h1 = None
    out = {}
    current = None
    buf = []
    for line in body.split("\n"):
        if line.startswith("# ") and h1 is None and current is None:
            h1 = line[2:].strip()
            continue
        if line.startswith("## "):
            if current is not None:
                out[current] = "\n".join(buf).strip()
            current = line.strip()
            buf = []
            continue
        buf.append(line)
    if current is not None:
        out[current] = "\n".join(buf).strip()
    return h1, out


def fenced_blocks(text):
    return re.findall(r"^```([a-z]*)\n(.*?)\n```$", text,
                      re.S | re.M)


def check_file(path, rel, house, fails, warns, seen_names):
    text = open(path, encoding="utf-8").read()
    data, body = parse_front_matter(text, rel, fails)
    if data is None:
        return

    # F2 keys
    for k in REQUIRED_KEYS:
        if k not in data or data[k] in (None, "", []):
            fails.append((rel, "F2", "missing or empty key %r" % k))
    for k in data:
        if k not in ALLOWED_KEYS:
            fails.append((rel, "F2", "key %r is not in the allowed set" % k))

    stem = os.path.splitext(os.path.basename(path))[0]
    folder = os.path.basename(os.path.dirname(path))

    # F3 name
    name = data.get("name")
    if isinstance(name, str):
        if name != stem:
            fails.append((rel, "F3", "name %r does not match the file name %r"
                          % (name, stem)))
        if not KEBAB.match(name) or not 1 <= len(name) <= 64:
            fails.append((rel, "F3", "name %r is not kebab case, 1 to 64 chars"
                          % name))
        if name in seen_names:
            fails.append((rel, "F12", "name %r is already used by %s"
                          % (name, seen_names[name])))
        else:
            seen_names[name] = rel

    # F4 mode
    mode = data.get("mode")
    if mode not in MODES:
        fails.append((rel, "F4", "mode %r is not one of %s"
                      % (mode, ", ".join(MODES))))
    elif mode != folder:
        fails.append((rel, "F4", "mode %r but the file sits in prompts/%s"
                      % (mode, folder)))

    # F5 category
    cat = data.get("category")
    if isinstance(cat, str) and (not KEBAB.match(cat) or len(cat) > 32):
        fails.append((rel, "F5", "category %r is not kebab case, 1 to 32 chars"
                      % cat))

    # F6 summary
    summary = data.get("summary")
    if isinstance(summary, str) and len(summary) > 160:
        fails.append((rel, "F6", "summary is %d chars, the cap is 160"
                      % len(summary)))

    # F7 use_when
    use_when = data.get("use_when")
    if isinstance(use_when, str):
        if not use_when.startswith("Use when"):
            fails.append((rel, "F7", "use_when does not start with 'Use when'"))
        if len(use_when) > 200:
            warns.append((rel, "W2", "use_when is %d chars, over the 200 guide"
                          % len(use_when)))

    # F8 inputs
    if not isinstance(data.get("inputs"), list):
        fails.append((rel, "F8", "inputs must be a list of one or more items"))

    # F9 writes
    writes = data.get("writes")
    writes_none = writes == "none"
    if not writes_none and not isinstance(writes, list):
        fails.append((rel, "F9", "writes must be 'none' or a list of writes"))

    # F10 headings, present once and in order
    h1, secs = sections(body)
    if not h1:
        fails.append((rel, "F10", "no level one title"))
    positions = []
    for h in HEADINGS:
        count = len(re.findall(r"^" + re.escape(h) + r"\s*$", body, re.M))
        if count != 1:
            fails.append((rel, "F10", "heading %r appears %d times, expected 1"
                          % (h, count)))
        else:
            positions.append(body.index(h))
    if len(positions) == len(HEADINGS) and positions != sorted(positions):
        fails.append((rel, "F10", "the four headings are out of order"))

    # F11 exactly one fenced block, under ## Prompt, language text, non-empty
    blocks = fenced_blocks(body)
    prompt_text = ""
    if len(blocks) != 1:
        fails.append((rel, "F11", "%d fenced blocks in the file, expected 1"
                      % len(blocks)))
    else:
        lang, prompt_text = blocks[0]
        if lang != "text":
            fails.append((rel, "F11", "the fenced block is tagged %r, expected"
                          " 'text'" % lang))
        if not prompt_text.strip():
            fails.append((rel, "F11", "the fenced block is empty"))
        if "```" not in secs.get("## Prompt", ""):
            fails.append((rel, "F11", "the fenced block is not under "
                                      "## Prompt"))
        if len(prompt_text) > 2500:
            warns.append((rel, "W1", "prompt block is %d chars, over the 2500"
                          " guide" % len(prompt_text)))
        for i, line in enumerate(prompt_text.split("\n"), 1):
            if len(line) > 78:
                warns.append((rel, "W3", "prompt line %d is %d chars, over 78"
                              % (i, len(line))))

    # F13 builtin_overlap
    overlap = data.get("builtin_overlap")
    if overlap is not None:
        if overlap not in BUILTIN_WORK_SKILLS:
            fails.append((rel, "F13", "builtin_overlap %r is not a Vibe Work "
                          "built-in skill" % overlap))
        if overlap not in secs.get("## Before you run it", ""):
            fails.append((rel, "F13", "builtin_overlap %r is never mentioned "
                          "in 'Before you run it'" % overlap))

    boundaries = secs.get("## Boundaries", "")

    # Mode rules
    if mode == "scheduled":
        if not writes_none:
            fails.append((rel, "M1", "a scheduled prompt runs unattended, so "
                                     "writes must be none"))
        hit = find_write(prompt_text)
        if hit:
            fails.append((rel, "M2", "%s (%r) in the prompt block of an "
                          "unattended task" % (hit[1], hit[0])))
        if not READ_ONLY_RE.search(prompt_text):
            fails.append((rel, "M3", "the prompt block never states that it "
                                     "changes nothing"))
    elif mode == "chat":
        if not writes_none:
            fails.append((rel, "M4", "a Chat prompt here reaches nothing, so "
                                     "writes must be none"))
        low = text.lower()
        for c in CONNECTORS:
            if c in low:
                fails.append((rel, "M5", "connectors are documented under "
                              "Work, but this Chat file names %r" % c))
        for w in WEB_PHRASES:
            if w in low:
                fails.append((rel, "M6", "a Chat prompt here works on what "
                              "you paste in, but this one asks for retrieval "
                              "(%r)" % w))
    elif mode == "work":
        if not writes_none and "approval" not in boundaries.lower():
            fails.append((rel, "M7", "writes are declared but Boundaries never "
                                     "mentions approval"))

    if not house:
        return

    # House rules
    for ch, label in DASHES.items():
        if ch in text:
            fails.append((rel, "H1", "%s in the file" % label))
    hit = SAFETY_RE.search(text)
    if hit:
        fails.append((rel, "H2", "safety authorisation language: %r"
                      % hit.group(0)))
    if "draft" not in boundaries.lower():
        fails.append((rel, "H3", "Boundaries never uses the word draft"))
    if not re.search(r"(?:^|\. )It does not\b", boundaries, re.M):
        fails.append((rel, "H3", "Boundaries has no sentence starting "
                                 "'It does not'"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--house", action="store_true",
                    help="also run the house rules")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("paths", nargs="*",
                    help="specific files to check, default is all of them")
    args = ap.parse_args()

    if args.paths:
        files = [os.path.abspath(p) for p in args.paths]
    else:
        files = []
        for mode in MODES:
            d = os.path.join(PROMPTS, mode)
            if not os.path.isdir(d):
                continue
            for fn in sorted(os.listdir(d)):
                if fn.endswith(".md"):
                    files.append(os.path.join(d, fn))

    fails, warns, seen = [], [], {}
    for path in files:
        rel = os.path.relpath(path, ROOT)
        check_file(path, rel, args.house, fails, warns, seen)

    if args.json:
        print(json.dumps({"checked": len(files),
                          "fail": [list(f) for f in fails],
                          "warn": [list(w) for w in warns]}, indent=2))
        return 1 if fails else 0

    for rel, rule, msg in fails:
        print("FAIL %-4s %s: %s" % (rule, rel, msg))
    for rel, rule, msg in warns:
        print("WARN %-4s %s: %s" % (rule, rel, msg))
    if not args.quiet or fails or warns:
        print()
    counts = {}
    for path in files:
        counts[os.path.basename(os.path.dirname(path))] = counts.get(
            os.path.basename(os.path.dirname(path)), 0) + 1
    print("%d prompts checked (%s), %d FAIL, %d WARN"
          % (len(files),
             ", ".join("%s %d" % (m, counts.get(m, 0)) for m in MODES),
             len(fails), len(warns)))
    if not fails:
        print("Every prompt matches its mode: nothing unattended writes, "
              "nothing in Chat reaches for a connector.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
