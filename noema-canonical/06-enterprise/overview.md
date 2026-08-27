Overview

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: 06-enterprise/overview.md

⸻

1. Definition

The Enterprise domain defines the boundary between Noema and the enterprise systems, organizational structures, identities, policies, resources, and business state that Noema operates against.

Noema is not the enterprise.

It does not become the system of record for:

customers
accounts
balances
employees
permissions
transactions
inventory
organizational structure

Instead, Noema operates across enterprise systems to turn human or agent Intent into controlled, auditable execution.

⸻

2. Purpose

The Enterprise domain answers a fundamental question:

What does Noema need to know about the enterprise, and what must remain owned and authoritative within the enterprise itself?

The domain establishes the conceptual boundaries around:

Identity
Organization
Business State
Resources
Data
Policies
Capabilities
Integrations
Audit

These concepts provide the environment in which Noema resolves Intent, evaluates Trust, and executes Actions.

⸻

3. The Enterprise–Noema Boundary

The fundamental architecture is:

┌──────────────────────────────────────────────┐
│                  ENTERPRISE                  │
│                                              │
│  Identity   Organization   Business State    │
│      │            │              │           │
│      └────────────┼──────────────┘           │
│                   │                          │
│              Enterprise APIs                │
│                   │                          │
└───────────────────┼──────────────────────────┘
                    │
              Enterprise Boundary
                    │
┌───────────────────┼──────────────────────────┐
│                   ▼                          │
│                  NOEMA                       │
│                                              │
│   Intent → Trust → Action → Execution       │
│                                              │
└───────────────────┼──────────────────────────┘
                    │
                    ▼
             Enterprise Systems

Noema sits between intent and enterprise state change.

⸻

4. Core Principle

The enterprise owns the business. Noema owns the execution journey.

The enterprise remains authoritative for:

identity
authorization
business state
resources
organizational structure
financial records
customer records
operational systems

Noema is authoritative for the execution journey it manages:

intent
intent resolution
trust evaluation
action selection
execution state
execution history
outcomes
intervention

This distinction is foundational.

⸻

5. Enterprise as External Authority

Enterprise systems provide authoritative facts.

For example:

Enterprise:
account.balance = $5,000

Noema may retrieve this fact.

It does not become the owner of:

account.balance

Likewise:

Enterprise:
Alice is a Finance Manager

Noema may use this information.

It does not become the authority that defines Alice’s employment status.

⸻

6. Enterprise State vs Noema State

The boundary can be represented as:

ENTERPRISE STATE
────────────────────────
Account
Balance
Customer
Employee
Permission
Invoice
Transaction
Inventory
        ↓ observed through integrations
NOEMA STATE
────────────────────────
Intent
Context
Trust
Action
Execution
Outcome
Intervention
Audit

Noema may maintain references and derived representations of enterprise state without replacing the enterprise systems of record.

⸻

7. Enterprise Domains

The Enterprise domain consists of several closely related concepts:

Identity
Organizational Boundaries
Business State
Data Boundaries
Resources
Capabilities
Policies
Integrations
Auditability

Together they describe the environment in which Noema operates.

⸻

8. Identity

Identity establishes:

who is acting
who is affected
who authorized an operation
which agent is acting
which service is executing

Identity is authoritative in the enterprise.

Noema consumes identity assertions and uses them as Trust inputs.

See:

identity.md

⸻

9. Organizational Boundaries

Organizational Boundaries establish where authority applies.

They may include:

business unit
department
team
project
legal entity
region
jurisdiction

An identity may be valid while still being outside the organizational scope required for a particular Action.

See:

organizational-boundaries.md

⸻

10. Business State

Business State represents the enterprise’s authoritative operational reality.

Examples:

account status
payment status
inventory
employee status
subscription
order
balance
transaction

Noema observes and changes Business State through authorized interfaces.

It should not create a competing system of record.

⸻

11. Data Boundaries

Data Boundaries determine:

what Noema may access
what it may process
what it may retain
what it may expose
what may reach a model
what may cross integrations

The guiding principle is:

Noema should have enough data to act safely, but not unrestricted access to enterprise data.

⸻

12. Resources

Resources are the enterprise objects upon which Actions operate.

Examples:

account
card
invoice
order
repository
employee record
subscription
device
document

A Resource generally belongs to or is managed by an enterprise system.

Noema references Resources and acts on them through Action Contracts.

⸻

13. Capabilities

Capabilities represent operations the enterprise exposes to Noema.

Examples:

refund_payment
freeze_card
create_invoice
grant_access
cancel_subscription
update_customer

A Capability describes what can be done.

It does not automatically establish:

who may do it
when it may be done
on which resources
under which conditions

Those concerns belong to authorization and Trust.

⸻

14. Policies

Enterprise Policies define constraints on operations.

Examples:

refunds above $5,000 require approval
only Finance Managers may approve invoices
customer accounts may not be closed while disputes are open

Policies provide the rules against which Trust evaluates an Action.

Noema may execute policies or consume policy decisions, but enterprise policy remains authoritative.

⸻

15. Integrations

Integrations connect Noema to enterprise systems.

They may expose:

APIs
events
webhooks
schemas
actions
queries

The integration boundary is where Noema’s execution model meets enterprise technology.

⸻

16. Auditability

Enterprise execution must be explainable.

Auditability allows the enterprise to determine:

what was requested
who requested it
what Noema understood
what evidence was used
which policy applied
what Trust decided
what Action was executed
what system executed it
what happened afterward

Auditability connects the Noema execution journey to enterprise accountability.

⸻

17. Enterprise Action Graph

The Enterprise Action Graph provides a structured representation of the enterprise environment.

Conceptually:

Identity
    │
    ├── belongs_to ──→ Organization
    │
    └── authorized_for ──→ Capability
                              │
                              ▼
                           Action
                              │
                              ▼
                           Resource
                              │
                              ▼
                       Business State

Additional relationships may connect:

Policy
Data
Events
Systems
Integrations

The graph allows Noema to reason over enterprise capabilities without hard-coding every workflow.

⸻

18. Enterprise Knowledge Sources

The Enterprise Action Graph may be constructed from multiple sources:

Enterprise APIs
API schemas
Documentation
Events
Workflow definitions
Policies
Human configuration
Identity systems
Organizational directories

No single source is necessarily sufficient.

The resulting graph should preserve provenance.

⸻

19. Enterprise Knowledge Is Not All Equal

Different enterprise sources have different authority.

For example:

Ledger
→ authoritative for balance
Identity Provider
→ authoritative for identity
HR system
→ authoritative for employment state
API documentation
→ descriptive of capability
Noema model inference
→ non-authoritative

Noema must distinguish source authority from semantic usefulness.

⸻

20. Enterprise Context

Enterprise Context is the subset of enterprise information relevant to a particular Intent.

For example:

Intent:
"Refund my last payment."
Relevant Context:
customer identity
candidate payment
payment status
refund policy
refund capability
authorization

Noema should not load the entire enterprise into Context.

⸻

21. Enterprise Context Is Dynamic

Enterprise state changes.

Therefore:

Context(t1)

may differ from:

Context(t2)

Noema must account for freshness when the difference could affect Trust or execution.

⸻

22. Enterprise State Is Not Noema Memory

Noema may remember:

an Intent occurred
an Action was attempted
an execution failed

It should not treat its stored snapshot of:

account.balance
employee.role
order.status

as permanently authoritative.

The enterprise system remains the source of truth.

⸻

23. Enterprise Authority

Authority can be represented as:

Enterprise System
      │
      ▼
Authoritative Fact
      │
      ▼
Noema Context
      │
      ▼
Trust Evaluation

Noema should preserve the distinction between:

observed fact

and:

model interpretation

⸻

24. Enterprise and Intent

The Enterprise domain supplies the information needed to turn an abstract Intent into an executable one.

Example:

User:
"Cancel my subscription."
Enterprise provides:
Identity
    ↓
Customer
Resources
    ↓
Subscriptions
Capability
    ↓
cancel_subscription
Policy
    ↓
cancellation rules
Business State
    ↓
subscription status

Noema then resolves the Intent against this environment.

⸻

25. Enterprise and Trust

Trust evaluates whether the resolved Action is sufficiently justified.

Relevant enterprise inputs may include:

identity
authorization
organization
resource state
policy
risk
evidence
capability

The Trust Engine produces a deterministic decision:

EXECUTE
CLARIFY
ESCALATE
REJECT

or another explicitly defined state.

⸻

26. Enterprise and Execution

Execution crosses from Noema into enterprise systems.

Noema
   │
   ▼
Action Contract
   │
   ▼
Integration
   │
   ▼
Enterprise Capability
   │
   ▼
Business State Change

The enterprise system remains responsible for the actual business-state mutation.

⸻

27. Enterprise and Outcome

After execution, Noema observes the enterprise result.

Example:

Action:
freeze_card
Enterprise:
card.status = FROZEN

Noema records:

Outcome:
SUCCESS

while the enterprise remains authoritative for the underlying card state.

⸻

28. Enterprise Events

Enterprise systems may emit events:

payment.completed
account.suspended
employee.terminated
order.shipped

These events may update Noema’s Context or execution state.

Events are evidence about enterprise state; they do not automatically become Noema-owned truth independent of their source.

⸻

29. Eventual Consistency

Enterprise systems may be eventually consistent.

Therefore Noema must account for cases where:

Action succeeded

but:

Business State

has not yet reflected the result.

Outcome verification should respect the consistency characteristics of the underlying enterprise system.

⸻

30. Enterprise Failure

Enterprise systems can fail independently of Noema.

Examples:

timeout
5xx
rate limit
network failure
provider outage
partial execution
unknown outcome

Noema must distinguish:

Action failed

from:

Action outcome unknown

This distinction is critical for safe recovery.

⸻

31. Unknown Enterprise State

A particularly important condition is:

Request sent
      ↓
network timeout
      ↓
No response

Noema must not assume:

FAILED

The enterprise may have successfully processed the Action.

The correct state may be:

OUTCOME_UNKNOWN

followed by reconciliation or verification.

⸻

32. Enterprise Idempotency

When Noema retries enterprise Actions, it must account for duplicate execution.

Where supported:

Action
   ↓
Idempotency Key
   ↓
Enterprise System

This allows Noema to retry safely without unintentionally repeating a business operation.

⸻

33. Enterprise Transactions

Noema should not assume that multi-system enterprise operations are atomic.

Example:

Payment
   ↓
Inventory
   ↓
Notification

A failure in one system may occur after another system has already changed state.

This is why:

compensation
reconciliation
postconditions
failure handling

are necessary.

⸻

34. Enterprise and Compensation

When an Action cannot be rolled back natively, Noema may need a compensating Action.

Example:

Create shipment
       ↓
Payment fails
       ↓
Cancel shipment

Compensation must itself satisfy:

authorization
policy
Trust
Action Contract

It is not an unrestricted rollback mechanism.

⸻

35. Enterprise Boundary and Determinism

The model may be probabilistic.

The enterprise execution boundary must not be.

Model
  ↓
candidate interpretation
  ↓
deterministic resolution
  ↓
deterministic Trust
  ↓
deterministic Action Contract
  ↓
enterprise execution

Noema must never cross the enterprise boundary based solely on model confidence.

⸻

36. Enterprise Boundary and Ambiguity

Ambiguity is particularly dangerous when it affects enterprise state.

Example:

"Refund John's payment."

If multiple Johns or multiple payments exist:

Model confidence = 94%

is not sufficient.

Noema should transition into a deterministic clarification state when policy requires disambiguation.

⸻

37. Enterprise Boundary and Least Privilege

Noema should use:

minimum required identity authority
minimum required data
minimum required capability
minimum required resource scope

for each execution.

This limits blast radius.

⸻

38. Enterprise Boundary and Human Intervention

Some operations should cross an additional human authorization boundary.

Intent
  ↓
Trust
  ↓
ESCALATE
  ↓
Human Approval
  ↓
Trust / Validation
  ↓
Execution

The approving identity and organizational authority must be preserved.

⸻

39. Enterprise Boundary and Security

Security is not a single layer.

The Enterprise domain intersects with:

Identity
Authorization
Data Boundaries
Organizational Boundaries
Trust
Integration Security
Auditability

Noema’s security model therefore emerges from the interaction of these boundaries.

⸻

40. Enterprise Boundary and Privacy

Noema may process sensitive enterprise information.

The architecture must therefore support:

data minimization
purpose limitation
tenant isolation
retention controls
redaction
access controls
regional constraints

Privacy requirements belong to enterprise policy and applicable governance.

⸻

41. Enterprise Boundary and Compliance

Some enterprise Actions are subject to regulatory or contractual constraints.

Noema should represent these constraints through:

Policy
Context
Evidence
Trust
Audit

rather than embedding jurisdiction-specific assumptions into the core execution engine.

⸻

42. Enterprise Boundary and Observability

Noema should expose enough execution telemetry to operate reliably without turning observability systems into uncontrolled copies of enterprise data.

Preferred:

execution_id
action_id
status
latency
provider
error_code
correlation_id

rather than indiscriminate raw enterprise payload logging.

⸻

43. Enterprise Boundary and Audit

The audit record should establish a causal chain:

Intent
   ↓
Resolution
   ↓
Context
   ↓
Trust
   ↓
Action
   ↓
Execution
   ↓
Enterprise Response
   ↓
Outcome

This provides the enterprise with an explainable execution history.

⸻

44. Enterprise Boundary and Human Accountability

Noema does not become the accountable human.

If:

Alice

authorizes:

Noema Agent

to perform:

refund_payment

the audit record should preserve:

Alice
→ delegated to Noema
→ Action
→ execution

The agent should not erase the principal.

⸻

45. Enterprise Boundary and Agents

Noema may operate alongside other enterprise agents.

For example:

User
 ↓
Noema
 ↓
Enterprise Agent
 ↓
Enterprise System

Each agent should remain identifiable.

Agent-to-agent delegation must not obscure:

originating principal
delegation chain
effective identity
authorization scope

⸻

46. Enterprise Boundary and External Systems

An enterprise may depend on:

payment providers
shipping providers
identity providers
CRM systems
ERP systems
communication systems

Noema must distinguish:

enterprise authority

from:

external provider authority

A provider response is evidence about an external system, not automatically the authoritative definition of enterprise Business State.

⸻

47. Enterprise Boundary and Integration Drift

Enterprise systems change.

Examples:

API versions
schemas
permissions
workflow rules
resource models

Noema’s representation of enterprise capabilities must therefore support versioning and validation.

⸻

48. Enterprise Boundary and Schema Drift

If an Action Contract expects:

customer_id
amount
currency

but the enterprise API changes:

customer_id
amount
currency_code

Noema must detect the incompatibility rather than silently guessing how to transform the request.

⸻

49. Enterprise Boundary and Capability Drift

A capability may be:

available
deprecated
disabled
restricted
changed

Noema should validate capability availability before consequential execution where required.

⸻

50. Enterprise Boundary and Policy Drift

Policies may change between:

Intent resolution

and:

Execution

For long-running or high-risk Actions, policy may need to be re-evaluated.

⸻

51. Enterprise Boundary and State Drift

Likewise:

Context at Trust time

may differ from:

Business State at execution time

For consequential operations, relevant Preconditions should be checked against current enterprise state.

⸻

52. Enterprise Boundary and Recovery

Recovery must operate within enterprise authority.

If an Action fails:

Noema
 ↓
Failure classification
 ↓
Retry / Compensate / Escalate / Reconcile

Noema must not perform arbitrary recovery mutations outside the Action model.

⸻

53. Enterprise Boundary and Reconciliation

When execution outcome is uncertain:

Noema
   ↓
Enterprise query
   ↓
Current Business State
   ↓
Reconciliation

This is preferable to guessing whether an Action succeeded.

⸻

54. Enterprise Boundary as a Contract

The Enterprise domain can therefore be understood as a contract:

Enterprise provides:
    identity
    organizational context
    resources
    capabilities
    policies
    business state
    events
    authoritative systems
Noema provides:
    intent resolution
    trust evaluation
    action orchestration
    execution state
    recovery
    auditability

The boundary defines the responsibilities of each side.

⸻

55. What Noema Must Not Become

The Enterprise domain establishes several explicit non-goals.

Noema should not become:

the enterprise identity provider
the enterprise HR system
the enterprise ledger
the enterprise CRM
the enterprise authorization source of truth
the enterprise database
the enterprise organizational directory

Noema may integrate with all of these.

It does not replace them.

⸻

56. What Noema Does Become

Noema becomes the system that understands and governs the journey from Intent to enterprise outcome.

Human Intent
     ↓
Intent Resolution
     ↓
Enterprise Context
     ↓
Trust
     ↓
Action
     ↓
Enterprise Execution
     ↓
Outcome
     ↓
Auditable History

This is the architectural wedge.

⸻

57. Enterprise Domain Relationships

The major relationships are:

Identity
   ↓
Organization
   ↓
Authorization
   ↓
Capability
   ↓
Action
   ↓
Resource
   ↓
Business State

with:

Policy ───────────────┐
Data Boundary ────────┤
Evidence ─────────────┤
Risk ─────────────────┤
                      ▼
                    Trust
                      │
                      ▼
                  Execution

And surrounding the entire journey:

                 Auditability
                       │
                       ▼
Intent → Trust → Action → Execution → Outcome

⸻

58. Canonical Enterprise Model

                         ENTERPRISE
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Identity ────── Organization ────── Policy             │
│      │                  │                │              │
│      │                  │                │              │
│      └────────────┬─────┴────────────────┘              │
│                   │                                     │
│                   ▼                                     │
│             Authorization                               │
│                   │                                     │
│                   ▼                                     │
│              Capabilities                               │
│                   │                                     │
│                   ▼                                     │
│               Resources                                 │
│                   │                                     │
│                   ▼                                     │
│             Business State                              │
│                                                         │
│  Data Boundaries ───── Integrations ───── Events        │
│                                                         │
└────────────────────────┬────────────────────────────────┘
                         │
                         │ Enterprise Boundary
                         ▼
┌─────────────────────────────────────────────────────────┐
│                         NOEMA                           │
│                                                         │
│     Intent → Context → Trust → Action → Execution       │
│                                      │                  │
│                                      ▼                  │
│                                   Outcome               │
│                                                         │
│                       Auditability                      │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
                    ENTERPRISE

⸻

59. Canonical Invariants

Invariant 1

The enterprise remains authoritative for Business State.

Invariant 2

The enterprise remains authoritative for Identity.

Invariant 3

The enterprise remains authoritative for organizational structure and authority.

Invariant 4

Noema owns the execution journey, not the enterprise’s underlying business systems.

Invariant 5

Noema must access enterprise data through explicit boundaries.

Invariant 6

Enterprise Context must be scoped to the current Intent and Action.

Invariant 7

Enterprise authority must not be inferred solely from model output.

Invariant 8

Identity, authorization, capability, resource, and policy are distinct concepts.

Invariant 9

Enterprise state observed by Noema may become stale and must be treated accordingly.

Invariant 10

Consequential execution must not proceed on unresolved ambiguity when policy requires deterministic resolution.

Invariant 11

Noema must distinguish failed execution from unknown execution outcome.

Invariant 12

Retries must account for enterprise idempotency and possible prior execution.

Invariant 13

Recovery and compensation must themselves remain within enterprise authorization and policy boundaries.

Invariant 14

Cross-organizational and cross-legal-entity operations must be explicitly evaluated.

Invariant 15

Enterprise events are evidence about enterprise state and must retain source provenance.

Invariant 16

Enterprise integrations must preserve sufficient identity, capability, schema, and version information to detect drift.

Invariant 17

Model-generated information is non-authoritative until validated through the appropriate deterministic mechanisms.

Invariant 18

Noema must not become a shadow system of record for enterprise Business State.

Invariant 19

Auditability must preserve the causal execution chain without requiring unrestricted retention of enterprise data.

Invariant 20

Noema must never bypass enterprise authority through inference, alternate integrations, cached state, or unauthorized identities.

⸻

60. Final Definition

The Enterprise domain defines the external world against which Noema operates: the identities, organizations, resources, capabilities, policies, data, integrations, and Business State that constitute an enterprise’s operational reality.

Noema sits at the boundary:

                ENTERPRISE
                    │
       authoritative business reality
                    │
                    ▼
                 NOEMA
                    │
       understands Intent
       establishes Context
       evaluates Trust
       constructs Actions
       governs Execution
       records Outcomes
                    │
                    ▼
                ENTERPRISE
                    │
            business state change

The key architectural distinction is:

The enterprise owns the state. Noema owns the journey.

That distinction should remain intact across every interface, integration, Action, Trust decision, and execution path.