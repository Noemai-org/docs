Yes. 01-ontology/action.md should define what an Action is in Noema’s conceptual model, without yet getting into the implementation-level action contract. That distinction matters because 11-contracts/action-contract.md will later define how an Action becomes executable.

I’d make the ontology document look like this:

Action

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: 01-ontology/action.md

⸻

1. Definition

An Action is a bounded operation that Noema can cause to occur in an external system or within a Noema-controlled execution boundary in pursuit of an Intent.

An Action represents what can be done, not what the user said and not what the system ultimately accomplished.

In the Noema model:

Intent
   ↓
Action
   ↓
Execution
   ↓
Outcome

An Action is therefore the bridge between intent and execution.

⸻

2. Action Is Not Intent

Intent expresses what an actor wants to accomplish.

Action expresses an operation that can contribute to accomplishing that objective.

For example:

Intent:
"Renew my expired card."
Possible Actions:
- Retrieve current card status
- Verify customer identity
- Determine renewal eligibility
- Request card renewal
- Generate replacement card
- Notify customer

A single Intent may require multiple Actions.

Conversely, the same Action may contribute to multiple different Intents.

Therefore:

Intent is goal-oriented; Action is operation-oriented.

⸻

3. Action Is Not Execution

An Action describes an operation that may be performed.

Execution is the actual attempt to perform that operation.

Action
  │
  │ execution
  ▼
Attempt
  │
  ▼
Result

The existence of an Action does not imply that it has been executed.

An Action may be:

* proposed
* selected
* authorized
* rejected
* scheduled
* executing
* completed
* failed
* cancelled

These are states of the Action’s lifecycle or execution, not different Actions.

⸻

4. Action Is Not Outcome

An Action describes what Noema intends to cause.

An Outcome describes what actually happened as a consequence of execution.

For example:

Action:
"Request card renewal."
Possible Outcomes:
SUCCESS
Card renewal request accepted.
FAILURE
Renewal request rejected by the banking system.
PARTIAL
Renewal request created but notification failed.
UNKNOWN
The external system did not provide a definitive result.

Therefore:

An Action is a desired operation; an Outcome is an observed consequence.

Noema must not assume that executing an Action guarantees its intended Outcome.

⸻

5. Action Has a Target

An Action operates on something.

The target may be:

* a business entity
* a resource
* a system
* an external service
* a collection of resources
* an internal Noema-controlled resource

For example:

Action:
RequestCardRenewal
Target:
CustomerCard#1234

The target must be sufficiently identified before an Action can become executable.

If the target is ambiguous and the ambiguity is material to execution, Noema must transition to clarification rather than guess.

⸻

6. Action Has Inputs

An Action may require structured inputs.

For example:

Action:
SchedulePayment
Inputs:
- source_account
- destination_account
- amount
- currency
- execution_date

Inputs may originate from:

* the resolved Intent
* contextual information
* enterprise system state
* previously executed Actions
* explicit user-provided information
* trusted external evidence

Noema must distinguish between:

known input

and

inferred input.

An inferred value must not automatically be treated as an authoritative value.

⸻

7. Action Has Preconditions

A precondition is a condition that must be satisfied before an Action may execute.

Examples:

Card is eligible for renewal.
Customer identity has been verified.
Actor has permission to request renewal.
Required system capability is available.
Required input fields are present.

Conceptually:

Intent
  ↓
Action
  ↓
Preconditions
  │
  ├── satisfied → executable
  │
  └── unsatisfied → cannot execute

Preconditions are part of the Action’s semantics.

They are not merely implementation checks.

⸻

8. Action Requires Capability

An Action must map to a capability that can actually perform it.

A capability represents the ability of a system or component to perform an operation.

For example:

Action:
RequestCardRenewal
Capability:
banking.cards.renew

Noema must not treat an abstract intention as executable merely because a model can describe how it might be performed.

There must be an actual capability through which the Action can be executed.

An Action without an available capability is not executable.

⸻

9. Action Is Subject to Authority

Capability does not establish authority.

A system may be capable of performing an Action while the current actor is not authorized to cause it.

Therefore:

Capability ≠ Authority

An Action becomes executable only when the relevant authority requirements are satisfied.

Authority may depend on:

* actor identity
* role
* organizational context
* resource ownership
* policy
* delegated authority
* approval requirements
* risk boundaries

⸻

10. Action Has Constraints

An Action may be subject to constraints derived from:

* the Intent
* user instructions
* organizational policy
* system policy
* regulatory requirements
* resource limitations
* temporal requirements
* financial limits
* security requirements

For example:

Intent:
"Book me the cheapest flight, but don't depart before 9am."
Action:
BookFlight
Constraint:
departure_time >= 09:00

Constraints restrict the permissible execution space.

Noema must preserve constraints when translating Intent into Actions.

⸻

11. Action May Produce Side Effects

Actions can change state outside Noema.

Examples include:

* creating a payment
* sending an email
* updating a customer record
* cancelling a subscription
* issuing a card
* creating an employee account

Actions with side effects require greater execution discipline than read-only Actions.

Conceptually:

Read Action
    ↓
Observe state
Write Action
    ↓
Change state

The ontology should therefore distinguish between actions that observe and actions that mutate, even if the precise classification is defined elsewhere.

⸻

12. Action Has Expected Postconditions

An Action may define conditions expected to hold after successful execution.

For example:

Action:
RequestCardRenewal
Expected Postcondition:
Card renewal request exists.

Postconditions provide a basis for verifying execution.

The expected postcondition is not itself proof that the Action succeeded.

Noema should verify the observed state where the external system permits verification.

Action
  ↓
Execution
  ↓
Observed State
  ↓
Postcondition Verification
  ↓
Outcome

⸻

13. Actions May Be Composed

Complex Intents may require multiple Actions.

For example:

Intent:
"Renew my expired card."
Action sequence:
1. RetrieveCard
2. VerifyEligibility
3. VerifyIdentity
4. RequestRenewal
5. VerifyRenewalRequest
6. NotifyCustomer

An Action sequence may contain:

* dependencies
* conditional branches
* parallel Actions
* retries
* compensating Actions
* human approval points

However, composition must not erase the identity and contract of individual Actions.

Each Action remains independently meaningful.

⸻

14. Actions May Be Conditional

An Action may depend on the result of another Action.

For example:

VerifyEligibility
       │
       ├── eligible → RequestRenewal
       │
       └── ineligible → NotifyCustomer

The decision to execute a subsequent Action must be based on explicit state or verified evidence rather than an assumed result.

⸻

15. Actions Have Different Risk Profiles

Not all Actions have equivalent consequences.

A read operation may have negligible external impact.

A financial transaction may have substantial consequences.

An Action’s risk may therefore influence:

* required authorization
* required evidence
* approval requirements
* trust thresholds
* human intervention
* execution controls
* audit requirements

Risk does not change the definition of Action.

It changes the conditions under which the Action may be executed.

⸻

16. Reversibility Matters

Actions differ in their reversibility.

An Action may be:

Reversible

Its effects can be reliably undone.

Compensatable

Its original operation cannot be directly undone, but another operation can compensate for the effect.

Irreversible

Its effects cannot reliably be reversed.

For example:

UpdateAddress
    → potentially reversible
SendPayment
    → potentially compensatable
DeleteIrreplaceableData
    → potentially irreversible

The reversibility of an Action should influence execution policy and risk evaluation.

⸻

17. Idempotency Is an Action Property

For Actions that may be retried, Noema must understand whether repeated execution produces the same effective result or creates additional side effects.

Conceptually:

Action A
   ↓
Execute
   ↓
Timeout
   ↓
Unknown outcome
   ↓
Retry?

The answer cannot be determined solely by the model.

It must be defined by the Action’s execution semantics.

Therefore Action semantics may include an idempotency model such as:

* naturally idempotent
* explicitly idempotent
* non-idempotent
* unknown

The precise contract is defined in 11-contracts/action-contract.md.

⸻

18. Actions Require Provenance

Noema should be able to determine why an Action exists in an execution flow.

The provenance of an Action may include:

Intent
  ↓
Context
  ↓
Policy
  ↓
Evidence
  ↓
Action Selection

This allows Noema to answer:

Why was this Action selected?

The answer should be represented through structured provenance rather than dependence on hidden model reasoning.

⸻

19. Action Lifecycle

At the ontology level, an Action may move through states such as:

PROPOSED
   ↓
VALIDATED
   ↓
AUTHORIZED
   ↓
READY
   ↓
EXECUTING
   ↓
COMPLETED

Alternative transitions may include:

PROPOSED
   ↓
REJECTED
VALIDATED
   ↓
BLOCKED
EXECUTING
   ↓
FAILED
EXECUTING
   ↓
UNKNOWN_OUTCOME
EXECUTING
   ↓
PARTIALLY_COMPLETED

The definitive Action state machine belongs in the relevant intent/execution specifications.

This document defines the conceptual lifecycle only.

⸻

20. Action and Trust

An Action does not become executable simply because it was generated from a trusted-looking Intent.

Noema must establish that the particular Action is appropriate and permitted.

Conceptually:

Trusted Intent
      ↓
Candidate Action
      ↓
Action Validation
      ↓
Authority + Capability + Preconditions
      ↓
Executable Action

Trust therefore applies to the transition from intent to permitted action, not merely to the interpretation of the user’s language.

⸻

21. Action and the Model

A model may:

* propose an Action
* rank possible Actions
* construct Action parameters
* suggest an Action sequence
* explain possible alternatives

But model output is not itself an Action in the executable sense.

The canonical distinction is:

Model Proposal
      ↓
Noema Validation
      ↓
Canonical Action
      ↓
Action Contract
      ↓
Execution

The model proposes; Noema establishes; the execution system performs.

⸻

22. Action and Business Systems

An Action may ultimately be executed by an external system.

For example:

Noema Action
    ↓
Banking Capability
    ↓
Banking API
    ↓
Banking System

The external system remains authoritative for the resulting business state.

Noema records the relevant execution and outcome state but does not become the owner of that business state merely because it initiated the Action.

⸻

23. Canonical Distinction

Noema must preserve the following distinctions:

Intent
"What does the actor want?"
Action
"What operation can advance that intent?"
Capability
"What system can perform that operation?"
Authority
"Who is permitted to cause that operation?"
Contract
"Under what explicit terms may the operation execute?"
Execution
"What attempt was made to perform it?"
Outcome
"What actually happened?"

These concepts are related but must not be collapsed into a single abstraction.

⸻

24. Action Ontology

At the conceptual level, an Action can be represented as:

Action
├── identity
├── objective
├── target
├── inputs
├── context
├── constraints
├── capability
├── authority requirements
├── preconditions
├── expected postconditions
├── side effects
├── risk profile
├── reversibility
├── idempotency semantics
├── provenance
└── lifecycle state

This is an ontology-level representation.

It is intentionally not an implementation schema.

The executable representation is defined separately by:

11-contracts/action-contract.md

⸻

25. Core Invariants

Invariant 1

An Action is an operation, not a human utterance.

Invariant 2

An Action is not an execution.

Invariant 3

An Action is not an Outcome.

Invariant 4

An Action must map to an available Capability before it can execute.

Invariant 5

Capability does not imply Authority.

Invariant 6

Materially ambiguous Action targets or parameters must not be guessed.

Invariant 7

Action execution must respect applicable Preconditions and Constraints.

Invariant 8

Model-generated Actions are proposals until validated by Noema.

Invariant 9

Side-effecting Actions require explicit execution semantics.

Invariant 10

Action outcomes must be distinguished from Action intent.

Invariant 11

Action selection must have sufficient provenance to explain why the Action was selected.

Invariant 12

Noema must not claim successful execution solely because an execution attempt was made.

Invariant 13

The authoritative business state resulting from an Action remains owned by the relevant external system.

⸻

26. Relationship to Other Canonical Domains

This document defines the ontology of Action.

Related definitions live in:

01-ontology/
├── intent.md
├── context.md
├── capability.md
├── constraint.md
├── policy.md
├── outcome.md
└── state.md

Action execution semantics live in:

04-execution/

Executable Action contracts live in:

11-contracts/action-contract.md

The Trust Engine’s treatment of Actions lives in:

03-trust/

Reference implementations of Actions live in:

09-reference-workflows/

⸻

27. Canonical Summary

An Action is a bounded, targetable operation that can advance an Intent and can become executable only when its required capability, authority, constraints, preconditions, and execution semantics have been established.

An Action is the canonical bridge between what a human intends and what a system can actually do.

It is neither the intent itself nor the resulting business outcome.

INTENT
  │
  │ motivates
  ▼
ACTION
  │
  │ executed through
  ▼
CAPABILITY
  │
  │ operates on
  ▼
TARGET
  │
  │ produces
  ▼
OUTCOME