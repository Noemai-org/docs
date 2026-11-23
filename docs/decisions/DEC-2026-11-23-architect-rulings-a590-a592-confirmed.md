# DEC-2026-11-23 · Architect rulings A590 to A592, in full (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Nothing new. It records the Architect's full text of A590, A591 and A592. |
| **Supersedes** | **The shorter text of A590, A591 and A592** in `DEC-2026-11-23-architect-rulings-a581-a592` (merged in docs#234 at `f2b2c65`), which the Steward recorded from a shorter relay. The meaning is the same; this record adds points the first text left out. **Where the two texts differ, this record governs.** The merged record is not edited. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: the full text of A590 to A592
- Decision: §1
- Rationale and evidence: the Architect's confirmation of 23 Nov 2026, relayed to the Steward after docs#234 had merged
- Affected requirement IDs / SoT sections: INV-02, INV-12; AGENT-09; `decision-record.v2`, `clarification.v1`; migration 0039
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. Migration 0039 is in A592's PR A (ledger on noema#183, unchanged).

## 1. The rulings, in full

### A590 (interim, early-decision key). Confirmed.

The key includes the tenant and the verified principal, as well as the turn (request id), intent hash, pack version, outcome and reason. Without them, one principal could replay another's request id and read their stored decision.

- A replay returns the stored record only when every one of those matches.
- Any mismatch is a new evaluation and a new record.
- Both identity values come from the authenticated session, never from the request (INV-12).

### A591 (interim, answering a SLOT card). Confirmed, with the safety properties made explicit.

- **Untrusted text.** The answer is ordinary untrusted text. It goes through the same intake and schema gate as any turn (INV-02, AGENT-09) and only supplies a slot value for Trust to evaluate again. It never binds anything directly.
- **Bound to the card.** The answer must reference the clarification it answers, come from the same session and principal, and be used once. An expired card is refused.
- **Question text.** It comes from pack templates, in plain language with no internal codes, and is labelled SYNTHETIC.

### A592 (interim, order for the verified-issuer change). Two PRs, not one.

- **PR A lands first.** It adds the nullable column (migration 0039), C2's store change and EL's gateway writer.
- **PR B lands only after PR A merges.** It turns on the recovery refusal.
- **Why two.** One PR leaves a window where `main` refuses rows the running stack just wrote. Two PRs make that impossible.
- **Legacy rows.** Rows written before the writer landed are refused or left for a person. They are never given an invented issuer.

## 2. What the Steward did

- **What the first text left out.** The merged record (docs#234) had the three rulings in a shorter form. This record adds: for A590, that any mismatch is a new evaluation and a new record, that the reason for the rule is cross-principal replay, and that both identity values come from the authenticated session and never from the request (INV-12); for A591, that the answer "never binds anything directly" and only supplies a slot value for Trust to evaluate again (INV-02, AGENT-09); for A592, the reason for two PRs (a window in which `main` refuses rows the running stack just wrote).
- **Nothing else changes.** The A592 line in the merged record "No change request for the STM-01 title. A467 stays blank." was part of the first relay and is not repeated here; it stands in `...-a581-a592`.
- **Migration ledger on noema#183:** unchanged (0037 DEBT-54, 0038 A574, 0039 A584 in PR A; next free 0040).
- **Next free ruling: A593** (unchanged).
