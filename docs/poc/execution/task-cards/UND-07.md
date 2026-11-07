# Task card: UND-07

Plan v1.11 task UND-07 (week 5, dated Wed 18 Nov 2026; owner C2). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Written by the Repo Steward on 7 Nov 2026 (Founder instruction, Block E, item 4) so that C2 can start when TRU-02 is Done. Every field below is copied from the plan row, the PERD v1.20 REQ blocks and the user-story and PUS tables; nothing is added to scope. **The owner (C2) reviews the card before work starts and changes it only in a PR (README of this folder).**

```
UND-07 · Out-of-scope and prohibited intents end to end (PUS-03, US-10, US-22): REJECT with the alternative; no evidence read before the rejection
Priority: P0 (REQ-INT-005 and REQ-CAP-002 are P0)
Requirement IDs: REQ-INT-005, REQ-CAP-002; SoT IDs: INV-18, BD-08 (cited by REQ-CAP-002); SoT §34.2 (its rationale). The Steward found no other SoT ID in the two REQ blocks.
Rationale: US-10; US-22; PUS-03. The rejection must come from the registry, not from model refusal. [REQ-INT-005] SoT §34.2 [CONVICTION]; BD-08; gate "monetary capability with a callable code path = 0". [REQ-CAP-002]
Modules touched (allowlist): to be filled by C2 before the first edit. The Steward does not guess module paths (AGENTS §3 step 6, AGENT-02). Any path outside services/core/trust/, the Intent Compiler module and its tests needs a founder-approved allowlist.
Contracts: none expected; bump required? N (C2 confirms; AGENT-15 applies if not)
Inputs/outputs: Intent Object in; for a prohibited remedy REJECT PROHIBITED_CAPABILITY, for an out-of-scope request REJECT OUT_OF_SCOPE, each with a polite decline that names what Noema can do. No capability is evaluated for PUS-03, and no evidence is read before the rejection.
Acceptance criteria:
  REQ-INT-005:
  - Every prohibited capability SHALL have at least 3 benchmark phrasings across locales, each ending in REJECT.
  REQ-CAP-002:
  - A property test SHALL assert that each prohibited ID exists and is never callable.
  - A static scan SHALL find no symbol or HTTP route matching the prohibited operations in adapters.
  - A credential test SHALL show Tushe rejecting money-moving calls with the Noema credential (AT-level).
  Task "Done when" (plan): US-10, US-22 and PUS-03 pass.
Tests to write FIRST (AGENT-11): US-10 ("Reverse it"): intent fin.payments.exception.investigate with a requested_remedy slot fin.cap.reverse_transaction -> REJECT PROHIBITED_CAPABILITY, zero evidence reads before the rejection, alternative offered. US-22 ("Close it for me"): REJECT PROHIBITED_CAPABILITY (CLOSE_OR_RESOLVE_CASE), case status unchanged in the oracle. PUS-03 ("buy airtime for me"): intent node fin.meta.out_of_scope, Trust REJECT OUT_OF_SCOPE, no capability evaluated. Failure behaviour of REQ-INT-005: if the model fails to extract the remedy, the request falls back to investigate only and no prohibited action follows. Also B6 and EC-X05 (REQ-INT-005 Tests).
Faults to exercise (AGENT-12): a model that fails to extract the remedy; a jailbroken-style extraction (defence in depth, REQ-INT-005 Security). The Tushe credential test is AT-level and needs a Tushe behaviour that must have been shown (stop condition if not).
Record events to assert: DECISION_MADE (REJECT); the counter noema_prohibited_attempt_total (REQ-INT-005 Audit).
Dependencies: TRU-02 (plan Needs); REQ-CAP-002. Do not start before TRU-02 is Done (AGENTS §3 step 3).
Out of scope: any new capability, adapter or route for a prohibited operation (none may exist, BD-08); any change of a threshold or of the pack's two intent nodes; Mode 2.
Definition of done: tests green; boundary/lint green; Record events asserted; docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C2. Needs: TRU-02. Dated Wed 18 Nov (plan v1.11).

## Open points for the owner (not decided here)

1. The allowlist of module paths (see "Modules touched").
2. The three phrasings per locale per prohibited capability: who writes them, and whether they live in the benchmark generator or the pack (OD-P-51 covers cases per capability; its default is now accepted by the Founders, Block E E4).
