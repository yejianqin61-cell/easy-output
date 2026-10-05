# Carriers

Read the section for the carrier you chose, and no other.

## ASCII

- Instant, diffable, pasteable into a terminal, a PR or a commit message. It survives every tool.
- Use `─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ▶ ▼`, and keep monospace alignment. Never rely on tabs.
- Keep every box the same width, and re-check the alignment after every edit: one stray character shifts
  a whole column.
- 100 characters wide is the practical limit for chat. Prefer fewer columns.
- Where the target may not render Unicode, fall back to `- | +`.

## Mermaid

- Fence it as ` ```mermaid ` so renderers pick it up.
- `flowchart TD` for process, `sequenceDiagram` for interaction, `stateDiagram-v2` for lifecycle,
  `erDiagram` for schema, `timeline` or `gantt` for time.
- Quote labels that contain punctuation: `A["cache (hot path)"]`.
- Keep node ids short and stable, and put the prose in the label.
- Avoid experimental syntax and raw HTML in labels where the diagram must render on GitHub.
- Very large graphs: set `direction` per subgraph rather than growing one direction.
- **Render it before you ship it.** Where this environment has no renderer, fall back to ASCII. Shipping
  syntax you cannot check is worse than a plainer figure you can.

## Standalone SVG

- Set `viewBox` and a width-to-height ratio. Never rely on a fixed pixel width.
- `fill="currentColor"` and `stroke="currentColor"`, so the diagram follows the light and dark theme.
- System font stacks only. No external font requests.
- Inline the SVG in the page. An external `.svg` reference breaks the one-self-contained-file rule.
- Add `<title>` and `<desc>` inside the SVG, for screen readers and hover tooltips.
- Coordinates on a 20px grid, stroke and fill from the page's variables.
- Where the diagram has stages, a step-through control beats a static picture.
