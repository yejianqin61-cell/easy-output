---
name: easy-task-act
description: >-
  Use when a phase of a plan has to become work that gets done: 子任务, 任务文档, 开工, 执行这个 phase,
  开始实现, write the task briefs, work through this phase. Writes one short brief per task, then
  implements them one at a time, each ending in its own commit. Reached from easy-plan, and it closes by
  calling easy-summary.
---

# Easy task and act

**A task ends in a commit.** That one sentence sizes the task, names its proof, and decides when it is
finished.

This skill has two halves, and the order between them is the point: **write every brief in the batch
first, then implement.** The batch is a gate. An agent that starts coding after the first brief has
stopped planning and started hoping.

Read [references/readability-law.md](references/readability-law.md) before writing. Its twelve clauses
hold here.

## Output

Ask once: **Markdown, or a single-file HTML report?** For a batch of briefs, Markdown is nearly always
the answer. For the report, finish the Markdown first, then call the Skill tool with "easy-report".

## Parts 1 to 4: the brief

One document per task. Four parts, and no others.

### 1. Where this task sits

Three lines: the phase it belongs to with that phase's goal, what this task moves, and its edges. Name
what must be true before it starts, and what waits on it.

Codes travel with their names here as everywhere: `Phase 2 An admin can unlock`, `R-3 Let an admin
unlock a user`.

### 2. What the developer needs to know

Five blocks, each with a budget. This part decides whether the task lands: a fact written here goes
stale, and a path does not.

| Block | Write | Budget |
|---|---|---|
| **Read first** | 3 to 5 entries, `path — the question it answers` | 3 to 5 lines |
| **Settled** | the decisions this task must not reopen, each with where it lives | ≤4 lines |
| **Edges and seam** | what it touches, what it leaves alone, the seam it is tested at | ≤3 lines |
| **Run** | the exact test command and typecheck command for this task | ≤3 lines |
| **Unknowns** | where it will probably snag, and the trigger to stop and ask | ≤3 lines |

A path without a question is noise. These are entry points, not an inventory. Give the three to five
places a person handing this over would name. Then let the agent expand the list by searching from them.

### 3. The workflow

Numbered steps for this task alone. One action per step, and each step says what it produces. Five to
eight steps is normal. Step one is always **read part 2 and restate the task in one line**, because that
restatement is what the reading was for.

### 4. The test cases

A table, and no test code:

| Case | Input | Expected | Seam |
|---|---|---|---|
| 1 | two failed logins | the user can still log in | `login()` |

The expected value comes from somewhere independent: a known-good literal, a worked example, the plan. An
expectation that recomputes what the code does passes by construction, and can never disagree with it.

Five cases is usually enough. The tests themselves are written red-first in part 5, one case at a time.

<task-brief>

## 1. Where this task sits

- **Phase 1 A lock that actually locks**, whose goal is that a locked user cannot log in.
- **This task moves R-1 Lock out after 3 failed logins** into place: the counter reads and writes real
  data.
- **Starts after**: nothing. **Waits on it**: `Clear the deadline and keep the count`.

## 2. What the developer needs to know

**Read first**

- `src/auth/login.ts` — where the login path branches today, and where a refusal fits.
- `src/auth/failedAttempts.ts` — the threshold, the counting rule, and who reads them.
- `docs/adr/0007-session-storage.md` — why the session record exists, so the lock does not duplicate it.

**Settled**

- The lock is server-side. The plan refused a client-side check.
- The counter belongs to the user, not to the session.
- The threshold comes from the constant, and not from configuration yet.

**Edges and seam**

- Touches `src/auth`. Leaves the admin surface alone.
- Seam: the existing `login()` entry point, and no new seam.

**Run**

- `npm test -- src/auth`, then `npm run typecheck`.

**Unknowns**

- Whether two failures can interleave and lose a count. If the read and the write cannot be made atomic
  here, stop and say so.

## 3. The workflow

1. Read the three files above, then restate this task in one line.
2. Write the failing test for case 1, at the `login()` seam.
3. Count the failure, and write the deadline at the threshold. Run the test.
4. Add cases 2 and 3, red first, then green.
5. Run `npm test -- src/auth`, then `npm run typecheck`.
6. Commit.

## 4. The test cases

| Case | Input | Expected | Seam |
|---|---|---|---|
| 1 | two failed logins | the user can still log in | `login()` |
| 2 | three failed logins | the third returns the lock error | `login()` |
| 3 | three failures, then the right password | still the lock error | `login()` |

</task-brief>

## Part 5: the act

Six steps. Each ends on a check you can make.

### 1. Write the whole batch

One brief per task in the phase, using the template above. If the phase has no plan yet, call the Skill
tool with "easy-plan" first.

**Done when** every task in the phase has a brief, and every brief fits its budgets.

### 2. Gate

Write no code until the batch is complete. This gate is the reason the two halves live in one skill.

**Done when** the batch is complete.

### 3. Take the frontier

Work the tasks whose predecessors are done, one at a time. Any task with nothing left in front of it can
start, which for a linear phase means top to bottom.

**Done when** one task is chosen, and you can say why it is the next one.

### 4. Red, then green

Inside one task: write one failing test at the seam from part 2, then the least code that passes it.
Repeat per case. Test only at the seam the brief names, and keep the slices vertical: one test, one
implementation, then the next case.

**Done when** every case in part 4 is green, and the tests are still read as behaviour rather than
structure.

### 5. Commit

One commit per intent, in the conventional format. A failing test fixed afterwards earns its own
commit, because the next reader wants to see what broke.

**Done when** the working tree is clean, and a reader can tell from the log what changed and why.

### 6. Close the batch

Call the Skill tool with "easy-summary" and produce the batch summary: what changed, what it means, and
what is still open.

**Done when** the summary document exists, and every task in the batch is either committed or named as
unfinished.

## Commits

`type(scope): what changed`, imperative, lowercase type: `feat(auth): count failed logins and lock at
the threshold`.

- One commit per intent. A task usually makes one, and a task holding two intents makes two.
- A fix after a red test is its own commit, `fix(auth): ...`. The test and the fix never share a commit.
- The commit body carries what the reading changed. That is where findings live, because a brief is not
  edited once it is written.

## Stop and ask

Stop, and say so, when any of these holds:

- Reading part 2 changes the task.
- The seam the plan named does not exist, or sits lower than the plan claimed.
- A case cannot get an expected value from an independent source.
- The task needs a decision the plan did not make.

## Anti-patterns

- Starting the code before the batch is written.
- A brief written as paragraphs of prose. Blocks, and lines.
- A read-first list with no questions attached. That is an inventory, not a handoff.
- A test whose expected value recomputes what the code does.
- Tests written for imagined behaviour, before the seam has taught you anything.
- The red test and its fix sharing a commit.
- Editing a brief after it is written.
- Finishing the last task without calling `easy-summary`.
