> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-005 — Explicit Execution Contracts

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Architecture / Execution
Canonical Path: decisions/ADR/ADR-005-explicit-execution-contracts.md

⸻

1. Title

Explicit Execution Contracts

⸻

2. Context

Noema exists at the boundary between human intent and execution across existing software systems.

A probabilistic model may interpret an Actor’s expression and propose an Intent, Action, or execution plan. However, model output must not itself become an executable instruction.

Noema therefore requires a deterministic boundary between:

Intent
   ↓
Trust
   ↓
Action
   ↓
Execution

The execution layer must receive an explicit representation of what is authorized to happen, under what conditions, through which capability, and with what expected behavior.

Without such a contract, execution risks becoming dependent on:

* model-generated instructions
* implicit application behavior
* undocumented assumptions
* conversational context
* tool-specific invocation formats
* unverified parameters
* hidden authorization assumptions
* ambiguous side effects

This would make the execution boundary difficult to audit, reproduce, constrain, and govern.

The Canon therefore establishes that Noema executes through explicit capabilities and contracts rather than directly executing model output.

⸻

3. Decision

Noema adopts explicit Execution Contracts as the canonical boundary between trusted Intent and execution.

A trusted Intent must be translated into an explicit Execution Contract before an execution consumer may perform the requested Action.

The canonical flow is:

Human Expression
      ↓
Intent
      ↓
Resolution
      ↓
Validation
      ↓
Trust Evaluation
      ↓
Action Selection
      ↓
Execution Contract
      ↓
Execution Consumer
      ↓
Outcome

The Execution Contract is the authoritative representation of the execution request presented to the execution boundary.

Noema must not treat arbitrary model output, natural-language instructions, or implicit tool calls as equivalent to an Execution Contract.

⸻

4. What the Contract Establishes

An Execution Contract should establish, where applicable:

* Action identity
* Intent identity
* Actor
* Target
* Inputs
* Required capability
* Authorization basis
* Preconditions
* Constraints
* Expected side effects
* Postconditions
* Failure semantics
* Idempotency semantics
* Execution limits
* Expiration
* Provenance
* Audit requirements

Conceptually:

ExecutionContract
├── contract_id
├── intent_id
├── action
├── actor
├── target
├── inputs
├── capability
├── authorization
├── preconditions
├── constraints
├── expected_effects
├── postconditions
├── failure_semantics
├── idempotency
├── validity
├── provenance
└── audit_requirements

The exact schema is defined by the relevant execution specifications and contracts.

This ADR establishes the architectural principle, not the final schema.

⸻

5. Contract Is Not Intent

An Intent describes what the Actor wants to accomplish.

An Execution Contract describes what the execution layer is authorized and instructed to perform.

Therefore:

Intent
"What does the Actor want?"

is distinct from:

Execution Contract
"What specific Action may the execution consumer perform?"

A single Intent may result in one or more execution contracts depending on the Action Graph and execution plan.

Conversely, an Execution Contract must remain traceable to the Intent from which it was derived.

⸻

6. Contract Is Not Trust

Trust establishes whether an Intent is eligible to cross the execution boundary.

The Execution Contract expresses the concrete execution request after that eligibility has been established.

Therefore:

Trust
   ↓
Execution Eligibility
   ↓
Execution Contract
   ↓
Execution

A contract must not be used to bypass Trust.

Creating a contract does not itself establish authorization.

The contract must be generated from a valid, trusted execution decision.

⸻

7. Contract Is Not Capability

A capability describes what an execution system can perform.

An Execution Contract describes what Noema is requesting that capability to perform in a particular execution context.

Therefore:

Capability
"Can this system perform this Action?"

while:

Execution Contract
"Perform this specific Action under these specific conditions."

Capability and contract must remain distinct.

⸻

8. Contract Is Not Permission

Permission determines whether an Actor or Intent is authorized to cause an Action.

The Execution Contract carries the execution request and, where appropriate, its authorization provenance.

Therefore:

Capability ≠ Permission ≠ Contract

Noema must not infer permission merely because a capability exists.

Likewise, a valid authorization must not be interpreted as permission to invoke arbitrary capabilities.

⸻

9. Model Output Is Not a Contract

A model may produce:

"Cancel John's subscription."

or a structured candidate such as:

{
  "action": "cancel_subscription",
  "customer": "john"
}

Neither representation is automatically an Execution Contract.

The candidate must pass through the appropriate Noema stages:

Model Output
    ↓
Candidate Intent
    ↓
Resolution
    ↓
Validation
    ↓
Trust
    ↓
Action Selection
    ↓
Execution Contract

This preserves the probabilistic/deterministic boundary established by Noema’s Canon and ADR-003.

⸻

10. Contract Generation

An Execution Contract may be generated only after the prerequisites for execution have been established.

Conceptually:

Resolved Intent
      ↓
Validation
      ↓
Trust Evaluation
      ↓
READY
      ↓
Action Selection
      ↓
Execution Contract

A contract should not be generated as though execution were authorized when the Intent remains:

* unresolved
* incomplete
* invalid
* blocked
* waiting for required approval
* waiting for required authorization
* waiting for required evidence
* otherwise outside the execution boundary

⸻

11. Contract Preconditions

An Execution Contract may specify conditions that must hold before execution.

Examples:

account.status == ACTIVE
authorization.valid == true
approval.status == APPROVED
resource.version == expected_version

These conditions are particularly important where business state may change between Trust evaluation and execution.

A contract therefore does not eliminate the need for final consumer-side checks.

⸻

12. Consumer-Side Validation

Execution consumers remain authoritative for their own business state and may perform final validation before mutating that state.

For example:

T1 — Noema validates Intent
T2 — Noema evaluates Trust
T3 — Noema creates Execution Contract
T4 — Consumer receives Contract
T5 — Business state has changed
T6 — Consumer performs final validation
T7 — Consumer executes or rejects

This is necessary because consequential execution may encounter time-of-check/time-of-use conditions.

A consumer rejection does not necessarily mean that the earlier Noema Trust decision was invalid.

It may mean that the external business state changed after the decision.

⸻

13. Contract Immutability

Once an Execution Contract has crossed the execution boundary, its material execution semantics should be immutable.

A contract should not silently change:

* Action
* Target
* Actor
* material inputs
* authorization basis
* constraints
* expected effects
* execution scope

If a material change is required, Noema should invalidate the existing contract and produce a new contract through the appropriate lifecycle.

Conceptually:

Contract A
    ↓
material change
    ↓
invalidate Contract A
    ↓
re-evaluate
    ↓
Contract B

This preserves auditability and prevents an execution request from changing underneath the consumer.

⸻

14. Contract Expiration

Execution Contracts may have explicit validity windows.

Example:

valid_from = T1
valid_until = T2

If the contract expires before execution begins:

Execution Contract
       ↓
expired
       ↓
invalid
       ↓
re-evaluation

Noema must not assume that a previously trusted Intent remains executable indefinitely.

This follows the Trust State Machine principle that READY is not permanent.

⸻

15. Contract Identity and Idempotency

Consequential Actions should have explicit identity and, where appropriate, idempotency semantics.

The contract should allow the execution consumer to distinguish:

same execution request

from:

new execution request

This is important when:

* network retries occur
* acknowledgements are lost
* execution results are temporarily unknown
* consumers retry operations
* distributed systems produce duplicate delivery

Noema must not assume that a retry is harmless merely because the Action is logically identical.

⸻

16. Contract and Partial Execution

An Execution Contract should establish whether partial execution is permitted where the Action consists of multiple operations.

Noema must not infer permission for partial execution.

For a composite Intent:

A
B
C

the contract must make clear whether execution semantics are:

atomic

or:

partially executable

If partial execution is permitted, the resulting execution records must identify which components were executed and which were not.

⸻

17. Contract and Failure Semantics

Execution Contracts should establish expected failure handling where the Action requires it.

Relevant outcomes may include:

SUCCESS
REJECTED
FAILED
PARTIALLY_COMPLETED
UNKNOWN

An Execution Contract should not imply that successful Trust guarantees successful execution.

The relationship remains:

Trust
   ↓
Execution Eligibility
   ↓
Execution
   ↓
Outcome

Therefore:

READY ≠ SUCCESS

⸻

18. Contract and Postconditions

Where applicable, an Execution Contract should identify expected postconditions.

For example:

Action:
renew_card
Expected postcondition:
card.status == RENEWAL_REQUESTED

The execution consumer or outcome layer may then determine whether the expected postcondition was actually established.

Noema must distinguish:

requested effect

from:

observed business outcome

The enterprise system remains authoritative for the actual business state.

⸻

19. Contract Provenance

Every Execution Contract must remain traceable to the decision chain that produced it.

Conceptually:

Execution Contract
      ↓
Action
      ↓
Trusted Intent
      ↓
Trust Evaluation
      ↓
Validation
      ↓
Evidence / Context
      ↓
Actor Expression

The exact provenance model belongs to the relevant canonical specifications.

The architectural requirement is that execution must be reconstructible from recorded provenance.

⸻

20. Contract and Auditability

The execution boundary must be auditable.

At minimum, Noema should be able to establish:

* which Intent produced the contract
* which Action was selected
* which actor was associated with the request
* which authorization supported execution
* which Trust evaluation established eligibility
* which capability was invoked
* which execution consumer accepted the contract
* when execution began
* what outcome was reported

This does not require exposing private model reasoning.

It requires recording the deterministic decision and execution artifacts necessary to reconstruct what happened.

⸻

21. Contract Rejection

An execution consumer may reject an Execution Contract.

Possible reasons include:

* contract malformed
* capability unavailable
* precondition failed
* authorization no longer valid
* business state changed
* resource unavailable
* contract expired
* duplicate execution
* consumer policy rejected execution
* downstream dependency unavailable

A rejection must produce an explicit execution result.

Noema must not reinterpret rejection as successful execution.

⸻

22. Unknown Execution Outcome

A particularly important case occurs when Noema cannot determine whether execution succeeded.

Example:

Contract sent
    ↓
Consumer may have executed
    ↓
Network failure
    ↓
No response

The result must not automatically become:

FAILED

nor:

COMPLETED

unless authoritative evidence establishes the result.

The execution lifecycle must support an explicitly represented unknown outcome where required.

⸻

23. Contract and the Execution Boundary

The canonical execution boundary is:

                    Noema
                       │
                       │
                Execution Contract
                       │
═══════════════════════╪══════════════════════
                       │
                Execution Consumer
                       │
                       ▼
               Enterprise System

The contract is the explicit artifact crossing that boundary.

This provides a clear separation between:

Noema decision

and:

consumer execution

⸻

24. No Direct Model-to-Tool Execution

Noema must not establish an architectural path equivalent to:

LLM
 ↓
Tool Call
 ↓
Business System

for consequential Actions.

The canonical path is:

LLM
 ↓
Candidate Intent / Proposal
 ↓
Resolution
 ↓
Validation
 ↓
Trust
 ↓
Action Selection
 ↓
Execution Contract
 ↓
Execution Consumer
 ↓
Business System

The execution contract is therefore part of Noema’s control boundary, not merely a serialization convenience.

⸻

25. Typed Execution

Where practical, Execution Contracts should be typed.

For example:

RenewCardContract
TransferFundsContract
CreateEmployeeContract
CancelSubscriptionContract

rather than relying on unrestricted natural-language execution instructions.

Typed contracts make it possible to establish:

* required fields
* permitted parameters
* input types
* constraints
* capability requirements
* execution semantics
* failure semantics

The exact type system remains an implementation concern governed by subsequent specifications.

⸻

26. Contract Schema Evolution

Execution Contracts are integration boundaries and therefore require explicit versioning.

A contract should identify its applicable schema or contract version where necessary.

Changes to a contract that alter execution semantics must not silently break existing consumers.

Conceptually:

Contract v1
Contract v2
Contract v3

Each version should have defined compatibility and migration semantics.

⸻

27. Security Boundary

Execution Contracts form part of Noema’s security boundary.

The contract must not allow the execution consumer to infer broader authority than was established by Trust.

For example:

Trusted:
Transfer ₦50,000

must not become:

Transfer arbitrary amount

because the consumer happens to expose a broader capability.

The contract must constrain execution to the authority established by the upstream decision.

⸻

28. Least Authority

Execution Contracts should carry only the authority and scope required for the requested Action.

Where possible:

specific Actor
+
specific Action
+
specific Target
+
specific Inputs
+
specific Constraints

should be preferred over broad execution authority.

The contract must not become a mechanism for privilege escalation.

⸻

29. Relationship to Action Graphs

An Action Graph may describe the Actions and dependencies required to accomplish an Intent.

The Execution Contract represents the concrete execution request for an individual executable step or explicitly defined execution unit.

Conceptually:

Intent
  ↓
Action Graph
  ↓
Executable Action
  ↓
Execution Contract
  ↓
Execution Consumer

The Action Graph determines execution structure.

The Execution Contract establishes the concrete boundary for execution.

⸻

30. Relationship to Execution Planner

The Execution Planner may determine how a trusted Intent should be decomposed into executable Actions.

The planner does not itself authorize execution.

Therefore:

Trust
  ↓
Execution Planner
  ↓
Action Plan
  ↓
Execution Contract
  ↓
Execution

The planner may propose a plan, but the resulting execution requests must remain subject to the applicable Trust and contract constraints.

⸻

31. Relationship to Execution Record

An Execution Contract describes what was requested and under what terms.

An Execution Record describes what happened during execution.

Therefore:

Execution Contract
        ↓
Execution
        ↓
Execution Record
        ↓
Outcome

These artifacts must not be conflated.

A contract is not evidence that execution occurred.

An execution record is evidence about execution.

⸻

32. Relationship to Outcome

The Execution Contract may specify expected postconditions.

The Outcome Engine determines the observed result using execution records and authoritative external state where necessary.

Therefore:

Contract
  ↓
Execution
  ↓
Observed Result
  ↓
Outcome

Noema must not manufacture an outcome merely because a contract was accepted.

⸻

33. Contract Lifecycle

A conceptual Execution Contract lifecycle is:

DRAFT
  ↓
ISSUED
  ↓
ACCEPTED
  ↓
EXECUTING
  ↓
COMPLETED / FAILED / UNKNOWN

Contracts may also become:

REJECTED
EXPIRED
INVALIDATED
CANCELLED

The exact execution state machine is defined elsewhere.

This ADR establishes that contract lifecycle must be explicit rather than implicit.

⸻

34. Cancellation

Where an Action supports cancellation, cancellation must itself be governed by explicit semantics.

Noema must not assume that every execution can be safely cancelled after execution begins.

A contract should therefore establish cancellation semantics where relevant.

Examples:

cancellable before execution
cancellable during execution
not cancellable

The authoritative consumer determines whether cancellation can actually occur.

⸻

35. Human Approval

Where policy requires human approval, the Execution Contract must not be issued as executable authority before the required approval condition has been satisfied.

The canonical lifecycle is:

Intent
  ↓
Trust Evaluation
  ↓
WAITING_FOR_APPROVAL
  ↓
Approval Received
  ↓
Re-evaluation
  ↓
READY
  ↓
Execution Contract

Approval is therefore part of the Trust lifecycle rather than an informal conversational confirmation.

⸻

36. Determinism

For the same:

* Intent
* Trust decision
* Action selection
* Context
* Evidence
* policy version
* capability definition
* contract schema version

contract generation should produce the same material execution semantics.

The model must not be able to alter a contract’s authority merely by producing a different explanation or wording.

⸻

37. Failure-Closed Principle

If a mandatory condition required to establish safe execution is unknown or unavailable, Noema must not broaden the Execution Contract to compensate.

For example:

Authorization = UNKNOWN

must not result in:

Contract = authorized

Similarly:

Target = UNKNOWN

must not result in:

Contract = best_guess_target

The correct response is to remain outside the execution boundary until the required conditions are established.

⸻

38. Explicitness Over Convenience

Noema deliberately accepts additional structure in exchange for:

* auditability
* determinism
* bounded authority
* interoperability
* reproducibility
* safer retries
* explicit failure semantics
* clearer system boundaries

The contract is therefore not considered unnecessary overhead.

It is part of the infrastructure Noema provides.

⸻

39. Alternatives Considered

Alternative A — Execute Model Output Directly

LLM → Tool → System

Rejected.

This would collapse probabilistic inference and deterministic execution authority into one path.

⸻

Alternative B — Use Natural Language as the Execution Contract

"Transfer ₦50,000 to John."

Rejected as the canonical mechanism.

Natural language may be an input to Intent resolution, but it does not provide sufficiently explicit and typed execution semantics.

⸻

Alternative C — Allow Each Consumer to Interpret Intent Independently

Intent
 ↓
Consumer-specific interpretation
 ↓
Execution

Rejected as the canonical architecture.

This would distribute semantic interpretation and authority decisions across consumers and make Noema’s execution boundary inconsistent.

⸻

Alternative D — Treat Capability Invocation as the Contract

A capability invocation alone is insufficient because capability does not establish:

* why the Action is authorized
* which Intent produced it
* which constraints apply
* what preconditions were established
* what postconditions are expected
* what execution scope was approved

Therefore capability invocation and Execution Contract remain separate concepts.

⸻

40. Consequences

Positive Consequences

Explicit Execution Contracts provide:

* a deterministic execution boundary
* typed execution semantics
* clearer authorization scope
* stronger auditability
* explicit preconditions and constraints
* consumer interoperability
* safer retries
* explicit failure semantics
* traceability from execution back to Intent
* separation between Noema and enterprise systems

Costs

The approach introduces:

* additional schemas
* contract versioning
* contract lifecycle management
* serialization and validation overhead
* integration work for execution consumers
* additional provenance requirements

These costs are accepted because the execution boundary is foundational to Noema’s architecture.

⸻

41. Invariants

Invariant 1

Model output is not an Execution Contract.

Invariant 2

A contract cannot bypass Trust.

Invariant 3

Capability does not imply permission.

Invariant 4

Permission does not imply capability.

Invariant 5

An Execution Contract must identify the Action being requested.

Invariant 6

Material execution semantics must be explicit.

Invariant 7

Execution Contracts must remain traceable to the Intent and Trust decision that produced them.

Invariant 8

Material contract changes require explicit invalidation and re-issuance.

Invariant 9

Contract acceptance does not guarantee successful execution.

Invariant 10

Enterprise systems remain authoritative for their business state.

Invariant 11

Unknown mandatory execution conditions must not be silently converted into authorization.

Invariant 12

Execution consumers may perform final authoritative validation.

Invariant 13

Contract execution must produce an explicit execution result.

Invariant 14

Consequential Actions require explicit failure and outcome semantics.

Invariant 15

Noema executes contracts, not arbitrary model-generated instructions.

⸻

42. Canonical Flow

                 Human Expression
                        │
                        ▼
                     Intent
                        │
                        ▼
                   Resolution
                        │
                        ▼
                    Validation
                        │
                        ▼
                 Trust Evaluation
                        │
                        ▼
                      READY
                        │
                        ▼
                  Action Selection
                        │
                        ▼
               Execution Contract
                        │
                        ▼
               Consumer Acceptance
                        │
                        ▼
                    Execution
                        │
                        ▼
                 Execution Record
                        │
                        ▼
                     Outcome

At any stage before contract issuance:

UNCERTAIN → CLARIFY
INVALID   → BLOCK
UNTRUSTED → WAIT

The execution boundary is crossed only through an explicit contract.

⸻

43. Relationship to the Canon

This ADR formalizes the Canon’s principle:

Execution must occur through explicit capabilities and contracts.

It also reinforces the following canonical boundaries:

Probabilistic inference
        ≠
Deterministic trust
        ≠
Execution authority
        ≠
Business state

The Execution Contract is the artifact that makes the transition from trusted Noema state to external execution explicit.

⸻

44. Final Decision

Noema will use explicit, typed, traceable Execution Contracts as the canonical mechanism for crossing the execution boundary.

No model output, natural-language instruction, capability declaration, or conversational exchange is by itself sufficient to authorize consequential execution.

The canonical principle is:

Intent
  ↓
Trust
  ↓
Action
  ↓
Execution Contract
  ↓
Consumer
  ↓
Execution
  ↓
Outcome

Noema does not execute what the model says.
Noema executes what has been established, authorized, contracted, and explicitly accepted for execution.