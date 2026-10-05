# Working in this repo

A set of agent skills for documents a human has to read. The family prefix is `easy-`.

## Layout

- [`RULES.md`](RULES.md) at the root: the readability law. Twelve clauses, each with a threshold.
- `skills/<bucket>/<name>/SKILL.md`, with the frontmatter `name` equal to the folder name.
  - `documents/`: one skill per document shape
  - `render/`: skills that turn a document into an artifact, such as a single-file HTML report
  - `in-progress/`: beta skills, public on purpose, not promoted
  - `deprecated/`: kept for reference, no longer reachable
- `parked/` at the root: retired material. Not installed, kept for salvage.
- [`tools/check.py`](tools/README.md) at the root: the dev-only check command. Not installed either.

## Checking

Run `python tools/check.py` before every commit. Four gates: the law copies match `RULES.md`, every
relative link resolves, every document obeys the countable clauses, and every skill is installable. It
exits 1 on a failure, and every finding names the file and the line.

## The law

`RULES.md` is the only source. Every skill under `skills/documents/` carries its own copy at
`references/readability-law.md`. That copy holds the same twelve clauses, and its closing note about
where the law is maintained is the only difference. Skills install separately, and a `../` path breaks
the moment one is installed alone. The render skills carry no copy: they render a document that already
obeys the law. Change the law in `RULES.md`, then run `python tools/check.py law --sync` to re-copy it
into every skill under `skills/documents/`.

## Adding or changing a skill

- Every skill carries `agents/openai.yaml` beside its `SKILL.md`, holding `interface.display_name` and
  `interface.short_description` for the Codex picker.
- Invocation is set in two places, and they agree:
  - **user-invoked**: `disable-model-invocation: true` plus `policy.allow_implicit_invocation: false` in
    `agents/openai.yaml`. The description is human-facing: one line, trigger lists stripped.
  - **model-invoked** (the default): omit both. The description is model-facing and keeps rich trigger
    phrasing, including the Chinese words a Chinese speaker would actually type.
- A skill reaches another by telling the agent to **call the Skill tool with its name**. Never link
  across skill folders.
- A user-invoked skill is unreachable from every other skill. Where a step needs one, write the
  instruction for the human: "tell the user to run `/name`".
- Bucket `README.md`s list every skill in the bucket, one line each, grouped user-invoked then
  model-invoked. The skill name links to its `SKILL.md`.
- A promoted bucket is one holding finished work, so its skills appear in the top-level `README.md`.
  This repo ships through `npx skills add` and not as a Claude Code plugin, so there is no plugin
  manifest to keep in sync. Add one the day a second install route exists.

## Language

- **Skills are written in English**, `SKILL.md` and `references/` alike. No Chinese in a skill.
- **Every skill and every root document has a Chinese companion**, named `<name>.zh-CN.md` beside the
  file it translates. For example: `README.zh-CN.md`, `RULES.zh-CN.md`, `SKILL.zh-CN.md`. The companion
  is for readers, and it changes nothing at run time.
- The **documents** these skills produce are written in the language the user is using. Where a skill
  fixes a vocabulary, it names the English words and says to translate them once and stay consistent.

## Prose

- A skill's `description` earns harder pruning than its body. It sits in the context window every turn.
  So it carries triggers and the leading word, and nothing the body already says.
- This repo's own prose follows the law where it applies: present state, one fact in one place, short
  cells, scarce emphasis.
