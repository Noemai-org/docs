> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Trust API

Status: Foundational
Version: 0.1
Domain: Interfaces
Canonical Path: interfaces/trust-api.md

⸻

1. Definition

The Trust API is the interface through which Noema exposes the deterministic evaluation of whether an intended Action may proceed under the applicable evidence, authorization, policy, risk, and execution constraints.

The Trust API sits between Executable Intent / Actions and Execution.

Intent
  ↓
Resolution
  ↓
Executable Intent
  ↓
Action
  ↓
┌──────────────┐
│  Trust API   │
└──────┬───────┘
       ↓
Deterministic Trust Engine
       ↓
EXECUTE / CLARIFY / ESCALATE / REJECT
       ↓
Execution

The Trust API does not create intent, execute Actions, or own enterprise authorization systems.

It exposes Noema’s trust decision boundary.

⸻

2. Purpose

The Trust API provides a controlled interface for:

* submitting an Action for trust evaluation
* evaluating authorization
* evaluating applicable policy
* evaluating risk
* validating preconditions
* supplying and retrieving evidence
* determining whether ambiguity remains
* producing a deterministic trust decision
* explaining the basis of a decision
* recording trust state
* requesting reevaluation when relevant facts change

⸻

3. Core Principle

The Trust API answers whether an Action is sufficiently trusted to proceed; it does not decide what the user meant and it does not perform the Action.

The separation is:

Intent:
"What does the user want?"
Trust:
"May this concrete Action proceed?"
Execution:
"Perform the Action."

These must remain distinct.

⸻

4. Trust Is a Decision Boundary

The Trust API represents the point at which Noema moves from:

semantic interpretation

to:

controlled execution

Conceptually:

                 HUMAN / AGENT
                       │
                       ▼
                    INTENT
                       │
                       ▼
                  RESOLUTION
                       │
                       ▼
               EXECUTABLE INTENT
                       │
                       ▼
                     ACTION
                       │
                       ▼
              ┌────────────────┐
              │   TRUST API    │
              └───────┬────────┘
                       │
           ┌───────────┬───────────┐
           │           │           │
           ▼           ▼           ▼
      AUTHORIZATION   POLICY      RISK
           │           │           │
           └───────────┼───────────┘
                       ▼
                    DECISION
                       │
       ┌────────┬─────┬───────┬───────┐
       ▼        ▼       ▼       ▼       ▼
   EXECUTE   CLARIFY ESCALATE  REJECT

⸻

5. Trust Is Not Model Confidence

This distinction is foundational to Noema.

Model confidence:
"How confident is the model in its interpretation?"
Trust:
"Given the resolved Action, evidence, policy, authorization,
risk, and constraints, may this Action proceed?"

A model can be highly confident while Trust rejects the Action.

A model can be uncertain while Trust requires clarification.

confidence = 99%
trust = REJECT

is entirely valid.

⸻

6. Trust Is Deterministic

The model may be probabilistic.

The Trust Engine must not be.

Probabilistic:
candidate interpretation
        ↓
Deterministic:
Trust evaluation
        ↓
Decision:
EXECUTE
CLARIFY
ESCALATE
REJECT

Given the same relevant inputs, policy version, evidence, and evaluation configuration, the Trust decision should be reproducible.

⸻

7. Trust Decision

The Trust API should produce an explicit decision.

Canonical outcomes:

EXECUTE
CLARIFY
ESCALATE
REJECT

The exact decision taxonomy is governed by trust/trust-engine.md and trust/trust-model.md.

The critical invariant is:

There is no “probably execute” state.

⸻

8. Execute

EXECUTE

means the Trust Engine has determined that the Action satisfies the requirements necessary to proceed.

It does not mean the Action has already executed.

TRUST DECISION
     ↓
EXECUTE
     ↓
Execution

⸻

9. Clarify

CLARIFY

means the current information is insufficient to safely determine the execution path.

Example:

Action:
transfer_money(recipient=John)
Trust:
CLARIFY
Reason:
recipient identity unresolved

This should return the system to the appropriate Intent/clarification flow.

⸻

10. Escalate

ESCALATE

means the Action cannot be safely authorized through the current automated trust path and requires human or higher-level intervention.

Example:

transfer_amount = $250,000
Policy:
human approval required

The Trust decision is therefore:

ESCALATE

not:

EXECUTE

⸻

11. Reject

REJECT

means the Action must not proceed under the current conditions.

Examples:

authorization denied
policy violation
prohibited operation
failed mandatory precondition
risk threshold exceeded

⸻

12. Deterministic Trust Engine Request

Conceptually:

POST /trust/evaluations

An evaluation request might contain:

{
  "action_id": "act_123",
  "actor_id": "user_456",
  "context_id": "ctx_789"
}

This is illustrative rather than a finalized wire schema.

The request identifies what is being evaluated.

⸻

13. Deterministic Trust Engine Identity

Every evaluation should have a stable identity.

trust_evaluation_id

Example:

trst_01JXYZ...

This allows the decision and its supporting evidence to be independently referenced.

⸻

14. Deterministic Trust Engine Inputs

A Trust evaluation may depend on:

Action
Actor
Context
Authorization
Policy
Evidence
Risk
Preconditions
Constraints
Resource state
Integration state
Historical information

The Trust Engine combines these according to deterministic evaluation rules.

⸻

15. Trust Does Not Own Enterprise State

Noema may need to evaluate:

account.balance
user.role
transaction.limit
card.status

But the enterprise remains authoritative for that business state.

Enterprise:
authoritative account state
Noema:
trust decision based on observed state

⸻

16. Authorization

The Trust API may expose authorization evaluation.

For example:

Actor:
user_123
Action:
freeze_account(account_456)
Authorization:
AUTHORIZED

But Noema should not assume that an actor’s claim of authorization is sufficient.

Authorization must be grounded in trusted enterprise evidence or an explicitly configured authorization source.

⸻

17. Authorization vs Authentication

These remain distinct.

Authentication:
"Who is this actor?"
Authorization:
"May this actor perform this Action?"

The Trust API may consume authentication assertions but ultimately evaluates authorization as part of Trust.

⸻

18. Policy Evaluation

Trust incorporates applicable Policy.

Example:

Action:
transfer_money($15,000)
Policy:
Transfers > $10,000 require approval.

The resulting Trust decision may be:

ESCALATE

Policy evaluation is therefore a component of Trust, not a substitute for Trust.

⸻

19. Risk Evaluation

Risk may consider:

amount
actor
resource
Action type
history
velocity
environment
destination
anomaly signals

Example:

risk_score = HIGH

does not itself define the final decision.

Policy determines how risk affects the decision.

Risk
  +
Policy
  +
Authorization
  +
Evidence
      ↓
Trust Decision

⸻

20. Evidence

Trust decisions must be grounded in evidence.

Examples:

actor identity
authorization record
account state
policy version
resource state
provider confirmation
previous execution
human approval

The Evidence model is defined under trust/evidence.md.

⸻

21. Evidence Provenance

Evidence should identify its source where possible.

source
timestamp
subject
type
version
confidence / quality where applicable

This allows the Trust Engine to determine whether evidence is sufficiently authoritative.

⸻

22. Evidence Is Not Truth by Default

An input can exist without being trustworthy.

For example:

LLM:
"user is authorized"

is not equivalent to:

Enterprise authorization service:
"user_123 is authorized for operation X"

Trust must distinguish evidence sources by authority.

⸻

23. Evidence Freshness

Some evidence becomes stale.

Example:

Account balance:
$5,000 at 10:00
Transfer requested:
$4,500 at 10:30

The Trust Engine may need current account state before authorizing the Action.

Therefore Trust evaluations may require fresh evidence.

⸻

24. Preconditions

Trust should evaluate required Preconditions before allowing execution.

Example:

Action:
withdraw_money
Precondition:
account.status = ACTIVE

If:

account.status = FROZEN

the decision may be:

REJECT

or another canonical decision depending on policy.

⸻

25. Preconditions vs Policy

These are different.

Precondition:
account must be active.
Policy:
withdrawals above $10,000 require approval.

Both may influence Trust.

⸻

26. Constraints

Trust must evaluate constraints originating from:

user intent
Action Contract
enterprise Policy
resource state
system configuration

Conflicting constraints must not be silently resolved through guesswork.

⸻

27. Ambiguity

Trust may encounter ambiguity even after Intent resolution.

For example:

Intent resolved:
transfer to John Smith
Action:
transfer from account X

If the source account is ambiguous:

Trust:
CLARIFY

Trust therefore provides a deterministic mechanism for stopping unsafe execution when unresolved uncertainty remains.

⸻

28. Trust and Ambiguity

The relationship is:

Ambiguity
    ↓
Can it be deterministically resolved?
    │
    ├── Yes → continue
    │
    └── No → CLARIFY

Trust must not “average away” consequential ambiguity.

⸻

29. Trust State

The Trust evaluation itself has state.

Conceptually:

PENDING
    ↓
EVALUATING
    ↓
DECIDED

The resulting decision may be:

EXECUTE
CLARIFY
ESCALATE
REJECT

The canonical Trust State Machine remains defined in trust/trust-state-machine.md.

⸻

30. Trust Decision vs Trust State

These must not be conflated.

State:
DECIDED
Decision:
EXECUTE

versus:

State:
EVALUATING

where no final decision exists yet.

⸻

31. Trust Decision Immutability

Once a consequential Trust decision has been made, it should be preserved as historical fact.

If conditions change:

Old evaluation:
EXECUTE
New evaluation:
REJECT

the original decision should not be rewritten.

A new evaluation should be created.

⸻

32. Reevaluation

Trust may need to be reevaluated when relevant inputs change.

Examples:

policy changed
authorization changed
resource state changed
risk changed
evidence expired
integration changed
Action changed

Conceptually:

Evaluation 1
   ↓
context changed
   ↓
Evaluation 2

⸻

33. Deterministic Trust Engine Version

A decision should identify the relevant evaluation configuration.

Conceptually:

trust_model_version
policy_version
authorization_source_version

This allows historical decisions to remain explainable.

⸻

34. Decision Provenance

A Trust decision should be able to answer:

What Action was evaluated?
Who initiated it?
What policy applied?
What authorization evidence was used?
What risk factors were considered?
What evidence supported the decision?
Which Trust rules were applied?
What was the final decision?

⸻

35. Decision Explanation

The API should expose structured reasons.

Example:

{
  "decision": "REJECT",
  "reasons": [
    {
      "code": "POLICY_VIOLATION",
      "policy": "transfer_limit",
      "message": "Transfer exceeds permitted limit."
    }
  ]
}

The exact schema remains implementation-specific.

The important principle is that explanations should be grounded in the deterministic evaluation.

⸻

36. Explanation Is Not Chain-of-Thought

The Trust API should expose decision evidence and reason codes, not private model reasoning.

For example:

decision:
REJECT
reason:
POLICY_VIOLATION
evidence:
transfer_limit = $10,000
requested = $15,000

This is sufficient for auditability without exposing internal reasoning traces.

⸻

37. Trust and Action Contracts

The Trust API evaluates an Action against its contract.

Action Contract
       │
       ├── Preconditions
       ├── Constraints
       └── Postconditions

Trust primarily determines whether the Action can safely begin.

Execution subsequently determines whether its postconditions are actually achieved.

⸻

38. Trust Does Not Guarantee Outcome

An EXECUTE decision means:

"Execution is permitted."

It does not mean:

"The Action will succeed."

For example:

Trust:
EXECUTE
Execution:
FAILED — provider unavailable

Both states are valid.

⸻

39. Trust and Execution

The boundary is:

Trust
  ↓
EXECUTE
  ↓
Execution

The Execution Engine must not reinterpret an EXECUTE decision as permission to ignore Action Contracts or policy.

⸻

40. Trust and Integration

Trust may depend on integration information.

Example:

Provider:
available
Provider credential:
valid
Provider capability:
supports refund

This can contribute to the Trust decision.

But the Integration Model remains responsible for the actual provider interaction.

⸻

41. Trust and Context API

Trust may request context:

Trust API
    ↓
Context API
    ↓
Current enterprise state

Context is evidence used by Trust.

The Trust API should not duplicate the entire Context system.

⸻

42. Trust and Event Model

Trust decisions can emit events:

trust.evaluation_started
trust.evaluation_completed
trust.decision.execute
trust.decision.clarify
trust.decision.escalate
trust.decision.reject

Events allow other systems to observe the Trust lifecycle.

⸻

43. Trust Events Are Facts

An event such as:

trust.decision.execute

means:

A Trust decision of EXECUTE was recorded.

It does not itself execute the Action.

⸻

44. Trust API and Intent API

The relationship is:

Intent API
     ↓
Intent Resolution
     ↓
Executable Intent
     ↓
Trust API

The Trust API should not need to reinterpret the original natural-language request.

⸻

45. Trust API and Action API

The relationship is:

Action API
    ↓
Action
    ↓
Trust API
    ↓
Decision

The Trust API evaluates a concrete Action rather than raw conversational intent.

⸻

46. Trust API and Execution API

The relationship is:

Trust API
    ↓
EXECUTE
    ↓
Execution API
    ↓
Execution

The Execution API should require an appropriate Trust decision before consequential execution.

⸻

47. Trust API and Human Intervention

Some decisions require a human.

Trust:
ESCALATE
      ↓
Human approval
      ↓
Trust reevaluation / approval transition
      ↓
EXECUTE

The exact mechanism belongs to the Human Intervention and Trust state models.

⸻

48. Trust API Commands

Conceptually, the API may support:

Evaluate Action
Get Evaluation
Get Decision
Get Decision Evidence
Get Decision History
Request Reevaluation
Submit Approval

Not every operation needs to be externally exposed.

⸻

49. Trust API Read Operations

Consumers may need to inspect:

evaluation state
decision
reasons
evidence references
policy references
authorization result
risk result
timestamps
versions

Sensitive evidence should be subject to access controls.

⸻

50. Trust API Write Operations

Write operations should be tightly controlled.

Examples:

submit evaluation
request reevaluation
submit authorized human approval

Clients should not be able to directly set:

decision = EXECUTE

The Trust Engine must produce the decision.

⸻

51. No Caller-Provided Trust

This is a critical invariant.

A request such as:

{
  "action_id": "act_123",
  "trust": "approved"
}

must not be accepted as authoritative merely because the caller supplied it.

Trust must be evaluated from trusted inputs.

⸻

52. Trust Decision Token

For downstream execution, Noema may issue a signed or otherwise verifiable authorization artifact.

Conceptually:

Trust Decision
      ↓
Execution Authorization
      ↓
Execution API

Such an artifact could contain:

evaluation_id
action_id
decision
policy_version
expiration
scope

The exact mechanism is an implementation decision.

⸻

53. Decision Expiration

Some Trust decisions should be time-bound.

For example:

EXECUTE
valid_until = 13:45

If the Action has not begun before relevant evidence becomes stale, Trust may require reevaluation.

⸻

54. One Decision, One Action

Trust decisions should be scoped appropriately.

A decision authorizing:

freeze_account(account_123)

must not automatically authorize:

close_account(account_123)

even if both Actions involve the same resource.

⸻

55. Scope

A Trust decision should clearly identify its scope:

actor
Action
resource
tenant
environment
time
policy context

This prevents authorization from leaking between unrelated executions.

⸻

56. Trust and Delegation

When an agent acts on behalf of a human:

Human
  ↓
Agent
  ↓
Noema

Trust must preserve the distinction between:

initiating actor
delegated executor

The agent’s ability to call Noema does not automatically grant it authority to perform every Action available to the human.

⸻

57. Trust and Agentic Systems

An AI agent may propose:

Action:
send_invoice(customer_123)

The Trust API determines:

May this Action proceed?

The agent does not determine the final Trust decision.

This is central to Noema’s role as a control plane for agentic enterprise execution.

⸻

58. Trust and Model Substitution

Trust should remain stable when the underlying model changes.

Model A
   ↓
Intent
Model B
   ↓
Intent
Same Trust Engine
   ↓
Same policy semantics

Changing the LLM should not silently change enterprise authorization rules.

⸻

59. Trust and Deterministic Clarification

Suppose:

Model confidence:
92%

but two possible targets remain.

Trust should produce:

CLARIFY

rather than:

EXECUTE

This embodies Noema’s central principle:

Uncertainty becomes an explicit execution state rather than an invitation to guess.

⸻

60. Trust Failure

The Trust Engine itself may fail.

Examples:

authorization provider unavailable
policy unavailable
required evidence unavailable
evaluation service unavailable

This is distinct from:

REJECT

A system failure does not necessarily mean the Action is forbidden.

Depending on policy, the result may be:

retry
escalate
hold
fail closed

⸻

61. Fail Closed

For high-risk operations, inability to establish required Trust may result in:

REJECT

or:

ESCALATE

rather than execution.

The appropriate behavior is determined by Policy and Risk.

⸻

62. Trust Audit Trail

Every consequential Trust evaluation should be auditable.

Conceptually:

Evaluation
    │
    ├── Action
    ├── Actor
    ├── Context
    ├── Evidence
    ├── Policy
    ├── Authorization
    ├── Risk
    ├── Decision
    └── Timestamp

⸻

63. Trust API Security

The Trust API is a high-value control boundary.

Access should therefore require appropriate:

authentication
authorization
tenant isolation
scope enforcement
audit logging
rate limiting
input validation

A consumer must not be able to manipulate the trust state of another tenant’s Action.

⸻

64. Trust API Availability

The Trust API sits on the critical path of consequential execution.

However:

Availability must not be achieved by weakening Trust guarantees.

If Trust cannot safely evaluate an Action, Noema should not silently proceed merely to maintain uptime.

⸻

65. Trust API Versioning

The interface should be versioned independently from:

LLM version
Trust Engine implementation
Policy version
Integration version

This allows each layer to evolve independently.

⸻

66. Backward Compatibility

Existing consumers should continue to receive canonical Trust concepts even as internal evaluation mechanisms evolve.

For example:

Trust Engine v2

may internally introduce additional risk models without requiring consumers to understand those implementation details.

⸻

67. Deterministic Trust Engine Example

Consider:

User:
"Transfer $5,000 to John."

After resolution:

Action:
transfer_money(
    source=account_123,
    destination=account_456,
    amount=5000
)

Trust evaluates:

Actor:
authorized
Policy:
limit = $10,000
Account:
ACTIVE
Risk:
LOW
Evidence:
fresh

Decision:

EXECUTE

The Execution API may now proceed.

⸻

68. Trust Rejection Example

Action:
transfer_money($20,000)

Policy:

maximum automated transfer = $10,000

Decision:

REJECT

No execution should be created as though the Action were approved.

⸻

69. Trust Escalation Example

Action:
transfer_money($20,000)

Policy:

amount > $10,000 requires manager approval

Decision:

ESCALATE

After approval, Trust may reevaluate the Action.

⸻

70. Trust Clarification Example

Action:
transfer_money(
    recipient = unresolved "John"
)

Decision:

CLARIFY

The Intent system obtains clarification.

The Action may then be reconstructed or updated.

Trust evaluates the resulting Action again.

⸻

71. Trust Invariants

Invariant 1

Trust evaluates whether an Action may proceed; it does not interpret raw user intent.

Invariant 2

Trust decisions are deterministic.

Invariant 3

Model confidence is not authorization.

Invariant 4

Trust cannot be supplied authoritatively by the caller.

Invariant 5

EXECUTE means permitted to execute, not successfully executed.

Invariant 6

Trust must not directly perform external side effects.

Invariant 7

Trust decisions must be based on identifiable evidence.

Invariant 8

Evidence provenance must be preserved.

Invariant 9

Stale evidence must not silently be treated as current evidence when freshness matters.

Invariant 10

Authorization and authentication remain distinct.

Invariant 11

Policy and authorization remain distinct inputs to Trust.

Invariant 12

Risk influences Trust according to explicit policy rather than arbitrary model judgment.

Invariant 13

Unresolved consequential ambiguity must not be converted into EXECUTE.

Invariant 14

Trust decisions must be appropriately scoped to the Action, actor, tenant, resource, and relevant context.

Invariant 15

A Trust decision must be historically reconstructable.

Invariant 16

Changing the underlying model must not silently change authorization semantics.

Invariant 17

A changed consequential input should trigger a new evaluation where required.

Invariant 18

Historical Trust decisions must not be overwritten.

Invariant 19

Trust failure must not silently become authorization.

Invariant 20

Clients cannot directly mutate Trust decisions.

⸻

72. Canonical Trust Flow

                      ACTION
                        │
                        ▼
                 ┌──────────────┐
                 │   TRUST API  │
                 └──────┬───────┘
                        │
        ┌─────────────┬──────────────┐
        ▼             ▼              ▼
  Authorization      Policy          Risk
        │             │              │
        └───────────┬──────────────┘
                        ▼
                     Evidence
                        │
                        ▼
                   Preconditions
                        │
                        ▼
               Deterministic Evaluation
                        │
       ┌───────┬───────┬───────┬───────┐
       ▼       ▼       ▼       ▼       ▼
    EXECUTE  CLARIFY ESCALATE  REJECT
       │       │       │       │
       ▼       ▼       ▼       ▼
   Execution  Intent  Human   End
              Flow    Flow

⸻

73. Relationship to the Trust Domain

The Interfaces layer exposes the Trust domain; it does not redefine it.

trust/
│
├── ambiguity.md
├── authorization.md
├── determinism.md
├── evidence.md
├── policy-evaluation.md
├── risk.md
├── trust-engine.md
├── trust-model.md
├── trust-state-machine.md
└── validation.md

interfaces/trust-api.md answers:

How do systems interact with the Trust Engine?

The trust documents answer:

What does Trust mean and how does it work?

⸻

74. Relationship to the Rest of Noema

Intent API
     │
     ▼
Executable Intent
     │
     ▼
Action API
     │
     ▼
┌─────────────────┐
│    TRUST API    │
└────────┬────────┘
         │
    ┌────┴────┐
    │          │
    ▼          ▼
 Context    Policy
    │          │
    └────┬────┘
         ▼
      Decision
      (EXECUTE / CLARIFY / ESCALATE / REJECT)
         │ (EXECUTE)
         ▼
 Execution API
         │
         ▼
 Integration Model
         │
         ▼
 Enterprise System

⸻

75. The Trust Boundary

The most important architectural property of the Trust API is that it creates a hard boundary between:

"What should happen?"

and:

"Are we allowed to make it happen?"

The first belongs to Intent and Action.

The second belongs to Trust.

Only after Trust permits the Action does execution become eligible.

⸻

76. Final Definition

The Trust API is Noema’s deterministic control boundary for evaluating whether a concrete Action may proceed. It combines authorization, policy, risk, evidence, context, constraints, and validation to produce an explicit decision—EXECUTE, CLARIFY, ESCALATE, or REJECT—without directly executing the Action or treating probabilistic model confidence as permission.

The core Noema chain is therefore:

USER INTENT
    ↓
INTENT RESOLUTION
    ↓
EXECUTABLE INTENT
    ↓
ACTION
    ↓
┌─────────────────────┐
│      TRUST API      │
│                     │
│ Authorization       │
│ Policy              │
│ Risk                │
│ Evidence            │
│ Preconditions       │
│ Determinism         │
└──────────┬──────────┘
           │
     ┌─────┼──────────────┐
     ▼     ▼              ▼
 EXECUTE CLARIFY       ESCALATE
     │     │              │
     │     ▼              ▼
     │  Resolve        Human
     │  Intent        Intervention
     │     │              │
     └─────┴──────┬───────┘
                  ▼
              EXECUTION

Trust is the gate between understanding an intention and allowing the world to be changed.