---
name: easy-output
description: >
  Use when a human must READ and understand what the model produces: explanations, summaries,
  design docs, hand-off notes, PR descriptions, READMEs. Makes output readable and concise first —
  ASD-STE100 constrained writing (dialable to a softer "80%"), strict cutting, and structure over
  prose. Diagrams and single-file HTML pages are support, used only when they read faster than the
  prose they replace. A custom explainer video is a final, opt-in rung, never proposed by default.

  Trigger when the user asks to 解释/讲清楚/说明白/写清楚/精简/太长了/看不懂/简化/可视化/画个图/做个网页, or
  says "explain X", "ELI5", "make this clearer", "too long", "tl;dr", "simplify this", "ASD-STE100",
  "make a diagram", "output in HTML". Also apply proactively to a draft before sending it, when that
  draft is long, padded, or serial prose.

  Don't use for writing code, for one-line facts, or when the output format is already fixed.
license: MIT
compatibility: No dependencies. Produces ordinary files (Markdown, HTML, SVG, MP4). Only the optional video rung needs ffmpeg and a TTS option.
metadata:
  author: easy-output contributors
  version: 0.1.0
  category: document-creation
  pattern: context-aware
  tags: [readability, conciseness, writing, diagram, html, explainer-video, ste100, output-format]
  source: "Interpretation of Andrej Karpathy's post on making LLM output easier to understand (https://x.com/karpathy/status/2105819303471976479). Independent work, not endorsed by the author."
---

# easy-output

**Readable and concise is the product. Everything else is support.**

Most model output is not wrong; it is unclear and too long. Fix it in this order: **cut first,
make it clear, then — only if it actually helps — change the medium.** This file holds the routing;
read the `references/` files only as each rung needs them.

## The ladder

| Rung | Medium | Buys | Cost | Status |
|---|---|---|---|---|
| 0 | Chat prose | speed, diffs, grep | seconds | one-line facts |
| 1 | Constrained, cut prose (ASD-STE100) | clarity + concision, one word = one meaning | +0 | **the core** |
| 2 | Diagram | structure, relationships, compression | minutes | support |
| 3 | Single-file interactive HTML | exploration, parameter manipulation | tens of minutes | support |
| 4 | Custom explainer video | narrative, motion, timing | hours, needs audio | **opt-in only** |

Rungs 0–2 cover almost every request. Rung 3 is for content the reader must explore. **Rung 4 is a
deliberate exception** — see "Where video stands". Climb only while the understanding gain beats the
cost, and **stop at the rung where the human can act**. Never climb for decoration.

## Operating rules (always in force)

1. **Cut first.** Delete what does not change what the reader knows or does: preamble, restating the
   question, recaps in short texts, hedges, "it's worth noting that". Put the answer in the first
   sentence. Prefer a list or a table over prose for parallel items. Read
   [references/conciseness.md](references/conciseness.md).
2. **Then make it clear.** One idea per sentence, active voice, short sentences, one word for one
   meaning, no nominalizations. Default: **ASD-STE100 at about 80%** — keep the discipline, drop the
   stiffness, allow one marked analogy. Read [references/writing.md](references/writing.md).
3. **Name the rung and the medium, chosen from the shape of the content** — never from what is fun to
   make. Work the five questions and the routing table below.
4. **The artifact is the answer.** Rung 3/4: give the path, how to open it, the takeaway, what to try
   first — do not restate it. Rung 1/2: the reply *is* the artifact; write it well and stop.
5. **Self-contained or it does not count.** Single file where possible; inline CSS/JS; no build step;
   opens from `file://`; no keys, tokens, or private paths baked in.
6. **Verify before you deliver.** Re-read your own draft against rules 1–2. For an artifact: open the
   HTML, confirm Mermaid parses and the SVG renders, confirm audio matches scene length. **If you
   cannot verify a format here, ship a plainer one you can verify** (Mermaid → ASCII) and say why.
   Gate: [references/checklist.md](references/checklist.md).
7. **The medium must not lie.** Real numbers with units and sources. No invented data as a chart. No
   stock footage implying it is real. Label every axis and arrow. **Check the facts that carry the
   argument** against a primary source first — a confident wrong citation is worse than none.
8. **Discardable, not disposable-looking.** One artifact per question per medium, written to a
   sensible path (`./<slug>.html`, `./<slug>/`). No repo, no framework, no maintenance burden. A rung
   1 answer plus a rung 2 diagram in chat is one reply, not two files.
9. **Offer the uplevel; do not impose it.** Give the readable answer, then offer once. Ask before
   anything that costs more than a few minutes of compute. Usually rung 1 was enough.
10. **A dedicated skill changes *how*, never *which rung*.** Use a diagramming or video skill to
    produce the rung already chosen — it does not raise the rung by itself, and it stays bound by the
    budget rule. Three arrows do not become an interactive page because a diagramming skill exists.

## Choosing, in five questions

1. **What can the reader do, decide, or restate afterwards?** "Explain it to someone else" and "stop
   being confused" are valid answers; a pure explanation needs no downstream decision.
2. **What shape is the content?** Sequence over time, static structure, a quantitative space, a
   definition/procedure, or an invisible mechanism. Shape picks the rung.
3. **Read once, or re-consulted and manipulated?** Read once → rung 1/2. Explored, stepped through, or
   parameterized → rung 3.
4. **What is the budget?** Under a minute of your own work → rung 1/2. Rung 4 is minutes-to-hours;
   ask first.
5. **What can you verify here?** If you cannot open or render a format in this environment, ship a
   plainer one you can verify and say so.

## Routing table

| The content is… | Go to | Read |
|---|---|---|
| **Anything you are about to write** | **cut it, then check clarity** — never skipped | [conciseness.md](references/conciseness.md) + [writing.md](references/writing.md) |
| A term, contract, spec, or runbook to follow, quote, or grep | Rung 1 | [writing.md](references/writing.md) |
| **A mechanism or process — "how does X work"** | **Rung 1 verdict + Rung 2 diagram** | [writing.md](references/writing.md) + [diagrams.md](references/diagrams.md) |
| Structure, hierarchy, flow, state, sequence, or causal relation | Rung 2 | [diagrams.md](references/diagrams.md) |
| A parameter space, a comparison, a "play with it" idea | Rung 3 | [html-pages.md](references/html-pages.md) |
| An invisible mechanism unfolding over time, a proof sketch | Rung 4 — **only if the user opts in** | [video-explainers.md](references/video-explainers.md) |
| A decision the reader must make | Rung 1 + Rung 2. Not a video. | [writing.md](references/writing.md) + [diagrams.md](references/diagrams.md) |
| One fact | Rung 0. Answer it. | — |

**Tie-break: prose and diagram compose, not compete.** If two rows match, do rung 1 + rung 2.

Other references, opened only when relevant: [prompt-templates.md](references/prompt-templates.md)
when the user wants a reusable prompt; [spirit.md](references/spirit.md) when the request is about
the approach itself, not a topic.

## Worked routing

| Request | Rung | Why |
|---|---|---|
| "Explain how the TCP three-way handshake works." | 1 + 2 | A mechanism: a tight verdict in prose, one sequence diagram. |
| "This doc is 4 pages and I still don't get it." | 1 (cut hard) | Readability problem — cut and restructure before adding anything. |
| "Explain TCP slow start as an interactive page." | 3 | The user named the medium; parameters make it explorable. |
| "I need the exact wording of the rate-limit contract." | 1 only | It must be quoted and grepped; a visual adds nothing. |
| "What port does the health check use?" | 0 | One fact. |

## Default move

For "explain X": ① a cut-hard rung 1 verdict (answer first, ~80% STE), ② one diagram only if it
replaces two or more paragraphs, ③ offer rung 3 once — and video only for a genuine mechanism
unfolding over time.

## Where video stands

Video is rung 4: most expensive, hardest to patch, easiest to over-build. It is here because the
source post is bullish on it and it is sometimes right — **not because it is what this skill is for.**
If rung 4 looks like the fix for a problem that deleting 30% of the text would fix, drop back to
rung 1.

## Non-negotiables

- Never answer "explain X" with a 900-word wall if 150 words plus one diagram carries it.
- Never pad to look thorough. Exhaustiveness is a cost, not a service.
- Never start a render longer than a few minutes without asking first.
- Never deliver an artifact you have not opened or rendered yourself.
- Never bake a key into a generated file; read credentials from the environment.
