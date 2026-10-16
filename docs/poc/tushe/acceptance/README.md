# Tushe acceptance (Phase A gate)

This folder holds the Phase A acceptance evidence for the Tushe synthetic environment: the AT-01 to AT-20 pass report (PERD REQ-ENV-007, SoT §36, §40.1). Noema's own checks are internal and are recorded elsewhere (below).

## Where each test is defined

- **AT-01 to AT-20** are defined only in the issued, frozen Tushe specification, [`../Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md`](../Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md), §22. The text below is imported verbatim from it. The titles in PERD §34.5 are only a working summary; where they differ, the specification's wording is the test.
- **TEN-01 to TEN-08** are Noema's own checks, defined in the current PERD §34.5 [REC]. They are internal and are not sent to Tushe. Their wording and results are kept outside this folder, in the [G0-N gate record](../../execution/gates/G0-N.md) (DEC-2026-10-16 E4).
- **AT-25** (simulated time reported consistently), proposed in [`../tushe-spec-delta-v1.1.md`](../tushe-spec-delta-v1.1.md), is **withdrawn** (12 Oct 2026): Tushe will not run a global clock (DEC-2026-10-12, D3).

## The session

One joint session with Tushe: walk through the worksheet, agree and sign it, then run the acceptance tests against it and sign the record (worksheet section 7). It was planned for **Fri 16 Oct 2026, 18:00–20:30 WAT** and is **postponed**: Tushe has not confirmed a new date, and this README records none. This is the Tushe half of G0 (G0-T); G0 passes only when G0-T and the Noema half (G0-N) both pass (DEC-2026-10-16 E4).

## The pass rule (REQ-ENV-007)

Each of AT-01 to AT-20 passes as written, passes under an amended condition signed by both sides, or is covered by an agreed exception naming owner, method and date, recorded in this folder (PERD REQ-ENV-007; SoT §36, §40.1). An exception stays an exception in the record; it is never counted as a pass.

## Who covers what

The worksheet records each test as Pass, Pass amended, Noema covers or Tushe by date (worksheet section 2).

| Outcome | Tests |
|---|---|
| **Noema covers** | AT-04, AT-05, AT-07, AT-14 and AT-17. Noema shows these to Tushe once each is complete |
| **Tushe, by date** | AT-09 (Fri 30 Oct), AT-19 (Fri 23 Oct) and AT-20 (Fri 30 Oct; Tushe's simulated-fault markers are the interim, shown Fri 16 Oct) |

## Files in this folder

| File | SHA-256 | What it is |
|---|---|---|
| [`G0-worksheet-2026-10-13-SENT.pdf`](G0-worksheet-2026-10-13-SENT.pdf) | `842bc6b4a402cd3eb75f9281bf4234718f12835df83a2f11dcca0dd087a4f56d` | The acceptance worksheet **as sent to Tushe on 13 Oct 2026**. **This PDF is the record.** Frozen record (listed in `tools/frozen-files.sha256`); not signed |
| [`G0-worksheet-2026-10-13-SENT.md`](G0-worksheet-2026-10-13-SENT.md) | `7c8d5986c3f90422dcaee6e8b444db2d555b1c8d34e21aae8e2c9783c27bbf52` | A Markdown source copy. Its text matches the PDF (layout differs). It has not been verified byte for byte against what was sent, so it is **not** a frozen record and is not on the frozen list. If it disagrees with the PDF, the PDF is right |
| [`G0-worksheet-2026-10-12-DRAFT.pdf`](G0-worksheet-2026-10-12-DRAFT.pdf) | `7a2339ece9e24e67391c3f3a5520b216d96986c725c34abfad3dfcc37244e1d9` | **Superseded draft, never sent.** Superseded by the 13 Oct worksheet above. Kept unchanged |
| `G0-worksheet-<date>-SIGNED.md` and `G0-worksheet-<date>-SIGNED.pdf` | — | The worksheet signed by both sides at the joint session (date to be confirmed by Tushe), in Markdown and PDF. Committed as separate files after the session (plan task ENV-12); the sent copy is never overwritten. Do not exist yet |
| `AT-report-<date>.md` | — | The record of the joint session (plan task ENV-07, G0-T). Does not exist yet |

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

## The signed report

The pass report from the joint session is stored here as `AT-report-<date>.md` (REQ-ENV-007). It lists every AT result with the run seed and the Tushe version, and is referenced from the release evidence bundle (REQ-BEN-008). The Noema-side TEN results are not recorded here (see above). No report exists yet.

Do not put benchmark details, hidden test material, TEN details or held-out cases in this folder or in anything sent to Tushe (AGENTS.md §4).
