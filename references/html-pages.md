# Rung 3 — Single-file interactive pages

An HTML page is the first rung where the reader can **act**: change a parameter, step through
time, toggle a comparison, hover to reveal. That interaction is the whole reason to climb this
high — if the page is static, rung 2 was cheaper and just as good.

## When rung 3 is right

- The idea only clicks when something is **varied** ("what happens when the batch size grows?").
- The reader will **re-consult** the artifact, not read it once.
- The content has **multiple layers** the reader should reveal at their own pace (overview → detail
  → edge case).
- The content is **spatial or temporal** and benefits from motion under the reader's control.
- The artifact will be **shared** with someone else ("open this file").

If none of these hold, drop to rung 2.

## The one-file contract

- **One `.html` file.** Inline CSS and JS in `<style>` and `<script>`. No build step, no bundler,
  no framework, no npm.
- **Opens from `file://` with no server** and works offline.
- **No CDN dependency for the content to be useful.** If you use a CDN library (e.g. a chart or math
  renderer), the page must degrade to readable content if the request fails. Prefer zero libraries:
  hand-written SVG, `<canvas>`, and the platform DOM are usually enough.
- **No secrets, no private paths, no local absolute file references** inside the artifact.
- **Portable filename**: `<topic-slug>.html`, lowercase, hyphens.

## Narrative skeleton

Structure the page like an explanation, not like a document:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>The claim, not the topic</title>
  <style>/* inline */</style>
</head>
<body>
  <header>
    <h1>The claim</h1>            <!-- title states the takeaway -->
    <p class="tldr">3–5 sentence verdict, in ~80% ASD-STE100.</p>
  </header>
  <nav><!-- optional: in-page sections, for long pages --></nav>
  <main>
    <section id="intuition"><h2>Why it feels like this</h2>…</section>
    <section id="mechanism"><h2>What is actually happening</h2>…</section>
    <section id="play"><h2>Try it</h2>…interactive…</section>
    <section id="caveats"><h2>Where this breaks</h2>…</section>
  </main>
  <footer>Sources, generated date, one line on what was generated.</footer>
  <script>/* inline, no build step */</script>
</body>
</html>
```

Rules for the skeleton:

- Sections are **questions the reader has**, in the order they have them.
- The "Try it" section is the point of the page. Everything before it sets it up.
- Caveats and limits are a real section, not a footnote. Overselling is the fastest way to lose trust.
- Footer states provenance: where the numbers came from, what was generated, when.

## Interaction patterns that earn their keep

| Content | Interaction |
|---|---|
| A parameter with a visible effect | Slider + live readout + live visual |
| A process over time | Play / pause / step / scrub + frame counter |
| Two options | Toggle that overlays both, or a side-by-side that stays in sync |
| A hierarchy | Expand/collapse, or a "zoom into this node" step-through |
| A dense figure | Hover to highlight the part and dim the rest, with a tooltip |
| A wrong mental model | A "before/after" switch that shows the misconception versus reality |
| Retention | A short self-quiz at the end (3 questions, immediate feedback) |

Two rules: **the initial state must already be informative** (never a blank canvas waiting for a
click), and **every control needs a keyboard-reachable equivalent** (a real `<button>`, `<input
type="range">`, `<details>`).

## Design defaults

- **Typography first.** System font stack, ~16–20 px body, 1.5–1.7 line-height, measure of 60–75
  characters. That single set of choices does most of the work.
- **Dark and light.** Use `@media (prefers-color-scheme: dark)` with CSS custom properties on
  `:root`; do not hardcode hex colours in components.
- **Respect motion.** Wrap animation in `@media (prefers-reduced-motion: no-preference)`; honour
  the OS setting.
- **Responsive by construction.** Fluid widths, `max-width` on the content column, no fixed pixel
  layouts. It must be readable at 375 px.
- **Restrained palette.** One accent colour, neutrals otherwise. Colour only where it carries
  meaning.
- **Focus visible.** `:focus-visible` outline on every interactive element.
- **Print-friendly.** Content readable with CSS off — this is the cheapest accessibility and
  resilience test.

## Data integrity

- Real numbers only, with units, and with sources.
- Charts: labeled axes, units, a title that states the takeaway, and honest axis ranges.
- If a number is illustrative or synthetic, label it as such in the artifact — visibly.
- No decorative dashboards. A metric that does not change the reader's understanding is noise.

## Verification

Before delivering, actually open the file in a browser (or take a headless screenshot) and check:
console is clean, no failed requests, layout at 375 px and 1440 px, keyboard tab order, dark mode,
reduced motion. Then confirm from disk over `file://`. Full gate:
[checklist.md](checklist.md).

## Deliverable message

Path, one line on how to open it, one line on the takeaway, one line on what to try first. Do not
re-narrate the page.

## Anti-patterns

- A static page that could have been a diagram (rung 2 was cheaper).
- A framework and a build step for a one-off artifact — the opposite of discardable.
- Animation that plays on load and cannot be paused or scrubbed.
- A generated page with invented data behind a polished chart.
- Interactivity that hides the conclusion behind a click.
- A page that only works after a network fetch.
