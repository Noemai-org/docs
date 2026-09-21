Observability

Status: Foundational
Version: 0.1
Domain: Engineering
Canonical Path: engineering/observability.md

⸻

1. Definition

Observability is Noema’s engineering discipline for making the state, behavior, transitions, dependencies, failures, execution history, and externally relevant outcomes of the system inspectable and reconstructible.

Observability exists so that Noema can answer, with evidence:

* what happened
* what was attempted
* what state the system was in
* why a state changed
* which Intent was involved
* which version of the Intent was used
* which Trust evaluation applied
* which Action Graph was selected
* which Action Contracts were bound
* which capabilities were invoked
* what execution actually occurred
* what failed
* what was retried
* what remained unknown
* what external evidence was observed
* what outcome was ultimately established

Observability does not create authority.

It records and exposes evidence about the operation of authoritative Noema components and external systems.

The central principle is:

Noema must make consequential system behavior reconstructible from durable, structured evidence without requiring access to hidden model reasoning.

⸻

2. Purpose

Noema is an intent-governance system whose correctness depends not only on whether an operation succeeds, but on whether the system can establish how and under what conditions that operation occurred.

Observability therefore supports:

* operational diagnosis
* incident investigation
* execution reconstruction
* failure analysis
* Trust investigation
* Intent provenance
* Action Graph inspection
* Action Contract verification
* idempotency analysis
* retry analysis
* recovery analysis
* external-system correlation
* compliance and audit requirements
* performance analysis
* capacity analysis
* security investigation
* system debugging
* deterministic reproduction where possible

Observability must support both real-time operation and historical reconstruction.

⸻

3. Core Principle

Observability must expose system behavior without turning operational telemetry into a second authority model.

Conceptually:

System Execution
      │
      ├── State
      ├── Events
      ├── Decisions
      ├── Dependencies
      ├── Evidence
      ├── Errors
      └── Outcomes
             │
             ▼
        Observability
             │
      ┌──────┼──────┐
      ▼      ▼      ▼
    Metrics  Logs  Traces
             │
             ▼
      Reconstruction

Observability describes what the system did.

It does not determine what the system is permitted to do.

⸻

4. Observability vs Authority

Observability must remain separate from the components whose behavior it records.

For example:

Trust
  ↓
establishes execution eligibility
Action Graph
  ↓
establishes execution structure
Action Contract
  ↓
establishes executable obligations
Execution
  ↓
performs the Action
Observability
  ↓
records evidence of the above

Observability must not become an implicit mechanism for:

* granting authorization
* changing Trust state
* mutating Intent
* approving Actions
* changing Action Contracts
* declaring external business state
* declaring successful execution without evidence

The observability layer records authoritative events and states produced by the responsible components.

⸻

5. Observability vs Audit

Observability and audit overlap but are not identical.

Observability primarily answers:

What is happening or what happened operationally?

Audit primarily answers:

What authoritative decisions, transitions, and actions must remain reconstructible?

Observability may include:

* metrics
* traces
* operational logs
* latency
* resource utilization
* queue depth
* retries

Audit evidence may include:

* Intent versions
* Trust decisions
* Action Graph versions
* Contract bindings
* approvals
* execution transitions
* outcome evidence
* material state changes

Some observability records may therefore contribute to audit reconstruction.

However:

Observability ≠ Audit

Neither should silently replace the other.

⸻

6. Observability vs Model Reasoning

Noema must not require private model chain-of-thought as an observability mechanism.

The system should record decision provenance rather than hidden reasoning.

For example, it may record:

generation_source = model
model_id = ...
model_version = ...
candidate_intent_id = ...
resolution_rule_version = ...
evidence_references = [...]
result = AMBIGUOUS

It does not need to record hidden internal reasoning.

The canonical requirement is:

Record the evidence and decision metadata necessary to reconstruct system behavior, not private model reasoning.

⸻

7. Observability Model

Noema observability should operate across multiple complementary signals.

Conceptually:

                 Observability
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
     Events          Logs          Metrics
       │              │              │
       └──────────────┼──────────────┘
                      ▼
                    Traces
                      │
                      ▼
              State Reconstruction
                      │
                      ▼
                 Investigation

The primary observability primitives are:

* events
* structured logs
* metrics
* traces
* state snapshots where required
* provenance references
* correlation identifiers
* outcome records

⸻

8. Structured Observability

Observability records should be structured wherever machine processing is required.

A record should not depend on parsing arbitrary human-readable text to determine:

* event type
* Intent identity
* execution identity
* Action identity
* state
* outcome
* failure class
* timestamp
* correlation
* version

Human-readable descriptions may accompany structured records.

They must not replace canonical fields.

⸻

9. Event Model

Material system transitions should produce explicit events.

Conceptual examples include:

intent.created
intent.updated
intent.resolved
intent.superseded
intent.cancelled
trust.evaluation_started
trust.evaluated
trust.approval_required
trust.blocked
trust.ready
trust.invalidated
action_graph.created
action_graph.validated
action_graph.invalidated
action_graph.revised
action.started
action.completed
action.failed
action.retry_scheduled
action.retry_started
action.unknown
execution.started
execution.paused
execution.completed
execution.failed
execution.partially_completed
execution.unknown
recovery.started
recovery.completed
recovery.failed
compensation.started
compensation.completed
compensation.failed

These are architectural event categories.

The final event protocol may be defined separately.

⸻

10. Event Immutability

Material historical events should be append-oriented.

A later correction should not silently rewrite historical evidence.

Instead:

Event v1
   ↓
Correction / new evidence
   ↓
Event v2

Where an event was incorrect or incomplete, the system should preserve the relationship between:

* original observation
* correction
* source
* timestamp
* reason for correction

Historical reconstruction must remain possible.

⸻

11. Event Ordering

Observability must distinguish:

* event creation time
* event occurrence time
* event ingestion time
* event processing time

These timestamps are not necessarily identical.

For example:

T1  Action occurs
T2  External system responds
T3  Noema receives response
T4  Event is persisted
T5  Telemetry pipeline processes event

Observability must not silently treat T5 as the moment the Action occurred.

Where event ordering matters, Noema should use explicit sequencing or causal relationships.

⸻

12. Correlation Identity

Noema should use explicit identifiers to correlate related operations.

Relevant identifiers may include:

intent_id
intent_version
trust_evaluation_id
action_graph_id
action_graph_version
action_node_id
action_execution_id
action_contract_id
execution_id
recovery_id
compensation_id
event_id
trace_id
span_id
external_correlation_id

The exact identifier taxonomy should remain aligned with the canonical architecture.

Identifiers must not be conflated merely because their values happen to be available together.

⸻

13. Causality

Observability should preserve causal relationships between events.

For example:

intent.resolved
      ↓
trust.evaluated
      ↓
action_graph.validated
      ↓
action.started
      ↓
action.failed
      ↓
action.retry_scheduled
      ↓
action.retry_started
      ↓
action.completed

The system should make it possible to determine which event caused or enabled a later transition.

Timestamp ordering alone is insufficient where concurrent operations exist.

⸻

14. Intent Observability

The Intent lifecycle must be observable.

At minimum, Noema should be able to reconstruct:

1. original Actor expression
2. candidate interpretation
3. relevant context
4. resolution requirements
5. clarification requests
6. clarification responses
7. Intent versions
8. semantic state transitions
9. provenance
10. final canonical Intent

Conceptually:

Expression
    ↓
Candidate Intent
    ↓
Resolution
    ↓
Clarification
    ↓
Intent v2
    ↓
Resolved

The observability layer must preserve the relationship between these stages.

⸻

15. Intent Provenance

Material Intent fields should retain provenance.

For example:

recipient:
    value = customer_123
    source = ACTOR
    evidence = clarification_event_456

Possible sources include:

ACTOR
MODEL
CONTEXT
EXTERNAL_EVIDENCE
DETERMINISTIC_RULE
DEFAULT
CLARIFICATION

Observability must make it possible to distinguish established information from inferred information.

⸻

16. Trust Observability

Trust decisions must be observable without allowing observability to become the Trust authority.

A Trust evaluation record may include:

trust_evaluation_id
intent_id
intent_version
policy_versions
evidence_references
decision
state
timestamp
evaluation_version

For example:

Intent v7
    ↓
Trust Evaluation 14
    ↓
READY

If the Intent subsequently changes:

Intent v8
    ↓
new Trust Evaluation

The earlier Trust decision must remain associated with the earlier Intent version.

⸻

17. Action Graph Observability

The Action Graph must be observable as explicit structure.

Noema should be able to inspect:

* graph identity
* graph version
* source Intent
* nodes
* dependencies
* conditions
* capability bindings
* Action Contracts
* graph validation
* graph state
* revisions
* invalidation
* execution history

Conceptually:

Intent v7
   ↓
Graph v3
   ├── A
   ├── B
   ├── C
   └── D

The observability representation must preserve the graph structure rather than reducing it to a textual execution log.

⸻

18. Action Node Observability

Each Action execution should be independently observable.

Conceptually:

ActionExecution {
    action_execution_id
    action_node_id
    action_identity
    action_contract_id
    capability_id
    execution_id
    state
    attempt
    timestamps
    inputs_reference
    outputs_reference
    error
    outcome
    provenance
}

Sensitive input and output values should not automatically be copied into telemetry.

References may be used where appropriate.

⸻

19. Action Contract Observability

The system should record which Action Contract governed an execution.

This is necessary because:

Action Identity
    ≠
Action Contract
    ≠
Capability
    ≠
Authorization

An execution record should therefore permit reconstruction of the applicable contract version.

For example:

Action:
TRANSFER_FUNDS
Contract:
transfer.v4
Capability:
payment.transfer
Execution:
execution_123

A later contract version must not silently rewrite the historical association.

⸻

20. Capability Observability

Capability selection and invocation should be observable.

Relevant information may include:

* capability identity
* capability version
* provider identity
* binding version
* invocation timestamp
* invocation outcome
* latency
* external correlation identifier
* failure classification

Capability observability must not be interpreted as authorization evidence.

⸻

21. Execution Observability

Execution must expose the operational lifecycle.

Conceptually:

NOT_STARTED
    ↓
READY
    ↓
EXECUTING
    ↓
COMPLETED

or:

EXECUTING
    ↓
FAILED
    ↓
RETRY
    ↓
UNKNOWN

The observability record must preserve actual transitions rather than only the final state.

⸻

22. State Transition Observability

Every material state transition should have an identifiable cause.

For example:

READY
  ↓
BLOCKED
Cause:
required approval missing

or:

EXECUTING
  ↓
UNKNOWN
Cause:
external response uncertain

A state should not appear to change without an observable event, dependency transition, contract result, material condition change, or deterministic re-evaluation.

⸻

23. Failure Observability

Failures must be structured.

A failure record should distinguish at least:

* failure class
* source
* Action
* execution attempt
* retryability
* external response
* recovery state
* final outcome

For example:

failure_class = TIMEOUT
source = EXTERNAL_SYSTEM
retryable = TRUE
attempt = 1
outcome = UNKNOWN

The system must not collapse all failures into a generic FAILED record.

⸻

24. Unknown Outcomes

Unknown execution outcomes are first-class observability states.

Example:

REQUEST_PAYMENT
      ↓
network timeout
      ↓
result = UNKNOWN

Observability must preserve the distinction between:

FAILED

and:

UNKNOWN

This distinction is essential for recovery and idempotency.

An unknown result must not be recorded as a failure merely because no response was received.

⸻

25. Retry Observability

Every retry should be observable.

A retry record should identify:

* original Action execution
* attempt number
* retry reason
* retry policy
* delay
* eligibility
* idempotency context
* result

Example:

Attempt 1
   ↓
TIMEOUT
   ↓
Retry permitted
   ↓
Attempt 2
   ↓
COMPLETED

Retries must remain distinguishable from independent executions.

⸻

26. Idempotency Observability

Observability must make idempotency behavior inspectable.

Relevant information may include:

idempotency_key
operation_identity
attempt
deduplication_result
original_execution_reference
provider_reference

This allows investigators to determine whether:

* an operation was retried
* a duplicate request was suppressed
* an external provider reused an existing operation
* an uncertain operation was reconciled

Observability must not expose idempotency keys unnecessarily where they are sensitive.

⸻

27. Recovery Observability

Recovery actions must be independently observable.

For example:

Action Failed
     ↓
Recovery Started
     ↓
Reconciliation
     ↓
Recovery Completed

The recovery record should identify:

* triggering failure
* recovery policy
* recovery attempt
* recovery Action
* result
* resulting execution state

Recovery must not disappear into an opaque error handler.

⸻

28. Compensation Observability

Compensating Actions require explicit observability.

Example:

A completed
B completed
C failed
Compensation:
B_compensate
A_compensate

Observability must distinguish:

original Action
compensating Action
rollback
reconciliation
manual intervention

Compensation does not imply transactional rollback.

The observed external state must determine the final outcome.

⸻

29. Human Intervention Observability

Human intervention is a legitimate system state and must be observable.

For example:

ACTION
  ↓
HUMAN_REVIEW_REQUIRED
  ↓
APPROVED
  ↓
CONTINUE

The system should record:

* why intervention was required
* what approval was requested
* who or what authority provided it, according to permitted identity semantics
* when it occurred
* what graph or Action it affected
* whether re-evaluation was required

Human intervention must not be represented merely as an unexplained delay.

⸻

30. Clarification Observability

Clarification is also a first-class observable lifecycle event.

Example:

Intent v1
recipient = ambiguous
      ↓
clarification_required
      ↓
Actor response
      ↓
Intent v2
recipient = customer_123

The relationship between the clarification and the resulting Intent version must be reconstructible.

⸻

31. Metrics

Metrics provide aggregate operational visibility.

Useful metric categories include:

Intent Metrics

* Intent creation rate
* resolution rate
* clarification rate
* unresolved Intent count
* Intent resolution latency
* Intent supersession rate
* Intent cancellation rate

Trust Metrics

* Trust evaluation rate
* READY rate
* BLOCKED rate
* approval-required rate
* Trust evaluation latency
* Trust invalidation rate

Graph Metrics

* graph construction rate
* graph validation failures
* graph revision rate
* graph invalidation rate
* graph size
* dependency count
* graph execution latency

Execution Metrics

* Action execution rate
* success rate
* failure rate
* unknown outcome rate
* retry rate
* recovery rate
* compensation rate
* execution latency

Infrastructure Metrics

* queue depth
* worker utilization
* resource saturation
* persistence latency
* event processing latency
* dependency availability

Metrics provide aggregate signals.

They do not replace event history.

⸻

32. Metrics Must Not Become Authority

A metric such as:

execution_success_rate = 99.9%

does not establish that a particular execution succeeded.

Similarly:

trust_ready_rate = 98%

does not establish that a particular Intent is trusted.

Metrics are aggregate observations.

Canonical state belongs to the responsible system components and durable records.

⸻

33. Histograms and Latency

Latency should be measured across meaningful lifecycle boundaries.

Examples:

expression → resolved Intent
resolution → validation
validation → Trust
Trust → graph construction
graph construction → execution
Action start → Action completion
execution start → final outcome

Where possible, latency should distinguish:

* queue time
* processing time
* external call time
* retry delay
* human waiting time
* recovery time

A single aggregate latency can hide important operational behavior.

⸻

34. Tracing

Distributed execution should support causal tracing across system boundaries.

A trace may represent:

Intent
 └── Resolution
      └── Validation
           └── Trust
                └── Action Graph
                     ├── Action A
                     │    └── Provider Call
                     └── Action B
                          └── Provider Call

Tracing should make dependencies and timing visible.

It must not be assumed that one trace is sufficient to reconstruct durable historical state.

Trace data may be sampled or retained for limited periods.

Durable events remain authoritative for historical reconstruction.

⸻

35. Trace Context Propagation

Where supported, trace context should propagate across internal service boundaries and external integrations.

Relevant identifiers may include:

trace_id
span_id
parent_span_id
external_correlation_id

Propagation must respect security and privacy boundaries.

Noema must not assume that an external provider will preserve Noema’s trace context.

External correlation identifiers should therefore be retained where available.

⸻

36. Logs

Logs should provide diagnostic detail while remaining structured.

A log record may include:

timestamp
severity
component
event_type
execution_id
intent_id
action_execution_id
trace_id
message
error_code
metadata

Logs should not be the only durable representation of material state transitions.

For example:

INFO: transfer completed

is insufficient as the canonical record of completion.

A structured execution event should establish the actual state.

⸻

37. Log Levels

Operational logging should distinguish severity.

Conceptual levels include:

DEBUG
INFO
WARN
ERROR
CRITICAL

The exact taxonomy may evolve.

The important principle is that severity should reflect operational significance rather than developer preference.

A normal expected business rejection should not necessarily be represented as an infrastructure error.

⸻

38. Error Classification

Observability should distinguish at least:

SEMANTIC_ERROR
VALIDATION_ERROR
TRUST_ERROR
CONTRACT_ERROR
AUTHORIZATION_ERROR
DEPENDENCY_ERROR
EXTERNAL_BUSINESS_ERROR
EXTERNAL_SYSTEM_ERROR
TIMEOUT
NETWORK_ERROR
RESOURCE_ERROR
CONFIGURATION_ERROR
INTERNAL_ERROR
UNKNOWN

The final error taxonomy should remain aligned with the relevant engineering specifications.

Error classification should preserve the difference between:

the system rejected the operation

and:

the system could not establish what happened

⸻

39. External System Observability

External systems remain authoritative for their business domains.

Observability should therefore record:

* provider
* operation
* provider request/reference
* provider response classification
* provider status
* timestamps
* correlation identifier
* reconciliation status

For example:

Noema:
execution = UNKNOWN
Provider:
operation_status = COMPLETED
provider_reference = 789

Reconciliation may subsequently establish the Noema execution outcome.

Noema must not invent external state when evidence is unavailable.

⸻

40. Business State vs Observed State

Observability must distinguish:

authoritative business state

from:

Noema's observed representation of that state

For example:

Provider:
account.status = ACTIVE
Noema:
observed_account_status = ACTIVE
observed_at = T1

At T2 the provider may change the state.

The older observation remains historically valid as an observation at T1 but may no longer represent current external state.

⸻

41. Staleness

Observability records that depend on external state should include sufficient temporal context to establish staleness.

For example:

evidence:
account.status = ACTIVE
observed_at = 10:00
source = AccountSystem

An execution at 14:00 must not silently treat the 10:00 observation as current merely because it exists.

Observability should make such temporal relationships visible.

⸻

42. Time Synchronization

Distributed observability depends on reliable timestamps.

Systems should use a consistent time basis and account for clock skew where relevant.

Where precise causal ordering cannot be established from timestamps, Noema should rely on:

* event sequence
* causal identifiers
* durable ordering
* provider references
* explicit state transitions

Timestamp proximity must not be mistaken for causality.

⸻

43. State Reconstruction

A primary purpose of observability is reconstructing historical system state.

Conceptually:

Initial State
    ↓
Event 1
    ↓
Event 2
    ↓
Event 3
    ↓
Event 4
    ↓
Reconstructed State

A reconstruction should identify:

* source records
* event versions
* applicable policies
* Intent version
* Action Graph version
* Contract version
* execution attempts
* outcome evidence

Reconstruction must preserve uncertainty where the historical evidence itself was uncertain.

⸻

44. Reconstruction Must Not Invent State

If historical evidence does not establish a fact, reconstruction must preserve:

UNKNOWN

rather than silently selecting:

FAILED

or:

SUCCESS

For example:

Action sent
Provider response missing

does not establish that the Action failed.

The reconstructed state should remain:

UNKNOWN

until authoritative evidence establishes otherwise.

⸻

45. Provenance

Every material observability record should be traceable to its source.

Provenance may identify:

* producing component
* source event
* external system
* version
* timestamp
* correlation identifier
* evidence reference
* transformation applied

For example:

Outcome:
COMPLETED
Evidence:
provider_event_789
Observed by:
reconciliation_service
Observed at:
T2

This allows later investigation of how an outcome was established.

⸻

46. Version Awareness

Observability records must retain relevant versions.

Potential version dimensions include:

Intent version
Trust evaluation version
policy version
Action Graph version
Action Contract version
capability version
resolution rule version
execution protocol version
component version

A current version must not overwrite the historical version associated with an earlier execution.

⸻

47. Configuration Observability

Material configuration changes should be observable.

Examples:

* retry policy changes
* timeout changes
* routing changes
* capability bindings
* policy versions
* feature activation
* execution limits

A production incident may otherwise be impossible to reconstruct if the system behavior changed because configuration changed.

Configuration history should therefore be versioned where materially relevant.

⸻

48. Deployment Observability

Execution evidence should be correlatable with the software version that produced it.

Relevant metadata may include:

service
component
build_id
release_id
deployment_version
runtime_version

This supports investigation of behavioral changes across deployments.

The deployment version does not establish semantic authority; it establishes implementation provenance.

⸻

49. Sampling

Tracing and high-volume telemetry may require sampling.

Sampling must not cause the loss of canonical evidence required for:

* material state transitions
* execution outcomes
* Trust decisions
* Action execution
* recovery
* compensation
* security events
* required audit evidence

Sampling may be applied to diagnostic telemetry where complete retention is unnecessary.

The distinction is:

Diagnostic telemetry may be sampled.
Canonical execution evidence must not be silently sampled away.

⸻

50. Retention

Observability data should have explicit retention policies.

Different classes may require different retention periods.

For example:

Metrics
    → short/medium operational retention
Traces
    → diagnostic retention
Logs
    → operational retention
Canonical events
    → durable historical retention
Audit evidence
    → policy-defined retention

Retention must account for:

* legal requirements
* security requirements
* operational needs
* privacy requirements
* reconstruction requirements
* storage constraints

The exact periods should be defined by applicable governance rather than embedded here.

⸻

51. Privacy

Observability must not become an uncontrolled copy of user data.

Telemetry should minimize sensitive information.

Where possible:

* store references instead of full payloads
* redact sensitive values
* tokenize identifiers
* restrict access
* avoid unnecessary duplication
* separate operational metadata from sensitive business data

The fact that data is useful for debugging does not automatically justify storing it in telemetry.

⸻

52. Secrets

Secrets must never be emitted into ordinary observability channels.

Examples include:

* credentials
* API keys
* access tokens
* private keys
* authentication secrets
* encryption keys

Redaction must occur before data enters telemetry systems where practical.

Observability pipelines should also enforce defensive filtering because application-level redaction may fail.

⸻

53. Payload Logging

Full Action payloads should not be logged by default.

Instead, observability should prefer:

payload_reference
schema
hash
field metadata
redacted representation

where sufficient for investigation.

If a payload is necessary for a specific audit or debugging requirement, its retention and access controls should be explicit.

⸻

54. Security Observability

Security-relevant events should be observable.

Examples include:

* unauthorized execution attempts
* Trust denial
* capability misuse
* contract violations
* unexpected Action requests
* identity mismatches
* policy violations
* privilege escalation attempts
* abnormal execution patterns

Security observability should support investigation without exposing unnecessary sensitive data.

⸻

55. Model Observability

Where models participate in Noema, model involvement should be observable.

Relevant metadata may include:

model_id
model_version
provider
generation_timestamp
request_reference
candidate_output_reference

For Intent processing:

model
   ↓
candidate interpretation
   ↓
Intent Engine

For Action Graph construction:

model
   ↓
candidate graph
   ↓
graph validation

Model provenance identifies the origin of a proposal.

It does not establish its correctness or authority.

⸻

56. Model Confidence

Model confidence may be recorded where operationally useful.

However:

confidence ≠ canonical state

For example:

model_confidence = 0.99
resolution = UNRESOLVED

is valid.

Observability must preserve both values rather than collapsing confidence into resolution.

⸻

57. Candidate and Canonical Artifacts

Observability should distinguish candidate artifacts from canonical artifacts.

Examples:

Candidate Intent
Canonical Intent
Candidate Action Graph
Executable Action Graph
Model Proposal
Validated Graph
Predicted Outcome
Observed Outcome

A model-generated artifact must not appear in telemetry as though it were an authoritative system state.

⸻

58. Operational Dashboards

Operational dashboards should expose system state at appropriate aggregation levels.

Useful dashboard dimensions include:

* Intent throughput
* resolution backlog
* clarification backlog
* Trust backlog
* Action Graph backlog
* execution backlog
* failure rates
* unknown outcomes
* retry rates
* recovery backlog
* external dependency health
* latency
* resource saturation

Dashboards should link aggregate conditions to reconstructible individual records.

A dashboard should not be the only place where a critical fact exists.

⸻

59. Alerting

Alerts should be based on explicit operational conditions.

Examples:

unknown outcomes exceed threshold
retry rate exceeds threshold
external dependency unavailable
execution queue exceeds threshold
recovery backlog exceeds threshold
event processing lag exceeds threshold

Alerts should identify:

* condition
* scope
* time window
* severity
* affected component
* relevant correlation identifiers where available

An alert is an operational signal, not an authoritative state transition.

⸻

60. SLO and Reliability Observability

Reliability objectives should be measurable through observability.

Potential dimensions include:

* Intent resolution latency
* Trust evaluation latency
* Action execution latency
* outcome establishment latency
* event durability latency
* reconciliation latency
* recovery latency
* availability of critical capabilities

Reliability measurements must distinguish:

system availability

from:

business operation success

A healthy execution platform does not guarantee that an external business operation will succeed.

⸻

61. Dependency Observability

Every material dependency should be observable.

Examples:

Intent Engine
    ↓
Context Service
Action
    ↓
Payment Provider
Execution
    ↓
Event Store

Dependency observability should capture:

* availability
* latency
* failure rate
* timeout rate
* response classes
* dependency version where relevant
* correlation identifiers

This supports diagnosis without incorrectly assigning external failures to Noema itself.

⸻

62. Queue and Worker Observability

Where durable execution uses queues or workers, observability should include:

* queue depth
* enqueue rate
* dequeue rate
* processing latency
* retry count
* dead-letter count
* worker availability
* worker saturation
* lease state
* stuck execution count

This is particularly important for distinguishing:

Action not executed

from:

Action executed and failed

Those are materially different states.

⸻

63. Durable Execution Observability

Durable execution requires enough observability to reconstruct execution after interruption.

At minimum, the system should preserve:

* execution identity
* current execution state
* completed Actions
* pending Actions
* failed Actions
* unknown Actions
* retry attempts
* recovery state
* compensation state
* Action Graph version
* Contract version
* external correlation identifiers

A process restart must not destroy the historical execution record.

⸻

64. Checkpoint Observability

Where execution checkpoints are used, observability should expose checkpoint identity and relationship.

Conceptually:

Execution
   ↓
Checkpoint 1
   ↓
Action A completed
   ↓
Checkpoint 2
   ↓
Action B executing

A checkpoint should not itself be treated as proof that an external Action succeeded unless the corresponding contract and evidence establish that fact.

⸻

65. Recovery After Restart

After restart, observability should permit the system to establish:

What was the last durable state?
What Actions were completed?
What Actions were executing?
What outcomes were unknown?
What retries are permitted?
What recovery policy applies?

This is essential to prevent duplicate or lost execution.

⸻

66. Reconciliation Observability

When an outcome is initially unknown, reconciliation should be observable.

Example:

Action
  ↓
UNKNOWN
  ↓
Reconciliation Requested
  ↓
Provider Query
  ↓
Provider:
COMPLETED
  ↓
Noema:
COMPLETED

The original unknown state must remain historically visible.

The later reconciliation establishes a subsequent state.

⸻

67. No Silent State Repair

Operational systems must not silently repair historical state without preserving the reason.

If an execution record changes from:

UNKNOWN

to:

COMPLETED

the system should preserve:

* original unknown event
* reconciliation event
* authoritative evidence
* transition cause
* timestamp
* actor/component responsible for reconciliation

This preserves historical truth.

⸻

68. Observability of Re-Evaluation

Material re-evaluation should be observable.

Examples:

Intent changed
    ↓
Validation rerun
    ↓
Trust rerun
    ↓
Graph revised

or:

External state changed
    ↓
Precondition invalidated
    ↓
Execution blocked

Re-evaluation must not appear as an unexplained state mutation.

⸻

69. Graph Revision Observability

Action Graph revisions should record:

* previous graph version
* new graph version
* reason
* triggering event
* changed nodes
* changed dependencies
* changed capabilities
* changed contracts
* affected execution state

For example:

Graph v3
   ↓
Capability unavailable
   ↓
Graph invalidated
   ↓
Graph v4

The relationship must remain reconstructible.

⸻

70. Configuration and Policy Correlation

Where a policy or configuration affects behavior, the applicable version should be observable.

Example:

Transfer amount > threshold
        ↓
Approval policy v8
        ↓
Approval node inserted

The system should be able to determine which policy version produced the requirement.

This is particularly important when policies change after an Intent has been created.

⸻

71. Observability of Atomicity

Observability must make partial execution semantics visible.

For example:

Intent:
partial execution = NOT_PERMITTED
Action A = COMPLETED
Action B = BLOCKED
Action C = NOT_STARTED

The resulting outcome must not be represented simply as:

SUCCESS

Similarly, where partial execution is explicitly permitted, observability should identify which components completed and which did not.

⸻

72. Outcome Observability

Outcome records should distinguish:

COMPLETED
FAILED
PARTIALLY_COMPLETED
BLOCKED
WAITING
UNKNOWN

The exact outcome taxonomy should remain aligned with the execution architecture.

Outcome observability should include the evidence supporting the final classification.

⸻

73. Trust State vs Execution State

Observability must preserve separate dimensions.

For example:

Trust:
READY
Execution:
FAILED

is valid.

Likewise:

Trust:
WAITING_FOR_APPROVAL
Execution:
NOT_STARTED

is valid.

Observability must not flatten these dimensions into one generic status.

⸻

74. Intent State vs Execution State

Similarly:

Intent:
RESOLVED
Execution:
FAILED

does not mean that the Intent was semantically invalid.

The observability system must preserve:

Intent state
Trust state
Graph state
Execution state
Outcome state

as distinct dimensions where applicable.

⸻

75. Observability Invariants

Invariant 1

Material system behavior must be observable through structured evidence.

Invariant 2

Observability must not become an authority mechanism.

Invariant 3

Historical material events must not be silently overwritten.

Invariant 4

Intent, Trust, Graph, Execution, and Outcome states must remain distinguishable.

Invariant 5

Unknown outcomes must remain distinguishable from failure.

Invariant 6

Retries must be distinguishable from independent executions.

Invariant 7

Recovery and compensation must be explicitly observable.

Invariant 8

Material version information must remain reconstructible.

Invariant 9

External business state must remain attributed to its authoritative source.

Invariant 10

Observability must preserve sufficient causal information for execution reconstruction.

Invariant 11

Sampling must not silently remove required canonical evidence.

Invariant 12

Sensitive information must not be unnecessarily replicated into telemetry.

Invariant 13

Secrets must never be exposed through ordinary observability channels.

Invariant 14

Model provenance does not establish authority.

Invariant 15

Model confidence does not establish semantic resolution or execution eligibility.

Invariant 16

A dashboard or metric must not substitute for canonical state.

Invariant 17

State repair must preserve the original state and the evidence supporting the correction.

Invariant 18

A final outcome must be supported by observable evidence appropriate to the outcome semantics.

⸻

76. Canonical Observability Record

Conceptually:

ObservabilityRecord {
    event_id
    event_type
    timestamp
    occurrence_time
    actor_reference
    intent_id
    intent_version
    trust_evaluation_id
    action_graph_id
    action_graph_version
    action_node_id
    action_execution_id
    action_contract_id
    capability_id
    execution_id
    trace_id
    span_id
    state
    outcome
    attempt
    source
    evidence_references
    external_correlation_id
    component
    component_version
    error
    metadata
}

The exact schema belongs to the implementation and protocol specifications.

The canonical requirement is that material relationships remain reconstructible.

⸻

77. Canonical Investigation Flow

A production investigation should be able to proceed from a high-level identifier down to individual execution evidence.

Conceptually:

Intent ID
   ↓
Intent Version
   ↓
Trust Evaluation
   ↓
Action Graph Version
   ↓
Action Node
   ↓
Action Contract
   ↓
Action Execution
   ↓
Attempt
   ↓
External Provider Reference
   ↓
Observed Outcome

This permits investigation without requiring access to undocumented internal state.

⸻

78. Incident Reconstruction

For a consequential incident, Noema should be able to reconstruct:

1. what the Actor expressed
2. which Intent was established
3. which Intent version was used
4. what context and evidence were used
5. what Validation occurred
6. what Trust evaluation occurred
7. which Action Graph was selected
8. which Action Contracts were bound
9. which Actions executed
10. which attempts occurred
11. what external systems returned
12. which failures occurred
13. what recovery occurred
14. what compensation occurred
15. what final outcome was established

This is the minimum conceptual reconstruction chain.

⸻

79. Reproducibility

Observability should support reproducibility where deterministic inputs are available.

For a deterministic operation:

Inputs
+
Versions
+
Rules
+
Evidence
+
Configuration

should provide enough information to understand why a result was produced.

Reproducibility does not imply that external systems can be recreated.

Where external state was involved, Noema should preserve references to the evidence that was available at the time.

⸻

80. Observability and Determinism

Observability should make deterministic behavior distinguishable from probabilistic behavior.

For example:

Model:
candidate interpretation
Intent Engine:
deterministic resolution
Validation:
deterministic result
Trust:
policy evaluation
Execution:
external outcome

The observability record should preserve these boundaries.

A probabilistic proposal must not appear indistinguishable from a deterministic canonical decision.

⸻

81. Observability and Failure Recovery

Failure recovery depends on accurate historical evidence.

Therefore recovery logic must be able to determine:

Was the Action executed?
Was its result known?
Was it retried?
Was an idempotency key used?
Did the provider acknowledge it?
Was compensation attempted?
What state was last durably recorded?

Observability is therefore a dependency of safe recovery.

It must not merely describe failures after recovery has already occurred.

⸻

82. Observability and Idempotency

Idempotency decisions require historical execution evidence.

The system should be able to establish whether:

operation X

was already attempted under:

idempotency identity Y

and what outcome was previously established.

This allows recovery logic to distinguish:

safe retry

from:

potential duplicate execution

Observability therefore supports, but does not itself implement, idempotency semantics.

⸻

83. Observability and Action Graph Integrity

The observability layer should make it possible to detect divergence between:

declared Action Graph

and:

actual execution

For example, if the graph contains:

A → B → C

but execution records show:

A → C

the discrepancy should be detectable.

Similarly, hidden consequential Actions should be observable and attributable to their contractual or graph source.

⸻

84. No Hidden Execution

Noema must not allow consequential execution to disappear from observability.

If an Action Contract internally performs multiple operations, the system must establish the appropriate abstraction boundary.

Those operations must be either:

* represented as graph Actions,
* represented as contractually defined internal operations,
* or otherwise explicitly attributable to the governing execution contract.

An unexplained consequential external operation is an observability and architectural integrity failure.

⸻

85. Observability Health

The observability system itself must be observable.

Noema should monitor:

* telemetry pipeline availability
* event persistence latency
* event delivery failures
* telemetry queue depth
* dropped records
* schema validation failures
* ingestion lag
* storage failures
* trace propagation failures
* redaction failures

A system cannot rely on observability that it cannot determine is functioning.

⸻

86. Canonical vs Diagnostic Telemetry

Noema should distinguish:

Canonical telemetry

Evidence required to reconstruct material system behavior.

Examples:

* state transitions
* execution outcomes
* Trust decisions
* graph versions
* contract bindings
* recovery events

Diagnostic telemetry

Evidence useful for operational investigation but not required as authoritative history.

Examples:

* debug logs
* detailed timing samples
* transient worker metrics
* sampled traces

Diagnostic telemetry may have different retention and reliability requirements.

Canonical telemetry must receive stronger durability guarantees.

⸻

87. Schema Evolution

Observability schemas will evolve.

Schema changes must preserve the ability to interpret historical records.

Where fields change:

* schema versions should be explicit
* deprecated fields should remain interpretable
* migrations should be documented
* historical records should not become semantically ambiguous

A telemetry consumer must be able to determine which schema governed a historical record.

⸻

88. Backward Compatibility

Observability consumers may include:

* dashboards
* alerts
* incident tooling
* audit systems
* recovery systems
* analytics
* debugging tools

Changes to canonical event semantics must therefore be versioned and compatibility-managed.

A field should not silently change meaning while retaining the same name.

⸻

89. Observability Access

Access to observability data should follow least-privilege principles.

Different users and systems may require access to:

* aggregate metrics
* operational logs
* execution traces
* Intent metadata
* audit records
* sensitive evidence

Access should therefore be scoped according to data sensitivity and operational responsibility.

Observability must not become an unrestricted path to business or Actor data.

⸻

90. Observability and Governance

Governance requirements may determine what must be retained and inspectable.

However, governance requirements should not cause the observability system to collapse distinct architectural layers.

For example:

Audit requirement
    ↓
retain Trust decision

does not mean:

Audit system
    ↓
becomes Trust Engine

Observability records governance-relevant evidence while preserving component boundaries.

⸻

91. Observability Failure

If the observability subsystem is unavailable, Noema must have explicitly defined behavior for consequential operations.

Depending on the operation, the system may:

* continue using durable canonical event mechanisms
* buffer telemetry
* degrade diagnostic telemetry
* block execution where required evidence cannot safely be established
* enter a controlled failure state

The system must not silently execute consequential operations when required canonical evidence cannot be durably recorded.

The exact fail-open or fail-closed semantics belong to the relevant execution and governance specifications.

⸻

92. Observability and Execution Boundary

Before consequential execution, Noema should be able to establish the minimum evidence necessary to reconstruct the execution attempt.

Conceptually:

Executable Action
      ↓
Execution Event
      ↓
External Invocation
      ↓
Outcome Event

The exact transactional relationship between event persistence and external invocation belongs to the durable execution architecture.

The observability requirement is that the system must preserve enough evidence to distinguish:

not attempted

from:

attempted

and:

attempted with unknown outcome

⸻

93. Observability State Machine Principle

Observability records state transitions; it does not invent them.

A state may change because of:

* defined event
* dependency transition
* contract result
* material condition change
* deterministic re-evaluation
* recovery
* reconciliation
* explicit human intervention

It must not change merely because:

* a model generated another answer
* a log was rewritten
* an operator inferred a likely outcome
* a metric crossed a threshold

Inference may be recorded as analysis.

It must not be represented as canonical state without supporting evidence.

⸻

94. Observability of Unknowns

Unknown information must remain explicit throughout observability.

Examples:

external_outcome = UNKNOWN
provider_response = NOT_RECEIVED
business_state = UNKNOWN
dependency_health = UNKNOWN

Unknown must not be silently converted into:

FALSE
FAILED
ABSENT
UNAUTHORIZED

The observability layer must preserve epistemic distinctions that are relevant to execution and recovery.

⸻

95. Observability and Outcome Finalization

An outcome should be finalized only when the applicable evidence establishes the relevant completion semantics.

For example:

provider response:
accepted

may establish:

request accepted

but not necessarily:

business operation completed

The observability system must preserve the distinction between:

* request submitted
* request accepted
* operation processed
* business outcome established

where the governing Action Contract requires those distinctions.

⸻

96. Canonical Observability Flow

The canonical observability lifecycle is:

Actor Expression
       ↓
Candidate Intent
       ↓
Intent Resolution
       ↓
Canonical Intent
       ↓
Validation
       ↓
Trust Evaluation
       ↓
Action Graph
       ↓
Action Contract
       ↓
Execution
       ↓
External Evidence
       ↓
Outcome

Across the lifecycle:

Events
Logs
Metrics
Traces
Provenance
State Transitions
Evidence References

provide the observable record.

⸻

97. Engineering Relationship

Observability connects Noema’s engineering subsystems without collapsing their responsibilities.

Conceptually:

Intent Engine
      │
      ├──────────────┐
      ▼              │
Validation           │
      │              │
      ▼              │
Trust                │
      │              │
      ▼              │
Action Graph         │
      │              │
      ▼              │
Action Contracts     │
      │              │
      ▼              │
Durable Execution    │
      │              │
      ▼              │
Failure Recovery     │
      │              │
      ▼              │
Outcome              │
      │              │
      └──────────────┘
             │
             ▼
       Observability

Observability provides the evidence plane across the architecture.

It does not replace any of these components.

⸻

98. Canonical Mental Model

Observability can be reduced to five questions:

1. What happened?
2. What state was the system in?
3. Why did the state change?
4. What evidence supports the observed result?
5. Can the consequential execution be reconstructed?

Which produces:

Event
  ↓
State
  ↓
Cause
  ↓
Evidence
  ↓
Reconstruction

⸻

99. Final Definition

Observability is Noema’s engineering evidence layer for making consequential system behavior, state transitions, dependencies, failures, recoveries, external interactions, and outcomes inspectable and reconstructible.

Its central invariant is:

Noema must never require hidden model reasoning, transient process state, or informal operator memory to explain what happened during consequential execution.

The system must preserve structured evidence across the lifecycle:

Intent
   ↓
Validation
   ↓
Trust
   ↓
Action Graph
   ↓
Action Contract
   ↓
Execution
   ↓
Recovery / Reconciliation
   ↓
Outcome

with sufficient provenance to distinguish:

what was proposed
from
what was established
what was authorized
from
what was attempted
what was attempted
from
what was observed
what failed
from
what remained unknown
what happened
from
what was merely inferred

The fundamental engineering boundary is therefore:

System Behavior
      ↓
Durable Evidence
      ↓
Observability
      ↓
Inspection
      ↓
Reconstruction

Observability does not make Noema authoritative.

It makes Noema’s authoritative decisions, execution behavior, failures, uncertainty, and outcomes inspectable, attributable, and reconstructible.