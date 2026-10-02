> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

# Noema Canonical Glossary

Status: Foundational
Version: 0.2
Canonical Path: GLOSSARY.md

⸻

## Purpose

This Glossary defines the canonical meaning of every term used throughout the Noema architecture, documentation, specifications, contracts, APIs, and engineering discussions.

Its primary purpose is to prevent semantic drift across the Canon.

If a term has a defined meaning in the Canon, all Noema documentation MUST use that meaning consistently unless a document explicitly establishes a narrower, domain-specific usage.

For deeper treatment of any term, follow the reference to the relevant canonical document. This Glossary establishes shared vocabulary and critical distinctions. Detailed semantics belong in the relevant domain documents.

⸻

## Normative Language

| Term | Meaning |
|---|---|
| MUST | Absolute requirement |
| MUST NOT | Absolute prohibition |
| SHOULD | Recommended unless a justified exception exists |
| SHOULD NOT | Generally prohibited unless justified |
| MAY | Optional |
| CAN | Describes capability or possibility, not permission |

In particular: **CAN does not mean MAY.** A system can possess a Capability without possessing Authority to exercise it in a particular circumstance.

⸻

## A

---

### Action

A concrete operation that can be performed against a target or set of targets within a Noema execution journey.

Examples: `CreateAccount`, `RenewCard`, `CancelSubscription`, `TransferFunds`, `RefundPayment`.

An Action describes **what is done**, rather than what an Actor wants to accomplish.

Action ≠ Intent. An Intent may be satisfied by different Actions depending on Capability, Resource, Context, Policy, Constraint, and State.

See: `ontology/action.md`

---

### Action Contract

The explicit definition of what an Action requires, permits, guarantees, and may cause.

An Action Contract specifies:
- Inputs and Targets
- Preconditions
- Constraints
- Authority requirements
- Capability requirements
- Side Effects
- Expected Outcome
- Failure Conditions
- Postconditions
- Verification requirements

Execution occurs through Action Contracts, not through free-form model output.

See: `contracts/action-contract.md`

---

### Action Graph

The directed graph representing the available enterprise capabilities, their relationships, and execution dependencies.

The Action Graph is the semantic map through which Noema determines what can be done to satisfy a trusted Intent.

See: `architecture/action-graph.md`, `graph/enterprise-graph.md`

---

### Actor

An Entity capable of expressing an Intent, initiating an Action, or participating in an execution according to the applicable semantics.

Examples: Customer, Employee, Administrator, Service, Agent, Organization.

Conceptually: `Actor ⊂ Entity`. Not every Entity is an Actor.

See: `ontology/actor.md`

---

### Adapter

The executable boundary between Noema and a provider system.

An Adapter translates between Noema's canonical execution semantics and provider-specific protocols, identifiers, authentication mechanisms, errors, and operational behaviour.

Adapters are translation boundaries. They are not decision-makers. An Adapter must not determine whether an Action is permitted — that is the responsibility of Trust and Policy.

See: `integrations/adapters.md`

---

### Ambiguity

A condition in which an Intent, Entity reference, parameter, or other semantic value cannot be uniquely and deterministically resolved from available information.

Noema must not guess in the presence of material ambiguity. The correct response to unresolvable material ambiguity is Clarification.

See: `trust/ambiguity.md`, `intent/intent-ambiguity.md`

---

### Approval

The satisfaction of an explicit approval requirement by an authorized Actor.

Approval ≠ Authorization. Authorization establishes whether an Actor has authority within a scope. Approval satisfies a distinct approval-specific requirement.

Approval is a form of Evidence supporting a Trust decision.

---

### Attempt Identity

A stable identifier distinguishing one Execution Attempt from another within the same Execution lifecycle.

An Action may have multiple Execution Attempts (e.g. due to retries). Each Attempt must remain distinguishable for audit and recovery.

See: `execution/execution-model.md`, `interfaces/execution-api.md`

---

### Authority

The recognized basis by which an Actor is permitted to perform an Action, access or affect a Resource, or make a decision within a defined scope.

Authority answers: *Who or what is permitted to cause this Action or make this decision?*

Authority may arise from role, organizational position, delegated authority, policy, ownership, or explicit authorization.

Authority ≠ Capability. An Actor may possess Authority without the relevant Capability being available. A system may possess a Capability without the Actor possessing Authority to invoke it.

See: `ontology/capability.md`, `enterprise/permissions.md`

---

### Authorization

The determination that an Actor is permitted to perform a particular Action against a particular Entity or Resource under specified Context.

Authorization is one **dimension** of Trust, not a substitute for it.

`Authorized ≠ Trusted`

A valid, authorized Intent may still be blocked by Policy, Risk, Constraints, or insufficient Evidence.

See: `trust/authorization.md`

---

## B

---

### Bounded Autonomy

The principle that Noema's autonomous behaviour is always constrained by explicit Authority, Policy, Capability, and Contract.

Noema must never interpret instructions as permission to invent its own authority. Agents operate inside Noema's established boundaries; they do not define those boundaries.

See: `thesis/principles.md`, `CANON.md` (Invariant 17)

---

### Business Rule

A domain-specific rule describing business behaviour, eligibility, conditions, obligations, or permissible operations.

Business Rules may be expressed through Policy, Constraint, Action Contract, or enterprise system rules.

---

### Business State

The current state of a business Entity, Resource, or process maintained by the **authoritative enterprise system** for that domain.

Examples: `Account.balance`, `Payment.status`, `Card.status`, `Subscription.status`.

Noema may consume Business State through Context. Noema does not become the owner of Business State merely by representing it.

`Business State ≠ Intent State`

See: `enterprise/business-state.md`, `CANON.md` (Invariant 1, 24)

---

## C

---

### Candidate

A possible interpretation, Entity, Action, Capability, reference, or other semantic result produced during a resolution process.

A Candidate is **not** necessarily canonical.

`Candidate ≠ Resolved Value`

Candidates may be generated probabilistically. Material resolution requires applicable validation, evidence, authority, constraints, and deterministic rules.

---

### Canonical

The representation designated by Noema as the authoritative semantic representation for a particular concept within the applicable scope.

Canonical does not necessarily mean: source-of-record ownership, enterprise authority, physical persistence, or immutability.

---

### Capability

A defined ability to perform a class of Actions.

Examples: `account.read`, `card.renew`, `payment.refund`, `payment.transfer.create`.

Capability answers: *What can this system, service, or integration do?*

Capability does **not** answer whether the Action is permitted in the current situation.

`Capability ≠ Permission`
`Capability ≠ Authorization`
`Capability available ≠ Trust READY`

See: `ontology/capability.md`, `graph/capability-model.md`

---

### Clarification

A deterministic request for additional information required to resolve a material ambiguity, missing requirement, or insufficiently specified Constraint or Context.

Clarification is a **legitimate, governed lifecycle state** — not an error condition.

Clarification is preferable to guessing when the ambiguity is material to the decision or execution.

See: `intent/clarification.md`, `loops/clarification-loop.md`

---

### Closed-Loop Execution

The complete Noema model in which an Intent proceeds through resolution, context, validation, trust, action, execution, verification, and outcome — and the system maintains an auditable record at every stage.

---

### Compensation

A compensating Action that reverses or offsets the effects of a previously executed Action.

Compensation ≠ Cancellation. Cancellation prevents an Action from continuing. Compensation reverses or offsets an effect that has already occurred.

See: `execution/compensation.md`

---

### Concept

An abstract semantic type or category used to define domain meaning.

Concepts define categories. Entities represent identifiable instances of those categories.

See: `ontology/concepts.md`

---

### Confidence

A probabilistic estimate associated with a Model's output or inference.

`Model Confidence ≠ Trust`
`Model Confidence ≠ Authority`
`Model Confidence ≠ Truth`

A high Model Confidence value does not by itself authorize execution or establish canonical state.

See: `intent/confidence.md`

---

### Constraint

A condition, boundary, or restriction that limits the set of permissible interpretations, Actions, Resources, or Executions associated with an Intent.

Examples: `amount <= $10,000`, `approval required above $50,000`, `only use approved vendors`.

Constraint answers: *What must not be violated?*

A Policy may impose or generate a Constraint, but the Policy and resulting Constraint remain distinct.

A hard constraint violation must not silently become executable.

See: `ontology/constraint.md`

---

### Context

The bounded, relevant, authority-aware information available to Noema for interpreting Intent, resolving ambiguity, evaluating Trust, planning Actions, executing against enterprise systems, and verifying Outcomes.

Context answers: *What information is relevant to this decision or execution at this point in time?*

Context is not synonymous with Enterprise State, Business State, Evidence, Intent, or Conversation History.

Context may resolve ambiguity. Context must not manufacture authority.

See: `ontology/context.md`, `data/context.md`, `interfaces/context-api.md`

---

### Context Freshness

Whether Context is sufficiently current for the requirements of the relevant decision or Action.

Freshness is distinct from authority. Information may be authoritative but stale. Stale mandatory context must be re-acquired.

---

### Context Snapshot

A representation of relevant Context at a particular point in time.

A Context Snapshot does not become current enterprise truth merely because Noema stores it. The enterprise system remains authoritative.

---

## D

---

### Decision

An explicit determination made within Noema concerning interpretation, resolution, validation, authority, Trust, Action selection, clarification, escalation, rejection, or execution progression.

A Decision is not synonymous with Model Output. A Model may propose information used by a Decision. Noema establishes the Decision through deterministic rules, evidence, policy, authority, constraints, and the Trust model.

---

### Delegated Authority

Authority exercised by one Actor on behalf of another Actor or Principal under explicitly defined scope and constraints.

Delegation does not automatically transfer all Authority of the delegating Actor.

---

### Deterministic

Describes behaviour whose result is governed by defined inputs and explicit rules such that equivalent relevant inputs produce the same semantic decision.

Determinism applies to the governing decision logic, not necessarily to every upstream Model component.

`Deterministic ≠ Probabilistic`

---

### Durable Execution

The architectural capability to maintain a Noema execution lifecycle across time, retries, failures, approvals, waiting periods, external events, and process restarts without losing authoritative state.

See: `architecture/durable-execution.md`

---

## E

---

### Effective Constraint Set

The collection of all applicable Constraints that must be satisfied for a particular Action or Execution.

Includes: Intent Constraints + Actor Constraints + Policy Constraints + Authority Constraints + System Constraints + Capability Constraints + Execution Constraints.

---

### Effective Context

The Context that Noema has determined to be sufficiently relevant, scoped, current, and valid for a particular decision or Action.

Effective Context is Action-specific. Context valid for one operation may be insufficient for another.

---

### Entity

A distinct, identifiable thing that can be represented, referenced, related, observed, or acted upon within a Noema domain.

Examples: Customer, Account, Card, Payment, Invoice, Subscription, Organization, Document.

See: `ontology/entities.md`

---

### Entity Resolution

The process of determining which canonical Entity a reference refers to.

Material Entity Resolution must not silently rely on probability when deterministic resolution is required. Ambiguous resolution that is material to execution must produce a Clarification, not a guess.

---

### Evidence

Information that supports or contradicts a proposition, decision, Entity resolution, Context fact, or other material semantic claim.

Evidence answers: *What supports or contradicts this conclusion?*

Evidence ≠ Context. Context is information available for reasoning. Evidence describes support or contradiction for a specific proposition.

Evidence ≠ Authority. A source may be authoritative without every observation from it automatically being sufficient Evidence for every decision.

See: `trust/evidence.md`, `data/evidence.md`

---

### Execution

The actual invocation or performance of an Action against an internal or external system.

Execution is distinct from: Intent interpretation, planning, Action definition, authorization, Trust, and Outcome verification.

`Execution ≠ Outcome`

See: `execution/execution-model.md`, `interfaces/execution-api.md`

---

### Execution Attempt

A concrete attempt to invoke or perform an Action.

One Action may have multiple Execution Attempts. Each Attempt must remain distinguishable for audit and recovery.

---

### Execution Contract

The explicit, typed contract governing what a specific execution may do, what it requires, and what it guarantees.

The Execution Contract establishes the boundary between Noema's Trust decision and the physical execution of the Action. Execution occurs only through Execution Contracts.

See: `contracts/execution-contract.md`

---

### Execution Failure

A condition in which an Action cannot be successfully completed or its result cannot be established according to the applicable execution semantics.

Examples: Timeout, Unavailable Capability, Authorization Failure, Validation Failure, External System Error, Unknown Result.

Execution Failure ≠ Constraint Violation.

---

### Execution Result

The immediate technical result returned by an Execution Attempt.

Execution Result is not necessarily equivalent to final business Outcome. A successful technical response may still require Outcome verification.

---

## F

---

### Fail-Closed

The principle that Noema must not default to permitting execution when mandatory conditions cannot be established.

`UNKNOWN mandatory condition → NOT READY`

Fail-closed does not require permanent denial. An unresolved condition may transition to WAITING and be re-evaluated when the condition becomes established.

See: `CANON.md` (Invariants 9, 28, 29)

---

### Failure Class

A canonical classification of Execution Failures that determines recovery behaviour.

Examples: `VALIDATION_FAILURE`, `AUTHORIZATION_FAILURE`, `PRECONDITION_FAILURE`, `TRANSIENT_FAILURE`, `PERMANENT_FAILURE`, `TIMEOUT`, `UNKNOWN`, `CONFLICT`, `PROVIDER_FAILURE`, `INTERNAL_FAILURE`.

See: `execution/failure.md`

---

## H

---

### Human Intervention

An explicit lifecycle state in which Noema stops autonomous progression and requires a human to take action.

Human Intervention is not necessarily failure. It is a legitimate outcome of bounded autonomy.

Examples: Intent remains ambiguous, Evidence unavailable, Policy requires approval, Risk controls require intervention, unexpected execution outcome.

See: `execution/human-intervention.md`, `CANON.md` (Invariant 25)

---

## I

---

### Idempotency

The property of an operation that can be performed multiple times without producing different effects after the first execution.

Noema must distinguish logical Action idempotency from execution attempt identity. Retries must not accidentally create new logical Actions.

See: `execution/idempotency.md`, `engineering/idempotency.md`

---

### Intent

The desired objective or outcome expressed or implied by an Actor.

Example: `"Renew my expired card."` resolved into a canonical Intent object containing Actor, Objective, Target, Constraints, and Context.

Intent describes **what the Actor wants to accomplish**. It is not an Action.

Intent ≠ Prompt. A prompt is an interface artifact. An Intent is a canonical semantic object.
Intent ≠ Action. Intent determines the semantic objective. Action determines what will be executed.

Once admitted into the Trust path, an Intent version is immutable. Material changes create a new version.

See: `ontology/intent.md`, `intent/intent-model.md`

---

### Intent Lifecycle

The sequence of states an Intent passes through from expression to completion.

Conceptual states include: `RECEIVED`, `INTERPRETING`, `AMBIGUOUS`, `RESOLVED`, `VALIDATING`, `TRUSTED`, `EXECUTING`, `COMPLETED`, `FAILED`, `CANCELLED`.

Intent Lifecycle ≠ Trust Lifecycle ≠ Execution Lifecycle. These are distinct state machines.

See: `intent/intent-lifecycle.md`

---

### Intent Parameter

A structured value required to sufficiently specify an Intent.

Examples: `destination = London`, `amount = $500`, `date = 2026-09-12`.

A missing material Intent Parameter may produce a Clarification Requirement.

---

### Intent Resolution

The process of transforming an expressed request into a canonical, structured Intent representation.

A model may propose interpretations during this process. Model output is not automatically canonical Intent.

See: `intent/intent-resolution.md`

---

## L

---

### Lineage

The trace connecting information to its source, transformations, semantic use, and resulting decisions or Outcomes.

Lineage is a form of Provenance.

---

## M

---

### Model

A probabilistic computational system used to interpret, classify, generate, infer, retrieve, transform, or otherwise process information.

The Model is a component within Noema. It is not the canonical authority for Trust or enterprise Business State.

---

### Model Confidence

See: **Confidence**

---

### Model Inference

A conclusion generated by a Model that is not directly established by authoritative Evidence.

Model Inference must remain distinguishable from: observed fact, canonical state, authoritative Context, Evidence, and validated resolution.

---

### Model Proposal

A candidate semantic interpretation or operation proposed by a Model for Noema to evaluate.

A Model Proposal becomes canonical only through the applicable resolution and validation process.

---

## O

---

### Observation

Information recorded from a source at a particular point in time.

An Observation is not necessarily equivalent to current Business State.

---

### Objective

The desired result represented by an Intent.

The Objective describes what the Actor seeks to accomplish. It is not itself the executable Action.

---

### Operational Memory

The historical record of Noema's intent and execution history, used for auditability, reconciliation, and operational learning.

Operational Memory does not assert business truth. It records what Noema did, observed, and decided.

See: `architecture/operational-memory.md`

---

### Ontology

The formal vocabulary of concepts, Entities, relationships, distinctions, properties, and semantic rules used to represent the Noema domain.

The ontology defines: *What things mean and how they relate.*

See: `ontology/`

---

### Outcome

The observable result of an attempted or completed Action, as verified by Noema against the expected postconditions.

Outcome ≠ Execution Result. An execution may return a successful technical result, but the Outcome is established only after Noema verifies postconditions.

Expected Outcome ≠ Observed Outcome. Both must remain distinct.

Outcome Verification is the process of determining whether the Observed Outcome satisfies the Expected Outcome and applicable Postconditions.

See: `ontology/outcome.md`, `architecture/outcome-engine.md`

---

## P

---

### Partial Execution

The condition in which some components of a composite Intent have executed while others have not.

Partial execution must be explicitly permitted by the Intent semantics or governing Contract. Noema must not assume that a composite Intent may be partially executed merely because some components are READY.

---

### Planning

The process of determining what sequence or composition of Actions can satisfy a trusted Intent.

Planning does not create authority. A Planner cannot: create a Capability, create permission, override Policy, bypass Trust, bypass Action Contracts, invent enterprise state, or convert uncertainty into authorization.

See: `execution/planning.md`, `architecture/execution-planner.md`

---

### Policy

A governing rule or organizational, regulatory, business, or system requirement that establishes permissible behaviour, eligibility, obligations, restrictions, or decision requirements.

A Policy may generate or impose one or more Constraints.

Policy ≠ Trust. Policy satisfaction is one dimension of Trust, not equivalent to Trust READY.

See: `ontology/policy.md`, `trust/policy-evaluation.md`

---

### Postcondition

A condition that must hold after execution for the Outcome to be considered verified and complete.

See: `execution/postconditions.md`

---

### Precondition

A condition that must hold before execution of an Action may begin.

See: `execution/preconditions.md`

---

### Probabilistic

Describes behaviour whose result is influenced by uncertainty, probability, statistical inference, or Model behaviour.

Probabilistic generation does not automatically constitute deterministic authorization.

Noema uses probabilistic components for: interpretation, candidate generation, extraction, classification, retrieval, and ranking. All probabilistic output must pass the deterministic Trust boundary before it can affect execution.

---

### Provenance

Information describing the origin, derivation, observation, transformation, or lineage of a fact, Entity, decision input, or other information.

Provenance answers: *Where did this information come from, when was it observed, and how did it become part of the current semantic representation?*

Provenance is particularly important for consequential Context, Evidence, Entity Resolution, Decisions, and Outcomes.

See: `data/provenance.md`

---

## R

---

### READY (Trust State)

The Trust State indicating that, at the evaluated time and under the evaluated conditions, the Intent satisfies all applicable Trust requirements for execution eligibility.

READY ≠ SUCCESS. READY does not guarantee execution success.
READY is not permanent. A READY Intent may become invalid if authorization changes, policy changes, Evidence expires, or Context changes.

There is no direct WAITING → READY or BLOCKED → READY transition. The canonical path is: → EVALUATING → READY.

---

### Reconciliation

The process of establishing the actual external state after an Execution Attempt produces an UNKNOWN outcome (e.g. due to timeout or connection failure).

UNKNOWN ≠ FAILED. UNKNOWN means Noema cannot establish whether the operation occurred. FAILED means Noema has sufficient evidence the operation failed.

See: `execution/failure.md`, `interfaces/execution-api.md`

---

### Resolution

The process of determining a canonical interpretation for an ambiguous, incomplete, non-canonical, or natural-language input.

Resolution may apply to: Intent, Entity, Action, Capability, Reference, Context, parameters, or other semantic values.

Resolution ≠ Validation. Resolution determines what the input means. Validation determines whether the resolved representation satisfies requirements.

---

### Resource

An Entity occupying a role as an object of an Action.

`Resource ⊂ Entity` where the Entity is relevant as something that an Action may inspect, create, modify, or otherwise affect.

See: `ontology/resource.md`

---

### Risk

The potential consequence profile associated with an Intent or Action.

Risk may determine: required Evidence, approval requirements, confirmation requirements, execution limits, autonomy requirements, and additional controls.

Risk does not necessarily imply denial.

`Risk Acceptable ≠ Trust READY`

See: `trust/risk.md`

---

## S

---

### Schema

A structural representation of information.

Schema describes: *How information is represented.*
Ontology describes: *What that information means.*

An implementation Schema must not redefine canonical ontology semantics without an explicit semantic change.

---

### Semantic Contract

An explicit definition of the meaning, structure, requirements, boundaries, or guarantees associated with a Noema concept.

Semantic Contracts establish stable meaning independently of implementation details.

---

### Side Effect

A material change or externally observable consequence caused by an Action beyond merely returning information.

Examples: Sending an email, Charging a card, Changing account state, Creating a record, Issuing a notification.

Side Effects are relevant to Action Contracts, Trust, Constraints, and Outcome verification.

---

### State

The condition of an Entity, Resource, system, workflow, or process at a particular point in time.

State is temporal and may change.

Important conditions must be represented as explicit state rather than inferred from side effects or application behaviour.

See: `ontology/state.md`

---

### System of Record

The authoritative system responsible for maintaining a particular category of enterprise Business State.

Examples: Banking System → account balance; CRM → customer profile; Billing System → subscription status.

Enterprise systems remain authoritative for their business domains. Noema defers to them and must not silently create a competing source of truth.

See: `enterprise/system-of-record.md`, `CANON.md` (Invariant 24)

---

## T

---

### Taxonomy

A hierarchical classification of Concepts or other semantic categories.

Ontology is broader than Taxonomy. A taxonomy describes classification. An ontology also describes relationships, properties, boundaries, and semantics.

See: `taxonomy/`

---

### Trust

Noema's explicit, deterministic determination that a proposed interpretation, Entity resolution, Action, or execution satisfies the conditions required for progression across the applicable decision boundary.

Trust answers: *May Noema permit this operation to proceed under the applicable evidence, authority, policy, constraints, Context, and risk conditions?*

Trust is **not**:
- Model Confidence
- Capability
- Authority
- Evidence in isolation
- Permission in isolation
- Successful execution

Trust is evaluated across applicable dimensions including: Resolution, Evidence, Authorization, Policy, Risk, Capability, Constraints, Context, Freshness.

Trust is a Noema-controlled decision boundary.

See: `trust/trust-model.md`, `architecture/trust-engine.md`

---

### Trust Boundary

The architectural decision boundary at which Noema transitions from interpretation, proposal, or planning into permitted consequential behaviour.

The Trust Boundary is distinct from the AI model itself.

---

### Trust Decision

A deterministic determination concerning whether Noema may permit a proposed Intent, Entity resolution, Action, or Execution to proceed.

Canonical Trust outcomes: `READY`, `WAITING`, `BLOCKED`, `CLARIFICATION_REQUIRED`.

Every non-ready decision must expose deterministic reasons.

See: `trust/trust-model.md`

---

### Trust State Machine

The explicit state machine governing how Trust state evolves over time.

Canonical states: `UNRESOLVED`, `EVALUATING`, `WAITING`, `BLOCKED`, `READY`.

There are no probabilistic transitions. Every state transition is governed by explicit predicates.

No direct WAITING → READY. No direct BLOCKED → READY. Each requires passing through EVALUATING.

WAITING ≠ BLOCKED:
- WAITING = not yet (condition may be satisfied)
- BLOCKED = prohibited (condition denies progression)

See: `trust/trust-state-machine.md`

---

## U

---

### UNKNOWN (State)

A system state in which Noema cannot establish a required fact, interpretation, Entity, Context value, decision, or execution result with sufficient certainty.

`UNKNOWN ≠ FALSE`
`UNKNOWN ≠ VALID` (for validation)
`UNKNOWN ≠ ALLOWED` (for authorization)
`UNKNOWN ≠ FAILED` (for execution)

Material uncertainty must be represented explicitly rather than defaulting to a permitted or successful state.

For consequential execution: `UNKNOWN mandatory condition → NOT READY` (fail-closed).

---

## V

---

### Validation

The deterministic verification layer for establishing that a resolved Intent is structurally complete, semantically applicable, and consistent with the explicit rules, references, Evidence, constraints, and Context required for its next lifecycle transition.

Validation is deterministic. It is not a probability or confidence score.

Validation ≠ Trust. A valid Intent may remain blocked.
Validation must not guess. If Validation cannot establish a required fact, it must represent that explicitly as UNKNOWN or INCOMPLETE.
Validation must not silently modify the Intent to make it valid.

Canonical result states: `VALID`, `INVALID`, `INCOMPLETE`, `UNKNOWN`.

See: `trust/validation.md`

---

### Version (Intent)

Trust belongs to a specific Intent version. A material change to an Intent creates a new version requiring a new Trust evaluation.

Trust must not silently carry across material Intent changes.

---

## W

---

### WAITING (Trust State)

A Trust State indicating that a required condition has not yet been satisfied but may become satisfied.

WAITING ≠ BLOCKED. WAITING means "not yet". BLOCKED means "prohibited".

Examples: `WAITING_FOR_CLARIFICATION`, `WAITING_FOR_EVIDENCE`, `WAITING_FOR_AUTHORIZATION`, `WAITING_FOR_CONFIRMATION`, `WAITING_FOR_APPROVAL`, `WAITING_FOR_CAPABILITY`.

A WAITING Intent may re-enter EVALUATING when the required condition is satisfied.

---

## Key Distinctions Reference

The following pairs are not interchangeable. Conflating them violates the canonical architecture.

| These are NOT the same | Why |
|---|---|
| Intent ≠ Action | Intent = desired objective. Action = executable operation. |
| Intent ≠ Prompt | Prompt = interface artifact. Intent = canonical semantic object. |
| Resolution ≠ Validation | Resolution = what it means. Validation = whether it is correct. |
| Validation ≠ Trust | Valid ≠ Trusted. |
| Trust ≠ Authorization | Authorization is one Trust dimension, not a substitute. |
| Trust ≠ Confidence | Confidence is probabilistic. Trust is a deterministic decision boundary. |
| Capability ≠ Permission | CAN does not mean MAY. |
| Execution ≠ Outcome | Execution = attempt. Outcome = verified result. |
| Business State ≠ Intent State | Enterprise systems own business state. Noema owns Intent state. |
| WAITING ≠ BLOCKED | WAITING = not yet. BLOCKED = prohibited. |
| READY ≠ SUCCESS | READY = eligible to execute. SUCCESS = verified business result. |
| UNKNOWN ≠ FALSE | Unknown is not equivalent to denied or failed. |
| UNKNOWN ≠ VALID | Unknown mandatory condition must not default to valid. |
| Approval ≠ Authorization | Separate requirements with separate authority and evidence. |
| Confirmation ≠ Approval | Confirmation = Actor confirms. Approval = separate authority grants permission. |
| Observation ≠ Business Truth | Noema observes; enterprise systems are authoritative. |
| Model Output ≠ Canonical State | Model proposals must pass resolution and validation before becoming canonical. |
| Risk ≠ Trust | Risk assessment is one input to Trust, not equivalent to it. |
| Policy ≠ Trust | Policy satisfaction is one Trust dimension, not a substitute for Trust READY. |
| Cancellation ≠ Compensation | Cancellation prevents; compensation reverses. |

⸻

## Further Reading

For detailed semantics of any term, refer to the canonical domain documents:

- Ontology: `ontology/`
- Intent: `intent/`
- Trust: `trust/`
- Execution: `execution/`
- Contracts: `contracts/`
- Architecture: `architecture/`
- Interfaces: `interfaces/`
- Data: `data/`
- Engineering: `engineering/`
- Enterprise: `enterprise/`
- Full canonical vocabulary: `ontology/glossary.md`
- Canonical invariants and principles: `CANON.md`
