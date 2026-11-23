# DEC-2026-11-23 · Architect rulings A542 to A550 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A542 to A550 (§1), every one Interim. A541 is noted (§2). |
| **Supersedes** | **A547 adds a lane 5** to the four lanes of A537 (`DEC-2026-11-23-architect-rulings-a534-a540`). **A548** names the key and login variables for the core-trust Record signing keys. **A543** changes the Writes port. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A542 to A550
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-14, INV-21, INV-29; AGENT-15, AGENT-16, AGENT-25; REQ-AMB-003, REQ-TRU-010; PERD §23, §32; AGENTS §5, §8
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A543 and A550 (C1's confirmation contract) may need additive contract changes with the AGENT-15 steps, in the same PR as the change. A544 adds a pack data kind (an additive limits kind, like #879).

## 1. The rulings

### A542 (interim, three review findings).

- **#892:** a `DECLINED_BY_APPROVER` reject must always name a valid `DeclinedRequestID`, and every other shape refuses the field. An empty id is refused.
- **#733:** a disposition must belong to the action decision's own intent (by intent hash), not only its tenant. C1 adds the check, with a test for a same-tenant different-intent disposition.
- **#882:** Codex's finding is not accepted. A490 says the sweep names and counts un-resumed rows, so an internal investigation id in the report is intended. A role or `authn_ref` value never appears in it. No follow-up PR.

### A543 (interim, the Writes port).

The Writes port takes the resolved slot values: `MayWrite(ctx, intent-with-slot-values)`. C1 changes the port in `trust/intake`, and EL's adapter follows.

### A544 (interim, Reconciler and Clocks routing).

The Reconciler and Clocks routing is pack data, owned by C2. C2 pins `limits/trust_limits.json` in the manifest (an additive limits kind, like #879). C2 fills each escalation reason per classification, `AllowedUnderFreeze`, phase routing and the anchor-to-entity mapping from the committed PERD and SoT text. Any value the documents do not state becomes an OPEN entry with the safest default: nothing allowed under freeze, and no route means UNKNOWN. Nobody invents a value.

### A545 (interim, ListEntities).

`ListEntities` needs no new decision. EL builds it from C2's mapping descriptors (`ScopeFromDescriptors`, the `fin.map.v1@2` list entities).

### A546 (interim, Candidates).

Candidates follows PERD REQ-AMB-003. C2 reads it and builds the deterministic ranker where the PERD places it (no provider call). EL builds the Reader (the merged portread case list, #830) and the Labeller. C2 adds the pack data (attribute order and label templates, SYNTHETIC), and any value mask follows the digit-run rule. If the PERD places ranking elsewhere, it is a CONFLICT block, not a guess.

### A547 (interim, lane 5).

Nobody composes the Execution Controller (ledger, dispatcher, receipt signer) or the Outcome request builder. That is a new lane 5, owned by C1, with EL integrating the ports. It is on the G1 critical path.

### A548 (interim, key directories and logins).

For the core-trust Record signing keys and the write login, use the names already in #881 (`NOEMA_TRUST_DSN_DIR`, `NOEMA_GRANT_KEY_DIR`). If a Go-side signing key directory is also needed, mirror the orchestrator pattern: `NOEMA_TRUST_KEY_DIR` and `NOEMA_TRUST_KEY_MAX_ACTIVE`, with `core-trust.ed25519.<n>.key` at mode 0400 owned by uid 65532. IL adds the mounts.

### A549 (interim, startup recovery).

The startup recovery pass may run in the background and gate `/readyz`. Plain "recovery" becomes a `missing()` line.

### A550 (interim, owners of the missing pieces).

- **C1:** the confirmation request-by-id read and any missing confirmation contract.
- **EL:** the pack confirmation-terms accessor, the registry accessor, and the plangraphs inputs.
- **C2:** `StepFactSource` (from the sealed-snapshot reader) and the explainer's facts source.
- **EL:** the recovery Postgres reader.

## 2. What the Steward did, and where the rulings are silent

- **A541** (docs#229 era) was cross-role reads. That is all the Architect gave; the Steward records no more and does not guess its text. It is named here so the sequence A534 to A550 has no gap.
- **A537 and A547.** A537's four lanes are in `DEC-2026-11-23-architect-rulings-a534-a540`. A547 adds a lane 5 (the Execution Controller and the Outcome request builder), owned by C1 with EL integrating the ports, on the G1 critical path. What each lane holds beyond A547's lane 5 was not relayed and is not listed here.
- **A542.** #892, #733 and #882 are noema pull requests. A542's #733 rule follows A534's rescope; the new check is C1's. The Steward changes no code.
- **A543 and A550.** A port change in `trust/intake` and any missing confirmation contract are C1's, with the AGENT-15 steps (a version bump, a migration note and regenerated models) where a contract changes.
- **A544.** The Steward fills no pack value. `limits/trust_limits.json` and its values are C2's; a value the PERD and the SoT do not state is an [OPEN] entry in `docs/open-decisions.md` with the safest default (nothing allowed under freeze; no route means UNKNOWN). Nobody invents a value (AGENT-02, AGENT-16).
- **A546.** The PERD table lists REQ-AMB-003 (deterministic scoring from pack weights) under Understanding (deterministic code, no model), which fits A546's "where the PERD places it". The Steward raises no conflict. C2 reads REQ-AMB-003 and raises a CONFLICT block if the placement differs. All SYNTHETIC labels are required (AGENT-25).
- **A548.** The Steward changes no Compose value; IL adds the mounts. A new key directory or login is also a secrets-handling path, so SR reads it.
- **A549.** A `/readyz` change is Platform's; no spec edit here.
- **Task status (`tasks.csv`).** Unchanged: it moves only on merged evidence, and nothing new has merged against a done-when since the OPS-24 pass (UND-17 → Done). The Steward rechecks in the next status pass.
- **Migration ledger on noema#183** is unchanged: 0037 stays reserved; these rulings add none.
- **Next free ruling: A551.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-architect-rulings-a530-a533` | A530 to A533 | |
| `DEC-2026-11-23-architect-rulings-a534-a540` | A534 to A540 (A474's follow-up is A488) | |
| A541 | cross-role reads (no further text) | |
| This record | A542 to A550 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank); A537 lane contents beyond lane 5 | **A551** |
