---
name: easy-audit
description: >-
  Use when a completed work round needs auditing against what it promised, or a change needs reviewing
  against its spec. Produces an audit document in three parts: last round's requirements with a
  completion percentage each, this round's defects on two axes, and one improvement plan per defect.
  Triggers on 审计, 审计报告, 复核这一轮, 验收上一轮需求, 这一轮做得怎么样, audit report, round review, and
  "did we deliver what we said". Downstream of mattpocock/skills' code-review, and it runs with
  code-review absent.
---

# Easy audit

Adapted from [`code-review`](https://github.com/mattpocock/skills) (MIT, © 2026 Matt Pocock): the same
two axes, Standards and Spec, and the same parallel sub-agents. What this skill adds is the document
the round closes on, and the ability to run with `code-review` absent.

The document is three parts and no preamble. A reader who stops after the first screen knows how much
of last round's promise landed, and what stands in the way now.

The plans in part 3 are promises. When one needs tracking across rounds, call the Skill tool with
"easy-registry".

Read [references/readability-law.md](references/readability-law.md) before writing. Its twelve clauses
hold here, and its edit pass runs last.

## Output

Ask once, before writing: **Markdown, or a single-file HTML report?** Markdown is the default when the
user does not care.

For the report, finish the Markdown first, then call the Skill tool with "easy-report". It owns the
template and the fill-in contract, and it keeps the facts identical.

## Process

Five steps. Each ends on a check you can make.

### 1. Pin the round

Both ends of the round are commits. The start is whatever the user names: a commit, a tag, a branch, or
"since the last audit". The end is `HEAD`.

A tree with uncommitted changes has no end to audit. The diff you read is not the diff anyone else can
read, and it moves while you work. When the tree is dirty, say so in one line and stop, or ask the user
to commit first.

Capture `git diff <start>...HEAD` and `git log <start>..HEAD --oneline`.

**Done when** `git rev-parse <start>` resolves, `git status --porcelain` is empty, and the diff is
non-empty. Fail here, in one line, rather than discovering an empty round three steps later.

### 2. Collect last round's requirements

Sources, in order: the previous audit's part 3 (one plan per defect). Then this round's spec or tickets,
issue references in the commit messages, or a path the user passed. A requirement that produced no plan
and no ticket still belongs in the table, because it was promised.

**Done when** every requirement carries a source reference and an acceptance list.

### 3. Run the two axes

Standards and Spec, as parallel sub-agents where the platform supports it, so neither pollutes the
other's context. Where it does not, run the axes one after the other, and record in the document which
way you ran them.

**Spec axis** takes the requirements from step 2 one at a time: which acceptance items are met, which
are partial, which are absent. Quote the requirement behind every finding.

**Standards axis** takes whatever the repo documents about how code is written, plus the smell baseline
in [references/smell-baseline.md](references/smell-baseline.md). Three rules bind it:

- The repo overrides. A documented standard wins, and where it endorses something the baseline flags,
  suppress the smell.
- Every smell is a judgement call, labelled as one (`possible Feature Envy`), never a hard violation.
- Tooling-enforced rules stay out of the report.

Sub-agent briefs:

- **Standards** — the diff command, the commit list, the standards files, and the smell baseline
  verbatim. "Report, per file and hunk: (a) each documented standard the diff breaks, citing the
  standard; (b) any baseline smell, named and quoted. Mark documented breaches as hard and baseline
  smells as judgement calls. Skip what tooling enforces. Under 400 words."
- **Spec** — the diff command, the commit list, and the requirements from step 2. "Report: (a)
  acceptance items missing or partial; (b) behaviour nobody asked for; (c) items that look implemented
  and are wrong. Quote the requirement for each. Under 400 words."

**Done when** both axes report, and every defect names a file and a line. Every defect's evidence came
from a command you ran, and that a reader can run again to see the same output. A defect you cannot
reproduce is not a defect yet: re-run it, and cut it if it does not hold.

### 4. Write the document

Use the template below. Part 1 lands first, so the reader meets the state of the promise before they
meet the complaints.

<audit-template>

## 1. Last round's requirements

**This round: 3 requirements, 1 delivered, 55% average completion.**

| # | Requirement | Source | Delivered | Completion | Evidence |
|---|---|---|---|---|---|
| R-1 | Lock out after 3 failed logins, for 5 minutes | spec §2.1 | Delivered | **100%** | `auth.ts:88`, test `auth.test.ts:41` |
| R-2 | Keep the counter after the lock is released | spec §2.2 | Partial | 60% | counter kept; release logic missing at `auth.ts:104` |
| R-3 | An admin can unlock a user manually | ticket #42 | Not delivered | 0% | scheduled for the next round |

## 2. Defects this round

| ID | Axis | Defect | Location | Severity |
|---|---|---|---|---|
| D-1 | Spec | Lock release does not clear the counter | `auth.ts:104` | Blocking |
| D-2 | Standards | Failed-login counting duplicated | `auth.ts:80`, `session.ts:31` | Minor |

### D-1 Lock release does not clear the counter

- **Symptom**: `releaseLock()` restores the initial `attempts` value, and the failures already recorded
  in the database stay.
- **Evidence**: `auth.ts:104`; acceptance item 2 of R-2 does not pass.
- **Impact**: after one lockout, every later failure locks the user again immediately.
- **Criterion**: spec §2.2 asks for the counter to survive release, and the implementation does the
  opposite.

### D-2 Failed-login counting duplicated

- **Symptom**: one counting rule is written in two modules, with the threshold written out in each.
- **Evidence**: `auth.ts:80` and `session.ts:31`.
- **Impact**: changing the threshold means changing two places, and the two already disagree (3
  attempts against 5).
- **Criterion**: smell baseline, Duplicated Code (a judgement call, not a hard violation).

## 3. Improvement plans

One plan per defect, IDs matched. A plan says what to build, and how you will know it works. `easy-plan`
turns a set of plans into phases and one-line tasks; this part stops at the plan. A plan that needs more
room becomes its own ticket.

### P-1 ← D-1 Clear the counter when the lock is released

- **What to build**: `releaseLock()` clears `attempts`, with an end-to-end test covering lock, release,
  then another failure.
- **Touches**: `src/auth/**`.
- **Acceptance**: [ ] the counter is 0 after release　[ ] the new test fails against the old
  implementation　[ ] every acceptance item of R-2 passes.
- **Blocked by**: nothing, it can start now.
- **Out of scope**: R-3 Let an admin unlock a user, next round.

### P-2 ← D-2 Gather the counting rule in one place

- **What to build**: move the threshold and the counting rule into `failedAttempts.ts`, and make both
  call sites reference it.
- **Touches**: `src/auth/**`, `src/session/**`.
- **Acceptance**: [ ] the threshold is defined once　[ ] both test files stay green.
- **Blocked by**: P-1 Clear the counter when the lock is released, same file area.
- **Out of scope**: a configurable source for the threshold.

</audit-template>

**Done when** the three parts exist, every defect has exactly one plan, and every plan names its
acceptance items.

### 5. Verify

Count the twelve clauses in [references/readability-law.md](references/readability-law.md) and run its
edit pass, then check the four things this shape adds:

- Every percentage traces to acceptance items.
- Every defect's evidence reproduces when the command is run again.
- Every defect in part 2 has exactly one plan in part 3, with the IDs lining up.
- Part 1 comes first.

## Completion percentages

A percentage is a claim, so it needs a denominator. Take the verified acceptance items over the total
acceptance items, rounded to 5%.

100% means every acceptance item passed, with evidence in the same row. A requirement whose acceptance
items you cannot enumerate gets `—` in the cell, plus one line naming what would make it countable.

Keep one rounding rule across the rows. A 53% beside a 55% invites a comparison the evidence cannot
support.

## Delivery words

Three, declared once, used in the Delivered column and nowhere else:

| Word | When |
|---|---|
| **Delivered** | Every acceptance item passed. |
| **Partial** | Some passed. |
| **Not delivered** | None passed, or the work has not started. |

## Severity words

Four, declared once, used in the Severity column and in the plan headings:

| Word | When |
|---|---|
| **Blocking** | The round cannot land until this is fixed. |
| **Major** | Correctness or data is at risk. |
| **Minor** | Convention or maintainability. |
| **Note** | Worth knowing. |

No synonyms, and no fifth word invented mid-document.

## Language

Write the document in the language the user is using. The seven words above are fixed by this skill.
Where the document is not in English, translate them once and use those translations everywhere.

## Bold and line breaks

Bold marks a label or a headline claim; sentences stay plain. Three places earn it:

- the field name opening a line in a defect and in a plan (`**Symptom**`, `**Acceptance**`)
- the total line at the head of part 1
- the percentage below 100, and the defect ID scored Blocking

Everything else stays plain: every other cell, every table header, every full sentence. The cap lives in
the readability law, clause 5.

Break a line where the reader's eye needs a fresh start:

- one field per line inside a defect and inside a plan
- a blank line before and after every table and every heading
- one defect per `###` section
- 3 sentences per paragraph at most, 120 characters per source line at most

## Anti-patterns

- A completion percentage with no acceptance list behind it.
- Part 2 opening the document.
- The same finding written twice, in part 2 and again in part 3.
- A plan that restates its defect instead of saying what changes.
- Twelve defects where three decide the round.
- A defect with no location. "Poor error handling" is a mood.
