# Using these prompts in Mistral Vibe

Three ways to run a prompt from this repository, and they are not
interchangeable. Product behaviour here was read from Mistral's documentation
on 19 September 2026.

## 1. Paste it

Open the file, copy the block under `## Prompt`, paste it into the mode named
in the front matter, replace the CAPITALISED placeholders, and attach whatever
`inputs:` lists.

For Work prompts, turn on the connectors the prompt needs first. Use the `+`
icon, or type `/` and pick Tools. The connectors Work exposes are Gmail,
Outlook, Slack, Notion, Linear, GitHub, Atlassian, Google Drive, SharePoint and
Stripe.

Work asks clarifying questions when a prompt is ambiguous, shows tool calls as
it makes them, and keeps a live todo panel. All three are useful here: the todo
panel is the fastest way to see that a prompt is doing something you did not
ask for.

## 2. Save it as a Work Skill

A Skill is the same instructions, stored, and triggered by its description
rather than by you pasting. Work Skills are authored in the UI with three
fields:

| Field | Take it from | Why |
|---|---|---|
| Title | the `# Title` line | shown in the picker |
| Description | the `use_when:` line | this is what decides when the Skill activates |
| SKILL.md | the prompt block, then the Boundaries section | the instructions themselves |

Things worth knowing before you paste:

- **The description is a router, not a summary.** Discovery loads name and
  description only, at roughly 100 tokens each, and the full body is read only
  once the Skill activates. Mistral's own guidance: "*Use when...* phrasing
  beats *This Skill helps with...* every time."
- **Scopes are Built-in, Personal and Workspace.** An admin can force enable a
  Workspace Skill so nobody can turn it off. If you are publishing one of these
  to a Workspace, read its Boundaries section first and decide whether you want
  that text in front of colleagues, because it is the part that says what the
  Skill will not do.
- **Edits reach new chats only.** A Skill you change mid conversation is not
  the Skill that conversation is running. Start a new chat to test a change.
- **Triggering** happens three ways: automatically from the description, from
  the `/` picker or `/{skill-name}`, or by naming the Skill in prose.

Twelve Skills ship built in: `challenge-my-thinking`, `data-analysis`,
`deep-research`, `doc-coauthoring`, `document-review`, `internal-comms`,
`meeting-prep`, `research-synthesis`, `skill-creator`,
`stakeholder-translator`, `structured-extraction` and `vibe-work-onboarding`.
Where a prompt here overlaps one, its front matter says so in
`builtin_overlap` and its "Before you run it" section says why you might still
want the narrower version.

## 3. Schedule it

Scheduled tasks are in Public Preview and are **Work mode only**. They are
built on the Workflows infrastructure, and they can use Skills, inline
Connectors, Web search, Libraries and Projects. Cadence is once, daily, weekly,
monthly or yearly. Triggers are time based only: there is no event trigger, so
nothing here can fire on a message arriving.

Two scoping facts decide where a schedule can live:

- A scheduled task **runs in the Workspace where it was created**.
- **Connector authentications are Workspace scoped.** A task created in a
  Workspace whose Gmail is not connected will not read your mail, whatever the
  prompt says.

### The approval question, which is the whole point

Before Work does anything that, in Mistral's words, "creates, modifies, sends,
posts, or deletes", it stops and asks. You get three options.

- **Continue** approves that one action. Work asks again next time.
- **Always allow** pre-authorises that function for the session.
- **Decline** cancels it, and Work either skips the step or asks you how to
  proceed.

Standing pre-authorisation is a different control in a different place. Open
the connector's card on the Connectors page and its Functions tab lists every
function it exposes, each with its own Always allow toggle, grouped into
interactive tools, which Mistral defines as the ones that "create, update,
delete, send, or post data", and read-only tools, which "retrieve information
(get, list, search)". Those settings are per user. Mistral's own advice is to
keep the interactive ones on manual approval until you are confident.

A scheduled run happens with nobody there to press Continue. So a scheduled
task can only write if somebody has already pre-authorised that function, and
Mistral's own guidance for unattended runs is to keep prompts read only:
summarise, brief, monitor.

Every prompt in `prompts/scheduled/` is built for that. All twelve declare
`writes: none`, none of them points a write verb at anything outside the
conversation, and each one states inside
the prompt that it changes nothing. `tools/verify.py` fails the build on all
three conditions, so the property survives contributions.

If you want a scheduled task that does write, the honest version is two steps:
a scheduled read-only task that produces the list, and a human who reads it and
runs a Work prompt that writes, with the approval prompt in front of them.

## What belongs in Chat

Chat is the legacy surface. Mistral documents Connectors, approvals and Skills
under Work, and the Chat page names none of them, so a Chat prompt that tells
the agent to go and read your mail, your tickets or your files is pointed at
the surface where none of that is documented. Treat what comes back
accordingly. Chat's old features have Work successors: Agents became Skills, Think
mode became an automatic reasoning level, Deep Research is Work only and
redirects, Code Interpreter became the built-in TypeScript code environment,
and Memories became the Knowledge Base.

The sixteen Chat prompts here are the ones that need none of that. They work on
text you paste, and several of them say inside the prompt that the model cannot
run or fetch anything, because that is exactly when a model is most likely to
pretend it did.
