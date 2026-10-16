# Task card: UND-05

Plan v1.7 task UND-05 (Wed 21 Oct; compiles to the two DEC C2 nodes). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Source decision: [DEC-2026-10-16 contract-and-pack-clarifications](../../../decisions/DEC-2026-10-16-contract-and-pack-clarifications.md). Repository: `noema` (the card lives in `docs`).

```
TASK-P5-001  UND-05 · Intent Compiler on the fintech pack: versioned prompt templates; compiles to exactly two nodes, `fin.payments.exception.investigate` (slots `question_type` and `requested_remedy`) and `fin.meta.out_of_scope`, and never to another node
Priority: P0
Requirement IDs: REQ-INT-005; SoT IDs: US-10, US-22; SoT §15.3, §15.4, §34.3, §43.7
Rationale: US-10; US-22; PUS-03. The rejection must come from the registry, not from model refusal. [REQ-INT-005]
Modules touched (allowlist; paths the agent may create or change in `noema`): services/model/ (the compiler, its prompt templates and the node catalogue it reads from the loaded pack); contracts/ is read-only here   ← nothing else may change
Contracts: the Intent Object and the pack schema from `contracts/`; bump required? N
Inputs/outputs: a canonical input and the loaded pack in → an Intent Object whose `intent_node` is one of the two nodes, or an explicit out-of-scope
Acceptance criteria:
  REQ-INT-005:
  - Every prohibited capability SHALL have at least 3 benchmark phrasings across locales, each ending in REJECT.
  Task "Done when" (plan v1.7): Golden examples G-A to G-E pass on all three providers
Tests to write FIRST (AGENT-11): golden examples G-A to G-E (PERD §20.5) on all three providers, written first; plus a case for each row of the C2 mapping (a `question_type` value or a `requested_remedy` slot is produced, never a node); a model output that names any other node is rejected at the schema gate
Faults to exercise (AGENT-12): provider outage and failover (PUS-04, UND-08), from the hostility proxy, never mocked
Dependencies: UND-03, PCK-01; REQ: REQ-CAP-002
Out of scope: any intent node other than the two; any upper-case legacy class label; Trust or Execution logic; the lexicon (UND-06); the schema gate itself (UND-03)
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C2 with a coding agent. Needs: UND-03, PCK-01. Dated Wed 21 Oct.

## Brief (DEC-2026-10-16 contract-and-pack-clarifications C2)

The compiler produces the nodes and slots of the pack as rewritten by PCK-01:

| Node | Slots | Outcome definitions |
|---|---|---|
| `fin.payments.exception.investigate` | `subject_resource`, `amount`, `counterparty`, `when`, `question_type` (Reference; vocabulary from PERD §20.4), `requested_remedy` (Reference to a `fin.cap.*` ID) | `fin.outcome.exception.status_explained`, `fin.outcome.exception.case_opened`, `fin.outcome.complaint.logged` |
| `fin.meta.out_of_scope` | none | none. Trust returns REJECT `OUT_OF_SCOPE`; no capability is evaluated (PUS-03) |

`question_type` takes the vocabulary of PERD §20.4. A requested remedy that is prohibited (refund, reverse, transfer, close the complaint) is carried in `requested_remedy` as a Reference to a `fin.cap.*` ID and rejected by Trust through the registry, never by the prompt (REQ-INT-005).

**Amounts (DEC-2026-10-16 money-and-value-lists M5).** Spoken or written amounts ("20k", "₦50,000") become integer minor units in the lexicon, which is deterministic code using the `contracts/currencies.json` table; the model may extract the surface form and never does arithmetic. Excess precision is rejected, never rounded.
