# POC Block 01: Core Realignment and Seam Extraction

## 1. GROUND TRUTH SUMMARY
- **Product Intent & Domain:** Noema is an enterprise execution infrastructure. It acts as a safety and authorization gateway between probabilistic AI understanding and deterministic enterprise execution. 
- **Architecture Decisions:** The architecture relies on Four Powers (Understanding, Trust, Execution, Outcome) with a strict separation of concerns. A recent founder decision (`DEC-2026-10-06-architecture-and-contracts.md`) mandates Temporal as the orchestrator bridging a Python-based Intent engine (Understanding) and a Go-based core (Trust, Execution, Outcome).
- **POC Scope:** A single wedge in the Nigerian Fintech sector (payment exception investigation/resolution), fronted by voice, using Gemini (Latest Pro) and Claude (Latest Sonnet) for Understanding, and Intron Health vs Deepgram for Speech.
- **Repo Map:**
  - `/backend` (Go): Houses `internal/trust`, `internal/execution`, `internal/validation` (deprecated). Built to run as a Temporal worker, but currently just a stub.
  - `/intent-engine` (Python): Houses `api/models.py` (legacy Intent schema), `taxonomy/fintech.py` (sector logic leaking into core).
  - **Data Flow:** Currently disjointed. Intended flow: Python Extracts Intent -> Temporal -> Go Trust Evaluates -> Go Execution Runs Adapter.

## 2. DRIFT REPORT

| Item | Docs Say | Code Does | Severity | Effort |
|---|---|---|---|---|
| **FactStatus Schema** | 8 distinct statuses (e.g., KNOWN, INFERRED, UNKNOWN, UNAUTHORIZED) | 5 legacy statuses in Go and Python | blocks-POC | S |
| **Intent Contract** | Signed `Intent Object` with abstract slots, ambiguity flags, 7 outcomes | Uses legacy `CanonicalIntent` without abstract types or strict boundaries | blocks-POC | M |
| **Trust Layer** | 7 Outcomes (ALLOW, CLARIFY, ESCALATE, etc.), Decision Grant | Uses `READY/WAITING/BLOCKED` state machine | blocks-POC | L |
| **Execution Contract** | `ExecutionReceipt` and single-use HMAC signed Grants | Uses `ExecutionContract` (missing principal binding, plan_hash) | blocks-POC | M |
| **Validation Layer** | Does not exist (folded into Understanding schema gate and Trust) | Explicit `/validation` layer exists in Go backend | blocks-POC | S |
| **Sector Leakage** | Core is completely sector-agnostic. Sectors defined in `/packs`. | `/intent-engine/taxonomy/fintech.py` hardcodes banking intents | blocks-banking-wedge | M |
| **Orchestration** | Temporal bridges Python Understanding and Go Execution | Temporal only exists in `docker-compose.yml`; `main.go` is a stub | blocks-POC | L |
| **Vendor Hardcoding** | Agnostic ports, configurable providers | `google-generativeai` hardcoded in `intent-engine` | debt | S |

**Doc Ambiguities & Contradictions:**
- *Ambiguity:* How exactly the Python intent engine passes the structured `Intent Object` to the Go backend.
  - *Interpretation:* The Python service will use the Temporal Python SDK to start a workflow executed by the Go worker, passing the serialized Pydantic model as the workflow input payload.

## 3. PROPOSED ARCHITECTURE FOR EXTENSIBILITY
- **Core Domain:** `backend/internal/core` will strictly define the abstract interfaces for `Intent`, `Grant`, `Receipt`, and `Verdict`. Zero mention of "funds", "accounts", or "banks".
- **Sector Packs:** We will introduce a `/packs` directory (loaded at runtime). A pack is pure data/config (JSON/YAML) defining schemas, prompts, capability mappings, and risk classes.
- **Integration Ports and Adapters:** 
  - *Decision:* Core will expose a `CapabilityRunner` interface. Integrations (e.g., Tushe API) implement this interface.
  - *Rejected Tradeoff:* Hardcoding external API calls in the execution layer is rejected as it breaks extensibility.
- **Registry and Discovery:** Adapters register themselves on startup mapping to string capability names (e.g., `see.transfer_funds`). If a pack asks for a capability with no registered adapter, it fails closed.
- **Config over Code:** Thresholds (like the 0.35 ambiguity margin) will move from hardcoded values into a global environment config injected at runtime.
- **Contract Tests:** A shared suite of JSON test payloads will exist in the `/docs` or a `/shared` repo. Both Python and Go CI must pass these to ensure schema serialization parity.
- **Idempotency:** Driven by a deterministically hashed `idempotency_key` (IntentHash + PlanHash) generated before workflow execution.

## 4. EXECUTION PLAN

**a. Drift Fixes (Cross-Repo Contracts) [Blocks-POC]**
- *Goal:* Rebuild Pydantic and Go structs to precisely match SoT v1.2 schemas (Intent Object, Decision Grant, Execution Receipt, 8 FactStatuses, 7 Outcomes, Reason Codes).
- *Acceptance:* Shared JSON fixtures successfully unmarshal in both Python and Go test suites.
- *Effort:* M

**b. Sector Extraction [Blocks-Banking-Wedge]**
- *Goal:* Delete `intent-engine/taxonomy/fintech.py`. Create `packs/fintech_v1.json` defining the banking capabilities and intents.
- *Acceptance:* Intent engine loads valid intents dynamically from the pack config, not hardcoded Python files.
- *Effort:* M

**c. Registry & Tushe Adapter Skeleton [Blocks-POC]**
- *Goal:* Build the `CapabilityRegistry` in Go. Implement a mock `TusheAdapter` that handles the `investigate_exception` capability.
- *Acceptance:* Go unit test successfully registers the adapter and routes a mock Decision Grant to it.
- *Effort:* S

**d. Core Realignment (Trust & Temporal Workflows) [Blocks-POC]**
- *Goal:* Delete the legacy `/validation` layer in Go. Rewrite `trust.go` to output the 7 canonical outcomes. Wire up the Temporal Workflow in Go that receives the Intent, calls Trust, and executes.
- *Acceptance:* Temporal worker successfully completes a test workflow when fed a valid Intent payload.
- *Effort:* L

**e. Extensibility Proof (Healthcare Skeleton) [Extensibility]**
- *Goal:* Add a `healthcare_admin_v1.json` pack config with a mock capability.
- *Acceptance:* System routes a healthcare intent without ANY edits to Go or Python core code.
- *Effort:* S

**f. E2E Tests [Blocks-POC]**
- *Goal:* Python script mimicking the voice/understanding layer extracts an intent, starts the Temporal workflow, and awaits the final ExecutionReceipt.
- *Acceptance:* Single `make test-e2e` command spins up Temporal, Go, and Python and passes.
- *Effort:* M

**g. Observability (Correlation IDs) [Deferrable]**
- *Goal:* Propagate IntentID across Python logs, Temporal workflow logs, and Go execution logs.
- *Effort:* S

*Critical Path:* a -> d -> c -> f. (Contracts -> Trust/Temporal -> Adapters -> E2E).

## 5. RISKS AND OPEN DECISIONS
- **Technical Risk 1:** *Temporal Data Serialization Parity (High/High).* Python Pydantic output might subtly mismatch Go struct expectations (e.g., datetime formats, nulls). 
  - *Mitigation:* Strict JSON schema validation at the Temporal ingest boundary.
- **Weak Spots in Docs:** The Tushe v1.0 Spec defines the external environment, but the exact LLM prompt engineering strategy to map messy speech transcripts into the strict `Intent Object` schema is dangerously underspecified.
- **Open Decision (Need your call):** How do we share schema definitions between Go and Python? 
  - *Recommendation:* Define schemas in OpenAPI/JSONSchema format in the `/docs/contracts` folder and use `datamodel-codegen` for Python and `oapi-codegen` for Go. 
  - *Default if no answer:* Manually write Pydantic models and Go structs and use contract tests to enforce parity (faster for POC, creates technical debt).

## 6. DEFINITION OF DONE FOR THIS BLOCK
- Go and Python repos have identical, test-verified schema representations.
- Legacy `Validation` and `READY/WAITING` states are completely erased from the codebase.
- Sector logic is completely purged from Python and Go codebases and moved to a `/packs` config.
- A basic end-to-end Temporal workflow can be triggered from Python, evaluated by Go Trust, and routed to a Go Adapter.
