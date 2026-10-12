# Gate record: G<n> <name>

<!-- Save as docs/poc/execution/gates/G<n>.md. Copy the matching checklist from "Checklists by gate" below into "Must be true". Fill only at the gate meeting, from evidence on the screen (plan §3.1). Never pre-fill. -->

- Gate: <!-- G0 to G7 and its name, as in plan §3.1. -->
- Date and time (WAT): <!-- When the review actually took place; scheduled times are in ../calendar.md. -->
- Deciders: <!-- Names for the roles in the gate's "Decides" column (plan §3.1). -->
- Must be true (checklist): <!-- Paste the gate's checklist from below; tick a line only with an evidence link beside it. -->
- Evidence links: <!-- Run IDs, CI links, reports and Record reconstructions shown at the meeting. -->
- Outcome: `PASS | FAIL | BLOCKED` <!-- Exactly one. Never "mostly done" or "pass with actions" (plan §3.1 gate rules). -->
- If it failed, what happens next: <!-- Quote the gate's "If it fails" text from below, then name the owners and dates. -->
- Regression cases added: <!-- Case IDs added because of this review; a fix after a failed gate gets its regression case first. -->
- Signatures: <!-- Each decider's name and date. -->

## Checklists by gate

Copied from plan §3.1 ("Must be true", "Evidence shown", "Decides" and "If it fails" columns), split into one checkbox per sentence.

### G0 Phase A exit

<!-- Plan v1.2 §3.1, row G0 (DEC-2026-10-12). Scheduled: Thu 15 Oct 17:00 WAT (calendar.md). -->

- Deciders: Engineering lead, integration lead, benchmark owner, Tushe lead
- Evidence to show: Signed AT/TEN report; contracts tag; fixture run log twice with identical output

Must be true (all of it):

Run against the signed worksheet in `docs/poc/tushe/acceptance/`; record each AT as Pass, Pass amended, Noema covers or Tushe by date.

- [ ] Each of AT-01 to AT-20 passes, passes under the amended conditions in the signed worksheet, or is covered by an agreed exception with owner and date (REQ-ENV-007)
- [ ] TEN-01 to TEN-08 pass
- [ ] `/contracts` v1 tagged
- [ ] ≥ 50 fixtures reproducible
- [ ] Isolation tests pass, including runtime refusal on Tushe `/partner/...` routes and the `mock-case` truth endpoint

If it fails (quoted): "Phase B work continues on adapters and core logic, but **no G1 attempt** until G0 passes. Hostility proxy covers missing faults (REQ-ENV-005). Noema-covered exceptions not shown by Fri 16 Oct block G1"

### G1 Unknown-outcome slice

<!-- Plan §3.1, row G1. Scheduled: Fri 16 Oct 16:00 WAT (calendar.md). -->

- Deciders: Engineering lead
- Evidence to show: Live run plus Record reconstruction plus CI

Must be true (all of it):

- [ ] One clean case (US-01) and one timeout-after-write case (US-06) run end to end on text through the public API
- [ ] The unknown outcome is verified by key, never retried
- [ ] The Record reconstructs both
- [ ] Property tests for INV-03, INV-07, INV-08 and the prohibited registry are green

If it fails (quoted): "Week 2 starts with the slice. Ambiguity work waits"

### G2 Trust depth

<!-- Plan §3.1, row G2. Scheduled: Fri 23 Oct 16:00 WAT (calendar.md). -->

- Deciders: Engineering lead and benchmark owner
- Evidence to show: Benchmark smoke run by family; CI

Must be true (all of it):

- [ ] US-02, US-03, US-05, US-07, US-08, US-10, US-11, US-13, US-14, US-15, US-18, US-19, US-20, US-21 and US-22 pass
- [ ] All four write capabilities verified
- [ ] Kill switch works
- [ ] Conformance packs and core lint green

If it fails (quoted): "Week 3 hardening starts only on the passing families; failing ones stay first in the queue"

### G3 Hardened

<!-- Plan §3.1, row G3. Scheduled: Fri 30 Oct 16:00 WAT (calendar.md). -->

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

<!-- Plan §3.1, row G4. Scheduled: Wed 4 Nov 16:00 WAT (calendar.md). -->

- Deciders: Benchmark owner and arm reviewer
- Evidence to show: Arm manifests; reviewer sign-off; comparison tables

Must be true (all of it):

- [ ] Arms A, B and D built, reviewed as competent by the independent reviewer, run on the frozen pack, and the report drafted
- [ ] Curve and operating point reviewed
- [ ] S2 budget agreed (PERD §69)

If it fails (quoted): "The release run proceeds; the comparison is reported as incomplete; "POC done" waits"

### G5 Voice

<!-- Plan §3.1, row G5. Scheduled: Wed 4 Nov 16:00 WAT (calendar.md). -->

- Deciders: Voice engineer and engineering lead
- Evidence to show: Field-session report

Must be true (all of it):

- [ ] Voice subset meets SoT §38.2: key-slot accuracy ≥ 95%, intent accuracy within 3 percentage points of text, every low-confidence key slot clarifies
- [ ] The real-conditions gate passes: Intent Object P95 ≤ 2.5 s on a Tecno Spark on Airtel 3G in Lagos noise, ≥ 100 sessions, ≥ 50% Pidgin, consent and retention rules met (PERD §45.4)

If it fails (quoted): "The demo runs in text; voice is shown only as a recorded measurement; **no design-partner demo** until it passes [SoT §37.5]"

### G6 Release run

<!-- Plan §3.1, row G6. Scheduled: Thu 5 Nov 18:00 WAT (calendar.md). -->

- Deciders: Founders
- Evidence to show: Signed evidence bundle

Must be true (all of it):

- [ ] Held-out plus full suite run by the benchmark owner on one release commit; results from different commits are never combined
- [ ] All PERD §60 acceptance criteria met, or each miss written down
- [ ] Clean-room reproduction passes
- [ ] Evidence bundle complete and signed

If it fails (quoted): "The demo shows the real result; external claims are limited to what the bundle permits"

### G7 Demo readiness

<!-- Plan §3.1, row G7. Scheduled: Fri 6 Nov 09:00 (dry run) WAT (calendar.md). -->

- Deciders: Founders
- Evidence to show: Dry run at 09:00 Fri 6 Nov

Must be true (all of it):

- [ ] D1 to D10 run from the engine
- [ ] Every number has n, method, bound and CI
- [ ] Clocks labelled SYNTHETIC
- [ ] No ROI claim
- [ ] Kill switch, rollback and incident playbook drilled

If it fails (quoted): "Drop any demo scenario that is not real. Never script one"
