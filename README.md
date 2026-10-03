# easy-output

An Agent Skill that raises the readability of an agent's output: cut the filler, write in
constrained English, then pick the cheapest medium that carries the idea — table, diagram,
single-file page, or video. Targets explanations, summaries, design docs, hand-off notes, and PR
descriptions.

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

## How it works

Three passes, in order. The first two are free and carry most of the value.

| Pass | What it does | Cost |
|---|---|---|
| **Cut** | Drops preamble, restated questions, recaps, hedges. Puts the answer in the first sentence. Swaps prose for tables and lists on parallel items. | none |
| **Clarify** | One idea per sentence, active voice, one word for one meaning, no nominalisations. ASD-STE100 at ~80%: its writing rules, ordinary vocabulary, one clearly marked analogy. | none |
| **Re-render** | Picks the medium that reads best at that density. | minutes to hours |

The media it chooses between:

| Rung | Output | Adds | Cost |
|---|---|---|---|
| 0 | Chat prose | speed, diffs, grep | seconds |
| 1 | Constrained, cut prose | clarity and concision together | — |
| 2 | Diagram | structure, compression | minutes |
| 3 | Single-file interactive HTML | exploration, parameter control, self-paced animation | tens of minutes |
| 4 | Custom explainer video | narrative, motion, timing | hours, plus TTS |

Rungs 0–2 cover most requests. Rung 3 suits content the reader has to explore. Rung 4 is opt-in: the
agent proposes it for a mechanism that unfolds over time, and asks about the cost first.

## Usage

The skill triggers on its own when you ask for an explanation or flag that output is hard to read.
It also fires before the agent sends a draft that has run long.

```
Explain how TCP slow start works.                          → rung 1, cut hard, plus one diagram
This doc is 4 pages and I still don't get it.              → cut a third, restructure
Explain our retry/backoff logic as a page I can play with. → rung 3
Make a 90-second 3b1b-style explainer on eigenvalues.      → rung 4, after the cost question
What port does the health check use?                       → one line
```

Copy-paste prompts for every rung live in
[`references/prompt-templates.md`](references/prompt-templates.md); template 1 is the cut pass.

## Structure

```
easy-output/
├── SKILL.md                    # rungs, 10 operating rules, 5 selection questions, routing table
└── references/
    ├── conciseness.md          # cutting: BLUF, length budgets, techniques, anti-patterns
    ├── writing.md              # ASD-STE100 rules, the 80% dial, before/after pairs
    ├── diagrams.md             # relation → diagram type; ASCII, Mermaid, SVG
    ├── html-pages.md           # single-file contract, interaction patterns
    ├── video-explainers.md     # 3b1b decoding, audio-first timing, TTS options and licences
    ├── prompt-templates.md     # prompts per rung, cut pass first
    ├── checklist.md            # per-rung verification gate
    └── spirit.md               # source post, 10 principles, guardrails
```

`SKILL.md` holds the routing and pulls in a `references/` file only when the rung calls for it.

## Operating rules

- Cut first. A 900-word draft that 150 words could carry has a text problem, and diagrams rarely
  rescue it.
- Verify before delivering. Re-read the draft against the rules; open the HTML, render the Mermaid,
  watch the draft render, measure the audio against scene length. When the environment can't verify
  a format, ship the plainer one.
- Ask before expensive work. Rung 4 runs minutes to hours, and the user signs off on the cost.
- Keep artifacts honest. Real numbers with units and sources, labeled axes, citations checked
  against a primary source.
- Read credentials from the environment (`ELEVENLABS_API_KEY`).
- A diagramming or office-document skill changes *how* a rung gets built; the rung itself stays put.

## Provenance

Compressed from Andrej Karpathy's post of 2 October 2026 on understanding LLM output:
<https://x.com/karpathy/status/2105819303471976479>, quoted in full in
[`references/spirit.md`](references/spirit.md). This repository is an independent interpretation, and
the author has not reviewed or endorsed it. The emphasis on readability and conciseness, and rung 4's
opt-in status, are this repository's editorial choices.

ASD-STE100 is published by the ASD at <https://www.asd-ste100.org/>.
[`references/writing.md`](references/writing.md) paraphrases its well-known rules for practical use.

3Blue1Brown, Manim, ElevenLabs, Kokoro, Piper, XTTS, and Remotion are the property of their
respective owners, referenced descriptively.

## License

[MIT](LICENSE).

## Contributing

Issues and PRs welcome; keep them small. Contributions that land well: a conciseness technique that
held up in practice, a sharper before/after STE pair, a verification step that caught a real failure,
a corrected tool or licence detail. Keep it dependency-free, keep `SKILL.md` thin, and keep this
README short — it gets read first.
