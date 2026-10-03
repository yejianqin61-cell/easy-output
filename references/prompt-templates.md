# Prompt templates

Copy, paste, adapt the bracketed parts. They are written for an agent with this skill loaded, and
they also work on a plain chat model.

The order matters: **cut first, clarify second, change medium third.** Most of the value is in
templates 0–3, which cost nothing and fix the majority of bad output.

## 0. The universal opener

> Before you answer: make this as readable as it can be. Cut anything that does not change what I
> know or do, put the answer in the first sentence, and prefer a list or a table over prose for
> parallel items. Then, if a diagram would read faster than two paragraphs of text, say so and give
> me one. Do not build a page or a video unless I ask, and tell me the cost first if it would take
> more than a couple of minutes.

## 1. Cut and rewrite for readability

> Rewrite the text below so it is short and clear, without losing information I need.
>
> - Put the conclusion in the first one or two sentences.
> - Delete the preamble, the restatement of my question, any recap (the text is short), hedges, and
>   "it's worth noting" filler.
> - One idea per sentence. Active voice. No nominalizations.
> - Three or more parallel items become a list; items compared on the same attributes become a table.
> - Target length: [150 words / one screen]. If you must exceed it, tell me why in one line.
> - Then show me, as a short list, what you deleted and why. If you deleted something that mattered,
>   say so.
>
> [paste text]

## 2. Rung 1 — ASD-STE100, full strength

> Explain [topic] in ASD-STE100 (Simplified Technical English). Follow the writing rules and use the
> approved vocabulary. Maximum 20 words per sentence for instructions, 25 for description. One
> instruction per sentence. Active voice. Simple tenses. One word for one meaning, and use the same
> word every time. No idioms, metaphor, or humor. Keep the articles. Explain it to [audience], who
> already knows [assumed background].

## 3. Rung 1 — the 80% dial (default for explanations)

> Explain [topic] at about **80% of the way to ASD-STE100**. Keep the discipline: short sentences, one
> idea per sentence, active voice, simple tenses, one word for one meaning, no nominalizations. Drop
> the stiffness: normal vocabulary is fine, and you may use exactly **one** analogy, clearly marked as
> an analogy. Put the conclusion first. Do not pad. Target [N] words.

## 4. Rung 1 — self-audit

> Review the text you just wrote as a hostile editor, in two passes.
>
> Pass 1 — conciseness: for every sentence, does it change what I know or do? List the sentences that
> fail and delete them.
> Pass 2 — clarity: check one word per meaning, active voice, sentence length, one instruction per
> sentence, noun clusters ≤ 3 words, no nominalizations, no idioms.
>
> Give me the corrected version and a list of what you changed. Add no new information.

## 5. Rung 2 — diagram, type-first

> Draw [the process / the state machine / the interaction / the data model] for [subject] as a diagram.
>
> - First tell me the one claim the diagram makes.
> - Choose the diagram type that fits the relation, and say why.
> - Output Mermaid inside a ` ```mermaid ` fence. If it renders on GitHub, prefer that syntax.
> - Every arrow needs a label. Every node label must match the real names in [codebase/doc].
> - Maximum ~12 top-level nodes; group the rest.
> - Give me a title and a one-sentence caption that states the takeaway.
> - Then verify your own Mermaid: check the syntax, and tell me how I should render it.

## 6. Rung 2 — quick shape in chat

> Before you explain, draw the shape of [subject] as ASCII box art, ≤ 100 characters wide, in a fenced
> code block. One diagram, one claim. Then give me 4 sentences at 80% ASD-STE100 — and only if the
> diagram does not already say it.

## 7. Rung 3 — single-file interactive explainer

> Build a single self-contained HTML file that explains [topic] to [audience].
>
> Requirements:
> - One file. Inline CSS and JS. No build step, no framework, no CDN needed for the content to work.
>   It must open from `file://` and work offline.
> - Title = the claim, not the topic. Start with a 3–5 sentence TL;DR written at 80% ASD-STE100.
> - Sections are the questions I actually have, in order: intuition → mechanism → **try it** → where
>   this breaks. No introduction section and no conclusion section.
> - The "try it" section is the point: give me [a slider over X / a scrubber over time / a toggle
>   comparing A and B / a step-through of the stages] with a live readout.
> - Real numbers only, with units and sources. If a value is illustrative, label it in the page.
> - System font stack, 16–20px body, responsive down to 375px, `prefers-color-scheme` and
>   `prefers-reduced-motion` respected, keyboard accessible, visible focus.
> - Footer: what was generated, sources, date.
> - Then open it (or screenshot it), check the console is clean, and tell me what you saw. Do not hand
>   it over without rendering it.
>
> Save it as `[slug].html` and reply with: path, how to open it, the takeaway, what to try first.

## 8. Rung 3 — turn an existing artifact into a page

> Take the diagram/text above and turn it into a single-file interactive HTML page. The interaction
> must add understanding, not decoration: let me [step through the stages / vary the parameter /
> toggle the two models]. Keep every fact identical; cut anything that does not earn its place; do not
> invent data to make the page richer.

## 9. Rung 4 — explainer video, full pipeline

> Create a [60–180] second [3Blue1Brown / Manim] style explainer video on [topic].
>
> Process, in this order:
> 1. Write `script.md`: per-scene narration and on-screen text. One idea per scene. Beats: hook →
>    intuition → mechanism → numbers → recap + caveat. Nothing on screen that isn't in the script.
> 2. Generate the narration **per scene** as separate audio files with [ElevenLabs, reading my
>    `ELEVENLABS_API_KEY` from the environment / a free local TTS — see below]. Never hardcode the key,
>    and never write it into a file.
> 3. Measure each scene's audio duration and **drive the animation timing from it**. Audio is the clock.
> 4. Render the visuals with [Manim CE / Remotion]. Precise geometry; two or three colours; motion that
>    *is* the explanation.
> 5. Render a **480p draft first** and let me watch it before the final render.
> 6. Mux audio and video with ffmpeg, add captions from the narration timestamps.
>
> Deliver `explainer.mp4`, `poster.png`, and `script.md`. Tell me the total render time before you
> start, and ask me before any step that will run longer than a few minutes.

## 10. Rung 4 — free / local audio instead of a paid key

> I do not have an ElevenLabs key. Find me the best currently available **free** TTS options that can
> run on my own machine, with their licences, then use the best one for this video. Prefer permissive
> licences (MIT / Apache-2.0) if I might publish the result. If you need to download a model or install
> a package, tell me the size and ask first. Do not stop the task because an API key is missing — route
> around it.

## 11. Rung 4 — script only (cheap gate)

> Before any rendering: give me the video as a script only — per scene, narration text plus a
> description of what moves on screen, with estimated durations. No code yet. I will approve the
> script, and only then do we render.

## 12. Verification pass

> Review the artifact you just produced as a hostile reviewer. For [text: check length against the
> budget and cut anything that does not change what I know / HTML: open it and check console errors,
> layout at 375px and 1440px, keyboard access, dark mode, reduced motion, offline use / video: check
> the last frame, scene-boundary sync, total runtime, caption match / diagram: check it parses, every
> edge label, ≤12 nodes, labelled axes].
> List what is broken, fix it, then tell me what you fixed. Do not claim it works without checking.

## 13. One-line uplevel offer

> Want this as [an interactive page / a 90-second explainer video]? It would cost about [estimate] to
> make. Say the word. — If what you actually want is just less text, I can cut this by a third instead.

## 14. Stop signal — when text is right

> Stay in text. I need [exact wording I can quote / something I can put in a PR / something I can grep].
> Do not build a page or a video. Just make it short and clear.

## Notes on using these

- **Do templates 0–3 first.** They are free, and they fix most bad output. Everything above rung 2 is
  a deliberate investment.
- Keep the **medium decision** in the prompt, but after the readability instruction — not instead of it.
- Always ask for the **draft pass** on rung 3 and 4. Cheap, and it catches most failures.
- Always ask for the **artifact plus its source file** (`script.md` for video). The video is
  discardable; the script is what you keep.
- If the artifact looks good but you cannot open it, it is not done — go back to template 12.
