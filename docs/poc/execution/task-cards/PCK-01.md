# Task card: PCK-01

Plan v1.7 task PCK-01 (in progress under DEC C3; dated Tue 20 Oct, after CON-01). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-16 contract-and-pack-clarifications](../../../decisions/DEC-2026-10-16-contract-and-pack-clarifications.md). Repository: `noema` (the card lives in `docs`).

```
TASK-P1-001  PCK-01 · Fintech pack v1 rewritten to SoT §15.3 shapes against the CON-01 pack schema (two intent nodes, trust profiles, outcome definitions, vendor-free evidence-source descriptors, policy rules as evaluable templates), on the reusable base of the 20 capability descriptors and the Action Graph; three conformance packs in the same shapes
Priority: P0
Requirement IDs: REQ-CAP-001, REQ-AG-001, REQ-AG-002, REQ-NFR-005; SoT IDs: INV-27, AGENT-06, INV-18, AGENT-09, POC-NFR-10, INV-14, POC-FR-15; SoT §15.3, §15.4, §34.3, §43.7
Rationale: AGENT-06; SoT §43.8. [REQ-CAP-001] SoT §43.9; INV-18. [REQ-AG-001] AGENT-09; SoT §47.1. [REQ-AG-002] POC-NFR-10, INV-14, POC-FR-15. [REQ-NFR-005]
Modules touched (allowlist; paths the agent may create or change in `noema`): packs/fintech_v1.json; packs/conformance/   ← nothing else may change
Contracts: the pack schema from CON-01 (`contracts/`); bump required? N (CON-01 owns the schema; a change to it goes through CON-01 and AGENT-15, never here)
Inputs/outputs: SoT §15.3 shapes in → the four pack files out
Acceptance criteria:
  REQ-CAP-001:
  - `packcheck` SHALL reject each of 8 crafted invalid descriptors.
  REQ-AG-001:
  - A pack containing a node with a PROHIBITED capability SHALL fail `packcheck` and CI.
  REQ-AG-002:
  - Fuzzed routing parameters outside the allowlist SHALL be rejected by the schema 100% of the time.
  REQ-NFR-005:
  - CI SHALL be green on the lint and on four-pack contract tests.
  Task "Done when" (plan v1.7): All four packs load and pass packcheck validate against the CON-01 pack schema; the fintech pack has no upper-case intent class and no node other than the two above; no evidence-source ID names a vendor. Status: in progress (DEC-2026-10-16 contract-and-pack-clarifications C3). Delivered 15 Oct 2026 and reusable as ported: the 20 capability descriptors and the Action Graph (commit ce8897e, ported by noema#1); the rest is rewritten here. The pack reason catalogue holds only fin.reason.* codes and case reasons; the core reason codes and NONE are removed from the pack (DEC-2026-10-16 money-and-value-lists §2.3). Brief: the C2 node table and the ten-class mapping in the task card
Tests to write FIRST (AGENT-11): one failing test per shape, written first and seen failing wherever the ported pack does not meet it: exactly two intent nodes in the fintech pack and no upper-case intent class; every trust profile carries the SoT fields (`risk_class`, `authority`, `policy_templates`, `clocks`, `approvals`, `prohibited_capabilities`, `evidence_required`, `max_evidence_age_seconds`, `data_sensitivity`); every outcome definition has a success predicate in the §43.7 expression language, verification sources and a settle window; every evidence-source ID is vendor-free; every policy rule is an evaluable template, not prose; each conformance pack stays within the SoT §15.4 cap (≤ 3 nodes, 1 trust profile, 1 outcome definition, no adapters, no executed capabilities)
Faults to exercise (AGENT-12): none (a pack-data task; no enterprise fault applies)
Dependencies: CON-01 (the pack schema, delivered in CON-01's first PR on Mon 19 Oct, so that PCK-01 can start); REQ: REQ-AG-001, REQ-CAP-001
Out of scope: the 20 capability descriptors and the Action Graph (reused as ported; change them only if a test shows an error); the compiler (UND-05); the `packcheck` checks (PCK-02); any new intent node; any ported upper-case intent class kept "at a boundary"; any adapter
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: EL, with a coding agent. Needs: CON-01. Dated Tue 20 Oct. Status: in progress (DEC C3).

## Brief for the rewrite (DEC-2026-10-16 contract-and-pack-clarifications C2)

The fintech pack has exactly two intent nodes. The ten upper-case classes of the pack ported on 15 October are mapped below and then deleted; nothing outside the pack uses the labels, so none is kept.

| Node | Slots | Outcome definitions |
|---|---|---|
| `fin.payments.exception.investigate` | `subject_resource`, `amount`, `counterparty`, `when`, `question_type` (Reference; vocabulary from PERD §20.4), `requested_remedy` (Reference to a `fin.cap.*` ID) | `fin.outcome.exception.status_explained`, `fin.outcome.exception.case_opened`, `fin.outcome.complaint.logged` |
| `fin.meta.out_of_scope` | none | none. Trust returns REJECT `OUT_OF_SCOPE`; no capability is evaluated (PUS-03) |

| Ported class | Becomes |
|---|---|
| `VERIFY_TRANSACTION`, `VIEW_PAYMENT_STATUS`, `VIEW_TRANSFER_STATUS`, `INVESTIGATE_EXCEPTION` | `investigate` with `question_type` = `STATUS` (or `WHY`, `REVERSAL_STATUS`, `CASE_STATUS` as said) |
| `DISPUTE_TRANSACTION`, `REPORT_UNAUTHORIZED_TRANSACTION` | `investigate` with `question_type` = `ESCALATION_REQUEST`; routing by policy (fraud to `FRAUD_REVIEW`) |
| `TRANSFER_FUNDS` | `investigate` with `requested_remedy` = `fin.cap.transfer_funds`, then REJECT `PROHIBITED_CAPABILITY` |
| `REQUEST_REFUND` | `investigate` with `requested_remedy` = `fin.cap.initiate_refund`, then REJECT |
| `RECOVER_FUNDS` | `investigate` with `requested_remedy` = `fin.cap.reverse_transaction`, then REJECT; the customer may still ask for `ESCALATION_REQUEST` |
| `SELECT_BENEFICIARY` | Not an intent. It is counterparty resolution inside the node (`candidate_search`, CLARIFY) |

Rules:

- An Intent Object's `intent_node` must exist in the loaded pack; a `question_type` value is never a node; an unknown node or slot is rejected at the schema gate.
- `TRANSFER_FUNDS` was an intent marked `WRITE` and `REQUEST_REFUND` was "routed via escalation case". Both contradict the money boundary: a refund or transfer request is a prohibited remedy that Trust rejects (REQ-INT-005, golden example G-E).
- The conformance packs (telecom, insurance, healthcare administration) follow the same shapes within the SoT §15.4 cap.
- **Reason catalogue (DEC-2026-10-16 money-and-value-lists §2.3).** The pack's reason catalogue holds only `fin.reason.*` codes and case reasons. Remove the core reason codes and `NONE` from the pack: the core codes are a closed enum in `/contracts`, and an empty `reason_codes[]` means no reason.
