# DEC-2026-11-21 · Architect rulings A502 to A506 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 21 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 21 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A502 to A506 (§1). |
| **Supersedes** | **A502 corrects A476** (`DEC-2026-11-20-architect-rulings-a469-a485`): no audit principal is seeded. **A503 settles** the conflict on noema#733 between the PR and PERD §23.1 / REQ-TRU-010. **A504 settles** the route request of noema#785. **A505 lifts** the hold FE had under "A176" and states the flow for a red run. **A506 gives** the Compose values read from the code. Otherwise per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 21 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A502 to A506
- Decision: §1
- Rationale and evidence: the Architect's message of 21 Nov 2026, relayed to the Steward; for A506, the code read at the heads of noema#838, `main` and noema#847
- Affected requirement IDs / SoT sections: INV-03, INV-12, INV-17, INV-21, INV-25, INV-29; AGENT-11, AGENT-13, AGENT-16; REQ-TRU-009, REQ-TRU-010, REQ-STM-001, REQ-SEC-009; PERD §23.1, §23.3; SoT §43.2a; conflicts register SOT-C-04
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A503 may need a contract minor bump with a migration note if `disposition_decision_id` is not in the contract (C1 confirms; AGENT-15).

## 1. The rulings, as given

### A502 (interim, corrects the Architect's A476).

No audit principal is seeded. The core verifies stateless synthetic-IdP tokens, and a random usr_ principal with role audit is accepted. reread.py uses IdpSessionProvider(...).token_for(probe_principal(), ["audit"]), the same as run.py. It drops --audit-credential-file.

*Supersedes or changes:* corrects **A476** ("The reader is an audit principal, seeded in the stack's tenant init").

### A503 (interim, noema#733 CONFLICT).

PERD §23.1 and REQ-TRU-010 say an ESCALATE disposition is its own Trust decision, and each escalation write step is its own action decision that references it. So the Writer's rule stays: a decision with escalation-set steps must link a disposition.

The production path changes. intake.RecordRequest gains an optional DispositionDecisionID. EL's escalation path first records the ESCALATE disposition (no steps, no grant) through the Recorder, which returns its id (A470). It then passes that id on each escalation action decision.

BO's expected Record events for US-06 include the disposition decision first.

The record already has disposition_decision_id. C1 confirms it is in the contract, and adds a minor bump with a migration note if it is not.

### A504 (interim, noema#785 route request).

A grant binds one capability, one target, one parameter hash and the plan step. RouteRequest carries only case_id and owner_queue, both bound inside the route step's parameter hash. VersionToken is read fresh by Execution at dispatch, so it is removed. CreateReceiptID is removed, because case_id comes from the verified create outcome. If code shows another field is needed, it goes inside the hash with a test, never outside it.

### A505 (interim, flow).

- There is no rule that delays a push. FE's "A176" hold is lifted: push your four local fixes now.
- If a red run has not produced a result within 20 minutes, record the local red once (A455) and push the green.
- Dependent work goes into one PR as separate commits. Nobody waits to base a PR on another.

### A506 (interim, Compose values, from the code).

These come from the code read at the heads of noema#838, main and noema#847.

**DSN directories:** one file per tenant, named exactly the tenant id (ten_xx), no extension. The logins are `record_read__<tenant>` for NOEMA_RECORD_READ_DSN_DIR, `orchestrator_rw__<tenant>` for NOEMA_ORCHESTRATOR_DSN_DIR (it also requires NOEMA_READ_TIMEOUT_MS=2000), and `record_emitter__<tenant>__core-edge` for NOEMA_EDGE_DSN_DIR. The loader checks no mode or owner for DSN files.

**Key directories:**

- File names are core-workflows.ed25519.1.key and core-edge.ed25519.1.key.
- Each file is a 64-hex-character seed with at most one trailing newline, mode exactly 0400, owned by the core's uid (the repo convention is 65532).
- NOEMA_ORCHESTRATOR_KEY_MAX_ACTIVE=2 and NOEMA_EDGE_KEY_MAX_ACTIVE=2.
- Input hash key: NOEMA_INPUT_HASH_KEY_FILE is at least 32 bytes after trimming, mode 0400, owner the core's uid. 64 hex characters work.

**Temporal:**

- NOEMA_TEMPORAL_NAMESPACE=default, the namespace auto-setup creates.
- NOEMA_TEMPORAL_TASK_QUEUE=noema-investigations, which the worker and the starter both read.
- NOEMA_TEMPORAL_TLS_CA_FILE is required and comes from secrets/tls/ca.crt.
- _CERT_FILE and _KEY_FILE stay unset (an optional pair, per A310 and DEBT-46).

**Escalation graph:** NOEMA_TRUST_ESCALATION_GRAPH=fin.graph.escalate, the graph_id in g2_escalate.json.

**NOEMA_WRITE_SWAP_DECISIONS:** a test-only switch for the proposer-swap fixture, never a Compose setting. Don't add it.

**Recorder settings:** NOEMA_TRUST_GRANT_LIFETIME_MS, NOEMA_TRUST_RECORD_LIFETIME_MS and NOEMA_TRUST_TX_TIMEOUT_MS, in whole milliseconds. EL states the values in noema#847's body (A475). The grant lifetime must not exceed the record lifetime, and EL's loader refuses it if it does.

## 2. What the Steward did, and where the rulings are silent

- **A502 corrects A476.** The merged record `DEC-2026-11-20-architect-rulings-a469-a485` is not edited; this one says A476's last bullet ("The reader is an audit principal, seeded in the stack's tenant init") is corrected. The rest of A476 (the restart-based recovery, `after_recovery`, `after_replay`, the oracle never used) stands.
- **A503 and the conflicts register.** The conflict is the one the register already lists as **SOT-C-04** (ESCALATE against grant issuance; the register's own answer is a linked disposition and action decisions). A503 chooses the production-path change (an optional `DispositionDecisionID`; the disposition recorded first through the Recorder, A470) and keeps the Writer's rule. The register is derived and is not edited by the Steward; the PERD §23.1 and REQ-TRU-010 text is unchanged. "C1 confirms `disposition_decision_id` is in the contract" is C1's; if it is not, the AGENT-15 steps apply (a version bump and a migration note), and the Steward registers any migration number on noema#183.
- **A506 and the settings rule (A330).** The Recorder settings (`NOEMA_TRUST_GRANT_LIFETIME_MS`, `NOEMA_TRUST_RECORD_LIFETIME_MS`, `NOEMA_TRUST_TX_TIMEOUT_MS`) have no value in this ruling: "EL states the values in #847's body (A475)". The Steward writes none. A475 says that where neither the PERD nor `trust_limits.json` names a value, 60 s, 60 s and 10 s are bench-only values, with the gap written in the PR for the Founder; this is not repeated as a ruling here.
- **A505.** "FE's A176 hold" is lifted. The Steward holds no text of an "A176" hold (A176 is `DEC-2026-11-12-architect-interim-a176`); it records the lift as given.
- **Close-out, as the Architect asked, checked against GitHub on 21 Nov 2026:**
  - **Merged:** noema#843 (11:22 UTC), #789 (13:07), #773 (12:44), #815 (10:50), #827 (12:58). Confirmed.
  - **noema#866 and noema#863: still OPEN** on GitHub when checked. The instruction says they were closed as redundant; they are redundant (noema#865 and noema#862 are merged and fixed the same breaks), but the Steward did not close them and finds them open. Their authors close them.
- **Task status follows merged evidence only.** No `tasks.csv` status changes in this record: UND-04 and TRU-02 are already Done; CON-07 stays In progress (its "done when" is longer than noema#815 alone, which the Steward has not checked line by line); TRU-10 and TRU-12 are not touched by a merge. **There is no `tasks.csv` row for STM-05** (noema#843 and #789 carry that ID in their titles): a task row needs a plan version and a change request, and the Steward opens one when told the row's text (the Founder's and EL's earlier "task rows for new IDs").
- **Migration ledger on noema#183:** noema#843 has merged, so **0036 is on `main`**; 0037 stays reserved for DEBT-54; 0032 (noema#756) is still open. Updated there with this record.
- **Next free ruling: A507.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-architect-rulings-a358-a453` | A358 to A362, A380 to A453 | |
| `DEC-2026-11-20-architect-rulings-a454-a467` | A454 to A466 | |
| `DEC-2026-11-20-architect-rulings-a469-a485` and `DEC-2026-11-20-architect-a468-and-a480-corrected` | A468; A469 to A485 | |
| `DEC-2026-11-21-architect-rulings-a489-a492` | A489 to A492 | |
| `DEC-2026-11-21-architect-rulings-a493-a500` (docs#221, open) | A493 to A500 | |
| This record | A502 to A506 (A501 not received) | |
| Named without text | A467, A474 follow-up, A475 conditions, A476 wording, A486, A487, A501 | **A507** |
