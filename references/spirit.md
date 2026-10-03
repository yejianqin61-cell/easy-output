# The spirit — what this skill is compressing

Source: Andrej Karpathy's post of **2 October 2026** on making LLM output easier to understand —
a single post, not a thread: <https://x.com/karpathy/status/2105819303471976479>. It is quoted
below, then turned into operating rules. This file is an independent interpretation. It is not
authored, reviewed, or endorsed by the author.

## The original post

> We'll be spending a lot more time trying to understand the outputs of language models. A few
> thoughts, tips & tricks:
>
> **Writing.** Something I've had success with: Ask your LLM to explain something in ASD-STE100,
> it's a controlled language specification originally developed for aerospace maintenance
> documentation. LLMs well-versed in this language and it comes with heavy constraints on clean
> writing style that I often find a lot more readable. Sometimes I've tried to soften it a bit e.g.
> ask for "80% of the way to ASD-STE100" because the spec is quite stringent. But even better:
>
> **Diagrams / images.** Instead of writing, ask your LLM to create a diagram. These can be a lot
> easier to process, parse, and understand. But even better:
>
> **Web pages.** Ask for output "in HTML" to get a beautiful, interactive webpage. LLMs are getting
> really good at frontend and can create beautiful experiences, animations, etc. But even better:
>
> **Explainer videos.** The output format I am most bullish on is fully custom / bespoke explainer
> videos generated on any arbitrary topic. Experiment with things like "Create a 3b1b style video
> explainer on X. Use my ElevenLabs API key for audio narration". (you'd need an API key for the
> latter or you can ask your LLM to find you decent free alternatives that use your local compute).
> This is actually starting to work!
>
> In summary:
> - As LLMs get better, they will do more and more of the legwork autonomously, and a lot more of
>   our work will rise up the abstractions into oversight and understanding.
> - Luckily, LLMs can help here too because as intelligence and code are increasingly abundant, you
>   can ask for large, custom, discardable software artifacts (e.g. web apps, video explainers) that
>   would have never made sense to create before. Push the boundaries here and you'll be surprised.

*(Reproduced from public unrolls of the post; x.com requires a login to read it directly. Two images
were attached — one appears to be the ASD-STE100 rules and the approved-word dictionary.)*

**Read the escalation the way it was written: four rungs, and each step up is introduced with the
same two words — "But even better:".** That phrase is the thesis. The medium is a variable with a
gradient, not a fixed choice, and each rung converts more of the model's internal state into
something the human eye can parse directly.

## The framing

Two shifts are happening at once, and the second is caused by the first:

1. Models increasingly do the legwork themselves. Less of our work is production.
2. Our work rises up the stack into **oversight and understanding**.

So the bottleneck moves. It is no longer "can we produce the artifact" — it is "can a human
absorb it fast and deeply enough to supervise it". The output medium is therefore a first-class
engineering decision, and it is usually left at its default value.

## Ten principles

**1. Output format is a variable, not a constant.** Chat prose is the default nobody chose. The
biggest single lever on comprehension is not prompt phrasing — it is *which medium* you ask for.

**2. Comprehension is bounded by the reader's perceptual channel.** Prose is serial and
symbolic. A diagram is parallel and spatial. An interactive page is explorable. A narrated,
animated video uses motion and voice. Each rung loads more of the human's hardware — which is
why "but even better" keeps working.

**3. Text is the right answer when precision, greppability, or normative force matters.** Do not
treat the ladder as "video always wins". The choice is: the cheapest medium that fully opens the
channel the content needs.

**4. Constraints produce readability, not taste.** ASD-STE100 is a controlled language for
aerospace maintenance documentation, and its power comes from hard limits: one word per meaning,
short sentences, active voice, no idioms. Clean writing is a specification you can follow, not a
mood you have to be in. See [writing.md](writing.md).

**5. Constraints are a dial, not a switch.** The spec is stringent, so you can ask for "80% of
the way to ASD-STE100" — keep the discipline, drop the stiffness. Being able to soften a strict
format is itself a useful prompt primitive.

**6. Name a known style or spec — the model already knows it.** Asking for "ASD-STE100",
"3Blue1Brown style", or "output in HTML" transfers an entire aesthetic and standard in two words,
because the model has seen thousands of examples. Naming is cheaper and higher-fidelity than
describing.

**7. The frontier moves; retry what failed last year.** Video explainers on arbitrary topics
"are actually starting to work". Treat last year's impossibility as this year's default setting,
and spend a slice of your effort on the version that seems too ambitious.

**8. Abundance changes the economics of *discardable* artifacts.** When intelligence and code are
abundant, a large, custom, single-use artifact becomes rational: a bespoke web app or explainer
video for one question, built in an hour and thrown away. These would never have justified
themselves before. The win is not the artifact — it is the understanding you keep and the artifact
you drop. See the discardable rule in [SKILL.md](../SKILL.md).

**9. Do not let credentials be the gate.** A missing key or an absent tool changes the route; ask
for a capable alternative and carry on.

**10. The human is the last consumer. Write for the human.** Every rule above is in service of a
person who has to understand something and then act on it.

## What this repository takes from the post

The post is a four-rung escalation, and its author is most bullish on the last rung: bespoke explainer
videos. This repository implements the first three rungs and applies them to **engineering documents**
— project analysis, evaluation, execution plans, specs, ADRs, runbooks — because those are the
artifacts a person has to approve and work from, and because that is where the failures hurt.

| Rung | In this repository |
|---|---|
| 1. Constrained, cut prose | Implemented, and it carries the value. See [writing.md](writing.md), [conciseness.md](conciseness.md). |
| 2. Diagrams | Implemented, as compression inside a document. See [diagrams.md](diagrams.md). |
| 3. Web pages | Implemented, as the single-file HTML report a document renders into. See [html-report.md](html-report.md). |
| 4. Explainer videos | Out of scope by choice. The source post's argument for it stands, and this repository does not carry the rung. |

Two further departures, both deliberate:

- **Conciseness is first-class here.** The post is about *representation* — which medium carries the
  idea. The sibling failure, a clear document that runs three times too long, is at least as common in
  model output, so [conciseness.md](conciseness.md) sits beside the medium question rather than under
  it.
- **The document shapes are ours.** The post supplies the writing standard. The section skeletons, the
  decision-first summary, and the scope fence come from this repository; they are what make a document
  auditable by a human in a couple of minutes. They build on
  [`to-spec`](https://github.com/mattpocock/skills) (MIT, Matt Pocock), which optimizes a spec for the
  agent consuming it. See [documents.md](documents.md).

## What the original post does not need, and this skill does

Karpathy's tips assume a human expert judging output turn by turn: he sees at a glance whether a
diagram is nonsense. An agent following the same tips needs the guardrails he gets for free from his
own eyes:

- **A verification gate.** Open it, render it, walk the reviewer's first pass. See
  [checklist.md](checklist.md).
- **A budget.** The HTML report costs real wall-clock time to get right. Ask before climbing.
- **A refusal path.** Small questions deserve small answers. A skill that always builds an artifact
  is a worse skill than no skill.
- **Honesty about the artifact.** Numbers need sources, charts need labelled axes, and assumptions
  get labelled as assumptions.
