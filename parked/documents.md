# Rung 1 — Engineering documents

A document here is read by a human who has to **approve it, act on it, or supervise the work that
follows**. That reader sets the design constraints.

[`to-spec`](https://github.com/mattpocock/skills) (MIT, Matt Pocock) optimizes a spec for the agent
that will implement from it: dense, reference-heavy, complete. This skill keeps that density and adds
the layer that makes the same document **auditable by a human in about two minutes** — a
decision-first summary, headings that are the reader's questions, an explicit scope fence, and named
assumptions.

## The document contract

The ten laws in [RULES.md](../RULES.md) hold for every type below: the verdict in the first screen, the
present state with no edit trail in the body, one verdict in one place, cells that hold facts, scarce
emphasis, one idea per line, references that supplement statements, no cross-section assembly, one
word for one meaning, no claim without a criterion. On top of them, five shape-level rules:

1. **Headings are the reader's questions**, in the order the reader asks them. Where the reader has
   no such question, the section stays out.
2. **Scope fence.** A named out-of-scope section listing what was deliberately declined. Reviewers
   read it first, and it is the cheapest place to catch a wrong decision.
3. **Unknowns get their own line.** Assumptions are labelled assumptions; open questions are listed
   with the way to resolve each. A guess in the indicative mood is the most expensive defect in the
   document.
4. **Status line at the top.** Document type, date, status (draft / for review / approved), and the
   decisions this document locks.
5. **Dense body, navigable surface.** Keep the body as dense as the implementing agent needs. The
   summary and the descriptive headings are the human interface to it.

## The six shapes

| Type | Reader | The question it answers | Budget |
|---|---|---|---|
| **Project analysis** 项目分析 | whoever commits effort or budget | what is the state, what does it cost us, what do we recommend | 600–1200 words + tables |
| **Evaluation** 评估 | the decision-maker | which option wins, on what criteria, and what would reverse the answer | 400–1000 words + scorecard |
| **Execution plan** 施工计划 | the executor and the approver | what happens, in what order, with what prerequisites, and how we know it is done | steps dominate, prose minimal |
| **Spec** 规格 | the implementing agent, plus the reviewing human | what problem, what solution, which decisions are already made | dense, no cap, summary required |
| **ADR** 决策记录 | a future maintainer | why is it like this | 200–500 words, one decision |
| **Runbook** 操作手册 | someone under time pressure | how to run it, undo it, and tell that it broke | commands, zero narrative |

## Project analysis

1. **Verdict** — recommendation, cost, main risk. ≤150 words.
2. **Current state** — the facts needed to judge the verdict, with numbers and sources.
3. **Problem** — what the current state costs, quantified where possible.
4. **Options** — a table: option, cost, what it buys, what it breaks.
5. **Recommendation and rationale** — why this option, and which alternatives were closed off.
6. **Risks and unknowns** — each with a mitigation or a resolution path.
7. **Out of scope.**

Avoid a chronological account of how the analysis was performed. The reader wants the state, the
options, and the call.

## Evaluation

1. **Verdict and scorecard** — the winner and the weighted table, up top.
2. **Criteria and weights** — published before the scores, with the reason behind each weight.
3. **Candidate table** — one row per candidate, one column per criterion.
4. **Evidence per criterion** — only the evidence that moves the ranking.
5. **Sensitivity** — what would reverse the decision: a named threshold, a missing datum, a price change.
6. **Unknowns and how to resolve them.**
7. **Out of scope.**

Three rules hold an evaluation together:

- Criteria are published before scores. A scorecard written criteria-last is an argument wearing a table.
- Every score traces to evidence in the same document, or is labelled as judgement.
- The sensitivity section is mandatory. An evaluation with no reversal condition is advocacy.

## Execution plan

1. **Objective and definition of done** — the end state, in checkable terms.
2. **Prerequisites and assumptions** — access, approvals, upstream work, environment.
3. **Phases** — numbered steps, imperative, one action per step, each with its expected result. Every
   phase closes with a verification step.
4. **Interfaces and handoffs** — who receives what, when, in what form.
5. **Rollback** — the way back, per phase.
6. **Risks and mitigations.**
7. **Not doing / out of scope.**

Three rules:

- Every step is executable by someone holding only this document.
- Verification lives inside each phase, on the spot where it applies.
- Rollback gets written before the work starts.

## Spec

Runs the [`to-spec`](https://github.com/mattpocock/skills) section set with two additions that make it
auditable by a human:

1. **Decision summary** at the top: ≤150 words covering the shape of the solution and what was refused.
2. **Every decision carries the alternative it beat**, on the same line. Rejected alternatives teach a
   reviewer more than the accepted ones.

Sections: problem statement, solution, decisions made (each with its rejected alternative), testing
decisions, out of scope, open questions. Keep the body dense and reference-heavy — the implementing
agent reads it end to end, and the summary plus headings are the human interface.

## ADR

Title is the decision ("Use X for Y"). Then: status and date; context in three to five sentences (the
forces at play); the decision; alternatives considered and why they lost; consequences (what gets
easier, what gets harder, what is now constrained); and the condition that would reopen it.

One decision per ADR. The consequences section is what pays for the file.

## Runbook

What it does and when to use it; prerequisites and access; numbered steps, each with the exact command
and the expected output; verification; rollback; failure modes and escalation; out of scope.

Imperative sentences, one action per step, zero narrative. The reader arrives under pressure, so the
first screen states the effect and the risk.

## The reviewer's first pass

What a reviewer checks, in order, inside about two minutes:

1. The verdict — and whether they can disagree with it using only the summary.
2. The out-of-scope section.
3. The assumptions and open questions.
4. The numbers that carry the argument.
5. Whether every heading answered a question they actually had.

Build the document so that pass succeeds.

## Anti-patterns

- The wall: a dense analysis whose conclusion appears on the last page.
- Background that restates the request.
- An evaluation whose criteria were written after its scores.
- A plan with no rollback and no per-phase verification.
- A spec asserting decisions nobody made.
- An assumption written as a fact.
- A "conclusion" that summarizes the document instead of stating the call.
- Padding to look thorough. Exhaustiveness is a cost the reader pays.
