# Gate record: G<n> <name>

<!-- Save as docs/poc/execution/gates/G<n>.md. Copy the matching checklist from "Checklists by gate" below into "Must be true". Fill only at the gate meeting, from evidence on the screen (plan §3.1). Never pre-fill. -->

- Gate: <!-- G0-T, G0-N and G1 to G7, with the name, as in plan §3.1. -->
- Date and time (WAT): <!-- When the review actually took place; scheduled times are in ../calendar.md. -->
- Deciders: <!-- The roles in the gate's "Decides" column (plan §3.1). Titles only: sign-offs read "Founder" and/or "Technical Co-Founder" (DEC-2026-10-16 E2). -->
- Must be true (checklist): <!-- Paste the gate's checklist from below; tick a line only with an evidence link beside it. -->
- Evidence links: <!-- Run IDs, CI links, reports and Record reconstructions shown at the meeting. -->
- Outcome: `PASS | FAIL | BLOCKED` <!-- Exactly one. Never "mostly done" or "pass with actions" (plan §3.1 gate rules). -->
- If it failed, what happens next: <!-- Quote the gate's "If it fails" text from below, then name the owners and dates. -->
- Regression cases added: <!-- Case IDs added because of this review; a fix after a failed gate gets its regression case first. -->
- Signatures: <!-- Each decider's title (Founder, Technical Co-Founder) and the date. No personal names. -->

## Checklists by gate

Copied from plan §3.1 ("Must be true", "Evidence shown", "Decides" and "If it fails" columns), split into one checkbox per sentence. G0 has two records, G0-T and G0-N (DEC-2026-10-16 E4). G0-N is also recorded in [`../gates/G0-N.md`](../gates/G0-N.md), which holds the internal TEN checks.

### G0-T Phase A exit, Tushe half

<!-- Plan §3.1, row G0-T. Scheduled: to be confirmed by Tushe (DEC-2026-10-16 E3, E4). Our request for the date goes to Tushe by Thu 22 Oct (calendar.md). Record: gates/G0-T.md. -->

- Deciders: Engineering lead, integration lead, benchmark owner, Tushe lead
- Evidence to show: Signed AT report; the signed worksheet

Must be true (all of it):

- [ ] Each of AT-01 to AT-20 passes, passes under the amended conditions in the signed worksheet, or is covered by an agreed exception with owner and date (REQ-ENV-007), in the joint session on the date Tushe confirms

If it fails (quoted): "Hostility proxy covers missing faults (REQ-ENV-005). No Phase B result counts until G0 passes. Our request for the date goes to Tushe by Thu 22 Oct (DEC-2026-10-16 E3)"

### G0-N Phase A exit, Noema half

<!-- Plan §3.1, row G0-N. Scheduled: Thu 22 Oct 2026, 17:00 (calendar.md). Record: gates/G0-N.md. -->

- Deciders: Engineering lead, integration lead, benchmark owner
- Evidence to show: Noema-side TEN report; contracts tag; fixture run log twice with identical output; isolation test log

Must be true (all of it):

- [ ] TEN-01 to TEN-08 pass (Noema-side checks against Tushe; internal, not in the worksheet and not sent to Tushe)
- [ ] `/contracts` v1 tagged. ≥ 50 fixtures reproducible
- [ ] Isolation tests pass, including runtime refusal on Tushe `/partner/...` routes and the `mock-case` truth endpoint

If it fails (quoted): "Phase B work continues on adapters and core logic. Noema-covered exceptions AT-04, AT-05, AT-07 and AT-14 not shown internally before the G1 review (Mon 26 Oct, 10:00) block G1"

### G1 Unknown-outcome slice

<!-- Plan §3.1, row G1. Scheduled: evidence run Fri 23 Oct 2026; review Mon 26 Oct 2026, 10:00 (calendar.md). Record: gates/G1.md. -->

- Deciders: Engineering lead
- Evidence to show: Live run plus Record reconstruction plus CI

Must be true (all of it):

- [ ] One clean case (US-01) and one timeout-after-write case (US-06) run end to end on text through the public API
- [ ] The unknown outcome is verified by key, never retried
- [ ] The Record reconstructs both
- [ ] Property tests for INV-03, INV-07, INV-08 and the prohibited registry are green

If it fails (quoted): "Week 2 starts with the slice. Ambiguity work waits"

### G2 Trust depth

<!-- Plan §3.1, row G2. Scheduled: Fri 30 Oct 2026, 16:00 (calendar.md). Record: gates/G2.md. -->

- Deciders: Engineering lead and benchmark owner
- Evidence to show: Benchmark smoke run by family; CI

Must be true (all of it):

- [ ] US-02, US-03, US-05, US-07, US-08, US-10, US-11, US-13, US-14, US-15, US-18, US-19, US-20, US-21 and US-22 pass
- [ ] All four write capabilities verified
- [ ] Kill switch works
- [ ] Conformance packs and core lint green

If it fails (quoted): "Week 3 hardening starts only on the passing families; failing ones stay first in the queue"

### G3 Hardened

<!-- Plan §3.1, row G3. Scheduled: Fri 6 Nov 2026, 16:00 (calendar.md). Record: gates/G3.md. -->

- Deciders: Engineering lead, benchmark owner, security reviewer
- Evidence to show: Scorecard; replay diff; chaos and scanner logs; drill records

Must be true (all of it):

- [ ] Full suite of ≥ 320 cases, with ≥ 300 hidden-oracle cases (SoT §40.3): every Tier 0 gate at zero
- [ ] All 30 invariant property tests green in deep mode
- [ ] US-01 to US-22 pass
- [ ] Replay of the full suite twice from a clean environment is identical
- [ ] The chaos matrix produces no ALLOW
- [ ] Evil-provider run clean
- [ ] Scanners clean
- [ ] Drills done

If it fails (quoted): "**No comparison arm starts** until G3 passes (SoT §38.5). Week 4 Monday is spent on the failure"

### G4 Comparison

<!-- Plan §3.1, row G4. Scheduled: Wed 11 Nov 2026, 16:00 (calendar.md). Record: gates/G4.md. -->

- Deciders: Benchmark owner and arm reviewer
- Evidence to show: Arm manifests; reviewer sign-off; comparison tables

Must be true (all of it):

- [ ] Arms A, B and D built, reviewed as competent by the independent reviewer, run on the frozen pack, and the report drafted
- [ ] Curve and operating point reviewed
- [ ] S2 budget agreed (PERD §69)

If it fails (quoted): "The release run proceeds; the comparison is reported as incomplete; "POC done" waits"

### G5 Voice

<!-- Plan §3.1, row G5. Scheduled: Wed 11 Nov 2026, 16:00 (calendar.md). Record: gates/G5.md. -->

- Deciders: Voice engineer and engineering lead
- Evidence to show: Field-session report

Must be true (all of it):

- [ ] Voice subset meets SoT §38.2: key-slot accuracy ≥ 95%, intent accuracy within 3 percentage points of text, every low-confidence key slot clarifies
- [ ] The real-conditions gate passes: Intent Object P95 ≤ 2.5 s on a Tecno Spark on Airtel 3G in Lagos noise, ≥ 100 sessions, ≥ 50% Pidgin, consent and retention rules met (PERD §45.4)

If it fails (quoted): "The demo runs in text; voice is shown only as a recorded measurement; **no design-partner demo** until it passes [SoT §37.5]"

### G6 Release run

<!-- Plan §3.1, row G6. Scheduled: Thu 12 Nov 2026, 18:00 (calendar.md). Record: gates/G6.md. -->

- Deciders: Founders
- Evidence to show: Signed evidence bundle

Must be true (all of it):

- [ ] Held-out plus full suite run by the benchmark owner on one release commit; results from different commits are never combined
- [ ] All PERD §60 acceptance criteria met, or each miss written down
- [ ] Clean-room reproduction passes
- [ ] Evidence bundle complete and signed

If it fails (quoted): "The demo shows the real result; external claims are limited to what the bundle permits"

### G7 External readiness

<!-- Plan §3.1, row G7. Scheduled: Fri 13 Nov 2026, 09:00 (dry run); the demo follows at 14:00 (calendar.md). Record: gates/G7.md. -->

- Deciders: Founders
- Evidence to show: Dry run at 09:00 Fri 13 Nov; the DoD pre-demo items signed at G6

Must be true (all of it):

- [ ] DoD signed at G6 (GOV-16, Thu 12 Nov 18:00) for every PERD §68 item that does not depend on the demo itself
- [ ] Every number has n, method, bound and CI
- [ ] Clocks labelled SYNTHETIC
- [ ] No ROI claim
- [ ] D1 to D10 run from the engine
- [ ] Kill switch, rollback and incident playbook drilled

If it fails (quoted): "Drop any demo scenario that is not real. Never script one"
