# DEC-2026-10-29 · A failed receipt signature alerts a human: the behaviour the next PERD version must define

| | |
|---|---|
| **Status** | **Proposed** by Session A on the Founders' instruction of 29 October 2026 (given in a working session, so it counts once this record is merged). It defines behaviour only. **The recipient and the delivery channel are placeholders for the Founders to confirm.** Nothing here is implemented |
| **Date** | 29 October 2026 |
| **Owner** | EL (accountable); SR reviews the rule and its fixture |
| **Closes** | None. Keeps DEBT-02 open ([`debt.md`](../poc/execution/debt.md)) |
| **Amends** | The next PERD version (the sections in §3). PERD v1.18 is not edited. No SoT text changes. [`DEC-2026-10-28-spent-grant-void`](DEC-2026-10-28-spent-grant-void.md) §7 is extended, not changed |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Proposed (see the table above)
- Date: 29 October 2026
- Owner: EL (accountable); SR reviews
- Decision: the five rules in §2
- Rationale and evidence: §1
- Affected requirement IDs / SoT sections: REQ-SEC-005, REQ-AUD-001, REQ-EXE-004, REQ-OBS-001; EC-X09, EC-E16; TM-17; INV-11 (not applicable); SoT §13.1, §47.4, §49. No SoT change
- Migration notes: §5
- Supersedes: none
- Decides: the behaviour only; opens OD-P-71 for the placeholders

---

## 1. Why

The Founders require that **a human is alerted when a receipt signature fails**. Today it is not met. A failed verification appends one `SECURITY_EVENT` `SIGNATURE_INVALID` to the Record ([`DEC-2026-10-28`](DEC-2026-10-28-spent-grant-void.md) §7). Nothing reads it and tells anyone. PERD v1.18 REQ-SEC-005 says verification failures "raise an alert"; EC-X09 says "security alert"; TM-17 names the `SECURITY_EVENT`. None of them defines who is told, how, or what happens when the event or the alert cannot be written or delivered. The alert list of PERD §44.1 has no entry for it, and `ops_alert` and `OPS_ALERT_RAISED` (PERD §38.2, §32.2) are not built. **A `SECURITY_EVENT` record or a log line is not a successful alert.**

The PERD has no proposed version to amend: the only proposed PERD v1.19, in `docs#71`, is closed and unmerged, and its branch belongs to another session. This record therefore carries the exact text for the next PERD version. It creates no PERD file, so it cannot collide with the receipt-verification work that will cut that version.

## 2. The behaviour (five rules)

| | Rule |
|---|---|
| R1 · Fails closed | A receipt whose signature does not verify is refused. No receipt, `RECEIPT` or `GRANT_VOIDED` event, RecoveryRequest or outbox event is written; the grant is not voided; the attempt stays `DISPATCHING` and the sweeper takes it over as `OUTCOME_UNKNOWN` (as DEC-2026-10-28 §6.2 and §7) |
| R2 · Own transaction | One `SECURITY_EVENT` `SIGNATURE_INVALID` is recorded in a transaction of its own, with nothing else (DEC-2026-10-28 §7.2, §7.3) |
| R3 · A person is alerted | A designated team member, **`[PLACEHOLDER: recipient, a role title, for the Founders to confirm]`**, receives an operational alert through **`[PLACEHOLDER: delivery channel, for the Founders to confirm]`**. The alert counts as delivered only when it has reached that person; a Record entry or a log line does not count |
| R4 · If the event write fails | The failure is returned to the caller (`ErrReceiptSignature` together with the append failure, as DEC-2026-10-28 §7.3) **and** is sent through a separate operator channel, **`[PLACEHOLDER: channel that does not depend on the database, for the Founders to confirm]`**. That channel does not use PostgreSQL, the Record, Temporal or any path whose failure caused the event write to fail. Nothing else is written |
| R5 · If alert delivery fails | That failure is itself alerted through the operator channel of R4. A failed delivery never changes R1: the receipt stays refused, and no dispatch is retried because of it |

**Open, not decided here (OD-P-71).** (a) The recipient and the channels above. (b) What happens when the operator channel itself fails: no further channel is named, so R5 ends there. Session A proposes no terminal behaviour and invents none. (c) How often a repeating fault may alert (DEC-2026-10-28 §7.3 adds one event per sweeper run). (d) Whether the alert reuses `ops_alert` and `OPS_ALERT_RAISED` (PERD §38.2 ties `ops_alert` to an `investigation_id`, which a receipt failure may not have) or is a separate path. (e) How the core reaches an outbound operator channel: INV-29 and PERD §65.1 give the core no route to providers, and a new egress is a network-policy and dependency decision (AGENT-14). The Founders' earlier instruction not to add an `ops_alert` table or a metric for the `SECURITY_EVENT` (D4) stands until they say otherwise.

## 3. The exact PERD sections to change in the next PERD version

PERD v1.18 text is quoted; the new text follows. Section numbers are v1.18's.

1. **REQ-SEC-005 · Key management (§41), Requirement, fourth bullet.**
   - Now: "Verification failures fail closed and raise an alert."
   - New: "Verification failures, including a failed receipt signature, fail closed and alert a human as §44.3 defines."
2. **REQ-SEC-005, Failure behaviour** (now "—"). New: "A receipt whose signature does not verify follows the five rules of §44.3."
3. **REQ-SEC-005, Audit.** Now: "`KEY_ROTATED`". New: "`KEY_ROTATED`; `SECURITY_EVENT:SIGNATURE_INVALID`."
4. **REQ-SEC-005, Acceptance criteria.** Add: "A test SHALL show that a forged receipt signature produces one `SECURITY_EVENT`, and that a person at the designated recipient receives the alert on the designated channel. A Record entry or a log line is not a received alert."
5. **EC-X09 (§12.5).** Now: "Forged Intent Object (bad or missing HMAC on the internal hop) or forged confirmation | Reject; security alert". New: "Forged Intent Object …, forged confirmation or forged execution receipt (bad or missing signature) | Reject; fail closed; `SECURITY_EVENT`; a human is alerted (§44.3)".
6. **§44.1, "Alerts beyond the must-be-zero metrics [REC]".** Add two rows. "Receipt signature failure | Any receipt whose signature fails verification, or whose `SECURITY_EVENT` cannot be written. A person receives it (§44.3)". "Alert delivery failure | Any alert of §44.3 that could not be delivered to its recipient. Sent through the operator channel".
7. **New §44.3 · Alert behaviour for a failed receipt signature.** The five rules of §2 of this record, the placeholders marked as placeholders, and the open points (a) to (e) marked [OQ] until a decision record adopts them (PERD P.2).
8. **§32.2 and §38.2.** No change. `SECURITY_EVENT` kind `SIGNATURE_INVALID` is already adopted. Whether `OPS_ALERT_RAISED` and `ops_alert` carry this alert is open point (d).
9. **The PERD change list** ("Changes in v1.NN") names items 1 to 7.

The plan is not changed by this record. OBS-01 builds the alert list of §44.1 ("Each alert fires on its fixture"); its `blocked` flag is set in `tasks.csv` by `docs#70`, an operational field, and its done-when text changes only by a change request (plan §19).

## 4. What this does not do

It does not implement the alert path, add a table, a metric, a schema field, a dependency or a service, and it does not choose a recipient or a channel. DEBT-02 stays open.

## 5. Migration notes (AGENT-15)

Documentation only. When the PERD version that carries §3 is cut, the PERD extracts vendored in `noema` are re-pointed in the same change set if their text changes (REQ-OPS-005); §3 changes none of the vendored sections (§28.2 and §32.2 are untouched).

## 6. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Requirement given; behaviour, recipient and channel pending | 29 October 2026 | Working session, summarised here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
