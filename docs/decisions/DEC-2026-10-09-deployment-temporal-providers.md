# DEC-2026-10-09-deployment-temporal-providers

- Status: Accepted
- Date: 9 October 2026
- Closes: OD-04, OD-05, OD-07, OD-11
- Owner: Founders (Founder and Technical Co-founder)
- Decision:
  1. **Two deployables, split at the model boundary.**
     - **Model service:** Python. It hosts Understanding (Input Gateway, Intent Compiler, Entity Resolution), the voice pipeline, the explanation renderer and every model or speech provider adapter.
     - **Core service:** Go. It hosts Trust, Execution, Outcome (verifier and outcome watch), the Record, the Evidence Layer, the enterprise adapters and the Temporal workers.
     - **No other application services in the POC.** The synthetic environment (Tushe), Postgres and Temporal are infrastructure, not Noema services.
  2. **Temporal is the durable workflow engine from the POC onward.** It runs long-running and timer-driven work. Postgres remains the only authoritative store.
  3. **Understanding models: GPT (OpenAI), Gemini (Google) and Claude (Anthropic)** are all integrated behind the provider-neutral interface. No single-provider dependence. Switching between them is configuration plus a benchmark run.
  4. **Speech: Aethex AI, Indigenius and N-ATLAS** are all integrated behind the provider-neutral speech interface. No single-provider dependence. Switching between them is configuration plus a benchmark run.
- Rationale and evidence:
  - The two-deployable split turns the rule "no model in Trust, Execution or the verdict" into a process and credential boundary, while keeping grant spend, idempotency and the Record write inside one transaction.
  - Temporal handles the durable timers v1.2 introduced (outcome watches, confirmation expiry, deadline-driven recovery) without hand-building them.
  - Multiple providers keep Noema model-agnostic (SoT §17, PLAT-NFR-09) and remove vendor and continuity risk.
  - Provider defaults are chosen by benchmark, never by assertion.
- Affected requirement IDs / SoT sections:
  - OD-04, OD-05, OD-07, OD-11;
  - BD-16, INV-29, INV-30, AGENT-05, AGENT-28, AGENT-29;
  - SoT §§0.4, 0.5, 14, 17, 34.5, 35.1, 35.3, 35.6 (new), 45, 45.1, 46, 47, 48, 51.
- Migration notes:
  - No application code exists yet, so there is no code migration.
  - Any scaffolding created under the earlier "per-component microservices" decision must be consolidated into the two deployables before Phase B.
  - Local development runs Postgres and a local Temporal server through Docker Compose.
  - The contracts in `/contracts` generate both Pydantic models (model service) and Go types (core service).
  - Provider adapters are built for all six providers; the benchmark configuration includes all of them.
- Supersedes:
  - `DEC-2026-10-06-architecture-and-contracts`, in part: the microservices layout is replaced by the two-deployable shape; Temporal is confirmed.
  - `DEC-2026-10-06-vendor-benchmarks`, in part: the benchmark-candidate shortlists are replaced by the selected multi-provider sets.
