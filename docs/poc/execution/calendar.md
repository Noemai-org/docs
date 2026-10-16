# POC build calendar (WAT)

Every fixed event in [the plan](NOEMA_POC_4WEEK_PLAN_v1.6.md), re-baselined by [DEC-2026-10-16](../../decisions/DEC-2026-10-16-execution-reset.md) E3: Mon 19 Oct to Fri 13 Nov 2026, with the work delivered on 12 to 16 Oct shown as week 0. Times are West Africa Time. Gates outrank dates: if a gate and the calendar conflict, the gate wins and the date moves (SoT §40.2). Tushe's own dates (R1 to R13) do not move.

| Day | Time (WAT) | Event | Plan section |
|---|---|---|---|
| Every working day | 09:00 (15 min) | Stand-up | §5 |
| Every working day | 12:30 (10 min) | Integration check | §5 |
| Every working day | 17:00 (30 min) | Daily review | §5 |
| Every working day | 17:30 | Daily note committed (`daily/<YYYY-MM-DD>.md`) | §15 |
| Every night | 02:00 | Nightly run (full suite from week 2, fault suite, deep properties, chain verification, performance) | §5 |
| Every day | 07:00 | Nightly report | §15 |
| Tuesdays 20, 27 Oct and 3, 10 Nov | 16:00 (30 min) | Founder evidence review | §5 |
| Fridays 30 Oct and 6 Nov | 16:00 (60 min) | Gate review (the week 1 Friday slot, 23 Oct, is used for the G1 evidence run) | §5, §3 |
| Fridays 23, 30 Oct and 6 Nov | 17:00 (30 min) | Week retrospective | §5 |
| Sun 11 Oct | before Mon 09:00 | Pre-Monday tasks PRE-01 to PRE-05 (done) | §7 |
| Mon 12 Oct | 11:00 | Tushe kickoff (done) | §7 (PRE-03) |
| Thu 15 Oct | all day | Tushe R1 batch 1 (3 to 5 tenants and all the credentials) and R13 (webhooks active on our tenants) due | §18 |
| Fri 16 Oct | all day | Tushe R6, R7 and R8 due | §18 |
| **To be confirmed by Tushe** | — | **G0-T**: date to be confirmed by Tushe. One joint session with Tushe (walkthrough, sign-off, then AT-01 to AT-20; ENV-12, ENV-07). The session planned for Fri 16 Oct, 18:00–20:30, did not take place | §3, §8 |
| Tue 20 Oct | all day | Tushe R1 batch 2 (the remaining tenants, to about 10) due | §18 |
| Thu 22 Oct | by end of day | Our request for the G0-T date goes to Tushe (DEC-2026-10-16 E3) | §3 |
| Thu 22 Oct | 17:00 | **G0-N** Phase A exit, Noema half (ENV-14): TEN-01 to TEN-08, `/contracts` v1 tag, fixtures, isolation tests | §3, §8 |
| Fri 23 Oct | all day | Tushe R2 (read surfaces), R3 (seeded histories) and R4 (switch state) due, at the latest | §18 |
| Fri 23 Oct | all day | **G1** evidence run (BEN-05) | §3, §8 |
| Sat 24 Oct | — | Reserve only, called by EL | §3 |
| Mon 26 Oct | before 10:00 | Noema-covered AT exceptions AT-04, AT-05, AT-07 and AT-14 shown internally (internal target) | §3.1 (G0-N) |
| Mon 26 Oct | 10:00 | **G1** Unknown-outcome slice review (GOV-07). Counts only once G0 passes; if G1 has not passed or fewer than 80% of the week-1 P0 tasks have merged, cut-line items 4 and 5 are applied that day (DEC C8) | §3, §9 |
| Fri 30 Oct | all day | Tushe R9 to R12 due (ambiguous name enquiry, approval states, scenario richness, diagnostics view) | §18 |
| Fri 30 Oct | before 16:00 | The two external people for the comparison arms, ARM and REV, engaged under NDA (GOV-21; DEC-2026-10-16 contract-and-pack-clarifications C8) | §3, §4 |
| Fri 30 Oct | 16:00 | **G2** Trust depth; ARM and REV confirmed (GOV-11) | §3 |
| Sat 31 Oct | — | Reserve only, called by EL | §3 |
| Fri 6 Nov | 16:00 | **G3** Hardened | §3 |
| Sat 7 Nov | — | Reserve only, called by EL | §3 |
| Wed 11 Nov | 12:00 | Code freeze: release candidate tagged (REL-01) | §11 |
| Wed 11 Nov | 16:00 | **G4** Comparison and **G5** Voice reviews (GOV-13) | §3, §11 |
| Thu 12 Nov | 18:00 | **G6** Release run review (GOV-16) | §3, §11 |
| Fri 13 Nov | 09:00 | **G7** External readiness: dry run (DEM-02), how G7 is met for the demo (DoD pre-demo items signed at G6) | §3.1, §11 |
| Fri 13 Nov | 13:00 | Demo pre-flight | §14 |
| Fri 13 Nov | 14:00 | Demo (DEM-03) | §3, §11, §14 |
| Fri 13 Nov | 16:00 | POC-done review (GOV-17) | §11 |
| Fri 13 Nov | all day | End of the sandbox no-change window we ask Tushe for (R5 as sent ends Fri 6 Nov; extension requested, DEC-2026-10-16 E3) | §18 |
| Sun 15 Nov | — | The window closes | §1 |
