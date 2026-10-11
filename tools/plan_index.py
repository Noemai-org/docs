#!/usr/bin/env python3
"""Generate and check the POC four-week plan task index.

Source: the newest docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v*.md.
Output: docs/poc/execution/tasks.csv (board import; never edit by hand).

A task row is a table line before "# APPENDICES" matching "| <ID> | ..." where
<ID> is <PREFIX>-<NN> and the prefix is not SR, OQ or OD. Pre-Monday rows
(under "## 7.") have no Needs column; their date is 2026-10-11 and week 0.
Other rows take their date from the nearest "### <Weekday> <D> <Month> · ..."
heading.

CSV columns:
    task_id, week, date, workstream, task, owner, req_ids, needs, done_when, gate

Usage:
    python3 tools/plan_index.py            # same as --write
    python3 tools/plan_index.py --write    # regenerate the CSV
    python3 tools/plan_index.py --check    # fail if the CSV is stale or the plan is inconsistent

--check fails if the CSV differs from what the plan generates; a task ID is
duplicated; a Needs entry names an unknown task or a task that appears later
in the plan; a task names a REQ ID that is not in the PERD index; a PERD REQ
has no task; Appendix C does not list exactly 105 edge cases or names an
unknown task; or Appendix D does not list exactly 22 stories or names an
unknown task.

Standard library only.
"""

import argparse
import csv
import datetime
import io
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAN_DIR = ROOT / "docs" / "poc" / "execution"
CSV_PATH = PLAN_DIR / "tasks.csv"
PERD_INDEX = ROOT / "docs" / "poc" / "perd" / "requirements-index.csv"

VERSION_RE = re.compile(r"^NOEMA_POC_4WEEK_PLAN_v(\d+(?:\.\d+)*)\.md$")
ROW_RE = re.compile(r"^\| ([A-Z]+-\d\d) \|")
NOT_TASKS = {"SR", "OQ", "OD"}
DAY_RE = re.compile(
    r"^### (?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) (\d{1,2}) "
    r"(January|February|March|April|May|June|July|August|September|October|November|December) · "
)
SECTION_RE = re.compile(r"^## (\d+)\. ")
APPENDICES = "# APPENDICES"
YEAR = 2026
PRE_MONDAY_DATE = datetime.date(2026, 10, 11)
WEEKS = [  # (first day, last day, week number)
    (datetime.date(2026, 10, 12), datetime.date(2026, 10, 16), 1),
    (datetime.date(2026, 10, 19), datetime.date(2026, 10, 23), 2),
    (datetime.date(2026, 10, 26), datetime.date(2026, 10, 30), 3),
    (datetime.date(2026, 11, 2), datetime.date(2026, 11, 6), 4),
]
# Plan §6: the fourteen workstreams, and the narrower prefixes that roll up to them.
WORKSTREAMS = ["GOV", "PLT", "CON", "ENV", "UND", "EVD", "TRU", "EXE", "OUT", "REC", "EXP", "VOI", "BEN", "SEC"]
ROLLUP = {
    "AGT": "PLT", "EDG": "PLT", "TST": "PLT",
    "PCK": "CON",
    "AMB": "UND", "INP": "UND",
    "RES": "EVD",
    "PLN": "EXE", "CAP": "EXE",
    "STM": "REC", "MEM": "REC",
    "RCV": "OUT",
    "UI": "EXP", "API": "EXP",
    "ARM": "BEN", "BIZ": "BEN",
    "OBS": "SEC", "OPS": "SEC", "DATA": "SEC",
    "DEM": "GOV", "REL": "GOV", "PRE": "GOV",
}
TASK_ID_RE = re.compile(r"\b([A-Z]+-\d\d)\b")
RANGE_RE = re.compile(r"\b([A-Z]+)-(\d\d) to (?:\1-)?(\d\d)\b")
REQ_RE = re.compile(r"\bREQ-[A-Z]+-\d{3}\b")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
GATE_RE = re.compile(r"\bG([0-7])\b")
COLUMNS = ["task_id", "week", "date", "workstream", "task", "owner", "req_ids", "needs", "done_when", "gate"]
EXPECTED = {"total": 201, "weeks": {0: 5, 1: 71, 2: 46, 3: 47, 4: 32}, "edge_cases": 105, "stories": 22}
MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"], 1)}


def newest_plan():
    found = []
    for path in PLAN_DIR.glob("NOEMA_POC_4WEEK_PLAN_v*.md"):
        m = VERSION_RE.match(path.name)
        if m:
            found.append((tuple(int(p) for p in m.group(1).split(".")), path))
    if not found:
        sys.exit(f"plan_index: no NOEMA_POC_4WEEK_PLAN_v*.md in {PLAN_DIR.relative_to(ROOT)}")
    return max(found)[1]


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def strip_markup(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"\1", text)
    return text.strip()


def task_ids(text):
    """Task IDs in text, in order, with 'X-06 to X-09' ranges expanded."""
    out = []
    pos = 0
    for m in RANGE_RE.finditer(text):
        out.extend(TASK_ID_RE.findall(text[pos:m.start()]))
        prefix, a, b = m.group(1), int(m.group(2)), int(m.group(3))
        out.extend(f"{prefix}-{n:02d}" for n in range(a, b + 1))
        pos = m.end()
    out.extend(TASK_ID_RE.findall(text[pos:]))
    return list(OrderedDict.fromkeys(out))


def week_of(date):
    if date == PRE_MONDAY_DATE:
        return 0
    for first, last, n in WEEKS:
        if first <= date <= last:
            return n
    return None


def parse(path):
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    errors = []
    try:
        cut = lines.index(APPENDICES)
    except ValueError:
        sys.exit(f"plan_index: '{APPENDICES}' heading not found in {path.relative_to(ROOT)}")

    tasks = []
    date = None
    section = None
    for lineno, line in enumerate(lines[:cut], 1):
        sm = SECTION_RE.match(line)
        if sm:
            section = int(sm.group(1))
            date = PRE_MONDAY_DATE if section == 7 else None
        dm = DAY_RE.match(line)
        if dm:
            date = datetime.date(YEAR, MONTHS[dm.group(2)], int(dm.group(1)))
        rm = ROW_RE.match(line)
        if not rm or rm.group(1).split("-")[0] in NOT_TASKS:
            continue
        c = cells(line)
        if section == 7:
            if len(c) != 5:
                errors.append(f"line {lineno}: pre-Monday row has {len(c)} cells, expected 5")
                continue
            tid, task, owner, req, done = c
            needs = ""
        else:
            if len(c) != 6:
                errors.append(f"line {lineno}: task row has {len(c)} cells, expected 6")
                continue
            tid, task, owner, req, needs, done = c
        if date is None:
            errors.append(f"line {lineno}: {tid} has no date heading above it")
            continue
        prefix = tid.split("-")[0]
        ws = prefix if prefix in WORKSTREAMS else ROLLUP.get(prefix)
        if ws is None:
            errors.append(f"line {lineno}: {tid} has a prefix not listed in plan §6")
        gates = []
        for bold in BOLD_RE.findall(line):
            for g in GATE_RE.findall(bold):
                if f"G{g}" not in gates:
                    gates.append(f"G{g}")
        tasks.append({
            "line": lineno,
            "task_id": tid,
            "week": week_of(date),
            "date": date.isoformat(),
            "workstream": ws or "",
            "task": strip_markup(task),
            "owner": strip_markup(owner),
            "req_ids": list(OrderedDict.fromkeys(REQ_RE.findall(line))),
            "needs": task_ids(needs),
            "done_when": strip_markup(done),
            "gate": gates,
        })
        if tasks[-1]["week"] is None:
            errors.append(f"line {lineno}: {tid} date {date} is outside the four weeks")

    # Duplicates and dependencies
    position = {}
    for i, t in enumerate(tasks):
        if t["task_id"] in position:
            errors.append(f"line {t['line']}: duplicate task ID {t['task_id']}")
        else:
            position[t["task_id"]] = i
    for i, t in enumerate(tasks):
        for need in t["needs"]:
            if need not in position:
                errors.append(f"line {t['line']}: {t['task_id']} needs unknown task {need}")
            elif position[need] > i:
                errors.append(f"line {t['line']}: {t['task_id']} needs {need}, which appears later in the plan")

    # Requirement coverage against the PERD index
    perd_reqs = []
    if PERD_INDEX.exists():
        with PERD_INDEX.open(encoding="utf-8", newline="") as fh:
            perd_reqs = [r["req_id"] for r in csv.DictReader(fh)]
    else:
        errors.append(f"{PERD_INDEX.relative_to(ROOT)} is missing")
    known = set(perd_reqs)
    covered = set()
    for t in tasks:
        for r in t["req_ids"]:
            if r not in known:
                errors.append(f"line {t['line']}: {t['task_id']} names {r}, which is not in the PERD index")
            covered.add(r)
    for r in perd_reqs:
        if r not in covered:
            errors.append(f"{r} has no task (plan Appendix A)")

    # Appendices C and D
    appendix = lines[cut:]
    ids = set(position)

    def appendix_rows(heading, row_prefix, cols):
        try:
            start = next(i for i, l in enumerate(appendix) if l.startswith(heading))
        except StopIteration:
            errors.append(f"appendix heading '{heading}' not found")
            return 0
        n = 0
        for offset, line in enumerate(appendix[start + 1:], start + 2):
            if line.startswith("## "):
                break
            if not line.startswith(f"| {row_prefix}"):
                continue
            n += 1
            c = cells(line)
            for col in cols:
                for tid in task_ids(c[col] if col < len(c) else ""):
                    if tid not in ids:
                        errors.append(f"line {cut + offset}: {c[0]} names unknown task {tid}")
        return n

    edge_cases = appendix_rows("## Appendix C", "EC-", [3, 4])
    stories = appendix_rows("## Appendix D", "US-", [2])
    if edge_cases != EXPECTED["edge_cases"]:
        errors.append(f"Appendix C lists {edge_cases} edge cases, expected {EXPECTED['edge_cases']}")
    if stories != EXPECTED["stories"]:
        errors.append(f"Appendix D lists {stories} user stories, expected {EXPECTED['stories']}")

    stats = {
        "tasks": tasks,
        "covered": len(covered & known),
        "perd_total": len(perd_reqs),
        "edge_cases": edge_cases,
        "stories": stories,
    }
    return stats, errors


def render(tasks):
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLUMNS, lineterminator="\n")
    w.writeheader()
    for t in tasks:
        row = {k: t[k] for k in COLUMNS}
        for k in ("req_ids", "needs", "gate"):
            row[k] = ";".join(t[k])
        w.writerow(row)
    return buf.getvalue()


def summary(stats, path):
    tasks = stats["tasks"]
    weeks = Counter(t["week"] for t in tasks)
    ws = Counter(t["workstream"] for t in tasks)
    out = [
        f"plan: {path.relative_to(ROOT)}",
        f"tasks: {len(tasks)}",
        "per week: " + ", ".join(f"week {w}: {weeks[w]}" for w in sorted(weeks)),
        "per workstream: " + ", ".join(f"{w} {ws[w]}" for w in WORKSTREAMS),
        f"requirements covered: {stats['covered']}/{stats['perd_total']}",
        f"edge cases (Appendix C): {stats['edge_cases']}",
        f"user stories (Appendix D): {stats['stories']}",
    ]
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="fail if the CSV is stale or the plan is inconsistent")
    mode.add_argument("--write", action="store_true", help="regenerate the CSV (default)")
    args = parser.parse_args()

    path = newest_plan()
    stats, errors = parse(path)
    expected_csv = render(stats["tasks"])
    weeks = Counter(t["week"] for t in stats["tasks"])
    if len(stats["tasks"]) != EXPECTED["total"] or dict(weeks) != EXPECTED["weeks"]:
        # Reported, never forced: the plan is the source.
        print("plan_index: note: task counts differ from the v1.1 baseline "
              "(201: 5/71/46/47/32)", file=sys.stderr)

    if args.check:
        if not CSV_PATH.exists():
            errors.append(f"{CSV_PATH.relative_to(ROOT)} is missing; run python3 tools/plan_index.py --write")
        elif CSV_PATH.read_text(encoding="utf-8") != expected_csv:
            errors.append(f"{CSV_PATH.relative_to(ROOT)} is stale; run python3 tools/plan_index.py --write")
    if errors:
        for e in errors:
            print(f"plan_index: FAIL: {e}", file=sys.stderr)
        return 1
    if not args.check:
        CSV_PATH.write_text(expected_csv, encoding="utf-8")
        print(f"plan_index: wrote {CSV_PATH.relative_to(ROOT)}")
    else:
        print("plan_index: OK")
    print(summary(stats, path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
