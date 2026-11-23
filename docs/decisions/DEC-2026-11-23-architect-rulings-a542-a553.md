# DEC-2026-11-23 · Architect rulings A542 to A553 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A542 to A553 (§1), every one Interim. A541 is noted (§2). |
| **Supersedes** | **A551 amends A475 and A512** (the accessor count rule goes). **A552 settles** the confirmation request row (follows A519) and removes the standalone creator. **A553 confirms** A548's reading. **A547 adds a lane 5** to the four lanes of A537 (`DEC-2026-11-23-architect-rulings-a534-a540`). **A548** names the key and login variables for the core-trust Record signing keys. **A543** changes the Writes port. Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A542 to A553
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-03, INV-07, INV-14, INV-21, INV-29; AGENT-15, AGENT-16, AGENT-25; REQ-AMB-003, REQ-TRU-010; PERD §23, §32; AGENTS §5, §8
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A543, A550 and A552 (C1's confirmation contract and the Writer's insert) may need additive contract changes with the AGENT-15 steps, in the same PR as the change. A544 adds a pack data kind (an additive limits kind, like #879).

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

### A551 (interim, pack accessors; amends A475 and A512).

- The count rule goes. A475 allowed one accessor and A512 a second, and `OwnershipKinds()` and `Ref()` are already on `main`, so the number is dead. It only ever stood in for the real intent: the verified `Pack` must not grow an API that reads anything but the verified bytes.
- **The new rule.** A475 and A512 are amended. Any number of accessors is allowed on a verified `Pack` if each one meets all five conditions:
  1. It is read-only.
  2. It derives only from the verified pack bytes, with no file, network or database access after verification.
  3. It returns copies or immutable values.
  4. It contains no industry or country terms (INV-14).
  5. It is named in a ruling or in the PR body, with a test that a pack failing verification yields no accessor.
- **Ratified** under the same rule: `OwnershipKinds()` and `Ref()`.
- The hard cap with a separate reader type is rejected. It is more code for no extra safety.

### A552 (interim, the confirmation request row; follows A519).

- **The Writer owns it.** The Recorder persists the new confirmation request in the same transaction as the CONFIRM decision. The Writer does not do that today, and that gap is why the A519 test cannot pass. C1 fixes it in the Writer.
- **Writer behaviour:** the Writer inserts the row using the store's transaction-bound insert, takes the time-to-live from the database clock, keeps the supersede-chain constraint, and returns the request id with the decision. The decline then carries that id as `DeclinedRequestID`, which A542 requires.
- **No standalone creator.** `Requests.Create` stops being a public creator. A request that exists without a recorded decision breaks "the Record comes first". The store keeps its read, answer and expire paths.
- **Re-request after expiry** is a new CONFIRM decision through the Recorder, not a bare `Create`. C1 greps every caller of `Create`. A caller that is not a test either moves to the Recorder path or is refused.
- **Test:** a CONFIRM through the real adapter leaves exactly one open request, and a crash between the decision and the request leaves neither.

### A553 (interim, A548 confirmed).

A548 changes nothing in AGENTS §6. Grants and confirmations stay HMAC-SHA-256, and the ed25519 keys sign Record events only. Uid 65532 must be the core's runtime user, and IL pins that in `deploy/`. EL checks first whether a Go-side signing key directory is needed at all, because decision records may be signed in the database.

## 2. What the Steward did, and where the rulings are silent

- **A541** (docs#229 era) was cross-role reads. That is all the Architect gave; the Steward records no more and does not guess its text. It is named here so the sequence A534 to A550 has no gap.
- **A537 and A547.** A537's four lanes are in `DEC-2026-11-23-architect-rulings-a534-a540`. A547 adds a lane 5 (the Execution Controller and the Outcome request builder), owned by C1 with EL integrating the ports, on the G1 critical path. What each lane holds beyond A547's lane 5 was not relayed and is not listed here.
- **A542.** #892, #733 and #882 are noema pull requests. A542's #733 rule follows A534's rescope; the new check is C1's. The Steward changes no code.
- **A543 and A550.** A port change in `trust/intake` and any missing confirmation contract are C1's, with the AGENT-15 steps (a version bump, a migration note and regenerated models) where a contract changes.
- **A544.** The Steward fills no pack value. `limits/trust_limits.json` and its values are C2's; a value the PERD and the SoT do not state is an [OPEN] entry in `docs/open-decisions.md` with the safest default (nothing allowed under freeze; no route means UNKNOWN). Nobody invents a value (AGENT-02, AGENT-16).
- **A546.** The PERD table lists REQ-AMB-003 (deterministic scoring from pack weights) under Understanding (deterministic code, no model), which fits A546's "where the PERD places it". The Steward raises no conflict. C2 reads REQ-AMB-003 and raises a CONFLICT block if the placement differs. All SYNTHETIC labels are required (AGENT-25).
- **A548.** The Steward changes no Compose value; IL adds the mounts. A new key directory or login is also a secrets-handling path, so SR reads it.
- **A542 and noema#892.** The Architect's message says #892 is still open, so the empty-`DeclinedRequestID` fix goes in #892 itself. GitHub shows noema#892 **merged** (11:43 UTC, 23 Nov 2026, by a Founder, no related PR open), so it cannot be fixed in place. The Steward records the fact: the empty-id fix is EL's small follow-up PR, tests first, and A542 is not read as closed until that fix merges with its test. If the Architect means another PR, EL names it.
- **A548 and A553.** A553 confirms the Steward's reading of A548 (grants stay HMAC; the ed25519 keys sign Record events only; uid 65532 must be the core's runtime user, pinned by IL in `deploy/`; EL first checks whether a Go-side signing key directory is needed at all). noema#884's shared reader checks the owner against the process's effective user.
- **A550 and the accessor limit.** Settled by A551: the count rule goes; any number of accessors on a verified `Pack`, each meeting the five conditions; `OwnershipKinds()` and `Ref()` ratified. EL names each accessor A550 gives in the PR body, with its verification test.
- **A519 and the request row.** Settled by A552: the Writer inserts the row in the CONFIRM decision's transaction (C1); no standalone `Requests.Create`; C1 greps every caller; the crash test. EL's A519 end-to-end test follows C1's Writer change.
- **A549.** A `/readyz` change is Platform's; no spec edit here.
- **Task status (`tasks.csv`).** Unchanged: it moves only on merged evidence, and nothing new has merged against a done-when since the OPS-24 pass (UND-17 → Done). The Steward rechecks in the next status pass.
- **Migration ledger on noema#183** is unchanged: 0037 stays reserved; these rulings add none.
- **Next free ruling: A554.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-architect-rulings-a530-a533` | A530 to A533 | |
| `DEC-2026-11-23-architect-rulings-a534-a540` | A534 to A540 (A474's follow-up is A488) | |
| A541 | cross-role reads (no further text) | |
| This record | A542 to A553 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank); A537 lane contents beyond lane 5 | **A554** |
