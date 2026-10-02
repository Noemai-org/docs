> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Action

Status: Foundational
Version: 0.3
Domain: Ontology
Canonical Path: ontology/action.md

⸻

1. Definition

An Action is a typed, bounded, declarative operation instance that may be used to advance a resolved Intent through a registered Capability.

An Action specifies:

* what operation is being proposed or planned
* what target or resources it concerns
* what typed parameters it carries
* what constraints apply
* what preconditions must hold
* which registered Capability can perform it
* what outcome is expected
* how the result is to be verified
* why the Action exists
* what authority, policy, and execution requirements govern it

An Action is not itself an API call.

It is not an execution attempt.

It is not an Outcome.

It is a bounded semantic/execution object between Intent and the actual invocation of a Capability.

The canonical relationship is:

Intent
   ↓
Action Graph / Plan
   ↓
Typed Action
   ↓
Registered Capability
   ↓
Execution Attempt
   ↓
Observed State
   ↓
Verification
   ↓
Outcome

Noema’s execution architecture requires the Model to select only from a finite, pre-registered Capability Registry and prohibits arbitrary model-constructed calls. The model has no credentials or direct system access; deterministic Noema components validate and govern the resulting object. NOEMA POC Specification PDF.pdf

An Action therefore represents a candidate or governed operation, not authority to perform that operation.

⸻

2. Action Is Not Intent

Intent answers:

What does the Actor want accomplished?

Action answers:

What bounded operation can advance that Intent?

Example:

Intent:
Investigate my failed transfer.
Possible Actions:
├── LOOKUP_TRANSACTION
├── LOOKUP_TRANSACTION_HISTORY
├── QUERY_SWITCH_STATUS
├── QUERY_SETTLEMENT_STATUS
├── RECONCILE_TRANSACTION_STATE
└── CREATE_ESCALATION_TICKET

The Intent is goal-oriented.

The Action is operation-oriented.

A single Intent may produce multiple Actions.

Conversely, one Action type may serve many different Intents.

Therefore:

Intent ≠ Action

The Noema architecture explicitly separates Intent, Context, Trust, Action Graph, Planner, Execution, Verification, Recovery, and Audit.

⸻

3. Action Is Not Capability

This distinction is fundamental.

A Capability describes an available ability of an execution system.

An Action is a particular typed operation instance that intends to use that ability.

Conceptually:

Capability:
LOOKUP_TRANSACTION
Action:
LOOKUP_TRANSACTION(
    transaction_ref = TX88213
)

Therefore:

Capability = what the system is registered to perform
Action     = the specific bounded operation being proposed/planned

A Capability is registered independently of any particular Intent.

An Action references a registered Capability.

Noema must never infer:

model can describe operation
        ↓
operation is executable

Instead:

Action
   ↓
Capability Registry lookup
   ↓
Registered Capability
   ↓
Contract validation
   ↓
Trust / authority / policy requirements
   ↓
Execution

The Capability Registry defines the permitted operation set and associated parameter schema, preconditions, authorization requirements, policy requirements, side effects, expected outcome, verification, retry/recovery semantics, risk, and audit requirements. NOEMA POC Specification PDF.pdf

⸻

4. Action Is Not Execution

An Action is a description of an operation.

Execution is the actual attempt to perform that operation.

Action
   ↓
Execution Attempt
   ↓
Result

The distinction is essential because execution can:

* succeed
* fail
* timeout
* return an ambiguous result
* partially complete
* produce an unknown outcome
* be interrupted
* require recovery

Therefore:

Action exists
≠
Action was executed

The actual execution attempt must have its own identity.

In the POC:

intent_id
    ≠
execution_attempt_id

A timeout must never be interpreted automatically as either failure or permission to retry.

A fresh verification read is required before determining what happened or whether retry is permissible. The POC explicitly requires verification before retry and treats EXECUTION_OUTCOME_UNKNOWN as a load-bearing state. NOEMA POC Specification PDF.pdf

⸻

5. Action Is Not Outcome

An Action describes what operation should be attempted.

An Outcome describes what actually happened.

Example:

Action:
CREATE_ESCALATION_TICKET
Execution:
Attempted through registered Capability
Observed:
Ticket exists in escalation system
Verified Outcome:
ESCALATION_CREATED

Or:

Action:
CREATE_ESCALATION_TICKET
Execution:
Request timed out
Observed:
Unknown
Outcome:
EXECUTION_OUTCOME_UNKNOWN

Noema must never infer successful Outcome merely because an Action was constructed or an execution request was submitted.

Verification determines whether the expected real-world result occurred.

⸻

6. Action Is Declarative, Not an Arbitrary Command

An Action is a typed declaration of an operation.

It is not arbitrary executable text.

Bad:

Action:
"Call whatever API seems appropriate to refund this customer."

Canonical:

Action {
    capability:
        CREATE_ESCALATION_TICKET
    parameters:
        case_id = CASE-123
        reason_code = DUPLICATE_TRANSACTION
    contract_version:
        v1
}

This distinction prevents the Model from becoming an uncontrolled execution authority.

The Model may propose an Action.

Noema validates the Action.

The Execution Controller executes only what the registered contract permits.

The model has no direct execution credentials or direct system access. NOEMA POC Specification PDF.pdf

⸻

7. Typed Action Contract

Every executable Action must conform to a typed Action Contract.

Conceptually:

Action
├── action_type
├── action_id
├── intent_id
├── capability
├── capability_version
├── target
├── parameters
├── preconditions
├── constraints
├── authority_requirements
├── policy_requirements
├── expected_outcome
├── verification
├── risk
├── side_effects
├── idempotency
├── provenance
└── status

The exact executable schema belongs in:

contracts/action-contract.md

The ontology defines the semantic meaning of these components.

The contract defines the machine-enforceable representation.

An Action Contract must not itself grant authority merely because a conforming Action can be serialized or transported.

⸻

8. Closed-World Capability Binding

Noema must operate under a closed-world assumption for executable capabilities.

That means:

If a Capability is not registered, it is not executable.

The Model cannot invent:

* a new endpoint
* a new tool
* a new capability name
* an arbitrary API
* an arbitrary parameter
* an undocumented operation

The Action must reference a Capability that exists in the authoritative Capability Registry.

Conceptually:

Candidate Action
      ↓
Capability Registry
      │
      ├── registered → continue validation
      │
      └── absent → NOT_EXECUTABLE

The registry is the architectural execution boundary.

For the POC, prohibited monetary capabilities are explicitly represented as prohibited registry entries with hard-coded rejection rather than being merely absent. NOEMA POC Specification PDF.pdf

⸻

9. Action Identity

Every Action instance should have a stable identity.

Conceptually:

ActionID

Example:

Action#A7F31

Action identity permits Noema to correlate:

* Intent
* Action Graph node
* Action Plan
* Capability
* parameters
* target
* authorization
* policy
* execution attempt
* verification
* Outcome
* audit events

Action identity must remain distinct from:

IntentID
ExecutionAttemptID
OutcomeID
TrustDecisionID

One Intent may contain many Actions.

One Action may produce multiple execution attempts only where the execution semantics explicitly permit them.

⸻

10. Action Version

Action definitions and contracts may evolve.

Therefore Noema should distinguish:

Action Identity

from:

Action Contract Version

Example:

Action#A7F31
Capability:
CREATE_ESCALATION_TICKET
Contract:
v1

A contract revision must not silently reinterpret an existing historical execution.

Consequential records must retain the version under which the Action was evaluated and executed.

⸻

11. Action Target

An Action may operate on:

* an Entity
* a Resource
* a collection
* a Case
* an enterprise record
* an internal Noema object
* an external system resource

Example:

Action:
RECORD_INVESTIGATION_EVIDENCE
Target:
Case#123

The target is a first-class part of Action identity and governance.

The target must be sufficiently grounded before execution.

If the target remains materially ambiguous:

Action
    ↓
TARGET = AMBIGUOUS
    ↓
cannot execute
    ↓
CLARIFY / ESCALATE

Noema must not resolve a material target by arbitrary selection merely to make execution possible.

Target Binding

Authorization, constraints, policy, and execution eligibility must bind to the specific resolved target, not merely to the Capability or Action type.

For example:

Capability:
LOOKUP_TRANSACTION
Action:
LOOKUP_TRANSACTION(TX88213)
Target:
Transaction#TX88213
Authorization:
Actor may investigate Transaction#TX88213

is materially different from:

Actor may invoke LOOKUP_TRANSACTION

The latter is technical capability authorization; it does not establish authorization to access every possible transaction.

A technically authorized Action against the wrong resolved entity is a confused-deputy condition. Noema therefore evaluates authorization against the specific resolved entity/action. NOEMA POC Specification_1.pdf

⸻

12. Action Parameters

Actions carry structured, typed parameters.

Example:

Action:
LOOKUP_TRANSACTION
Parameters:
    transaction_ref:
        value = "TX88213"
        type = TransactionReference

Parameters may originate from:

* resolved Intent
* Context
* authoritative enterprise state
* evidence
* previous Action results
* explicit Actor input

The source of each material parameter should remain traceable.

Noema must distinguish:

KNOWN

from:

INFERRED

and must not silently convert an inference into an authoritative execution parameter.

Where a parameter depends on enterprise state, its provenance should identify the source and relevant freshness/status.

The model’s proposal of a parameter is evidence of proposal, not proof of correctness or authority.

⸻

13. Action Preconditions

A precondition is a condition that must hold before the Action may execute.

Examples:

* transaction exists
* case is open
* actor identity is established
* required evidence exists
* required capability is registered
* required authority exists
* policy evaluation has succeeded
* target is not ambiguous
* required enterprise state is sufficiently fresh
* required state facts are not contradictory
* required verification state exists

Preconditions must be explicit.

They are not merely implementation checks.

Conceptually:

Action
   ↓
Preconditions
   │
   ├── satisfied → eligible for execution
   │
   └── unsatisfied → blocked

An Action must not execute merely because its parameters are syntactically valid.

⸻

14. Action Constraints

Constraints restrict the permissible execution space.

Constraints may originate from:

* Intent
* Actor instructions
* Policy
* Authority or delegation
* domain rules
* security requirements
* temporal requirements
* system limits
* risk controls
* Capability requirements

Example:

Intent:
Investigate this transaction, but do not expose another customer's data.
Action:
LOOKUP_TRANSACTION
Target:
Resolved Transaction#TX88213
Constraint:
requested transaction must belong to the authorized Actor's investigation scope

Constraints must survive the transformation:

Intent
   ↓
Action Graph
   ↓
Action Plan
   ↓
Action
   ↓
Execution

No planner or execution layer may silently discard them.

Material constraints must be evaluated against the actual Action target and relevant current state before execution.

⸻

15. Authority Is Separate From Capability

Capability answers:

Can the system perform this operation?

Authority answers:

Is this Actor permitted to cause this operation on this specific target under the current circumstances?

Therefore:

Capability ≠ Authority

An Action can reference a valid Capability and still be prohibited because:

* the Actor lacks authority
* the Actor is not the verified party
* the resource belongs to another principal
* required delegation is absent
* approval is missing
* a threshold is exceeded
* policy prohibits the operation

Noema distinguishes technical authorization, policy authorization, and business authorization. In particular, authorization must bind to the fully resolved business Action rather than stopping at general tool or capability access. NOEMA POC Specification_1.pdf

The Action therefore carries authority requirements and binding context, while the actual authorization decision remains a governance decision.

⸻

16. Policy Is Separate From Action

Policy determines whether a particular Action may proceed under applicable rules.

The Action should not mutate itself to satisfy Policy.

Example:

Requested Action:
CREATE_ESCALATION_TICKET
Policy:
Manager approval required
Trust Decision:
CONFIRM / ESCALATE / REJECT

The semantic Action remains the operation the system evaluated.

The governance decision remains separate.

Policy is versioned and its governing version must be retained with the Trust Decision. The POC resolves policy against the timestamp at which the Intent Object enters Trust evaluation rather than silently changing the governing policy merely because execution occurs later. NOEMA POC Specification_1.pdf

⸻

17. Action Risk

Actions may have different risk classifications.

Relevant dimensions include:

* side-effect magnitude
* reversibility
* authorization sensitivity
* data sensitivity
* financial consequence
* operational consequence
* security consequence
* regulatory consequence

Risk may determine:

* required authorization
* required confirmation
* evidence requirements
* policy checks
* human approval
* execution controls
* audit requirements
* verification requirements

Risk does not change what an Action is.

It changes the conditions under which it may proceed.

⸻

18. Side Effects

An Action must declare whether it produces side effects.

Conceptually:

side_effects:
    NONE

or:

side_effects:
    CASE_CREATED

or:

side_effects:
    CUSTOMER_RECORD_MODIFIED

Side effects are important because execution safety requirements differ substantially between observation and mutation.

For the Noema POC, read-only diagnostic depth is in scope together with narrowly governed non-monetary writes. Operations changing monetary balances are outside the execution boundary. NOEMA POC Specification PDF.pdf

⸻

19. POC Execution Boundary

The current POC has an explicit capability boundary.

Allowed capabilities include:

LOOKUP_TRANSACTION
LOOKUP_ACCOUNT
LOOKUP_TRANSACTION_HISTORY
QUERY_SWITCH_STATUS
QUERY_SETTLEMENT_STATUS
LOOKUP_BENEFICIARY
RECONCILE_TRANSACTION_STATE
EVALUATE_SLA_STATUS
CREATE_ESCALATION_TICKET
LOG_COMPLIANT_COMPLAINT_REFERENCE
ROUTE_TO_INTERNAL_OWNER
RECORD_INVESTIGATION_EVIDENCE

Explicitly prohibited capabilities include:

TRANSFER_FUNDS
REVERSE_TRANSACTION
ADJUST_BALANCE
INITIATE_REFUND

The prohibited capabilities are represented explicitly in the registry as PROHIBITED with hard-coded rejection.

This is a POC execution profile, not a universal limitation of the Action ontology. NOEMA POC Specification PDF.pdf

⸻

20. Action and the Execution Boundary

The Action is the object crossing toward execution.

It must not cross the execution boundary merely because a Model proposed it.

Canonical flow:

Model
  ↓
Candidate Action
  ↓
Schema / Contract Validation
  ↓
Target Binding
  ↓
Capability Validation
  ↓
Trust / Authority / Policy
  ↓
Precondition / Constraint Validation
  ↓
Planner / Action Graph
  ↓
Bounded Action
  ↓
Execution Controller
  ↓
Execution Attempt

The Execution Controller must reject anything outside the registered boundary.

The architecture therefore treats execution authority as a property of the deterministic system rather than the Model.

Execution-Gate Revalidation

A previously governed Action is not automatically executable forever.

Where relevant state, authorization, constraint applicability, policy, target binding, or other execution-critical facts may have changed, the execution boundary must re-evaluate the material requirements against current authoritative state before committing the side effect.

A Trust Decision has an evaluation time and expiry semantics; execution must not treat an expired or materially stale governance result as indefinitely valid. The POC explicitly models decision expiry and requires current state verification in recovery/resume scenarios. NOEMA POC Specification MD.md

⸻

21. Action and the Model

The Model may:

* propose an Action
* identify candidate Actions
* construct candidate parameters
* suggest an Action sequence
* identify candidate dependencies
* propose candidate targets

The Model may not:

* execute the Action
* construct arbitrary calls
* invent capabilities
* bypass the Capability Registry
* grant itself authority
* determine its own Trust decision
* declare execution successful
* turn untrusted retrieved/tool content into authoritative Action requirements

Canonical distinction:

Model Proposal
      ↓
Noema Validation
      ↓
Target / Parameter Grounding
      ↓
Canonical Action
      ↓
Action Contract
      ↓
Trust / Policy / Authority
      ↓
Execution Controller
      ↓
Execution Attempt

The Model’s output is a proposal source.

It is not an authority source.

Enterprise data, tool output, retrieved content, or model-generated text must not become authoritative merely because they were ingested into the Action pipeline. Authority derives from the governing Noema/enterprise source and its applicable contract, policy, or system-of-record semantics.

The POC security architecture explicitly requires the Trust Engine to evaluate proposals against real state and policy regardless of their source. NOEMA POC Specification PDF.pdf

⸻

22. Action Graph

Actions exist within an Action Graph when an Intent requires multiple operations.

The Action Graph is executable architecture, not merely a visualization.

Example:

Resolve User
     ↓
Identify Account
     ↓
Generate Transaction Candidates
     ↓
Resolve Ambiguity
     ↓
Query Ledger
     ├── Query Switch
     └── Query Settlement
     ↓
Reconcile State
     ↓
Evaluate Policy
     ↓
Determine Outcome
     ↓
Explain / Escalate / Execute Non-Monetary Action
     ↓
Verify
     ↓
Audit

Each graph node carries execution-relevant information including:

* preconditions
* required evidence
* authority requirements
* policy requirements
* expected outcome
* verification method
* failure path
* recovery/escalation path

The Action Graph must preserve Action identity, target binding, constraints, and provenance as an Action moves through planning.

The POC defines the Action Graph as an executable graph rather than a diagram. NOEMA POC Specification PDF.pdf

⸻

23. Action Plan Is Not Action

An ActionPlan is a plan containing one or more Actions and their relationships.

Therefore:

Action
    = one bounded operation
ActionPlan
    = structured set of Actions and execution relationships

Example:

ActionPlan#42
1. LOOKUP_TRANSACTION
2. QUERY_SWITCH_STATUS
3. QUERY_SETTLEMENT_STATUS
4. RECONCILE_TRANSACTION_STATE
5. CREATE_ESCALATION_TICKET

The ActionPlan may contain:

* ordering
* dependencies
* conditional branches
* parallelism
* retry policy
* compensation
* escalation
* verification requirements

The individual Actions retain their own identities and contracts.

⸻

24. Action Dependencies

Actions may depend on previous Actions.

Example:

LOOKUP_TRANSACTION
        ↓
RECONCILE_TRANSACTION_STATE
        ↓
CREATE_ESCALATION_TICKET

The downstream Action must consume actual outputs or verified state rather than assumed outputs.

For example:

Query
  ↓
Observed State
  ↓
Decision
  ↓
Next Action

not:

Query
  ↓
Assumed State
  ↓
Next Action

This is especially important when enterprise systems can return stale, contradictory, delayed, or semantically misleading responses.

A dependency on enterprise state must identify the state facts required by the Action and must not silently substitute stale or lower-authority data where the authoritative source is available.

⸻

25. Conditional Actions

An Action may be executed only if an explicit condition is satisfied.

Example:

RECONCILE_TRANSACTION_STATE
        │
        ├── state = CONTRADICTORY
        │       ↓
        │   ESCALATE
        │
        └── state = RESOLVED
                ↓
            EXPLAIN

Conditions must be evaluated from governed state.

They must not depend solely on Model-generated assumptions.

Where a condition depends on enterprise state, the state used for the decision must be sufficiently fresh and sourced from the authoritative system applicable to that fact.

⸻

26. Parallel Actions

Independent Actions may execute in parallel where their contracts permit it.

Example:

                ┌── QUERY_SWITCH_STATUS ──┐
                │                         │
RECONCILE ──────┼── QUERY_SETTLEMENT ─────┼──→ RECONCILE
                │                         │
                └── LOOKUP_TRANSACTION ───┘

Parallelism must not weaken:

* dependency requirements
* authority checks
* target binding
* policy checks
* constraint evaluation
* idempotency
* evidence requirements
* verification

The POC’s canonical graph explicitly queries ledger, switch, and settlement sources in parallel before reconciliation. NOEMA POC Specification PDF.pdf

⸻

27. Expected Outcome

An Action should identify what successful execution is expected to produce.

Example:

Action:
CREATE_ESCALATION_TICKET
Expected Outcome:
Escalation ticket exists in authoritative escalation system

The expected Outcome is not evidence that the Outcome occurred.

It is the criterion against which verification is performed.

Therefore:

Expected Outcome
        ↓
Execution
        ↓
Observed State
        ↓
Verification
        ↓
Actual Outcome

⸻

28. Verification Strategy

An Action that can produce a consequential side effect should have a defined verification strategy.

Example:

Action:
CREATE_ESCALATION_TICKET
Verification:
Re-query escalation system using case correlation key.

For a state-changing operation:

Action
  ↓
Execution
  ↓
Fresh read from authoritative source
  ↓
Compare observed state
  ↓
Verified / Mismatch / Unknown

A transport-level success response is not sufficient proof of business success.

Noema’s execution architecture explicitly requires post-execution verification against actual enterprise state. NOEMA POC Specification PDF.pdf

⸻

29. Unknown Execution Outcome

An Action may enter an execution state where the system cannot determine whether its effect occurred.

Example:

Action
  ↓
Execution
  ↓
Timeout
  ↓
EXECUTION_OUTCOME_UNKNOWN

This must not be converted automatically into:

FAILED

or:

RETRY

The required next step is a fresh verification read.

Conceptually:

EXECUTION_OUTCOME_UNKNOWN
          ↓
Fresh verification
     ┌────┼────┐
     ↓    ↓    ↓
 EFFECT  NONE  UNKNOWN

The POC explicitly prohibits blind retry after uncertain execution. NOEMA POC Specification PDF.pdf

⸻

30. Idempotency

Idempotency is part of Action execution semantics.

An Action contract should establish whether the operation is:

NATURALLY_IDEMPOTENT
EXPLICITLY_IDEMPOTENT
NON_IDEMPOTENT
UNKNOWN

For retryable Actions, Noema must know how duplicate execution is prevented or detected.

The execution layer uses:

* client-generated idempotency keys
* unique execution_attempt_id
* row-level locking where applicable
* bounded retry budgets
* verification before retry
* duplicate webhook deduplication
* duplicate submission deduplication

These controls are part of safe execution, not optional implementation details. NOEMA POC Specification PDF.pdf

⸻

31. Reversibility and Compensation

An Action should identify whether its effects are:

Reversible

The effect can be reliably undone.

Compensatable

The original operation cannot be directly undone, but a separate compensating operation can restore the intended business condition.

Irreversible

The effect cannot reliably be undone.

This property influences:

* risk
* authorization
* approval
* recovery
* verification
* retry behavior

A compensating Action is itself a separate Action.

It must not be confused with simply declaring the original Action reversible.

⸻

32. Action Provenance

Every consequential Action must have structured provenance.

Provenance should answer:

Why does this Action exist?

Relevant provenance may include:

Actor expression
      ↓
Intent
      ↓
Context
      ↓
Evidence
      ↓
State reconstruction
      ↓
Trust decision
      ↓
Action selection

The record should not depend on hidden Model reasoning.

The POC audit requirement is causal: it must establish what was intended, what was ambiguous, how it was resolved, what authority existed, which policy version applied, what state was observed, what evidence supported the decision, why the Action was allowed/blocked/escalated, what was executed, and what final state was verified. NOEMA POC Specification PDF.pdf

⸻

33. Action Selection Provenance

For each material Action, Noema should be able to answer:

* Why this Action?
* Why this Capability?
* Why these parameters?
* Why this target?
* Why now?
* Why was it permitted?
* Which evidence supported it?
* Which policy version governed it?
* Which authoritative state supported the decision?

A statement such as:

“The model selected this tool.”

is insufficient provenance.

The model’s proposal is evidence about what the Model proposed, not authoritative evidence that the Action was correct or permitted.

The provenance record should identify the source and status of material facts used in Action selection.

⸻

34. Action and Enterprise State

Actions operate against enterprise reality.

The enterprise system remains authoritative for business state.

For example:

Action:
CREATE_ESCALATION_TICKET
Enterprise:
Escalation System

Noema may record:

* Action
* Execution Attempt
* Verification
* Outcome
* Audit

But Noema does not become the owner of the underlying enterprise state merely because it initiated the operation.

This preserves the distinction between:

Noema execution state

and:

Enterprise business state

Where multiple enterprise systems expose the same business fact, the applicable system of record and reconciliation precedence must govern which source is authoritative.

For the POC, ledger is authoritative for money movement, switch/processor logs are authoritative for interbank routing, and the application transaction table may be stale and must not override those sources. NOEMA POC Specification_1.pdf

⸻

35. Action and State Reconstruction

Some Actions depend upon reconstructed state.

Example:

User:
"Should I send the money again?"
Intent:
Determine whether another transfer is appropriate.
Required Actions:
├── LOOKUP_TRANSACTION
├── LOOKUP_TRANSACTION_HISTORY
├── QUERY_SWITCH_STATUS
├── QUERY_SETTLEMENT_STATUS
└── RECONCILE_TRANSACTION_STATE

The system must establish the actual transaction state before allowing a consequential next step.

This is why Action selection cannot be separated from Context, State Reconstruction, Trust, and Verification.

A state-dependent Action must carry or reference the state evidence required to establish that its preconditions, constraints, and authorization remain valid.

Stale state is not equivalent to current state. The POC requires stale facts to remain explicitly marked rather than silently treated as current. NOEMA POC Specification_1.pdf

⸻

36. Action and Trust

Trust does not mean:

This Intent looks trustworthy.

Trust evaluates whether a proposed consequence is allowed given:

* resolved Intent
* Actor
* authority
* policy
* enterprise state
* ambiguity
* evidence
* risk
* Action
* Capability
* constraints
* target binding

Conceptually:

Resolved Intent
      ↓
Resolved Target / State
      ↓
Candidate Action
      ↓
Trust Evaluation
      ↓
ALLOW / CLARIFY / CONFIRM / WAIT /
ESCALATE / REJECT / UNKNOWN
      ↓
Planner
      ↓
Execution

The Trust Engine is deterministic and evaluates the exact resolved action, including identity, authority, authorization, policy, current reconstructed state, evidence, ambiguity, action risk, confirmation, enterprise constraints, policy version, and regulatory constraints. NOEMA POC Specification_1.pdf

An Action therefore cannot be considered governed merely because its Capability is valid.

⸻

37. Action and Confirmation

Some Actions may require explicit Actor confirmation even when they are otherwise understood and potentially permitted.

This must remain distinct from semantic resolution.

Example:

Intent:
Create escalation for my disputed transfer.
Resolution:
Resolved
Trust:
CONFIRM
Action:
CREATE_ESCALATION_TICKET

Confirmation is therefore a governance/execution condition.

It does not mean the Intent was ambiguous.

⸻

38. Action and Failure

Action failure must be classified explicitly.

Potential execution conditions include:

REJECTED
FAILED
TIMEOUT
EXECUTION_OUTCOME_UNKNOWN
PARTIAL
DUPLICATE
DEPENDENCY_UNAVAILABLE
POLICY_BLOCKED
AUTHORIZATION_FAILURE
CONSTRAINT_VIOLATION
VERIFICATION_MISMATCH

These states must not be collapsed into a generic:

FAILED

because recovery depends on the actual failure class.

The POC adversarial catalogue explicitly covers timeout, silent 200, duplicate submission, missing response, duplicate/reordered webhook, dependency failure, authorization failure, policy conflict, stale state, contradictory state, and recovery scenarios. NOEMA POC Specification MD.md

⸻

39. Action Recovery

Recovery is not a property of the Model.

It is defined by the Action’s execution semantics and the relevant recovery policy.

Example:

Action:
CREATE_ESCALATION_TICKET
Result:
TIMEOUT
Recovery:
Re-query escalation system
        ↓
Ticket exists?
   ├── yes → verify
   └── no  → determine whether retry is permitted

The system must never blindly repeat a side-effecting Action after an uncertain result.

Recovery must re-establish the relevant target, state, authorization, constraints, and execution conditions where those facts may have changed.

The POC recovery playbook explicitly requires re-querying the source of truth before assuming a timed-out escalation submission failed. NOEMA POC Specification PDF.pdf

⸻

40. Consumer-Side Execution Boundary

The Action object should be safe to transport between systems without granting execution authority merely by possession of the object.

Conceptually:

Action Producer
      ↓
Typed Action
      ↓
Consumer / Execution Boundary
      ↓
Validate contract
      ↓
Bind target
      ↓
Check registry
      ↓
Check authority / policy / preconditions / constraints
      ↓
Revalidate material current state
      ↓
Execute

Possessing or transmitting an Action does not itself authorize execution.

This is important for Noema’s broader architecture, including the case where an external enterprise agent proposes a consequential Action and Noema acts as the independent trust boundary.

In that model:

External Agent
      ↓
Proposed Action
      ↓
Noema
      ↓
Resolve target / state / policy / authority
      ↓
Trust Decision
      ↓
Bounded execution
      ↓
Verification
      ↓
Signed decision/execution record

The downstream trust-boundary mode is explicitly part of Noema’s long-term architecture, while the POC builds only the full-stack Mode 1 path. NOEMA POC Specification HTML.html

⸻

41. Action and Security

Actions must be resilient against hostile or malformed inputs.

The Action boundary must prevent:

* arbitrary tool invocation
* free-form API construction
* parameter injection
* capability escalation
* privilege escalation
* prompt injection through enterprise data
* execution of nonexistent resources
* execution against unauthorized resources
* bypass of confirmation
* bypass of prohibited capability rules
* substitution of untrusted data for authoritative governance data
* target confusion between authorized and unauthorized resources

The POC explicitly tests prompt injection embedded in enterprise fields, confirmation-bypass attempts, out-of-registry capability calls, unauthorized targets, and confused-deputy cases. NOEMA POC Specification MD.md

The security invariant is:

Untrusted proposal
       ↓
Validation
       ↓
Authoritative resolution
       ↓
Deterministic governance
       ↓
Bounded execution

not:

Untrusted proposal
       ↓
trusted because Noema ingested it

⸻

42. Action and Audit

Every consequential Action should generate sufficient audit evidence to reconstruct:

WHO
WHAT INTENT
WHAT ACTION
WHAT CAPABILITY
WHAT TARGET
WHAT PARAMETERS
WHAT AUTHORITY
WHAT POLICY
WHAT CONSTRAINTS
WHAT EVIDENCE
WHAT STATE
WHAT STATE SOURCE
WHAT EXECUTION ATTEMPT
WHAT DOWNSTREAM RESULT
WHAT WAS VERIFIED
WHAT OUTCOME RESULTED

Audit must be causal rather than merely operational logging.

A record such as:

agent called API

is not sufficient.

The POC requires complete causal reconstruction from the audit store alone. NOEMA POC Specification PDF.pdf

⸻

43. Action Lifecycle

The Action lifecycle should not be confused with the Execution Attempt lifecycle.

A conceptual Action lifecycle is:

PROPOSED
   ↓
VALIDATED
   ↓
PLANNED
   ↓
GOVERNED
   ↓
READY

Execution then creates a separate:

ExecutionAttempt
   ↓
STARTED
   ↓
EXECUTING
   ├── COMPLETED
   ├── FAILED
   ├── TIMEOUT
   ├── PARTIAL
   └── EXECUTION_OUTCOME_UNKNOWN

Governance decisions such as:

ALLOW
CLARIFY
CONFIRM
WAIT
ESCALATE
REJECT
UNKNOWN

belong to the Trust Decision model.

Business-state transitions belong to the relevant enterprise system.

Action lifecycle state must not be used as a substitute for enterprise business state.

⸻

44. Action Does Not Own Business State

Noema owns:

* Intent state
* Action state
* execution state
* Trust decisions
* verification records
* audit records

The enterprise system owns:

* accounts
* transactions
* balances
* settlement
* customer records
* operational cases
* other domain business state

Therefore:

Action:
CREATE_ESCALATION_TICKET

does not mean:

Case:
CREATED

until the authoritative system confirms the resulting state.

⸻

45. Action and Verification

The Action contract should define how success can be proven.

A successful HTTP response is not necessarily sufficient.

For example:

HTTP 200
    ↓
does not automatically mean
    ↓
business effect occurred

The system must distinguish:

Transport Success

from:

Business Success

and verify the latter against authoritative state.

This distinction is central to Noema’s execution model. NOEMA POC Specification PDF.pdf

⸻

46. Action and Determinism

Noema’s deterministic boundary does not require every Action proposal to originate deterministically.

The Model may generate a probabilistic proposal.

The commitment to an executable Action must be governed deterministically.

Conceptually:

Probabilistic
    │
    ▼
Candidate Action
    │
    ▼
Schema Validation
    │
    ▼
Target / Parameter Validation
    │
    ▼
Capability Validation
    │
    ▼
Trust / Policy / Authority
    │
    ▼
Constraint / Precondition Validation
    │
    ▼
Canonical Governed Action
    │
    ▼
Execution

The Model proposes.

Noema commits.

The Execution Controller performs.

The enterprise system establishes the resulting business state.

⸻

47. Action Invariants

Invariant 1

An Action is an operation, not a human utterance.

Invariant 2

An Action is not an Intent.

Invariant 3

An Action is not a Capability.

Invariant 4

An Action is not an Execution Attempt.

Invariant 5

An Action is not an Outcome.

Invariant 6

Every executable Action must reference a registered Capability.

Invariant 7

The Model must never construct an arbitrary executable call.

Invariant 8

Action parameters must conform to the Action/Capability contract.

Invariant 9

Materially ambiguous targets or parameters must not be guessed.

Invariant 10

Capability does not imply Authority.

Invariant 11

Authority does not imply Policy approval.

Invariant 12

Trust decisions must remain separate from Action identity.

Invariant 13

Constraints must survive from Intent through Action planning and execution.

Invariant 14

Expected Outcome must remain distinct from observed Outcome.

Invariant 15

An execution attempt must not be reported as successful without appropriate verification.

Invariant 16

An unknown execution result must not be converted into failure or retry without verification.

Invariant 17

Side-effecting Actions must have explicit execution semantics.

Invariant 18

Retry behavior must respect the Action’s idempotency semantics.

Invariant 19

Every consequential Action must have sufficient provenance to explain why it exists and why it was permitted.

Invariant 20

Noema must not silently transform an Actor’s requested Action into a different Action merely to satisfy policy, capability, or implementation convenience.

Invariant 21

Enterprise business state remains authoritative to the relevant enterprise system.

Invariant 22

Prohibited capabilities must be explicitly blocked at the execution boundary.

Invariant 23

Authorization must bind to the specific resolved Action target, not merely to the Capability or Action type.

Invariant 24

A materially stale governance decision must not be treated as indefinitely executable when execution-critical state may have changed.

Invariant 25

Material execution constraints must be re-evaluated at the execution boundary when their applicability or satisfaction may have changed.

Invariant 26

Model-generated, retrieved, or tool-provided content must not become authoritative merely through ingestion.

Invariant 27

Material enterprise-state dependencies must use the applicable authoritative system of record and preserve freshness/status.

Invariant 28

Policy and authorization versions governing a consequential Action must be preserved with the governance record.

Invariant 29

Possession or transmission of an Action must never itself constitute execution authority.

Invariant 30

A target that is unresolved, unauthorized, or materially ambiguous cannot become executable through Capability validity alone.

⸻

48. Canonical Action Representation

Conceptually:

Action {
    id: ActionID
    intent:
        IntentID
    type:
        CanonicalActionType
    capability:
        CapabilityID
    capability_version:
        Version
    target:
        ResolvedTarget
    parameters:
        TypedParameters
    context:
        ActionContext
    constraints:
        Constraint[]
    preconditions:
        Precondition[]
    authority_requirements:
        AuthorityRequirement[]
    policy_requirements:
        PolicyRequirement[]
    expected_outcome:
        ExpectedOutcome
    verification:
        VerificationStrategy
    side_effects:
        SideEffect[]
    risk:
        RiskClassification
    reversibility:
        Reversibility
    idempotency:
        IdempotencySemantics
    provenance:
        Provenance
    status:
        ActionStatus
}

ResolvedTarget is intentionally distinct from an arbitrary identifier supplied by the Model.

Where target resolution is material, the Action must retain sufficient binding/provenance to establish:

Actor
   +
Resolved Intent
   +
Resolved Target
   +
Action
   +
Capability

as the governed unit.

This is the structural control against target confusion and confused-deputy execution.

This is an ontology-level representation.

It is not the final serialization format.

The executable schema belongs in the Action Contract.

⸻

49. Action Contract Boundary

The ontology defines:

what an Action means.

The Action Contract defines:

exactly what an execution system may accept.

Therefore:

ontology/action.md
        ↓
Semantic definition
contracts/action-contract.md
        ↓
Machine-enforceable contract
capability registry
        ↓
Allowed operation set
execution controller
        ↓
Actual invocation

These layers must remain separate.

The Action Contract does not replace:

* Capability Registry
* Trust Decision
* Authority evaluation
* Policy evaluation
* Constraint evaluation
* enterprise state
* verification

It provides the machine-enforceable shape through which those controls operate.

⸻

50. Relationship to Other Canonical Domains

Action depends on and interacts with:

Intent
Context
Entity
Resource
Capability
Authority
Policy
Constraint
Trust
Outcome
State
Provenance
Execution
Verification
Recovery

The relationships are:

Intent
   ↓
Action Graph
   ↓
Action
   ↓
Capability
   ↓
Execution
   ↓
Observed State
   ↓
Verification
   ↓
Outcome

Governance crosses the path:

Actor
   ↓
Authority
   ↓
Policy
   ↓
Constraint
   ↓
Trust
   ↓
Permission to execute

Target binding crosses the governance boundary:

Intent
   ↓
Target Resolution
   ↓
Action + Target
   ↓
Authority / Policy / Constraint
   ↓
Trust
   ↓
Execution

Evidence and provenance cross the entire path:

Input
 ↓
Intent
 ↓
Resolution
 ↓
Trust
 ↓
Action
 ↓
Execution
 ↓
Verification
 ↓
Outcome

Authoritative enterprise state anchors the path wherever business-state facts are material.

⸻

51. Canonical Noema Action Model

The shortest canonical formulation is:

An Action is a typed, bounded, declarative operation instance that advances a resolved Intent through a registered Capability under explicit parameters, target binding, preconditions, constraints, authority, policy, and execution semantics.

The critical distinctions are:

INTENT
What does the Actor want?
ACTION
What bounded operation can advance it?
CAPABILITY
What registered ability can perform that operation?
TARGET
Which specific Entity or Resource is the Action about?
AUTHORITY
Who may cause this Action against this target?
POLICY
Under what governing rules may it proceed?
CONSTRAINT
What boundaries must the Action satisfy?
CONTRACT
What exact typed terms govern the operation?
EXECUTION ATTEMPT
What attempt was actually made?
VERIFICATION
Did the expected effect actually occur?
OUTCOME
What is established to have happened?

The resulting Noema boundary is:

              HUMAN / AGENT
                    │
                    ▼
                 INTENT
                    │
                    ▼
             ACTION GRAPH
                    │
                    ▼
              TYPED ACTION
                    │
              ┌─────┴─────┐
              │           │
              ▼           ▼
        TARGET BINDING   PROVENANCE
              │
              ▼
       TRUST / GOVERNANCE
       ┌──────┼─────────┐
       │      │         │
   AUTHORITY POLICY CONSTRAINT
       │      │         │
       └──────┼─────────┘
              ▼
          CAPABILITY
              │
              ▼
       EXECUTION GATE
              │
              ▼
          EXECUTION
              │
              ▼
    AUTHORITATIVE STATE
              │
              ▼
         VERIFICATION
              │
              ▼
           OUTCOME
              │
              ▼
            AUDIT

The core architectural boundary is:

The Model proposes; Noema validates and governs; the Action remains typed, bounded, and target-bound; the registered Capability defines what may be performed; the Execution Controller enforces the execution boundary; authoritative enterprise state determines what actually happened; Verification establishes the business effect; and Audit preserves the causal chain.

A valid Action is therefore not merely a valid Capability invocation. It is a governed operation whose specific target, parameters, constraints, authority, policy, relevant current state, and provenance have been established sufficiently for the applicable execution boundary.