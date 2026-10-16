# G0-T joint session with Tushe

> **Date: to be confirmed by Tushe.** The session planned for Fri 16 Oct 2026, 18:00–20:30 WAT did not take place. Tushe has not confirmed a new date, and none is invented here. Our request for a date goes to Tushe by Thu 22 Oct 2026 (DEC-2026-10-16 E3). When Tushe confirms, record the date, then update [`../calendar.md`](../calendar.md), the plan rows ENV-12 and ENV-07 (a new plan version, plan §19) and [`../gates/G0-T.md`](../gates/G0-T.md).

This is the Tushe half of G0 (G0-T). G0 passes only when G0-T and the Noema half, [G0-N](../gates/G0-N.md), both pass (DEC-2026-10-16 E4).

## Purpose

Walk through the acceptance worksheet, agree it, sign it, run the acceptance tests against it, and sign the record, all in one sitting (worksheet section 7). The sent worksheet is the PDF [`../../tushe/acceptance/G0-worksheet-2026-10-13-SENT.pdf`](../../tushe/acceptance/G0-worksheet-2026-10-13-SENT.pdf). It is never edited; the signed copy is committed as a separate file.

Plan tasks: ENV-12 (agree and sign the worksheet) and ENV-07 (run AT-01 to AT-20, record, sign). Both carry the date TBC.

## Agenda: worksheet AT-01 to AT-20

The times are the worksheet's, as sent for a 18:00 start (section 7). They shift with the confirmed start time.

| Time | Step |
|---|---|
| 18:00 | Walk through the worksheet together. Agree the three definitions (section 1), every test and scenario row (sections 2 and 3), and the dates in section 4. Note any amendment in the document |
| 18:45 | Sign the agreed worksheet. Then confirm tenant, keys and sandbox version, and record the version |
| 18:55 | AT-02 and AT-18 (credential boundaries) |
| 19:05 | AT-16, then AT-01 (reset, then deterministic replay against M1 to M6) |
| 19:30 | AT-03, AT-11, AT-10 (commit-then-timeout, retry, idempotency) |
| 19:50 | AT-08, AT-06, AT-15 (contradiction, duplicate delivery, time) |
| 20:05 | AT-12, AT-13 (authorisation, policy versions) |
| 20:15 | AT-20 interim (Tushe's simulated-fault markers) |
| 20:20 | Read back the record: every test and its outcome, every exception with its owner and date |
| 20:30 | Both sides sign the record |

**Outcomes per test (worksheet section 2):** Pass: AT-02, 06, 08, 10, 11, 12, 13, 16, 18. Pass, amended: AT-01, 03, 15. Noema covers (shown once complete, not in this session): AT-04, 05, 07, 14, 17. Tushe, by date: AT-09 (Fri 30 Oct), AT-19 (Fri 23 Oct), AT-20 (Fri 30 Oct; markers shown in the session as the interim). An exception stays an exception in the record, with its owner and date; it is never counted as a pass (REQ-ENV-007).

## Before the session (Noema side)

- The Founder holds the Tushe administrator and fixture credentials and runs the harness; the Technical Co-Founder and the coding agents never read them (DEC-2026-10-16 E2, point 1).
- A tenant, keys and the sandbox version are confirmed with Tushe (R1, R5).
- The read surfaces R2 to R4 (due Fri 23 Oct) and R6 to R8 (due Fri 16 Oct) are checked against what arrived; any miss is raised the day it is missed.
- Nothing internal is brought into the Tushe-facing material: no benchmark detail, no held-out material, no TEN detail (AGENTS.md §4).

## After the session

- Commit the signed worksheet as `G0-worksheet-<date>-SIGNED.md` and `.pdf` and the AT report as `AT-report-<date>.md` in [`../../tushe/acceptance/`](../../tushe/acceptance/README.md).
- Fill [`../gates/G0-T.md`](../gates/G0-T.md) from the evidence, with exactly one outcome.
