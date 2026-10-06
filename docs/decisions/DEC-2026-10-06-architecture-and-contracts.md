# DEC-2026-10-06-architecture-and-contracts

- Date: 6 October 2026
- Owner: Founders (Technical Co-founder)
- Decision:
  1. **Orchestration & Language (Overrides OD-07 & OD-11 defaults):** Noema will use Temporal as the durable execution engine from Day 1 to avoid a Phase 3 rewrite. The architecture will be a multi-language microservice split: the Understanding/Intent layer in Python, and the Trust/Execution/Outcome layers in Go, communicating via strict JSON contracts over Temporal.
  2. **Repository Layout (Closes OD-P-01):** The organization uses a multi-repo strategy. `/docs`, `/brain`, `/backend`, and `/intent-engine` are separate repositories. There is no single monorepo.
  3. **Tushe Specification (Closes OD-P-03):** The v1.0 Tushe specification is verified to exist in `docs/poc/tushe/` and serves as the authoritative source for the POC wedge.
  4. **Contract Enums (Closes OD-P-06 & OD-P-08):**
     - **Intent Status:** `EXTRACTED`, `VALIDATED`, `REJECTED_AT_GATE`, `SUPERSEDED`.
     - **Authority Results:** `PASS`, `FAIL`, `NOT_EVALUATED`, `OVERRIDDEN`.
     - **Trust Reason Codes:** `PROHIBITED_CAPABILITY`, `AMBIGUOUS_COUNTERPARTY`, `DECLINED_BY_APPROVER`, `POLICY_VERSION_MISMATCH`, `INSUFFICIENT_EVIDENCE`, `STALE_EVIDENCE`.
- Rationale and evidence:
  - Adopting Temporal and Go + Python immediately aligns with Noema's post-POC enterprise scalability requirements, avoiding massive technical debt and re-engineering.
  - Multi-repo layout is already the established pattern.
  - Enum standardization is required to unblock the freeze of v1 contracts for Phase A.
- Affected requirement IDs / SoT sections:
  - Closes: OD-07, OD-11, OD-P-01, OD-P-03, OD-P-06, OD-P-08.
- Supersedes: The recommended SoT defaults for OD-07 and OD-11.
