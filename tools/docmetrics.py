# -*- coding: utf-8 -*-
"""Countable readability metrics for Markdown, one per clause of `RULES.md`.

This is a library. `tools/check.py` is the command.

Every function that reports a problem returns the line number that produced it, so a
failure can be fixed without a search.

The detectors are high-precision rather than complete. Clause 11 asks for "0
nominalisations where a verb exists"; the patterns below catch one English shape and one
Chinese shape and miss the rest. A human reading is still the only full test.
"""
import re
from pathlib import Path

CJK = re.compile(r"[\u4e00-\u9fff]")
WORD = re.compile(r"[A-Za-z0-9_`'\-]+")
SENT_END = re.compile(r"(?<=[.!?。！？])\s+")
LIST_START = re.compile(r"^(?:[-*+]|\d+\.)\s")
EMPHASIS = re.compile(r"\*\*|`")
BOLD = re.compile(r"\*\*[^\n]+?\*\*")

# Clause 2. History kept in the body instead of in a changelog.
HISTORY = {
    "strikethrough": r"~~[^~\n]+?~~",
    "round-number": r"第[一二三四五六七八九十]+轮",
    "recheck/amend": r"复检|修正",
    "previous-round": r"上一轮|上一版|上轮",
    "closed-by-ruling": r"已解除|已裁决|已关闭",
}

# Clause 11. A light verb in front of a deverbal noun, in both languages. The Chinese
# lookahead drops `进行中` ("in progress"), which is a status word rather than a light
# verb. `实施` and `加以` are absent because they match compounds such as `实施方案`.
NOM_EN = re.compile(
    r"\b(?:perform|conduct|carry out|make|provide|give|do|take)\s+(?:an?|the)?\s*"
    r"\w{4,}(?:tion|sion|ment|ance|ence)\b",
    re.I,
)
NOM_ZH = re.compile(r"(?:进行|开展|作出)(?![中时着完了])(?=[\u4e00-\u9fff])")

# Clause 12. A code is named when a word follows it on the same line: `R-3 Keep the
# counter`. Table rows are exempt, because the row is the name.
CODE = re.compile(r"(?:[A-Z]{1,4}-\d+|Phase \d+|rung \d+)")
PAREN = re.compile(r"[（(][^（()）]*[)）]")
NAMED = re.compile(r"^\s*[:—–\-←→]*\s*[\w\u4e00-\u9fff]")
# A connective is not a name. `R-1 and R-2 is met` names neither code.
CONNECTIVE = re.compile(
    r"^\s*[:—–\-←→]*\s*(?:and|or|then|also|plus|is|are|was|were|be|been|"
    r"will|would|can|could|should|must|has|have|had)\b",
    re.I,
)
CELL_SPLIT = re.compile(r"(?<!\\)\|")

VERDICT = re.compile(r"结论|判定|建议|决定|推荐")


def visible(text):
    """The page as the reader sees it: a link target takes no space."""
    return re.sub(r"\]\([^)\s]*\)", "]", text)


def prose_blocks(lines):
    """Group prose lines into paragraphs, as `[(lineno, text)]`.

    Frontmatter, tables, headings, HTML comments and code fences are not prose.
    """
    blocks, cur, start, fence = [], [], 0, False
    i = 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        i += 1

    def flush():
        nonlocal start
        if cur:
            blocks.append((start, " ".join(cur)))
            cur.clear()
        start = 0

    for n in range(i, len(lines)):
        s = lines[n].strip()
        if s.startswith("```"):
            fence = not fence
            flush()
            continue
        if fence or not s or s.startswith(("|", "#", "<!--")):
            flush()
            continue
        s = re.sub(r"^>\s?", "", s)
        if LIST_START.match(s):
            flush()
        if not cur:
            start = n + 1
        cur.append(s)
    flush()
    return blocks


def split_sentences(text):
    """Sentences in one block, with emphasis and code markers removed."""
    out = []
    for s in SENT_END.split(EMPHASIS.sub("", text)):
        s = s.strip()
        if s:
            out.append(s)
    return out


def sentences(lines):
    """Every prose sentence in the file, as `[(lineno, sentence)]`."""
    return [
        (n, s) for n, block in prose_blocks(lines) for s in split_sentences(block)
    ]


def is_english(sentence):
    """Clause 11 drops its word counts for a document that is not in English."""
    return len(WORD.findall(sentence)) > len(CJK.findall(sentence))


def table_cells(lines):
    """Every table cell as `[(lineno, text)]`. Separator rows are skipped.

    A pipe escaped as `\\|` stays inside its cell.
    """
    out = []
    for n, ln in enumerate(lines, 1):
        s = ln.strip()
        if not s.startswith("|"):
            continue
        parts = [c.strip() for c in CELL_SPLIT.split(s.strip("|"))]
        if all(set(c) <= set("-: ") for c in parts):
            continue
        out.extend((n, c) for c in parts)
    return out


def nominalisations(lines):
    """Clause 11, as `[(lineno, hit)]`."""
    out = []
    for n, ln in enumerate(lines, 1):
        out.extend((n, m.group(0)) for m in NOM_EN.finditer(ln))
        out.extend((n, m.group(0)) for m in NOM_ZH.finditer(ln))
    return out


def bare_codes(lines):
    """Codes that never get a name, as `[(lineno, code, line)]`.

    Table rows are exempt, because the row is the name. A parenthetical holding only
    codes is not: `(R-1, R-2)` names neither code, and it is the exact shape a reader
    cannot hold, two identifiers and no way to tell them apart.
    """
    hits = []
    for n, ln in enumerate(lines, 1):
        s = ln.strip()
        if s.startswith("|"):
            continue
        for m in CODE.finditer(s):
            rest = s[m.end():]
            if NAMED.match(rest) and not CONNECTIVE.match(rest):
                continue
            hits.append((n, m.group(0), s[:70]))
    return hits


def history_markers(text):
    """Clause 2. Anything that keeps the past in the body instead of a changelog."""
    return {k: len(re.findall(v, text, re.M)) for k, v in HISTORY.items()}


LIST_PREFIX = re.compile(r"^\s*(?:[-*+]|\d+\.)\s*")


def content_start(line):
    """Offset of the first character the reader sees, past any list marker."""
    m = LIST_PREFIX.match(line)
    return m.end() if m else len(line) - len(line.lstrip())


def is_label(line):
    """Clause 5. One bold span, opening the line, names the field.

    `**Goal**: ...` and `- **Symptom**: ...` are structure. A bold span inside the
    running text is emphasis, and emphasis is what the clause spends.
    """
    spans = list(BOLD.finditer(line))
    return len(spans) == 1 and spans[0].start() == content_start(line)


def bold_stats(lines):
    """Clause 5. The ratio counts emphasis, because a label is not emphasis."""
    non_empty = [ln for ln in lines if ln.strip()]
    spans = sum(len(BOLD.findall(ln)) for ln in non_empty)
    bold_lines = [ln for ln in non_empty if BOLD.search(ln)]
    emphasis = [ln for ln in bold_lines if not is_label(ln)]
    return {
        "bold": spans,
        "bold_per_line": round(spans / max(len(non_empty), 1), 2),
        "bold_line_pct": round(100 * len(bold_lines) / max(len(non_empty), 1), 1),
        "bold_emphasis_pct": round(100 * len(emphasis) / max(len(non_empty), 1), 1),
    }


def long_sentences(lines, limit=25):
    """Clause 11, English only, as `[(lineno, words, sentence)]`."""
    out = []
    for n, s in sentences(lines):
        words = len(WORD.findall(s))
        if is_english(s) and words > limit:
            out.append((n, words, s))
    return out


def scan(path):
    """Every countable metric for one file, as a dict."""
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    lines = visible(text).split("\n")
    raw = text.split("\n")
    non_empty = [ln for ln in lines if ln.strip()]

    cells = table_cells(lines)
    cell_lens = sorted((len(c) for _, c in cells), reverse=True)
    bold = bold_stats(lines)

    sents = sentences(lines)
    english = [s for _, s in sents if is_english(s)]
    chinese = [s for _, s in sents if not is_english(s)]
    sent_words = [len(WORD.findall(s)) for s in english]

    verdict_line = None
    for n, ln in enumerate(lines, 1):
        if VERDICT.search(ln) and not ln.lstrip().startswith("#"):
            verdict_line = n
            break

    return {
        "file": p.name,
        "path": str(p),
        "lines": len(lines),
        "non_empty": len(non_empty),
        "headings": sum(1 for ln in lines if ln.lstrip().startswith("#")),
        "table_rows": len({n for n, _ in cells}),
        "cells": len(cells),
        "bold": bold["bold"],
        "bold_per_line": bold["bold_per_line"],
        "bold_line_pct": bold["bold_line_pct"],
        "bold_emphasis_pct": bold["bold_emphasis_pct"],
        "strike": len(re.findall(HISTORY["strikethrough"], text)),
        "round_markers": len(re.findall(HISTORY["round-number"], text)),
        "max_line": max((len(ln) for ln in lines), default=0),
        "max_line_raw": max((len(ln) for ln in raw), default=0),
        "lines_over_200": sum(1 for ln in lines if len(ln) > 200),
        "max_cell": cell_lens[0] if cell_lens else 0,
        "cells_over_40": sum(1 for c in cell_lens if c > 40),
        "cells_over_120": sum(1 for c in cell_lens if c > 120),
        "cell_mean": round(sum(cell_lens) / max(len(cell_lens), 1), 1),
        "sentences": len(sents),
        "sent_en": len(english),
        "longest_sent": max(sent_words, default=0),
        "sent_over_25w": sum(1 for w in sent_words if w > 25),
        "longest_sent_cjk": max((len(CJK.findall(s)) for s in chinese), default=0),
        "nominalisations": len(nominalisations(lines)),
        "bare_codes": len(bare_codes(lines)),
        "verdict_line": verdict_line,
        "verdict_pct": round(100 * (verdict_line or len(lines)) / max(len(lines), 1), 1),
        "history": history_markers(text),
    }
