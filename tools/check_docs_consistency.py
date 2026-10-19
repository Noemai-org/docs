#!/usr/bin/env python3
"""Keep the Source of Truth, the open-decisions register and the decision records in agreement.

Usage (from the repository root):
    python3 tools/check_docs_consistency.py --check   # default; exits non-zero on any failure
    python3 tools/check_docs_consistency.py --write   # regenerates the canonical register section from SoT §46

Standard library only. Every failure is printed on one line.
"""
import argparse
import hashlib
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOT = "docs/NOEMA_SOURCE_OF_TRUTH.md"
REGISTER = "docs/open-decisions.md"
DECISIONS = "docs/decisions"
FROZEN_LIST = "tools/frozen-files.sha256"
FROZEN_SOURCE_DIR = "docs/poc/tushe/source/"
README = "README.md"

BEGIN = ("<!-- BEGIN GENERATED: canonical-open-decisions (source: docs/NOEMA_SOURCE_OF_TRUTH.md §46). "
         "Do not edit by hand. Run: python3 tools/check_docs_consistency.py --write -->")
END = "<!-- END GENERATED: canonical-open-decisions -->"

# The retired GitHub organisation. Built from parts so this file does not contain it (DEC-2026-10-16 E1).
RETIRED_ORG_URL = "github.com/" + "noema" + "-org"

# `docs` holds documents, not product code (DEC-2026-10-16 E7). Exempt: the archive and this repository's own checkers.
ARCHIVE_DIR = "docs/archive/"
NO_CODE_DIRS = ("contracts/", "packs/")
CODE_EXTENSIONS = {
    ".py", ".go", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".rs", ".java", ".kt", ".rb", ".php",
    ".c", ".cc", ".cpp", ".h", ".cs", ".swift", ".sh", ".sql",
}
OWN_CHECKERS = {
    "tools/check_docs_consistency.py", "tools/perd_index.py", "tools/plan_index.py",
    "tools/test_check_docs_consistency.py", "tools/test_plan_index.py",
}

# Built from parts so this file does not itself contain the misspelling it looks for.
OLD_SPELLING = "tu" + "che"

REQUIRED_RECORD_FIELDS = [
    "Status", "Date", "Owner", "Decision", "Rationale and evidence",
    "Affected requirement IDs / SoT sections", "Migration notes", "Supersedes",
]

# Files that state the current SoT version, and the patterns that state it.
VERSION_FILES = [
    "README.md", "AGENTS.md", "CLAUDE.md", "docs/README.md", "docs/requirements-index.md",
    "docs/open-decisions.md", "docs/engineering/boundary-map.md", "docs/engineering/state-registry.md",
    "docs/poc/README.md", "docs/poc/tushe/README.md", "docs/decisions/README.md",
]
VERSION_PATTERNS = [
    r"\(v(\d+\.\d+), \d{1,2} \w+ \d{4}\)",          # (v1.3, 9 October 2026)
    r"\*\*SoT\*\*, v(\d+\.\d+)",                       # (the **SoT**, v1.3, ...)
    r"Generated from SoT v(\d+\.\d+)",                 # requirement index header
    r"current SoT version: v(\d+\.\d+)",
]


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def write(path, text):
    with open(os.path.join(ROOT, path), "w", encoding="utf-8") as fh:
        fh.write(text)


def cells(row):
    """Split a Markdown table row into stripped cells, honouring escaped pipes."""
    parts = re.split(r"(?<!\\)\|", row.strip())
    return [p.strip() for p in parts[1:-1]]


# ---------------------------------------------------------------- SoT parsing

def section(text, heading_re, next_heading_re=r"^## "):
    m = re.search(heading_re, text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    n = re.search(next_heading_re, rest, re.M)
    return rest[: n.start()] if n else rest


def sot_open_decisions(sot):
    """Rows of §46 keyed by ID, in document order: (id, decision, default, decide_by)."""
    body = section(sot, r"^## 46\. Open decisions.*$")
    rows = []
    for line in body.splitlines():
        m = re.match(r"^\| (OD-\d+) \|", line)
        if m:
            c = cells(line)
            if len(c) < 4:
                rows.append((m.group(1), None, None, None))
            else:
                rows.append((c[0], c[1], c[2], c[3]))
    return rows


def od_status(default, decide_by):
    if decide_by.strip().lower() == "closed":
        return "Closed"
    if "**DECIDED" in default:
        return "DECIDED"
    return "OPEN"


# ------------------------------------------------------------ decision records

def decision_records():
    """{filename: (text, fields dict, closes set)} for every record except README.md."""
    out = {}
    folder = os.path.join(ROOT, DECISIONS)
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md") or name == "README.md":
            continue
        text = read(f"{DECISIONS}/{name}")
        fields = {}
        for line in text.splitlines():
            m = re.match(r"^- ([A-Za-z][A-Za-z /]*?):(.*)$", line)
            if m:
                fields.setdefault(m.group(1).strip(), m.group(2).strip())
        closes = set()
        for key in ("Closes", "Decides"):
            if key in fields:
                closes |= set(re.findall(r"\bOD-\d+\b", fields[key]))
        out[name] = (text, fields, closes)
    return out


# ------------------------------------------------------------ register section

def generate_register(sot, records):
    lines = [
        "| ID | Decision | Default or decision (SoT §46) | Decide by | Status | Record |",
        "|---|---|---|---|---|---|",
    ]
    for od, decision, default, decide_by in sot_open_decisions(sot):
        if decision is None:
            continue
        recs = [n[:-3] for n, (_, _, closes) in records.items() if od in closes]
        rec = ", ".join(f"[{r}](decisions/{r}.md)" for r in recs) if recs else "—"
        lines.append(f"| {od} | {decision} | {default} | {decide_by} | {od_status(default, decide_by)} | {rec} |")
    return BEGIN + "\n" + "\n".join(lines) + "\n" + END


def current_register_block(register):
    i, j = register.find(BEGIN), register.find(END)
    if i < 0 or j < 0 or j < i:
        return None
    return register[i: j + len(END)]


# ------------------------------------------------------------------ the checks

def tracked_files():
    """Every file in the working tree: tracked plus untracked, honouring .gitignore.

    The name is kept for the callers; scanning only tracked files let an untracked file with the
    old spelling pass locally and fail nowhere, so the scan covers the working tree.
    """
    try:
        res = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                             cwd=ROOT, capture_output=True, text=True, check=True)
        files = sorted({l for l in res.stdout.splitlines() if l})
        return [f for f in files if os.path.isfile(os.path.join(ROOT, f))]
    except (OSError, subprocess.CalledProcessError):
        out = []
        for dp, dn, fn in os.walk(ROOT):
            dn[:] = [d for d in dn if d != ".git"]
            for f in fn:
                out.append(os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/"))
        return out


def frozen_listed():
    """{path: sha256} from the frozen-files list; empty if the list is missing."""
    listed = {}
    if os.path.exists(os.path.join(ROOT, FROZEN_LIST)):
        for line in read(FROZEN_LIST).splitlines():
            if line.strip() and not line.startswith("#"):
                digest, path = line.split(None, 1)
                listed[path.strip()] = digest
    return listed


def check_spelling(fail):
    """The old spelling of Tushe may not appear in any working-tree file or path.

    Exempt: paths on the frozen-files list and the partner's own source documents.
    """
    frozen = set(frozen_listed())
    for path in tracked_files():
        if path.startswith(FROZEN_SOURCE_DIR) or path in frozen:
            continue
        if OLD_SPELLING in path.lower():
            fail(f"{path}: path contains the old spelling of Tushe")
            continue
        try:
            text = read(path)
        except (UnicodeDecodeError, OSError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if OLD_SPELLING in line.lower():
                fail(f"{path}:{n}: old spelling of Tushe")


def check_no_code(fail):
    """No contracts/, packs/ or source code in this repository, except the archive and the checkers' own files."""
    for path in tracked_files():
        if path.startswith(ARCHIVE_DIR) or path in OWN_CHECKERS:
            continue
        if path.startswith(NO_CODE_DIRS):
            fail(f"{path}: contracts/ and packs/ belong in the noema repository, not in docs (DEC-2026-10-16 E7)")
        elif os.path.splitext(path)[1].lower() in CODE_EXTENSIONS:
            fail(f"{path}: source code belongs in the noema repository, not in docs (DEC-2026-10-16 E7)")


def check_links_to_retired_org(fail):
    """No URL may point to the retired organisation, except inside frozen records."""
    frozen = set(frozen_listed())
    for path in tracked_files():
        if path.startswith(FROZEN_SOURCE_DIR) or path in frozen:
            continue
        try:
            text = read(path)
        except (UnicodeDecodeError, OSError):
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if RETIRED_ORG_URL in line.lower():
                fail(f"{path}:{n}: link to the retired organisation (use github.com/Noemai-org/...)")


def check(fail):
    sot = read(SOT)
    register = read(REGISTER)
    records = decision_records()
    sot_rows = sot_open_decisions(sot)

    # 1. Register equals SoT
    for od, decision, *_ in sot_rows:
        if decision is None:
            fail(f"SoT §46: row {od} does not have four cells")
    block = current_register_block(register)
    if block is None:
        fail(f"{REGISTER}: generated-section markers missing")
    elif block != generate_register(sot, records):
        fail(f"{REGISTER}: canonical section differs from SoT §46 and docs/decisions/ (run --write)")
    if block is not None:
        outside = register.replace(block, "")
        for m in re.finditer(r"^\| (OD-\d+) \|", outside, re.M):
            fail(f"{REGISTER}: canonical row {m.group(1)} found outside the generated section")

    # 2. Decision records agree with the SoT
    status = {od: od_status(d, b) for od, dec, d, b in sot_rows if dec is not None}
    changelog = section(sot, r"^## Appendix D.*$", r"^## |\Z")
    all_closed_by_records = set().union(*(c for _, _, c in records.values())) if records else set()
    for od, st in status.items():
        if st in ("DECIDED", "Closed") and od not in all_closed_by_records and od not in changelog:
            fail(f"{od} is {st} in SoT §46 but no decision record (Closes/Decides) or change-log entry names it")
    for name, (_, _, closes) in records.items():
        for od in sorted(closes):
            if od not in status:
                fail(f"{DECISIONS}/{name}: closes {od}, which is not in SoT §46")
            elif status[od] == "OPEN":
                fail(f"{DECISIONS}/{name}: closes {od}, but SoT §46 shows it as OPEN")

    # 3. Decision records are complete
    for name, (_, fields, _) in records.items():
        for f in REQUIRED_RECORD_FIELDS:
            if f not in fields:
                fail(f"{DECISIONS}/{name}: missing field '{f}'")
        if "Closes" not in fields and "Decides" not in fields:
            fail(f"{DECISIONS}/{name}: missing field 'Closes' or 'Decides'")

    # 4. IDs contiguous and unique; Appendix B ranges match
    series = {
        "BD": re.findall(r"^\| BD-(\d+) \|", sot, re.M),
        "INV": re.findall(r"^\| INV-(\d+) \|", sot, re.M),
        "AGENT": re.findall(r"^\| AGENT-(\d+) \|", sot, re.M),
        "OD": re.findall(r"^\| OD-(\d+) \|", section(sot, r"^## 46\. Open decisions.*$"), re.M),
        "US": re.findall(r"^\*\*US-(\d+) ", sot, re.M),
    }
    appendix_b = section(sot, r"^## Appendix B.*$")
    for prefix, found in series.items():
        nums = [int(n) for n in found]
        if not nums:
            fail(f"SoT: no {prefix} IDs found")
            continue
        if sorted(nums) != list(range(1, max(nums) + 1)) or len(nums) != len(set(nums)):
            fail(f"SoT: {prefix} IDs are not contiguous and unique from 1 (found {sorted(nums)})")
        width = len(found[0])
        expected = f"{prefix}-{1:0{width}d} to {prefix}-{max(nums):0{width}d}"
        if expected not in appendix_b:
            fail(f"SoT Appendix B: expected range '{expected}'")

    # 5. Version consistency
    m = re.search(r"^Version (\d+\.\d+) · ", sot, re.M)
    sot_version = m.group(1) if m else None
    if not sot_version:
        fail("SoT: version line not found")
    top = re.search(r"^\| (\d+\.\d+) \|", changelog, re.M)
    if not top or top.group(1) != sot_version:
        fail(f"SoT Appendix D: top entry {top.group(1) if top else 'missing'} does not match version {sot_version}")
    readme_versions = re.findall(VERSION_PATTERNS[0], read(README))
    if sot_version not in readme_versions:
        fail(f"{README}: does not state SoT v{sot_version}")
    for path in VERSION_FILES:
        if not os.path.exists(os.path.join(ROOT, path)):
            continue
        text = read(path)
        for pat in VERSION_PATTERNS:
            for v in re.findall(pat, text):
                if v != sot_version:
                    fail(f"{path}: states SoT v{v}, but the SoT is v{sot_version}")

    # 6. Spelling
    check_spelling(fail)

    # 6b. No links to the retired organisation
    check_links_to_retired_org(fail)

    # 6c. No contracts, packs or product code
    check_no_code(fail)

    # 7. Relative Markdown links resolve
    md = [p for p in tracked_files() if p.endswith(".md") and (p.startswith("docs/") or p in ("README.md", "AGENTS.md", "CLAUDE.md"))]
    for path in md:
        text = read(path)
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in re.findall(r"\]\(([^)\s]+)\)", text):
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                continue
            file_part = target.split("#", 1)[0]
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), file_part))
            if not os.path.exists(os.path.join(ROOT, resolved)):
                fail(f"{path}: broken link to {target}")

    # 8. Frozen files unchanged
    if not os.path.exists(os.path.join(ROOT, FROZEN_LIST)):
        fail(f"{FROZEN_LIST}: missing")
    else:
        listed = frozen_listed()
        required = ["docs/poc/tushe/Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md"]
        required += [p for p in tracked_files() if p.startswith(FROZEN_SOURCE_DIR)]
        for path in required:
            if path not in listed:
                fail(f"{FROZEN_LIST}: no hash recorded for frozen file {path}")
        for path, digest in listed.items():
            full = os.path.join(ROOT, path)
            if not os.path.exists(full):
                fail(f"{path}: frozen file missing")
                continue
            with open(full, "rb") as fh:
                actual = hashlib.sha256(fh.read()).hexdigest()
            if actual != digest:
                fail(f"{path}: frozen file changed (sha256 {actual}, recorded {digest})")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="verify consistency (default)")
    mode.add_argument("--write", action="store_true", help="regenerate the canonical register section from SoT §46")
    args = ap.parse_args()

    if args.write:
        register = read(REGISTER)
        block = current_register_block(register)
        if block is None:
            print(f"{REGISTER}: generated-section markers missing; add them first", file=sys.stderr)
            return 1
        write(REGISTER, register.replace(block, generate_register(read(SOT), decision_records())))
        print(f"{REGISTER}: canonical section regenerated from SoT §46")
        return 0

    failures = []
    check(failures.append)
    for f in failures:
        print(f"FAIL: {f}")
    if failures:
        print(f"{len(failures)} failure(s)")
        return 1
    print("docs-consistency: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
