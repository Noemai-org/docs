# Noema Documentation

This is the documentation root for the Noema organisation.

All canonical architecture, specifications, ontology, contracts, engineering standards, strategy, and product documentation lives here.

⸻

## What Noema Is

Noema is an intent infrastructure layer.

It sits between sources of human intent — people, agents, systems, interfaces — and existing enterprise software. Its responsibility is to transform what an Actor means into validated, trusted, contractually executable Actions across those systems, while preserving explicit authority, contextual governance, provenance, and ownership of business truth.

Noema does not replace enterprise systems. It makes their capabilities semantically addressable and governable through Intent.

The canonical lifecycle is:

```
Intent → Resolution → Validation → Trust → Contract → Execution → Outcome
```

For the full thesis, principles, and invariants, see `noema-canonical/CANON.md`.

⸻

## Documentation Structure

| Path | What it contains |
|---|---|
| `noema-canonical/` | The canonical Noema repository: thesis, ontology, architecture, trust model, execution model, contracts, interfaces, engineering standards, enterprise boundaries, taxonomy, strategy, product, decisions, research, and reference workflows. This is the authoritative source for what Noema is and how it works. |

As the Noema organisation grows, additional documentation areas will live alongside `noema-canonical/`:

| Future path | Anticipated purpose |
|---|---|
| `noema-sdk/` | SDK documentation, API references, and integration guides for developers building on Noema. |
| `noema-platform/` | Platform operations, deployment, infrastructure, and operational runbooks. |
| `noema-guides/` | Tutorials, onboarding guides, and worked examples for new team members and partners. |

These do not exist yet. When they do, each will have its own README following the same principles.

⸻

## Where to Start

### If you are new to Noema

Read these documents in order:

1. **`noema-canonical/thesis/thesis.md`** — The full thesis: the problem, the claim, and the architecture it implies.
2. **`noema-canonical/CANON.md`** — The canonical principles, invariants, and foundational distinctions. This is the most important document in the repository.
3. **`noema-canonical/GLOSSARY.md`** — Quick-reference glossary of every canonical term. Read this before diving into any domain document to avoid semantic confusion.
4. **`noema-canonical/architecture/overview.md`** — The system architecture: components, boundaries, and responsibilities.
5. **`noema-canonical/trust/trust-model.md`** — The Trust model: the deterministic decision boundary at the core of Noema.

After these five documents, you will understand what Noema is, what it owns, what it refuses to do, and how the system is structured.

### If you are looking for something specific

| You want to understand... | Go to |
|---|---|
| What Noema is and its core invariants | `noema-canonical/CANON.md` |
| The canonical vocabulary | `noema-canonical/GLOSSARY.md` or `noema-canonical/ontology/glossary.md` |
| The system architecture | `noema-canonical/architecture/overview.md` |
| How Trust works | `noema-canonical/trust/trust-model.md` |
| The Trust State Machine | `noema-canonical/trust/trust-state-machine.md` |
| How Intent is structured | `noema-canonical/ontology/intent.md` and `noema-canonical/intent/intent-model.md` |
| How execution works | `noema-canonical/execution/execution-model.md` |
| Action Contracts | `noema-canonical/contracts/action-contract.md` |
| How integrations work | `noema-canonical/integrations/integration-model.md` |
| The external APIs | `noema-canonical/interfaces/overview.md` |
| Engineering standards | `noema-canonical/engineering/constitution.md` |
| How enterprise systems relate to Noema | `noema-canonical/enterprise/overview.md` |
| Strategic positioning and market | `noema-canonical/strategy/positioning.md` |
| Product model | `noema-canonical/product/product-model.md` |
| Architectural decisions | `noema-canonical/decisions/README.md` |
| A real end-to-end workflow | `noema-canonical/reference-workflows/card-renewal/` |
| What Noema explicitly does not do | `noema-canonical/thesis/non-goals.md` |

⸻

## Authority Hierarchy

Not all documentation is equally authoritative. The hierarchy is:

| Level | What it means | Examples |
|---|---|---|
| **Canon** | Foundational truth. Requires a deliberate change process with an ADR. | `CANON.md`, `thesis/`, foundational `ontology/` |
| **Specification** | Precise behaviour, schemas, and semantics derived from the Canon. | `interfaces/`, `contracts/`, `execution/`, `trust/`, `intent/` |
| **Architecture** | How specifications are realized in the current system design. | `architecture/`, `engineering/`, `data/`, `graph/` |
| **Decision Records** | Recorded reasoning for important architectural and canonical decisions. | `decisions/ADRs/` |
| **Research** | Hypotheses, experiments, and rejected ideas. May challenge Canon but does not become Canon automatically. | `research/` |
| **Reference** | Canonical concepts demonstrated in real scenarios. | `reference-workflows/` |
| **Strategy** | Commercial and organizational direction. | `strategy/`, `product/` |

When documents conflict, higher-authority documents take precedence.

When the Canon needs to change, the change must be deliberate, recorded in an ADR, and propagated to affected specifications and implementations.

⸻

## Key Principle

> The Model proposes. Noema decides.

Probabilistic AI may assist with interpretation, classification, entity resolution, and candidate generation. But consequential execution crosses a deterministic Trust boundary governed by explicit authority, policy, capability, constraints, evidence, and contracts.

No model output directly authorizes consequential execution. That is the architectural invariant at the heart of everything in this repository.

⸻

## Contributing

All contributions to canonical documentation must respect the authority hierarchy above.

Changes to Canon-level documents require an Architecture Decision Record (ADR). See `noema-canonical/decisions/README.md` for the format and process.

Terminology must remain consistent with the canonical glossary. If a term needs to change, the glossary must be updated first, and affected documents must be updated to match.
