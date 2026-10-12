# Tushe acceptance (Phase A gate)

This folder holds the Phase A acceptance evidence for the Tushe synthetic environment: the AT-01 to AT-20 pass report and the Noema-side checks TEN-01 to TEN-08 (PERD REQ-ENV-007, SoT §36, §40.1).

## Where each test is defined

- **AT-01 to AT-20** are defined only in the issued, frozen Tushe specification, [`../Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md`](../Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md), §22. The text below is imported verbatim from it. The titles in PERD §34.5 are only a working summary; where they differ, the specification's wording is the test.
- **TEN-01 to TEN-08** are defined in [PERD](../../perd/NOEMA_POC_PERD_v1.2.md) §34.5 [REC]. They are Noema's own checks and are not sent to Tushe.
- **AT-25** (simulated time reported consistently), proposed in [`../tushe-spec-delta-v1.1.md`](../tushe-spec-delta-v1.1.md), is **withdrawn** (12 Oct 2026): Tushe will not run a global clock (DEC-2026-10-12, D3).

## The pass rule (REQ-ENV-007)

Each of AT-01 to AT-20 passes as written, passes under an amended condition signed by both sides, or is covered by an agreed exception naming owner, method and date, recorded in this folder (PERD v1.2 REQ-ENV-007; SoT §36, §40.1). An exception stays an exception in the record; it is never counted as a pass.

Noema-covered exceptions are shown on **Fri 16 Oct 2026**, and their evidence is added to this folder the same day.

## Files in this folder

| File | What it is |
|---|---|
| [`G0-worksheet-2026-10-12-DRAFT.pdf`](G0-worksheet-2026-10-12-DRAFT.pdf) | The acceptance worksheet, **draft for agreement on Tue 13 Oct**. Not signed; not yet sent |
| `G0-worksheet-2026-10-13-SIGNED.pdf` | The worksheet signed by both sides on Tue 13 Oct. Committed as a separate file after the call (plan task ENV-12). Does not exist yet |
| `AT-TEN-report-2026-10-15.md` | The record of the joint session on Thu 15 Oct (plan task ENV-07). Does not exist yet |

## AT-01 to AT-20 (verbatim)

Source: `docs/poc/tushe/Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md`, §22, lines 405–430 (heading on line 405, table on lines 409–430).

> The environment is ready for meaningful integration once these are demonstrated in a joint session. All are P0.

| ID | Test | How we check | Pass condition |
|---|---|---|---|
| AT-01 | Deterministic replay | Run the same scenario twice with the same seed. | Material fault sequence and authoritative outcome reproduce. |
| AT-02 | Ground-truth isolation | Attempt ground-truth access with ordinary credentials. | Access denied. |
| AT-03 | Post-commit timeout | Run commit-then-timeout. | Client sees ambiguity; privileged oracle confirms the actual outcome. |
| AT-04 | Stale state | Write, then read under a stale-state profile. | Read returns the configured prior version; authoritative state stays correct. |
| AT-05 | Event loss | Drop a configured event. | State changes; event absent from normal delivery; diagnostics show the drop. |
| AT-06 | Duplicate event | Duplicate a configured event. | Configured duplicate deliveries occur and are traceable. |
| AT-07 | Out-of-order event | Reorder configured events. | Events arrive in the configured order with sequence metadata intact. |
| AT-08 | Cross-system conflict | Configure ledger/switch/settlement disagreement. | Each source stays independently queryable and contradictory. |
| AT-09 | Ambiguous beneficiary | Run an ambiguous name enquiry. | Multiple/conflicting candidates returned; no silent auto-selection. |
| AT-10 | Idempotency conflict | Reuse a key with a different payload. | Deterministic conflict; no unintended second effect. |
| AT-11 | Retry after timeout | Time out the first request, retry the same key. | Configured business-effect semantics reproduce deterministically. |
| AT-12 | Authorization boundary | Use an authenticated but unauthorized principal. | Action denied, with a traceable reason. |
| AT-13 | Policy mutation | Change policy during a scenario. | Both policy versions and their effective times are traceable. |
| AT-14 | Concurrent update | Modify a resource between read and mutation. | Stale/concurrent mutation detected as documented. |
| AT-15 | Time control | Freeze, then advance the clock. | Scheduled transitions fire according to simulated time. |
| AT-16 | Reset & replay | Reset, then replay a named scenario. | No manual reconstruction required. |
| AT-17 | Ground-truth export | Export a completed run. | Machine-readable scenario/state/event artefacts are produced. |
| AT-18 | Mutation isolation | Attempt a monetary mutation with initial credentials. | Denied unless explicitly enabled. |
| AT-19 | Audit completeness | Inspect a material transition. | Actor / request / correlation / state / timestamp metadata all present. |
| AT-20 | Simulator diagnostics | Trigger an injected fault and a genuine platform error separately. | Privileged diagnostics tell them apart. |

## TEN-01 to TEN-08 (PERD §34.5)

Source: `docs/poc/perd/NOEMA_POC_PERD_v1.1.md`, §34.5, lines 3156–3165, verbatim.

| ID | Check |
|---|---|
| TEN-01 | No runtime container can reach the oracle (network and credential) |
| TEN-02 | A replayed scenario gives identical Trust decisions and verdicts |
| TEN-03 | Every case read returns a version token, and a stale expected version is rejected with no change |
| TEN-04 | A case committed with its response dropped is found by idempotency key |
| TEN-05 | The virtual clock and Temporal test time advance together |
| TEN-06 | Every integration-hostility fault (429, pagination, schema drift, near-timeout, skew) can be produced on demand |
| TEN-07 | Every evidence response carries the provenance fields of §21.1 |
| TEN-08 | The Noema integration credential cannot perform any prohibited operation in Tushe |

## The signed report

The pass report from the joint session is stored here as `AT-TEN-report-<date>.md` (REQ-ENV-007). It lists every AT and TEN result with the run seed and the Tushe version (REQ-ENV-007 acceptance criteria), and is referenced from the release evidence bundle (REQ-BEN-008). No report exists yet.

Do not put benchmark details, hidden test material or held-out cases in this folder or in anything sent to Tushe (AGENTS.md §4).
