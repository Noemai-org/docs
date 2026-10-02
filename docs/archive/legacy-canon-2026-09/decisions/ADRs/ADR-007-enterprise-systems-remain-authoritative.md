> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-007 — Enterprise Systems Remain Authoritative

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Architecture / Authority / Business State
Canonical Path: decisions/ADRs/ADR-007-enterprise-systems-remain-authoritative.md

⸻

1. Context

Noema operates across existing enterprise systems.

Those systems already own authoritative business domains and maintain the state that governs those domains.

Examples include:

* payment processors owning payment state
* banking systems owning account state
* identity providers owning identity state
* CRM systems owning customer records
* HR systems owning employee records
* enterprise applications owning their respective operational state

Noema needs to reason about this state in order to resolve Intent, validate conditions, evaluate Trust, plan execution, and verify outcomes.

However, reasoning about business state does not mean owning that state.

Without an explicit authority boundary, Noema could gradually become a competing system of record by:

* copying business state into its own database and treating the copy as authoritative
* making decisions from stale snapshots
* asserting business outcomes based solely on its own execution records
* mutating business state without the authoritative system confirming the result
* treating Noema’s interpretation of external state as equivalent to the external system’s actual state

This would create conflicting sources of truth and undermine the architectural role of Noema.

⸻

2. Decision

Enterprise systems remain authoritative for the business state within their respective domains.

Noema owns and manages Intent state, Trust state, execution coordination state, provenance, and other state explicitly assigned to Noema.

Noema does not become the authoritative owner of business state merely because it:

* reads that state
* reasons about that state
* caches that state
* plans an Action against that state
* requests a business mutation
* records an execution result

The authoritative enterprise system remains responsible for determining the actual state of its business domain.

Therefore:

Noema
  │
  │ Intent / Trust / Contract
  ▼
Enterprise Capability
  │
  │ authoritative business operation
  ▼
Enterprise System
  │
  │ authoritative business state
  ▼
Business Outcome

Noema may coordinate the transition.

The enterprise system remains authoritative for the resulting business state.

⸻

3. Authority Boundary

The canonical distinction is:

Noema owns:
    Intent State
    Trust State
    Execution Coordination
    Execution Records
    Provenance
    Noema-owned lifecycle state
Enterprise System owns:
    Business State
    Domain Records
    Domain Invariants
    Authoritative Business Outcomes

For example:

If a banking system owns an account:

Account balance = ₦500,000

Noema may retrieve that balance and use it during Trust evaluation.

Noema does not thereby become the authority for:

Account balance

The banking system remains authoritative.

⸻

4. Rationale

The decision establishes a clear separation between coordination and domain authority.

Noema’s role is to make human Intent executable across existing systems.

It is not to reproduce the business logic and authoritative state of every system with which it integrates.

This allows Noema to operate as infrastructure rather than as a replacement ERP, CRM, banking system, payment processor, identity system, or other system of record.

The distinction is:

Noema:
    "This Intent is authorized and an Action may be attempted."
Enterprise System:
    "This is the actual state of the business domain."

⸻

5. Noema May Observe Business State

Noema may obtain business state through explicit interfaces.

Examples:

Customer Registry
        ↓
customer = customer_123
status = ACTIVE
        ↓
Noema Context

or:

Banking System
        ↓
account balance
        ↓
Noema Trust Evaluation

The retrieved information becomes evidence or context for Noema’s own decisions.

It does not transfer ownership of the underlying business state to Noema.

⸻

6. Noema May Cache Business State

Caching may be necessary for performance, resilience, or operational efficiency.

However:

Cached Business State
        ≠
Authoritative Business State

A cache must therefore be treated according to its:

* source
* timestamp
* freshness
* validity
* provenance
* applicable consistency guarantees

A cached value must not automatically be treated as current merely because Noema possesses it.

Where freshness is material to a consequential Action, Noema must account for the possibility that the authoritative state has changed.

⸻

7. Noema Must Preserve Provenance

When Noema uses external business state, it should retain sufficient provenance to establish:

* which system supplied the information
* what information was obtained
* when it was obtained
* which resource or entity it referred to
* what version or representation was used where applicable
* how the information contributed to the decision

Conceptually:

Evidence
├── source
├── subject
├── value
├── observed_at
├── freshness
└── provenance

This allows Noema to distinguish:

"The banking system reported X at time T"

from:

"Noema owns X as business truth"

⸻

8. Enterprise Systems Remain Authoritative After Execution

Execution through Noema does not transfer business authority to Noema.

For example:

Intent
  ↓
Trust
  ↓
Execution Contract
  ↓
Payment Service
  ↓
Payment State

If the payment service reports:

payment = successful

Noema may record that result.

The payment service remains authoritative for the payment’s business state.

Noema’s execution record is not a replacement for the payment provider’s authoritative payment record.

⸻

9. Execution Records Are Not Business Truth

Noema may maintain an execution record such as:

ExecutionRecord {
    execution_id
    intent_id
    action
    consumer
    accepted_at
    started_at
    completed_at
    result
}

This records what Noema knows about the execution lifecycle.

It does not automatically establish the authoritative state of the external business domain.

Therefore:

ExecutionRecord
      ≠
Business Record

and:

Execution Success
      ≠
Noema owns business state

⸻

10. Consumer-Side Authority

Execution consumers may perform authoritative checks immediately before or during execution.

For example:

Noema:
    Trust = READY
        ↓
Payment Service:
    final balance check
    final authorization check
    final business-rule check
        ↓
Payment Service:
    accepts or rejects Action

This is expected.

Business state may change between:

Validation
Trust Evaluation
Execution

The authoritative consumer therefore retains authority over the final business operation.

⸻

11. TOCTOU Conditions

Noema must account for time-of-check-to-time-of-use conditions.

For example:

T1:
Account balance = ₦100,000
T2:
Noema evaluates Intent
T3:
Another transaction changes balance
T4:
Noema submits Action
T5:
Banking system evaluates current state

The fact that Noema observed a particular value at T1 does not mean that value remains authoritative at T4.

Where the domain requires current state, the authoritative system must perform the appropriate final validation.

⸻

12. Business-State Mutation

Noema may cause a business-state mutation by invoking an authorized capability.

For example:

Noema
  ↓
"Renew card"
  ↓
Card Management Capability
  ↓
Banking System
  ↓
Card state changed

Noema coordinates the request.

The banking system owns the resulting card state.

Noema must not claim that its own internal record supersedes the authoritative system.

⸻

13. Outcome Verification

After execution, Noema should verify the resulting outcome where the workflow requires it.

Verification may involve querying the authoritative enterprise system.

For example:

Execution requested
        ↓
Consumer reports completion
        ↓
Query authoritative system
        ↓
Observe current business state
        ↓
Outcome verified

This distinguishes:

Action execution reported as successful

from:

Authoritative business state confirms expected outcome

Both may be relevant, but they are not identical concepts.

⸻

14. Failure and Unknown Outcome

If an execution consumer cannot establish the final business result, Noema must not manufacture one.

For example:

Request submitted
      ↓
Network failure
      ↓
Outcome unknown

Noema should not automatically convert this into:

SUCCESS

or:

FAILURE

unless authoritative evidence establishes the result.

The appropriate state may instead be:

UNKNOWN_OUTCOME

followed by reconciliation or authoritative verification.

⸻

15. No Competing Source of Truth

Noema must not intentionally create competing authoritative records for business domains.

It may maintain:

* references
* snapshots
* caches
* derived context
* execution records
* provenance
* workflow state
* Intent state
* Trust state

But these must not silently become substitutes for the authoritative business system.

The canonical principle is:

Noema may maintain representations of business state without becoming the authority for that state.

⸻

16. Authority Is Domain-Specific

There may be multiple enterprise systems in a single Intent.

For example:

Identity Provider
    ↓
identity authority
CRM
    ↓
customer authority
Payment System
    ↓
payment authority
Noema
    ↓
intent / trust / execution authority

Authority should therefore be determined by domain and explicitly represented rather than assumed to belong to whichever system happens to coordinate the workflow.

⸻

17. Noema as Cross-System Coordinator

Noema’s architectural value increases when an Intent crosses system boundaries.

Example:

Human Intent
     │
     ▼
Noema
     │
     ├── Identity System
     │
     ├── CRM
     │
     ├── Payment System
     │
     └── Notification System

Each system retains authority over its own domain.

Noema coordinates the Intent across those systems without absorbing their domain ownership.

⸻

18. Relationship to Trust

Trust may depend on authoritative external state.

For example:

Intent
  +
Actor
  +
Authorization System
  +
Policy
  +
Current Account State
  +
Capability
  ↓
Trust Evaluation

The Trust Engine can use authoritative external facts.

It does not become the owner of those facts.

Trust establishes whether Noema has sufficient grounds to proceed.

It does not redefine the business state against which those grounds were evaluated.

⸻

19. Relationship to Validation

Validation may establish facts using external systems.

For example:

Recipient Validation
        ↓
Customer Registry
        ↓
customer_123 exists

The Customer Registry remains authoritative for the existence and state of that customer record.

Noema records the validation result and its provenance.

It does not become the customer system of record.

⸻

20. Relationship to Context

Context may contain representations of external business state.

For example:

Context
├── actor
├── customer
├── account
├── card
├── policy
└── capability

Context is an input to Noema’s reasoning and Trust processes.

Context does not transfer ownership of those entities to Noema.

⸻

21. Relationship to Outcome

Outcome must distinguish between:

1. what Noema observed about execution, and
2. what the authoritative business system reports as the resulting domain state.

Conceptually:

Execution
    ↓
Observed Execution Result
    ↓
Authoritative State Verification
    ↓
Business Outcome

Where authoritative verification is unavailable, Noema should preserve that uncertainty rather than collapsing it into an assumed business outcome.

⸻

22. Implications for Integrations

Integrations should explicitly identify:

* authoritative source
* supported capabilities
* readable business state
* mutable business state
* validation responsibilities
* execution responsibilities
* outcome reporting
* reconciliation mechanisms
* freshness requirements
* failure semantics

An integration should not merely define:

endpoint = /doSomething

It should establish the authority relationship surrounding that endpoint.

⸻

23. Implications for Data Modeling

Noema data models should distinguish between:

Noema-owned state

and:

externally authoritative state

References to external entities should preferably preserve identity and provenance rather than pretending the external representation is a Noema-owned canonical entity.

For example:

customer_ref = customer_123
source = CRM
observed_at = T

is preferable to silently treating a copied customer record as Noema’s authoritative customer state.

⸻

24. Implications for Reconciliation

Where execution may produce uncertain outcomes, Noema should support reconciliation against the authoritative system.

Conceptually:

Unknown Execution Result
        ↓
Reconciliation Request
        ↓
Authoritative System
        ↓
Current Business State
        ↓
Reconciled Outcome

This is particularly important for consequential or non-idempotent Actions.

⸻

25. What This Decision Does Not Mean

This decision does not mean Noema cannot:

* store business information
* cache external state
* transform external state
* derive context
* maintain workflow state
* maintain execution records
* verify outcomes
* coordinate multiple systems
* reason about business entities

It means these representations do not automatically become authoritative business truth.

⸻

26. Consequences

Positive consequences

This decision:

* prevents competing systems of record
* preserves enterprise domain ownership
* reduces duplication of business authority
* makes integrations easier to reason about
* supports cross-system orchestration
* clarifies provenance
* supports authoritative outcome verification
* makes TOCTOU conditions explicit
* allows Noema to remain an infrastructure layer rather than a replacement enterprise application

Negative consequences

This decision also means:

* Noema depends on external systems for authoritative business facts
* integrations must handle external availability and latency
* cached information may become stale
* execution may require final consumer-side validation
* outcome verification may require additional calls
* Noema cannot always determine final business state from its own records
* reconciliation mechanisms may be necessary

These are accepted consequences of preserving domain authority.

⸻

27. Alternatives Considered

Alternative A — Noema becomes the global system of record

Rejected.

A single Noema-owned representation of all enterprise business state would require Noema to reproduce and continuously synchronize the domain logic and state of every integrated enterprise system.

This would create substantial duplication and authority conflicts.

⸻

Alternative B — Noema owns a synchronized copy of business state

Rejected as an authority model.

Noema may maintain caches and projections where operationally useful, but synchronization does not make those copies authoritative.

The external domain system remains authoritative.

⸻

Alternative C — The execution result recorded by Noema becomes business truth

Rejected.

An execution result describes what happened from the execution layer’s perspective.

The authoritative enterprise system remains responsible for establishing the resulting business state.

⸻

Alternative D — Authority is determined per workflow

Rejected as the default architectural model.

Authority must derive from explicit domain ownership rather than being implicitly reassigned by whichever workflow happens to coordinate the operation.

⸻

28. Relationship to Other Canonical Decisions

This ADR reinforces several foundational Noema boundaries.

Intent ownership

Noema owns Intent state rather than business state.

Deterministic Trust

Trust may rely on external authoritative evidence without becoming the owner of that evidence.

Explicit Execution Contracts

Execution contracts invoke capabilities exposed by authoritative enterprise systems.

Capability / Permission Separation

An enterprise system may expose a capability while Noema independently determines whether the Actor and Intent are permitted to invoke it.

Outcome Verification

Business outcomes should ultimately be established against the authoritative domain system where required.

⸻

29. Architectural Rule

The following rule is normative:

Noema must not represent a business-domain state as authoritative when another system is the designated authority for that domain.

Where Noema stores such state for operational purposes, its representation must remain distinguishable from the authoritative source.

⸻

30. Invariants

Invariant 1

Enterprise systems remain authoritative for their respective business domains.

Invariant 2

Noema owns Intent state, not enterprise business state.

Invariant 3

A Noema cache is not automatically authoritative.

Invariant 4

An execution record is not automatically a business record.

Invariant 5

External business facts must retain appropriate provenance.

Invariant 6

Noema must not manufacture business outcomes when authoritative evidence is unavailable.

Invariant 7

Consumer-side validation may remain authoritative at execution time.

Invariant 8

Business state may change between Trust evaluation and execution.

Invariant 9

Outcome verification may require querying the authoritative enterprise system.

Invariant 10

Noema must not silently create a competing source of truth.

⸻

31. Canonical Model

The decision can be reduced to:

                 NOEMA
        ┌─────────────────────┐
        │ Intent              │
        │ Context             │
        │ Validation          │
        │ Trust               │
        │ Contracts           │
        │ Execution Records   │
        │ Provenance          │
        └──────────┬──────────┘
                   │
             explicit contract
                   │
                   ▼
        ┌─────────────────────┐
        │ ENTERPRISE SYSTEM   │
        │                     │
        │ Business Rules      │
        │ Business State      │
        │ Domain Authority    │
        └─────────────────────┘

Noema controls the intent-to-action boundary.

The enterprise system controls the authoritative business domain.

⸻

32. Final Decision

Noema is an intent infrastructure layer, not a universal system of record.

It may understand, contextualize, validate, trust, plan, contract, execute, observe, and verify Actions across enterprise systems.

But the systems that own the relevant business domains remain authoritative for their business state.

The foundational rule is:

Noema coordinates business actions; authoritative enterprise systems determine business truth.