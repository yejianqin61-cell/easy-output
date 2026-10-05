---
name: easy-diagram
description: >-
  Use when a relationship, a flow, a state machine or a structure is easier to see than to read, or when
  the user asks for a diagram: 画个图, 别写了, 可视化, 一张图说明, 流程画一下, diagram, visualize, draw this,
  sketch the flow, "show me the shape of it". Turns one claim into one diagram, picks the type from the
  relation, and delivers it as ASCII, Mermaid, or a standalone SVG.
---

# Easy diagram

**A diagram is one claim, drawn.** Write the claim in one sentence before anything else. If you cannot,
you have two diagrams.

That sentence is the whole method and the whole test. A figure that cannot be summarised in one sentence
is a picture of a topic, and the reader will not know where to look.

## Process

Five steps. Each ends on a check you can make.

### 1. Write the claim

One sentence, with a verb and a direction: "retries double p99 latency", "only the leader accepts
writes", "the state leaves open without a user action".

**Done when** the sentence has a subject, a verb and a direction. "Overview of the retry logic" has none
of the three, and is not a claim.

### 2. Pick the type from the relation

| The relation is | Type | Notes |
|---|---|---|
| What happens, in what order | Flowchart | one direction, never both |
| Who talks to whom, in what order | Sequence | time on the vertical axis |
| A thing that changes state | State machine | every transition carries an event label |
| What contains what | Tree | depth is meaning; do not decorate depth |
| What connects to what | Graph | cluster, or stop at 12 nodes |
| Entities and how they relate | ER | cardinality on both ends |
| What changed when | Timeline | order and duration are the payload |
| Why the system behaves this way | Causal loop | label edges `+` and `−` |
| Which option wins on which axis | Comparison matrix | beats a bar chart past three dimensions |
| A quantity against another | Plot | axes, units, and the takeaway in the title |

**Done when** exactly one row is chosen, and no second type has crept into the figure.

### 3. Choose the carrier

Say it in chat: **ASCII**. Keep it in a repo: **Mermaid**. Re-consult or explore it: **standalone SVG**.
Before drawing in one, read [references/carriers.md](references/carriers.md) for that carrier's rules, and
skip the other two sections.

**Done when** the carrier is named, and this environment can render or display it. Where it cannot, drop
to a plainer carrier you can check.

### 4. Draw it

- Every edge is a sentence. An arrow with no verb is an arrow to delete.
- One flow direction per figure. Two crossing flows are two panels.
- Twelve top-level nodes at most. Past that, cluster, or split into an overview and a detail view.
- The same thing carries the same label everywhere, and the same label as in the code.
- Colour never carries meaning alone: add a shape, a dash or a label, and a legend.
- Whitespace is a feature. Group into containers, then space the containers.
- Annotate the one node that matters. That annotation is what turns a figure into an explanation.

**Done when** every label is one the reader will recognise, and nothing is encoded by colour alone.

### 5. Verify

- It renders. Mermaid: render it. SVG: open it. ASCII: check the column alignment.
- Reading the figure aloud reproduces the claim from step 1.
- The caption states the takeaway, not the topic: "Retries double p99 latency", not "Retry diagram".

**Done when** all three hold on the artifact you are handing over.

## Inside a document, or as the artifact

Inside a Markdown document, a diagram sits at the point where it replaces the paragraphs it compresses.
It takes a Mermaid fence or an ASCII block, with its caption. As a standalone page, call the Skill tool
with "easy-report" and put the SVG in `figure.diagram`. That page brings the theme, the print stylesheet
and the accessibility wiring.

Where the content is a definition, or a list of facts, text is the cheaper carrier. A diagram that repeats
the prose has cost the reader time.

## Anti-patterns

- The hairball: 40 nodes and 80 edges with no grouping.
- Mermaid nobody rendered, so the reader sees source instead of a figure.
- Decorated depth: shadows, gradients, 3D, which encode nothing.
- Colour as the only encoding.
- A diagram that repeats the prose instead of compressing it.
- Unlabelled axes on a plot.
- A diagram where the content was a definition. Text was the cheaper carrier.
