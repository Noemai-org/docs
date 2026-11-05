# Task card: EXP-01

Plan task EXP-01 (owner C2; REQ-EXP-002; Needs OUT-01, now merged; week 4, 9 Nov 2026; G1 path: US-01 requires the explanation to cite the masked account). Template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Repository: `noema` (the card lives in `docs`). Drafted 5 Nov 2026 by the Core Engineer 2 role agent. **Status: DRAFT until the Founder approves and merges it. Nothing is built before then.** Two decisions below are the agent's defaults and one is a question for the Architect.

```
TASK-EXP-01  EXP-01 · Template-only explanations for the slice: facts in, deterministic template text out, no model; every statement maps to a verified fact or a template
Priority: P0
Requirement IDs: REQ-EXP-002 (the deterministic part: fallback templates and the claim rules of PERD §31.2 that need no model); SoT IDs: INV-13 (no false certainty), AGENT-17, INV-22 (no model in this task), BD-10
Rationale: US-01 and US-06 end with an explanation that cites the masked account and states only what is KNOWN, a verdict or an unknown. Until the model renderer exists (EXP-03), the fallback template is the whole explanation, and it is also what the core falls back to whenever the renderer fails or is blocked. [REQ-EXP-002]
Modules touched (allowlist; paths in `noema`):
  services/core/explanation/                       (new package: template selection, slot filling, the deterministic claim rules)
  services/core/explanation/README.md
  packs/fintech_v1.json                            (template texts for the five existing template IDs, locale en-NG only; see Q1)
  packs/README.md, packs/tests/                    (shape tests for the new pack section)
  status/EXP-01.md
  ← nothing else may change. contracts/ is read-only (explanation-facts.v1 exists). No new dependency (AGENT-14): the standard library only. If Q1 requires a pack-schema change, that is a contract change (AGENT-15) and a change request first.
Contracts: none; bump required? Only if Q1 is answered "new pack section with its own schema" (then Y, by change request).
Inputs/outputs: `Render(facts ExplanationFacts) (Explanation, error)`, pure and deterministic. `Explanation` is `{text, claims[], template_id, template_version}` where every sentence is a template with slots filled from `facts`, `unknowns`, `actions`, `advice` or `next_steps`. No fact, no sentence: a slot with no fact makes the sentence an "unknown" sentence from the template set, never a guess.
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

## Question for the Architect (blocks the build)

- **Q1: where do the template texts live, and in what shape?** PERD §31.2 says the pattern lists are pack data and `packs/fintech/templates/` is in the §64.2 layout, but `packs/fintech_v1.json` today holds only template IDs (`fin.expl.case_opened.v1`, `fin.expl.case_routed.v1`, `fin.expl.complaint_logged.v1`, `fin.expl.evidence_recorded.v1`, `fin.expl.status_explained.v1`) and no text, and the pack schema has no templates section. The §64.2 layout also names no core package for the deterministic renderer. **Agent default (smallest safe):** a new `templates` section in the pack (`template_id → {locale → text with {slot} markers, slot kinds}`), en-NG only; the renderer in `services/core/explanation/`. That is a pack-schema change (AGENT-15), so it needs the Architect's yes and a change request before any code. **What would invalidate it:** a decision that texts live in `packs/fintech/templates/*.json` files loaded as data, or that EXP-04 owns the schema.

## Decisions taken by the agent (reversible)

| # | Question | Default |
|---|---|---|
| D1 | A slot with no fact | the template's own "unknown" sentence; never an empty slot and never a guess |
| D2 | Locale in this task | en-NG only; other locales fall back to en-NG (REQ-EXP-003 failure behaviour) |
| D3 | An INFERRED fact | stated with its rule ID's template ("based on rule …"), never as KNOWN |
| D4 | Where it lives | `services/core/explanation/`, imported by no power package (SoT §51) |
