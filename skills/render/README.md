# Render

Skills that turn a document into something other than text. They do not decide content. They render what
a shape skill has already written, or carry a claim in a medium the eye parses faster than prose.

## Model-invoked

| Skill | What it does |
|---|---|
| [easy-diagram](easy-diagram/SKILL.md) | Turns one claim into one diagram, picks the type from the relation, delivers ASCII, Mermaid or SVG. |
| [easy-report](easy-report/SKILL.md) | Fills a fixed HTML template, so the page looks considered and carries the same facts as the Markdown it renders. |

A diagram that ships inside a report goes into `figure.diagram` on the page `easy-report` fills.
