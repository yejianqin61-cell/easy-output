---
name: easy-summary
description: >-
  Use when the user needs a briefing on what changed over a window: a round, a sprint, a week, a
  release, a handover. Produces a summary in three parts: the headline with a change table, what the
  changes mean, and what is still open. Delivers Markdown or a single-file HTML report, whichever the
  user picks. Triggers on 总结, 汇报, 周报, 日报, 这一轮做了什么, 进展, 交接, summary, briefing, changelog,
  wrap-up, "what changed".
---

# Easy summary

A summary is a **briefing**: one page for someone who was not there, and who will pass it on. An audit
judges a round; a summary retells it.

The difference shows in one test. A document that starts saying "we should fix", "must do" or carries
acceptance criteria is an audit. Call the Skill tool with "easy-audit" instead.

Read [references/readability-law.md](references/readability-law.md) before writing. Its twelve clauses
hold here.

## The selection rule

A change earns its place only if it **changes what the reader expects or does**. Everything else is
routine, and routine takes one line.

That rule is the whole job. Asked for a summary, an agent defaults to listing everything in the order it
happened. A briefing lists the few things that matter and says what they mean.

## Output

Ask once, before writing: **Markdown, or a single-file HTML report?** Markdown is the default when the
user does not care.

For the report, finish the Markdown first, then call the Skill tool with "easy-report". It owns the
template and the fill-in contract, and it keeps the facts identical.

## Process

Five steps. Each ends on a check you can make.

### 1. Pin the window and the baseline

The window is the period covered. The baseline is what the reader compares it against: the last summary,
the plan, the release, "before this round". Ask for whichever is missing, and only that one.

**Done when** both appear in the header, as a date range and a named baseline.

### 2. Collect the changes

Sources: `git log` over the window, the plans from the last audit, closed tickets, the user's notes.
Include work that was dropped or deferred, because that changes expectations too.

**Done when** every candidate change names a source.

### 3. Select

Apply the selection rule to each candidate. Keep the few. A kept change the reader would have expected
anyway is not carrying its weight.

**Done when** every kept row says what it changes for the reader, and the routine remainder is one line
at the foot of the table.

### 4. Write the three parts

<summary-template>

## 1. Headline

**This round: 9 changes, 6 done, 1 dropped. Private messages are now realtime.**

| # | Change | Where | Kind | State | What it means for the reader |
|---|---|---|---|---|---|
| C-1 | Realtime chat replaces 4s polling | `src/chat/**` | Changed | Done | Messages arrive without a refresh |
| C-2 | Push notifications wired for messages | `src/push/**` | New | In progress | Needs a device-token endpoint to reach a phone |
| C-3 | The polling path leaves the plan | — | Removed | Done | The old poller still ships this round |

Routine: dependency bumps, two test-only refactors, a token rotation.

## 2. What it means

Two or three sentences that connect the changes: the direction, what it unblocks, what it costs. This is
the part the reader quotes, so it carries a claim rather than a list.

## 3. Still open

- The device-token endpoint, so push reaches a real phone.
- The old poller still ships, so two paths read messages until it goes.

</summary-template>

**Done when** the three parts exist, part 1 fits one screen, and part 3 states the situation rather than
giving instructions.

### 5. Check

Run the edit pass in [references/readability-law.md](references/readability-law.md), then these three:

- A reader who stopped after part 1 can retell the change and its meaning.
- No severity words, no owners, no acceptance criteria. Those belong to an audit.
- Every row in the table carries something in the meaning column.

## Change words

Two sets, declared once, used in the table and nowhere else.

| Kind | When |
|---|---|
| **New** | It did not exist before. |
| **Changed** | Behaviour the reader already knew, now different. |
| **Fixed** | It was broken, and now it is not. |
| **Removed** | It is gone. |

| State | When |
|---|---|
| **Done** | Complete and verified. |
| **In progress** | Started, not finished. |
| **Not started** | Planned, untouched. |

Seven words, no synonyms, and no eighth invented mid-document. Where the document is not in English,
translate them once and stay in that translation.

## Language

Write the document in the language the user is using.

## Bold and line breaks

Bold marks a label or the headline claim; sentences stay plain. Three places earn it:

- the headline line at the head of part 1
- the change ID of anything still **In progress**, in the table
- the field name opening a line, where a part uses fields

Everything else stays plain: every other cell, every table header, every full sentence. The cap lives in
the readability law, clause 5.

Break a line where the reader's eye needs a fresh start:

- one field per line
- a blank line before and after every table and every heading
- one change per row; a change that needs two rows is two changes
- 3 sentences per paragraph at most, 120 characters per source line at most

## Anti-patterns

- A chronological dump. The default output, and the thing this skill replaces.
- Every change, with no meaning layer.
- Severity words, owners, or acceptance criteria. Those belong to an audit.
- A summary as long as the work it summarizes.
- Part 3 giving instructions. A summary reports what is open.
- A percentage with no denominator. Where a number earns its place, say what it is out of.
