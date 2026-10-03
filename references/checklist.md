# Verification checklist — before you deliver

An artifact you have not opened is a guess. Run the gate for the rung you climbed.

## All rungs

- [ ] Answer first: the conclusion is in the first sentence or two — no preamble, no restating the
      question, no recap.
- [ ] Within budget: every sentence changes what the reader knows or does, and the length fits the
      genre (see [conciseness.md](conciseness.md) for budgets).
- [ ] The artifact answers the exact question asked, not a neighbouring question.
- [ ] It is self-contained: one file where possible, no build step, no network needed to be useful.
- [ ] No API keys, tokens, absolute private paths, or private data inside it.
- [ ] Numbers carry units; numbers carry sources if they are not yours; no invented data.
- [ ] You know the path, and you tell the user how to open it.
- [ ] You have not also re-narrated the entire artifact in chat.

## Rung 1 — clarity (ASD-STE100)

- [ ] One word per meaning; no synonym drift inside one document ("start" never becomes "begin").
- [ ] Sentences under the limit (STE: 20 words procedural, 25 descriptive). Check the longest one.
- [ ] Active voice, simple tenses, one instruction per sentence.
- [ ] The dial you claimed is the dial you used (100% STE reads like a manual; ~80% keeps warmth).
- [ ] Every term of art is either approved vocabulary or explicitly defined.

## Rung 2 — diagram

- [ ] It actually parses/renders. Mermaid: render it (GitHub preview, `mmdc`, or a viewer) — do not
      ship unparsed Mermaid. SVG: open it in a browser.
- [ ] Every arrow has a direction that means something; every edge has a verb or label.
- [ ] Axes, units, and legend labeled. Color is never the only encoding.
- [ ] One diagram type only. Readable at the size it will be viewed (≤ ~12 top-level nodes).
- [ ] Caption states the takeaway, not the topic ("Retries double p99 latency", not "Retry diagram").

## Rung 3 — HTML page

- [ ] Opened it in a real browser (or headless screenshot) and looked at it. Not "it should render".
- [ ] Zero console errors and zero failed requests.
- [ ] It works from `file://` offline, and after a hard refresh.
- [ ] Responsive at ~375 px and ~1440 px; nothing overflows or overlaps.
- [ ] Keyboard accessible: tab order sane, focus visible, controls are real controls.
- [ ] `prefers-color-scheme` and `prefers-reduced-motion` respected.
- [ ] Interactivity serves understanding (slider, scrubber, step-through, toggle, quiz) — not just motion.
- [ ] Text is selectable; a reader can copy the conclusion out.

## Rung 4 — explainer video

- [ ] Audio was generated first, and scene timing is driven by the audio, not guessed.
- [ ] Total runtime matches the plan (30–180 s for one concept). Narration pace ~140–160 wpm.
- [ ] A low-res draft was watched end to end before the final render.
- [ ] Last frame is intentional; nothing is cut mid-sentence or mid-motion.
- [ ] Audio and visuals line up at every scene boundary, not just the start.
- [ ] Captions exist (burned in or sidecar `.srt`) and match the audio.
- [ ] Nothing on screen claims to be real footage it is not.
- [ ] You also delivered the script/outline, so the content is greppable and patchable.

## Rung gate (stop signals)

Stop and drop a rung, out loud, when any of these is true:

- You cannot render or open the artifact in this environment.
- The content does not actually have the shape the rung assumes (a "video" of a static list).
- The user asked for prose and did not opt into a bigger artifact.
- The render is going to run longer than a few minutes and the user does not know yet.
