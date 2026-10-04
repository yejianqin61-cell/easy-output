# Verification checklist — before you deliver

An artifact you have not opened is a guess. This is the gate a reviewer will run; run it yourself
first.

## Every document

The document contract, checked in order (see [documents.md](documents.md)):

- [ ] The verdict sits in the first ≤150 words: recommendation, cost, main risk, what is asked of the
      reader.
- [ ] A reviewer can disagree with the verdict using only that summary.
- [ ] Every heading is a question the reader has, in the order they ask it.
- [ ] An out-of-scope section exists and names real refusals.
- [ ] Assumptions are labelled as assumptions; open questions carry a way to resolve each.
- [ ] Numbers carry units, sources, and a date. Illustrative values are marked in the same line.
- [ ] The length fits the budget for its type.
- [ ] No section answers a question the reader does not have.
- [ ] Nothing asserts a decision nobody made.

## All deliverables

- [ ] It answers the exact request, not a neighbouring one.
- [ ] Every sentence changes what the reader knows or does.
- [ ] Self-contained: one file, no build step, no network needed for it to be useful.
- [ ] No API keys, tokens, absolute private paths, or private data inside it.
- [ ] You know the path, and you tell the reader how to open it.
- [ ] You have not also re-narrated the document in chat.

## Rung 1 — clarity (ASD-STE100)

- [ ] One word per meaning; no synonym drift inside one document ("start" never becomes "begin").
- [ ] Sentences under the limit (STE: 20 words procedural, 25 descriptive). Check the longest one.
- [ ] Active voice, simple tenses, one instruction per sentence.
- [ ] The dial you claimed is the dial you used (100% STE reads like a manual; ~80% keeps warmth).
- [ ] Every term of art is either approved vocabulary or explicitly defined.

## Rung 2 — diagram

- [ ] It actually parses or renders. Mermaid: render it (GitHub preview, `mmdc`, a viewer). SVG: open
      it in a browser.
- [ ] Every arrow has a direction that means something; every edge carries a verb or a label.
- [ ] Axes, units, and legend labelled. Colour is never the only encoding.
- [ ] One diagram type only, readable at the size it will be viewed (≤ ~12 top-level nodes).
- [ ] The caption states the takeaway ("Retries double p99 latency") rather than the topic ("Retry
      diagram").

## Rung 3 — HTML report (filling the shipped template)

- [ ] Built from `report-template.html`, not from scratch. The `<style>` block is unchanged.
- [ ] No `{{` and no `<!--` left anywhere in the file. Grep it before delivering.
- [ ] No CSS added: no new `<style>`, and no `style=` beyond a `--v` / `--max` / `--cols` custom
      property.
- [ ] Class names come only from the vocabulary in [html-report.md](html-report.md).
- [ ] Opened it in a real browser (or took a headless screenshot). Not "it should render".
- [ ] The verdict block sits at the top, matches the Markdown wording, and is ≤150 words.
- [ ] Every TOC link resolves to a section id that exists, and every section appears in the TOC.
- [ ] Zero console errors, zero failed requests. Works from `file://` offline.
- [ ] Readable at 375 px and at 1440 px, with no horizontal scroll on the page body.
- [ ] Print preview checked: TOC gone, no section split across pages, tables not clipped.
- [ ] Dark mode checked (or the OS toggle simulated): no invisible text, no washed-out badges.
- [ ] Keyboard: tab reaches every link or control, and focus is visible.
- [ ] The verdict can be selected and copied out as text.
- [ ] The report was offered only after the Markdown document was done, and built only on request.

## Stop signals

Stop, drop back a rung, and say so when any of these holds:

- You cannot open or render the artifact in this environment.
- The content lacks the shape the rung assumes.
- The user asked for a memo and did not opt into a report.
- A render would run longer than a few minutes and the user does not know yet.
