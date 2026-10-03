# Rung 2 — Diagrams

A diagram is not a picture of a topic. **A diagram is one claim, drawn.** If you cannot write the
claim in one sentence, you have two diagrams, not one.

The claim is singular; its supporting edges are not. A sequence diagram with five labelled arrows is
still one claim — "both sides know one byte number in each direction before data flows" — supported
by five sentences. If the edges support two *different* claims, split the figure.

## Pick the type from the relation, not from taste

| The relation is… | Type | Notes |
|---|---|---|
| What happens, in what order | Flowchart / pipeline | left-to-right or top-down, never both |
| Who talks to whom, in what order | Sequence diagram | shows time on the vertical axis |
| A thing that changes state | State machine | every transition needs an event label |
| What contains what | Hierarchy / tree | depth is meaning; do not decorate depth |
| What connects to what | Graph / network | stop at ~12 nodes or cluster first |
| Entities and how they relate | ER / data model | cardinality on both ends |
| What changed when | Timeline / Gantt | order and duration are the payload |
| Why the system behaves this way | Causal loop | label edges `+` / `−` and mark delays |
| Which option is better on which axis | Comparison matrix | beats a bar chart for 3+ dimensions |
| Where this is in a real thing | Annotated screenshot / photo | callouts beat redrawn art |
| A quantity or relationship | Plot | axes, units, and a takeaway in the title |

Do not mix two types in one figure. A flowchart with a timeline buried in it is a diagram that
answers nothing.

## The format ladder (cheapest first)

1. **ASCII / Unicode box art, in the reply.** Instant, diffable, pasteable into a terminal, PR, or
   commit message, survives every tool. Best when the diagram lives in conversation or code.
   Use `─│┌┐└┘├┤┬┴┼ ▶ ▼` and keep to monospace alignment; never rely on tabs.
2. **Mermaid.** Renders natively on GitHub, many wikis, and most editors; versionable and editable
   by the reader. Best when the diagram lives in a repo or a document. **Verify it parses** — do not
   ship Mermaid you have not rendered. If there is no Mermaid renderer in your environment, fall
   back to ASCII: shipping syntax you cannot check is worse than a plainer figure you can.
3. **Standalone SVG / single-file HTML.** Best when the diagram will be re-consulted, explored,
   zoomed, or shared. See [html-pages.md](html-pages.md) for the page shell; inline the SVG so the
   file stays portable.

Rule of thumb: **say it in chat → ASCII. Keep it in a repo → Mermaid. Re-consult it or explore it →
HTML/SVG.**

## Construction rules

- **Every edge is a sentence.** If an arrow has no verb, delete the arrow.
- **Direction is meaning.** One flow direction per figure. If two flows cross, use two panels.
- **Label both ends of a relation** where cardinality or direction is ambiguous (many-to-one,
  caller → callee).
- **≤ ~12 top-level nodes.** More is a map, not an explanation. Cluster, or split into an overview
  plus detail views.
- **Bounded, consistent terminology.** The same thing has the same label everywhere, and the same
  label as in the code.
- **Caption = the takeaway**, not the topic. "Retries double p99 latency" — not "Diagram of retry
  logic". Put the caption in the chat reply and in the artifact.
- **Legend for every colour or shape.** Colour must never be the only encoding (accessibility and
  greyscale printing). Add shape, dash, or a label.
- **Annotate the interesting part.** A red box or a callout on the one node that matters turns a
  diagram into an explanation.
- **Whitespace is a feature.** A tight diagram is unreadable. Group with containers, then space the
  containers.

## Mermaid specifics

- Fence it as ` ```mermaid ` so renderers pick it up.
- `flowchart TD` for process, `sequenceDiagram` for interaction, `stateDiagram-v2` for lifecycle,
  `erDiagram` for schema, `timeline`/`gantt` for time.
- Quote labels that contain punctuation: `A["cache (hot path)"]`.
- Avoid experimental syntax and raw HTML in labels if the diagram must render on GitHub.
- Node ids stay short and stable; put the prose in the label.
- Very large graphs: set `direction` per subgraph rather than growing one direction.

## ASCII specifics

- Keep every box the same width and re-check alignment after editing — one stray character shifts a
  whole column.
- Prefer fewer columns; ~100 characters wide is the practical limit for chat.
- Use `─` `│` `┌` etc. where the target renders Unicode; fall back to `-|+` for maximum portability.

## SVG / HTML specifics

- Always set `viewBox` and a width/height ratio; never rely on a fixed pixel width.
- `fill="currentColor"` and `stroke="currentColor"` so the diagram inherits dark/light theme.
- Use system font stacks; no external font requests.
- Inline the SVG in the HTML — external `.svg` references break the "one self-contained file" rule.
- Add a `<title>` and `<desc>` inside the SVG for accessibility and hover tooltips.
- If the diagram has stages, a step-through control (buttons or a scrubber) beats a static picture.

## Anti-patterns

- The hairball: 40 nodes and 80 edges with no grouping. Cluster it or split it.
- Unparsed Mermaid: the reader sees source code instead of the figure.
- Decorated depth: drop shadows, gradients, and 3D, which encode nothing.
- Colour-only semantics.
- A diagram that repeats the prose instead of compressing it.
- Unlabeled axes on a plot — the most common way a chart quietly lies.
- Serving a diagram when the content was actually a definition — text was the right rung.
