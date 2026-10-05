#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove that the gates can fail.

The gates make five claims about this repository. A check that cannot fail is decoration,
so this copies the repository into a temporary directory, injects one real fault per
claim, and asserts that `check.py` reports it there. Nothing in the working tree is
written to.

    python tools/selftest.py
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IGNORE = shutil.ignore_patterns(".git", "__pycache__")

# gate, file, text to replace, replacement, what the report must say
FAULTS = [
    (
        "law",
        "skills/documents/easy-plan/references/readability-law.md",
        "Threshold: longest cell \u2264120.",
        "Threshold: longest cell \u2264999.",
        "drifted",
    ),
    (
        "links",
        "README.md",
        "[`tools/README.md`](tools/README.md)",
        "[`tools/README.md`](tools/NOPE.md)",
        "no such file",
    ),
    (
        "links",
        "README.md",
        "[`tools/README.md`](tools/README.md)",
        "[`tools/README.md`](tools/README.md#no-such-heading)",
        "no such heading",
    ),
    (
        "skills",
        "skills/documents/easy-audit/SKILL.md",
        "name: easy-audit",
        "name: easy-auditt",
        "folder is easy-audit",
    ),
]

PROBE = "a-probe-file.md"
PROBE_BODY = (
    "# Probe\n"
    "\n"
    "This single sentence deliberately runs on well past the twenty five word limit that "
    "the law sets, so that the prose gate has something real to catch.\n"
    "\n"
    "| a | b |\n|---|---|\n| " + "x" * 150 + " | " + "y" * 150 + " |\n"
    "\n"
    "R-7\n"
)
PROBE_EXPECTS = ("sentence is", "cell is 150 chars", "code without a name")


def run(check, *gates):
    p = subprocess.run(
        [sys.executable, str(check), *gates],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        cwd=str(check.parent.parent),
    )
    return p.returncode, p.stdout + p.stderr


def main():
    with tempfile.TemporaryDirectory(prefix="easy-check-") as tmp:
        repo = Path(tmp) / "repo"
        shutil.copytree(ROOT, repo, ignore=IGNORE)
        check = repo / "tools" / "check.py"

        code, out = run(check)
        if code != 0:
            print("FAIL  the copied repository does not pass its own gates")
            print(out)
            return 1
        print("PASS  a clean copy passes every gate")

        failures = 0
        for gate, target, old, new, want in FAULTS:
            path = repo / target
            original = path.read_text(encoding="utf-8")
            if old not in original:
                print("FAIL  %-22s pattern not found in %s" % (gate, target))
                failures += 1
                continue
            path.write_text(original.replace(old, new, 1), encoding="utf-8")
            code, out = run(check, gate)
            path.write_text(original, encoding="utf-8")
            ok = code == 1 and want in out
            failures += 0 if ok else 1
            print(
                "%-5s %-9s %-22s exit=%d, saw %s"
                % (
                    "PASS" if ok else "FAIL",
                    gate,
                    target.rsplit("/", 1)[-1],
                    code,
                    repr(want) if want in out else "nothing matching",
                )
            )

        probe = repo / PROBE
        probe.write_text(PROBE_BODY, encoding="utf-8")
        code, out = run(check, "prose")
        probe.unlink()
        for want in PROBE_EXPECTS:
            ok = want in out and code == 1
            failures += 0 if ok else 1
            print("%-5s prose     probe: %s" % ("PASS" if ok else "FAIL", want))

        code, out = run(check)
        if code != 0:
            print("FAIL  the copy no longer passes after the faults were removed")
            failures += 1
        else:
            print("PASS  the copy passes again once the faults are removed")

    print()
    if failures:
        print("%d self-test(s) failed" % failures)
        return 1
    print("every gate caught its fault")
    return 0


if __name__ == "__main__":
    sys.exit(main())
