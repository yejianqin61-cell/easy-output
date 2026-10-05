---
name: easy-plan
description: >-
  Use when a set of requirements needs an order to be built in: 施工计划, 开发计划, 实施方案, 拆阶段, 排期,
  implementation plan, build plan, "break this into phases", "how do we build this". Produces a plan in
  three parts: the requirements as a list, a rough approach for each one, and the phases with their
  tasks. `easy-task-act` expands those tasks afterwards.
---

# Easy plan

**A plan turns a requirement list into a queue of proofs.** Each phase exists to prove something, and
the plan is the order in which those proofs come cheap.

A plan is not a spec: the decisions were made there, and this file does not reopen them. A plan is not a
A plan is not a brief either: a task here is one line, and `easy-task-act` expands it later.

Read [references/readability-law.md](references/readability-law.md) before writing. Its twelve clauses
hold here.

## Output

Ask once, before writing: **Markdown, or a single-file HTML report?** Markdown is the default when the
user does not care. For the report, finish the Markdown first, then call the Skill tool with
"easy-report".

## Process

Five steps. Each ends on a check you can make.

### 1. Collect the requirements

Sources: the conversation so far, the spec, the plans from the last audit, the open tickets. A
requirement nobody wrote down still belongs here, because the plan has to carry it.

Give each one a code and a name: `R-1 Lock out after 3 failed logins`. The code is a handle; the name is
the content. Part 1 lists them, and nothing later in the document invents a requirement.

**Done when** every requirement has a code, a name, and a source.

### 2. Sketch the approach, one requirement at a time

Four lines each, and no more:

- **Approach**: the shape of the solution, in one or two sentences.
- **Touches**: the module or the area, not the file.
- **Test seam**: where this gets tested. Prefer a seam that exists, and prefer the highest one. The
  ideal number of new seams is zero.
- **Hard part**: what is most likely to go wrong, or what is still open.

Keep it rough. Name no file, quote no code, and settle no decision that belongs to the spec.

**Done when** every requirement has a seam, and no line names a file or contains code.

### 3. Cut the phases

Order by risk, not by layer. The phase that could invalidate the plan runs first, while changing course
is still cheap.

**Done when** every phase ends somewhere a person can see, and every requirement appears in at least one
phase.

### 4. Write the tasks

One line per task, verb first. The first task of a phase is the tracer bullet: a thin path through every
layer, so the phase proves itself on its first day.

No codes on tasks. The brief carries the whole task, and this list stays one line each.

**Done when** no task needs a second line, and each phase holds three to seven of them.

### 5. Check the spine

- Every requirement in part 1 appears in part 2 and in at least one phase.
- Every phase names the requirements it advances or hardens.
- Every phase carries a goal, tasks, a proof, and a "not here".

Then run the edit pass in the law.

**Done when** no orphans remain in either direction.

## The three parts

<plan-template>

## 1. Requirements

- **R-1 Lock out after 3 failed logins, for 5 minutes** — spec §2.1
- **R-2 Keep the counter when the lock is released** — spec §2.2
- **R-3 Let an admin unlock a user** — ticket #42

## 2. The approach, requirement by requirement

### R-1 Lock out after 3 failed logins, for 5 minutes

- **Approach**: count each failure, and write a lock deadline when the count reaches the threshold. The
  login path checks the deadline first.
- **Touches**: `src/auth`, and the `users` table.
- **Test seam**: the existing `login()` entry point. No new seam.
- **Hard part**: two failures arriving at once, and whether the count can miss one.

### R-2 Keep the counter when the lock is released

- **Approach**: releasing the lock clears the deadline, and leaves the count alone.
- **Touches**: `src/auth`.
- **Test seam**: the same `login()` entry point that R-1 Lock out after 3 failed logins uses.
- **Hard part**: the write order against the counter from R-1 Lock out after 3 failed logins.

### R-3 Let an admin unlock a user

- **Approach**: the admin action calls the same release path, and writes an audit line.
- **Touches**: `src/admin`, `src/auth`.
- **Test seam**: a new seam at the admin entry point. One new seam, and the lowest one that works.
- **Hard part**: which layer owns the permission check.

## 3. Phases

### Phase 1 — A lock that actually locks (R-1, R-2)

**Goal**: after three failures a user sees the lock message, and the correct password stops working
until the lock lifts.

**Tasks**

- Move the threshold and the counting rule into one module
- Count a failed login, and write the deadline at the threshold
- Check the deadline at the login entry, and refuse on a hit
- Release the lock by clearing the deadline, and keep the count
- Cover it end to end: three failures, lock, release, one more failure locks again

**Proof**: that test passes, and every acceptance item of R-1 and R-2 is met.
**Not here**: the admin path, and everything about concurrency.

### Phase 2 — An admin can unlock (R-3)

**Goal**: an admin unlocks a user from the back office, and the action leaves a trace.

**Tasks**

- Add the unlock action to the admin surface, calling the same release path
- Put the permission check in the route layer
- Write an audit line for each unlock

**Proof**: an unlocked user can log in immediately, and the audit line is there.
**Not here**: bulk unlock.

### Phase 3 — It holds under load (hardens R-1 Lock out after 3 failed logins)

**Goal**: concurrent failures do not lose a count, and the threshold comes from configuration.

**Tasks**

- Make the counter increment atomic
- Read the threshold and the duration from configuration
- Cover it with 20 concurrent failures, and assert the count is exactly 20

**Proof**: the concurrency test passes.
**Not here**: a distributed counter across instances.

</plan-template>

## Phase rules

A phase is the unit of proof, so it carries four things: **Goal**, **Tasks**, **Proof**, **Not here**.

- **A phase ends demoable.** The goal is something a person can see or do when the phase closes.
  "Refactor the auth module" is not a goal. "A locked user cannot log in" is.
- **Riskiest first.** Order by what could invalidate the plan, not by what is comfortable to build first.
- **One tracer bullet leads each phase.** The first task cuts a thin path end to end, so a phase that is
  going to fail fails early.
- **Every phase says how we know it landed.** A test, a command, or something a person can do. A feeling
  is not a proof.
- **Every phase fences what it is not.** "Not here" keeps the next phase from swallowing this one.

A phase holding fewer than three tasks merges with a neighbour. More than seven, and it is two phases
wearing one goal.

## Bold, breaks, words, codes

Bold marks a phase goal and the field name opening a line. Nothing else, and the cap lives in the
readability law, clause 5.

Break a line before every field, every task, and every phase. A phase delivered as one paragraph is a
phase the reader skips.

Use the common word, and the same word every time. `lock` stays `lock`; it does not become `restrict` or
`freeze` halfway down. Clause 9 of the law carries this.

Every code travels with its name: `R-3 Let an admin unlock a user`. The first mention teaches it, and
every later mention repeats it. A bare code sends the reader back to part 1, and the reader does not go
back. Clause 12 of the law carries this.

## Anti-patterns

- Phases named after layers. "Backend phase, frontend phase" proves nothing until the last day.
- A goal that is a task. "Add the lock table" is work, not proof.
- Tasks detailed enough to be briefs. That work belongs in `easy-task-act`.
- A phase with no proof, or a proof that is a feeling.
- The spec, retold. Those decisions were settled there.
- A requirement that appears in part 1 and nowhere else.
- A bare code.
