# tools

Dev-only. Nothing here is installed, and no skill ships it.

```bash
python tools/check.py             # every gate
python tools/check.py prose       # one gate: law, links, prose, skills
python tools/check.py --report    # the metric table, one row per file
python tools/check.py law --sync  # re-copy the law into every skill
python tools/selftest.py          # prove the gates can fail
```

`check.py` exits 1 when a gate fails, so it drops straight into CI.

## The gates

| Gate | Fails when |
|---|---|
| `law` | a copy of the law differs from `RULES.md` |
| `links` | a relative link, or the heading it points at, is missing |
| `prose` | a document breaks a countable clause of the law |
| `skills` | a skill cannot be installed |

`discover` is not a gate. It runs the installer and reports what it found, so a broken install shows up
here without failing the build.

## What each gate counts

`law` compares the body of every copy: everything above `## Where it came from`. The closing note is the
one part allowed to differ, because a copy sits inside a skill, and a link out of it would break. The
copies are the five under `skills/documents/`.

`prose` holds the countable clauses. Cells ≤120 characters. Lines ≤200. No strikethrough, no round
marker. Sentences ≤25 words. No nominalisation and no bare code. Bold under one span per line, and
emphasis on under 40% of lines. `parked/` is exempt, being retired material.

Two of those need a word of explanation.

A bold span that opens a line is a label, not emphasis, so `**Goal**: ...` and `- **Symptom**: ...`
cost nothing. Emphasis is a bold span inside the running text, and that is what the 40% covers. The
earlier wording counted line shape, and so failed one document in English and passed it in Chinese.

A code counts as bare when no name follows it on the line. A parenthetical holding only codes is not a
name. Write `(R-1 Lock out after 3 failed logins, R-2 Keep the counter)`, never two codes in brackets. A
table row is exempt, because the row is the name.

Clauses 1, 3, 7, 8 and 10 are absent. They ask about a document's argument, and a script cannot read for
it. The skills check those while they write.

`skills` holds the install contract: a `SKILL.md` whose `name` matches its folder, a description under
1024 characters, and an `agents/openai.yaml`. The expected count lives in `EXPECTED_SKILLS`, and a new
skill has to raise it.

## docmetrics.py

The metric library, and the only file here that knows what a sentence is. It measures what the reader
sees, so a link target takes no space on the page.

The detectors are high-precision rather than complete. Clause 11 asks for zero nominalisations, and the
patterns catch one English shape and one Chinese shape. The rest need a human reading.

## selftest.py

A check that cannot fail is decoration. `selftest.py` copies the repository into a temporary
directory, injects one real fault per gate, and asserts that `check.py` reports it there. The working
tree is never written to. Run it after you change a gate.

## Adding a check

Add the detector to `docmetrics.py`, returning the line number that produced each hit. Then add the
threshold to `check.py`. A check that cannot say where the problem is costs more than it saves.
