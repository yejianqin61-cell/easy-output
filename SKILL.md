---
name: easy-output
description: >
  Use when an agent produces a document a human must read, review, approve, or act on: project
  analysis, evaluation and option comparisons, execution plans, specs, ADRs, runbooks, hand-off
  notes, PR descriptions. Enforces a decision-first summary, a heading per reader question, an
  explicit scope fence, labelled assumptions, and ASD-STE100-grade clarity at ~80% strength with
  strict cutting. Tables, diagrams and single-file HTML reports serve as compression, never as
  decoration.

  Trigger when the user asks for 项目分析/评估/评估报告/方案对比/施工计划/实施方案/设计文档/需求文档/复盘/写文档,
  or says "write a spec", "write up an analysis", "evaluate these options", "write the plan",
  "make this readable", "too long", "tl;dr", "simplify this", "ASD-STE100", "output in HTML".
  Apply it to a draft before it is sent, whenever that draft has run long or buried its conclusion.

  Don't use for writing code, for one-line facts, or when the output format is already fixed.
license: MIT
compatibility: No dependencies. Writes Markdown, plus optional SVG diagrams and single-file HTML reports built from the bundled report template.
metadata:
  author: easy-output contributors
  version: 0.3.0
  category: document-creation
  pattern: context-aware
  tags: [documents, spec, analysis, evaluation, execution-plan, adr, runbook, html-report, readability, conciseness, ste100]
  source: "Applies Andrej Karpathy's post on making LLM output easier to understand (https://x.com/karpathy/status/2105819303471976479) to engineering documents, and sits as a readability layer over mattpocock/skills' to-spec (https://github.com/mattpocock/skills, MIT). Independent work; endorsed by neither author."
---

# easy-output

**Engineering documents a human can read in minutes, holding the density the agent needs.**

The main case: the agent writes the deliverable — project analysis, evaluation, execution plan, spec,
ADR, runbook — and a person has to approve it or work from it. This skill makes that document
auditable fast: **cut, clarify, structure**, and only then render it differently.

Explaining a topic in chat stays supported as the secondary case.

## The rungs

| Rung | Output | Adds | Cost |
|---|---|---|---|
| 0 | A few sentences | speed, diffs, grep | seconds |
| 1 | A written document: cut, constrained English | the document contract | — |
| 2 | Plus tables and one or two diagrams | compression, structure | minutes |
| 3 | Plus a single-file HTML report | navigability, badges, print, circulation | minutes |

Rung 1 carries the value. Rung 2 earns its place by replacing paragraphs. Rung 3 suits documents that
get re-read, circulated, or carry several tables. **Stop at the rung where the human can approve the
document.**

**Rung 3 is a fill-in job, not a design job.** Copy
[references/report-template.html](references/report-template.html), replace its slots, and leave its
`<style>` block untouched. The design system is not yours to invent, and it is the reason the output
looks considered: roughly 60% of the finished page is that fixed stylesheet. Fill it, do not author it.

## Operating rules (always in force)

1. **Cut first.** Delete what does not change what the reader knows or does: preamble, restating the
   question, recaps in short documents, hedges. Read
   [references/conciseness.md](references/conciseness.md).
2. **Then make it clear.** One idea per sentence, active voice, short sentences, one word for one
   meaning, no nominalizations. Default: **ASD-STE100 at about 80%** — the writing rules, ordinary
   vocabulary, one clearly marked analogy. Read [references/writing.md](references/writing.md).
3. **Shape before prose.** Name the document type, publish the verdict in the first ≤150 words, make
   every heading a question the reader has, and name the scope fence. Read
   [references/documents.md](references/documents.md).
4. **Keep facts labelled.** Numbers carry units, sources, and a date. Assumptions are labelled
   assumptions. Open questions are listed with a way to resolve each. Check the facts that carry the
   argument against a primary source before delivering.
5. **The artifact is the answer.** For rung 3, give the path, how to open it, and the verdict — do not
   restate the document. At rung 1/2 the reply *is* the document: write it well and stop.
6. **Self-contained or it does not count.** Single file; inline CSS/JS; no build step; opens from
   `file://`; no keys, tokens, or private paths inside.
7. **Verify before you deliver.** Run the reviewer's first pass from
   [references/documents.md](references/documents.md) on your own draft. For rung 3, open the report,
   confirm it renders, and confirm that no `{{` or `<!--` marker survived. When this environment
   cannot verify a format, ship a plainer one you can verify. Gate:
   [references/checklist.md](references/checklist.md).
8. **One artifact per request.** Write to a sensible path (`./<slug>.md`, `./<slug>.html`). No
   framework, no maintenance burden, no repo to clean up afterwards.
9. **Close every document delivery with one question.** When the user asked for a Markdown document —
   or asked for "a document" without naming a format — finish the work, then ask **once**, in one
   line: *"Want this as an HTML report you can circulate?"* Ask every time, including when the
   document looked short. Build nothing until the answer is yes: the ask is required, the artifact is
   not.
10. **A dedicated skill changes *how*, never *which rung*.** Use a diagramming, document, or specs
    skill to produce the rung already chosen — it does not raise the rung by itself.

## Choosing, in five questions

1. **Is this a document to be approved or worked from, or an answer to a question?** A document → the
   shapes in [documents.md](references/documents.md). A question → rung 0/1 and stop.
2. **Which shape fits?** Analysis, evaluation, execution plan, spec, ADR, runbook.
3. **What must the reader be able to stop after?** That sentence is the summary at the top.
4. **Does structure compress it?** Three or more parallel items → table. A flow, state, or structure →
   one diagram.
5. **Will it be re-read, circulated, or compared?** Those documents earn a single-file HTML report.
   Ask before building it.

## Routing table

| The request is… | Go to | Read |
|---|---|---|
| **A deliverable document: analysis, evaluation, plan, spec, ADR, runbook** | Rung 1 + the matching shape | [documents.md](references/documents.md) + [conciseness.md](references/conciseness.md) + [writing.md](references/writing.md) |
| **Anything you are about to write** | cut it, then check clarity — never skipped | [conciseness.md](references/conciseness.md) + [writing.md](references/writing.md) |
| A comparison or a trade-off between options | Evaluation shape: criteria before scores | [documents.md](references/documents.md) |
| A procedure someone else will execute | Execution plan or runbook shape | [documents.md](references/documents.md) |
| Structure, flow, state, sequence, or a decision matrix | Rung 2 — diagram | [diagrams.md](references/diagrams.md) |
| A report the user wants to re-read, circulate, or compare | Rung 3 — **fill the shipped template** | [html-report.md](references/html-report.md) + [report-template.html](references/report-template.html) |
| A term, contract, or spec the reader must quote or grep | Rung 1 | [writing.md](references/writing.md) |
| "Explain how X works" | Rung 1 verdict plus one diagram | [writing.md](references/writing.md) + [diagrams.md](references/diagrams.md) |
| One fact | Rung 0. Answer it. | — |

**Tie-break: prose and structure compose, they do not compete.** Tables and diagrams sit inside the
document at the point where they replace paragraphs.

Other references, opened when relevant: [prompt-templates.md](references/prompt-templates.md) when the
user wants a reusable prompt; [spirit.md](references/spirit.md) when the request is about the approach
itself.

## Worked routing

| Request | Output |
|---|---|
| "Write up an analysis of our auth layer and what we should do." | Project analysis; verdict first, options table, out of scope, then the HTML question |
| "Evaluate these three queue services for our workload." | Evaluation; criteria and weights published before the scorecard |
| "Write the migration plan for moving off RabbitMQ." | Execution plan; phases with per-phase verification, rollback written up front |
| "Turn what we just decided into a spec." | Spec; to-spec sections plus a decision summary and rejected alternatives |
| "Why did we pick Postgres? Write it down." | ADR; one decision, consequences, reopen condition |
| "This doc is 4 pages and I still don't get it." | Cut a third, add the verdict at the top, restructure the headings |
| "Just give me the Markdown." | Write the Markdown, then ask once about the HTML report |
| "Explain how TCP slow start works." | Secondary case: tight verdict plus one diagram |
| "What port does the health check use?" | One line |

## Default move

For a document request: ① pick the shape, ② write the ≤150-word verdict, ③ cut the body hard at ~80%
STE, ④ add a table or one diagram where it replaces two paragraphs, ⑤ close with the HTML question in
one line.

## Non-negotiables

- A document whose conclusion sits on the last page gets sent back.
- No section that answers a question the reader does not have.
- No assumption written as a fact, and no scorecard without published criteria.
- No execution plan without rollback and per-phase verification.
- No Markdown-only delivery that ends without the HTML question, and no HTML report built before the
  answer.
- No CSS added to the report template, and no artifact shipped with `{{` markers still in it.
- No artifact delivered unopened, and no credential written inside one.
