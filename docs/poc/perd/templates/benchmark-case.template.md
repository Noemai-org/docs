# Benchmark case template: field options

<!-- Companion to benchmark-case.template.json. Source: PERD §48.2 (case contract [REC]). Replace every "<…>" in the JSON; use only the options listed here. Where an option list is TODO, ask its owner; do not invent codes. -->

The JSON template has exactly the fields of the PERD §48.2 case contract, with every value replaced by a `"<…>"` placeholder. The contract is a [REC] default (PERD §48.2, mirrored as [OD-P-39](../../../open-decisions.md#od-p-39)). Admitted cases are immutable within a released suite version; fixes create new case versions (PERD §48.2).

Held-out cases never go in this repository (OD-16, REQ-BEN-003, REQ-AGT-004). This template is for the case *format* only.

| Field | Options | Source |
|---|---|---|
| `suite_layer` | `GENERATED` · `HELD_OUT` · `PARTNER` <!-- PARTNER only from Phase 2, with written consent --> | PERD §48.2, §48.1 |
| `channel` | `text` · `voice` | PERD §48.2 |
| `provenance` | `generated` · `written_by:<owner>` · `regression_of:<incident>` | PERD §48.2 |
| `families` | `B1` Understanding · `B2` State · `B3` Trust · `B4` Execution · `B5` Outcome · `B6` Security · `B7` Record · `B8` Business <!-- B8 is computed across all cases (PERD §48.1) --> | SoT §20.2; PERD §48.1 |
| `category` | TODO(benchmark owner): codes not defined. PERD §48.1 names ten categories (clean, unique; ambiguity and entity resolution; cross-system state conflict; timeout and unknown outcome; duplicate, replay, idempotency; authorisation and confused deputy; policy mutation and clocks; prompt injection; stale session, abandon and resume; integration hostility). §48.2's only example code is `AMBIGUITY`. | PERD §48.1, §48.2 |
| `locale_mix` | `en-NG` · `pcm` · `yo` · `ha` · `ig` | PERD §31.2, REQ-INT-003 |
| `expected.disposition`, `expected.acceptable_alternatives` | `ALLOW` · `CLARIFY` · `CONFIRM` · `WAIT` · `ESCALATE` · `REJECT` · `UNKNOWN` | SoT PLAT-FR-05, POC-FR-06; PERD §23.1 |
| `expected.classification` | `null`, or one of: `SUCCESS_CONFIRMED` · `REJECTED_CONFIRMED` · `DEBIT_POSTED_CREDIT_UNCONFIRMED` · `SETTLEMENT_PENDING` · `REVERSAL_PENDING` · `REVERSED_CONFIRMED` · `POSSIBLE_DUPLICATE` · `PARTIAL` · `EXECUTION_OUTCOME_UNKNOWN` · `CONTRADICTORY_STATE` · `EVENT_ORDER_UNCERTAIN` · `INSUFFICIENT_EVIDENCE` <!-- [REC] set; SoT §35.5 governs where they overlap --> | PERD §22.3; SoT §35.5 |
| `expected.clarification_expected`, `expected.escalation_expected` | `true` · `false` (JSON booleans, not strings) | PERD §48.2 |
| `expected.required_audit_events` | Record event types from PERD §32.2 [REC]; SoT examples: `DECISION_MADE`, `GRANT_SPENT`, `RECEIPT`, `VERDICT` | PERD §32.2 |
| `severity_if_failed` | `S0` · `S1` · `S2` · `S3` | PERD §58; SoT §38.3 |
| `safety_gate_relevance` | TODO(benchmark owner): gate codes not defined. Gates are the SoT §38.3 safety gates; §48.2's only example code is `CROSS_ACCOUNT_DISCLOSURE`. | SoT §38.3; PERD §48.2 |
| `fault_plan` | A `fault_plan_id` from the FaultPlan contract, or `fp_none` | PERD §37.1, §48.2 |
| `version`, `generator.seed`, `utterances[].turn` | JSON integers, not strings | PERD §48.2 |
