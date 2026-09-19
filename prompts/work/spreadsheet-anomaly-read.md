---
name: spreadsheet-anomaly-read
mode: work
category: analysis
summary: Read a spreadsheet or export and report what looks wrong in the data before anyone draws a conclusion from it.
use_when: Use when you have been handed a file to analyse and want the data quality problems surfaced before the analysis, not after.
inputs:
  - The spreadsheet, CSV or export
writes: none
outputs: A structure summary, a row per anomaly with the cells involved, and separate lists for What I assumed and What I could not check.
builtin_overlap: data-analysis
---

# Spreadsheet anomaly read

## Prompt

```text
Read the attached file. Do not analyse it yet. Tell me what is wrong
with it first.

Start with structure. Rows, columns, the header row you used, and one
line per column: what it appears to hold, its type, how many cells are
empty, and how many distinct values it has. Say which column you think
is the key and why.

Then anomalies, one row each:

  What. The problem, named plainly.
  Where. The column, and the row numbers or a count if there are many.
  Example. Two actual values from the file.
  Why it matters. What an analysis would get wrong if nobody noticed.

Look for at least: duplicate keys, mixed types in one column, dates in
more than one format, numbers stored as text, trailing spaces, values
that should be in a fixed set and are not, totals that do not match the
rows above them, gaps in a series that should be continuous, and values
outside a range the column's own meaning allows.

Then two sections.

What I assumed. Every assumption you made to read the file at all: the
header row, the date format, the decimal separator, which sheet.

What I could not check. Anything that needs a source outside this file,
including whether the extract is complete and whether the period is the
one I think it is.

Rules. Do not clean, correct or reshape the data. Do not compute any
business metric from it yet. Report on the file as it is.
```

## Before you run it

- Vibe Work ships a built-in `data-analysis` skill for tables, metrics and anomalies. Use `/data-analysis` when you want the analysis; use this when you want the reasons not to trust it yet.
- Say where the extract came from and what period it should cover. Completeness cannot be checked from inside the file.

## What you get

A structural read and an anomaly list with real example values, plus the assumptions the model had to make to open the file at all, which is usually where a wrong number starts.

## Boundaries

It reports on the file. It does not correct it, and it draws no business conclusion. The output is a draft for whoever owns the data to confirm before the analysis runs.
