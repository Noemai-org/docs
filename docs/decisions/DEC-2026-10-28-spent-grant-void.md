# DEC-2026-10-28 · A SPENT grant becomes VOID only for a confirmed REJECTED_STALE_VERSION refusal

| | |
|---|---|
| **Status** | Accepted in principle by the Founders on 28 October 2026 (Option 1 of the conflict recorded in `noema` pull request 90, with the conditions in §1; decisions given in a working session, so they count once this record is merged). The Technical Co-Founder confirms by approving the pull request that adds it |
| **Date** | 28 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None. Resolves a conflict inside the PERD that was not in [`conflicts-register.md`](../poc/perd/conflicts-register.md) |
| **Amends** | The PERD: a new version, [v1.18](../poc/perd/NOEMA_POC_PERD_v1.18.md) (§38.2, REQ-EXE-001, REQ-EXE-004). `services/core/migrations/` in `Noemai-org/noema`: one new forward-only migration. No SoT text changes |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted in principle by the Founders (see the table above)
- Date: 28 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: REQ-EXE-001, REQ-EXE-004, REQ-AUD-001; INV-03, INV-17, INV-27; US-19; EC-E11; SoT §43.3; PERD §27.1, §28.1, §38.2. No SoT change; the requirement count stays 154
- Migration notes: §4
- Supersedes: none

---

## 1. The decisions

The Founders' instruction of 28 October 2026, recorded as given and as applied:

| | Decision |
|---|---|
| D1 | **Option 1.** The PERD §38.2 `decision_grant` lifecycle permits `SPENT → VOID`, only for a confirmed `REJECTED_STALE_VERSION` refusal. Every other transition out of `SPENT`, `VOID` and `EXPIRED` stays refused. The `decision_grant_guard` trigger is changed by a new forward-only migration, never bypassed |
| D2 | **One transaction.** The receipt, the invalidation of the grant, the RecoveryRequest and the outbox writes happen in one transaction. The Record events `RECEIPT` and `GRANT_VOIDED` are written in it. If any write fails, none is kept |
| D3 | **Audit continuity.** The `GRANT_SPENT` event stays on the Record. `GRANT_VOIDED` follows `RECEIPT`, and its payload names the change from `SPENT` to `VOID`, so the earlier state and the transition stay visible in the Record |
| D4 | **Regression evidence is a condition of merging.** The migration, this amendment, this record and the regression tests (the permitted transition, and every refused transition still refused) are reviewed before the `noema` pull request 90 merges |

## 2. Rationale and evidence

The conflict, quoted from the PERD v1.17 and the SoT (checked 28 October 2026):

> A. PERD REQ-EXE-004: "A version mismatch gives `REJECTED_STALE_VERSION`: the grant is void, the case returns to Trust, and there is no automatic retry." SoT §43.3: "`REJECTED_STALE_VERSION` voids the grant and returns the case to Trust." SoT US-19: "the conditional write is rejected (`REJECTED_STALE_VERSION`), no write is applied, the grant is void". PERD §28.1: "Grant | ISSUED, SPENT, VOID, EXPIRED".
>
> B. PERD §38.2, `decision_grant`: "ISSUED → SPENT, VOID or EXPIRED | Status only (via spend and void)". REQ-EXE-001 Audit: "`GRANT_SPENT` or `GRANT_VOIDED{reason}`". Migration 0001 enforces B with `decision_grant_guard` ("decision_grant: SPENT is final").

The refusal is made at E9, after E8 has spent the grant, so a refused grant is always `SPENT` first. A and B could not both hold. No line supported a grant that is both `SPENT` and `GRANT_VOIDED`. The Founders chose to keep A, change B, and keep the guard in force for everything else.

The exact §38.2 text this record changes (PERD v1.17, the `decision_grant` row, lifecycle column):

> before: `ISSUED → SPENT, VOID or EXPIRED`
>
> after (PERD v1.18): `ISSUED → SPENT, VOID or EXPIRED. SPENT → VOID only for a confirmed `REJECTED_STALE_VERSION` refusal (REQ-EXE-004); every other change of a grant that is SPENT, VOID or EXPIRED is refused`

The other two PERD lines changed are REQ-EXE-001's Audit line and REQ-EXE-004's Expected behaviour (before: "—"), Audit and Tests lines; PERD v1.18 lists them under "Changes in v1.18".

## 3. Agent decisions

1. **What "confirmed" means.** The instruction asks that the transition be permitted "when the receipt carries REJECTED_STALE_VERSION and the outcome check has confirmed that no write was applied". The Outcome verifier is not built (plan task OUT-01) and its read is asynchronous (it runs from the outbox event that `Complete` writes), while D2 requires the void to be in the receipt's transaction. A gate on an Outcome verdict would therefore make D2 impossible. The check the database can make in that transaction is the receipt itself, and PERD v1.18 defines a **confirmed refusal** as a receipt that (a) has execution state `REJECTED_STALE_VERSION`, (b) records the target's version-conflict refusal as its transport result (`VERSION_CONFLICT_409_412`), (c) has no external acknowledgement and (d) is the grant's only receipt. A refused conditional write applies nothing (INV-27; the mock target's contract test shows it), so that is the evidence that no write was applied. Outcome's own read still follows from the outbox event in the same transaction. **This is the one reading the Founders should confirm.** If they want the void to wait for an Outcome verdict, D2 changes: the receipt would be written first and the void in a later transaction, and the transition's precondition would be a recorded verdict.
2. **Payload fields, not a new contract.** `payload` is not part of `record-event.v3.json`; its hash is. The `GRANT_VOIDED` payload therefore carries `from_status`, `to_status` and `receipt_id` without a contract change. The void reason and the event type are unchanged.
3. **The guard is replaced, not bypassed.** The migration uses `CREATE OR REPLACE FUNCTION decision_grant_guard()` and leaves the triggers as they are. Migration 0001 is not edited (forward-only).
4. **Pre-write voids are unchanged** (`ISSUED → VOID`), apart from the payload fields of decision 2.
5. **No conflicts-register entry.** The conflict was never listed there, so there is nothing to close in it.

## 4. Migration notes (AGENT-15)

- **Specification.** PERD v1.18 is a new file; v1.17 and earlier stay unchanged. The current-PERD pointers in [`docs/README.md`](../README.md) and [`poc/perd/README.md`](../poc/perd/README.md) move to v1.18.
- **Vendored copies.** The two PERD extracts in `noema` (`contracts/perd-32-2-event-types.md`, `services/core/orchestrator/perd-28-2-state-machine.md`) name the PERD file, and the other vendored copies name the docs commit, so they are re-pointed in the same session after this record merges (REQ-OPS-005). Their text does not change.
- **Code.** In `noema`: one forward-only migration (`decision_grant_guard` replaced); `ledger.Complete` makes the void in the receipt's transaction; the ledger tests assert `VOID` and every refused transition. No contract file changes. No existing row changes.
- **Nothing is migrated.** No grant exists outside tests and throwaway databases (checked 28 October 2026: the writer is not wired into `cmd/core`).

## 5. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted in principle, with conditions | 28 October 2026 | Working session, summarised here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
