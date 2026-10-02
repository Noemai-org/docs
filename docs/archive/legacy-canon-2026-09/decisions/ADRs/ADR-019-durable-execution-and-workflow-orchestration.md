ADR-019 — Durable Execution and Workflow Orchestration

Status: Proposed
Version: 0.1
Date: 2026-09-21
Decision Type: Architecture
Domain: Execution / Architecture
Canonical Path: decisions/ADRs/ADR-019-durable-execution-and-workflow-orchestration.md

⸻

1. Title

Adopt durable workflow orchestration as a foundational execution capability for Noema.

⸻

2. Context

Noema is not merely a request/response system.

A Noema Intent may progress through a lifecycle involving:

Intent
  ↓
Resolution
  ↓
Validation
  ↓
Trust
  ↓
Planning
  ↓
Execution Contract
  ↓
Execution
  ↓
Outcome

That lifecycle may span:

* multiple enterprise systems
* asynchronous operations
* approvals
* human intervention
* retries
* waiting periods
* external callbacks
* capability availability
* policy changes
* execution failures
* partial execution
* outcome verification

Therefore execution cannot be modeled reliably as a single synchronous function call.

A consequential Intent may need to remain active for seconds, minutes, hours, or potentially much longer.

Noema therefore requires a mechanism for maintaining durable execution state across process restarts, infrastructure failures, retries, worker failures, and asynchronous events.

⸻

3. Problem

A conventional application-level orchestration model might look like:

API Request
    ↓
Application Process
    ↓
Call System A
    ↓
Call System B
    ↓
Call System C
    ↓
Return Result

This becomes fragile when execution involves:

Call A
   ↓
WAIT
   ↓
Approval
   ↓
Resume
   ↓
Call B
   ↓
External callback
   ↓
Resume
   ↓
Verify outcome

If orchestration state exists only in process memory, Noema risks losing the execution lifecycle when:

* a worker crashes
* a deployment occurs
* a container restarts
* a network connection fails
* an external system responds asynchronously
* a human approval takes hours
* a retry occurs
* an execution step partially succeeds

Noema must not depend on a continuously running application process to remember where an Intent is in its execution lifecycle.

⸻

4. Decision

Noema will use durable workflow orchestration as the execution mechanism for long-running, asynchronous, retryable, or multi-step Intent execution.

The orchestration layer will provide durable execution semantics for workflows while preserving Noema’s canonical architectural boundaries.

The orchestration technology itself is an implementation concern and does not become part of the semantic definition of:

* Intent
* Trust
* Policy
* Capability
* Contract
* Outcome

The canonical architecture therefore becomes:

                 Noema
                   │
                   ▼
              Trusted Intent
                   │
                   ▼
             Action Graph
                   │
                   ▼
          Execution Planner
                   │
                   ▼
        Execution Contract
                   │
                   ▼
       Durable Workflow Layer
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
      Consumer A Consumer B Human
          │        │        │
          └────────┼────────┘
                   ▼
               Outcome
                   │
                   ▼
            Outcome Engine

⸻

5. Durable Execution Is Not Trust

The workflow orchestration layer must not become the Trust Engine.

The distinction remains:

Trust
  ↓
"May this Intent proceed?"

while durable orchestration answers:

Execution
  ↓
"How do we reliably carry out the authorized execution lifecycle?"

Therefore:

Trust ≠ Workflow Orchestration

A workflow engine must not independently decide that an Intent is trusted.

Trust remains governed by Noema’s deterministic Trust model and Trust State Machine.

⸻

6. Durable Execution Is Not Business Truth

The workflow engine must not become the system of record for enterprise business state.

For example:

Payment Provider
    owns payment state
CRM
    owns customer state
Banking System
    owns account state
Noema
    owns Intent / Trust / Execution coordination state

The workflow orchestration layer maintains execution state necessary to reliably coordinate the process.

It does not replace authoritative enterprise systems.

⸻

7. Why Durable Execution Is Required

Durable execution provides several properties that are directly relevant to Noema.

7.1 Persistence Across Failures

Execution should survive worker or process failure.

Workflow
   ↓
Worker crashes
   ↓
Workflow state persists
   ↓
Another worker resumes

⸻

7.2 Durable Waiting

Noema must support states such as:

WAITING_FOR_APPROVAL
WAITING_FOR_CONFIRMATION
WAITING_FOR_CAPABILITY
WAITING_FOR_RESOURCE
WAITING_FOR_EXTERNAL_EVENT

These should not require a process to remain alive while waiting.

⸻

7.3 Reliable Retries

Enterprise integrations frequently fail transiently.

Examples:

timeout
network failure
temporary service unavailable
rate limit
connection reset

Retry behavior should therefore be explicit and controlled rather than implemented ad hoc throughout application code.

⸻

7.4 Asynchronous Events

Execution may depend on events arriving later.

For example:

Execution
   ↓
External system
   ↓
processing
   ↓
callback/event
   ↓
resume workflow

The orchestration layer should support this lifecycle natively.

⸻

7.5 Long-Running Processes

Some Noema workflows may remain active for substantial periods.

Examples:

Approval required
     ↓
Human approves tomorrow
     ↓
Execution resumes

or:

External operation initiated
     ↓
Await completion
     ↓
Verify outcome

This requires durable state rather than ordinary request-scoped execution.

⸻

8. Workflow vs Action

Noema must distinguish between an Action and a Workflow.

An Action represents an executable operation.

A Workflow represents the durable orchestration of one or more operations and lifecycle events.

For example:

Action:
    Replace Card
Workflow:
    1. Validate eligibility
    2. Request approval if required
    3. Create replacement
    4. Wait for issuance
    5. Verify status
    6. Record outcome

Therefore:

Action ≠ Workflow

A workflow may contain multiple Actions.

⸻

9. Workflow vs Action Graph

The Action Graph represents the logical relationship between actions.

The durable workflow represents the operational execution of that graph.

Conceptually:

Action Graph
     │
     │ planning
     ▼
Execution Plan
     │
     │ materialization
     ▼
Durable Workflow
     │
     ├── Action A
     ├── Action B
     ├── Wait
     ├── Action C
     └── Verification

The Action Graph therefore remains a Noema semantic/architectural abstraction.

The workflow engine is an execution mechanism.

⸻

10. Workflow Determinism

Workflow orchestration must not undermine Noema’s deterministic boundaries.

In particular, workflow execution must not allow arbitrary nondeterministic model behavior to silently change an established execution contract.

The durable workflow should operate against explicit:

* Intent versions
* Execution Contracts
* Action identifiers
* inputs
* preconditions
* policies
* authorization decisions
* retry policies
* timeout policies
* compensation semantics
* outcome requirements

AI reasoning may occur where explicitly permitted, but the workflow itself must maintain deterministic execution semantics for consequential operations.

⸻

11. Execution Contract Boundary

The workflow layer must consume an explicit Execution Contract rather than arbitrary model output.

Conceptually:

Trusted Intent
      ↓
Planning
      ↓
Execution Contract
      ↓
Durable Workflow
      ↓
Capability Consumer

The workflow must not reinterpret the original natural-language request and decide independently what should happen.

This preserves the boundary:

Model
  ↓
Intent
  ↓
Trust
  ↓
Contract
  ↓
Workflow
  ↓
Execution

⸻

12. Idempotency

Durable workflows frequently retry operations.

Therefore Noema must treat idempotency as a first-class execution concern.

An operation such as:

Create Payment

must not accidentally execute twice merely because a workflow retried after an uncertain network response.

Execution Contracts should therefore define appropriate:

* idempotency keys
* operation identifiers
* retry semantics
* deduplication requirements

Conceptually:

Execution Contract
       │
       ├── operation_id
       ├── idempotency_key
       ├── retry_policy
       └── timeout_policy

⸻

13. Retries Must Be Semantically Safe

Not every operation can simply be retried.

For example:

GET account status

may be naturally retryable.

Whereas:

Transfer funds

requires stronger idempotency and execution guarantees.

Therefore retry behavior belongs to the Execution Contract and capability semantics rather than being globally assumed.

⸻

14. Timeouts

Workflows must explicitly represent timeout semantics.

Possible timeout categories include:

activity timeout
workflow timeout
approval timeout
external-system timeout
human-response timeout
execution-contract expiry

A timeout must produce an explicit state transition or outcome.

It must not silently disappear into application logs.

⸻

15. Cancellation

Noema must distinguish:

cancel requested

from:

execution cancelled

Cancellation may itself require coordination with an external system.

For example:

Workflow
   ↓
Cancel requested
   ↓
Consumer cancellation
   ↓
Cancellation confirmed

Therefore cancellation should be represented explicitly in the execution lifecycle.

⸻

16. Compensation

Some multi-step workflows cannot be rolled back transactionally across enterprise systems.

Example:

Action A → succeeded
Action B → succeeded
Action C → failed

Noema cannot assume that the entire sequence can simply be rolled back.

Where appropriate, the Execution Contract or workflow definition may specify compensating Actions.

For example:

A
↓
B
↓
C fails
↓
Compensate B
↓
Compensate A

Compensation must never be inferred automatically merely because a previous Action succeeded.

It must be explicitly defined by the applicable execution semantics.

⸻

17. Human Interaction

Durable workflows provide a natural mechanism for human-in-the-loop execution.

Example:

Workflow
   ↓
Trust evaluation
   ↓
WAITING_FOR_APPROVAL
   ↓
Human approval
   ↓
Workflow resumes
   ↓
Re-evaluation
   ↓
Execution

The approval itself remains an explicit Trust event.

The workflow engine is responsible for durable waiting and resumption.

⸻

18. Trust Re-Evaluation Before Execution

A workflow must not assume that a previously obtained Trust decision remains valid indefinitely.

For example:

T1:
READY
T2:
approval received
T3:
authorization revoked
T4:
workflow resumes

The workflow must therefore interact with the Trust State Machine according to Noema’s re-evaluation rules.

A durable workflow provides persistence.

It does not eliminate the need for Trust re-evaluation.

⸻

19. Execution Contract Expiration

Execution Contracts may have validity periods.

For example:

valid_until = 14:00

If execution resumes at:

14:30

the workflow must not assume that the original authorization remains valid.

The contract may require:

revalidation
      ↓
Trust Engine
      ↓
READY / WAITING / BLOCKED

before continuing.

⸻

20. External Events

Noema should support event-driven workflow progression.

Examples:

approval.granted
capability.available
payment.completed
resource.created
execution.completed
execution.failed

Events must be:

* authenticated where required
* correlated to the appropriate Intent/workflow
* validated
* idempotently processed
* recorded with provenance

An external event must not automatically become trusted merely because it exists.

⸻

21. Workflow State and Noema State

Workflow state and Noema Intent state should not be blindly collapsed into a single state model.

For example:

Intent State:
RESOLVED
Trust State:
READY
Execution State:
EXECUTING
Workflow State:
WAITING_FOR_PAYMENT_PROVIDER

Each represents a different dimension.

The architecture should preserve these distinctions.

⸻

22. Durable Execution and Execution Records

Every consequential workflow should produce an Execution Record containing sufficient information to reconstruct the execution lifecycle.

Conceptually:

Execution Record
├── intent_id
├── execution_id
├── contract_id
├── workflow_id
├── action_id
├── consumer
├── timestamps
├── state transitions
├── retries
├── external references
├── outcomes
└── provenance

The workflow engine may provide operational history, but Noema’s canonical Execution Record remains the authoritative Noema representation of execution history.

⸻

23. Workflow Engine as Infrastructure

The selected workflow technology should be treated as infrastructure.

Noema’s domain model must not become coupled to vendor-specific concepts unnecessarily.

The architecture should therefore provide a boundary such as:

Noema Execution Model
        │
        ▼
Workflow Orchestration Adapter
        │
        ▼
Workflow Engine

This allows the orchestration implementation to evolve without redefining Noema’s canonical semantics.

⸻

24. Candidate Technology

The preferred implementation technology for durable workflow orchestration is Temporal.

Temporal provides a durable execution model suited to workflows involving:

* long-running processes
* retries
* asynchronous events
* timers
* human interaction
* workflow recovery
* activity execution
* durable state

The adoption of Temporal is an implementation decision rather than a change to Noema’s canonical ontology.

The canonical architecture should therefore describe the capability as:

Durable Workflow Orchestration

while the implementation architecture may specify:

Temporal

⸻

25. Temporal’s Role

Where adopted, Temporal should sit primarily within the execution infrastructure layer.

Conceptually:

                    Noema
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
    Intent          Trust         Planning
       │              │              │
       └──────────────┼──────────────┘
                      ▼
              Execution Contract
                      │
                      ▼
                   Temporal
                      │
              ┌───────┼───────┐
              ▼       ▼       ▼
          Activity Activity Activity
              │       │       │
              ▼       ▼       ▼
          Enterprise Consumers

Temporal should orchestrate execution; it should not become the owner of Noema’s semantic authority model.

⸻

26. Technology Independence

Noema should avoid embedding Temporal-specific terminology into foundational semantic specifications unless necessary.

For example, the Canon should say:

durable workflow orchestration

rather than:

Temporal workflow

Architecture documentation may state:

Temporal is the selected implementation of durable workflow orchestration.

This preserves a clean separation between:

Canonical concept
        ↓
Architecture decision
        ↓
Implementation technology

⸻

27. Programming Language Alignment

The workflow orchestration technology should align with Noema’s broader implementation language strategy.

If Python is adopted as Noema’s primary application language, Python should be the default language for:

* Intent processing
* Context processing
* Validation
* Trust
* Policy evaluation
* Planning
* Outcome interpretation
* API services

Workflow workers may use the same language where practical.

The exact language/runtime matrix remains an implementation decision and should be established in the relevant architecture documentation.

⸻

28. Messaging Is Not the Same as Workflow

Noema must distinguish event transport from durable workflow orchestration.

Messaging answers:

How do we transport an event?

Workflow orchestration answers:

How do we durably coordinate a multi-step process over time?

Therefore:

Messaging ≠ Workflow

A messaging platform may transport:

approval.granted

while the workflow engine determines:

what should resume
what state should be restored
what activity should execute next
what retry policy applies

⸻

29. Events Remain First-Class

Adopting a workflow engine does not eliminate Noema’s event model.

Events remain necessary for:

* Trust state changes
* Intent changes
* external system notifications
* approvals
* capability availability
* execution outcomes
* provenance
* auditability

The workflow layer consumes and produces events as appropriate.

⸻

30. Workflow Boundaries

A workflow should begin only after the appropriate Noema prerequisites have been satisfied.

A conceptual boundary is:

Candidate Intent
      ↓
Resolution
      ↓
Validation
      ↓
Trust
      ↓
Planning
      ↓
Execution Contract
      ↓
DURABLE WORKFLOW

Noema should not create durable execution merely because a model proposed an Action.

⸻

31. Workflow Versioning

Long-running workflows introduce versioning concerns.

A workflow may remain active while the underlying application is deployed multiple times.

Therefore workflow definitions must support controlled version evolution.

Noema must be able to distinguish:

Workflow Definition Version

from:

Intent Version
Execution Contract Version
Policy Version

These versions may evolve independently.

Historical execution must remain reconstructible.

⸻

32. Deployment Independence

A deployment must not invalidate active workflows merely because application code has changed.

The architecture must support safe evolution of workflow definitions and workers.

This is particularly important for workflows that may remain active for long periods.

⸻

33. Observability

Durable workflows must integrate with Noema’s observability architecture.

Relevant telemetry includes:

* workflow execution duration
* activity duration
* retries
* failures
* timeout counts
* queue latency
* workflow state
* execution contract state
* consumer response
* outcome verification

Observability data should support operational diagnosis without becoming the canonical source of business truth.

⸻

34. Security

Workflow execution must preserve Noema’s authority boundaries.

Sensitive execution data must be protected.

The orchestration layer must not become an uncontrolled repository of credentials or authorization material.

Credentials should be managed through appropriate secret-management infrastructure.

Workflow inputs should contain only the information required to execute the workflow.

⸻

35. Failure Semantics

The workflow layer must distinguish at least:

Transient Failure
Permanent Failure
Timeout
Cancellation
Consumer Rejection
Unknown Outcome
Partial Execution
Compensation Required

These outcomes should flow into Noema’s Execution Record and Outcome Engine.

⸻

36. Unknown Execution Outcome

A particularly important case is:

Request sent
    ↓
Connection lost
    ↓
No response

Noema must not automatically conclude:

FAILED

because the external operation may have succeeded.

Instead:

UNKNOWN OUTCOME

may require:

Outcome Verification
        ↓
Authoritative Consumer
        ↓
CONFIRMED SUCCESS / CONFIRMED FAILURE / UNKNOWN

This is consistent with Noema’s fail-closed and authoritative-system principles.

⸻

37. Workflow and Outcome

The workflow’s responsibility is to coordinate execution.

The Outcome Engine determines what actually happened based on authoritative evidence.

Therefore:

Workflow completed
        ≠
Business outcome succeeded

A workflow may complete its orchestration successfully while the business operation itself fails.

Outcome verification remains a distinct Noema concern.

⸻

38. Decision

Noema will establish durable workflow orchestration as a required architectural capability for consequential, asynchronous, long-running, or multi-step execution.

Temporal is selected as the preferred implementation technology for this capability, subject to implementation validation and operational requirements.

The architectural abstraction remains:

Durable Workflow Orchestration

rather than:

Temporal

This preserves technology independence at the canonical layer while providing a concrete implementation direction.

⸻

39. Consequences

Positive

This decision provides:

* durable execution
* failure recovery
* explicit retries
* durable timers
* asynchronous execution
* human-in-the-loop workflows
* long-running process support
* execution observability
* clearer separation between planning and execution
* stronger execution reliability
* explicit workflow history

Negative

It introduces:

* additional infrastructure
* operational complexity
* workflow versioning requirements
* worker management
* new deployment concerns
* additional observability requirements
* more complex local development
* another architectural subsystem to operate

These costs are accepted because consequential Intent execution cannot safely depend on ephemeral application processes alone.

⸻

40. Alternatives Considered

40.1 Application-Level Orchestration

Example:

Python service
    ↓
database state
    ↓
background workers

Rejected as the primary orchestration model because durable execution semantics would need to be rebuilt across the application.

⸻

40.2 Message Queue Only

A message queue provides durable transport but does not by itself provide the complete semantics required for:

* long-running workflows
* durable timers
* workflow state
* retries
* human waiting
* workflow versioning
* orchestration history

Messaging may still be used alongside workflow orchestration.

⸻

40.3 Scheduled Jobs

Scheduled jobs are useful for periodic processing but are insufficient as the primary model for arbitrary multi-step Intent execution.

⸻

40.4 Database-Driven State Machines

A database-backed state machine can represent workflow state, but implementing durable retries, timers, concurrency, recovery, event correlation, and execution history independently would create substantial infrastructure complexity.

It may still be appropriate for specific Noema state machines where workflow orchestration is unnecessary.

⸻

40.5 Temporal

Temporal directly addresses durable execution and workflow orchestration requirements relevant to Noema.

It is therefore selected as the preferred implementation technology.

⸻

41. Architectural Invariants

The following invariants apply.

Invariant 1

Durable workflow orchestration does not replace Trust.

Invariant 2

A workflow may execute only against an explicit Execution Contract.

Invariant 3

Workflow state does not become enterprise business truth.

Invariant 4

Workflow execution does not imply successful business outcome.

Invariant 5

Retries must respect Action and Contract idempotency semantics.

Invariant 6

Unknown external outcomes must not be silently classified as failures.

Invariant 7

Material Trust conditions may require re-evaluation before execution continues.

Invariant 8

Human approval remains an explicit Trust event.

Invariant 9

Workflow technology must not redefine Noema’s canonical semantics.

Invariant 10

Long-running workflows must survive worker/process failure.

Invariant 11

Workflow definitions must be versionable.

Invariant 12

Enterprise systems remain authoritative for their respective business domains.

⸻

42. Relationship to Existing Canonical Concepts

This ADR establishes the relationship between durable execution and existing Noema abstractions:

Intent
  │
  ▼
Validation
  │
  ▼
Trust
  │
  ▼
Action Graph
  │
  ▼
Execution Planner
  │
  ▼
Execution Contract
  │
  ▼
Durable Workflow
  │
  ├── Action
  ├── Action
  ├── Wait
  ├── Event
  ├── Retry
  └── Verification
  │
  ▼
Outcome Engine
  │
  ▼
Execution Record

This ADR therefore connects the previously defined Intent, Trust, Planning, Contract, Execution, Outcome, and Provenance abstractions into a durable operational execution model.

⸻

43. Implementation Direction

The initial implementation should evaluate:

* Temporal Server / Temporal Cloud
* Python Temporal SDK
* workflow worker architecture
* activity worker architecture
* workflow persistence
* retry policies
* timeout policies
* idempotency strategy
* workflow versioning
* human approval integration
* event integration
* Execution Record integration
* observability integration
* secret management
* local development workflow
* production deployment model

These are implementation concerns and should be captured in architecture and implementation documentation rather than treated as foundational Canon.

⸻

44. Future Questions

The following remain open:

1. Temporal Cloud vs self-hosted Temporal.
2. Exact worker topology.
3. Whether all Actions become Temporal Activities.
4. Which operations should remain synchronous.
5. How Noema’s event bus interacts with Temporal Signals.
6. Exact workflow versioning strategy.
7. How execution leases interact with Trust expiration.
8. How workflow cancellation interacts with consumer-side cancellation.
9. How compensation is represented in Execution Contracts.
10. How workflow history maps into the canonical Execution Record.
11. How Python workers integrate with other language-specific consumers.
12. Which workloads require durable workflows versus ordinary request/response execution.

These questions should be resolved through subsequent ADRs or architecture specifications where necessary.

⸻

45. Canonical Summary

Noema requires a durable mechanism for carrying trusted Intent through consequential execution across time, failures, asynchronous events, human intervention, and multiple enterprise systems.

Therefore:

Trusted Intent
      ↓
Execution Contract
      ↓
Durable Workflow
      ↓
Enterprise Capability
      ↓
Outcome Verification

The canonical abstraction is durable workflow orchestration.

The preferred implementation technology is Temporal.

The governing principle is:

Noema should make execution durable without making the workflow engine the owner of intent, trust, authority, or enterprise business truth.