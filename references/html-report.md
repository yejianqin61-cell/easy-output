# Rung 3 — HTML report

The report is **filled, not designed**. Copy [`report-template.html`](report-template.html), replace
its slots, and leave the `<style>` block untouched. Roughly 60% of the finished page is that
stylesheet; the agent contributes the content on top of it.

That is what keeps the output looking considered. Hand-authored CSS from a model produces a page that
opens but reads badly, because every visual decision competes with every other one. Here those
decisions were made once, in the template, and then compiled into every report.

## When rung 3 is right

The document will be re-read, circulated, reviewed by several people, or compared against another
version, or it carries enough tables that Markdown stops being scannable.

**Ask before building.** The ask is required; the artifact is not. Deliver the Markdown first, then ask
once.

## The fill-in contract

1. Copy `report-template.html` to `./<slug>.html`.
2. Replace every `{{TOKEN}}` and every `<!-- SLOT -->` marker.
3. Delete every comment that remains. Nothing starting with `<!--` may survive.
4. Add no CSS. No new `<style>`. The only `style=` allowed sets a custom property: `--v`, `--max`, or
   `--cols`.
5. Use only the classes in the vocabulary below.
6. Open it, and run the rung 3 gate in [checklist.md](checklist.md).

## Slots

| Marker | What goes in |
|---|---|
| `{{LANG}}` | `zh-CN` or `en`, matching the document's language |
| `{{TITLE}}` | the claim, used in both `<title>` and `<h1>` |
| `{{DOC_TYPE}}` | Project analysis / Evaluation / Execution plan / Spec / ADR / Runbook |
| `{{SUBTITLE}}` | one line of context. Delete the element when there is nothing to say |
| `.meta` rows | status, date, what the document locks, where the numbers came from. Delete unused rows |
| `{{VERDICT_HEADING}}` | the verdict's label, for example "Recommendation" |
| `{{VERDICT}}` | ≤150 words: recommendation, cost, main risk, what is asked of the reader |
| TOC `<li>` | one per section, in the order the reader asks |
| sections | one `<section class="sec" id="sec-N">` per heading, with the `id` matching the TOC link |
| `{{COLOPHON}}` | what this is, what was generated, the date |

## Class vocabulary

| Class | Renders | Use it for |
|---|---|---|
| `.kicker` | a 12px mono uppercase label | the document type |
| `.meta` with `dt`/`dd` | a two-line status strip | date, status, locks, source |
| `.verdict`, `.verdict-title`, `.verdict-body` | the framed box at the top | the ≤150-word verdict |
| `.toc` | a horizontal link list | the section list |
| `.sec`, `.sec-body` | one card per section | a heading's content |
| `table.data` inside `.table-wrap` | a bordered, scrollable table | options, comparisons, scorecards |
| `.st` with `--ok` / `--no` / `--warn` | a ✓ / ✗ / ! badge | status columns |
| `.callout` with `--ok` / `--warn` / `--err` | a tinted box with a title | a conclusion, a warning, a risk |
| `.flow`, `.flow-step` | a numbered vertical rail | a linear process or sequence |
| `.grid-2` / `.grid-3` with `.card` | responsive card grids | parallel options, at-a-glance facts |
| `.bars`, `.bar`, `.bar-track`, `.bar-fill` | labelled bars against a maximum | limits, budgets, scores |
| `.kv` with `dt`/`dd` | a term and definition grid | a short metadata block inside a section |
| `figure.diagram` | an inline-SVG wrapper | a real diagram, when a table or a flow will not do |
| `pre > code` | a code block | commands, configuration |
| `.colophon` | the muted footer | provenance |

## Rules for the content you insert

- **Same facts as the Markdown version.** The report adds navigation and legibility, and no claims.
- **Copy the verdict word for word.** A report that disagrees with the document it renders is worse
  than no report.
- **Status columns become badges.** A cell reading `ok approved` becomes
  `<span class="st st--ok">approved</span>`.
- **A bar needs a maximum.** `style="--v:13;--max:20"` on the `.bar`. A bar without `--max` is a lie
  with a gradient, and an axis that starts anywhere but zero is the same lie.
- **`figure.diagram` is the last resort.** Coordinates on a 20px grid, stroke and fill only from the
  template's variables, a `<title>` for screen readers, and a `<figcaption>` stating the takeaway.
- **No controls.** No sorting, filtering, or toggles: a report is read, not operated. Content that
  genuinely must be operated belongs in an interactive page, which is a different rung.
- **Delete the slots you do not need**, and nothing else.

## What the template already handles

- Light and dark through `prefers-color-scheme`, with every colour behind a custom property, so your
  content never names a colour.
- The type scale, the measure limits, and the one rhythm rule that keeps sibling spacing even.
- A print stylesheet: the TOC is dropped, and sections avoid page breaks.
- Responsive behaviour at 760 px, including the card grids and the bars.
- `prefers-reduced-motion` and a visible focus ring.
- Semantic structure: `main`, `header`, `nav`, `article`, `section`, `footer`, `dl`, `table`,
  `figure`. Keep them.

## Verification

Run the rung 3 gate in [checklist.md](checklist.md). Two checks catch most failures: `grep -c '{{'
<slug>.html` returns 0, and the page opens from `file://` in a real browser.

## Anti-patterns

- Authoring CSS. It is the fastest route back to an ugly page.
- Inventing class names outside the vocabulary. They render as unstyled text.
- Shipping with `{{` or `<!--` markers still in the file.
- Rewriting the verdict or the numbers for the report, so the two versions disagree.
- A bar without `--max`, or an axis that starts above zero.
- Adding a table that does not exist in the Markdown version: a new claim nobody reviewed.
