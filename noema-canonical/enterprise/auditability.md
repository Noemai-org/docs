Auditability

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/auditability.md

⸻

1. Definition

Auditability is Noema’s ability to reconstruct, inspect, and verify the complete lifecycle of a consequential Intent—from what was requested and understood, through Trust evaluation and execution, to the resulting Outcome—without requiring Noema to own the underlying enterprise business state.

Auditability answers:

What happened, why did it happen, who or what caused it, what evidence supported the decision, and what was the resulting outcome?

It is not merely logging.

⸻

2. Purpose

Enterprise systems need to establish more than the fact that an operation occurred.

They need to establish:

Who initiated it?
What did they intend?
What did Noema understand?
What Action was produced?
What context was available?
What Trust decision was made?
Why was that decision made?
Which policies applied?
What evidence supported it?
What was executed?
Which external system performed it?
What happened afterward?
What was the final Outcome?

Noema’s auditability model exists to make this journey reconstructable.

⸻

3. Core Principle

Every consequential execution should leave behind enough durable evidence to reconstruct the execution journey and the decisions that governed it.

The canonical journey is:

Human / Agent
      ↓
Intent
      ↓
Intent Resolution
      ↓
Context
      ↓
Trust Evaluation
      ↓
Action
      ↓
Execution
      ↓
Enterprise System
      ↓
Outcome

Auditability must connect these stages.

⸻

4. Auditability Is Not Logging

Traditional logging answers:

"Something happened at 10:42."

Auditability answers:

"User X requested Y.
Noema resolved the request to Intent Z.
The relevant context was A.
Action B was generated.
Policy P and authorization evidence E were evaluated.
Trust produced EXECUTE.
Execution E began.
Enterprise system Q performed the operation.
The resulting Outcome was R."

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
├── intent state
├── resolution
├── clarification
├── context used
├── trust decisions
├── action state
├── execution state
├── evidence references
└── outcome journey

The distinction is fundamental.

⸻

6. Enterprise State vs Execution Journey

For example, a bank remains authoritative for:

account.balance = $4,250

Noema may record:

"At the time of Trust evaluation, the enterprise reported
the account balance as $4,250."

Noema does not become the authoritative ledger.

⸻

7. Auditability as a Causal Chain

Audit records should establish relationships between events and decisions.

Intent
  │
  ├── resolved_from
  ▼
Executable Intent
  │
  ├── produced
  ▼
Action
  │
  ├── evaluated_by
  ▼
Trust Evaluation
  │
  ├── authorized_by
  ├── governed_by
  ├── supported_by
  ▼
Trust Decision
  │
  ├── permitted
  ▼
Execution
  │
  ├── invoked
  ▼
Enterprise System
  │
  ├── produced
  ▼
Outcome

The audit trail should preserve these relationships.

⸻

8. Audit Record

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
causal relationship

Additional fields depend on the event or object being recorded.

⸻

9. Identity

Every consequential object should have a stable identifier.

Examples:

intent_id
action_id
trust_evaluation_id
execution_id
event_id
outcome_id

These identifiers allow independent records to be correlated.

⸻

10. Correlation

A complete execution should be traceable through a common correlation chain.

intent_id
    ↓
action_id
    ↓
trust_evaluation_id
    ↓
execution_id
    ↓
integration_request_id
    ↓
provider_reference
    ↓
event_id
    ↓
outcome_id

This is one of the most important properties of Noema’s enterprise audit model.

⸻

11. Actor Attribution

Auditability must identify the relevant actor.

An actor may be:

human
agent
service
system
administrator
integration

Where an agent acts on behalf of a human, the audit trail should preserve both identities.

initiating_actor
        ↓
delegated_actor
        ↓
Action

⸻

12. Actor vs Subject

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

13. Intent Audit

Noema should preserve the Intent that initiated a consequential journey.

This may include:

intent_id
input
actor
timestamp
channel
resolution state
resolved interpretation
clarifications

Where raw user input contains sensitive information, retention and access must follow applicable enterprise policy.

⸻

14. Intent Resolution Audit

When Noema resolves an Intent, the audit trail should establish:

original Intent
candidate interpretation
resolved interpretation
context used
ambiguities encountered
clarifications obtained
resolution outcome

This makes it possible to answer:

What did Noema believe the user meant?

⸻

15. Clarification History

Clarification is part of the execution journey and must therefore be auditable.

Example:

User:
"Send it to John."
Noema:
"Which John?"
User:
"John Smith in Finance."

The audit trail should preserve that the original Intent was ambiguous and how the ambiguity was resolved.

⸻

16. Model Output

Where a model contributes to Intent interpretation, auditability may preserve relevant model metadata.

Examples:

model identifier
model version
input reference
candidate interpretation
confidence
timestamp

The model’s internal reasoning trace is not required to establish auditability.

The canonical semantic result is.

⸻

17. Confidence Is Historical Evidence

If model confidence materially influenced the transition into clarification or another state, that fact may be recorded.

Example:

confidence:
0.92
resolution:
CLARIFICATION_REQUIRED

This establishes what the model produced without allowing confidence to become authorization.

⸻

18. Context Audit

Trust decisions depend on context.

Therefore, auditability should preserve references to the context used during evaluation.

Examples:

actor state
resource state
authorization state
environment
historical facts
enterprise records

The audit trail does not necessarily need to duplicate the entire source database.

It needs enough information or references to establish what was relied upon.

⸻

19. Evidence Audit

Every consequential Trust decision should be traceable to its supporting evidence.

Trust Decision
      │
      ├── Evidence A
      ├── Evidence B
      ├── Evidence C
      └── Policy P

Evidence should preserve provenance.

⸻

20. Evidence Provenance

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

This allows an auditor to determine whether the evidence was appropriate at the time.

⸻

21. Evidence Snapshot vs Reference

Noema may preserve either:

evidence snapshot

or:

reference to authoritative evidence

depending on sensitivity, retention, and reproducibility requirements.

The important requirement is:

The historical Trust decision must remain explainable even if the underlying enterprise state subsequently changes.

⸻

22. Policy Audit

A Trust decision must identify the Policy context under which it was made.

Example:

policy:
transfer-limit
version:
7
decision:
REJECT

This matters because policies change.

An audit record must not make a historical decision appear to have been evaluated under today’s policy when it was actually evaluated under an earlier version.

⸻

23. Authorization Audit

Authorization should also be attributable.

authorization source
authorization result
authorization scope
authorization timestamp

The audit trail should establish:

What authorization information did Noema rely upon?

⸻

24. Risk Audit

Where risk contributes materially to a Trust decision, the relevant risk evaluation should be traceable.

For example:

risk:
HIGH
policy:
HIGH risk requires human approval
decision:
ESCALATE

The audit trail should connect these facts.

⸻

25. Trust Decision Audit

A Trust decision should record:

evaluation_id
action_id
actor
decision
reasons
evidence references
policy references
authorization result
risk result
Trust model version
timestamp

The exact representation belongs to the Trust API and Trust model.

⸻

26. Deterministic Decision Reconstruction

For consequential decisions, an auditor should be able to determine:

Inputs
   ↓
Evaluation rules
   ↓
Decision

The goal is not necessarily to reproduce every internal computation.

The goal is to establish that the decision was produced according to the applicable deterministic Trust rules.

⸻

27. No “Because the AI Said So”

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
evidence:
fresh and authoritative

The model may contribute to Intent interpretation.

It does not become the authority for execution.

⸻

28. Action Audit

The Action record should establish:

what Action was created
who or what created it
which Intent produced it
which resources it targets
which Action Contract applies
which version was used

⸻

29. Action Mutation

Consequential Actions should not silently mutate after Trust evaluation.

If an Action materially changes:

Original Action
      ↓
Modified Action

the system should establish that a new Trust evaluation may be required.

The audit trail must preserve the relationship.

⸻

30. Execution Audit

Execution records should establish:

execution_id
action_id
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
final state

⸻

31. Execution State History

Recording only the final state is insufficient.

For example:

FAILED

does not explain whether the execution:

started
retried
waited
was interrupted
was compensated

The audit trail should preserve consequential state transitions.

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

32. Retry Audit

Every consequential retry should be attributable.

attempt_1
    ↓
FAILED
    ↓
attempt_2
    ↓
COMPLETED

The audit trail should establish why another attempt was permitted.

⸻

33. Human Intervention Audit

If a human becomes involved:

Trust:
ESCALATE
       ↓
Human approval
       ↓
Trust / Execution continues

the audit trail should record:

who intervened
what authority they possessed
what decision they made
when they made it
what object they acted upon

⸻

34. External Execution Audit

Noema may invoke an external enterprise system.

The audit trail should connect:

Noema Action
      ↓
Integration
      ↓
External request
      ↓
Provider response

Provider-specific identifiers should be retained where appropriate.

⸻

35. External System Authority

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

36. Outcome Audit

The final Outcome should establish what actually happened.

Expected:
card replaced
Observed:
provider confirms replacement

The audit trail should distinguish expected outcomes from observed outcomes.

⸻

37. Expected vs Observed

This distinction is critical.

Action Contract:
postcondition = card.status == REPLACED
Execution:
completed
Outcome:
enterprise reports card.status == REPLACED

Execution completion alone does not prove the postcondition.

⸻

38. Failed Outcomes

An execution may succeed technically while the desired Outcome fails.

Therefore:

Execution:
COMPLETED
Outcome:
FAILED

can be valid.

Auditability must preserve this distinction.

⸻

39. Audit Events

Events provide the chronological backbone of the audit trail.

Examples:

intent.created
intent.clarification_requested
intent.resolved
action.created
trust.evaluation_started
trust.decision_recorded
execution.started
execution.failed
execution.retried
execution.completed
outcome.verified

⸻

40. Events Are Immutable Facts

An event represents something that happened.

Historical events should not be rewritten merely because the current state has changed.

Event:
trust.decision.recorded
Decision:
REJECT
Later:
Policy changes

The historical event remains true.

⸻

41. Append-Oriented Audit History

Consequential audit history should conceptually behave as an append-oriented record.

Event 1
Event 2
Event 3
Event 4
...

Corrections should generally be represented as subsequent events rather than destructive edits.

⸻

42. State vs History

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

43. Causality

Auditability should preserve causality wherever possible.

For example:

clarification.requested
      ↓
clarification.received
      ↓
intent.resolved
      ↓
action.created

This is more useful than a flat list of unrelated timestamps.

⸻

44. Temporal Accuracy

Audit records should distinguish:

occurred_at
recorded_at

An external event may have happened at one time and reached Noema later.

These timestamps should not be conflated.

⸻

45. Clock and Ordering

Distributed systems may not provide a perfectly ordered global clock.

Therefore auditability should rely on:

timestamps
sequence information
causal identifiers
event identifiers
source timestamps

rather than assuming that database insertion order alone represents real-world causality.

⸻

46. Tenant Isolation

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

47. Audit Access Control

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

⸻

48. Data Minimization

Auditability does not mean storing everything forever.

Noema should preserve what is necessary to establish:

what happened
why it happened
who caused it
what evidence was used
what decision was made
what outcome occurred

Sensitive or unnecessary payloads should not be retained without a legitimate reason.

⸻

49. Immutability

Historical audit records should be tamper-resistant.

For consequential records, the system should provide mechanisms such as:

append-only storage
cryptographic integrity
signed records
hash chains
immutable retention

The specific implementation is not canonical at this stage.

The requirement is integrity.

⸻

50. Audit Record Integrity

An auditor must be able to distinguish:

original record

from:

modified or fabricated record

Therefore integrity mechanisms should be appropriate to the risk of the operation.

⸻

51. Retention

Audit retention should be configurable according to:

enterprise policy
regulatory requirements
data sensitivity
operation criticality
legal requirements

Noema should not assume that every record has the same retention period.

⸻

52. Deletion and Retention Conflicts

Auditability must coexist with privacy and retention requirements.

The canonical requirement is:

Preserve the evidentiary integrity of the execution journey while respecting applicable data-retention and deletion policies.

Implementation must distinguish immutable audit facts from sensitive payloads that may have separate retention requirements.

⸻

53. Auditability and Privacy

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

54. Auditability and Security

Security events may themselves become part of the audit trail.

Examples:

unauthorized access
Trust rejection
policy violation
credential failure
privilege escalation
manual override

This creates a broader enterprise security picture around Noema execution.

⸻

55. Manual Overrides

Manual intervention is itself consequential.

If a human overrides or changes an automated path, the audit trail must record:

original decision
override actor
authority
reason
timestamp
new decision/state

No override should silently erase the automated history.

⸻

56. Trust Re-evaluation Audit

Suppose:

Evaluation 1:
EXECUTE

then new evidence arrives:

Evaluation 2:
REJECT

The audit history should show both.

Evaluation 1
      ↓
Context changed
      ↓
Evaluation 2

The first decision must not be rewritten.

⸻

57. Auditability and Determinism

Determinism makes auditability substantially stronger.

If:

same Action
same policy
same evidence
same relevant context
same Trust model

are provided to the Trust Engine, the decision should be reproducible.

This allows the enterprise to distinguish:

deterministic system decision

from:

probabilistic model interpretation

⸻

58. Auditability of Ambiguity

Ambiguity itself is auditable state.

Example:

Intent:
"Send it to John."
State:
AMBIGUOUS
Reason:
multiple matching actors
Resolution:
CLARIFICATION_REQUIRED

This demonstrates that Noema did not silently guess.

⸻

59. Auditability of Non-Execution

Not executing an Action is also an important event.

Examples:

CLARIFY
ESCALATE
REJECT

These outcomes should be auditable just like execution.

A good enterprise audit trail explains both:

what Noema did

and:

what Noema deliberately refused to do.

⸻

60. Auditability of “Why Not?”

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
Execution dependency unavailable

This is a first-class audit requirement.

⸻

61. Audit Queryability

Audit records should be queryable by important dimensions.

Examples:

intent_id
actor_id
action_id
execution_id
trust_evaluation_id
resource_id
tenant_id
policy_id
decision
state
time range
integration
outcome

This enables operational investigation without requiring raw log archaeology.

⸻

62. Audit Views

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

⸻

63. Audit API Relationship

The Interfaces layer may expose audit information through APIs.

However, 06-enterprise/auditability.md defines what must be auditable, not the API mechanics.

The interface boundary is defined separately under 05-interfaces.

⸻

64. Auditability and Observability

These concepts overlap but are not identical.

Observability

Answers:

Is the system healthy?

Examples:

latency
throughput
error rate
resource usage

Auditability

Answers:

What happened in a consequential execution and why?

Examples:

Intent
Trust decision
Action
Execution
Outcome

Noema requires both, but they serve different purposes.

⸻

65. Auditability and Debugging

Debugging investigates system behavior.

Auditability establishes an authoritative historical account of consequential behavior.

A debug log may say:

retrying request

An audit record should establish:

Execution 123 entered RETRYING
because attempt 1 failed with provider timeout.

⸻

66. Auditability and Memory

Noema may retain historical information useful for future Intent resolution.

That does not make all memory an audit record.

Memory:
useful historical context
Audit:
authoritative record of consequential events and decisions

These should remain conceptually distinct.

⸻

67. Auditability as Enterprise Trust

The enterprise value of Noema depends partly on being able to answer:

Can I trust what happened?
Can I prove why it happened?
Can I reconstruct the decision?
Can I identify who authorized it?
Can I determine what system actually performed it?

Auditability provides that foundation.

⸻

68. Canonical Audit Object Graph

                    INTENT
                      │
                      ▼
                RESOLUTION
                      │
                      ▼
                   ACTION
                      │
            ┌─────────┴─────────┐
            ▼                   ▼
         CONTEXT              CONTRACT
            │                   │
            └─────────┬─────────┘
                      ▼
                 TRUST EVAL
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   AUTHORIZATION    POLICY         RISK
        │             │             │
        └─────────────┼─────────────┘
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
                   OUTCOME

Every significant node and relationship should be auditable.

⸻

69. Minimum Audit Chain

At minimum, a consequential operation should establish:

1. Who initiated the Intent
2. What Intent was received
3. What Intent was resolved
4. What Action was created
5. What Trust evaluation occurred
6. What evidence and policy supported it
7. What Trust decision resulted
8. What execution occurred
9. What external system was involved
10. What Outcome resulted

⸻

70. Canonical Audit Invariants

Invariant 1

Consequential Intent journeys must be reconstructable.

Invariant 2

Historical audit records must not be silently rewritten.

Invariant 3

Every consequential object must have stable identity.

Invariant 4

Intent, Action, Trust, Execution, and Outcome must remain distinguishable in the audit trail.

Invariant 5

Trust decisions must be traceable to their relevant evidence and policy.

Invariant 6

Model confidence must not be treated as authorization evidence.

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

⸻

71. The Enterprise Audit Question

The ultimate test for Noema’s auditability is whether an authorized enterprise operator can reconstruct:

WHO
 ↓
requested WHAT
 ↓
Noema understood WHAT
 ↓
using WHICH context
 ↓
created WHICH Action
 ↓
evaluated under WHICH policy
 ↓
using WHICH evidence
 ↓
received WHICH Trust decision
 ↓
executed WHICH operation
 ↓
against WHICH enterprise system
 ↓
producing WHICH Outcome

If that chain cannot be reconstructed, the system is not sufficiently auditable.

⸻

72. Final Definition

Auditability is the durable, attributable, and reconstructable record of Noema’s execution journey—from Intent through resolution, Trust, Action, Execution, and Outcome—preserving the evidence, policies, actors, state transitions, and causal relationships necessary to explain consequential behavior.

The fundamental distinction is:

Enterprise:
"What is the business state?"
Noema:
"What happened on the journey that attempted to change it,
and why did Noema permit, stop, or escalate that journey?"

That distinction should remain intact throughout the entire 06-enterprise domain.

Noema should make every consequential decision explainable without becoming the system of record for the enterprise’s underlying business reality.