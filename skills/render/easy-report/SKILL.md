---
name: easy-report
description: >-
  Use when a document should reach the reader as a single-file HTML page instead of Markdown: a review,
  a summary, an audit, a plan, or anything the reader will re-read, circulate, print or compare. Fills a
  fixed template, so the page looks considered and carries exactly the facts the Markdown already has.
  Triggers on HTML 报告, 出一份 HTML, 排版, 给领导看, 要转发, 打印出来, HTML report, make it a page,
  one-pager. Other skills reach it when the user picks the HTML output.
---

# Easy report

A report is the same document, rendered for reading rather than for editing. It adds navigation and
legibility, and no claims.

The page is **filled, not designed**. Copy
[references/report-template.html](references/report-template.html), replace its slots, and leave the
`<style>` block untouched. Roughly 60% of the finished page is that stylesheet, and it is the reason the
output looks considered. Hand-authored CSS produces a page that opens and reads badly, because every
visual decision then competes with every other one.

## Process

Five steps. Each ends on a check you can make.

### 1. Name the source

A report renders a document that already exists. Point at its path. Where there is no document yet,
write it first: this skill renders, it does not decide.

**Done when** the source path exists and you have read it.

### 2. Copy the template

`cp references/report-template.html ./<slug>.html`.

**Done when** the copy opens in a browser and shows the placeholder page.

### 3. Fill the slots

Work from [references/fill-in-contract.md](references/fill-in-contract.md). It covers every `{{TOKEN}}`,
every `<!-- SLOT -->`, the class vocabulary, and the rules for the content you insert. Delete the slots
the document does not need, and nothing else.

**Done when** `grep -c '{{' <slug>.html` and `grep -c '<!--' <slug>.html` both return 0.

### 4. Keep the facts identical

The verdict word for word. The same numbers, the same statuses, the same tables. A report that disagrees
with the document it renders is worse than no report, because the reader trusts the prettier one.

**Done when** every claim in the page can be found in the source document, and no claim exists only in
the page.

### 5. Open it

Open the file from `file://` in a real browser. Check dark mode, check print preview, check a 375 px
window. Run the gate in [references/verify.md](references/verify.md).

**Done when** the gate passes on the file you are about to hand over.

## Delivery

Give the path and how to open it. Do not restate the document in chat.

## Anti-patterns

- Authoring CSS. The fastest route back to an ugly page.
- Inventing class names outside the vocabulary. They render as unstyled text.
- Shipping with a `{{` or `<!--` marker left in the file.
- Rewriting the verdict or the numbers for the page, so the two versions disagree.
- Adding a table the source document does not have: a new claim nobody reviewed.
- A bar without `--max`, or an axis that starts above zero.
