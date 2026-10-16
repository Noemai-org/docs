#!/usr/bin/env python3
"""Generate and check the POC four-week plan task index.

Source: the newest docs/poc/execution/NOEMA_POC_4WEEK_PLAN_v*.md.
Output: docs/poc/execution/tasks.csv (board import; never edit by hand).

A task row is a table line before "# APPENDICES" matching "| <ID> | ..." where
<ID> is <PREFIX>-<NN>, optionally followed by one lower-case letter for a split task (BEN-17a), and the prefix is not SR, OQ or OD. Pre-Monday rows
(prefix PRE, under "## 7.") have no Needs column; their date is 2026-10-11 and
week 0. Other rows take their date from the nearest "### <Weekday> <D> <Month> · ..."
heading. Work delivered before the re-baseline (dates up to Sun 18 Oct) is week 0.
A heading "### To be confirmed by Tushe · ..." gives its rows the literal date
TBC; that is accepted only on rows whose gate is G0-T (DEC-2026-10-16 E3, E4).

CSV columns:
    task_id, week, date, workstream, task, owner, req_ids, needs, done_when, gate

The needs column holds task IDs and, after them, external inputs written in
the Needs cell as "R<n> received" or "R<n> batch <m> received" (Tushe deliveries).

Usage:
    python3 tools/plan_index.py            # same as --write
    python3 tools/plan_index.py --write    # regenerate the CSV
    python3 tools/plan_index.py --check    # fail if the CSV is stale or the plan is inconsistent

--check fails if the CSV differs from what the plan generates; a task ID is
duplicated; a Needs entry names an unknown task or a task that appears later
in the plan (allowed only for a row whose Done when says "delivered <date>",
which was done out of order); a dated task needs a TBC task; the TBC date is on
a row that is not gate G0-T; Appendix A or B differs from the task rows; the
task-cards index is stale; a task names a REQ ID that is not in the PERD index; a PERD REQ
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
CARDS_DIR = PLAN_DIR / "task-cards"
CARDS_README = CARDS_DIR / "README.md"

VERSION_RE = re.compile(r"^NOEMA_POC_4WEEK_PLAN_v(\d+(?:\.\d+)*)\.md$")
ROW_RE = re.compile(r"^\| ([A-Z]+-\d\d[a-z]?) \|")
NOT_TASKS = {"SR", "OQ", "OD"}
TBC = "TBC"
TBC_RE = re.compile(r"^### To be confirmed by Tushe · ")
DAY_RE = re.compile(
    r"^### (?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) (\d{1,2}) "
    r"(January|February|March|April|May|June|July|August|September|October|November|December) · "
)
SECTION_RE = re.compile(r"^## (\d+)\. ")
APPENDICES = "# APPENDICES"
YEAR = 2026
PRE_MONDAY_DATE = datetime.date(2026, 10, 11)
# Re-baselined by DEC-2026-10-16 E3: every date moved forward seven days. Dates up to Sun 18 Oct are
# week 0: the pre-Monday tasks and the work delivered before the re-baseline.
WEEK0_LAST_DAY = datetime.date(2026, 10, 18)
WEEKS = [  # (first day, last day, week number)
    (datetime.date(2026, 10, 19), datetime.date(2026, 10, 23), 1),
    (datetime.date(2026, 10, 26), datetime.date(2026, 10, 30), 2),
    (datetime.date(2026, 11, 2), datetime.date(2026, 11, 6), 3),
    (datetime.date(2026, 11, 9), datetime.date(2026, 11, 13), 4),
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
TASK_ID_RE = re.compile(r"\b([A-Z]+-\d\d[a-z]?)\b")
RANGE_RE = re.compile(r"\b([A-Z]+)-(\d\d) to (?:\1-)?(\d\d)\b")
REQ_RE = re.compile(r"\bREQ-[A-Z]+-\d{3}\b")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
GATE_RE = re.compile(r"\bG(0-T|0-N|[0-7])\b")
EXTERNAL_RE = re.compile(r"\bR\d{1,2}(?: batch \d)? received\b")
DELIVERED_RE = re.compile(r"\bdelivered \d{1,2} (?:Oct|Nov)", re.I)
COLUMNS = ["task_id", "week", "date", "workstream", "task", "owner", "req_ids", "needs", "done_when", "gate"]
EXPECTED = {"total": 214, "weeks": {0: 9, 1: 75, 2: 48, 3: 48, 4: 32, TBC: 2}, "edge_cases": 105, "stories": 22}
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
    if date == TBC:
        return TBC
    if PRE_MONDAY_DATE <= date <= WEEK0_LAST_DAY:
        return 0
    for first, last, n in WEEKS:
        if first <= date <= last:
            return n
    return None


def parse_text(text, label="plan"):
    return _parse(text.split("\n"), label)


def parse(path):
    return _parse(path.read_text(encoding="utf-8").split("\n"), str(path.relative_to(ROOT)))


def _parse(lines, label):
    errors = []
    try:
        cut = lines.index(APPENDICES)
    except ValueError:
        sys.exit(f"plan_index: '{APPENDICES}' heading not found in {label}")

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
        if TBC_RE.match(line):
            date = TBC
        rm = ROW_RE.match(line)
        if not rm or rm.group(1).split("-")[0] in NOT_TASKS:
            continue
        c = cells(line)
        if section == 7 and rm.group(1).split("-")[0] == "PRE":
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
            "date": date if date == TBC else date.isoformat(),
            "workstream": ws or "",
            "task": strip_markup(task),
            "owner": strip_markup(owner),
            "req_ids": list(OrderedDict.fromkeys(REQ_RE.findall(line))),
            "needs": task_ids(needs) + EXTERNAL_RE.findall(strip_markup(needs)),
            "done_when": strip_markup(done),
            "gate": gates,
        })
        if tasks[-1]["week"] is None:
            errors.append(f"line {lineno}: {tid} date {date} is outside the four weeks")
        if date == TBC and "G0-T" not in gates:
            errors.append(f"line {lineno}: {tid} has the date {TBC}, which is accepted only on rows whose gate is G0-T")

    # Duplicates and dependencies
    position = {}
    for i, t in enumerate(tasks):
        if t["task_id"] in position:
            errors.append(f"line {t['line']}: duplicate task ID {t['task_id']}")
        else:
            position[t["task_id"]] = i
    by_id = {t["task_id"]: t for t in tasks}
    for i, t in enumerate(tasks):
        for need in t["needs"]:
            if EXTERNAL_RE.fullmatch(need):
                continue
            if need not in position:
                errors.append(f"line {t['line']}: {t['task_id']} needs unknown task {need}")
            elif by_id[need]["date"] == TBC and t["date"] != TBC:
                errors.append(f"line {t['line']}: {t['task_id']} has a date but needs {need}, which is {TBC}")
            elif position[need] > i and not DELIVERED_RE.search(t["done_when"]):
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

    perd_rows = []
    if PERD_INDEX.exists():
        with PERD_INDEX.open(encoding="utf-8", newline="") as fh:
            perd_rows = list(csv.DictReader(fh))
    if perd_rows:
        found_a = appendix_table(appendix, "## Appendix A", "| REQ-")
        if found_a != render_appendix_a(tasks, perd_rows):
            errors.append("Appendix A differs from the task rows; run python3 tools/plan_index.py --write")
    found_b = appendix_table(appendix, "## Appendix B", "| ")
    if found_b[2:] != render_appendix_b(tasks)[2:]:
        errors.append("Appendix B differs from the task rows; run python3 tools/plan_index.py --write")
    m = re.search(r"The plan holds \*\*(\d+) tasks\*\*", "\n".join(appendix))
    if not m or int(m.group(1)) != len(tasks):
        errors.append(f"Appendix B states {m.group(1) if m else 'no'} tasks, but the plan has {len(tasks)}")

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


def appendix_table(appendix, heading, row_prefix):
    """The table lines of one appendix: the header, the rule and every row starting with row_prefix."""
    try:
        start = next(i for i, l in enumerate(appendix) if l.startswith(heading))
    except StopIteration:
        return []
    out = []
    for line in appendix[start + 1:]:
        if line.startswith("## "):
            break
        if line.startswith("| REQ |") or line.startswith("| Workstream |") or line.startswith("|---"):
            out.append(line)
        elif line.startswith(row_prefix):
            out.append(line)
    return out


def render_appendix_a(tasks, perd_rows):
    by = OrderedDict()
    for t in tasks:
        for r in t["req_ids"]:
            by.setdefault(r, []).append(t["task_id"])
    out = ["| REQ | Title | Priority | Delivered by |", "|---|---|---|---|"]
    for r in perd_rows:
        out.append(f"| {r['req_id']} | {r['title']} | {r['priority']} | {', '.join(by.get(r['req_id'], []))} |")
    return out


def render_appendix_b(tasks):
    ws = Counter(t["workstream"] for t in tasks)
    out = ["| Workstream | Tasks |", "|---|---|"]
    out += [f"| {w} | {ws[w]} |" for w in WORKSTREAMS]
    out.append(f"| **Total** | **{len(tasks)}** |")
    return out


def day_label(date):
    if date == TBC:
        return "To be confirmed by Tushe (G0-T)"
    d = datetime.date.fromisoformat(date)
    return f"{d:%a} {d.day} {d:%b}"


CARDS_HEADER = """# Task cards

- A task card is required before a task starts (plan §4.1; REQ-AGT-002).
- Cards use the PERD template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Acceptance criteria are copied verbatim from the PERD REQ blocks (PERD v1.2; GOV-20 and ENV-13 from PERD v1.3; PLT-01 to PLT-04 from PERD v1.4; the ENV-13 relay wording from PERD v1.5; PCK-01, PCK-02 and UND-05 from PERD v1.6).
- File name: `<TASK-ID>.md`, for example `ENV-08.md`.
- A card is changed only by its owner, in a PR, and says what changed and why.
- This index is generated from the card files and the plan by `python3 tools/plan_index.py --write`; CI runs `--check`. Never edit it by hand.

"""


def short_title(text):
    """The first clause of a task description: up to the first colon, full stop, semicolon or bracket."""
    title = re.split(r"[:;] |\. | \(", text, maxsplit=1)[0].rstrip(".:;")
    return title if len(title) <= 100 else title[:97].rstrip() + "..."


def render_cards_index(tasks, cards):
    """The task-cards README: one row per card file, in plan order, each card exactly once.

    cards maps a task ID to the task text on its card (so the title keeps its code formatting)."""
    by_id = {t["task_id"]: t for t in tasks}
    rows = ["| Card | Task | Day (plan v1.6) |", "|---|---|---|"]
    for t in tasks:
        tid = t["task_id"]
        if tid not in cards:
            continue
        rows.append(f"| [{tid}]({tid}.md) | {short_title(cards[tid] or t['task'])} | {day_label(t['date'])} |")
    missing = sorted(set(cards) - set(by_id))
    return CARDS_HEADER + "\n".join(rows) + "\n", missing


def cards_on_disk():
    """{task ID: task text from the card's TASK line} for every card file."""
    out = {}
    if not CARDS_DIR.exists():
        return out
    for path in sorted(CARDS_DIR.glob("*.md")):
        if not re.fullmatch(r"[A-Z]+-\d\d[a-z]?", path.stem):
            continue
        m = re.search(rf"^TASK-P\d-\d+  {re.escape(path.stem)} · (.+)$", path.read_text(encoding="utf-8"), re.M)
        out[path.stem] = m.group(1) if m else ""
    return out


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
        "per week: " + ", ".join(f"week {w}: {weeks[w]}" for w in sorted(weeks, key=str)),
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
        print("plan_index: note: task counts differ from the v1.6 baseline "
              "(214: week 0 9, week 1 75, week 2 48, week 3 48, week 4 32, TBC 2)", file=sys.stderr)

    cards_text = None
    if CARDS_DIR.exists():
        cards_text, missing = render_cards_index(stats["tasks"], cards_on_disk())
        for m in missing:
            errors.append(f"task card {m}.md has no task row in the plan")

    if args.check:
        if cards_text is not None and (not CARDS_README.exists() or CARDS_README.read_text(encoding="utf-8") != cards_text):
            errors.append(f"{CARDS_README.relative_to(ROOT)} is stale; run python3 tools/plan_index.py --write")
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
        if cards_text is not None:
            CARDS_README.write_text(cards_text, encoding="utf-8")
            print(f"plan_index: wrote {CARDS_README.relative_to(ROOT)}")
    else:
        print("plan_index: OK")
    print(summary(stats, path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
