#!/usr/bin/env python3
"""Own MANIFEST.json and the generated tables in README.md.

Nothing in this repository lists the prompts by hand. The front matter is
the source, this script is the only writer, and --check is what CI runs so
a hand edit to a table cannot survive a commit.

    python3 tools/manifest.py            rewrite MANIFEST.json and README.md
    python3 tools/manifest.py --check    exit 1 if either is out of date
"""

import argparse
import importlib.util
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location(
    "verify", os.path.join(ROOT, "tools", "verify.py"))
verify = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verify)

MODES = verify.MODES
MODE_TITLE = {"work": "Work", "scheduled": "Scheduled tasks", "chat": "Chat"}
README = os.path.join(ROOT, "README.md")
MANIFEST = os.path.join(ROOT, "MANIFEST.json")


def load():
    out = []
    for mode in MODES:
        d = os.path.join(ROOT, "prompts", mode)
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if not fn.endswith(".md"):
                continue
            path = os.path.join(d, fn)
            text = open(path, encoding="utf-8").read()
            fails = []
            data, _ = verify.parse_front_matter(text, fn, fails)
            if data is None:
                raise SystemExit("cannot read %s: %s" % (fn, fails))
            entry = {
                "name": data.get("name"),
                "mode": data.get("mode"),
                "category": data.get("category"),
                "summary": data.get("summary"),
                "use_when": data.get("use_when"),
                "inputs": data.get("inputs"),
                "writes": data.get("writes"),
                "outputs": data.get("outputs"),
                "path": "prompts/%s/%s" % (mode, fn),
            }
            if data.get("builtin_overlap"):
                entry["builtin_overlap"] = data["builtin_overlap"]
            out.append(entry)
    return out


def manifest_text(entries):
    counts = {m: sum(1 for e in entries if e["mode"] == m) for m in MODES}
    counts["total"] = len(entries)
    writes = sum(1 for e in entries if e["writes"] != "none")
    doc = {
        "repo": "awesome-mistral-vibe-prompts",
        "for": "Mistral Vibe Work, scheduled tasks and Chat",
        "counts": counts,
        "prompts_that_write": writes,
        "prompts": entries,
    }
    return json.dumps(doc, indent=2, ensure_ascii=False) + "\n"


def table(entries, mode):
    rows = [e for e in entries if e["mode"] == mode]
    lines = []
    for cat in sorted({e["category"] for e in rows}):
        lines.append("")
        lines.append("**%s**" % cat)
        lines.append("")
        lines.append("| Prompt | Use when | Writes |")
        lines.append("|---|---|---|")
        for e in sorted(rows, key=lambda x: x["name"]):
            if e["category"] != cat:
                continue
            use = e["use_when"]
            if use.startswith("Use when "):
                use = use[len("Use when "):]
            use = use.rstrip(".")
            if e["writes"] == "none":
                wr = "nothing"
            else:
                wr = "**yes, with approval**"
            lines.append("| [`%s`](%s) | %s | %s |"
                         % (e["name"], e["path"], use, wr))
    lines.append("")
    return "\n".join(lines)


def set_marker(text, marker, value):
    begin = "<!-- %s:start -->" % marker
    end = "<!-- %s:end -->" % marker
    if begin not in text or end not in text:
        raise SystemExit("README.md has no %s marker" % marker)
    head, rest = text.split(begin, 1)
    _, tail = rest.split(end, 1)
    return head + begin + str(value) + end + tail


def readme_text(entries):
    text = open(README, encoding="utf-8").read()
    counts = {m: sum(1 for e in entries if e["mode"] == m) for m in MODES}
    text = set_marker(text, "n-prompts", len(entries))
    for mode in MODES:
        text = set_marker(text, "n-" + mode, counts[mode])
    text = set_marker(text, "n-writes",
                      sum(1 for e in entries if e["writes"] != "none"))
    text = set_marker(text, "n-overlap",
                      sum(1 for e in entries if e.get("builtin_overlap")))
    text = set_marker(
        text, "badge-prompts",
        "[![Prompts](https://img.shields.io/badge/prompts-%d-blue)](prompts/)"
        % len(entries))
    for mode in MODES:
        begin = "<!-- BEGIN:%s -->" % mode
        end = "<!-- END:%s -->" % mode
        if begin not in text or end not in text:
            raise SystemExit("README.md has no %s / %s markers"
                             % (begin, end))
        head, rest = text.split(begin, 1)
        _, tail = rest.split(end, 1)
        text = head + begin + "\n" + table(entries, mode) + end + tail
    return text


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true",
                    help="do not write, exit 1 if anything is out of date")
    args = ap.parse_args()

    entries = load()
    want_manifest = manifest_text(entries)
    want_readme = readme_text(entries) if os.path.exists(README) else None

    if args.check:
        stale = []
        have = (open(MANIFEST, encoding="utf-8").read()
                if os.path.exists(MANIFEST) else "")
        if have != want_manifest:
            stale.append("MANIFEST.json")
        if want_readme is not None:
            if open(README, encoding="utf-8").read() != want_readme:
                stale.append("README.md")
        if stale:
            print("STALE: %s. Run python3 tools/manifest.py"
                  % ", ".join(stale))
            return 1
        print("MANIFEST.json and README.md match the %d prompts on disk"
              % len(entries))
        return 0

    with open(MANIFEST, "w", encoding="utf-8") as fh:
        fh.write(want_manifest)
    if want_readme is not None:
        with open(README, "w", encoding="utf-8") as fh:
            fh.write(want_readme)
    counts = ", ".join("%s %d" % (m, sum(1 for e in entries
                                         if e["mode"] == m)) for m in MODES)
    print("wrote MANIFEST.json and the README tables: %d prompts (%s)"
          % (len(entries), counts))
    return 0


if __name__ == "__main__":
    sys.exit(main())
