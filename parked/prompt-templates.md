# Prompt templates

Copy, paste, adapt the bracketed parts. Order matters: **cut, clarify, shape, then render.**

Templates 0–2 carry the most value and cost nothing.

## 0. Universal opener

> Before you answer, make this a document I can approve in two minutes. Open with the verdict — the
> recommendation, its cost, its main risk, and what you need from me — in 150 words or less. Make
> every heading a question I have. Give me an out-of-scope section, and label every assumption.
> Cut anything that does not change what I know or do. Add a table or a diagram where it replaces two
> paragraphs. Offer me an HTML report if the document will be re-read, and ask before anything that
> takes more than a couple of minutes.

## 1. Cut and rewrite

> Rewrite the text below so I can approve it, keeping every fact I need.
>
> - Verdict in the first one or two sentences.
> - Delete the preamble, the restatement of my question, recaps, hedges, and "it's worth noting".
> - One idea per sentence. Active voice. No nominalizations.
> - Three or more parallel items become a list; items compared on the same attributes become a table.
> - Target length: [150 words / one screen]. Tell me in one line if it must run longer.
> - Then list what you deleted and why. Flag anything that turned out to matter.
>
> [paste text]

## 2. Retrofit an existing document

> This document is [N] pages and I still cannot approve it. Rewrite it: verdict in the first 150
> words, headings turned into my questions, a third of it cut, every assumption labelled, an
> out-of-scope section added. Leave the facts and the numbers unchanged.

## 3. Project analysis

> Write a project analysis of [subject].
>
> - Verdict first: recommendation, cost, main risk, in ≤150 words.
> - Current state: the facts and numbers needed to judge that verdict, with sources.
> - Problem: what the current state costs, quantified where possible.
> - Options: a table of option / cost / what it buys / what it breaks.
> - Recommendation and rationale, including which alternatives you closed off.
> - Risks and unknowns, each with a mitigation or a resolution path.
> - Out of scope.
>
> Target [600–1200] words. Skip the chronological account of your research.

## 4. Evaluation

> Evaluate [candidates] for [purpose].
>
> - Publish the criteria and their weights **before** any scores.
> - Scorecard: one row per candidate, one column per criterion, weighted total.
> - Evidence per criterion — only the evidence that moves the ranking.
> - Sensitivity: what would reverse the decision. Name the threshold.
> - Unknowns, each with a way to resolve it.
> - Out of scope.
>
> Mark judgement as judgement, and trace every score to evidence in this document.

## 5. Execution plan

> Write the execution plan for [goal].
>
> - Objective and a checkable definition of done.
> - Prerequisites and assumptions.
> - Phases: numbered steps, imperative, one action each with its expected result. Every phase closes
>   with a verification step.
> - Interfaces and handoffs.
> - Rollback per phase, written before the work starts.
> - Risks and mitigations, then what we are not doing.
>
> Every step must be executable by someone holding only this document.

## 6. Spec (to-spec compatible)

> Turn what we decided into a spec. Do not interview me; synthesize what is already settled.
>
> - Decision summary at the top, ≤150 words: the shape of the solution and what was refused.
> - Problem statement, solution, decisions made, testing decisions, out of scope, open questions.
> - Each decision on one line, with the alternative it beat beside it.
> - Keep the body dense — the implementing agent reads it end to end.

## 7. ADR

> Write an ADR for [decision]. Title = the decision. Status and date. Context in three to five
> sentences. The decision. The alternatives and why they lost. Consequences: what gets easier, what
> gets harder, what is now constrained. The condition that would reopen it. 200–500 words, one
> decision per file.

## 8. Runbook

> Write the runbook for [operation]. Imperative sentences, one action per step, each with the exact
> command and the expected output. Then verification, rollback, failure modes with escalation, and
> out of scope. No narrative, and the first screen states the effect and the risk.

## 9. Single-file HTML report

> Turn this document into an HTML report using the report template bundled with this skill
> (`references/report-template.html`). Copy that file, keep its `<style>` block byte for byte, and
> replace every `{{TOKEN}}` and `<!-- SLOT -->` marker. Delete every comment that remains.
>
> - Verdict block at the top, same wording as the Markdown version, 150 words or less.
> - Table of contents built from the section headings, in the order the reader asks.
> - Move the existing tables and the diagram in as-is: `table.data` and `figure.diagram`. No new
>   content, no new claims.
> - Status column values become `ok` / `no` / `warn` badges.
> - Class names only from the template's vocabulary. Add no CSS. The only inline style allowed sets
>   `--v` / `--max` / `--cols`.
> - Then open it, check the console, check 375 px and 1440 px, check the print preview, and tell me
>   what you saw.
>
> Save as `[slug].html` and reply with the path, the verdict in one line, and what to read first.

## 10. Self-review — the reviewer's first pass

> Review your own draft the way the reviewer will. Can I disagree with the verdict from the summary
> alone? Is every heading a question I have? Is the out-of-scope section real? Is every assumption
> labelled, and does every number carry a source? Cut a third, then show me what you removed. Add no
> new information.

## 11. Explanation — the secondary case

> Explain [topic] at about 80% of the way to ASD-STE100: verdict in the first two sentences, one idea
> per sentence, active voice, short sentences, one clearly marked analogy allowed. Then one diagram if
> it replaces two paragraphs. Target [N] words.

## 12. One-line offer

> Want this as a single-file HTML report you can circulate? Roughly [estimate] to produce.

## 13. Stop signal

> Keep it to a memo. One screen, pasteable into the tracker, verdict first.

## Notes on using these

- Run template 0 or 1 first. It is free, and it fixes most documents.
- Name the document type early. The shape carries more of the quality than any wording polish.
- Ask for the **draft pass** on rung 3. It catches most rendering failures.
- Deliver the artifact plus its source file, so the content stays greppable and patchable.
- If a document looks good but you cannot open it, it is not done. Go back to template 10.
