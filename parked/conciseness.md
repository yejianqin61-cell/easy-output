# Conciseness — the half of readability nobody prompts for

Readability is two things, and prompts usually ask for only one of them:

- **Clarity** — is each sentence easy to parse? (That is [writing.md](writing.md), ASD-STE100.)
- **Conciseness** — does every sentence earn its place?

A document can be perfectly clear and still be unreadable, because there is three times too much
of it. Padding is not neutral: it moves the answer further from the reader, and every extra sentence
is another sentence they must decide to skip.

**The test for every sentence: does this change what the reader knows or does?** If not, delete it.

## Rules

1. **Answer first.** The conclusion goes in the first one or two sentences. Setup, context, and
   reasoning come after — and only as much of them as the conclusion needs. Never build to a
   reveal.
2. **No preamble.** Delete "Great question", "Let me break this down", "It's worth noting that",
   "In today's world", "As you may know", "There are several factors to consider". They carry zero
   information and cost the reader attention.
3. **No restating the question.** The reader knows what they asked.
4. **No recap unless the text is long.** Below ~800 words, a summary section is pure duplication.
5. **One idea per sentence, one topic per paragraph.** This is both clarity and compression: mixed
   sentences have to be read twice.
6. **Prefer structure over prose when enumerating.** Three or more parallel items → a list. Two or
   more items compared on the same attributes → a table. Prose for enumeration is the single most
   common source of bloat.
7. **Cut hedges and intensifiers** unless they carry real probability or magnitude: "very",
   "quite", "really", "basically", "essentially", "somewhat", "arguably", "generally speaking".
   If the caveat matters, state it precisely ("in ~5% of cases" beats "sometimes").
8. **Cut the nominalisations.** "Perform an analysis of" → "analyse". "Is a demonstration of" →
   "shows". Wordiness is usually a noun where a verb belongs.
9. **Do not explain what you are about to do, or what you just did.** The document is not a
   commentary on itself.
10. **Prefer the concrete.** "Latency dropped from 400 ms to 90 ms" beats "performance improved
    significantly" — shorter *and* more informative.
11. **Set a length budget before writing, and honour it.** Vague instructions produce padding.
12. **Delete, don't rewrite, in the edit pass.** Cutting is the reliable move; polishing keeps the
    length.

## Length budgets

Rough targets. Over-running them is a signal, not a crime — but "why is this longer?" must have an
answer. Budgets for the engineering document types — analysis, evaluation, execution plan, spec, ADR,
runbook — live in [documents.md](documents.md).

| Output | Target |
|---|---|
| Direct answer to a factual question | 1–3 sentences |
| Verdict + reasoning for a decision | 150–300 words, or a table |
| Explanation of a mechanism | 300–600 words + one diagram |
| Design rationale / ADR | 400–800 words, one decision, alternatives in a table |
| Section of a longer document | 1 topic, ≤ 6 sentences per paragraph |

## Techniques that cut length without losing content

- **Front-load and stop.** Lead with the answer; if the reasoning is not needed for the reader's
  next action, it is not needed.
- **Move detail into a table or a diagram.** A 5×3 table replaces several paragraphs and is faster
  to scan. This is the main reason diagrams and HTML pages belong to *readability*: they are
  compression devices, not decoration.
- **Put the caveat where it applies**, not in a trailing paragraph. Fewer words, less ambiguity.
- **Name the thing once, then use the name.** Re-explaining a concept on every mention is the most
  common form of bloat in long technical writing.
- **Convert process descriptions into numbered steps.** Verbs instead of nouns, no transitions.
- **Trust the reader.** Assume competence; define terms on first use and move on.

## Anti-patterns

- The wall: 900 words where 150 plus a diagram would be clearer. The most common failure of LLM
  output, and the one this whole skill exists to fix.
- Symmetry padding: a bullet list padded to a fixed count, or three options where two exist.
- The sandwich: caveat, answer, restatement of the caveat.
- A table that repeats prose that already said the same thing.
- "In conclusion" sections in short documents.
- Thoroughness used as a proxy for helpfulness. Exhaustiveness is a cost, not a service.

## Interaction with the ladder

Conciseness is not an argument for a bigger artifact — it is an argument for a **smaller** one.
The correct response to "this is hard to read" is usually: cut a third of it, and possibly replace
two paragraphs with one diagram or one table. That is rung 1 and rung 2. Climbing to rung 3 to solve a
readability problem that deletion would solve is over-building.
