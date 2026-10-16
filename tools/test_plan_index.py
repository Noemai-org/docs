#!/usr/bin/env python3
"""Tests for plan_index.py (DEC-2026-10-16 E3, E4; the task-cards index).

Run from the repository root:
    python3 -m unittest discover -s tools -p 'test_*.py'

Standard library only. The mini plans below are synthetic and only exercise the parser.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_index as pi  # noqa: E402

HEAD = "| ID | Task | Owner | REQ | Needs | Done when |\n|---|---|---|---|---|---|\n"


def plan(*sections):
    """A mini plan: section 7 with a PRE row, then the given raw sections, then the appendices marker."""
    pre = ("## 7. Before Monday\n\n| ID | Task | Owner | REQ | Done when |\n|---|---|---|---|---|\n"
           "| PRE-01 | Prepare | EL | — | Done |\n\n")
    return pre + "\n".join(sections) + "\n# APPENDICES\n"


def day(heading, *rows):
    return f"### {heading}\n\n" + HEAD + "\n".join(rows) + "\n"


def run(text):
    stats, errors = pi.parse_text(text, "synthetic")
    return {t["task_id"]: t for t in stats["tasks"]}, errors


def only(errors, needle):
    return [e for e in errors if needle in e]


class Dates(unittest.TestCase):
    def test_week_numbers_follow_the_rebaselined_calendar(self):
        text = plan(
            day("Wednesday 14 October · Delivered", "| CON-04 | A | EL | — | — | Delivered 14 Oct 2026 |"),
            day("Monday 19 October · One", "| GOV-01 | B | FND | — | — | x |"),
            day("Friday 13 November · Demo", "| DEM-03 | C | FND | — | — | x |"),
        )
        tasks, _ = run(text)
        self.assertEqual(tasks["PRE-01"]["week"], 0)
        self.assertEqual(tasks["CON-04"]["week"], 0)
        self.assertEqual(tasks["GOV-01"]["week"], 1)
        self.assertEqual(tasks["DEM-03"]["week"], 4)

    def test_date_outside_the_window_is_an_error(self):
        _, errors = run(plan(day("Monday 16 November · Late", "| GOV-01 | B | FND | — | — | x |")))
        self.assertTrue(only(errors, "outside the four weeks"))


class TbcDate(unittest.TestCase):
    TBC = "### To be confirmed by Tushe · G0-T\n\n"

    def test_tbc_is_accepted_on_a_g0t_row(self):
        text = plan(self.TBC + HEAD + "| ENV-07 | **G0-T** joint session | IL | — | — | Signed → **G0-T** |\n")
        tasks, errors = run(text)
        self.assertEqual(tasks["ENV-07"]["date"], "TBC")
        self.assertEqual(tasks["ENV-07"]["week"], "TBC")
        self.assertEqual(tasks["ENV-07"]["gate"], ["G0-T"])
        self.assertFalse(only(errors, "accepted only on rows whose gate is G0-T"))

    def test_tbc_is_rejected_on_any_other_row(self):
        text = plan(self.TBC + HEAD + "| ENV-12 | Sign the worksheet | IL | — | — | Signed |\n")
        _, errors = run(text)
        self.assertTrue(only(errors, "accepted only on rows whose gate is G0-T"))

    def test_tbc_is_rejected_on_a_row_with_another_gate(self):
        text = plan(self.TBC + HEAD + "| ENV-12 | Sign | IL | — | — | **G0-N** |\n")
        _, errors = run(text)
        self.assertTrue(only(errors, "accepted only on rows whose gate is G0-T"))

    def test_a_dated_task_cannot_wait_for_a_tbc_task(self):
        text = plan(
            self.TBC + HEAD + "| ENV-07 | **G0-T** | IL | — | — | **G0-T** |\n",
            day("Monday 26 October · Review", "| GOV-07 | G1 review | EL | — | ENV-07 | Gate record |"),
        )
        _, errors = run(text)
        self.assertTrue(only(errors, "has a date but needs ENV-07"))

    def test_both_gate_halves_are_read_from_bold_text(self):
        text = plan(day("Thursday 22 October · G0-N", "| ENV-14 | **G0-N** Noema half | IL | — | — | → **G0-N** |"))
        tasks, _ = run(text)
        self.assertEqual(tasks["ENV-14"]["gate"], ["G0-N"])


class SplitTaskIds(unittest.TestCase):
    def test_a_lower_case_suffix_is_part_of_the_task_id(self):
        text = plan(
            day("Monday 19 October · One",
                "| BEN-16 | A | B | — | — | x |",
                "| BEN-17a | Triage | B | — | BEN-16 | x |",
                "| BEN-17b | Fix | C1, C2 | — | BEN-17a | x |",
                "| BEN-18 | Replay | B | — | BEN-17b | x |"),
        )
        tasks, errors = run(text)
        self.assertEqual(only(errors, "needs"), [])
        self.assertEqual(tasks["BEN-17b"]["needs"], ["BEN-17a"])
        self.assertEqual(tasks["BEN-18"]["needs"], ["BEN-17b"])

    def test_a_need_on_the_old_unsplit_id_is_unknown(self):
        text = plan(day("Monday 19 October · One",
                        "| BEN-17a | Triage | B | — | — | x |", "| BEN-18 | Replay | B | — | BEN-17 | x |"))
        _, errors = run(text)
        self.assertTrue(only(errors, "unknown task BEN-17"))


class Needs(unittest.TestCase):
    def test_forward_need_is_an_error(self):
        text = plan(
            day("Monday 19 October · One", "| GOV-01 | B | FND | — | GOV-02 | x |"),
            day("Tuesday 20 October · Two", "| GOV-02 | C | FND | — | — | x |"),
        )
        _, errors = run(text)
        self.assertTrue(only(errors, "needs GOV-02, which appears later"))

    def test_forward_need_is_allowed_for_a_delivered_row(self):
        text = plan(
            day("Monday 12 October · Delivered", "| GOV-19 | A | FND | — | GOV-01 | Merged; delivered 12 Oct 2026 |"),
            day("Monday 19 October · One", "| GOV-01 | B | FND | — | — | x |"),
        )
        _, errors = run(text)
        self.assertFalse(only(errors, "appears later"))

    def test_external_input_is_kept_in_needs(self):
        text = plan(day("Tuesday 20 October · One", "| ENV-11 | Map | IL | — | ENV-01, R1 batch 1 received | x |"),)
        text = text.replace("| ENV-11 |", "| ENV-01 | Kick off | IL | — | — | x |\n| ENV-11 |")
        tasks, errors = run(text)
        self.assertEqual(tasks["ENV-11"]["needs"], ["ENV-01", "R1 batch 1 received"])
        self.assertFalse(only(errors, "unknown task"))


class Cards(unittest.TestCase):
    TASKS = [
        {"task_id": "PLT-01", "task": "Create the `noema` skeleton per DEC R1. It includes: manifests", "date": "2026-10-16"},
        {"task_id": "ENV-13", "task": "Webhook relay: verifies signatures", "date": "2026-10-22"},
        {"task_id": "ENV-07", "task": "G0-T: joint session", "date": "TBC"},
    ]

    def test_each_card_appears_exactly_once_in_plan_order(self):
        text, missing = pi.render_cards_index(self.TASKS, {"ENV-13": "", "PLT-01": "", "ENV-07": ""})
        self.assertEqual(missing, [])
        rows = [l for l in text.splitlines() if l.startswith("| [")]
        self.assertEqual([r.split("]")[0] for r in rows], ["| [PLT-01", "| [ENV-13", "| [ENV-07"])
        self.assertEqual(len(rows), len(set(rows)))

    def test_generator_is_idempotent(self):
        cards = {"PLT-01": "", "ENV-13": "", "ENV-07": ""}
        first, _ = pi.render_cards_index(self.TASKS, cards)
        second, _ = pi.render_cards_index(self.TASKS, cards)
        self.assertEqual(first, second)

    def test_card_without_a_plan_row_is_reported(self):
        _, missing = pi.render_cards_index(self.TASKS, {"PLT-01": "", "XYZ-99": ""})
        self.assertEqual(missing, ["XYZ-99"])

    def test_title_comes_from_the_card_and_keeps_its_code_formatting(self):
        text, _ = pi.render_cards_index(self.TASKS, {"PLT-01": "Create the `noema` skeleton per DEC R1. It includes: manifests"})
        self.assertIn("| Create the `noema` skeleton per DEC R1 |", text)

    def test_short_title_stops_at_the_first_clause(self):
        self.assertEqual(pi.short_title("Hostility proxy: transport faults, stale reads"), "Hostility proxy")
        self.assertEqual(pi.short_title("CI pipeline (build, unit tests)"), "CI pipeline")
        self.assertLessEqual(len(pi.short_title("x" * 300)), 100)

    def test_tbc_day_label(self):
        self.assertEqual(pi.day_label("TBC"), "To be confirmed by Tushe (G0-T)")
        self.assertEqual(pi.day_label("2026-10-19"), "Mon 19 Oct")


class Appendices(unittest.TestCase):
    def test_appendix_b_counts_follow_the_rows(self):
        tasks = [{"workstream": "GOV"}, {"workstream": "GOV"}, {"workstream": "ENV"}]
        table = pi.render_appendix_b(tasks)
        self.assertIn("| GOV | 2 |", table)
        self.assertIn("| ENV | 1 |", table)
        self.assertEqual(table[-1], "| **Total** | **3** |")

    def test_appendix_a_lists_tasks_in_plan_order(self):
        tasks = [{"task_id": "B-01", "req_ids": ["REQ-X-001"]}, {"task_id": "A-01", "req_ids": ["REQ-X-001"]}]
        table = pi.render_appendix_a(tasks, [{"req_id": "REQ-X-001", "title": "T", "priority": "P0"}])
        self.assertEqual(table[-1], "| REQ-X-001 | T | P0 | B-01, A-01 |")


if __name__ == "__main__":
    unittest.main()
