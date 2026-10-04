# easy-output

Makes an agent's engineering documents readable in minutes and dense enough to build from: project
analysis, evaluation, execution plans, specs, ADRs, runbooks. Verdict first, headings that answer the
reader's questions, an explicit scope fence, and ASD-STE100-grade clarity at ~80% strength.

Built on Andrej Karpathy's advice about LLM output, applied to the documents a person has to approve.
Sits as a readability layer over Matt Pocock's [`to-spec`](https://github.com/mattpocock/skills).

Follows the [Agent Skills](https://agentskills.io/) format. Markdown only; no scripts, no
dependencies.

[中文说明 →](README.zh-CN.md)

## Install

```bash
npx skills add yejianqin61-cell/easy-output -g
```

That is [Vercel Labs' `skills` CLI](https://github.com/vercel-labs/skills). It resolves the repo,
reads `SKILL.md` from the root, and installs to every agent it detects — Claude Code, Codex, Cursor,
OpenCode and ~75 others.

```bash
npx skills add yejianqin61-cell/easy-output -g -a claude-code -y    # target agents, non-interactive
npx skills add yejianqin61-cell/easy-output --list                  # preview the repo
npx skills use yejianqin61-cell/easy-output --skill easy-output --agent claude-code
npx skills update easy-output
npx skills remove easy-output
```

`-g` installs for every project; drop it for `./.claude/skills/`. Installation runs through symlinks,
so a `git pull` in the clone updates the skill; add `--copy` where symlinks are awkward.

Manual install:

```bash
git clone https://github.com/yejianqin61-cell/easy-output.git ~/.claude/skills/easy-output   # global
git clone https://github.com/yejianqin61-cell/easy-output.git .claude/skills/easy-output     # project
```

## What it produces

| Document | Reader | The question it answers |
|---|---|---|
| **Project analysis** 项目分析 | whoever commits effort or budget | what is the state, what it costs, what we recommend |
| **Evaluation** 评估 | the decision-maker | which option wins, on what criteria, what would reverse it |
| **Execution plan** 施工计划 | the executor and the approver | what happens, in what order, how we know it is done |
| **Spec** 规格 | the implementing agent, plus the reviewer | what problem, what solution, which decisions are locked |
| **ADR** 决策记录 | a future maintainer | why it is like this |
| **Runbook** 操作手册 | someone under time pressure | how to run it, undo it, and tell that it broke |

Skeletons, section lists, and length budgets for all six are in
[`references/documents.md`](references/documents.md).

## The document contract

Eight rules, applied to every type. The first one is what makes a document approvable:

1. **Decision-first.** The verdict — recommendation, cost, main risk, the ask — lands in the first
   ≤150 words. A reviewer who stops there still knows where the document stands.
2. Headings are the reader's questions, in the order the reader asks them.
3. One screen, one idea.
4. An out-of-scope section naming what was deliberately declined.
5. Assumptions labelled as assumptions; open questions listed with a way to resolve each.
6. Numbers carry units, sources, and a date.
7. A status line: type, date, status, the decisions this document locks.
8. A dense body with a navigable surface — the summary and headings are the human interface.

## How it works

Four steps, in order. The first three are free.

| Step | What it does |
|---|---|
| **Cut** | Drops preamble, restated questions, recaps, hedges. Prefers a table to a paragraph for parallel items. |
| **Clarify** | One idea per sentence, active voice, one word for one meaning, no nominalizations. ASD-STE100 at ~80%: its writing rules, ordinary vocabulary, one clearly marked analogy. |
| **Shape** | Picks the document type, writes the verdict, orders headings as the reader's questions, fences the scope. |
| **Render** | Tables and one or two diagrams where they replace paragraphs; a single-file HTML report when the document gets re-read or circulated. |

The rungs run 0–3: a few sentences, a cut document, a document plus structure, a document plus an
HTML report. Rung 1 carries the value. Stop at the rung where the human can approve the document.

## Usage

The skill triggers on its own when you ask for a document or flag that one is unreadable. It also
fires before the agent sends a draft that has run long.

```
Write up an analysis of our auth layer and what we should do.   → project analysis, verdict first
Evaluate these three queue services for our workload.           → criteria and weights before scores
Write the migration plan for moving off RabbitMQ.               → phases, per-phase verification, rollback
Turn what we just decided into a spec.                          → spec plus a decision summary
Why did we pick Postgres? Write it down.                        → ADR, one decision
This doc is 4 pages and I still don't get it.                   → cut a third, verdict at the top
Explain how TCP slow start works.                               → the secondary case: verdict + diagram
```

Prompts for each document type are in [`references/prompt-templates.md`](references/prompt-templates.md).

## Structure

```
easy-output/
├── SKILL.md                    # rungs, 10 operating rules, 5 selection questions, routing table
└── references/
    ├── documents.md            # the document contract and the six shapes
    ├── conciseness.md          # cutting: verdict first, length budgets, techniques, anti-patterns
    ├── writing.md              # ASD-STE100 rules, the 80% dial, before/after pairs
    ├── diagrams.md             # relation → diagram type; ASCII, Mermaid, SVG
    ├── html-report.md          # rung 3: how to fill the template, class vocabulary
    ├── report-template.html    # the fixed design system the agent fills in
    ├── prompt-templates.md     # prompts per document type, cut pass first
    ├── checklist.md            # the reviewer's first pass, per rung
    └── spirit.md               # source post, principles, and what this repo takes from it
```

`SKILL.md` holds the routing and pulls in a `references/` file only when the rung calls for it.

## Operating rules

- Verdict first. A document whose conclusion sits on the last page gets sent back.
- Cut before decorating. A 900-word draft that 150 words could carry has a text problem.
- Criteria before scores. An evaluation with no reversal condition is advocacy.
- Rollback before work. A plan with no per-phase verification cannot be executed by anyone else.
- Label assumptions, source numbers, fence the scope.
- Walk the reviewer's first pass on your own draft, and open the report before delivering it.
- Close every Markdown delivery with one question: would you like this as an HTML report? Build it
  only on a yes.
- Add no CSS to the report template, and ship no artifact with `{{` markers still in it.
- Ask before a render that takes more than a few minutes, and read credentials from the environment.

## Provenance

Two sources. The writing standard comes from Andrej Karpathy's post of 2 October 2026 on making LLM
output easier to understand: <https://x.com/karpathy/status/2105819303471976479>, quoted in full in
[`references/spirit.md`](references/spirit.md). The document shapes build on
[`to-spec`](https://github.com/mattpocock/skills) by Matt Pocock (MIT), which turns a conversation into
a spec for the agent that will implement it; this repository adds the layer that makes the same
document auditable by a human. Neither author has reviewed or endorsed this repository.

ASD-STE100 is published by the ASD at <https://www.asd-ste100.org/>.
[`references/writing.md`](references/writing.md) paraphrases its well-known rules for practical use.

## License

[MIT](LICENSE).

## Contributing

Issues and PRs welcome; keep them small. Contributions that land well: a sharper before/after STE
pair, a document shape that earns its sections, a verification step that caught a real failure, a
corrected fact or licence detail. Keep it dependency-free, keep `SKILL.md` thin, and keep this README
short — it is the first thing a reader sees.
