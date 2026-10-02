> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Concepts

Status: Foundational Draft
Version: 0.2
Domain: Ontology
Canonical Path: ontology/concepts.md

⸻

1. Purpose

This document defines the major concepts that constitute the Noema ontology and establishes the relationships between them.

It is an ontology map, not the detailed specification of every concept.

The individual ontology documents are authoritative for the detailed semantics of each concept.

The purpose of this document is to answer:

What are the fundamental things that exist in the Noema model, and how do they relate to one another?

Noema is an execution infrastructure layer between a source of Intent and enterprise systems capable of producing consequential outcomes. The source of Intent may be a human, an agent, or another system.

The ontology therefore models not only interpretation, but also state reconstruction, authorization, policy, bounded action, execution, verification, and provenance. Noema Master Company Document FINAL.pdf

⸻

2. The Noema Ontology

At its highest level, Noema models the transformation of an expressed Intent into a trusted, bounded, executable, and verifiable enterprise outcome.

Actor / Source
      │
      │ expresses
      ▼
   Intent
      │
      │ contextualized by
      ▼
   Context
      │
      │ resolved against
      ▼
Evidence + Enterprise State
      │
      ▼
Intent Resolution
      │
      ▼
Trust Decision
      │
      ├── REJECT
      ├── CLARIFY
      ├── CONFIRM
      ├── WAIT
      ├── ESCALATE
      ├── UNKNOWN
      └── ALLOW
             │
             ▼
          Action
             │
       requires / bounded by
             │
             ├── Capability
             ├── Authority
             ├── Policy
             ├── Constraint
             └── Contract
             │
             ▼
          Execution
             │
             ▼
       Verification
             │
             ▼
          Outcome
             │
             ▼
     Verified Business State

The Trust Decision is not merely a confidence threshold. It is a deterministic control boundary between probabilistic interpretation and consequential execution.

The POC defines seven Trust outcomes: ALLOW, CLARIFY, CONFIRM, WAIT, ESCALATE, REJECT, and UNKNOWN. NOEMA POC Specification_1.pdf

This lifecycle exists within additional concepts including:

* Identity
* Principal
* Actor
* Role
* Authority
* Delegation
* Policy
* Constraint
* Evidence
* Confidence
* Trust
* Resource
* Capability
* Contract
* State
* Execution
* Outcome
* Provenance
* System

These concepts constrain, explain, or contextualize the primary lifecycle.

⸻

3. Conceptual Layers

The Noema ontology can be understood through five conceptual layers.

Layer 1 — Participation and Identity

Who or what is participating?

* Identity
* Principal
* Actor
* Role
* Organization
* System
* Delegation

A Principal must be established by authentication and identity infrastructure, not inferred from model-generated prose. Model output may propose an interpretation of a request, but it cannot establish the authenticated principal. Noema Master Company Document FINAL.pdf

⸻

Layer 2 — Intent and State Understanding

What is someone trying to accomplish, and what is true now?

* Intent
* Objective
* Context
* Resource
* Business State
* Evidence
* Constraint
* State
* Intent Resolution

Noema must resolve Intent against relevant enterprise state rather than treating the language expression as sufficient by itself.

Enterprise state may be fragmented across multiple systems and may contain stale, contradictory, incomplete, or unavailable information. The ontology therefore treats state and evidence as first-class inputs to resolution.

⸻

Layer 3 — Trust and Authorization

Why is Noema justified in proceeding?

* Authority
* Authorization
* Policy
* Evidence
* Trust
* Confidence
* Risk
* Provenance

Trust is established from explicit, inspectable inputs.

Authorization must be evaluated against the specific Actor or Principal, Action, Target, and applicable Context.

The POC distinguishes three authorization layers:

1. Technical authorization — whether the principal may invoke the capability.
2. Policy authorization — whether the parameterization satisfies applicable static rules.
3. Business authorization — whether the fully resolved action against the reconstructed enterprise state should be permitted at that moment. NOEMA POC Specification_1.pdf

⸻

Layer 4 — Bounded Execution

What can actually be done, and under what explicit terms?

* Action
* Capability
* Contract
* Execution
* Preconditions
* Postconditions
* Idempotency
* Side Effects
* Recovery
* Verification

Consequential execution must occur only through explicitly registered and bounded capabilities.

A model-generated tool call is not itself a trusted executable capability. The capability must exist in the registered capability set and the resulting Action must pass the applicable controls. NOEMA POC Specification_1.pdf

⸻

Layer 5 — Result and Accountability

What actually happened, what state was verified, and why?

* Outcome
* Business State
* Execution State
* Verification
* Provenance
* Audit
* Operational Memory

Noema must distinguish an execution attempt from its actual downstream consequence.

A successful transport response is not sufficient evidence of successful business execution. Actual state must be verified where the relevant system permits verification.

⸻

4. Foundational Concepts

The following concepts form the primary vocabulary of Noema.

⸻

4.1 Actor

An Actor is an entity participating in the Intent-to-Action lifecycle.

An Actor may be:

* a human
* an organization
* a service
* an automated agent
* another system
* a delegated representative

Actor answers:

Who or what is participating?

Actor is distinct from Identity, Principal, Authority, and Role.

Canonical definition:

01-ontology/actor.md

⸻

4.2 Intent

An Intent represents a desired objective or state of affairs expressed by an Actor, agent, or system.

Intent answers:

What is being requested or what outcome is being sought?

Natural-language input is an expression of Intent, not the canonical executable representation.

Noema’s Intent Engine may use probabilistic inference to construct a strictly typed Intent Object, but the resulting object must cross a schema-validation boundary before downstream components consume it. NOEMA POC Specification_1.pdf

An admitted Intent Object is immutable. A material change creates a new version that explicitly supersedes the previous version rather than silently mutating it. NOEMA POC Specification HTML.html

Canonical definition:

01-ontology/intent.md

⸻

4.3 Context

Context is the information relevant to interpreting, validating, trusting, executing, and verifying an Intent or Action.

Context may include:

* Actor and Principal information
* resource information
* enterprise business state
* system state
* temporal information
* organizational context
* prior valid Intent versions
* policy
* capability availability
* authorization information
* evidence
* previous execution state
* relevant external information

Context answers:

What information is necessary to understand and safely act on this Intent?

Context is not a generic unrestricted data feed.

Noema should use minimum necessary data and scope information to the investigation or execution at hand. Enterprise systems remain authoritative for business state. NOEMA POC Specification PDF.pdf

Canonical definition:

01-ontology/context.md

⸻

4.4 Action

An Action is a bounded operation that can advance an Intent.

Action answers:

What operation can be performed to advance the Intent?

An Action is not an execution attempt and is not an outcome.

An Action must be sufficiently specified to identify its target, parameters, constraints, required authority, required capability, and applicable execution contract.

Canonical definition:

01-ontology/action.md

⸻

4.5 Capability

A Capability is an explicit, registered ability of a system or execution environment to perform an operation.

Capability answers:

What can this system actually do?

Capability does not establish:

* permission
* authority
* trust
* business authorization
* current availability
* successful execution

Enterprise capabilities are allowlisted and typed. Arbitrary HTTP, arbitrary SQL, or arbitrary model-generated tool definitions are not capabilities merely because a system can technically reach them. Noema Master Company Document FINAL.pdf

Canonical definition:

01-ontology/capability.md

⸻

4.6 Outcome

An Outcome represents what actually happened as a consequence of execution or an execution attempt.

Outcome answers:

What actually happened?

Outcome must be grounded in observed evidence.

Possible execution-related conditions include:

* successful
* partially completed
* failed
* unknown
* contradicted by downstream state

A timeout is not automatically a failure or success. It produces an unknown execution outcome that must be resolved through verification. NOEMA POC Specification PDF.pdf

Canonical definition:

01-ontology/outcome.md

⸻

5. Supporting Concepts

The following concepts support the primary lifecycle.

⸻

5.1 Identity

Identity represents the recognized identity of an entity.

Identity answers:

Who is this entity?

Identity is not equivalent to:

* Actor
* Principal
* Authority
* Permission
* Trust

Authentication and identity infrastructure establish the Principal used by downstream authorization. A model must not establish or redefine the Principal through natural-language interpretation. Noema Master Company Document FINAL.pdf

Canonical identity semantics belong to the relevant identity and security specifications.

⸻

5.2 Principal

A Principal is the authenticated or otherwise authoritative security subject on whose identity authorization decisions are evaluated.

Principal answers:

Which authenticated security subject is this request being evaluated for?

The Principal is not inferred from model prose.

The canonical security relationship is:

Authentication / Identity Layer
              │
              ▼
          Principal
              │
              ├── Action
              ├── Target
              └── Context
                    │
                    ▼
             Authorization

Principal and Actor may refer to the same real-world entity, but they are not interchangeable concepts.

For example, an authenticated human may be the Principal while participating as an Initiator, while a service or agent may be the Executor.

This distinction is essential for authorization, delegation, audit, and confused-deputy protection.

⸻

5.3 Authority

Authority represents the permission or delegated ability of an Actor or Principal to cause a particular operation under defined conditions.

Authority answers:

What may this Actor or Principal legitimately cause?

Authority may depend on:

* Principal
* Actor
* Action
* target
* resource ownership
* organizational role
* delegation
* policy
* temporal conditions
* risk
* approval requirements
* current state

Authority is not Capability.

Capability establishes technical possibility.

Authority establishes whether the relevant participant may cause the operation.

⸻

5.4 Policy

A Policy is a rule or set of rules governing what may occur under defined conditions.

Policy answers:

What rules govern this Intent, Action, or execution?

Policies may originate from:

* enterprise organizations
* regulatory requirements
* system owners
* security controls
* product rules
* Noema configuration

Policy may affect:

* Intent resolution
* authorization
* Trust
* Action selection
* execution
* escalation
* verification

Policy is versioned.

Where policy evaluation materially affects a Trust Decision, the governing policy version must be recorded.

In the POC, policy resolution is keyed to the timestamp at which the Intent Object is admitted to the Trust Engine, rather than silently changing because execution occurs later. NOEMA POC Specification_1.pdf

Canonical definition:

01-ontology/policy.md

⸻

5.5 Constraint

A Constraint is a condition that limits the permissible interpretation, planning, or execution of an Intent or Action.

Constraint answers:

What must remain true, or what must not be violated?

Examples:

amount <= configured_limit
departure_time >= 09:00
only approved vendors
do not contact customer by SMS

Constraints may originate from:

* Actor
* Intent
* Policy
* Contract
* system requirements
* regulatory requirements

Constraints must survive translation from Intent into Action and execution.

Canonical definition:

01-ontology/constraint.md

⸻

5.6 Evidence

Evidence is information used to support or challenge a proposition relevant to Intent resolution, Trust, authorization, execution, or verification.

Evidence answers:

What supports this conclusion?

Examples include:

* authenticated identity information
* enterprise system records
* policy records
* authorization records
* API responses
* explicit user statements
* execution results
* verified downstream state
* external data

Evidence must have provenance.

Tool responses and retrieved enterprise content are evidence, not instructions. Model output is not sufficient provenance for a consequential decision. NOEMA POC Specification PDF.pdf

Evidence may be:

* known
* inferred
* ambiguous
* unavailable
* stale
* contradictory
* unknown
* unauthorized

The POC uses these statuses explicitly during state reconstruction. NOEMA POC Specification HTML.html

Canonical definition:

01-ontology/evidence.md where applicable.

⸻

5.7 Trust

Trust represents Noema’s deterministic determination that sufficient grounds exist for a particular transition toward Action or Execution.

Trust answers:

Has Noema established sufficient grounds to proceed with this specific request under the current applicable conditions?

Trust is not:

* model confidence
* generic system trust
* permission
* capability
* authentication

Trust is derived from explicit inputs including:

* resolved Intent
* Principal and Actor context
* target
* reconstructed state
* evidence
* authority
* authorization
* policy
* constraints
* risk
* required confirmation or approval
* capability availability
* other applicable execution conditions

The Trust boundary separates probabilistic interpretation from deterministic consequence. Noema’s architecture requires probabilistic inference to propose and deterministic controls to decide. NOEMA POC Specification_1.pdf

Canonical Trust decisions must be explicit and machine-readable.

⸻

5.8 Confidence

Confidence represents the degree of certainty associated with a probabilistic interpretation or inference.

Confidence answers:

How strongly does the probabilistic interpretation support this hypothesis?

Confidence may assist Intent interpretation, candidate generation, ranking, or other probabilistic tasks.

It does not itself establish:

* Trust
* Authority
* Authorization
* business truth
* permission to execute

A high-confidence interpretation of an unauthorized, ambiguous, stale, or incorrect target remains non-executable.

The POC explicitly requires confused-deputy protection regardless of confidence level. NOEMA POC Specification PDF.pdf

⸻

5.9 Resource

A Resource is an entity that an Action may operate on, inspect, create, modify, or otherwise affect.

Examples:

* Customer
* Account
* Card
* Subscription
* Invoice
* Document
* Payment
* Employee
* Transaction
* Case

Resources frequently belong to enterprise systems of record.

A Resource is especially important to authorization because authorization must bind to the specific resolved target rather than merely to a general capability.

This target binding is the structural control against confused-deputy failures. NOEMA POC Specification_1.pdf

Canonical definition:

01-ontology/resource.md

⸻

5.10 System

A System is a software or technological environment that stores state, exposes capabilities, or executes operations.

Examples:

* CRM
* Banking Platform
* Payment Processor
* Identity Provider
* ERP
* Notification Service
* Database

A System may provide or consume Capabilities without becoming part of Noema itself.

The authoritative business state remains in the relevant enterprise System of Record.

⸻

5.11 State

State represents the condition of an entity or process at a particular point in time.

Noema must distinguish:

* Intent State
* Context State
* Trust State
* Action State
* Execution State
* Outcome State
* Noema State
* Business State

Business State remains authoritative in the relevant enterprise system.

Noema reconstructs state for decision-making; it must not rewrite authoritative business truth by inference. Noema Master Company Document FINAL.pdf

State may explicitly represent uncertainty.

Relevant states include:

* KNOWN
* INFERRED
* AMBIGUOUS
* UNAVAILABLE
* STALE
* CONTRADICTORY
* UNKNOWN
* UNAUTHORIZED

Unknown and contradictory states are not implementation defects to be silently smoothed away. They are valid conditions that may force clarification, escalation, waiting, rejection, or verification.

⸻

5.12 Provenance

Provenance describes where information, decisions, Actions, executions, and Outcomes came from.

Provenance answers:

Where did this information, decision, or transition originate?

Material provenance may include:

* source system
* Principal
* Actor
* Intent Object version
* target
* evidence source
* policy version
* capability version
* contract version
* execution identifier
* idempotency key
* workflow transition
* verification result
* timestamp

Noema’s audit must reconstruct business causality, not merely model activity.

A record such as “agent called get_transaction()” is insufficient provenance for a consequential decision. The audit record must be able to explain who initiated the request, what was intended, what was ambiguous, what authority existed, what policy applied, what state was observed, what evidence supported the decision, what was executed, and what was verified. NOEMA POC Specification PDF.pdf

Canonical definition:

01-ontology/provenance.md where applicable.

⸻

6. Derived Concepts

Some Noema concepts arise primarily from relationships between foundational concepts.

⸻

6.1 Delegation

Delegation is a relationship in which one Actor or Principal permits another Actor to act on its behalf.

Principal
    │
    │ delegates
    ▼
Delegation
    │
    ├── permitted Actions
    ├── scope
    ├── conditions
    ├── duration
    └── revocation
    │
    ▼
Delegate

Delegation affects effective Authority.

Delegation must preserve the distinction between:

* Principal
* Delegate
* authority granted
* Action
* target
* scope
* conditions

A Delegate does not become the Principal merely because it performs the Action.

⸻

6.2 Role

A Role describes how an Actor participates in an Intent, Action, or workflow.

Examples:

* Initiator
* Principal
* Delegate
* Beneficiary
* Approver
* Executor
* Observer

Role does not define Actor identity.

The same Actor may occupy multiple roles.

⸻

6.3 Authorization

Authorization is the evaluation of whether a Principal or Actor is permitted to cause a particular Action against a particular target under particular conditions.

A useful conceptual model is:

Principal / Actor
        +
Action
        +
Target
        +
Context
        +
Policy
        +
Authority
        ↓
Authorization Decision

Authorization must not be reduced to generic tool access.

The Noema POC explicitly separates:

Technical Authorization
        ↓
Policy Authorization
        ↓
Business Authorization

Technical authorization determines whether the principal may invoke the capability.

Policy authorization determines whether the requested parameterization satisfies static rules.

Business authorization determines whether the fully resolved operation against the reconstructed current enterprise state should be permitted.

Target-bound authorization is required to prevent a technically authorized Actor from causing an Action against an unauthorized or incorrect resource. NOEMA POC Specification_1.pdf

⸻

6.4 Intent Resolution

Intent Resolution is the deterministic process of converting a validated Intent representation plus relevant Context and Evidence into a sufficiently specified interpretation for downstream Trust evaluation.

It may include:

* entity resolution
* target resolution
* transaction or resource candidate generation
* ambiguity detection
* state reconstruction
* evidence reconciliation
* constraint extraction
* required Action identification

Intent Resolution must not silently guess when material ambiguity remains.

If multiple candidate resources remain materially indistinguishable, the system must represent that ambiguity and transition appropriately rather than selecting one merely because it has the highest probabilistic score.

⸻

6.5 State Reconstruction

State Reconstruction is the process of assembling the relevant current enterprise state from authoritative or otherwise qualified sources.

Enterprise Source A
        +
Enterprise Source B
        +
Enterprise Source C
        +
Temporal Context
        +
Evidence Quality
        ↓
State Reconstruction
        ↓
KNOWN / STALE / CONTRADICTORY / UNKNOWN / ...

The purpose is not to create a competing system of record.

The purpose is to establish what Noema can responsibly know about the state relevant to the Intent and Action.

Conflicting enterprise sources must remain distinguishable. Noema must not average conflicting state or select the more convenient source without an explicit rule.

⸻

6.6 Execution

Execution is the actual attempt to perform an Action through an authorized, registered, bounded Capability.

Action
   ↓
Contract Validation
   ↓
Capability Resolution
   ↓
Authority / Authorization
   ↓
Execution Gate
   ↓
Execution Attempt
   ↓
Observed Result
   ↓
Verification

Execution is distinct from:

* Action selection
* Capability existence
* API invocation
* Outcome
* Business State

The executor must revalidate the relevant conditions immediately before consequential execution because state, policy, authority, and other conditions may have changed since planning.

The Noema architecture explicitly requires executor-side revalidation immediately before action. Noema Master Company Document FINAL.pdf

⸻

6.7 Contract

A Contract defines explicit executable semantics and constraints for an Action or Capability.

A Contract may define:

* typed inputs
* typed outputs
* target requirements
* preconditions
* postconditions
* authorization requirements
* side effects
* failure semantics
* idempotency semantics
* retry semantics
* version
* verification method

Contracts are the mechanism through which ontology-level meaning becomes executable boundary conditions.

A typed Action Contract must be validated before execution.

The contract must not be treated as merely descriptive documentation.

⸻

6.8 Verification

Verification is the process of determining whether the expected real-world or enterprise-state consequence of an execution actually occurred.

Execution Attempt
       ↓
Observed Response
       ↓
Source-of-Truth Query
       ↓
Postcondition Check
       ↓
Verified Outcome

Verification is distinct from reading an API success code.

For uncertain execution, Noema must verify the downstream state before retrying or claiming success.

The principle is:

A timeout creates uncertainty; verification resolves uncertainty.

⸻

6.9 Recovery

Recovery describes the controlled handling of execution uncertainty, failure, partial completion, duplication, unavailable dependencies, and other exceptional states.

Recovery may include:

* verification
* safe retry
* waiting
* compensation
* escalation
* clarification
* termination

Recovery must respect Action contracts, idempotency semantics, policy, authority, and observed state.

Noema must not use blind retries to resolve uncertainty.

⸻

7. Primary Relationships

The most important relationships in the Noema ontology are:

Actor / Source
  │
  ├── expresses ─────────────► Intent
  │
  ├── participates in ──────► Action
  │
  └── may possess/exercise ─► Authority
Identity
  │
  │ establishes
  ▼
Principal
  │
  └── evaluated in ─────────► Authorization
Intent
  │
  ├── has ───────────────────► Context
  ├── contains ──────────────► Constraint
  ├── refers to ─────────────► Resource
  └── motivates ─────────────► Action
Context
  │
  ├── contains ──────────────► State
  ├── contains ──────────────► Evidence
  └── includes ──────────────► Policy / Authority
Intent
  │
  ▼
Intent Resolution
  │
  ├── resolves ─────────────► Target
  ├── reconstructs ─────────► State
  └── evaluates ────────────► Evidence
Trust
  │
  ├── considers ─────────────► Evidence
  ├── considers ─────────────► Authority
  ├── considers ─────────────► Policy
  ├── considers ─────────────► Constraint
  ├── considers ─────────────► Capability
  └── determines ────────────► Trust Decision
Action
  │
  ├── operates on ───────────► Resource
  ├── requires ──────────────► Capability
  ├── requires ──────────────► Authority
  ├── governed by ───────────► Policy
  ├── constrained by ────────► Constraint
  └── governed by ───────────► Contract
Capability
  │
  ├── belongs to ────────────► System
  └── enables ───────────────► Execution
Contract
  │
  └── constrains ────────────► Execution
Execution
  │
  ├── attempts ──────────────► Action
  ├── produces ──────────────► Observations
  └── requires ──────────────► Verification
Verification
  │
  └── establishes ───────────► Outcome
Outcome
  │
  └── may establish/change ──► Business State
Provenance
  │
  └── records ───────────────► Material concepts, decisions, and transitions

⸻

8. The Central Noema Relationship Graph

The core ontology can therefore be represented as:

                    ┌─────────────────┐
                    │ Actor / Source  │
                    └────────┬────────┘
                             │
                         expresses
                             │
                             ▼
                    ┌─────────────────┐
                    │     Intent      │
                    └────────┬────────┘
                             │
                    contextualized by
                             │
                             ▼
                    ┌─────────────────┐
                    │     Context     │
                    └────────┬────────┘
                             │
                     resolved against
                             │
                   ┌─────────┴─────────┐
                   ▼                   ▼
             ┌───────────┐       ┌───────────┐
             │  Evidence │       │   State   │
             └─────┬─────┘       └─────┬─────┘
                   └─────────┬─────────┘
                             ▼
                    ┌─────────────────┐
                    │ Intent Resolution│
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Trust Decision │
                    └────────┬────────┘
                             │
                     permitted transition
                             │
                             ▼
                    ┌─────────────────┐
                    │     Action      │
                    └────────┬────────┘
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
          Capability      Authority     Contract
                │            │            │
                └────────────┼────────────┘
                             ▼
                    ┌─────────────────┐
                    │    Execution     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Verification  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Outcome     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Business State  │
                    └─────────────────┘

Cross-cutting concepts:

Identity ─────────────► Principal
Delegation ───────────► Authority
Role ─────────────────► Participation
Policy ───────────────► Trust / Authorization / Action / Execution
Constraint ───────────► Intent / Action / Contract / Execution
Evidence ─────────────► Resolution / Trust / Verification
Resource ─────────────► Resolution / Authorization / Action
System ───────────────► Capability / Business State
Provenance ───────────► Material facts / decisions / transitions
State ────────────────► Intent / Context / Trust / Action / Execution / Outcome

⸻

9. The Intent-to-Action Boundary

The most important conceptual boundary in Noema is:

                 PROBABILISTIC
                 UNDERSTANDING
                      │
                      ▼
                   Intent
                      │
                      ▼
              Context + Evidence
                      │
                      ▼
              Intent Resolution
                      │
══════════════════════╪══════════════════════
                      │
                 Trust Decision
                      │
══════════════════════╪══════════════════════
                      │
                      ▼
                    Action
                      │
                 DETERMINISTIC
                  EXECUTION

The first side permits probabilistic inference for understanding and proposal.

The second side requires deterministic validation and control.

Trust is the architectural consequence boundary.

The model may propose.

Noema must establish.

The governed execution system performs.

This separation is foundational to Noema’s architecture. NOEMA POC Specification_1.pdf

⸻

10. The Authority Boundary

A second important boundary is:

Capability
    │
    │ "Can the system technically do this?"
    ▼
Technical Authorization
    │
    │ "May this principal invoke this capability?"
    ▼
Policy Authorization
    │
    │ "Does this parameterization satisfy policy?"
    ▼
Business Authorization
    │
    │ "Should this specific operation against this
    │  specific resolved target and current state occur?"
    ▼
Trust Decision

Capability and Authority must never be collapsed.

A Capability establishes technical possibility.

Authorization establishes whether a particular Principal or Actor may cause a particular Action against a particular target under applicable conditions.

The POC treats target-bound business authorization as distinct from generic capability access. NOEMA POC Specification_1.pdf

⸻

11. The Business-State Boundary

A third important boundary is:

                 NOEMA
        ┌────────────────────────┐
        │                        │
        │ Intent State            │
        │ Context State           │
        │ Trust State             │
        │ Action State            │
        │ Execution State         │
        │ Provenance              │
        │                        │
        └───────────┬────────────┘
                    │
                    │ reads / acts through
                    ▼
        ┌────────────────────────┐
        │ External Systems       │
        │                        │
        │ Business State         │
        │ System-of-Record Truth │
        │                        │
        └────────────────────────┘

Noema coordinates with enterprise systems but does not become the authoritative owner of their business state.

Noema reconstructs enough state to make governed decisions.

It does not replace the system of record by inference. Noema Master Company Document FINAL.pdf

⸻

12. The Data and Trust Boundary

Noema must also preserve a boundary between information used for reasoning and information trusted for execution.

User Input
    │
    ▼
Model / Intent Engine
    │
    │ untrusted proposal
    ▼
Schema Validation
    │
    ▼
Noema Core
    │
    ├── Enterprise Evidence
    ├── Identity / Principal
    ├── Authorization
    ├── Policy
    ├── State
    └── Capability Registry
    │
    ▼
Trust Decision
    │
    ▼
Governed Execution

The following are untrusted inputs:

* user input
* model output
* retrieved documents
* enterprise text fields
* tool responses as instructions

Tool responses may provide evidence, but they do not become commands.

Credentials must remain outside model context.

Arbitrary HTTP and arbitrary SQL are not capabilities.

The execution boundary must therefore not depend on the model remaining uncompromised. Noema Master Company Document FINAL.pdf

⸻

13. Minimum Necessary Visibility and Capability

Noema’s ontology must support a least-necessary operating model.

The relevant principle is:

Minimum necessary data
+
Minimum necessary capability
+
Maximum necessary traceability

Noema should obtain only the information and capability required for the particular investigation or execution.

This means:

* data access should be scoped to the relevant investigation
* enterprise connectors should be controlled
* reads should be principal-scoped
* sensitive information should be minimized or redacted where appropriate
* credentials should be short-lived and protected
* tenant boundaries must be preserved
* capabilities must be explicitly registered
* material decisions must remain reconstructable

This principle does not conflict with auditability. The objective is not maximum visibility; it is sufficient visibility with maximum traceability of consequential decisions. NOEMA POC Specification PDF.pdf

⸻

14. Canonical Concept Categories

For clarity, Noema concepts can be categorized as follows.

Participation and Identity

* Identity
* Principal
* Actor
* Role
* Organization
* Delegation

Intent and Understanding

* Intent
* Objective
* Context
* Resource
* Intent Resolution
* State
* Evidence
* Constraint

Trust and Authorization

* Authority
* Authorization
* Policy
* Trust
* Confidence
* Risk

Execution

* Action
* Capability
* Contract
* Execution
* Preconditions
* Postconditions
* Idempotency
* Side Effects
* Recovery
* Verification

Result and Accountability

* Outcome
* Business State
* Provenance
* Audit
* Operational Memory
* System

Some concepts intentionally appear across multiple categories because their relationships cross conceptual boundaries.

⸻

15. Concepts That Must Not Be Collapsed

The following distinctions are canonical:

Identity          ≠ Actor
Identity          ≠ Principal
Actor             ≠ Principal
Actor             ≠ Authority
Actor             ≠ User
Actor Role        ≠ Actor Identity
Intent            ≠ Action
Intent            ≠ Execution
Action            ≠ Execution
Action            ≠ Outcome
Capability        ≠ Authority
Capability        ≠ Permission
Capability        ≠ Trust
Capability        ≠ Authorization
Technical Auth    ≠ Policy Auth
Policy Auth       ≠ Business Auth
Confidence        ≠ Trust
Confidence        ≠ Evidence
Evidence          ≠ Assertion
Trust             ≠ Authorization
Policy            ≠ Constraint
State             ≠ Evidence
Business State    ≠ Intent State
Business State    ≠ Noema State
API Response      ≠ Verified Outcome
Execution Attempt ≠ Successful Outcome
Timeout           ≠ Failure
Timeout           ≠ Success
Model Proposal    ≠ Canonical Action
Tool Definition   ≠ Registered Capability
Retrieved Content ≠ Instruction

These distinctions represent different responsibilities and failure modes in the Noema architecture.

⸻

16. Ontological Invariants

Invariant 1

Intent is the central object through which Noema represents a requested objective.

Invariant 2

An Actor participates in an Intent but is not the Intent itself.

Invariant 3

A Principal used for authorization must originate from an authoritative identity/authentication layer and must not be inferred from model prose.

Invariant 4

An Action is a bounded operation that can advance an Intent.

Invariant 5

A Capability establishes what a system can technically perform.

Invariant 6

Authority establishes what an Actor or Principal may legitimately cause.

Invariant 7

Authorization is specific to the relevant Principal or Actor, Action, target, and applicable Context.

Invariant 8

Technical authorization, policy authorization, and business authorization are distinct evaluation layers.

Invariant 9

Trust establishes whether Noema has sufficient grounds to permit the relevant transition.

Invariant 10

Confidence does not establish Trust, Authority, Authorization, or permission.

Invariant 11

Model output is a proposal and must cross explicit validation boundaries before it can affect execution.

Invariant 12

No capability outside the registered Capability set may be invoked.

Invariant 13

Arbitrary HTTP, arbitrary SQL, or arbitrary model-generated tool definitions do not constitute capabilities.

Invariant 14

Material ambiguity must be represented explicitly and must not be silently resolved by probabilistic confidence alone.

Invariant 15

Enterprise state may be stale, unavailable, contradictory, or unknown, and these are valid states rather than errors to be hidden.

Invariant 16

A timeout does not establish execution success or failure; uncertain execution must be verified against authoritative downstream state.

Invariant 17

Every consequential execution must have explicit idempotency semantics.

Invariant 18

Every consequential write must be verified against its expected postcondition where verification is possible.

Invariant 19

The executor must revalidate applicable execution conditions immediately before consequential action.

Invariant 20

Policy versions governing material Trust Decisions must be recorded.

Invariant 21

Business State remains owned by the relevant enterprise system of record.

Invariant 22

Noema must preserve minimum necessary visibility and capability while maintaining sufficient traceability.

Invariant 23

Material decisions and transitions must have sufficient provenance to reconstruct business causality.

Invariant 24

Retrieved enterprise content and tool responses are evidence, not instructions.

Invariant 25

Credentials must not be placed in model context.

Invariant 26

A Delegate does not become the Principal merely because it performs an Action.

Invariant 27

An Agent does not acquire authority merely because it can reason, generate a tool call, or invoke a Capability.

Invariant 28

Noema must not claim a successful business outcome solely because an API returned a success code.

Invariant 29

Noema must fail closed when a required deterministic control cannot be established.

Invariant 30

Noema’s autonomous operating boundary is limited by the intersection of trusted Intent, applicable Policy, Authority, registered Capability, explicit Contract, and verified execution conditions.

⸻

17. Ontology Dependency Order

The ontology should be understood in dependency order.

Identity
   │
   ▼
Principal
   │
   ▼
Actor
   │
   ├──────────────────────┐
   ▼                      ▼
Intent                  Authority
   │                      │
   ▼                      │
Context                   │
   │                      │
   ├──────────────┐       │
   ▼              ▼       │
Evidence      Constraint  │
   │              │       │
   └──────┬───────┘       │
          ▼               │
   Intent Resolution      │
          │               │
          ▼               │
   State Reconstruction   │
          │               │
          └──────┬────────┘
                 ▼
             Trust
                 │
          ┌──────┴──────┐
          ▼             ▼
        Action      Authorization
          │
          ├──────────────┐
          ▼              ▼
     Capability       Contract
          │              │
          └──────┬───────┘
                 ▼
             Execution
                 │
                 ▼
            Verification
                 │
                 ▼
              Outcome
                 │
                 ▼
          Business State

This ordering is conceptual rather than a strict implementation dependency.

⸻

18. Relationship to Individual Ontology Documents

This document provides the ontology map.

Detailed definitions belong in:

01-ontology/
├── actor.md
├── identity.md
├── authority.md
├── intent.md
├── context.md
├── action.md
├── capability.md
├── resource.md
├── policy.md
├── constraint.md
├── state.md
├── outcome.md
├── provenance.md
└── relationships.md

Where additional concepts become canonical, they should receive their own authoritative ontology document rather than being defined inconsistently across unrelated documents.

When a detailed ontology document conflicts with this document, the conflict must be resolved explicitly rather than allowing terminology to diverge silently.

⸻

19. Ontology and Implementation

The ontology is independent of implementation.

For example, the ontology may define:

Capability:
payments.transfer.create

without requiring a particular:

* HTTP endpoint
* GraphQL mutation
* gRPC method
* SDK
* database
* programming language
* model
* infrastructure provider

Likewise:

Action:
InvestigateTransaction

does not imply a particular implementation sequence.

Implementation details belong in the architecture, execution, integration, and contract layers.

The ontology defines meaning.

The contracts define executable semantics.

The architecture defines implementation.

⸻

20. Ontology and Typed Action Contracts

The ontology must remain compatible with typed, bounded Action Contracts.

The conceptual progression is:

Intent
   ↓
Resolved Action
   ↓
Action Contract
   ↓
Capability
   ↓
Validation
   ↓
Authorization
   ↓
Execution
   ↓
Verification

The Action Contract is the explicit boundary through which a proposed operation becomes eligible for execution.

A contract should make material execution properties explicit, including:

* target
* typed inputs
* allowed values
* preconditions
* authority requirements
* side effects
* idempotency
* retry semantics
* postconditions
* verification
* failure behavior
* version

This prevents execution semantics from being reconstructed from model intent or implementation-specific tool descriptions.

⸻

21. Ontology and Bounded Autonomy

Noema’s autonomy is not an independent ontological capability.

Autonomy exists only within explicit boundaries.

Conceptually:

Autonomous Execution
        ⊆
Trusted Intent
        ∩
Applicable Policy
        ∩
Granted Authority
        ∩
Registered Capability
        ∩
Valid Action Contract
        ∩
Sufficient Current State
        ∩
Verified Execution Conditions

The objective is not unrestricted autonomy.

The system should automate work only inside a defensible safety envelope.

The Noema architecture explicitly treats responsibility and safety as prerequisites for expanding autonomous execution. Noema Master Company Document FINAL.pdf

⸻

22. Ontology and Multi-Source Grounding

Noema’s understanding of Intent must be grounded in relevant evidence rather than in language alone.

The conceptual pattern is:

Expression
   │
   ▼
Candidate Interpretation
   │
   ├── identity/context
   ├── enterprise state
   ├── resource candidates
   ├── policy
   ├── prior valid context
   └── external evidence
   │
   ▼
Grounded Intent Understanding
   │
   ▼
Validated Intent Object

Grounding is therefore not equivalent to model confidence.

An interpretation becomes operationally useful only when the relevant claims can be connected to evidence and authoritative state.

This is particularly important where:

* references are ambiguous
* multiple resources match
* systems disagree
* evidence is stale
* information is incomplete
* user language is code-switched
* the consequence of choosing incorrectly is material

The POC explicitly requires state reconstruction, ambiguity resolution, evidence collection, and verification rather than relying on a model’s linguistic interpretation alone. NOEMA POC Specification PDF.pdf

⸻

23. Ontology and Security Boundaries

The ontology must support a system in which the model may be wrong or compromised without automatically gaining consequential authority.

The conceptual boundary is:

Untrusted Input
      │
      ▼
Probabilistic Proposal
      │
      ▼
Schema Validation
      │
      ▼
Deterministic Resolution
      │
      ▼
Authorization + Policy + Trust
      │
      ▼
Registered Capability
      │
      ▼
Bounded Contract
      │
      ▼
Execution Gate
      │
      ▼
Verification

This means that a compromised or manipulated model does not bypass the Trust boundary.

Indirect prompt injection, poisoned enterprise content, forged context, privilege escalation, cross-tenant access, and confused-deputy attacks must be handled at deterministic boundaries rather than through confidence in the model. Noema Master Company Document FINAL.pdf

⸻

24. Ontology and Research

Research may introduce new concepts or challenge existing ones.

However, a concept does not become canonical merely because it appears in:

* a paper
* an agent framework
* an AI model
* an external architecture
* an industry standard
* an experiment

A proposed concept should be evaluated for:

1. semantic necessity
2. relationship to existing concepts
3. architectural consequences
4. operational usefulness
5. compatibility with Noema’s invariants
6. whether it introduces a genuinely distinct responsibility or merely renames an existing concept

Only then should it become part of the canonical ontology.

Research may strengthen or refine Noema’s implementation without automatically changing the ontology.

⸻

25. The Minimal Noema Vocabulary

If Noema were reduced to its smallest meaningful execution vocabulary, the following concepts would remain:

Actor
Intent
Trust
Action
Capability
Execution
Verification
Outcome

The security and governance boundary additionally requires:

Principal
Authority
Authorization
Policy
Contract

The contextual foundation requires:

Context
State
Resource
Evidence
Constraint
Provenance

The minimal lifecycle is therefore:

ACTOR / SOURCE
      ↓
INTENT
      ↓
CONTEXT + EVIDENCE + STATE
      ↓
TRUST
      ↓
ACTION
      ↓
CAPABILITY + AUTHORITY + CONTRACT
      ↓
EXECUTION
      ↓
VERIFICATION
      ↓
OUTCOME

This is more precise than treating the system as a simple:

Intent → Action → Outcome

pipeline because Noema’s central problem is not merely selecting an Action. It is establishing whether the Action is justified, authorized, bounded, executable, and verifiably successful.

⸻

26. Canonical Summary

The Noema ontology models the entities, relationships, states, evidence, and controls required to transform an expressed Intent into a trusted, bounded, executable, and verifiable enterprise outcome.

At the highest level:

Actor / Source
      ↓
Intent
      ↓
Context
      ↓
Evidence + State Reconstruction
      ↓
Intent Resolution
      ↓
Trust
      ↓
Action
      ↓
Capability + Authority + Policy + Contract
      ↓
Execution
      ↓
Verification
      ↓
Outcome
      ↓
Authoritative Business State

With:

Identity
Principal
Role
Delegation
Constraint
Resource
System
Confidence
Provenance
Authorization

providing the identity, participation, context, boundaries, and accountability around that lifecycle.

The ontology exists to give Noema a stable language for intent, state, trust, authority, capability, execution, and outcome independent of any particular model, interface, enterprise application, or implementation technology.

The central architectural principle is:

Probabilistic systems may propose.
Deterministic systems must decide.
Bounded capabilities may execute.
Authoritative systems establish business truth.
Verification establishes what actually happened.
Provenance establishes why.

Noema therefore does not treat intelligence, tool access, model confidence, or API reachability as substitutes for Trust.

Its ontology exists to preserve the boundaries that make consequential autonomy governable. Noema Master Company Document FINAL.pdf