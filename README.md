# easy-output

Agent skills that make the documents an agent writes readable in minutes, and dense enough to build
from. One law, five document shapes, two renderers.

The law compresses [Karpathy's point](https://x.com/karpathy/status/2105819303471976479): we will spend
more time reading what a model produced than writing prompts for it. A document earns that time when it
is short enough to finish, and clear enough to act on. Twelve clauses, each with a threshold you can
count: [`RULES.md`](RULES.md).

Follows the [Agent Skills](https://agentskills.io/) format. Markdown only, with no runtime dependencies.

[中文说明 →](README.zh-CN.md)

## Install

```bash
npx skills add yejianqin61-cell/easy-output -g
```

That is [Vercel Labs' `skills` CLI](https://github.com/vercel-labs/skills). It finds every `SKILL.md`
under `skills/`. Then it installs into every agent it detects: Claude Code, Codex, Cursor, OpenCode and
about 75 more.

```bash
npx skills add yejianqin61-cell/easy-output --list                 # preview first
npx skills add yejianqin61-cell/easy-output -g -a claude-code -y   # one agent
npx skills use yejianqin61-cell/easy-output --skill easy-audit --agent claude-code
```

`-g` installs for every project. Drop it to install into `./.claude/skills/` instead. Installs run
through symlinks, so a `git pull` keeps them current; add `--copy` where symlinks are awkward.

To install by hand, clone the repo and symlink `skills/<bucket>/<name>` into your agent's skills
directory.

## The skills

| Skill | What it does |
|---|---|
| [easy-audit](skills/documents/easy-audit/SKILL.md) | Requirements with percentages, defects, one plan each |
| [easy-summary](skills/documents/easy-summary/SKILL.md) | What changed, what it means, what is still open |
| [easy-plan](skills/documents/easy-plan/SKILL.md) | Requirements into phases, each ending somewhere demoable |
| [easy-task-act](skills/documents/easy-task-act/SKILL.md) | One brief per task, then each task in its own commit |
| [easy-registry](skills/documents/easy-registry/SKILL.md) | One row per item, kept current across many edits |
| [easy-diagram](skills/render/easy-diagram/SKILL.md) | One claim, one figure: ASCII, Mermaid or SVG |
| [easy-report](skills/render/easy-report/SKILL.md) | The document as a single-file HTML page |

Each `SKILL.md` carries the full contract, so this table stays a directory.

The chain runs audit, plan, task and act. `easy-audit` names the defects and their plans, `easy-plan`
orders the requirements into phases, and `easy-task-act` writes the briefs and lands them.
`easy-summary` closes the round. `easy-registry` holds what nobody is working on yet.

Every shape that writes a document asks once, before writing, whether the user wants Markdown or a
single-file HTML report. The render is `easy-report`'s job.

Research documents are out of scope. That shape is already served.

## The ladder

Karpathy's post climbs four rungs, each introduced by the same two words: "But even better". The medium
is a variable, and the cheapest one that opens the channel the content needs wins.

| Rung | In this repository |
|---|---|
| 1. Constrained, cut prose | The law: [`RULES.md`](RULES.md), carried by every shape skill. |
| 2. A diagram | [easy-diagram](skills/render/easy-diagram/SKILL.md), inside a document or as the artifact. |
| 3. A web page | [easy-report](skills/render/easy-report/SKILL.md), a fixed template the document renders into. |
| 4. An explainer video | Out of scope: this reader approves documents rather than watching explanations. |

The source post is most bullish on the rung 4 explainer video, and this repository does not carry that
rung. Text stays the right medium where the reader must quote, grep, or check precision.

## Language

Skills are written in English. Every skill and every root document has a Chinese companion beside it,
named `<name>.zh-CN.md`. Two examples: [`RULES.zh-CN.md`](RULES.zh-CN.md) and
[`SKILL.zh-CN.md`](skills/documents/easy-audit/SKILL.zh-CN.md). The companions are for readers, and they
change nothing at run time.

The documents these skills produce are written in the language you are using. A skill names its fixed
words in English, and tells the agent to translate them once and stay consistent.

## Checking this repository

```bash
python tools/check.py            # every gate
python tools/check.py prose      # one gate
python tools/check.py --report   # the metric table
```

Four gates hold the promises this repository makes. The law is in six places, and they must match. Every
relative link must resolve. Every document must obey the countable clauses. Every skill must be
installable. See [`tools/README.md`](tools/README.md).

## Structure

```
easy-output/
├── RULES.md                      # the readability law: twelve clauses and their thresholds
├── RULES.zh-CN.md                # the same law, in Chinese
├── CLAUDE.md                     # how skills are written here
├── tools/                        # the check command, with its metrics library
├── parked/                       # retired material, kept out of the install
└── skills/
    ├── documents/                # one skill per document shape
    │   ├── easy-audit/           SKILL.md + SKILL.zh-CN.md + agents/ + references/
    │   ├── easy-summary/         SKILL.md + SKILL.zh-CN.md + agents/ + references/
    │   ├── easy-plan/            SKILL.md + SKILL.zh-CN.md + agents/ + references/
    │   ├── easy-task-act/        SKILL.md + SKILL.zh-CN.md + agents/ + references/
    │   └── easy-registry/        SKILL.md + SKILL.zh-CN.md + agents/ + references/
    └── render/                   # a document turned into another medium
        ├── easy-diagram/         SKILL.md + SKILL.zh-CN.md + agents/ + references/
        └── easy-report/          SKILL.md + SKILL.zh-CN.md + agents/ + references/
```

Each of the five document skills carries a copy of the law at `references/readability-law.md`, because
skills install separately. The two render skills carry none: they render a document that already obeys
the law. `easy-report` owns `references/report-template.html`, the fill-in contract, and the render
gate. `easy-diagram` owns the carrier rules.

## Provenance

The law comes from Andrej Karpathy's post of 2 October 2026 on making LLM output easier to understand.
It is quoted in full in [`parked/spirit.md`](parked/spirit.md). The post:
<https://x.com/karpathy/status/2105819303471976479>. Karpathy has not reviewed or endorsed this
repository.

## License

[MIT](LICENSE).

## Contributing

Small contributions land best. A sharper before/after pair in the law. A document shape that earns its
sections. A check that caught a real failure. A corrected fact or licence detail. Keep it
dependency-free, keep each `SKILL.md` thin, and keep this README short.
