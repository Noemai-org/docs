> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Auditability

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/auditability.md

⸻

1. Definition

Auditability is Noema’s ability to reconstruct, inspect, and verify the complete lifecycle of a consequential Intent—from what was requested and understood, through State Reconciliation, Trust evaluation, execution, verification, and the resulting Outcome—without requiring Noema to own the underlying enterprise business state.

Auditability answers:

What happened?
Why did it happen?
Who or what caused it?
What did Noema know at the time?
What evidence supported the decision?
What state was observed and reconciled?
What was the resulting Outcome?

It is not merely logging.

⸻

2. Purpose

Enterprise systems need to establish more than the fact that an operation occurred.

They need to establish:

Who or what initiated it?
What did they intend?
What did Noema understand?
What Intent version was admitted?
What context was available?
What enterprise observations were available?
How were those observations reconciled?
What Fact Status was established?
What Action was selected?
What Trust decision was made?
Why was that decision made?
Which policies applied?
What evidence supported it?
What was executed?
Which external system performed the operation?
What happened afterward?
What was verified?
What was the final Outcome?

Noema’s auditability model exists to make this journey reconstructable.

⸻

3. Core Principle

Every consequential execution should leave behind enough durable, attributable evidence to reconstruct the execution journey and the decisions that governed it.

The canonical journey is:

Source of Intent
      ↓
Intent
      ↓
Hard Schema Validation / Admission
      ↓
Intent Resolution
      ↓
Enterprise Observations
      ↓
State Reconciliation
      ↓
Facts / Fact Status / Evidence
      ↓
Temporal Context
      ↓
Trust Evaluation
      ↓
Action
      ↓
Execution
      ↓
Enterprise System
      ↓
Verification
      ↓
Outcome
      ↓
Operational Memory / Audit

Auditability must connect these stages without collapsing them into one state model.

⸻

4. Auditability Is Not Logging

Traditional logging answers:

“Something happened at 10:42.”

Auditability answers:

“Actor X initiated Intent Y.
Noema admitted Intent version Z.
The request was resolved to interpretation A.
Enterprise observations B and C were reconciled into facts with defined Fact Status.
Action D was selected under the applicable Action Contract.
Policy P and authorization evidence E were evaluated.
Trust produced EXECUTE.
Execution F began.
Enterprise system Q performed the operation.
The resulting state was subsequently verified.
Outcome R was established.”

Logs may contribute to auditability.

They are not themselves the audit model.

⸻

5. Noema’s Audit Boundary

Noema owns the audit trail of the execution journey.

It does not become the authoritative database for enterprise business state.

Enterprise
├── accounts
├── balances
├── permissions
├── transactions
├── ledgers
└── business records
Noema
├── Intent versions
├── resolution history
├── clarification history
├── context references
├── observations and evidence references
├── State Reconciliation records
├── Fact Status classifications
├── Trust decisions
├── action state
├── execution state
├── execution attempts
├── verification history
├── Noema Outcomes
├── intervention / case state
└── audit / operational records

The distinction is fundamental.

⸻

6. Enterprise State vs Execution Journey

For example, a bank remains authoritative for:

account.balance = $4,250

Noema may record:

At Trust evaluation time:
enterprise reported account.balance = $4,250

Noema does not become the authoritative ledger.

The audit record establishes what Noema observed and relied upon at a particular time.

⸻

7. Domain State, Execution State, and Knowledge State

Auditability must distinguish at least three temporal realities.

Enterprise domain state

What is actually true in the enterprise system of record.

Noema execution-domain state

What Noema owns about its own execution process.

Examples:

intent.status
trust.decision
execution.state
execution.attempt
case.state
intervention.state

Noema knowledge state

What Noema currently knows or has established about enterprise reality.

These states must not be conflated.

For example:

Enterprise domain state:
refund = SUCCEEDED
Noema knowledge state:
refund status = UNKNOWN
Reason:
authoritative verification has not yet been obtained.

What happened, what Noema knew, and what Noema inferred are different audit dimensions.

⸻

8. Observation, Evidence, Fact Status, and Context

Auditability must preserve the distinction between:

Observation
    ↓
Evidence
    ↓
Reconciliation
    ↓
Fact Status
    ↓
Context

An observation is something received or obtained from a source.

Evidence is information that supports or informs a claim.

State Reconciliation evaluates observations against applicable authority, temporal validity, consistency, identity, and other rules.

Fact Status is the deterministic classification of a claim after applicable reconciliation.

Context is the information made available to a particular evaluation or execution.

These concepts must not be treated as interchangeable.

⸻

9. Fact Status

Fact Status is distinct from Evidence.

Canonical Fact Status values are:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

Fact Status represents the system’s classification of a claim under applicable source, authority, temporal, consistency, freshness, and reconciliation rules.

It is not a measure of model confidence.

For example:

Evidence:
provider response received at 10:42
Fact Status:
VERIFIED

or:

Evidence:
two authoritative systems report conflicting states
Fact Status:
CONFLICTED

The audit trail should preserve both the supporting evidence and the resulting Fact Status.

⸻

10. Hard Admission Boundary

External inputs are not authoritative merely because they exist.

The following must be treated as untrusted until they pass the relevant validation and admission boundary:

user input
model output
retrieved enterprise text
external event
tool response
integration payload
external API response

The canonical boundary is:

Untrusted Input
      ↓
Hard Schema Validation / Admission
      ↓
Eligible Canonical Noema Input

Persistence does not create authority.

An unvalidated payload stored in an audit or diagnostic store remains unvalidated data.

⸻

11. Audit of Admission

Where an external input materially contributes to a consequential journey, the audit trail should preserve:

source
source identity
schema/version
validation result
admission time
validation context
mapping/integration version
classification

If the input was rejected, that rejection may itself be consequential and auditable.

⸻

12. Canonicality Is Scoped

“Canonical” does not mean universally authoritative.

Canonicality is scoped to:

claim
domain
field
tenant
resource
time
authority
semantic version

Enterprise Systems of Record remain authoritative for enterprise business state.

Noema may own canonical data within its execution domain, including:

Intent versions
Trust Decisions
execution state
execution attempts
Noema Outcomes
intervention state
case state
audit records
Operational Memory

A Noema audit record referencing an enterprise fact does not make Noema authoritative for that enterprise fact.

⸻

13. Auditability as a Causal Chain

Audit records should establish relationships between events and decisions.

Intent
  │
  ├── admitted_as
  ▼
Intent Version
  │
  ├── resolved_to
  ▼
Resolved Intent
  │
  ├── informed_by
  ▼
Observations / Context
  │
  ├── reconciled_into
  ▼
Facts / Fact Status
  │
  ├── evaluated_by
  ▼
Trust Evaluation
  │
  ├── governed_by
  ├── supported_by
  ├── authorized_by
  ▼
Trust Decision
  │
  ├── permits
  ▼
Action
  │
  ├── executed_as
  ▼
Execution
  │
  ├── invoked
  ▼
Enterprise System
  │
  ├── observed_by
  ▼
Verification
  │
  ├── establishes
  ▼
Outcome

The audit trail should preserve these relationships.

⸻

14. Audit Record

An audit record should establish at minimum:

identity
timestamp
actor
tenant
object
operation
state
decision
source
authority
causal relationship
semantic version

Additional fields depend on the event or object being recorded.

⸻

15. Identity

Every consequential object should have a stable identifier.

Examples:

intent_id
intent_version_id
action_id
trust_evaluation_id
trust_decision_id
execution_id
execution_attempt_id
event_id
observation_id
reconciliation_id
outcome_id

These identifiers allow independent records to be correlated.

⸻

16. Correlation

A complete execution should be traceable through a common correlation chain.

intent_id
    ↓
intent_version_id
    ↓
action_id
    ↓
trust_evaluation_id
    ↓
execution_id
    ↓
execution_attempt_id
    ↓
integration_request_id
    ↓
provider_reference
    ↓
observation_id
    ↓
verification_id
    ↓
outcome_id

Not every journey contains every identifier.

The requirement is that applicable causal relationships remain reconstructable.

⸻

17. Actor Attribution

Auditability must identify the relevant actor.

An actor may be:

human
agent
service
system
administrator
integration
workflow
application

Where an agent acts on behalf of a human, the audit trail should preserve both identities.

initiating_actor
        ↓
delegated_actor
        ↓
Action

Actor identity does not itself establish authorization.

⸻

18. Actor vs Subject vs Resource

The actor causing an operation and the entity affected by the operation may differ.

Example:

Actor:
customer_service_agent
Subject:
customer_123
Resource:
account_456

Auditability must preserve these distinctions.

⸻

19. Intent Audit

Noema should preserve the Intent that initiated a consequential journey.

This may include:

intent_id
intent_version
source
source_reference
actor
timestamp
channel
intent_kind
resolution state
resolved interpretation
clarifications
scope

Where raw user input contains sensitive information, retention and access must follow applicable enterprise policy.

⸻

20. Intent Version Audit

An Intent Object is immutable once admitted to Trust.

If clarification or another material change alters the semantic Intent:

Intent v1
    ↓
supersedes
    ↓
Intent v2

The audit trail must preserve both versions.

Historical records must never silently reinterpret an earlier Intent version as the newer one.

⸻

21. Intent Resolution Audit

When Noema resolves an Intent, the audit trail should establish:

original Intent
candidate interpretation
resolved interpretation
context used
ambiguities encountered
clarifications obtained
resolution outcome
resolution identity

This makes it possible to answer:

What did Noema determine the source of Intent meant?

⸻

22. Clarification History

Clarification is part of the execution journey and must therefore be auditable.

Example:

User:
"Send it to John."
Noema:
"Which John?"
User:
"John Smith in Finance."

The audit trail should preserve that the original Intent was ambiguous and how the ambiguity was resolved.

Clarification must not silently mutate the original Intent.

⸻

23. Resolved Identity

For consequential operations, audit records should preserve the resolved:

actor
action
target
resource
scope
resolution identity

Entity ambiguity must be resolved before consequential execution.

A historical audit record should make it possible to determine exactly which resource or subject the Action referred to.

⸻

24. Model Output

Where a model contributes to Intent interpretation, auditability may preserve relevant model metadata.

Examples:

model identifier
model version
input reference
candidate interpretation
model confidence
timestamp
inference context

The model’s internal reasoning trace is not required to establish auditability.

The canonical semantic result and the deterministic decisions that followed are.

⸻

25. Model Confidence Is Not Fact Status

Model confidence may be recorded as interpretation metadata.

It must not be treated as:

Fact Status
authorization
authority
evidence validity
policy satisfaction
execution permission

For example:

model_confidence:
0.92
resolution:
CLARIFICATION_REQUIRED

The recorded confidence establishes what the model produced.

It does not establish that the underlying claim is true or authorized.

⸻

26. Context Audit

Trust decisions depend on context.

Therefore, auditability should preserve references to the context used during evaluation.

Examples:

actor state
resource state
authorization state
enterprise observations
reconciled facts
temporal facts
environment
historical facts
policy context
integration state

The audit trail does not necessarily need to duplicate the entire source database.

It needs enough information or durable references to establish what was relied upon.

⸻

27. State Reconciliation Audit

State Reconciliation is a first-class part of the audit journey.

The canonical relationship is:

Enterprise Observations
        ↓
State Reconciliation
        ↓
Reconciled Facts / State
        ↓
Fact Status

The audit trail should establish:

which observations were considered
which sources were involved
which authority rules applied
which temporal rules applied
which conflicts existed
what reconciliation produced
what Fact Status resulted
when reconciliation occurred

Temporal recency alone must not be represented as the reason an observation became authoritative.

⸻

28. Evidence Audit

Every consequential Trust decision should be traceable to its supporting evidence.

Trust Decision
      │
      ├── Evidence A
      ├── Evidence B
      ├── Evidence C
      ├── Reconciliation R
      └── Policy P

Evidence should preserve provenance.

⸻

29. Evidence Provenance

Where appropriate, an audit record should identify:

source
source type
timestamp
subject
scope
authority
version
freshness
validity
observation identity

This allows an auditor to determine whether the evidence was appropriate at the time.

Source identity and authority must remain distinct.

A source can provide evidence without being authoritative for every claim.

⸻

30. Evidence Snapshot vs Reference

Noema may preserve either:

evidence snapshot

or:

reference to authoritative evidence

depending on sensitivity, retention, and reproducibility requirements.

The important requirement is:

The historical Trust decision must remain explainable even if the underlying enterprise state subsequently changes.

⸻

31. Policy Audit

A Trust decision must identify the Policy context under which it was made.

Example:

policy:
transfer-limit
version:
7
decision:
REJECT

Policies change.

An audit record must not make a historical decision appear to have been evaluated under today’s policy when it was actually evaluated under an earlier version.

⸻

32. Contract and Graph Version Audit

A consequential decision should preserve the semantic versions that governed it.

Depending on the journey, this may include:

Intent Contract version
Context Contract version
Trust Contract version
Action Contract version
Execution Contract version
Event Contract version
Policy version
Enterprise Action Graph version
Capability Registry version
integration mapping version

The exact applicable versions must remain reconstructable.

⸻

33. Authorization Audit

Authorization should be attributable.

The audit trail should establish:

authorization source
authorization type
authorization result
authorization scope
authorization timestamp
authorization version

Noema should distinguish:

technical authorization
policy authorization
business authorization

Trust does not create enterprise permissions.

The audit trail records what authorization information was relied upon and how it contributed to the decision.

⸻

34. Risk Audit

Where risk contributes materially to a Trust decision, the relevant risk evaluation should be traceable.

For example:

risk:
HIGH
policy:
HIGH risk requires human approval
decision:
ESCALATE

The audit trail should connect these facts.

Risk classification must not be treated as an implicit substitute for deterministic policy evaluation.

⸻

35. Trust Decision Audit

A Trust decision should record:

trust_evaluation_id
trust_decision_id
intent_version
action_id
actor
target
decision
reasons
evidence references
Fact Status references
policy references
authorization result
risk result
Trust Contract version
Action Contract version
Enterprise Action Graph / Capability Registry version
timestamp
validity window
decision context identity

The exact representation belongs to the Trust API and Trust model.

The canonical Trust outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

Revalidation is not a fifth Trust outcome.

⸻

36. Trust EXECUTE Is Not Success

A historical Trust decision of:

EXECUTE

means that the resolved execution path satisfied applicable Trust conditions and was permitted to proceed at that time.

It does not establish that:

execution succeeded
enterprise state changed
postconditions were satisfied
Outcome was achieved

The audit trail must preserve these as separate facts.

⸻

37. Deterministic Decision Reconstruction

For consequential decisions, an auditor should be able to determine:

Inputs
   ↓
Relevant state / evidence
   ↓
Evaluation rules
   ↓
Decision

The goal is not necessarily to reproduce every internal computation.

The goal is to establish that the decision was produced according to the applicable deterministic Trust rules and versions.

⸻

38. No “Because the AI Said So”

This is a core Noema auditability requirement.

An audit record such as:

decision:
EXECUTE
reason:
AI was confident

is insufficient.

Instead:

decision:
EXECUTE
authorization:
valid
policy:
satisfied
risk:
within threshold
preconditions:
satisfied
Fact Status:
VERIFIED
evidence:
fresh and authoritative

The model may contribute to Intent interpretation.

It does not become the authority for execution.

⸻

39. Action Audit

The Action record should establish:

what Action was created
who or what created it
which Intent version produced it
which resources it targets
which Action Contract applies
which version was used
which capability was selected
which graph version permitted its selection

Action selection must remain bounded by the Enterprise Action Graph, Capability Registry, and registered Action Contracts.

⸻

40. Action Mutation

Consequential Actions should not silently mutate after Trust evaluation.

If an Action materially changes:

Original Action
      ↓
Modified Action

the system should establish whether a new Trust evaluation is required.

The audit trail must preserve the relationship between versions.

⸻

41. Planner Audit

A planner may select or propose an Action within the allowed execution space.

Auditability should establish:

planner input
graph version
capability registry version
candidate actions
selected action
selection identity
Trust constraints

Persistence of a plan does not create authority.

A planner cannot:

invent capabilities
invent authority
modify Action Contracts
bypass Trust

The audit trail should make the governing boundaries reconstructable.

⸻

42. Execution Audit

Execution records should establish:

execution_id
action_id
intent_version
trust_evaluation_id
executor
start time
end time
state transitions
attempts
integration calls
failures
retries
human intervention
verification
final execution state

Execution history should be sufficient to reconstruct consequential transitions.

⸻

43. Execution State History

Recording only the final state is insufficient.

For example:

FAILED

does not explain whether the execution:

started
retried
waited
was interrupted
was compensated
became UNKNOWN
was subsequently reconciled

The audit trail should preserve consequential state transitions.

Example:

PENDING
  ↓
RUNNING
  ↓
FAILED
  ↓
RETRYING
  ↓
RUNNING
  ↓
COMPLETED

⸻

44. Retry Audit

Every consequential retry should be attributable.

attempt_1
    ↓
FAILED
    ↓
verification
    ↓
attempt_2
    ↓
COMPLETED

The audit trail should establish why another attempt was permitted.

An UNKNOWN execution must not be blindly retried merely because no success response was received.

⸻

45. Unknown Execution Audit

UNKNOWN is a first-class execution condition.

For example:

request submitted
      ↓
provider timeout
      ↓
execution = UNKNOWN

This does not establish:

success

or:

failure

The audit trail should preserve:

last known state
uncertainty cause
provider reference
verification attempts
reconciliation attempts
subsequent authoritative observation
final classification

Timeout is not automatically failure.

⸻

46. Recovery and Revalidation Audit

Recovery should preserve the distinction between historical execution state and current evaluation.

Canonical recovery path:

Historical Execution State
        ↓
External Operation State
        ↓
Current Authoritative Observation
        ↓
State Reconciliation
        ↓
Revalidate Trust / Preconditions
        ↓
Continue / Clarify / Escalate / Reject

Revalidation is a new evaluation.

It does not mutate the historical Trust decision.

⸻

47. Human Intervention Audit

If a human becomes involved:

Trust:
ESCALATE
       ↓
Human intervention
       ↓
Trust / Execution continues

the audit trail should record:

who intervened
what authority they possessed
what decision they made
when they made it
what object they acted upon
what justification was supplied

Human intervention must not silently erase the automated history.

⸻

48. External Execution Audit

Noema may invoke an external enterprise system.

The audit trail should connect:

Noema Action
      ↓
Integration
      ↓
External request
      ↓
Provider response
      ↓
Observation

Provider-specific identifiers should be retained where appropriate.

⸻

49. External System Authority

The enterprise system remains authoritative for the business result.

For example:

Noema:
execution completed
Enterprise:
transaction_id = txn_123
status = SETTLED

Noema records the relationship.

It does not replace the enterprise transaction ledger.

⸻

50. Outcome Audit

The final Outcome should establish what Noema determined actually happened after execution and verification.

Example:

Expected:
card replaced
Observed:
provider confirms replacement
Outcome:
VERIFIED

The audit trail should distinguish expected outcomes from observed outcomes.

⸻

51. Expected vs Observed

This distinction is critical.

Action Contract:
postcondition = card.status == REPLACED
Execution:
COMPLETED
Verification:
enterprise reports card.status == REPLACED
Outcome:
VERIFIED

Execution completion alone does not prove the postcondition.

⸻

52. Outcome vs Enterprise State

Outcome is not enterprise business state.

Noema may record:

Outcome:
refund request submitted successfully

while the enterprise remains authoritative for:

refund.status
ledger entries
account balance
settlement state

Outcome describes the result established by the Noema journey.

Enterprise state remains enterprise-owned.

⸻

53. Failed Outcomes

An execution may succeed technically while the desired Outcome fails.

Therefore:

Execution:
COMPLETED
Outcome:
FAILED

can be valid.

Auditability must preserve this distinction.

⸻

54. Unknown Outcome

An Outcome may remain:

UNKNOWN

when Noema cannot establish whether the intended result occurred.

For example:

Execution:
UNKNOWN
Enterprise verification:
unavailable
Outcome:
UNKNOWN

Later authoritative reconciliation may establish the actual enterprise state.

The historical UNKNOWN Outcome must not be rewritten as though certainty existed at the earlier time.

⸻

55. Audit Events

Events provide the chronological backbone of the audit trail.

Examples:

intent.created
intent.admitted
intent.clarification_requested
intent.version_created
intent.resolved
observation.received
observation.validated
reconciliation.completed
fact.status_classified
action.created
trust.evaluation_started
trust.decision_recorded
execution.started
execution.failed
execution.unknown
execution.revalidated
execution.retried
execution.completed
verification.started
verification.completed
outcome.recorded
human.intervention

⸻

56. Events Are Historical Records

An event represents something that happened.

Historical events should not be rewritten merely because current state has changed.

Example:

Event:
trust.decision.recorded
Decision:
REJECT
Later:
Policy changes

The historical event remains true.

A later evaluation is a new event.

⸻

57. Append-Oriented Audit History

Consequential audit history should conceptually behave as an append-oriented record.

Event 1
Event 2
Event 3
Event 4
...

Corrections should generally be represented as subsequent events rather than destructive edits.

Historical corrections must preserve lineage.

⸻

58. State vs History

Current state:

execution.state = COMPLETED

History:

PENDING
→ RUNNING
→ FAILED
→ RETRYING
→ RUNNING
→ COMPLETED

Both are valuable.

State tells us where something is.

History tells us how it got there.

⸻

59. Causality

Auditability should preserve causality wherever possible.

For example:

clarification.requested
      ↓
clarification.received
      ↓
intent.version_created
      ↓
intent.resolved
      ↓
action.created

This is more useful than a flat list of unrelated timestamps.

⸻

60. Temporal Accuracy

Audit records should distinguish:

occurred_at
observed_at
received_at
recorded_at
validated_at
reconciled_at
decision_at
execution_started_at
execution_completed_at
verified_at
outcome_at

An external event may have happened at one time and reached Noema later.

These timestamps should not be conflated.

⸻

61. Version Dimensions

Historical reconstruction may depend on several independent version dimensions.

Auditability should distinguish, where applicable:

semantic version
source version
event / transport schema version
contract version
policy version
integration mapping version
Enterprise Action Graph version
Capability Registry version
resource version / concurrency token
model version

It should also preserve relevant temporal dimensions.

A single generic version field is insufficient where these dimensions materially affect interpretation.

⸻

62. Historical Interpretation

Historical reconstruction must use the versions applicable at the historical decision point.

For example:

Intent version:
3
Trust Contract:
0.1
Policy:
7
Action Contract:
4
Graph:
12
Integration mapping:
8

The current versions must not silently replace historical versions during reconstruction.

⸻

63. Replay Semantics

Historical replay must be non-executing by default.

A replay should use:

historical Intent
historical context
historical observations
historical versions
historical policies
historical decisions

Historical replay must not create a new enterprise business occurrence.

Modern re-evaluation is a distinct operation and must be explicitly identified as such.

⸻

64. Replay vs Re-evaluation

These are different operations.

Historical replay

Answers:

“What happened according to the historical execution path?”

Re-evaluation

Answers:

“What would Noema decide using current or explicitly selected rules?”

The latter must not rewrite the former.

⸻

65. Clock and Ordering

Distributed systems may not provide a perfectly ordered global clock.

Therefore auditability should rely on:

timestamps
sequence information
causal identifiers
event identifiers
source timestamps
resource versions

rather than assuming that database insertion order alone represents real-world causality.

⸻

66. Temporal Authority

Recency does not equal authority.

A later observation from a lower-authority source does not automatically supersede an earlier authoritative observation.

Authority itself may be time-scoped.

The audit trail should therefore preserve both:

when the observation was produced

and:

what authority applied to it at that time

⸻

67. Tenant Isolation

Audit data is enterprise data.

A tenant must not be able to inspect another tenant’s execution history.

Tenant A
  ↓
Audit records A only
Tenant B
  ↓
Audit records B only

Cross-tenant access requires explicit authority.

⸻

68. Audit Access Control

Not every user who can see an execution should see every audit detail.

Sensitive information may require additional authorization.

For example:

Operator:
execution state
Auditor:
Trust decision + evidence metadata
Security administrator:
sensitive authorization evidence

Access should be governed by enterprise policy.

Read-only audit access can itself be consequential when it exposes protected information and therefore may require Trust.

⸻

69. Data Minimization

Auditability does not mean storing everything forever.

Noema should preserve what is necessary to establish:

what happened
why it happened
who caused it
what Noema knew
what evidence was used
what decision was made
what outcome occurred

Sensitive or unnecessary payloads should not be retained without a legitimate reason.

⸻

70. Immutability and Integrity

Historical audit records should be tamper-resistant.

For consequential records, the system may provide mechanisms such as:

append-only storage
cryptographic integrity
signed records
hash chains
immutable retention

The specific implementation is not canonical at this stage.

The requirement is historical integrity.

⸻

71. Audit Record Integrity

An auditor must be able to distinguish:

original record

from:

modified
corrected
superseded
or fabricated record

Corrections should preserve the original historical record where applicable and establish their relationship to it.

Integrity mechanisms should be appropriate to the risk of the operation.

⸻

72. Retention

Audit retention should be configurable according to:

enterprise policy
regulatory requirements
data sensitivity
operation criticality
legal requirements

Noema should not assume that every record has the same retention period.

⸻

73. Deletion and Retention Conflicts

Auditability must coexist with privacy and retention requirements.

The canonical requirement is:

Preserve the evidentiary integrity of the execution journey while respecting applicable data-retention and deletion policies.

Implementation must distinguish immutable audit facts from sensitive payloads that may have separate retention requirements.

⸻

74. Auditability and Privacy

Auditability is not permission to expose private data.

The audit model should support:

access control
redaction
field-level protection
data minimization
retention policies
tenant isolation

while preserving the ability to establish consequential facts.

⸻

75. Auditability and Security

Security events may themselves become part of the audit trail.

Examples:

unauthorized access
Trust rejection
policy violation
credential failure
privilege escalation
manual override
prohibited capability request

This creates a broader enterprise security picture around Noema execution.

⸻

76. Manual Overrides

Manual intervention is itself consequential.

If a human overrides or changes an automated path, the audit trail must record:

original decision
override actor
authority
reason
timestamp
new decision/state
object affected

No override should silently erase the automated history that preceded it.

⸻

77. Trust Re-evaluation Audit

Suppose:

Evaluation 1:
EXECUTE

then new evidence arrives:

Evaluation 2:
REJECT

The audit history should show both.

Evaluation 1
      ↓
Context / evidence changed
      ↓
State Reconciliation
      ↓
Evaluation 2

The first decision must not be rewritten.

⸻

78. Auditability and Determinism

Determinism makes auditability substantially stronger.

If the same applicable:

Intent version
Action
policy
evidence
Fact Status
relevant context
Trust Contract

are provided to the deterministic Trust Engine under the same applicable versions, the decision should be reproducible.

This allows the enterprise to distinguish:

deterministic system decision

from:

probabilistic model interpretation

⸻

79. Auditability of Ambiguity

Ambiguity itself is auditable state.

Example:

Intent:
"Send it to John."
State:
AMBIGUOUS
Reason:
multiple matching actors
Trust outcome:
CLARIFY

This demonstrates that Noema did not silently guess.

The clarification and subsequent Intent version should remain linked to the original ambiguity.

⸻

80. Auditability of Non-Execution

Not executing an Action is also an important event.

Examples:

CLARIFY
ESCALATE
REJECT

These outcomes should be auditable just like execution.

A good enterprise audit trail explains both:

what Noema did

and:

what Noema deliberately refused to do

⸻

81. Auditability of “Why Not?”

Enterprise operators frequently need to answer:

Why didn’t this request execute?

The audit trail should support answers such as:

Ambiguous recipient
Authorization unavailable
Policy violation
Risk threshold exceeded
Human approval required
Precondition failed
Capability unavailable
Enterprise state unknown
Conflicting evidence
Execution dependency unavailable

This is a first-class audit requirement.

⸻

82. Audit Queryability

Audit records should be queryable by important dimensions.

Examples:

intent_id
intent_version_id
actor_id
action_id
execution_id
trust_evaluation_id
resource_id
tenant_id
policy_id
decision
state
fact_status
integration
outcome
time range

This enables operational investigation without requiring raw log archaeology.

⸻

83. Audit Views

Different enterprise roles may require different views.

Customer Support
    → execution journey
Security
    → authorization + Trust
Compliance
    → policy + evidence + decisions
Engineering
    → execution + integration failures
Operations
    → current state + history

The underlying audit model remains canonical.

Views do not create separate semantic audit models.

⸻

84. Audit API Relationship

The Interfaces layer may expose audit information through APIs.

However, enterprise/auditability.md defines what must be auditable, not the API mechanics.

The interface boundary is defined separately under the Interfaces domain.

⸻

85. Auditability and Observability

These concepts overlap but are not identical.

Observability

Answers:

Is the system healthy?

Examples:

latency
throughput
error rate
resource usage
queue depth

Auditability

Answers:

What happened in a consequential execution and why?

Examples:

Intent
Trust decision
Action
Execution
Evidence
Outcome

Noema requires both, but they serve different purposes.

⸻

86. Auditability and Debugging

Debugging investigates system behavior.

Auditability establishes a durable historical account of consequential behavior.

A debug log may say:

retrying request

An audit record should establish:

Execution 123 entered RETRYING
because attempt 1 failed with provider timeout.

Debugging information may assist investigation without becoming canonical audit history.

⸻

87. Auditability and Operational Memory

Noema may retain historical information useful for future Intent resolution and operational improvement.

Operational Memory is structured historical execution and case information.

It is not:

generic AI memory
enterprise system of record
current enterprise truth
authorization

Operational Memory may contain or reference audit information, but the concepts remain distinct.

⸻

88. Auditability and Knowledge State

The audit trail should distinguish:

what happened

from:

what Noema knew

and:

what Noema inferred

For example:

Enterprise state:
transaction = SETTLED
Noema knowledge state at 10:42:
UNKNOWN
Noema observation at 10:47:
provider reports SETTLED
Reconciled Fact Status:
VERIFIED

This is essential for reconstructing decisions made under uncertainty.

⸻

89. Auditability of Read-Only Operations

Read-only does not mean non-consequential.

An operation that retrieves protected information may have significant enterprise consequences.

Therefore the audit trail may need to establish:

who requested access
what information was requested
which resources were accessed
what authorization applied
what Trust decision permitted access
what information was disclosed

Noema must not assume that absence of a write means absence of audit requirements.

⸻

90. Auditability and Concurrency

Temporal history alone cannot guarantee concurrency safety.

Where supported, auditability should preserve relevant:

resource version
ETag
concurrency token
transaction identity
idempotency key
reservation / lease identity
conditional operation

This allows auditors to determine whether the execution operated against the expected version of a resource.

⸻

91. TOCTOU Audit

Time-of-check-to-time-of-use conditions should be reconstructable where materially relevant.

For example:

Trust evaluation:
balance = $5,000
Execution:
conditional operation requires balance >= $5,000
Enterprise:
resource version changed

The audit trail should make the temporal relationship visible.

Noema should prefer enterprise atomic conditional operations where supported.

⸻

92. Auditability of Security Boundaries

The model, user input, retrieved text, and tool responses are untrusted inputs.

The model must not have direct enterprise credentials or unrestricted enterprise access.

Auditability should preserve enough information to establish:

source of proposal
validated semantic object
Trust decision
registered capability
Action Contract
executor
enterprise operation

It must not require storing secrets or credentials.

⸻

93. Auditability Does Not Require Chain-of-Thought

Noema’s auditability requirement is causal and semantic.

It does not require storing private model reasoning traces.

The system should instead preserve:

input reference
candidate interpretation
validated Intent
resolved context
evidence
Fact Status
policy
deterministic conditions
Trust decision
Action
Execution
verification
Outcome

This provides explainability without making private model reasoning an audit dependency.

⸻

94. Audit Object Graph

The canonical audit object graph is:

                         INTENT
                           │
                           ▼
                      RESOLUTION
                           │
                           ▼
                  HARD ADMISSION
                           │
                           ▼
                    OBSERVATIONS
                           │
                           ▼
                 STATE RECONCILIATION
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                 EVIDENCE      FACT STATUS
                    │             │
                    └──────┬──────┘
                           ▼
                      CONTEXT
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
        ACTION GRAPH                  CONTRACT
             │                           │
             └─────────────┬─────────────┘
                           ▼
                      TRUST EVAL
                           │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
    AUTHORIZATION       POLICY           RISK
          │               │               │
          └───────────────┼───────────────┘
                          ▼
                       DECISION
                          │
                          ▼
                      EXECUTION
                          │
                          ▼
                     INTEGRATION
                          │
                          ▼
                  ENTERPRISE SYSTEM
                          │
                          ▼
                     VERIFICATION
                          │
                          ▼
                       OUTCOME
                          │
                          ▼
               OPERATIONAL MEMORY

Every significant node and relationship should be auditable.

⸻

95. Minimum Audit Chain

At minimum, a consequential operation should establish:

1. Who or what initiated the Intent.
2. What Intent was received.
3. Whether and how it passed admission.
4. What Intent version was admitted.
5. What Intent was resolved.
6. What actor, Action, target, and resource were resolved.
7. What observations and context were used.
8. What State Reconciliation occurred.
9. What Fact Status resulted.
10. What Action was created.
11. What Trust evaluation occurred.
12. What evidence and policy supported it.
13. What Trust decision resulted.
14. What execution occurred.
15. What external system was involved.
16. What verification occurred.
17. What Outcome resulted.

⸻

96. Canonical Audit Invariants

Invariant 1

Consequential Intent journeys must be reconstructable.

Invariant 2

Historical audit records must not be silently rewritten.

Invariant 3

Every consequential object must have stable identity.

Invariant 4

Intent, Action, Trust, Execution, Verification, and Outcome must remain distinguishable in the audit trail.

Invariant 5

Trust decisions must be traceable to their relevant evidence and policy.

Invariant 6

Model confidence must not be treated as authorization evidence or Fact Status.

Invariant 7

Ambiguity and non-execution must be auditable.

Invariant 8

Execution completion must not be treated as proof of business Outcome.

Invariant 9

Noema must preserve the distinction between its execution record and enterprise business state.

Invariant 10

External system identifiers should be correlated with Noema execution identifiers where appropriate.

Invariant 11

Human intervention must never erase the automated history that preceded it.

Invariant 12

Trust reevaluations must create distinguishable historical evaluations.

Invariant 13

Audit records must preserve sufficient provenance to explain consequential decisions.

Invariant 14

Audit access must respect tenant and authorization boundaries.

Invariant 15

Auditability must not require indiscriminate retention of sensitive data.

Invariant 16

Audit records must have appropriate integrity guarantees.

Invariant 17

The audit model must distinguish event occurrence from event recording time where necessary.

Invariant 18

The audit trail must support investigation of both execution and deliberate non-execution.

Invariant 19

Noema must not claim authoritative ownership of enterprise business records merely because it references them in an audit trail.

Invariant 20

Auditability must remain meaningful even when the underlying enterprise state has subsequently changed.

Invariant 21

Unvalidated external data must not become authoritative merely because it is persisted.

Invariant 22

Hard schema validation and admission must precede canonical use of external inputs.

Invariant 23

Fact Status must remain distinct from Evidence, Context, State, and Outcome.

Invariant 24

State Reconciliation must be a first-class auditable operation.

Invariant 25

Canonicality must always be scoped to the relevant domain, claim, authority, and temporal context.

Invariant 26

Source identity, authority, freshness, and authorization must remain distinct audit dimensions.

Invariant 27

Historical Intent versions admitted to Trust must remain immutable and identifiable.

Invariant 28

Material Intent changes must create a new Intent version linked through supersedes.

Invariant 29

Consequential audit records must preserve the resolved actor, Action, target, resource, scope, and resolution identity where applicable.

Invariant 30

Planner persistence must not create capabilities or authority.

Invariant 31

Action selection must remain traceable to the applicable Enterprise Action Graph, Capability Registry, and Action Contract.

Invariant 32

A Trust decision of EXECUTE must never be interpreted as proof of execution success or business Outcome.

Invariant 33

Outcome must remain distinct from enterprise business state.

Invariant 34

UNKNOWN must remain a first-class auditable condition.

Invariant 35

Timeout must not automatically be classified as execution failure.

Invariant 36

Recovery from UNKNOWN must use verification and State Reconciliation before consequential retry where required.

Invariant 37

Revalidation must create a new evaluation rather than mutate a historical Trust decision.

Invariant 38

Historical replay must be non-executing by default.

Invariant 39

Replaying an event must not create a new enterprise business occurrence.

Invariant 40

Historical corrections must be additive and preserve lineage.

Invariant 41

Operational Memory must not become a substitute for enterprise authority.

Invariant 42

Auditability must distinguish enterprise domain truth, Noema execution state, and Noema knowledge state.

Invariant 43

Model output and historical model metadata must not become authoritative merely because they are retained in the audit trail.

Invariant 44

Read-only access to protected enterprise information may be consequential and therefore auditable.

Invariant 45

Auditability must preserve sufficient temporal and version information to reconstruct the conditions under which a consequential decision was made.

⸻

97. The Enterprise Audit Question

The ultimate test for Noema’s auditability is whether an authorized enterprise operator can reconstruct:

WHO
 ↓
requested WHAT
 ↓
Noema admitted WHICH Intent
 ↓
Noema understood WHAT
 ↓
using WHICH observations and context
 ↓
reconciled into WHICH facts
 ↓
with WHICH Fact Status
 ↓
created WHICH Action
 ↓
evaluated under WHICH policy and contracts
 ↓
using WHICH evidence
 ↓
received WHICH Trust decision
 ↓
executed WHICH operation
 ↓
against WHICH enterprise system
 ↓
verified WHICH result
 ↓
producing WHICH Outcome

If that chain cannot be reconstructed, the system is not sufficiently auditable.

⸻

98. Final Definition

Auditability is the durable, attributable, temporally accurate, and reconstructable record of Noema’s consequential execution journey—from Source of Intent through hard admission, Intent resolution, State Reconciliation, Trust, Action, Execution, Verification, and Outcome—preserving the evidence, Fact Status, policies, actors, versions, state transitions, and causal relationships necessary to explain consequential behavior.

The fundamental distinction is:

Enterprise:
"What is the business state?"
Noema:
"What happened on the execution journey,
what did Noema know at each relevant point,
what evidence and rules governed its decisions,
and why did Noema permit, stop, or escalate that journey?"

Noema should make every consequential decision explainable without becoming the system of record for the enterprise’s underlying business reality.

Auditability therefore establishes a durable causal account of Noema’s execution domain while preserving the enterprise as the authority for enterprise business state.