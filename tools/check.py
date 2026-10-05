#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The one command for this repo: `python tools/check.py`.

Four gates, each holding one promise the repository makes:

    law      every copy of the readability law matches `RULES.md`
    links    every relative Markdown link resolves, heading included
    prose    every document obeys the countable clauses of the law
    skills   every skill is installable: frontmatter, name, description, picker file

Name a gate to run only that one. `--report` prints the metric table instead of the
verdict, one row per file. The exit code is 1 when any gate fails.

Clauses 1, 3, 7, 8 and 10 are not here. They ask about a document's argument, and a
script cannot read for it. The skills check those while they write.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docmetrics  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
LAW = ROOT / "RULES.md"
DOCUMENT_SKILLS = ROOT / "skills" / "documents"
SKIP_DIRS = {".git", "parked"}

LAW_ANCHOR = "## Where it came from"
MAX_CELL = 120
MAX_LINE = 200
MAX_SENT_WORDS = 25
BOLD_PER_LINE = 1.0
BOLD_LINE_PCT = 40
MAX_DESCRIPTION = 1024
EXPECTED_SKILLS = 7

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
STRIKE = re.compile(r"~~[^~\n]+?~~")
ROUND = re.compile(r"第[一二三四五六七八九十]+轮")


def markdown_files():
    return sorted(
        f for f in ROOT.rglob("*.md") if not (set(f.parts) & SKIP_DIRS)
    )


def rel(path):
    return str(Path(path).relative_to(ROOT)).replace("\\", "/")


def slug(title):
    s = re.sub(r"`|\*|_|~", "", title.strip().lower())
    s = re.sub(r"[^\w\u4e00-\u9fff \-]", "", s)
    return s.replace(" ", "-")


def frontmatter(text):
    """The YAML block's top-level keys, folded lines joined."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    out, key, buf = {}, None, []
    for ln in lines[1:]:
        if ln.strip() == "---":
            if key:
                out[key] = " ".join(buf).strip()
            return out
        if re.match(r"^[A-Za-z_-]+:", ln):
            if key:
                out[key] = " ".join(buf).strip()
            k, _, v = ln.partition(":")
            key, buf = k.strip(), []
            v = v.strip()
            if v and v not in (">-", ">", "|", "|-"):
                buf.append(v)
        elif key is not None:
            buf.append(ln.strip())
    return out or None


# --- gate: law ---------------------------------------------------------------------

def law_body(path):
    """The law without its closing note. The note is the one part allowed to differ."""
    lines = Path(path).read_text(encoding="utf-8").split("\n")
    for n, ln in enumerate(lines):
        if ln.strip() == LAW_ANCHOR:
            return "\n".join(lines[:n]).rstrip()
    return None


def gate_law():
    canonical = law_body(LAW)
    if canonical is None:
        return "fail", ["RULES.md has no `%s` heading" % LAW_ANCHOR], ""
    findings = []
    copies = []
    for skill in sorted(d for d in DOCUMENT_SKILLS.iterdir() if d.is_dir()):
        copy = skill / "references" / "readability-law.md"
        if not copy.exists():
            findings.append(
                "%s carries no references/readability-law.md" % rel(skill)
            )
            continue
        copies.append(copy)
        if law_body(copy) != canonical:
            findings.append("%s drifted from RULES.md" % rel(copy))
    if findings:
        findings.append("fix with: python tools/check.py law --sync")
    summary = "%d copies match RULES.md" % (len(copies) + 1)
    return ("ok" if not findings else "fail"), findings, summary


def sync_law():
    """Write the canonical law body into every copy, keeping each one's closing note."""
    canonical = law_body(LAW)
    text = LAW.read_text(encoding="utf-8")
    if canonical is None or LAW_ANCHOR not in text:
        print("RULES.md has no `%s` heading" % LAW_ANCHOR)
        return 2
    if canonical + "\n\n" + LAW_ANCHOR + text.split(LAW_ANCHOR, 1)[1] != text:
        print("refusing to sync: the body and the note do not rebuild RULES.md exactly")
        return 2

    changed, failed = [], []
    for skill in sorted(d for d in DOCUMENT_SKILLS.iterdir() if d.is_dir()):
        copy = skill / "references" / "readability-law.md"
        if not copy.exists():
            failed.append("%s carries no references/readability-law.md" % rel(skill))
            continue
        old = copy.read_text(encoding="utf-8")
        if LAW_ANCHOR not in old:
            failed.append("%s has no `%s` heading" % (rel(copy), LAW_ANCHOR))
            continue
        rebuilt = canonical + "\n\n" + LAW_ANCHOR + old.split(LAW_ANCHOR, 1)[1]
        if rebuilt != old:
            copy.write_text(rebuilt, encoding="utf-8", newline="\n")
            changed.append(rel(copy))

    for name in changed:
        print("synced %s" % name)
    for name in failed:
        print("cannot sync %s" % name)
    if not changed and not failed:
        print("every copy already matches RULES.md")
    return 1 if failed else 0


# --- gate: links -------------------------------------------------------------------

def gate_links():
    files = markdown_files()
    anchors = {}
    for f in files:
        found = set()
        for line in f.read_text(encoding="utf-8").split("\n"):
            if line.startswith("#"):
                found.add(slug(line.lstrip("#").strip()))
        anchors[f.resolve()] = found

    findings, relative, external = [], 0, 0
    for f in files:
        for target in LINK.findall(f.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                external += 1
                continue
            relative += 1
            path, _, anchor = target.partition("#")
            if not path:
                continue
            dest = (f.parent / path).resolve()
            if not dest.exists():
                findings.append("%s -> %s (no such file)" % (rel(f), target))
            elif anchor and dest.suffix == ".md" and anchor.lower() not in anchors.get(dest, set()):
                findings.append("%s -> %s (no such heading)" % (rel(f), target))
    summary = "%d relative links resolve, %d external" % (relative, external)
    return ("ok" if not findings else "fail"), findings, summary


# --- gate: prose -------------------------------------------------------------------

def gate_prose():
    findings = []
    for f in markdown_files():
        name = rel(f)
        text = f.read_text(encoding="utf-8")
        lines = text.split("\n")
        vis = docmetrics.visible(text).split("\n")
        m = docmetrics.scan(f)

        for n, cell in docmetrics.table_cells(vis):
            if len(cell) > MAX_CELL:
                findings.append(
                    "%s:%d cell is %d chars (max %d): %s"
                    % (name, n, len(cell), MAX_CELL, cell[:60])
                )
        for n, ln in enumerate(vis, 1):
            if len(ln) > MAX_LINE:
                findings.append(
                    "%s:%d line is %d chars (max %d)" % (name, n, len(ln), MAX_LINE)
                )
            if STRIKE.search(ln):
                findings.append("%s:%d carries a strikethrough" % (name, n))
            if ROUND.search(ln):
                findings.append("%s:%d keeps a round marker" % (name, n))
        for n, words, sentence in docmetrics.long_sentences(vis, MAX_SENT_WORDS):
            findings.append(
                "%s:%d sentence is %d words (max %d): %s"
                % (name, n, words, MAX_SENT_WORDS, sentence[:60])
            )
        for n, hit in docmetrics.nominalisations(vis):
            findings.append("%s:%d nominalisation: %s" % (name, n, hit))
        for n, code, line in docmetrics.bare_codes(vis):
            findings.append("%s:%d code without a name: %s" % (name, n, line))
        if m["bold_per_line"] > BOLD_PER_LINE:
            findings.append(
                "%s carries %.2f bold spans per line (max %.1f)"
                % (name, m["bold_per_line"], BOLD_PER_LINE)
            )
        if m["bold_emphasis_pct"] > BOLD_LINE_PCT:
            findings.append(
                "%s puts emphasis on %.1f%% of lines (max %d%%)"
                % (name, m["bold_emphasis_pct"], BOLD_LINE_PCT)
            )
    summary = "%d documents pass every countable clause" % len(markdown_files())
    return ("ok" if not findings else "fail"), findings, summary


# --- gate: skills ------------------------------------------------------------------

def gate_skills():
    findings = []
    skills = sorted(ROOT.glob("skills/*/*"))
    count = 0
    for d in skills:
        if not d.is_dir():
            continue
        skill_md = d / "SKILL.md"
        if not skill_md.exists():
            findings.append("%s has no SKILL.md" % rel(d))
            continue
        count += 1
        fm = frontmatter(skill_md.read_text(encoding="utf-8"))
        if not fm:
            findings.append("%s has no frontmatter" % rel(skill_md))
            continue
        if fm.get("name") != d.name:
            findings.append(
                "%s says name: %s, folder is %s" % (rel(skill_md), fm.get("name"), d.name)
            )
        desc = fm.get("description", "")
        if not desc:
            findings.append("%s has no description" % rel(skill_md))
        elif len(desc) > MAX_DESCRIPTION:
            findings.append(
                "%s description is %d chars (max %d)"
                % (rel(skill_md), len(desc), MAX_DESCRIPTION)
            )
        picker = d / "agents" / "openai.yaml"
        if not picker.exists():
            findings.append("%s has no agents/openai.yaml" % rel(d))
        else:
            y = picker.read_text(encoding="utf-8")
            for key in ("display_name", "short_description"):
                if key not in y:
                    findings.append("%s has no %s" % (rel(picker), key))
    if count != EXPECTED_SKILLS:
        findings.append(
            "%d skills found, EXPECTED_SKILLS is %d" % (count, EXPECTED_SKILLS)
        )
    summary = "%d skills installable" % count
    return ("ok" if not findings else "fail"), findings, summary


def discover():
    """Optional: confirm the installer finds the same skills. Never fails the build."""
    npx = shutil.which("npx") or shutil.which("npx.cmd")
    if not npx:
        return "skipped, npx is not on PATH"
    try:
        out = subprocess.run(
            [npx, "skills", "add", ".", "--list"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=180,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return "skipped, %s" % exc
    if out.returncode != 0:
        return "skipped, the installer exited %d" % out.returncode
    expected = {
        d.name for d in ROOT.glob("skills/*/*") if (d / "SKILL.md").exists()
    }
    found = set(re.findall(r"\b(easy-[a-z-]+)\b", out.stdout or ""))
    missing = expected - found
    if missing:
        return "installer missed %s" % ", ".join(sorted(missing))
    extra = {n for n in found - expected if n not in str(ROOT)}
    tail = " (also prints %s)" % ", ".join(sorted(extra)) if extra else ""
    return "installer sees all %d skills%s" % (len(expected), tail)


# --- report ------------------------------------------------------------------------

REPORT_KEYS = [
    ("lines", "lines"),
    ("non_empty", "non-empty"),
    ("cells", "cells"),
    ("max_cell", "max cell"),
    ("cells_over_40", "cells >40"),
    ("bold", "bold"),
    ("bold_per_line", "bold/line"),
    ("bold_line_pct", "bold lines %"),
    ("bold_emphasis_pct", "emphasis %"),
    ("lines_over_200", "lines >200"),
    ("longest_sent", "longest sent"),
    ("sent_over_25w", "sent >25w"),
    ("nominalisations", "nominal."),
    ("bare_codes", "bare codes"),
    ("strike", "strike"),
]


def report():
    files = markdown_files()
    rows = [docmetrics.scan(f) for f in files]
    name_w = max(len(rel(f)) for f in files) + 2
    head = "%-*s" % (name_w, "file") + "".join(
        "%12s" % label for _, label in REPORT_KEYS
    )
    print(head)
    print("-" * len(head))
    for f, r in zip(files, rows):
        print("%-*s" % (name_w, rel(f)) + "".join("%12s" % r[k] for k, _ in REPORT_KEYS))
    print()
    print("%d files" % len(rows))


# --- entry -------------------------------------------------------------------------

GATES = {
    "law": gate_law,
    "links": gate_links,
    "prose": gate_prose,
    "skills": gate_skills,
}


def main():
    args = sys.argv[1:]
    if "--report" in args:
        report()
        return 0
    if "--sync" in args:
        return sync_law()

    names = [a for a in args if not a.startswith("--")] or list(GATES)
    unknown = [a for a in names if a not in GATES]
    if unknown:
        print("unknown gate: %s" % ", ".join(unknown))
        print("gates: %s" % ", ".join(GATES))
        return 2

    failed = 0
    for name in names:
        status, findings, summary = GATES[name]()
        if status == "fail":
            failed += 1
        print("%-8s %-5s %s" % (name, status, summary))
        for finding in findings[:40]:
            print("         %s" % finding)
        if len(findings) > 40:
            print("         ... and %d more" % (len(findings) - 40))

    if "skills" in names:
        print("%-8s %-5s %s" % ("discover", "note", discover()))

    print()
    if failed:
        print("%d gate(s) failed" % failed)
        return 1
    print("all gates pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
