> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-016 — Consumer-Side Authoritative Validation

Status: Accepted
Version: 0.1
Date: 2026-09-19
Decision Type: Foundational
Domain: Execution / Validation / Architecture
Canonical Path: decisions/ADRs/ADR-016-consumer-side-authoritative-validation.md

⸻

1. Decision

Noema shall treat the execution consumer as the authoritative validator of final business-state conditions at the point of execution where the consumer owns that business truth.

Noema’s Validation and Trust decisions establish whether an Intent is sufficiently understood, structurally valid, trusted, and eligible for execution based on the information available to Noema at evaluation time.

They do not transfer ownership of authoritative business-state validation from the execution consumer to Noema.

Therefore:

Noema Validation
       ↓
Noema Trust
       ↓
Execution Contract
       ↓
Consumer-Side Authoritative Validation
       ↓
Execution
       ↓
Outcome

A consumer may reject an otherwise READY Intent when current authoritative business state no longer satisfies the consumer’s execution requirements.

⸻

2. Context

Noema operates across existing enterprise systems.

Those systems remain authoritative for their respective domains.

For example:

* a banking system owns account state
* a payment system owns payment state
* an identity system owns identity state
* a CRM owns customer records
* an inventory system owns inventory state

Noema may retrieve and reason about these states, but it does not become the authoritative owner merely because it evaluated them.

Between Trust evaluation and execution, business state may change.

For example:

T1
Noema evaluates account balance
        ↓
₦100,000 available
T2
Noema establishes Trust = READY
T3
Another transaction changes the balance
T4
Execution consumer receives the contract
T5
Consumer checks authoritative account state
        ↓
insufficient funds

The consumer’s rejection is not evidence that Noema’s earlier Trust evaluation was necessarily invalid.

It reflects the fact that the authoritative business state changed.

⸻

3. Problem

Noema cannot guarantee that every business condition remains unchanged between:

Validation
Trust Evaluation
Execution

This creates a potential time-of-check/time-of-use condition:

T1: Validate
T2: Trust
T3: Execute

A predicate that was true at T1 may no longer be true at T3.

If Noema were treated as the final authority over business state, it would have to maintain synchronized replicas of every relevant enterprise system.

That would violate a foundational Noema boundary:

Noema owns Intent state, not enterprise business state.

The architecture therefore requires final authoritative validation to remain with the system that owns the relevant business truth.

⸻

4. Core Principle

The canonical principle is:

The system that owns authoritative business state remains authoritative for final validation of that state at execution time.

Noema may establish:

"This Intent was trusted based on the evidence and conditions available during evaluation."

The consumer may establish:

"The requested operation is valid against the current authoritative business state."

These are different claims.

⸻

5. Noema Validation vs Consumer Validation

The distinction is:

Layer	Primary Question
Intent Resolution	What does the Actor mean?
Noema Validation	Is the Intent structurally and semantically valid?
Trust	May the Intent proceed toward execution?
Execution Contract	What operation is authorized to be requested?
Consumer Validation	Is the requested operation valid against current authoritative business state?
Execution	Can the consumer perform the operation?
Outcome	What actually happened?

Noema and the consumer therefore perform complementary validation rather than competing validation.

⸻

6. Noema Does Not Delegate Its Own Trust Responsibility

Consumer-side authoritative validation does not mean Noema may omit its own Validation or Trust evaluation.

Noema must still establish:

* what the Actor intends
* whether the Intent is resolved
* whether the Intent is structurally valid
* whether applicable Trust conditions are satisfied
* whether the Action is authorized within Noema’s control boundary
* whether the appropriate capability exists
* whether the Execution Contract may be issued

The consumer then performs the validation that only the consumer can authoritatively perform.

Therefore:

Noema Validation
        ≠
Consumer Validation

and:

Noema Trust
        ≠
Consumer Business-State Authority

⸻

7. Business-State Authority Remains External

Noema must not silently become a competing source of truth.

For example, if a banking system owns:

Account Balance

then Noema may hold:

Observed Balance = ₦100,000
Observed At = T1
Source = Banking System

but the authoritative business state remains:

Banking System:
Current Balance = authoritative value

Noema’s stored observation is evidence.

It is not ownership of the business state.

⸻

8. Evidence Has Temporal Meaning

Evidence used by Noema has a temporal boundary.

Conceptually:

Evidence
    ↓
Observed at T1
    ↓
Trust evaluated
    ↓
Execution at T2

The fact that the evidence was authoritative when observed does not necessarily mean it remains current at T2.

Therefore Noema should distinguish:

Evidence was authoritative when observed

from:

Business state is still authoritative at execution time

The latter may only be established by the system that owns the current state.

⸻

9. TOCTOU Conditions

This ADR explicitly recognizes time-of-check/time-of-use conditions.

Example:

T1:
Balance = ₦100,000
T2:
Noema validates Intent
T3:
Noema evaluates Trust
T4:
Trust = READY
T5:
Another transaction consumes ₦80,000
T6:
Execution consumer receives request
T7:
Current balance = ₦20,000
T8:
Consumer rejects transfer requiring ₦50,000

Noema must not assume that its earlier observation overrides the consumer’s current authoritative state.

⸻

10. Consumer Rejection Is a Valid Outcome

A consumer rejection after READY is a legitimate execution outcome.

The lifecycle may therefore be:

READY
   ↓
EXECUTION CONTRACT
   ↓
CONSUMER VALIDATION
   ↓
REJECTED
   ↓
FAILED / REQUIRES RE-EVALUATION

The exact resulting execution state depends on the execution architecture.

The important distinction is:

READY ≠ GUARANTEED SUCCESS

⸻

11. Trust Does Not Guarantee Business-State Validity

Trust establishes execution eligibility according to Noema’s Trust model.

It does not guarantee that every downstream business precondition remains true.

Therefore:

Trust = READY

does not imply:

Consumer = MUST EXECUTE

The consumer remains responsible for authoritative business validation.

⸻

12. Execution Contract Boundary

The Execution Contract establishes the boundary between Noema and the execution consumer.

Conceptually:

Trusted Intent
      ↓
Execution Planning
      ↓
Execution Contract
      ↓
Consumer
      ↓
Authoritative Validation
      ↓
Execution

The contract should communicate the information required by the consumer to determine whether the requested operation can be executed.

The consumer remains free—and in some cases obligated—to reject execution if authoritative business conditions are not satisfied.

⸻

13. Consumer Validation Must Not Expand Authority

Consumer-side validation does not grant the consumer permission to reinterpret Noema’s Intent or exceed the Execution Contract.

The consumer validates whether the requested operation is executable under its authoritative business rules.

It does not thereby gain authority to:

* invent a different Intent
* modify the Actor’s objective
* execute unrelated Actions
* expand requested scope
* bypass Noema’s Trust boundary

The execution consumer validates and executes the contracted Action within its own authority.

⸻

14. Consumer Validation May Be More Current

Noema may evaluate an Intent using evidence retrieved moments earlier.

The consumer may have access to a more current transactionally authoritative state.

Therefore:

Noema:
Observed state at T1
Consumer:
Authoritative state at T2

The consumer’s current state governs the consumer’s business operation.

This is a consequence of distributed system boundaries, not an indication that Noema’s earlier observation was inherently incorrect.

⸻

15. Consumer Validation May Be Transactional

Where appropriate, the execution consumer may combine validation and mutation within a transaction or equivalent atomic mechanism.

For example:

Check current balance
       +
Reserve / debit funds
       ↓
Atomic business operation

This can prevent a condition from changing between a consumer’s own final validation and its mutation.

Noema should not attempt to reproduce such domain-specific transactional semantics outside the authoritative system.

⸻

16. Consumer Validation and Idempotency

Consumer-side validation should operate consistently with the Action Contract’s idempotency semantics.

For example, if an execution request is retried:

Request A
   ↓
Consumer
   ↓
partial/network uncertainty
   ↓
Retry Request A

the consumer may need to determine whether the original operation already occurred.

This is part of the consumer’s authoritative execution semantics.

Noema should preserve the Execution Contract’s identity and idempotency information rather than assuming that repeated delivery represents a new business operation.

⸻

17. Consumer Validation and Constraints

Some constraints are best enforced by Noema.

Examples:

* Intent structure
* Actor scope
* Noema-level policy
* approval requirements
* execution boundaries

Other constraints belong to the authoritative consumer.

Examples:

* current account balance
* current inventory
* current payment status
* current resource ownership
* domain-specific transactional invariants

The architecture should not require Noema to duplicate every consumer-side rule.

⸻

18. Example — Banking Transfer

Suppose the Intent is:

Transfer ₦500,000 from Account A to Account B.

Noema may establish:

Intent resolved
Validation = VALID
Authorization = SATISFIED
Policy = SATISFIED
Capability = AVAILABLE
Risk controls = SATISFIED
Trust = READY

The banking system then checks:

Current account status
Current available balance
Account restrictions
Transaction limits
Current beneficiary state
Transactional invariants

If the bank rejects the transfer because the current balance is insufficient:

Execution Outcome = FAILED / REJECTED

Noema must record the outcome rather than override the bank’s authoritative state.

⸻

19. Example — Inventory

Noema evaluates:

Purchase item X

At evaluation time:

Inventory = 3

Noema becomes:

READY

Before execution, another customer purchases two units.

The authoritative inventory system now reports:

Inventory = 1

If the requested quantity is two, the consumer rejects the operation.

Noema must not execute against its stale observation.

⸻

20. Example — Customer State

Noema evaluates:

Close customer account.

The customer system may own account status.

Between Trust evaluation and execution:

Account state changes

The customer system may determine that the account is no longer eligible for closure or that another workflow has already closed it.

The consumer’s current authoritative state determines the result.

⸻

21. Relationship to Validation

The canonical Validation specification states that external systems may perform additional authoritative validation.

This ADR makes that architectural principle explicit.

The relationship is:

Resolved Intent
      ↓
Noema Validation
      ↓
Trust Evaluation
      ↓
Execution Contract
      ↓
Consumer Validation
      ↓
Execution

Consumer validation is therefore not an accidental duplicate layer.

It is a deliberate architectural boundary.

⸻

22. Relationship to Trust State

A consumer-side rejection does not automatically imply that the original Trust state was invalid.

For example:

T1:
Trust = READY
T2:
Business state changes
T3:
Consumer rejects execution

The historical Trust decision remains:

READY at T1

The later execution outcome is:

FAILED / REJECTED at T3

Trust history must remain historically accurate.

Noema should not rewrite historical Trust state simply because downstream business state subsequently changed.

⸻

23. Relationship to Re-Evaluation

A consumer rejection may provide new evidence that requires Trust re-evaluation.

For example:

READY
   ↓
Consumer rejects
   ↓
New authoritative evidence
   ↓
EVALUATING
   ↓
WAITING / BLOCKED / READY

Whether re-evaluation is appropriate depends on the semantics of the rejection.

A temporary resource condition may be recoverable.

A permanent business rule violation may produce BLOCKED.

The consumer’s result should be interpreted through explicit deterministic rules.

⸻

24. Relationship to Unknown

A consumer may itself return an uncertain execution result.

For example:

Request sent
      ↓
Network timeout
      ↓
Consumer outcome = UNKNOWN

Noema must not assume either:

SUCCESS

or:

FAILURE

without authoritative evidence.

This is particularly important for operations that may have succeeded before the communication failure.

The handling of unknown execution outcomes belongs to the execution/outcome model, while the fail-closed principle established by ADR-015 remains applicable to any subsequent consequential decision.

⸻

25. Provenance

Noema should record the distinction between:

Noema Validation

and:

Consumer Validation

Where relevant, provenance should include:

* consumer identity
* validation result
* validation timestamp
* relevant contract identifier
* consumer rule or operation identifier where exposed
* authoritative business-state reference where available
* resulting execution outcome

This allows Noema to reconstruct what happened without claiming ownership of the consumer’s internal business logic.

⸻

26. Noema Must Not Pretend to Know Consumer Internals

Noema may consume the consumer’s authoritative result.

It should not claim knowledge of internal business rules that the consumer has not exposed.

For example:

Consumer:
TRANSFER_REJECTED

does not necessarily allow Noema to assert:

The bank rejected the transfer specifically because of rule X.

unless the consumer explicitly provides that reason.

Noema should preserve the consumer’s authoritative result and provenance without inventing internal explanations.

⸻

27. Error and Outcome Mapping

Consumers should provide structured execution results where possible.

Conceptually:

ExecutionResult {
    status
    code
    message
    authoritative
    timestamp
    details
}

The exact schema belongs to the execution contract.

The important principle is that machine-readable consumer results should be preserved as canonical execution evidence.

⸻

28. Consequences

Positive consequences

* preserves enterprise system authority
* prevents stale Noema state from overriding current business truth
* supports transactional consumer semantics
* reduces duplication of domain-specific business rules
* handles TOCTOU conditions explicitly
* preserves clear architectural ownership
* makes execution outcomes more trustworthy
* supports distributed-system correctness

Negative consequences

* execution may fail after Noema reaches READY
* consumers must expose appropriate validation and execution semantics
* Noema must handle consumer rejection and unknown outcomes
* some business rules will exist outside Noema
* debugging may require cross-system provenance

These consequences are accepted as necessary to preserve system-of-record boundaries.

⸻

29. Implementation Guidance

Implementations should:

1. treat enterprise consumers as authoritative for their owned business state
2. perform Noema Validation before Trust evaluation
3. perform Noema Trust evaluation before issuing executable contracts
4. allow consumers to perform final authoritative validation
5. preserve the distinction between Noema evidence and consumer authority
6. never override a consumer’s authoritative business-state rejection
7. preserve contract identity across retries
8. support consumer-side transactional semantics where available
9. record consumer validation and execution outcomes as provenance
10. support re-evaluation when consumer results materially change the Intent’s eligibility
11. distinguish consumer rejection from consumer uncertainty
12. avoid duplicating authoritative business-state ownership inside Noema

⸻

30. What This ADR Does Not Decide

This ADR does not define:

* the complete Execution Contract schema
* consumer API protocols
* transaction semantics for individual domains
* retry policies
* idempotency-key format
* compensation strategies
* distributed transaction protocols
* consumer-specific validation rules
* the exact mapping of every consumer error to Noema execution states

Those concerns belong to the relevant specifications and consumer contracts.

This ADR establishes the ownership boundary.

⸻

31. Canonical Invariants

Invariant 1

Enterprise systems remain authoritative for their owned business state.

Invariant 2

Noema Validation does not replace consumer-side authoritative validation.

Invariant 3

Trust READY does not guarantee execution success.

Invariant 4

Business state may change between Trust evaluation and execution.

Invariant 5

A consumer may reject an otherwise READY Intent when current authoritative conditions prohibit execution.

Invariant 6

Noema must not override authoritative consumer validation.

Invariant 7

Noema must not treat its own observations as permanent ownership of external business state.

Invariant 8

Consumer validation does not grant authority to reinterpret or expand the Execution Contract.

Invariant 9

Historical Trust decisions must remain historically accurate.

Invariant 10

Consumer-side authoritative results must be represented as execution evidence and outcome, not silently rewritten into Noema-owned business truth.

⸻

32. Canonical Flow

                  HUMAN INTENT
                       │
                       ▼
               INTENT RESOLUTION
                       │
                       ▼
                 VALIDATION
                       │
                       ▼
                TRUST ENGINE
                       │
                       ▼
                    READY
                       │
                       ▼
              EXECUTION CONTRACT
                       │
                       ▼
          ┌─────────────────────────┐
          │   AUTHORITATIVE         │
          │   EXECUTION CONSUMER    │
          └────────────┬────────────┘
                       │
              Current Business State
                       │
                       ▼
             Consumer Validation
                       │
                 ┌─────┴─────┐
                 │           │
              Valid       Invalid
                 │           │
                 ▼           ▼
             EXECUTE      REJECT
                 │           │
                 ▼           ▼
              OUTCOME    FAILED / RE-EVALUATE

⸻

33. Final Decision

Noema shall preserve a strict distinction between Noema’s determination that an Intent is eligible for execution and the execution consumer’s authoritative determination that the requested operation is valid against current business state.

The canonical relationship is:

Noema
  ↓
Understand
  ↓
Validate
  ↓
Trust
  ↓
Contract
  ↓
Consumer
  ↓
Authoritatively validate current business state
  ↓
Execute
  ↓
Report outcome

The fundamental rule is:

Noema may establish that an Action is trusted and eligible to be attempted; the system that owns the relevant business state remains authoritative over whether that Action can actually be performed against the current state.

Therefore:

READY ≠ GUARANTEED EXECUTION

and:

Noema Trust
      ≠
Enterprise Business-State Authority

This preserves the core Noema boundary:

Noema owns Intent and Trust state. The enterprise system owns its business truth.