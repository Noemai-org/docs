> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

ADR-012 — Provenance and Auditability

Status: Accepted
Version: 0.1
Date: 2026-09-19
Decision Type: Foundational
Domain: Architecture / Trust
Canonical Path: decisions/ADRs/ADR-012-provenance-and-auditability.md

⸻

1. Decision

Noema will treat provenance and auditability as first-class architectural requirements.

Every material Noema decision and lifecycle transition must be reconstructible from explicit records of:

* what Intent was being processed
* which Intent version was evaluated
* what context was available
* what evidence was considered
* which rules and policies were applied
* which authorization conditions were evaluated
* which capabilities were selected
* which Trust evaluation produced the decision
* which Execution Contract governed execution
* what execution occurred
* what outcome was observed
* which human interventions occurred
* when each material event occurred

Noema must be able to explain what it did and why it was permitted to do it without depending on hidden model reasoning.

⸻

2. Context

Noema operates at the boundary between probabilistic interpretation and consequential execution.

A typical lifecycle may involve:

Human Expression
      ↓
Interpretation
      ↓
Intent Resolution
      ↓
Validation
      ↓
Trust Evaluation
      ↓
Action Selection
      ↓
Execution Contract
      ↓
Execution
      ↓
Outcome

Each stage may involve different inputs, systems, rules, and state transitions.

Without provenance, Noema may be able to report only the final result:

Action completed.

That is insufficient for a system whose purpose includes establishing whether an action was understood, authorized, trusted, and correctly executed.

Noema therefore requires a reconstructible history of material decisions.

⸻

3. Problem

A consequential action may later require answers to questions such as:

* What did the Actor actually intend?
* Which Intent representation was used?
* What information was available at the time?
* Which external systems supplied relevant evidence?
* Was the evidence current?
* Which authorization applied?
* Which policy version was evaluated?
* Why was the Intent READY?
* Why was clarification requested?
* Why was execution blocked?
* Which Action Contract was selected?
* Which capability was invoked?
* Which execution consumer accepted the contract?
* What happened during execution?
* What outcome was returned?
* Did the system require human intervention?
* What changed between evaluation and execution?

These questions cannot reliably be answered from application logs, model transcripts, or final business-system state alone.

⸻

4. Decision Drivers

The decision is driven by the following requirements:

4.1 Deterministic Trust

Trust decisions must be explainable in terms of explicit conditions rather than model confidence.

4.2 State Transition Determinism

Trust and lifecycle transitions must have identifiable causes.

4.3 Execution Accountability

Noema must be able to establish what execution it authorized and what actually occurred.

4.4 Reproducibility

Historical decisions should be reconstructible using the relevant Intent, evidence, rules, and versions.

4.5 Separation of Authority

Noema must distinguish its own decisions from authoritative facts supplied by external systems.

4.6 Human Oversight

Human approvals, confirmations, clarifications, and interventions must be represented as explicit events.

4.7 Operational Debugging

Failures must be diagnosable without relying on informal reconstruction from unrelated logs.

⸻

5. What Provenance Means in Noema

For Noema, provenance means maintaining the relationship between a material decision and the information, rules, state, and events that produced it.

Conceptually:

Decision
   │
   ├── Intent
   ├── Context
   ├── Evidence
   ├── Rules
   ├── Authorization
   ├── Policy
   ├── Capability
   ├── Constraints
   ├── Evaluation
   └── Event

Provenance does not mean storing every internal model operation.

It means retaining the information necessary to establish the basis of consequential system decisions.

⸻

6. What Auditability Means in Noema

Auditability means that a material Noema lifecycle can be reconstructed after the fact.

For example:

T0
Intent created
T1
Intent resolved
T2
Validation completed
T3
Trust evaluation performed
T4
WAITING_FOR_APPROVAL
T5
Approval received
T6
Trust re-evaluated
T7
READY
T8
Execution Contract created
T9
Consumer accepted Contract
T10
Execution started
T11
Execution completed
T12
Outcome recorded

The system should preserve sufficient records to establish this sequence.

⸻

7. Provenance Is Not Chain-of-Thought

Noema does not require storage or exposure of private model chain-of-thought.

The canonical requirement is decision provenance, not unrestricted reasoning traces.

Noema should record:

Decision:
READY
Basis:
- Intent resolved
- Validation valid
- Authorization satisfied
- Policy satisfied
- Required approval received
- Capability available
- Required evidence fresh
- Constraints satisfied

It does not need to record hidden internal reasoning such as:

private model reasoning...

The distinction is foundational.

⸻

8. Material Events Must Be Recorded

A material event is an event that can affect:

* Intent meaning
* Intent state
* Validation state
* Trust state
* authorization
* policy applicability
* capability availability
* execution eligibility
* execution state
* outcome
* human intervention

Examples include:

intent.created
intent.updated
intent.resolved
intent.clarification_requested
intent.clarification_received
validation.completed
validation.invalid
validation.incomplete
evidence.added
evidence.expired
authorization.granted
authorization.revoked
approval.requested
approval.received
approval.revoked
approval.expired
policy.changed
trust.evaluated
trust.state_changed
trust.expired
trust.invalidated
action.selected
execution.contract_created
execution.accepted
execution.started
execution.completed
execution.failed
outcome.recorded
human.intervention_requested
human.intervention_received

The exact event vocabulary may evolve, but the requirement for material event provenance is canonical.

⸻

9. Trust Decision Provenance

Every material Trust decision should identify its basis.

Conceptually:

TrustEvaluation {
    evaluation_id
    intent_id
    intent_version
    timestamp
    validation_result
    evidence_references
    authorization_result
    policy_references
    capability_result
    constraint_result
    context_references
    risk_result
    resulting_state
    reason
}

The exact schema belongs to the relevant Trust specifications.

The architectural requirement is that the decision be traceable.

⸻

10. State Transition Provenance

Every significant state transition should record:

previous_state
event
new_state
timestamp
intent_version
evaluation_id
reason
relevant_evidence

For example:

Previous:
WAITING_FOR_APPROVAL
Event:
approval.received
New:
EVALUATING
Intent Version:
v7
Evaluation:
eval_184
Reason:
Required approval established.

The resulting transition may subsequently produce:

READY

only after deterministic re-evaluation.

⸻

11. Validation Provenance

Validation results must be traceable to the rules and inputs that produced them.

Conceptually:

ValidationRecord {
    validation_id
    intent_id
    intent_version
    rule_id
    rule_version
    inputs
    evidence
    result
    timestamp
}

Example:

Rule:
TRANSFER_AMOUNT_POSITIVE
Rule Version:
3
Input:
amount = -500
Result:
INVALID

This allows historical validation decisions to be reconstructed even after validation rules evolve.

⸻

12. Rule and Policy Versioning

A historical decision cannot be reconstructed reliably if Noema knows only that a rule existed but not which version was applied.

Therefore material evaluations should identify applicable versions of:

* validation rules
* Trust rules
* policies
* authorization rules where versioned
* Action Contracts
* capability definitions where versioned
* relevant schemas

Conceptually:

Decision
    ↓
Rule Version
    ↓
Policy Version
    ↓
Contract Version

This is required for historical interpretability.

⸻

13. Evidence Provenance

Evidence used in a material decision should be referenceable.

The provenance record should establish, where applicable:

* evidence identity
* source
* retrieval time
* effective time
* freshness
* version
* relationship to the evaluated condition

For example:

Evidence:
customer_123
Source:
Customer Registry
Retrieved:
2026-09-19T10:14:00Z
Condition:
customer exists
Result:
satisfied

Noema should distinguish between evidence it owns and authoritative evidence supplied by another system.

⸻

14. External Authority

External systems may remain authoritative for business facts.

For example:

Payment System
    ↓
payment status = SETTLED

Noema may record that fact as evidence.

It must not represent itself as the authoritative owner of the payment state merely because it consumed or recorded the information.

Provenance should therefore preserve the distinction between:

Source:
Payment System
Noema Decision:
Intent eligible for refund

⸻

15. Authorization Provenance

When authorization materially affects Trust, the authorization basis should be traceable.

Conceptually:

Actor
   ↓
Authorization Source
   ↓
Authorization Result
   ↓
Trust Evaluation

The record should establish:

* Actor
* requested Action
* relevant Resource
* authorization source
* authorization result
* time of evaluation
* applicable authorization version or policy where available

Authorization must not be inferred merely from the fact that an Action was technically executable.

⸻

16. Approval Provenance

Human approval is evidence and must therefore be represented explicitly.

An approval record should establish, where applicable:

approver
intent
action
approval scope
timestamp
approval status
expiration
approval policy

The system should be able to distinguish:

approval requested
approval pending
approval granted
approval revoked
approval expired

An approval should not be represented merely as conversational text.

⸻

17. Clarification Provenance

Clarification is a material Intent lifecycle event.

Noema should retain the relationship between:

Ambiguity
   ↓
Clarification Request
   ↓
Actor Response
   ↓
Updated Intent
   ↓
Re-evaluation

For example:

Question:
Which John do you mean?
Response:
John Smith in Finance.
Resulting Intent:
recipient = customer_742

The provenance should establish how the canonical Intent changed as a consequence of clarification.

⸻

18. Execution Contract Provenance

Every consequential execution should be traceable to the Execution Contract that authorized it.

Conceptually:

Trusted Intent
      ↓
Action Selection
      ↓
Execution Contract
      ↓
Consumer Acceptance
      ↓
Execution

The provenance chain should identify:

* Intent
* Action
* contract
* contract version
* required capability
* authorization basis
* relevant preconditions
* consumer
* execution identifier

Noema should never rely on an untraceable model-generated instruction as the basis for execution.

⸻

19. Execution Provenance

The execution record should establish, where applicable:

execution_id
contract_id
intent_id
consumer
start_time
completion_time
execution_status
external_reference
failure_information

The execution record should distinguish:

execution authorized

from:

execution succeeded

Trust does not guarantee business success.

⸻

20. Outcome Provenance

The final outcome must be linked back to the execution that produced it.

Conceptually:

Intent
  ↓
Trust Evaluation
  ↓
Execution Contract
  ↓
Execution
  ↓
Outcome

This allows Noema to distinguish:

READY
+
EXECUTION_FAILED

from:

READY
+
EXECUTION_COMPLETED

and prevents execution outcomes from being incorrectly interpreted as proof that the original Trust decision was valid or invalid.

⸻

21. Human Intervention Provenance

Human intervention must be explicit.

For example:

Trust:
WAITING_FOR_APPROVAL
        ↓
Approval:
received
        ↓
Trust:
EVALUATING
        ↓
Trust:
READY

Similarly:

Execution:
unexpected outcome
        ↓
Human intervention requested
        ↓
Human decision
        ↓
Recovery / termination

The system should preserve the intervention as part of the lifecycle history.

⸻

22. Immutable Historical Record

Material historical records should be protected from silent alteration.

The precise storage mechanism remains an implementation concern.

The architectural requirement is:

A historical Noema decision must not be silently rewritten without the change itself becoming observable.

Corrections should therefore be represented through explicit corrective events or versioned records rather than destructive mutation of historical meaning.

⸻

23. Current State vs Historical Record

Noema must distinguish:

Current State

from:

State History

For example:

Current Trust State:
READY

does not eliminate the need to retain:

UNRESOLVED
→ EVALUATING
→ WAITING_FOR_APPROVAL
→ EVALUATING
→ READY

Current state supports operational behavior.

Historical state supports auditability and reconstruction.

⸻

24. Provenance Graph

The canonical relationship can be represented as:

                 Intent
                   │
          ┌────────┼────────┐
          │        │        │
       Context   Evidence  Actor
          │        │        │
          └────────┼────────┘
                   ▼
               Validation
                   │
                   ▼
             Trust Evaluation
                   │
          ┌────────┼─────────┐
          │        │         │
       Policy  Authorization Capability
          │        │         │
          └────────┼─────────┘
                   ▼
              Trust State
                   │
                   ▼
            Execution Contract
                   │
                   ▼
               Execution
                   │
                   ▼
                Outcome

The provenance model should preserve these relationships.

⸻

25. Provenance and Re-Evaluation

When a Trust decision is re-evaluated, the new evaluation should not overwrite the historical evaluation.

Instead:

Evaluation 1
    ↓
READY
Material Event
    ↓
Evaluation 2
    ↓
BLOCKED

Both evaluations remain part of the historical record.

This is particularly important when:

* authorization changes
* evidence expires
* policy changes
* context changes
* capabilities become unavailable
* Trust expires

⸻

26. Provenance and Intent Versioning

Material Intent changes should produce distinguishable Intent versions.

For example:

Intent v1
recipient = John
clarification
Intent v2
recipient = John Smith

A Trust evaluation must identify which Intent version it evaluated.

This prevents a historical decision from becoming ambiguous after the Intent changes.

⸻

27. Provenance and Determinism

Provenance strengthens deterministic architecture.

A Trust result should conceptually be reconstructible from:

Intent Version
+
Context
+
Evidence
+
Rules
+
Policies
+
Authorization
+
Capabilities
+
Constraints
+
Evaluation Time

Therefore:

Decision
    ↓
Evidence
    ↓
Rules
    ↓
Versions

must be traceable.

⸻

28. Provenance and Failure

Failure records must preserve the distinction between different classes of failure.

Examples:

RESOLUTION_FAILURE
VALIDATION_FAILURE
AUTHORIZATION_FAILURE
POLICY_BLOCK
CAPABILITY_UNAVAILABLE
EXECUTION_FAILURE
PARTIAL_EXECUTION
UNKNOWN_OUTCOME

A generic:

FAILED

record is insufficient where the failure class materially affects recovery or interpretation.

⸻

29. Provenance and Unknown Outcomes

An external system may accept an Action but fail to provide a definitive result.

For example:

Execution submitted
       ↓
network failure
       ↓
result unknown

Noema must not infer:

FAILED

or:

COMPLETED

without sufficient evidence.

The provenance record should preserve the fact that the outcome is unknown.

⸻

30. Provenance and TOCTOU

Consequential execution may involve a time gap:

T1 — Validation
T2 — Trust
T3 — Contract
T4 — Execution
T5 — Outcome

Business state may change between these points.

Provenance should therefore make the relevant timestamps and evidence retrieval times visible.

This allows later analysis of conditions that changed between Trust evaluation and execution.

⸻

31. Privacy and Data Minimization

Auditability does not require indiscriminate retention of all available data.

Noema should retain sufficient information to establish material decisions while respecting applicable privacy, security, and data-retention requirements.

Where possible, provenance should reference authoritative records rather than unnecessarily duplicating sensitive business data.

The canonical requirement is:

Auditable
≠
Store everything

⸻

32. Security of Audit Records

Provenance records themselves may contain sensitive information.

Therefore access to audit records must be controlled.

Auditability must not become an unrestricted data-access mechanism.

The implementation should establish appropriate:

* access control
* integrity protection
* retention policies
* confidentiality controls
* redaction mechanisms where required

The exact security architecture is defined elsewhere.

⸻

33. Provenance Record Structure

A conceptual common record may contain:

ProvenanceRecord {
    record_id
    intent_id
    intent_version
    event_type
    event_timestamp
    previous_state
    resulting_state
    actor
    system
    evaluation_id
    evidence_references
    rule_references
    policy_references
    authorization_references
    capability_references
    contract_reference
    reason
    result
    correlation_id
}

This is illustrative rather than a final schema.

⸻

34. Correlation

Material records belonging to the same lifecycle should be correlatable.

Conceptually:

correlation_id
    │
    ├── Intent
    ├── Validation
    ├── Trust evaluations
    ├── State transitions
    ├── Execution Contract
    ├── Execution
    └── Outcome

This allows an entire Intent lifecycle to be reconstructed across services and external systems.

⸻

35. Noema-Owned vs External Records

Noema should distinguish:

Noema-owned records

Examples:

* Intent versions
* Trust evaluations
* Trust state transitions
* Action selection
* Execution Contracts
* Noema lifecycle events

External authoritative records

Examples:

* payment transaction state
* account balance
* customer record
* identity state
* external execution result

Noema may reference external records without claiming ownership of their authoritative state.

⸻

36. Auditability Does Not Mean Centralized Ownership

Noema does not need to replicate every enterprise system’s audit database.

It needs sufficient references and provenance to reconstruct its own decisions and interactions.

The architecture should therefore favor:

Noema Decision
     ↓
Reference
     ↓
Authoritative External Record

where duplication would create competing sources of truth.

⸻

37. Operational Observability vs Decision Provenance

These concepts are related but distinct.

Operational observability

Answers:

Is the system functioning correctly?

Examples:

* latency
* error rate
* throughput
* service availability

Decision provenance

Answers:

Why did Noema make this decision?

Examples:

* Intent version
* Trust evaluation
* evidence
* policy
* authorization
* state transition

Both are required, but they serve different purposes.

⸻

38. Provenance Must Survive Service Boundaries

Noema may contain multiple components:

Intent Engine
Context Engine
Trust Engine
Execution Planner
Execution Consumer
Outcome Engine

A provenance chain must remain correlatable across these boundaries.

A service boundary must not destroy the ability to reconstruct the lifecycle.

⸻

39. Provenance and Model Versions

Where an AI model materially contributes to Intent interpretation or candidate generation, the system should be able to identify the relevant model or model configuration.

For example:

Model:
<model identifier>
Model Version:
<version>
Prompt / configuration reference:
<reference>

This establishes which probabilistic component contributed to the candidate Intent.

However:

Model Version

does not become:

Trust Authority

The deterministic Trust decision remains separately attributable.

⸻

40. Provenance of Candidate Intent Generation

Where the model produces a candidate Intent:

Human Expression
      ↓
Model Interpretation
      ↓
Candidate Intent

Noema should preserve sufficient provenance to distinguish:

Actor expression

from:

Model interpretation

and:

Canonical resolved Intent

This prevents inferred content from being confused with explicit Actor input.

⸻

41. Provenance of Clarification

A clarification cycle should establish:

Original Intent
      ↓
Ambiguity identified
      ↓
Clarification requested
      ↓
Actor response
      ↓
Updated Intent
      ↓
Validation
      ↓
Trust

This provides an auditable explanation of why the final Intent differs from the original interpretation.

⸻

42. Provenance of Trust Invalidation

If a previously READY Intent becomes invalid:

READY
  ↓
authorization.revoked
  ↓
EVALUATING
  ↓
BLOCKED

the provenance must establish that the authorization change caused the re-evaluation.

Noema should not simply replace:

READY

with:

BLOCKED

without preserving the causal transition.

⸻

43. Provenance and Expiration

When a Trust decision expires:

READY
valid_until = 10:30

and:

10:31

the resulting re-evaluation should preserve:

Cause:
trust.expired

This allows the historical reason for the transition to remain reconstructible.

⸻

44. Provenance and Partial Execution

If a composite Intent permits partial execution, provenance must distinguish each component.

Example:

Intent
 ├── Action A → COMPLETED
 ├── Action B → FAILED
 └── Action C → WAITING

Noema must not collapse these into a single ambiguous outcome.

Partial execution must remain explicit.

⸻

45. Provenance and Recovery

Recovery actions should themselves be auditable.

For example:

Execution failed
      ↓
Recovery initiated
      ↓
Retry authorized
      ↓
Execution retried
      ↓
Outcome recorded

A retry must not erase the history of the original attempt.

⸻

46. Provenance and Idempotency

Where an Action has idempotency semantics, provenance should preserve the relevant execution identity.

For example:

intent_id
+
action_id
+
idempotency_key

This allows Noema and execution consumers to distinguish:

new execution

from:

repeated submission of an existing execution

The exact idempotency contract belongs to execution specifications.

⸻

47. Canonical Audit Principle

The canonical principle is:

If a material Noema decision cannot be reconstructed from recorded state, events, evidence references, and applicable versions, the system is not sufficiently auditable.

This does not require recording every internal computation.

It requires recording the material basis of consequential decisions.

⸻

48. Invariants

Invariant 1

Material Noema decisions must have provenance.

Invariant 2

Material Trust state transitions must have identifiable causes.

Invariant 3

Historical Trust evaluations must not be silently overwritten by later evaluations.

Invariant 4

Intent versions must be distinguishable.

Invariant 5

Material rules and policies must be versionable or otherwise historically identifiable.

Invariant 6

Evidence used for consequential decisions must be referenceable.

Invariant 7

External systems remain authoritative for their business state.

Invariant 8

Human approvals and interventions must be explicit records.

Invariant 9

Execution must be traceable to an Execution Contract.

Invariant 10

Execution outcomes must be traceable to execution attempts.

Invariant 11

Unknown outcomes must not be converted into success or failure without sufficient evidence.

Invariant 12

Audit records must not silently rewrite historical meaning.

Invariant 13

Provenance must not depend on access to private model chain-of-thought.

Invariant 14

Model provenance and Trust authority must remain distinct.

Invariant 15

Provenance must remain correlatable across Noema service boundaries.

⸻

49. Consequences

Positive consequences

This decision provides:

* reconstructible Trust decisions
* explainable state transitions
* stronger operational debugging
* clearer separation between Noema and external authority
* historical reproducibility
* explicit human-intervention records
* improved incident investigation
* stronger governance over consequential execution

Costs

This decision introduces:

* additional storage requirements
* event and record-management complexity
* versioning requirements
* correlation requirements across services
* privacy and retention considerations
* additional implementation overhead

These costs are accepted because provenance is foundational to Noema’s trust and execution model.

⸻

50. Relationship to Other Canonical Concepts

This ADR establishes a dependency relationship with:

Intent
   ↓
Validation
   ↓
Trust
   ↓
Trust State Machine
   ↓
Execution Contract
   ↓
Execution
   ↓
Outcome

It therefore supports the canonical distinctions between:

* Intent state and execution state
* Validation and Trust
* Capability and permission
* probabilistic inference and deterministic authority
* Noema-owned state and external business truth

⸻

51. Canonical Provenance Flow

                 Human Expression
                       │
                       ▼
                Candidate Intent
                       │
                 model provenance
                       │
                       ▼
                 Resolved Intent
                       │
                       ▼
                  Validation
                       │
                validation record
                       │
                       ▼
               Trust Evaluation
                       │
          ┌────────────┼────────────┐
          │            │            │
       Evidence     Policy     Authorization
          │            │            │
          └────────────┼────────────┘
                       ▼
                 Trust Decision
                       │
               state transition
                       │
                       ▼
              Execution Contract
                       │
                       ▼
                   Execution
                       │
                       ▼
                    Outcome

Every material transition in this flow should remain reconstructible.

⸻

52. Final Definition

Provenance and Auditability are the architectural mechanisms by which Noema preserves the evidence, versions, events, decisions, state transitions, contracts, executions, and outcomes necessary to reconstruct material Intent lifecycles and explain why Noema permitted, blocked, delayed, or otherwise acted upon an Intent.

The core invariant is:

Noema must be able to reconstruct the material basis of a consequential decision without relying on hidden model reasoning or retrospective guesswork.