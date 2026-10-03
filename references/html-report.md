# Rung 3 — Single-file HTML report

Use this when the document gets re-read, circulated, reviewed by several people, compared against
alternatives, or carries enough tables that a Markdown file stops being scannable. Everything below
also holds for the Markdown version of the same document — the content contract lives in
[documents.md](documents.md), and this file covers the rendering.

## The one-file contract

- **One `.html` file.** Inline CSS and JS. No build step, no framework, no npm.
- **Opens from `file://`** and works offline, so a reviewer can open an attachment.
- **No CDN dependency for the content to be readable.** Reach for zero libraries: hand-written SVG,
  `<canvas>`, and the platform DOM cover a report.
- **No secrets, no private paths, no local absolute file references.**
- **Portable name:** `<topic-slug>.html`.

## Report structure

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>The verdict, not the topic</title>
  <style>/* inline */</style>
</head>
<body>
  <header>
    <h1>The verdict</h1>
    <p class="status">Project analysis · 2026-10-04 · for review · locks: the queue choice</p>
    <section class="verdict"><!-- ≤150 words: recommendation, cost, risk, the ask --></section>
  </header>
  <nav><!-- table of contents; reports get skimmed, then re-read --></nav>
  <main>
    <section id="state"><h2>What is the state today</h2>…</section>
    <section id="problem"><h2>What it costs us</h2>…</section>
    <section id="options"><h2>What the options are</h2>…table…</section>
    <section id="recommendation"><h2>What we recommend</h2>…</section>
    <section id="risks"><h2>What could go wrong</h2>…</section>
    <section id="scope"><h2>What is out of scope</h2>…</section>
  </main>
  <footer>Sources, generation date, and the one line saying what was generated.</footer>
  <script>/* inline, no build step */</script>
</body>
</html>
```

The headings are the questions the reader has, taken straight from the shape in
[documents.md](documents.md). The verdict block is the same ≤150 words as the Markdown version.

## When interactivity earns its place

| Content | Control |
|---|---|
| A long table of candidates | Sort and filter columns |
| Detail a reviewer may skip | `<details>` for the per-criterion evidence |
| Alternative scenarios | Tabs, so the reader compares rather than scrolls |
| A weighting or threshold | Slider over the weights, with the ranking updating live |
| A chart | Hover to read the exact value; label the axes |
| A prompt or a query to reuse | Copy button with the text selectable |

Two rules: **the default view stands on its own** (a reader who touches nothing still gets the
document), and **every control has a keyboard-reachable equivalent** (a real `<button>`,
`<input type="range">`, `<details>`).

## Design defaults

- **Typography first.** System font stack, 16–20 px body, 1.5–1.7 line-height, 60–75 character
  measure.
- **Dark and light** through `@media (prefers-color-scheme: dark)` with custom properties on `:root`.
- **Respect motion.** Wrap animation in `@media (prefers-reduced-motion: no-preference)`.
- **Responsive by construction.** Fluid widths, `max-width` on the content column, readable at 375 px.
- **Print stylesheet.** Reports get printed and PDF'd: a `@media print` block that drops the nav,
  expands `<details>`, and keeps tables off page breaks.
- **Restrained palette.** One accent colour; colour only where it carries meaning.
- **Visible focus** on every control.

## Data integrity

- Real numbers with units and sources. Illustrative values labelled in the page.
- Charts: labelled axes, units, a title stating the takeaway, honest ranges.
- A table that hides its evidence behind a click also hides it from a reviewer reading a PDF — keep
  the numbers in the markup, and let the interaction sort or expand rather than reveal.

## Verification

Open the file and check: the console is clean, no failed requests, layout at 375 px and 1440 px,
keyboard tab order, dark mode, reduced motion, and the print preview. Then confirm it opens from disk
over `file://`. Full gate: [checklist.md](checklist.md).

## Deliverable message

Path, how to open it, the verdict in one line, and what the reviewer should read first. The document
states the rest.

## Anti-patterns

- A report that could have been a three-paragraph memo.
- A framework and a build step for a one-off document.
- Interactivity that hides the conclusion behind a click.
- A page that needs a network fetch to be readable.
- Charts carrying unlabelled axes, or numbers with no source.
