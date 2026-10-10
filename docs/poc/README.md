# The POC: what we are building now

> **Derived, non-normative.** This page is a working brief and checklist for the proof of concept. The POC is defined only in [`NOEMA_SOURCE_OF_TRUTH.md`](../NOEMA_SOURCE_OF_TRUTH.md) (the SoT), Part VII (§30–40). Read those sections before building anything. If this page and the SoT disagree, the SoT wins.

## The fence (SoT §30, BD-03, BD-04)

**Noema is not its POC.**

- **Noema** is a global, cross-industry trusted-execution layer for consequential action (BD-01).
- **The POC** is one narrow, hostile workflow chosen for evidence, not prestige. It is not the product definition, and POC numbers never define the company's market, architecture or ceiling (BD-04).

When in doubt, a POC statement says "POC".

| | The POC (SoT §30) |
|---|---|
| Problem | "Where is my money?": failed, delayed, duplicated or disputed transactions that customers cannot see into (§31) |
| First wedge | Voice-fronted **transaction-exception resolution** inside Nigerian fintech (BD-03). This is the only canonical first wedge. Card replacement and customer account inquiry, which appear in the archive, are **not** the wedge. |
| Who it serves | One synthetic Nigerian fintech and its customers |
| Mode | Mode 1 only. The Trust interface stays clean for Mode 2, which is not built (POC-FR-16, BD-13). |
| Interfaces | Voice as the front door; text as the canonical internal contract. Correctness is benchmarked text-first (BD-14, §34.4). |
| Verticals | Fintech pack (POC subset) populated; telecom, insurance and healthcare-administration conformance packs skeletal (§15.4, POC-FR-15) |
| Actions | Reads, diagnosis and **non-monetary** writes only. **No money movement of any kind** (BD-08, §34). |
| Environment | The synthetic enterprise environment on Tushe, with deterministic fault injection (BD-07, §36) |
| Success | Benchmark gates passed, competent baselines beaten or honestly matched, and a design partner's own numbers moved (§30, §40.3) |

The test for every feature request (§33): *does this help prove that a probabilistic system can propose while Noema deterministically decides, executes, verifies and proves, under hostile conditions?* If not, it is out of scope.

## Scope: where it is defined

| Topic | SoT |
|---|---|
| Allowed governed, non-monetary actions | §34.1 |
| Prohibited actions, whatever the confidence | §34.2 |
| The complete POC capability registry (12 callable, 8 `PROHIBITED`), with retry safety and consequence profiles | §34.3, §43.8 |
| Languages and channels | §34.4 |
| Non-goals, with reasons | §34.5 |
| What is built and what is deferred, by power | §35.1 |
| The POC loop | §35.2 |
| Technology choices [DECISION]; deployment shape (two deployables) and Temporal rules | §35.3, §35.6, §46 |
| Idempotency key, state classifications, recovery types, revalidation | §35.5 (see also [`../engineering/state-registry.md`](../engineering/state-registry.md)) |
| Synthetic environment | §36 |
| Synthetic environment (Tushe) | [`tushe/README.md`](tushe/README.md): the issued requirements and acceptance specification for the Tushe environment; frozen; changes go through delta files. |
| Requirements and user stories | §37 (see [`../requirements-index.md`](../requirements-index.md)) |
| Benchmark, targets, safety gates, comparison arms | §38 |
| Deployment path (shadow → assisted → governed non-monetary production) | §39 |
| Phases A–F, the four-week time box, definition of done | §40 |

## Things that are deliberately **not** being built in the POC

These come from SoT §34.5 and §35.1. Each has a reason in the SoT.

- Any monetary write, any refund, reversal or transfer, and any compensation for monetary actions.
- Non-monetary writes that end obligations or silence alerts: closing or resolving a case or complaint; changing, pausing or stopping an SLA or regulatory clock; editing or deleting recorded evidence; lowering a case's priority or severity (§34.2).
- The Mode 2 integration.
- Verticals beyond the conformance packs.
- Studio, and natural-language policy authoring.
- An agent builder, MCP server product or agent gateway.
- Fine-tuning or learning from production data.
- More application services than the two agreed deployables (the Python model service and the Go core service); Kubernetes "for appearance".
- Vector databases, graph databases or Kafka, and Redis as authoritative state.
- WhatsApp, SMS or other channels.
- A consumer banking app.
- Broad analytics dashboards.
- Treating synthetic results as proof of production readiness, ROI or compliance.

## Order of work (SoT §35.4, §40.1)

1. **Phase A (environment):**
   - the Tushe environment to spec;
   - contracts and schemas first;
   - fixtures.

   Exits when AT-01 to AT-20 pass, `/contracts` v1 is frozen, and at least 50 adversarial fixtures run reproducibly.
2. **First vertical slice, on text, no faults:** Text → Input Gateway → Intent Object → Entity Resolution → evidence reads → State Reconciliation → Trust decision → Planner → Execution → Outcome verdict → Explanation → Record.
3. **Then, in this order:**
   - timeout after write → `OUTCOME_UNKNOWN` → independent verification by idempotency key;
   - ambiguity and clarification;
   - contradictory state;
   - policy edge cases, clocks and the confirmation flow;
   - recovery and the pending-outcome watch;
   - adversarial and security cases;
   - finally voice.

   Voice (Track E) runs in parallel from Phase A and depends only on the canonical input contract. If schedule pressure threatens Phases B–D, voice work slips before any Trust, Execution or Outcome work is cut; the real-conditions voice gate (§37.5) must still pass before any design-partner demo (§40.1).
4. **Phases B–F** follow §40.1, with exit conditions there. If the time box and the safety gates conflict, the gates win and the date moves (§40.2).

## Claims discipline for POC numbers

- The 73% autonomous-resolution and 89% handling-time figures are **[HYPOTHESIS]**. They are never published as facts until measured (§38.2).
- The manual-touch reduction is a **[HYPOTHESIS]** that must be measured with a design partner (§31.3).
- §38.2 targets are **[TARGET]** synthetic gates, not real-world performance claims.
- Zero failures in n cases supports only a bound of about 3/n at 95% confidence, never "zero" (§38.8). Any external safety claim states the number of cases, how they were generated, the conditions exercised and the bound.
- Results from generated cases alone are never reported as the release result; release runs use the held-out set (§38.1, OD-16).
- No monetary saving is claimed outside the company until a design partner's numbers validate it (§38.6).
- Synthetic switch response codes are labelled synthetic and never presented as NIBSS semantics (§34.5, AGENT-25).

## Definition-of-done checklist (SoT §40.3)

None of these is demonstrated yet. This repository contains no implementation ([OD-P-01](../open-decisions.md#od-p-01)). Tick an item only with evidence from the live benchmark.

### Safety
- [ ] Zero S0 ever.
- [ ] Zero S1 in the release suite.
- [ ] Every confused-deputy and unauthorised case is blocked (US-07, B3).
- [ ] No false-confidence answer (INV-13).
- [ ] §38.3 safety gates all at threshold.

### Correctness
- [ ] §38.2 targets met.
- [ ] All five faces of the problem (§31.4) pass their cases.
- [ ] Every outcome independently verified (INV-04).
- [ ] Every decision reconstructable from the Record alone (INV-10).

### Generality
- [ ] Fintech pack and three conformance packs load.
- [ ] Core contract tests pass on all four packs (POC-FR-15).
- [ ] The core lint finds no vertical terms (INV-14, POC-NFR-10).

### Competition
- [ ] Comparison arms built competently, run and reported honestly (§38.5).

### Business
- [ ] Safety–autonomy curve produced with a defended operating point (§38.4).
- [ ] Headline intervention metric measured against a realistic baseline.

### Voice
- [ ] The demo runs live and unscripted through voice, on the same core.
- [ ] A low-confidence key slot always clarifies.
- [ ] The real-conditions gate holds (§37.5).

### Mechanics
- [ ] Principal and resource scope enforced on every read and write.
- [ ] Unknown, stale, ambiguous and contradictory states are explicit.
- [ ] Every grant is bound to principal, resource, intent, capability, policy version, evidence set and plan hash.
- [ ] Revalidation before every write (INV-17).
- [ ] Stable idempotency keys (INV-08).
- [ ] Unknown outcomes verified before any retry (INV-07).
- [ ] Postconditions independently verified.
- [ ] Complete causal record for every governed write.
- [ ] Explanation claims bound to evidence.

### Environment and reproducibility
- [ ] At least 300 hidden-oracle cases with versioned fixtures.
- [ ] Deterministic replay passes (INV-21).
- [ ] The oracle is unreachable from runtime credentials (INV-22).
- [ ] Controllable clock, reset and seed reproducibility.
- [ ] Every fault family in §36 can be generated.
- [ ] The non-monetary write boundary is enforced.
- [ ] Baselines run on the same scenarios.
- [ ] Verification is independent of the explanation generator.

### Reporting
- [ ] Results include safety, correctness, false blocks, intervention, recovery, latency and cost, not just automation.
- [ ] No S0 defects and no unresolved S1 defects.

### Discovery
- [ ] Baseline economics gathered.
- [ ] A design-partner path agreed.

**Added before any production use (Phase 2 onward):** see the closing paragraph of SoT §40.3 and [OD-P-04](../open-decisions.md#od-p-04) (runbooks).
