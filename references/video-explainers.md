# Rung 4 — Custom explainer videos

**This is the opt-in rung.** It is here because it is sometimes right, not because it is the point of
this skill. Reach for it only when the content is a mechanism that unfolds over time and no cheaper
rung can show it, and only after the user agrees to the cost. If the real problem is that the text is
too long or too dense, fix the text — rungs 1 and 2 — first.

The most expensive rung, and the one that explains things the other rungs cannot: a mechanism that is
**invisible and unfolds over time**. It is also, per the source post, the rung that is newly viable —
"actually starting to work".

**Always ask before starting.** A rung-4 artifact costs minutes to hours of compute and cannot be
patched like text.

## What makes 3Blue1Brown-style work

Decode the style before copying it. The style is not the colour palette:

1. **One idea per scene.** The scene ends when the idea lands.
2. **The motion *is* the explanation.** An object moves, transforms, or accumulates; the animation
   is the argument, not an illustration of it. Static slides with a voice-over are a podcast.
3. **The narration carries the logic**, the visuals carry the structure. They are not redundant.
4. **Precise geometry.** When the maths says a line is tangent, it is drawn tangent. Hand-waving
   visuals destroy trust faster in video than in text.
5. **Continuity.** Objects persist and transform between scenes, so the viewer builds one mental
   model instead of nine disconnected pictures.
6. **Restraint.** Two or three colours, one accent for emphasis, no decorative motion, quiet music
   or none.
7. **Pacing.** ~140–160 words per minute. Slow enough to think, fast enough not to bore. Silence is
   allowed and useful.

## Two production routes

| Route | Tools | Good for | Cost |
|---|---|---|---|
| **Code-rendered (default)** | Manim Community Edition (the maintained fork of 3b1b's engine), Motion Canvas, Remotion (React), or matplotlib + ffmpeg | maths, geometry, data, diagrams, anything where precision matters | deterministic, reproducible, slow to render |
| **Generative video** | hosted text/image-to-video models | mood, metaphor, b-roll, "what it might look like" | fast, but invents text, geometry, and numbers |

**Default: code-rendered visuals.** For an explanation, precision beats realism. Use generative
video only for interstitial or metaphorical footage, and never for anything bearing a number, a
label, or a formula.

## Audio first — the audio is the clock

This single rule prevents most video rework:

1. Write the **script** first, scene by scene, one idea per scene.
2. Generate **narration per scene** as separate audio files — never one long file.
3. **Measure the duration of each scene's audio.**
4. Drive the animation timing from those durations. Do not guess, and do not render first and then
   stretch the audio to fit.
5. Mux with ffmpeg; the audio track is authoritative.

Consequences: script edits are cheap until step 2; after that, a wording change means re-recording
one scene. Keep narration in per-scene files so a fix stays local.

### Narration options

| Option | Cost / access | Notes |
|---|---|---|
| ElevenLabs | paid, free tier; the user's own API key | strongest quality; returns **word-level timestamps** — use them to drive captions and emphasis |
| Kokoro (82M) | free, local, Apache-2.0 | small, fast on CPU, surprisingly good; the usual local default |
| Piper | free, local, MIT | very fast on CPU, many voices and languages; quality below Kokoro |
| Coqui XTTS-v2 | free, local, **CPML — non-commercial** | voice cloning; check the licence before shipping anything public |
| Chatterbox (Resemble) | free, local, MIT | newer, expressive |
| `edge-tts` | free, no key, **requires network**, unofficial | excellent quality for zero setup; treat the ToS as a risk for public artifacts |
| OS built-in (SAPI / `say`) | free, offline | last resort; instantly recognisable as robotic |

Rules:

- **Never hardcode a key.** Read it from the environment (`ELEVENLABS_API_KEY`) at run time, and
  never write it into a generated file that the user might commit or share.
- **No key? Do not stop.** Pick a free local option, offer the choice, and proceed. Ask the model
  to find current free alternatives rather than assuming.
- **One voice for one video.** A voice change mid-video reads as a bug.
- State the licence of any local model you use, especially for anything the user will publish.

## Structure and budget

A single concept fits in **60–180 s**. Beyond ~4 minutes, split it into parts.

| Beat | Share | Content |
|---|---|---|
| Hook | ~10% | The surprising fact or the question. No logo, no intro music. |
| Intuition | ~30% | A visual metaphor that is honest about being one. |
| Mechanism | ~35% | Step by step, the actual machinery, precise. |
| Numbers / example | ~15% | One concrete case, real values. |
| Recap + caveat | ~10% | What to remember, and where this breaks. |

## Verification and honesty

- **Render a low-resolution draft first** (e.g. 480p, low quality) and watch it end to end. Only
  then render the final. This is the cheapest quality lever in the whole pipeline.
- Check the **last frame** — nothing cut mid-sentence or mid-motion.
- Check audio/visual alignment at **every scene boundary**, not just the start.
- Ship **captions** (burned in or `.srt`) derived from the narration timestamps.
- Any number on screen must have a source in the script.
- Generated footage must not be presented as real. Say what was generated.

## Deliverables

Always deliver more than the video:

1. `explainer.mp4` — the video.
2. `poster.png` — a representative frame, for the file browser and for previews.
3. `script.md` — the per-scene narration and on-screen text. This is the part that stays useful
   after the video is discarded, and it is what makes a wording fix cheap.

## Failure modes

- Rendering before the script is final: every wording change invalidates the audio and the timing.
- Static slides plus voice-over, sold as an explainer. That is a narrated document.
- Generated footage carrying text, formulas, or numbers — it will be wrong and illegible.
- Guessed timings, then stretched audio. Audio artefacts and drifting sync.
- No draft pass, then a dark, cut-off, or silent final render.
- A 20-minute video for a two-sentence idea.
