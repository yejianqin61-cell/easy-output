# Documents

One skill per document shape. Each carries the readability law and everything else it needs, so it
installs on its own.

## Model-invoked

| Skill | What it does |
|---|---|
| [easy-audit](easy-audit/SKILL.md) | Last round's requirements with a completion percentage each, this round's defects, one plan per defect. |
| [easy-summary](easy-summary/SKILL.md) | What changed over a window: the headline, a change table, what it means, what is still open. |
| [easy-plan](easy-plan/SKILL.md) | Turns a requirement list into phases, each ending somewhere demoable, with one-line tasks. |
| [easy-task-act](easy-task-act/SKILL.md) | Writes one brief per task in the batch, then implements them one at a time, each ending in its own commit. |
| [easy-registry](easy-registry/SKILL.md) | Keeps a list current across many edits: one row per item, amendments supersede, the change log at the end. |

Every shape that writes a document asks once whether the user wants Markdown or a single-file HTML
report, and hands the render to `easy-report`.

The last shape on the way is `easy-research`.
