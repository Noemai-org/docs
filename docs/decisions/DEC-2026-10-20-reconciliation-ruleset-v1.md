# DEC-2026-10-20 · Reconciliation rule set v1, where it differs from PERD §22.3

| | |
|---|---|
| **Status** | Accepted — 21 October 2026 — normai-systems (recorded at the user's direction) |
| **Date** | 20 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Decides** | Whether the three differences in section 2 enter rule set v1 and PERD §22.3 |
| **Supersedes** | Nothing |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Accepted (see the table above)
- Date: 20 October 2026
- Owner: Founder and Technical Co-Founder
- Decision: section 4 (requested)
- Rationale and evidence: sections 1 and 3
- Affected requirement IDs / SoT sections: REQ-RES-001, REQ-RES-002, PERD §22.3, §21.1; SoT §14, §35.5; INV-19
- Migration notes: adoption needs a new PERD version (never an in-place edit) amending §22.3; `packs/fintech/recon_rules/rules.v1.json` in noema#27 already holds the proposed rules, so rejection means changing that file and the tests that assert the properties
- Supersedes: nothing
- Decides: see the table above

## 1. Why this record exists

PERD §22.3 lists rules R1 to R7 with a precedence, and REQ-RES-001 lists metamorphic properties the engine must satisfy. Building both showed that the rules as written violate two of the properties. The build chose the safer reading (AGENT-20) in three places. Those choices go beyond the PERD text, so they need a recorded decision and not a silent change.

## 2. The three differences

| # | PERD §22.3 text | Rule set v1 as built | The property it protects |
|---|---|---|---|
| 1 | R1: debit POSTED and credit CREDITED, both KNOWN | R1 also requires no KNOWN pending settlement, no KNOWN pending reversal, and no required source UNAVAILABLE | "No pending state is collapsed into a terminal one"; losing a source never raises certainty |
| 2 | R3 is checked before R4; "R4 still fires when the reversal itself conflicts" | R3 does not fire when a contradiction labelled `reversal_conflict` or `conflict:reversal` exists | The sentence quoted from the PERD |
| 3 | R4: facts incompatible under the compatibility matrix | Two KNOWN rows of a single-valued fact (credit, switch, settlement, reversal) with different states are also a contradiction | PERD §21.1: CONTRADICTORY is incompatible values for the same fact |

The certainty tiers used by the "losing a source never raises certainty" property are data in the rule set: the three terminal classes, CONTRADICTORY_STATE and POSSIBLE_DUPLICATE are tier 2, and every indefinite classification, INSUFFICIENT_EVIDENCE included, is tier 1. With INSUFFICIENT_EVIDENCE at tier 0 the property fails, because losing a credit read turned INSUFFICIENT_EVIDENCE into EXECUTION_OUTCOME_UNKNOWN, which is not more certainty about the payment.

## 3. Evidence

The rule data is checked by one test per rule, all 1500 combinations of five fact kinds against a hand-written restatement of PERD §22.3, every matrix entry, and 4000 random sets for four metamorphic properties. Mutating each of the three differences (and two other rule edits) makes a named test fail.

## 4. Decision requested

Adopt the three differences into rule set v1, and amend PERD §22.3 in a new PERD version to match, or name the literal R1 to R7 and accept that the two properties cannot both hold. **Recommendation:** adopt.

## 5. Not decided here

Five classifications have no rule in v1 (REJECTED_CONFIRMED, DEBIT_POSTED_CREDIT_UNCONFIRMED, REVERSAL_PENDING, PARTIAL, EVENT_ORDER_UNCERTAIN). They are separate open decisions (OD-P-52 to OD-P-56); until decided they fall to INSUFFICIENT_EVIDENCE.

## Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted | 20 October 2026 | Prior agreement, confirmed by the Founder on 21 October 2026; formalized in this decision record through PR #53. |
| Technical Co-Founder | Accepted | 20 October 2026 | Prior agreement, as confirmed by the Founder on 21 October 2026; formalized in this decision record through PR #53. |
