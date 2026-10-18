# DEC-2026-10-18 · CON-01 gap closure: seven decisions found while building the contract schemas

| | |
|---|---|
| **Status** | Accepted by the Founders on 18 October 2026 (written instruction to the coding agent). The Technical Co-Founder confirms by approving the pull request that adds this record |
| **Date** | 18 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | The open questions raised in the CON-01 pull requests noema#9, #10, #11 and #12 ("Founder actions"): the clarification-answer fields, the recovery request for a voided grant, the event table, the Record event ID prefix, the idempotency-key form, the retryable error codes, and whether an ALLOW needs three PASS layers |
| **Amends** | SoT §43.3 and §43.6 examples (SoT v1.9); PERD REQ-TRU-001, REQ-VER-003, REQ-AMB-005, §32.2 and §39.1 (PERD v1.9) |
| **Authority order applied** | SoT → decision records → PERD → plan. Where an example disagrees with an adopted PERD value or with the committed golden vectors, the PERD and the vectors win, in that order |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the Founders (see the table above)
- Date: 18 October 2026
- Closes: the open questions listed above
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1, and the correction in §2
- Rationale and evidence: the CON-01 pull requests (noema#9 to #12) and the verification in the pull request that adds this record
- Affected requirement IDs / SoT sections: SoT §43.3 and §43.6 (SoT v1.9); PERD REQ-TRU-001, REQ-VER-003, REQ-AMB-005, REQ-VOI-004, REQ-API-007, REQ-API-008, REQ-OPS-003, §32.2, §39.1 (PERD v1.9). The requirement count (153) and every invariant are unchanged
- Migration notes: the `noema` contracts follow in the CON-01 C-5 and C-6 pull request, which applies these decisions to the schemas and fixtures (`/contracts` v1 is not tagged and holds no data)
- Supersedes: None

---

## 1. The decisions

| Gap | Decision |
|---|---|
| ALLOW and the authority layers | An ALLOW decision requires **all three** authority layers at `PASS`. `FAIL` or `NOT_EVALUATED` on any layer makes ALLOW invalid (fail-closed). |
| Recovery request for a void grant | `verdict_id` is required unless the trigger is a voided grant. In that case `grant_id` is required and `verdict_id` must be absent. |
| Clarification answer | The answer carries the base fields every object carries plus `clarification_id`. It also carries `answers`, a map from each slot name the clarification requested to a value that validates against that slot's type in the Intent Object schema. Unknown slot names are rejected. No other field is defined. |
| Retryable error codes | An error is retryable **only if** sending the identical request again can succeed with no change by the caller (transient: unavailable, timeout, rate-limited, dependency down). Every decision or reason code, every validation error and every authorization error is **non-retryable**. |
| Record event ID prefix (`rec_1001` or `recev`) | The PERD wins: `recev` (PERD §32.3). The SoT §43.6 example is corrected (SoT v1.9). |
| Idempotency-key form (`idk_v1_sha256:…` or the PERD) | The encoding in `contracts/fixtures/golden_vectors.json` and PERD §27.2 wins, in that order: `idk_v1_` plus 64 lower-case hex characters. The SoT §43.3 example is corrected (SoT v1.9). |
| Event types the PERD uses but §32.2 omits | They are added to the §32.2 table, each citing the requirement that uses it (see §2 for which ones). |

**Retryable codes.** Applying the rule to the error catalogue of PERD §39.1: `EVIDENCE_UNAVAILABLE`, `TARGET_RATE_LIMITED`, `TARGET_TIMEOUT`, `PROVIDER_UNAVAILABLE` and `DEPENDENCY_UNAVAILABLE` are retryable. Every other code is non-retryable, including `CALLBACK_DELIVERY_FAILED` (the callback's own 12-attempt budget is already spent when it is raised; PERD REQ-VER-005). A retryable error never overrides a capability's retry-safety class: a write is retried only under a new grant (AGENT-08).

## 2. Correction from the evidence: three of the seven strings are not Record event types

The instruction listed seven strings as event types missing from §32.2. Reading each requirement line that uses them:

| String | Used by | What it is |
|---|---|---|
| `AUDIO_RETAINED` | REQ-VOI-004 | A Record event |
| `INBOUND_EVENT_RECEIVED` | REQ-API-008 | A Record event |
| `RESOLUTION_POSTED` | REQ-API-007 | A Record event |
| `CONFIG_CHANGED` | REQ-OPS-003 | A Record event |
| `INTENT_SUPERSEDED` | REQ-INT-004 | The reason carried by `GRANT_VOIDED` (`GRANT_VOIDED` reason `INTENT_SUPERSEDED`) |
| `STATE_CHANGED` | REQ-RES-004 | The reason carried by `GRANT_VOIDED` |
| `RECORD_ACCESSED` | REQ-AUD-003 | An access-log entry: "in the access log, not the chain" |

Adding the last three to the Record event list would put void reasons and an access-log entry into the hash chain's vocabulary, contradicting the requirement lines that define them. So **only the four Record events are added to §32.2**; the other three keep the role their requirements give them. This keeps the PERD consistent with itself, which is the rule for anything the instruction does not settle.

## 3. What this does not change

- Every invariant, every gate and the 153 requirements.
- The money rules (DEC-2026-10-16 money-and-value-lists) and the two-tier reason codes.
- `/contracts` v1 stays untagged until the schemas are complete.

## Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Approved | 18 Oct 2026 | Written instruction to the coding agent |
| Technical Co-Founder | Confirms | Date of approval | Approving review on the pull request that adds this record |
