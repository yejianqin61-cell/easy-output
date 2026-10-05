---
name: easy-registry
description: >-
  Use when a set of items has to stay current across many edits: 待办, TODO, 待确认, 决策册, 风险册,
  decision log, risk register, "keep this list up to date", "what is still blocking", "sort out this
  TODO". Maintains one row per item, amends by superseding rather than appending, and keeps the change
  log at the end. Reached from the other shapes when their output needs tracking.
---

# Easy registry

**A registry holds the current state of every item, once each. Amendments supersede.**

A registry is read on many different days, always by someone who wants to know what stands now. That is
what makes it the hardest shape in this set: every other document is written once, and a registry is
rewritten forever. The failure is always the same one. A new round appends its conclusion above the old
one, the old one stays, and the document starts arguing with itself.

Read [references/readability-law.md](references/readability-law.md) before writing. Its twelve clauses
hold here, and clauses 2, 3 and 12 carry most of the weight.

## Output

Ask once: **Markdown, or a single-file HTML report?** A list someone edits weekly is usually Markdown.
For the report, finish the Markdown first, then call the Skill tool with "easy-report".

## Kinds

One registry holds one kind of item, and the kind fixes the columns and the state words. Declare the
kind in the header; never mix two kinds in one table.

| Kind | A row is | State words | The columns that matter |
|---|---|---|---|
| **Work** 待办 | a thing decided, not done | Ready, In progress, Blocked, Done, Dropped | blocker, latest point, source |
| **Decision** 待裁 | a question for one person | Open, Settled, Refused | options, your call, delay cost, decider |
| **Risk** 风险 | something that may hurt | Watching, Happened, Closed | trigger, impact, mitigation |

Two registries of different kinds stay in two documents. That is not duplication: they have different
readers, and the work registry should not wait on a decision it cannot make.

## Process

Five steps. Each ends on a check you can make.

### 1. Collect the items

Sources: the conversation, the last audit's plans, the summary's open list, the tickets. An item nobody
wrote down still belongs here, because a registry is where promises are kept.

**Done when** every item has a code, a name, and a source.

### 2. Declare the vocabulary

Pick the kind, write its state words at the top, and use those words and no others.

**Done when** the state set is written down, and every row uses a word from it.

### 3. Write the rows

One row per item. The row holds the state; the argument lives in the source the row points at.

**Done when** every code appears with its name, every cell holds one short fact, and no item has two
rows.

### 4. Write the status line

The first screen states what stands now: how many items, which are blocking, and the next action.

**Done when** the status line and the rows agree. Recompute it from the rows, never from memory of what
the last round said.

### 5. Amend

On every later pass, work the protocol below.

**Done when** the body holds no strikethrough, no round number, and no second verdict, and the change log
carries one dated line per change.

## The amendment protocol

This is the whole skill. Everything above is a table.

1. **A state change edits the row.** The new word replaces the old one. The old one leaves.
2. **A meaning change closes the row and opens a new one.** When an item stops being the same item, close
   the old row as `Dropped` or `Closed`. The new row then carries `Supersedes W-4 Let an admin unlock a
   user`. Two rows tell one story, and no reader has to diff anything.
3. **Nothing is struck through.** A struck-through line asks the reader to reconstruct the present from
   the past. Strikethroughs, `(round N)`, `previously`, `corrected`, and `the last pass got this wrong`
   are the same defect wearing different clothes.
4. **The change goes to the change log**, one dated line, at the end of the document. That is the only
   place the past is allowed.
5. **The status line is recomputed.** After any amendment, read the rows and rewrite the first line. A
   stale first line is how a registry starts lying: it is the one sentence a reader trusts without
   checking.

## The change log

At the foot of the document, newest first, one line each:

```
- 2026-10-02: W-4 dropped; the plan moved it to the next round.
- 2026-10-01: W-3 blocked by W-2 Count a failed login, which the spike showed is the real order.
```

The header carries the date and the version. The change log carries what changed. The body carries only
what is true now.

<registry-template>

# Work registry — the auth change

**Now (2026-10-02)**: 4 items, 1 blocking. Next: W-1 Move the threshold and the counting rule into one
module.

State words, and no others: **Ready** · **In progress** · **Blocked** · **Done** · **Dropped**.

| ID | Item | State | Blocking | Latest | Source |
|---|---|---|---|---|---|
| W-1 | Move the threshold and the counting rule into one module | Ready | no | Phase 1 | plan, Phase 1 |
| W-2 | Count a failed login, and write the deadline | Ready | no | Phase 1 | plan, Phase 1 |
| W-3 | Check the deadline at the login entry | Blocked | yes, by W-2 Count a failed login | Phase 1 | plan, Phase 1 |
| W-4 | Let an admin unlock a user | Dropped | no | — | audit, R-3 Let an admin unlock a user |

## Change log

- 2026-10-02: W-4 dropped; the plan moved it to the next round.
- 2026-10-01: W-3 blocked by W-2 Count a failed login, which the spike showed is the real order.

</registry-template>

## Anti-patterns

These are the ways a registry dies, in the order they tend to appear:

- The registry that became a diary: strikethroughs, round numbers, and two conclusions in one body.
- A verdict in two places. They drift, and the day they disagree no reader can tell which half is
  current.
- The same item written into three tables, kept consistent by hand.
- A cell holding the argument. Past a line or two, the argument belongs in the source the row points at.
- A field whose whole content is a reference. The row says what happened; the reference adds depth.
- The change log in the header, ahead of the first fact.
- The status line at 65% of the document, under three tables of history.
- Emphasis on most of the rows. When every row is bold, no row stands out.
