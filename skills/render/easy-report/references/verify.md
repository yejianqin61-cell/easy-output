# The render gate

Run this on the file you are about to hand over, not on the file you think you produced. Two checks
catch most failures: no marker survives, and the page opens from `file://` in a real browser.

- [ ] Built from `references/report-template.html`, and the `<style>` block is unchanged.
- [ ] No `{{` and no `<!--` anywhere in the file.
- [ ] No CSS added: no new `<style>`, and no `style=` beyond a `--v`, `--max` or `--cols` custom
      property.
- [ ] Class names come only from the vocabulary in [fill-in-contract.md](fill-in-contract.md).
- [ ] Opened it in a real browser, or took a headless screenshot. Not "it should render".
- [ ] The verdict matches the source document word for word.
- [ ] Every TOC link resolves to a section id that exists, and every section appears in the TOC.
- [ ] Zero console errors, zero failed requests, and it works offline from `file://`.
- [ ] Readable at 375 px and at 1440 px, with no horizontal scroll on the page body.
- [ ] Print preview checked: the TOC is gone, no section splits across pages, tables are not clipped.
- [ ] Dark mode checked: no invisible text, no washed-out badges.
- [ ] Keyboard: tab reaches every link, and focus is visible.
- [ ] The verdict can be selected and copied out as text.

## Stop signals

Stop, and say so, when any of these holds:

- You cannot open the artifact in this environment.
- The source document does not exist yet. Write it first.
- The page needs controls to be useful. That is an interactive page, a different artifact.
