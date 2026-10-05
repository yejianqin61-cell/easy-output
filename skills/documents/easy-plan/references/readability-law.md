# The readability law

Andrej Karpathy's point, compressed: **we will spend far more of our time reading what a language model
produced than writing prompts for it.** A document earns that time when it is short enough to finish.
It earns it when it is clear enough to act on.

Write for a person who reads the document **once**, in the language they are using.

Every clause carries a threshold, so a reviewer can count instead of argue.

## The law

1. **Land the verdict in the first screen.** Verdict, cost, next action, within the first ≤150 words.
   Threshold: the verdict appears within the first 15% of the document.
2. **Write the present state.** Date and version in the header, changes in a changelog at the end.
   Threshold: 0 strikethroughs and 0 round markers in the body.
3. **Give each fact one home.** Every other mention cites its ID. Threshold: 0 items stated twice.
4. **Keep cells short.** One fact, ≤40 characters, when the reader scans the cell for a value. A cell that
   names an item, or that lists a vocabulary, may run longer. Threshold: longest cell ≤120.
5. **Spend emphasis on the few things that decide the page.** One bold span per paragraph, none inside a
   cell. A bold span that opens a line is a label, not emphasis. Threshold: ≤1.0 bold spans per line;
   ≤40% of lines carrying emphasis inside the line.
6. **Give each idea its own line.** Threshold: 0 lines over 200 characters.
7. **Pair every reference with a sentence that stands alone.** Threshold: 0 citation-only fields.
8. **Let each section stand alone.** Threshold: 0 references needed to finish a sentence.
9. **Choose one word per meaning, and the common one.** Declare the vocabulary once, in the reader's
   language, and use those words from then on. Prefer the word the reader already knows: `use` over
   `utilise`, 锁定 over 封禁. Dates in `YYYY-MM-DD`. Threshold: 0 synonyms for a declared status word.
10. **State the criterion beside the judgement.** Every softened obligation, and every "blocking", traces
    to one.
11. **Keep sentences short, and let verbs do the work.** One idea per sentence, active voice, the
    condition before its action. 20 words in a step, 25 in an explanation; "should" becomes "must" or
    leaves. Where the document is not in English, keep the shape of this clause and drop the word
    counts. Threshold: 0 sentences over 25 words; 0 nominalisations where a verb exists.
12. **Let every code travel with its name.** `R-3 计数保留`, `Phase 2 管理员能解锁`. The first mention
    teaches it, and every later mention repeats it. In a table whose first column is the code, the row
    itself is the name; a parenthetical holding only codes is not a name. Threshold: 0 codes outside a
    table row that appear without a name on the line.

## The edit pass

Verdict up. Trail out. Bold down to one per paragraph. Cells down to one fact. Sentences split at 25
words. Every code given its name. Every reference read with its target file closed.

## Where it came from

Andrej Karpathy, 2 October 2026, on making model output easier to understand:
<https://x.com/karpathy/status/2105819303471976479>. The post is quoted in full in the repository's
`parked/spirit.md`.
