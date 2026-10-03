# easy-output

**Readable output first. Diagrams and pages when they help. Video only if you ask.**

An Agent Skill that makes a coding agent write output a human can actually read: cut hard, write
clearly (ASD-STE100, with a softer "80%" setting), and reach for a diagram or a single-file web page
only when that reads faster than the prose it replaces.

Pure Markdown. No scripts, no dependencies, no build step.

[中文说明 →](README.zh-CN.md)

---

## The problem

Model output is rarely wrong. It is unclear and too long. Two failures, and prompts usually address
neither:

- **Clarity** — long sentences, three ideas each, synonyms that shift meaning mid-paragraph.
- **Conciseness** — preamble, restatement, recaps, hedges, and 900 words where 150 would do.

Changing the *medium* helps — a diagram can replace two paragraphs — but it is the third move, not
the first. This skill enforces the order: **cut, then clarify, then change medium.**

## The ladder

| Rung | Medium | Buys | Cost | Status |
|---|---|---|---|---|
| 0 | Chat prose | speed, diffs, grep | seconds | for a one-line fact |
| 1 | Constrained, cut prose (ASD-STE100) | clarity **and** concision, one word = one meaning | +0 | **the core** |
| 2 | Diagram | parallel structure, relationships, compression | minutes | support |
| 3 | Single-file interactive HTML | exploration, parameter manipulation | tens of minutes | support |
| 4 | Custom explainer video | narrative, motion, timing | hours, needs audio | **opt-in only** |

Rungs 0–2 cover almost every request. Rung 3 is for content the reader must explore. **Rung 4 is a
deliberate exception** — proposed only for an invisible mechanism unfolding over time, only after the
user agrees to the cost. See [Where video stands](#where-video-stands).

---

## Install

### One line (recommended)

```bash
npx skills add yejianqin61-cell/easy-output -g
```

That is [Vercel Labs' `skills` CLI](https://github.com/vercel-labs/skills), the package manager for
the agent-skills ecosystem. It resolves the repo, reads `SKILL.md` from the repository root, and
installs it to every agent it detects — Claude Code, Codex, Cursor, OpenCode and ~75 others.

```bash
# global (all projects) — as above; drop -g to install into ./.claude/skills/ etc. for this project
npx skills add yejianqin61-cell/easy-output -g

# target specific agents, non-interactive
npx skills add yejianqin61-cell/easy-output -g -a claude-code -y

# preview what is in the repo without installing
npx skills add yejianqin61-cell/easy-output --list

# use it once without installing at all
npx skills use yejianqin61-cell/easy-output --skill easy-output --agent claude-code

# later
npx skills update easy-output
npx skills remove easy-output
```

Agents install by **symlink** by default, so updating the repo updates the skill; add `--copy` if
your setup does not support symlinks.

> This repo lives at <https://github.com/yejianqin61-cell/easy-output>.

### Manual

```bash
git clone https://github.com/yejianqin61-cell/easy-output.git ~/.claude/skills/easy-output   # global
git clone https://github.com/yejianqin61-cell/easy-output.git .claude/skills/easy-output     # project
```

On Windows those are `%USERPROFILE%\.claude\skills\easy-output` and `.claude\skills\easy-output`.
Any harness that follows the Agent Skills convention — a folder with `SKILL.md` carrying `name` and
`description` frontmatter — works the same way.

Verify it loaded by asking your agent *"what skills do you have?"*; then try *"explain how TCP slow
start works"*, or *"this doc is too long — make it readable"*.

### Do I need to publish an npm package?

No. `npx skills add` reads the public repo directly, so publishing is one `git push` — there is no
package to version, no `bin` script to maintain, and no version skew between the repo and npm.

`easy-output` *is* unclaimed on npm if you later want `npx easy-output` as a shorter alias, or a
listing on npmjs.com. It would mean adding a `package.json` with a small installer `bin` and
republishing on every change. Reasonable, but redundant for most people — the CLI above is the
ecosystem standard.

---

## Use

The skill triggers on its own when you ask for understanding or complain about readability, and it is
written to fire **proactively** — before the agent sends a draft that is padded or serial.

```
Explain how TCP slow start works.                     → rung 1, cut hard, + one diagram
This doc is 4 pages and I still don't get it.         → rung 1: cut a third, restructure
Explain our retry/backoff logic, as a page I can play with. → rung 3
Make a 90-second 3b1b-style explainer on eigenvalues. → rung 4, and only because you asked
What port does the health check use?                  → rung 0: one line
```

Ready-to-paste prompts for every rung, including the cheap "script only, no rendering yet" gate:
[`references/prompt-templates.md`](references/prompt-templates.md).

---

## What's inside

```
easy-output/
├── SKILL.md                        # ladder, 10 rules, 5 selection questions, routing table
└── references/
    ├── conciseness.md              # cut first: BLUF, budgets, techniques, anti-patterns
    ├── writing.md                  # clarity: ASD-STE100 rules, the 80% dial, before/after
    ├── diagrams.md                 # relation → diagram type, ASCII / Mermaid / SVG
    ├── html-pages.md               # the one-file contract, interaction patterns
    ├── video-explainers.md         # the opt-in rung: 3b1b decoded, audio-first, TTS licences
    ├── prompt-templates.md         # copy-paste prompts, the cut-first pass first
    ├── checklist.md                # the per-rung verification gate
    └── spirit.md                   # the source argument, as 10 principles + guardrails
```

Progressive disclosure: `SKILL.md` holds only the selection logic and routes into `references/`, so
the agent loads the depth it needs and nothing more.

---

## Where video stands

Video is rung 4: the most expensive, hardest to patch, easiest to over-build. It is in this skill
because Karpathy's post is bullish on it and because it is sometimes the right answer. **It is not
what this skill is for.** Reaching for rung 4 to fix a problem that deleting 30% of the text would
fix is a misreading of the skill.

## Design rules

- **Cut first; decorate second.** If a draft is 900 words where 150 would be clearer, the medium was
  never the problem.
- **Verify or don't ship.** Re-read your own draft against the rules; open the HTML, render the
  Mermaid, watch the draft, measure the audio. Unverifiable format → ship a plainer one you can verify.
- **Ask before the expensive rung.** Video is minutes to hours; the user decides.
- **Refuse to over-build.** A 90-second video about a one-line fact is a worse answer than the line. A
  dedicated diagramming or document skill changes *how* you build, never *which* rung you pick.
- **The medium must not lie.** Real numbers with units and sources, labeled axes, no generated footage
  implying it is real, citations checked against a primary source.
- **Never bake in a key.** Read `ELEVENLABS_API_KEY` (or any credential) from the environment.

---

## Attribution

The ideas compressed here are Andrej Karpathy's, from his single post of 2 October 2026 on
understanding LLM output: <https://x.com/karpathy/status/2105819303471976479> (quoted in full in
[`references/spirit.md`](references/spirit.md), reproduced from public unrolls since x.com requires a
login). The skill itself is an independent interpretation — an attempt to turn a set of tips from an
expert human into a repeatable procedure for an agent — and is **not authored, reviewed, or endorsed
by him**. The editorial emphasis (readability and conciseness first, video last and opt-in) is this
skill's own; see [How this skill weighs the four rungs](references/spirit.md).

ASD-STE100 is a specification published by the ASD, free to download at
<https://www.asd-ste100.org/>. Its text is not reproduced here; `references/writing.md` paraphrases
the well-known rules for practical use.

3Blue1Brown, Manim, ElevenLabs, Kokoro, Piper, XTTS, Remotion and others are the property of their
respective owners, referenced descriptively.

## License

[MIT](LICENSE). Replace the copyright holder with your own name or handle before publishing.

## Contributing

Issues and PRs welcome — and please keep the PR small. Useful contributions: a conciseness technique
that actually worked, a better before/after STE example, a verification step that caught a real
failure, a corrected tool or licence detail. Keep it dependency-free, keep `SKILL.md` thin, and keep
the repo's own writing short: this README is the first thing a reader sees, so it is where we get
tested first.
