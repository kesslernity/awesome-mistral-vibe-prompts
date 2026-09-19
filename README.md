# Awesome Mistral Vibe Prompts

**A prompt is not portable between Vibe's three modes, and the failure is quiet in the direction that matters.** Mistral documents Connectors, approvals and Skills under Work. The Chat page names none of them, and Deep Research launched in Chat redirects you to Work. So a Chat prompt that tells the agent to go and read your mail is pointed at the wrong surface, and whatever comes back is not your mail. A scheduled task is the other end of it: Work with nobody in the room, so the prompt that was safe at your desk on Tuesday is a write nobody watched at six on Sunday morning. This library is therefore sorted by mode, not by topic, and a checker enforces the mode: no scheduled prompt may aim a write verb at anything outside the conversation, and no Chat prompt may name a connector.

> **<!-- n-prompts:start -->49<!-- n-prompts:end --> prompts for Mistral Vibe: <!-- n-work:start -->21<!-- n-work:end --> for Work, <!-- n-scheduled:start -->12<!-- n-scheduled:end --> for scheduled tasks, <!-- n-chat:start -->16<!-- n-chat:end --> for Chat. <!-- n-writes:start -->1<!-- n-writes:end --> of them writes anything, and it says so in its front matter.**

[![Licence: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
<!-- badge-prompts:start -->[![Prompts](https://img.shields.io/badge/prompts-49-blue)](prompts/)<!-- badge-prompts:end -->
[![Checked by](https://img.shields.io/badge/checked%20by-tools%2Fverify.py-green)](tools/verify.py)

Not affiliated with, or endorsed by, Mistral AI. Product behaviour described below was read from Mistral's own documentation on 19 September 2026 and is named as behaviour of a product that moves. The rules the checker enforces are mine.

---

## Pick the mode first

Mistral's own routing, quoted:

| Mode | When Mistral says to use it |
|---|---|
| **Work** | "Pick Work when you want the agent to do the legwork, not just answer a question." |
| **Code** | "Pick Code when the task depends on a codebase, terminal, IDE, or coding session." |
| **Chat** | "Pick Chat when you want a quick turn-based conversation, or when you rely on a legacy feature." |

This repository covers Work and Chat. Code prompts belong next to the code, and the skills for Code live in [awesome-mistral-vibe-skills](https://github.com/kesslernity/awesome-mistral-vibe-skills?utm_source=github&utm_medium=repo&utm_campaign=amv_prompts).

What actually differs, and why it decides the prompt:

| | Work | Scheduled task | Chat |
|---|---|---|---|
| Connectors | Yes: Atlassian, Box, Gmail, GitHub, Google Calendar, Linear, Notion, Outlook, Outlook Calendar, SharePoint, Slack, Stripe | Yes, Connectors are on the list of what a scheduled task may use | None documented |
| Can it act on your behalf | Yes, after you approve | Only where the function was pre-authorised | Nothing documented |
| Who is watching | You are | Nobody | You are |
| Skills | Yes | Yes | No. Chat's Agents are the legacy feature Skills replaced |
| What a prompt may ask for here | Read, gather, draft; write only with the approval named | Read and report. Nothing else | Reason over text you pasted |

Two of those cells need their caveat said out loud. The connector list above is the one on Mistral's Connectors page; the mode-routing page names Google Drive in its own list, which the Connectors table does not carry. Where two of Mistral's pages disagree, this repository says so rather than picking the tidier one. And "none documented" for Chat is exactly that, an absence in the documentation rather than a denial from Mistral: the Chat page describes what Chat keeps, not what it lacks.

So the two Chat rules the checker enforces are filing rules for this library, not claims about the product. A prompt that needs a connector, or needs something fetched, goes in Work, where both are documented. Chat keeps the work that needs nothing but a model and the text in front of it.

Chat is the legacy surface by Mistral's own framing, and its residents have Work successors: Agents became Skills, Think mode became an automatic reasoning level, Deep Research is Work only and launching it in Chat redirects you, Code Interpreter became the built-in TypeScript code environment, and Memories became the Knowledge Base. The Chat prompts here are the ones that survive that migration untouched: rewriting, decoding, framing, arguing with you.

## The unattended rule

Scheduled tasks are in Public Preview, they are Work mode only, and they run on a clock: once, daily, weekly, monthly or yearly, time based, with no event triggers. They can use Skills, inline Connectors, Web search, Libraries and Projects. They run in the Workspace where they were created, and connector authentications are Workspace scoped.

Now the part that decides this library's shape. Before Work does anything that, in Mistral's words, "creates, modifies, sends, posts, or deletes", it stops and asks, with three options. **Continue** approves that one action and Work asks again next time. **Always allow** pre-authorises that function for the session. **Decline** cancels it. Standing pre-authorisation lives somewhere else entirely: the Functions tab on the connector's own card, where each function carries its own Always allow toggle, and those settings are per user.

A scheduled run happens with nobody there to press anything. So for a scheduled task to write, somebody has to have pre-authorised the function in advance, and Mistral's own guidance for unattended runs is to keep the prompts read only: summarise, brief, monitor.

Which turns a doctrine into a rule a script can check:

```
mode: scheduled  →  writes: none
                 →  no write verb in the prompt block aimed at
                    anything outside the conversation
                 →  the prompt block must state that it changes nothing
```

`tools/verify.py` fails the build on any of the three. The ruler for what counts as a write is Mistral's own: its safety page calls a tool interactive when it "creates, updates, deletes, sends, or posts data", and read only when it "retrieves information (get, list, search)".

The checker carries that as two lists rather than one, because most of those verbs have a harmless reading. Send, reply, delete, archive, pay, approve, merge, revoke and unsubscribe fail on the verb alone. Create, update, modify, post, move, assign, schedule, upload, submit, publish, rename, transfer, invite, grant, share and write fail only when the verb is aimed, within the next few words, at something that lives outside the conversation: a connector by name, or an issue, a ticket, a pull request, an email, a draft, a calendar event, a channel, a canvas, a commit, a branch, a repository. So "create a table of the five biggest movers" passes and "create a Linear issue" does not. Word boundaries do the rest: "sender" is a reader and passes, "send" does not.

What this cannot do is prove that a prompt never writes. A prompt that describes a write without naming it will pass. The rule catches the prompts that say what they are about to do, which is nearly all of them, and `tools/selftest.py` carries four negative controls alongside the positive cases, because a rule that fires on a correct file is a rule somebody silences within a month.

## Install

There is nothing to install. A prompt here is a file you paste from, and the repository is the thing that keeps them honest.

```bash
git clone https://github.com/kesslernity/awesome-mistral-vibe-prompts.git
cd awesome-mistral-vibe-prompts
python3 tools/verify.py --house      # stdlib only, any python3
```

**To use one.** Open the file, copy the block under `## Prompt`, paste it into the mode named in its front matter, and fill the CAPITALISED placeholders. Read `## Before you run it` first, because most of these have one precondition that decides whether the output is any good.

**To make a Work prompt permanent, turn it into a Skill.** Work Skills are authored in the UI with three fields, so the mapping is direct:

| Skill field | Take it from |
|---|---|
| Title | the `# Title` line |
| Description | the `use_when:` line |
| SKILL.md | the prompt block, plus the Boundaries section |

The description is what decides when a Skill activates, and Mistral's own guidance is blunt about the shape: "*Use when...* phrasing beats *This Skill helps with...* every time". Every `use_when` in this repository opens with "Use when", and the checker fails a file that does not. Discovery loads name and description only, about 100 tokens each, so the description is doing the work of a router rather than a summary.

**To schedule one**, create the task in the Workspace whose connectors you want it to use, paste a prompt from `prompts/scheduled/`, and leave every connector function unauthorised. These twelve are built so that nothing needs pre-authorising.

## The one prompt that writes

`reply-drafts-for-review` creates unsent drafts in your mailbox. It is the only file in the repository whose `writes:` is not `none`, and it is here because the approval step is worth showing rather than describing.

It is also the clearest case in the library of the mode question being a connector question underneath. Mistral asks Gmail for the `gmail.compose` scope rather than `gmail.send`, and explains the choice in as many words: Vibe "only creates drafts, never sends emails directly", and you send from Gmail yourself. Outlook's connector is documented as "Read and send emails", and drafting is not on that list. Same prompt, same three approval buttons, and on one of the two the nearest documented action to the one you asked for is the irreversible one. So the prompt tells you to answer **Continue** every time rather than **Always allow**: on this file the approval is the control, and Always allow would hand it back.

Everything else reads, gathers, compares and drafts into the conversation, where nothing has been done to anybody's system yet. That is the whole posture of this library, and the checker enforces its narrow half: a Work prompt that declares a write and never mentions approval in its Boundaries section is a failure, not a style note.

## What the checker enforces

`tools/verify.py` is under 400 lines of standard library Python. It parses the front matter itself, so it runs on any `python3` with no dependency and no minimum version worth worrying about.

| Rule | What fails |
|---|---|
| F1 to F2 | front matter is unparseable, a required key is missing or empty, or a key is not in the allowed set |
| F3 | `name` does not match the file name, or is not kebab case |
| F4 | `mode` is not one of the three, or does not match the folder the file is in |
| F5 to F6 | category is not kebab case, summary is over 160 characters |
| F7 | `use_when` does not open with "Use when" |
| F8 to F9 | `inputs` is not a list, `writes` is neither `none` nor a list |
| F10 | the four headings are missing, duplicated or out of order |
| F11 | not exactly one fenced block, not tagged `text`, empty, or not under `## Prompt` |
| F12 | two prompts share a name |
| F13 | `builtin_overlap` is not one of Work's twelve built-in Skills, or is never mentioned in "Before you run it" |
| M1 to M3 | a scheduled prompt declares a write, aims a write verb outside the conversation, or never says it changes nothing |
| M4 to M6 | a Chat prompt declares a write, names a connector, or asks for something to be fetched |
| M7 | a Work prompt declares a write and never mentions approval in Boundaries |
| H1 to H3 | an em dash, safety authorisation language, or a Boundaries section that never says what the prompt does not do |

Three warnings that never fail the build: a prompt block over 2,500 characters, a `use_when` over 200 characters, a prompt line over 78 characters. If a warning fires on a file that is right, the rule is wrong.

`tools/selftest.py` breaks a clean baseline once per rule and asserts that the rule fires, asserts that all three baselines stay clean, and carries four negative controls that must stay clean too. 48 cases. A new rule ships with its case in the same commit.

## The prompts

### Work

Read, gather, compare, draft. These expect connectors and a person reading the output.

<!-- BEGIN:work -->

**analysis**

| Prompt | Use when | Writes |
|---|---|---|
| [`cost-driver-breakdown`](prompts/work/cost-driver-breakdown.md) | a cost has moved and you need to know which components moved, before anyone explains it in a meeting | nothing |
| [`metric-definition-audit`](prompts/work/metric-definition-audit.md) | two teams report the same metric with different numbers and you need to find out whether they are measuring the same thing | nothing |
| [`spreadsheet-anomaly-read`](prompts/work/spreadsheet-anomaly-read.md) | you have been handed a file to analyse and want the data quality problems surfaced before the analysis, not after | nothing |

**comms**

| Prompt | Use when | Writes |
|---|---|---|
| [`change-announcement-draft`](prompts/work/change-announcement-draft.md) | a change is about to affect colleagues and you need an announcement that survives the first ten replies | nothing |
| [`exec-update-draft`](prompts/work/exec-update-draft.md) | you owe someone senior a written update and the material is scattered across tickets, documents and threads | nothing |
| [`stakeholder-reframe`](prompts/work/stakeholder-reframe.md) | one piece of work has to be told to a second audience and you want the translation visible rather than invisible | nothing |

**customer**

| Prompt | Use when | Writes |
|---|---|---|
| [`support-theme-synthesis`](prompts/work/support-theme-synthesis.md) | you have a pile of tickets, reviews or survey answers and need the themes with numbers rather than an impression | nothing |

**documents**

| Prompt | Use when | Writes |
|---|---|---|
| [`contract-renewal-risk-read`](prompts/work/contract-renewal-risk-read.md) | a contract is coming up for renewal and you need the mechanical terms in front of you before any conversation with the vendor | nothing |
| [`policy-gap-questions`](prompts/work/policy-gap-questions.md) | you have to review an internal policy against a framework and want the gaps in a form you can take to the owner | nothing |
| [`rfp-requirement-extract`](prompts/work/rfp-requirement-extract.md) | a tender, RFP or statement of work arrives and you need every requirement as a row before anyone starts writing answers | nothing |

**governance**

| Prompt | Use when | Writes |
|---|---|---|
| [`ai-use-case-intake`](prompts/work/ai-use-case-intake.md) | someone proposes an AI use case and you need it written down in a comparable shape before anyone assesses it | nothing |

**inbox**

| Prompt | Use when | Writes |
|---|---|---|
| [`inbox-triage-plan`](prompts/work/inbox-triage-plan.md) | you are behind on mail and need a plan for the next hour instead of a folder full of unread items | nothing |
| [`reply-drafts-for-review`](prompts/work/reply-drafts-for-review.md) | you have triaged your mail and want the routine replies written but not sent | **yes, with approval** |

**meetings**

| Prompt | Use when | Writes |
|---|---|---|
| [`decision-log-entry`](prompts/work/decision-log-entry.md) | a decision has just been taken in a meeting or a thread and you need it written down before the reasoning evaporates | nothing |
| [`meeting-prep-brief`](prompts/work/meeting-prep-brief.md) | you are walking into a meeting you did not organise and need the history, the open questions and the likely asks | nothing |

**planning**

| Prompt | Use when | Writes |
|---|---|---|
| [`risk-register-draft`](prompts/work/risk-register-draft.md) | you need a first risk register for a project and want it built from what people actually wrote rather than from a generic list | nothing |
| [`rollout-plan-draft`](prompts/work/rollout-plan-draft.md) | a change has to reach a population in stages and you need a first plan that makes the unknowns visible | nothing |

**research**

| Prompt | Use when | Writes |
|---|---|---|
| [`claim-check-pack`](prompts/work/claim-check-pack.md) | something is about to be published or sent and you need each factual claim checked against a source rather than read for tone | nothing |
| [`regulation-change-watch`](prompts/work/regulation-change-watch.md) | you need the current state of a specific regulation on specific questions, and secondhand summaries are not good enough | nothing |
| [`vendor-landscape-scan`](prompts/work/vendor-landscape-scan.md) | you need a first pass at who is in a market and what they claim, before anyone books a demo | nothing |

**status**

| Prompt | Use when | Writes |
|---|---|---|
| [`weekly-project-catchup`](prompts/work/weekly-project-catchup.md) | you have been away from a project and need what changed, what is blocked and what needs you, before you walk into a meeting | nothing |
<!-- END:work -->

### Scheduled tasks

Work mode, on a clock, with nobody watching. Every one of these reads and reports and nothing else.

<!-- BEGIN:scheduled -->

**documents**

| Prompt | Use when | Writes |
|---|---|---|
| [`doc-change-watch`](prompts/scheduled/doc-change-watch.md) | a policy or procedure space matters and nobody is watching what quietly changed in it | nothing |

**finance**

| Prompt | Use when | Writes |
|---|---|---|
| [`spend-anomaly-watch`](prompts/scheduled/spend-anomaly-watch.md) | spend is spread across vendors and nobody notices a change until the quarter closes | nothing |
| [`vendor-renewal-lookahead`](prompts/scheduled/vendor-renewal-lookahead.md) | auto-renewal has already cost you once and nobody owns the calendar | nothing |

**governance**

| Prompt | Use when | Writes |
|---|---|---|
| [`access-review-prep`](prompts/scheduled/access-review-prep.md) | access reviews stall because assembling the lists takes longer than reviewing them | nothing |
| [`regulation-diff-watch`](prompts/scheduled/regulation-diff-watch.md) | a small set of official sources governs your work and you need the change before the newsletter tells you | nothing |

**inbox**

| Prompt | Use when | Writes |
|---|---|---|
| [`inbox-triage-digest`](prompts/scheduled/inbox-triage-digest.md) | you want the state of your mailbox in one note each morning instead of opening it cold | nothing |

**operations**

| Prompt | Use when | Writes |
|---|---|---|
| [`overnight-incident-digest`](prompts/scheduled/overnight-incident-digest.md) | incidents are discussed across a chat tool and a tracker and you want one read before the stand-up | nothing |

**projects**

| Prompt | Use when | Writes |
|---|---|---|
| [`backlog-ageing-report`](prompts/scheduled/backlog-ageing-report.md) | the backlog keeps growing and nobody can say which parts of it are actually dead | nothing |
| [`project-rollup`](prompts/scheduled/project-rollup.md) | you write the same weekly status by hand from three tools every Friday | nothing |

**reporting**

| Prompt | Use when | Writes |
|---|---|---|
| [`kpi-pack-prep`](prompts/scheduled/kpi-pack-prep.md) | the monthly pack takes a day to assemble and half the meeting is spent questioning the numbers | nothing |

**research**

| Prompt | Use when | Writes |
|---|---|---|
| [`competitor-watch`](prompts/scheduled/competitor-watch.md) | you want a steady signal on a handful of competitors without a daily feed of commentary | nothing |

**revenue**

| Prompt | Use when | Writes |
|---|---|---|
| [`pipeline-hygiene-check`](prompts/scheduled/pipeline-hygiene-check.md) | pipeline reviews keep turning into arguments about whether the data is right | nothing |
<!-- END:scheduled -->

### Chat

Text in, thinking out. Nothing in this folder names a connector or asks for anything to be fetched, so every one of them works on what you paste.

<!-- BEGIN:chat -->

**explaining**

| Prompt | Use when | Writes |
|---|---|---|
| [`analogy-check`](prompts/chat/analogy-check.md) | you are about to build an explanation or a pitch on a comparison | nothing |
| [`explain-to-a-newcomer`](prompts/chat/explain-to-a-newcomer.md) | you have to bring somebody up to speed and you have stopped being able to tell what is obvious | nothing |
| [`jargon-decode`](prompts/chat/jargon-decode.md) | you are reading something in an unfamiliar area and half the nouns are doing unknown work | nothing |

**technical**

| Prompt | Use when | Writes |
|---|---|---|
| [`error-message-decode`](prompts/chat/error-message-decode.md) | an error is unfamiliar and you want the reading before you start changing things | nothing |
| [`regex-explain`](prompts/chat/regex-explain.md) | you are about to trust a pattern somebody else wrote, or one you wrote a month ago | nothing |
| [`sql-read`](prompts/chat/sql-read.md) | a number came from a query you did not write and you have to decide whether to trust it | nothing |

**thinking**

| Prompt | Use when | Writes |
|---|---|---|
| [`assumption-list`](prompts/chat/assumption-list.md) | a plan feels solid and you want the things nobody stated written down | nothing |
| [`options-table`](prompts/chat/options-table.md) | a choice has drifted into a conversation and nobody has written the options next to each other | nothing |
| [`pre-mortem-quick`](prompts/chat/pre-mortem-quick.md) | a plan is agreed, the deadline is real, and nobody wants to reopen it | nothing |
| [`second-order-effects`](prompts/chat/second-order-effects.md) | a change will alter what people are measured on, paid for or asked to report | nothing |
| [`steelman-the-objection`](prompts/chat/steelman-the-objection.md) | you are about to present something and every objection in your head is an easy one | nothing |
| [`tradeoff-frame`](prompts/chat/tradeoff-frame.md) | a discussion keeps going in circles because both sides are right about different things | nothing |

**writing**

| Prompt | Use when | Writes |
|---|---|---|
| [`plain-english-rewrite`](prompts/chat/plain-english-rewrite.md) | a paragraph reads as important and you cannot tell what it commits anyone to | nothing |
| [`subject-line-options`](prompts/chat/subject-line-options.md) | the message is written and the subject line is the part still costing you ten minutes | nothing |
| [`tighten-this`](prompts/chat/tighten-this.md) | something you wrote is too long and you want the cut shown rather than hidden | nothing |
| [`tone-shift`](prompts/chat/tone-shift.md) | a message is right in substance and wrong in temperature | nothing |
<!-- END:chat -->

## Where these meet Work's built-in Skills

Vibe Work ships twelve built-in Skills: `challenge-my-thinking`, `data-analysis`, `deep-research`, `doc-coauthoring`, `document-review`, `internal-comms`, `meeting-prep`, `research-synthesis`, `skill-creator`, `stakeholder-translator`, `structured-extraction` and `vibe-work-onboarding`.

<!-- n-overlap:start -->7<!-- n-overlap:end --> prompts here sit next to one of them, and each says so in its front matter with `builtin_overlap`, and says why in its "Before you run it" section. The checker fails a file that names an overlap and then never mentions it. The honest summary: try the built-in first. These exist for the narrower case, usually because they ask for the thing a general skill leaves out, which is normally the list of what could not be established.

## Check before you ship

```bash
python3 tools/verify.py --house      # 49 prompts, format and mode rules, house rules
python3 tools/selftest.py            # 48 cases, proves each rule fires
python3 tools/manifest.py --check    # MANIFEST.json and the README tables match disk
```

The tables above are generated. `MANIFEST.json` is generated. Neither is edited by hand, and `--check` is what stops a hand edit surviving a commit.

## What these prompts will not do for you

- **They do not decide.** Every one drafts, lists, compares or questions. Where a prompt could plausibly be read as deciding, its Boundaries section says otherwise in a sentence beginning "It does not".
- **They are not safety authorisation.** Nothing here goes anywhere near a permit to work, an isolation, a confined space entry, an incident classification or an inspection. AI prepares, a qualified human decides, and the checker greps for the language.
- **They do not verify.** A prompt that asks for sources gets you sources to check, not checked sources.
- **They do not know your organisation.** Most of them have a section that asks the model to name what it could not establish. That section is the deliverable more often than the rest of the output.

## Reference

- [`docs/USING-IN-VIBE.md`](docs/USING-IN-VIBE.md): what differs between pasting a prompt, saving it as a Skill and scheduling it, with the Workspace and connector scoping that decides where a scheduled task can run.
- [`docs/WRITING-PROMPTS.md`](docs/WRITING-PROMPTS.md): the file format, every front matter key, and the shape these prompts share.
- [`CONTRIBUTING.md`](CONTRIBUTING.md): the loop, and the rule that a new check ships with the case that proves it fires.
- [`MANIFEST.json`](MANIFEST.json): every prompt with its front matter, generated by `tools/manifest.py`.

## Related

- [awesome-mistral-vibe-skills](https://github.com/kesslernity/awesome-mistral-vibe-skills?utm_source=github&utm_medium=repo&utm_campaign=amv_prompts): 137 skills in the format Vibe Code reads, and the bodies you would paste into a Work Skill.
- [awesome-mistral-vibe-agents](https://github.com/kesslernity/awesome-mistral-vibe-agents?utm_source=github&utm_medium=repo&utm_campaign=amv_prompts): agent profiles for the Vibe CLI, where the humans-decide posture is expressed as a permission block rather than as prose.
- [mistral-vibe](https://github.com/mistralai/mistral-vibe): the CLI itself, Apache 2.0.
- More on how these are built and why: [kesslernity.com](https://www.kesslernity.com/?utm_source=github&utm_medium=repo&utm_campaign=amv_prompts).

## Licence

CC BY-SA 4.0. Use them, change them, ship them in your own repository. Keep the licence and say where they came from.
