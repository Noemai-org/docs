Next is:

decisions/ADRs/ADR-002-noema-owns-intent-state-not-business-state.md

ADR-002: Noema Owns Intent State, Not Business State

Status: Accepted
Version: 0.1
Decision Type: Foundational
Domain: Architecture / State Ownership
Canonical Path: decisions/ADRs/ADR-002-noema-owns-intent-state-not-business-state.md

⸻

1. Context

Noema operates between human intent and existing software systems.

To fulfill an Intent, Noema may need to read from and interact with systems such as:

* payment systems
* banking systems
* CRM systems
* identity systems
* HR systems
* workflow systems
* enterprise databases
* external service providers

These systems already own authoritative business state.

For example:

* a banking system owns account state
* a payment provider owns payment state
* an identity system owns identity state
* a CRM owns customer records
* an HR system owns employee records

Noema must therefore establish a clear boundary between the state it owns and the state it observes or changes through external systems.

Without such a boundary, Noema could become an accidental competing system of record.

⸻

2. Decision

Noema owns Intent state, not authoritative business state.

Noema is authoritative for the lifecycle and state of the Intent as it passes through Noema’s semantic, validation, Trust, planning, execution, and outcome processes.

The external system responsible for a business domain remains authoritative for that domain’s business state.

Conceptually:

                 NOEMA
                   │
             owns Intent state
                   │
                   ▼
              Action Contract
                   │
                   ▼
        ┌──────────────────────┐
        │ External System      │
        │                      │
        │ owns business state  │
        └──────────────────────┘

Noema may:

* retrieve business state
* contextualize Intent using business state
* validate references against business state
* evaluate Trust using business state
* request business-state changes
* observe resulting business state
* record references to authoritative external facts

Noema must not silently claim ownership of those external facts.

⸻

3. Rationale

Noema’s purpose is to provide an intent-to-action infrastructure layer rather than to replace the systems through which business operations are actually performed.

The distinction can be expressed as:

Intent State
     ↓
owned by Noema
Business State
     ↓
owned by the authoritative domain system

This allows Noema to coordinate across multiple systems without becoming a universal database or enterprise application.

It also prevents Noema’s internal representation from becoming confused with the actual state of the external world.

⸻

4. State Ownership Model

4.1 Noema-Owned State

Noema may own state such as:

Intent
Intent Version
Intent Lifecycle State
Resolution State
Validation Result
Trust State
Execution Plan
Execution Contract
Execution Record
Outcome Observation
Provenance
Clarification State
Approval State
Decision History

These represent Noema’s processing and governance of an Intent.

⸻

4.2 External Business State

External systems may own:

Account Balance
Card Status
Payment Status
Customer Record
Employee Record
Inventory Quantity
Subscription Status
Identity Record
Order Status

The authoritative ownership depends on the relevant domain and system.

Noema may consume these facts without becoming their authoritative owner.

⸻

5. Noema as a Consumer of Business Truth

When Noema requires external information, it should obtain that information through explicit interfaces.

For example:

Intent:
Replace expired card
        ↓
Context request
        ↓
Banking System
        ↓
Card:
status = EXPIRED
        ↓
Noema Context / Evidence
        ↓
Validation / Trust

The fact that Noema stores or references:

card.status = EXPIRED

does not make Noema the authoritative owner of card status.

The banking system remains authoritative.

⸻

6. Noema Must Preserve Provenance

External facts used by Noema should retain appropriate provenance.

Conceptually:

Evidence
├── source
├── reference
├── retrieved_at
├── freshness
└── relevant value

This allows Noema to distinguish:

What Noema knows

from:

Where that knowledge came from

and:

Who is authoritative for the underlying business fact

Noema should not represent externally sourced information as though it originated from Noema.

⸻

7. Observation Is Not Ownership

Reading business state does not transfer ownership of that state to Noema.

For example:

Payment Provider
      │
      │ payment.status = SETTLED
      ▼
    Noema
      │
      │ uses fact for Trust / Context
      ▼
  Execution decision

Noema can rely upon the provider’s authoritative representation while maintaining the distinction between:

* external business truth
* Noema’s observation of that truth
* Noema’s decision based on that observation

⸻

8. Mutation Is Not Ownership

Noema may cause a business-state mutation without becoming the owner of the resulting state.

For example:

Noema
  │
  │ Execute:
  │ cancel_subscription
  ▼
Subscription System
  │
  │ authoritative mutation
  ▼
Subscription:
status = CANCELLED

Noema may record:

Execution:
SUCCESS
Observed Outcome:
subscription cancellation accepted

But the subscription system remains authoritative for:

subscription.status

⸻

9. Outcome Does Not Transfer Authority

The Outcome Engine may observe or record the result of execution.

For example:

Execution
    ↓
External System
    ↓
Business State Changed
    ↓
Outcome Observation

The Outcome Record does not become the authoritative replacement for the external business record.

Noema records what happened from the perspective necessary to manage the Intent lifecycle.

The domain system remains authoritative for its own state.

⸻

10. Distributed State and Race Conditions

Business state may change independently of Noema.

For example:

T1:
Noema reads balance = ₦100,000
T2:
Another system changes balance
T3:
Noema executes transfer
T4:
Payment system evaluates current balance

The value observed at T1 may no longer represent current business truth at T3.

Therefore Noema must not assume that an observation remains authoritative indefinitely.

This reinforces the need for:

* freshness
* validation
* Trust re-evaluation
* execution-time checks
* consumer-side authoritative validation where required

⸻

11. Consumer-Side Authority

An execution consumer may reject an otherwise trusted Execution Contract because business state has changed.

For example:

Noema:
Intent = VALID
Trust = READY
        ↓
Payment Service:
Current balance insufficient
        ↓
Execution rejected

This does not necessarily mean Noema incorrectly owned or evaluated the business state.

It means the authoritative system evaluated the current state at execution time.

The external system remains authoritative.

⸻

12. Cross-System Operations

Noema may coordinate an Intent across multiple systems.

For example:

Intent
  │
  ├── Identity System
  │
  ├── CRM
  │
  ├── Payment System
  │
  └── Notification System

Each system may remain authoritative for its own domain.

Noema provides the coordination layer without absorbing all domain state into a single Noema-owned business database.

This distinction is especially important for composite and multi-step Intents.

⸻

13. Alternatives Considered

13.1 Noema Becomes the System of Record

Rejected.

Making Noema authoritative for external business domains would duplicate enterprise state and introduce competing sources of truth.

It would also expand Noema beyond its intended role as an intent infrastructure layer.

⸻

13.2 Noema Maintains a Complete Replica of Business State

Rejected as a canonical ownership model.

Caching, indexing, materialized views, or locally retained evidence may be necessary for performance or reasoning.

However, a replica does not become authoritative merely because Noema stores it.

The source system remains authoritative.

⸻

13.3 Noema Stores Only References and Never Values

Rejected as an absolute rule.

Noema may need to retain relevant observations, evidence, or contextual snapshots to support:

* Trust evaluation
* auditability
* provenance
* reproducibility
* outcome analysis
* historical reconstruction

The requirement is not that Noema store nothing.

The requirement is that stored observations not be confused with authoritative business ownership.

⸻

14. Consequences

14.1 Positive Consequences

This decision:

* prevents competing systems of record
* preserves enterprise system authority
* keeps Noema’s architectural scope bounded
* enables integration across heterogeneous systems
* supports explicit provenance
* makes business-state changes observable without requiring Noema to own them
* allows Noema to remain focused on intent, Trust, execution, and outcome coordination

⸻

14.2 Negative Consequences

This decision means Noema must deal with distributed-system realities.

These include:

* stale observations
* inconsistent snapshots
* network failures
* unavailable external systems
* race conditions
* eventual consistency
* external transaction boundaries
* consumer-side rejection
* unknown execution outcomes

Noema therefore cannot assume that its internal state is an authoritative representation of the entire business environment.

⸻

15. Architectural Implications

The architecture should preserve the following relationship:

                 Noema
                   │
        ┌──────────┴──────────┐
        │                     │
   Intent State          Decision State
        │                     │
        └──────────┬──────────┘
                   │
             Execution Contract
                   │
                   ▼
          External Capability
                   │
                   ▼
        Authoritative System
                   │
                   ▼
            Business State

Noema owns the left side of this boundary.

The external domain system owns the business state on the right.

⸻

16. Canonical Invariants

This ADR establishes the following invariants:

1. Noema owns Intent state, not authoritative business state.
2. External systems remain authoritative for their respective business domains.
3. Observing business state does not transfer ownership of that state to Noema.
4. Causing a business-state mutation does not make Noema the owner of the resulting state.
5. Noema must preserve appropriate provenance for externally sourced facts.
6. Noema must not represent stale or locally cached information as inherently authoritative.
7. Execution consumers may perform final authoritative checks against current business state.
8. Noema’s Outcome records do not replace authoritative external business records.
9. A locally stored observation is not equivalent to ownership of the underlying business fact.
10. Noema must preserve the distinction between Intent State, Noema decision state, and external Business State.

⸻

17. Canonical Impact

This decision reinforces a central statement in the Noema Canon:

Noema owns intent state, not business state.

It establishes this distinction as an architectural boundary rather than merely a descriptive principle.

The decision affects:

* Context Engine
* Validation
* Trust Engine
* Execution Planner
* Action Graph
* Execution Record
* Outcome Engine
* Operational Memory
* provenance
* integrations with external systems
* consumer-side execution contracts

Any future architecture that proposes making Noema authoritative for a business domain must explicitly challenge and supersede this ADR.

⸻

18. Affected Specifications

At minimum:

CANON.md
ontology/
trust/
architecture/
execution/
context/
outcome/

Exact affected files should be maintained as the repository evolves.

⸻

19. Related Decisions

* ADR-001 — Intent as a First-Class Object
* ADR-003 — Probabilistic / Deterministic Boundary
* ADR-004 — Deterministic Trust Evaluation
* ADR-005 — Explicit Execution Contracts
* ADR-007 — Enterprise Systems Remain Authoritative
* ADR-016 — Consumer-Side Authoritative Validation
* ADR-017 — Outcome Separate From Trust

⸻

20. Supersedes

None.

⸻

21. Superseded By

None.

⸻

22. Decision Summary

The canonical architectural boundary is:

Human Intent
      ↓
     Noema
      │
      ├── owns Intent state
      ├── owns Trust state
      ├── owns execution coordination
      └── owns decision provenance
      │
      ▼
Execution Contract
      │
      ▼
External System
      │
      └── owns authoritative business state

Noema coordinates and governs the transition from Intent to Action; it does not become the system of record for the business domains through which those Actions are executed.