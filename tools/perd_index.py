#!/usr/bin/env python3
"""Generate and check the PERD requirements index.

Source: the newest docs/poc/perd/NOEMA_POC_PERD_v*.md (the POC Product &
Engineering Requirements Document). Output: docs/poc/perd/requirements-index.csv.

Every requirement heading in the PERD has the form

    #### REQ-<AREA>-<NNN> · <Title> · <P0|P1|P2>

The CSV has one row per requirement:

    req_id, title, priority, area, perd_section, sot_ids, dependencies

- perd_section: the nearest preceding "## N. ..." heading.
- sot_ids: SoT IDs found in the requirement's block (POC-FR-, POC-NFR-,
  PLAT-FR-, PLAT-NFR-, INV-, US-, AGENT-, BD-, OD-), de-duplicated in order
  of first appearance and joined with ";".
- dependencies: REQ IDs on the block's "Dependencies:" line, joined with ";".
  A range such as REQ-EXE-002..004 is expanded.

Usage:
    python3 tools/perd_index.py            # same as --write
    python3 tools/perd_index.py --write    # regenerate the CSV
    python3 tools/perd_index.py --check    # fail if the CSV is stale or IDs are broken

--check fails if the committed CSV differs from what the PERD generates, if a
REQ ID is defined twice, if a "#### REQ-" heading does not match the format,
or if any REQ reference in the PERD has no matching heading.

Standard library only.
"""

import argparse
import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PERD_DIR = ROOT / "docs" / "poc" / "perd"
CSV_PATH = PERD_DIR / "requirements-index.csv"

HEADING_RE = re.compile(r"^#### (REQ-[A-Z]+-\d{3}) · (.+?) · (P[012])$")
SECTION_RE = re.compile(r"^## (\d+)\. (.+)$")
ANY_HEADING_RE = re.compile(r"^#{1,4} ")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
# A REQ reference, optionally followed by a range end: REQ-EXE-002..004 or
# REQ-EXE-002..REQ-EXE-004.
REQ_REF_RE = re.compile(r"\b(REQ-([A-Z]+)-(\d{3}))(?:\.\.(?:REQ-\2-)?(\d{3}))?\b")
SOT_ID_RE = re.compile(
    r"(?<![\w-])("
    r"POC-FR-\d+|POC-NFR-\d+|PLAT-FR-\d+|PLAT-NFR-\d+|"
    r"INV-\d+|US-\d+|AGENT-\d+|BD-\d+|OD-\d+"
    r")\b"
)
DEPENDENCIES_RE = re.compile(r"^\s*- \*\*Dependencies:\*\*(.*)$")
VERSION_RE = re.compile(r"^NOEMA_POC_PERD_v(\d+(?:\.\d+)*)\.md$")

COLUMNS = ["req_id", "title", "priority", "area", "perd_section", "sot_ids", "dependencies"]
EXPECTED = {"total": 152, "P0": 128, "P1": 21, "P2": 3}


def newest_perd():
    found = []
    for path in PERD_DIR.glob("NOEMA_POC_PERD_v*.md"):
        m = VERSION_RE.match(path.name)
        if m:
            found.append((tuple(int(p) for p in m.group(1).split(".")), path))
    if not found:
        sys.exit(f"perd_index: no NOEMA_POC_PERD_v*.md in {PERD_DIR.relative_to(ROOT)}")
    return max(found)[1]


def expand_refs(text):
    """Return the REQ IDs referenced in text, with ranges expanded, in order."""
    ids = []
    for m in REQ_REF_RE.finditer(text):
        start_id, area, start = m.group(1), m.group(2), m.group(3)
        end = m.group(4)
        if end is None or int(end) <= int(start):
            ids.append(start_id)
            continue
        for n in range(int(start), int(end) + 1):
            ids.append(f"REQ-{area}-{n:03d}")
    return ids


def dedupe(items):
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


def parse(path):
    lines = path.read_text(encoding="utf-8").split("\n")
    errors = []
    reqs = []  # dicts in document order
    current = None
    section = ""
    in_fence = False

    for lineno, line in enumerate(lines, 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
        if not in_fence and ANY_HEADING_RE.match(line):
            current = None
            sm = SECTION_RE.match(line)
            if sm:
                section = f"{sm.group(1)}. {sm.group(2).strip()}"
            if line.startswith("#### REQ-"):
                hm = HEADING_RE.match(line)
                if not hm:
                    errors.append(f"line {lineno}: REQ heading does not match the format: {line!r}")
                    continue
                current = {
                    "req_id": hm.group(1),
                    "title": hm.group(2),
                    "priority": hm.group(3),
                    "area": hm.group(1).split("-")[1],
                    "perd_section": section,
                    "line": lineno,
                    "body": [],
                    "deps": [],
                }
                reqs.append(current)
            continue
        if current is not None:
            current["body"].append(line)
            dm = DEPENDENCIES_RE.match(line)
            if dm:
                current["deps"].extend(expand_refs(dm.group(1)))

    first_seen = {}
    for r in reqs:
        if r["req_id"] in first_seen:
            errors.append(
                f"line {r['line']}: duplicate {r['req_id']} (first defined on line {first_seen[r['req_id']]})"
            )
        else:
            first_seen[r["req_id"]] = r["line"]

    defined = set(first_seen)
    for lineno, line in enumerate(lines, 1):
        for ref in expand_refs(line):
            if ref not in defined:
                errors.append(f"line {lineno}: {ref} is referenced but has no heading")

    rows = []
    for r in reqs:
        sot_ids = dedupe(SOT_ID_RE.findall("\n".join(r["body"])))
        deps = [d for d in dedupe(r["deps"]) if d != r["req_id"]]
        rows.append(
            {
                "req_id": r["req_id"],
                "title": r["title"],
                "priority": r["priority"],
                "area": r["area"],
                "perd_section": r["perd_section"],
                "sot_ids": ";".join(sot_ids),
                "dependencies": ";".join(deps),
            }
        )
    return rows, errors


def render(rows):
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=COLUMNS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue()


def counts(rows):
    c = {"total": len(rows), "P0": 0, "P1": 0, "P2": 0}
    for r in rows:
        c[r["priority"]] += 1
    return c


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="fail if the CSV is stale or IDs are broken")
    mode.add_argument("--write", action="store_true", help="regenerate the CSV (default)")
    args = parser.parse_args()

    perd = newest_perd()
    rows, errors = parse(perd)
    expected_csv = render(rows)
    c = counts(rows)
    summary = f"{c['total']} requirements ({c['P0']} P0, {c['P1']} P1, {c['P2']} P2) in {perd.relative_to(ROOT)}"
    if c != EXPECTED:
        # Reported, never forced: the PERD is the source.
        print(
            f"perd_index: note: counts differ from the v1.1 baseline "
            f"{EXPECTED['total']} ({EXPECTED['P0']}/{EXPECTED['P1']}/{EXPECTED['P2']})",
            file=sys.stderr,
        )

    if args.check:
        if not CSV_PATH.exists():
            errors.append(f"{CSV_PATH.relative_to(ROOT)} is missing; run python3 tools/perd_index.py --write")
        elif CSV_PATH.read_text(encoding="utf-8") != expected_csv:
            errors.append(f"{CSV_PATH.relative_to(ROOT)} is stale; run python3 tools/perd_index.py --write")
        if errors:
            for e in errors:
                print(f"perd_index: FAIL: {e}", file=sys.stderr)
            return 1
        print(f"perd_index: OK: {summary}")
        return 0

    if errors:
        for e in errors:
            print(f"perd_index: FAIL: {e}", file=sys.stderr)
        return 1
    CSV_PATH.write_text(expected_csv, encoding="utf-8")
    print(f"perd_index: wrote {CSV_PATH.relative_to(ROOT)}: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
