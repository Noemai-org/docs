# Task card: EXP-01

Plan task EXP-01 (owner C2; REQ-EXP-002; Needs OUT-01, now merged; week 4, 9 Nov 2026; G1 path: US-01 requires the explanation to cite the masked account). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Repository: `noema` (the card lives in `docs`). Drafted 5 Nov 2026 by the Core Engineer 2 role agent. **Status: DRAFT until the Founder approves and merges it. Nothing is built before then.** The decisions below are the agent's defaults. Where the template texts live is settled by DEC-2026-11-04-architect-rulings R3 (c) (below); there is no open question.

```
TASK-EXP-01  EXP-01 · Template-only explanations for the slice: facts in, deterministic template text out, no model; every statement maps to a verified fact or a template
Priority: P0
Requirement IDs: REQ-EXP-002 (the deterministic part: fallback templates and the claim rules of PERD §31.2 that need no model); SoT IDs: INV-13 (no false certainty), AGENT-17, INV-22 (no model in this task), BD-10
Rationale: US-01 and US-06 end with an explanation that cites the masked account and states only what is KNOWN, a verdict or an unknown. Until the model renderer exists (EXP-03), the fallback template is the whole explanation, and it is also what the core falls back to whenever the renderer fails or is blocked. [REQ-EXP-002]
Modules touched (allowlist; paths in `noema`):
  services/core/explanation/                       (new package: template selection, slot filling, the deterministic claim rules)
  services/core/explanation/README.md
  packs/fintech/templates/en-NG.json               (template texts, one JSON file per locale keyed `<outcome_id>/<classification>`, locale en-NG only; DEC-2026-11-04-architect-rulings R3 (c))
  packs/fintech/templates/README.md, packs/tests/  (shape tests for the templates file)
  status/EXP-01.md
  ← nothing else may change. contracts/ is read-only (explanation-facts.v1 exists). `packs/fintech_v1.json` stays untouched: the texts are data files under `packs/fintech/templates/`, not a pack-schema change. No new dependency (AGENT-14): the standard library only.
Contracts: none; bump required? N.
Inputs/outputs: `Render(facts ExplanationFacts) (Explanation, error)`, pure and deterministic. The template is looked up by (outcome, classification) and locale, keyed `<outcome_id>/<classification>` in the locale's file; `template_id` is an output of that lookup, never the key. `Explanation` is `{text, claims[], template_id, template_version}` where every sentence is a template with slots filled from `facts`, `unknowns`, `actions`, `advice` or `next_steps`. No fact, no sentence: a slot with no fact makes the sentence an "unknown" sentence from the template set, never a guess.
Acceptance criteria:
  REQ-EXP-002:
  - Every sentence of the output SHALL map to a template ID, and every number, time and masked identifier in it SHALL appear in `facts` (PERD §31.2 checks 1 and 2).
  - No unmasked digit run longer than 4 SHALL appear (check 4).
  - A fact whose status is not KNOWN, INFERRED or a verdict SHALL never be stated as fact; it SHALL appear only in an unknown sentence (INV-13, INV-19).
  - The forbidden claims of PERD §31.2 ("your money is safe", a reversal time, "done" without an ACHIEVED verdict) SHALL not be producible: there is no template for them.
  - Template coverage: every (outcome × classification) combination of the slice has a template (checked by the pack shape test now; by `packcheck` when PCK-02 enforcement moves to EXP-04).
Task "Done when" (plan): Explanations use only verified facts
Tests to write FIRST (AGENT-11):
  - a golden for each slice outcome: US-01 (ALLOW, zero grants, the explanation cites the masked account, no state change claimed) and US-06 (verdict ACHIEVED by key, the case reference masked)
  - property test over generated `ExplanationFacts`: every digit run in the text is a substring of a fact value or of a template literal; no run of more than 4 unmasked digits
  - an UNKNOWN or STALE or UNAVAILABLE fact never appears as a stated fact; a CONTRADICTORY pair gives the "we cannot tell yet" sentence
  - the 200-case hallucination corpus of REQ-EXP-002 is the validator's, not this task's (EXP-02); here a small adversarial table (an injected instruction in a fact's `value_masked`, a fact with a digit run of 12) shows the text carries only the masked form
  - determinism: same facts, same text, byte for byte; no clock read
Faults to exercise (AGENT-12): none (pure). The caller's real-fault evidence comes from EVD-01 and OUT-01.
Record events asserted: none in this task. `EXPLANATION_RENDERED` and `EXPLANATION_BLOCKED` are written by the caller that stores the explanation (REQ-EXP-001, EXP-03).
Dependencies: OUT-01 (merged); EVD-01 slices 1 to 3 (facts come from evidence items); PCK-02 mechanism (merged).
Out of scope: the model renderer (EXP-03); the claim validator against model output (EXP-02); other locales and native-speaker review (EXP-04, GOV-10); the operator evidence packet (EXP-05); storing the explanation (the `explanation` table is an Orchestrator/edge concern).
Definition of done: tests green; boundary lint green (explanation is never imported by trust, execution or outcome); docs updated; PR answers the SoT §52 questions
If blocked or conflicting: STOP and emit the CONFLICT block (§71.3)
```

Owner: C2. Needs: OUT-01 (merged). Gate: G1.

## Where the template texts live (settled, no question open)

DEC-2026-11-04-architect-rulings **R3 (c)**, on `main`: "Template format: one JSON file per locale at `packs/fintech/templates/<locale>.json`, keyed `<outcome_id>/<classification>`. Locales: `en-NG`, `pcm`, `yo`, `ha`, `ig`." This task writes `en-NG` only. `packs/fintech_v1.json` holds only the five template IDs and is not changed, so there is no pack-schema change and no change request (AGENT-15 does not apply). The renderer lives in `services/core/explanation/`, imported by no power package (D4).

## Decisions taken by the agent (reversible)

| # | Question | Default |
|---|---|---|
| D1 | A slot with no fact | the template's own "unknown" sentence; never an empty slot and never a guess |
| D2 | Locale in this task | en-NG only; other locales fall back to en-NG (REQ-EXP-003 failure behaviour) |
| D3 | An INFERRED fact | stated with its rule ID's template ("based on rule …"), never as KNOWN |
| D4 | Where it lives | `services/core/explanation/`, imported by no power package (SoT §51) |
