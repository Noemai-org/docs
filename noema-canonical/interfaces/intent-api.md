Intent API

Status: Foundational
Version: 0.1
Domain: Interfaces
Canonical Path: interfaces/intent-api.md

⸻

1. Definition

The Intent API is the interface through which Noema receives, represents, resolves, clarifies, and exposes executable human intent.

It is the primary boundary between a user or upstream system and Noema’s Intent Engine.

User / System
      │
      ▼
  Intent API
      │
      ▼
 Intent Model
      │
      ▼
Intent Resolution
      │
      ▼
 Executable Intent
      │
      ▼
 Trust

The Intent API is therefore concerned with what the user wants to accomplish, not with directly performing the requested operation.

⸻

2. Purpose

The Intent API provides interfaces for:

* submitting intent
* identifying the actor
* attaching context
* representing ambiguity
* requesting clarification
* resolving intent
* inspecting intent state
* composing intents
* producing executable intent
* observing intent lifecycle
* associating intent with Actions
* preserving intent history

⸻

3. Core Principle

The Intent API accepts intent as an expression of desired outcome, not as an instruction to blindly execute an operation.

For example:

User:
"Replace my card."
        ↓
Intent API
        ↓
Intent:
replace_card
        ↓
Resolution
        ↓
Executable Intent
        ↓
Trust
        ↓
Action

The API does not treat the user’s initial utterance as sufficient authority to execute.

⸻

4. Intent Is Not Action

This distinction is foundational.

Intent:
"Replace my card."
Action:
issue_replacement_card(card_123)

Intent describes the desired objective.

Action describes the concrete operation required to achieve it.

⸻

5. Intent Is Not Execution

The Intent API ends conceptually before execution begins.

Intent API
    ↓
Intent
    ↓
Resolution
    ↓
Executable Intent
    ↓
Trust
    ↓
Action
    ↓
Execution API

The Intent API must not directly invoke enterprise side effects.

⸻

6. Intent Is Not Authorization

A user expressing an intent does not establish that the requested operation is authorized.

User intent
    ≠
Authorization

Authorization belongs to the Trust domain.

⸻

7. Intent Submission

Conceptually:

POST /intents

creates an Intent.

Example:

{
  "input": "Replace my card",
  "actor": {
    "id": "user_123"
  }
}

This is illustrative rather than a finalized wire schema.

⸻

8. Intent Identity

Every Intent receives a stable identity:

intent_id

Example:

int_01JXYZ...

The identity remains stable throughout the Intent lifecycle.

⸻

9. Intent Lifecycle

The canonical lifecycle is defined by 02-intent/intent-lifecycle.md.

Conceptually:

RECEIVED
   ↓
INTERPRETING
   ↓
RESOLVING
   ↓
CLARIFICATION_REQUIRED
   ↓
RESOLVED
   ↓
EXECUTABLE
   ↓
TRUST_EVALUATION

Not every Intent traverses every state.

⸻

10. Initial Intent

An initial Intent may contain little more than:

input
actor
timestamp
channel

For example:

{
  "input": "Send $500 to John",
  "actor_id": "user_123"
}

At this stage, Noema should not assume:

which John
which account
which currency
which transfer method

unless the context establishes those facts.

⸻

11. Intent Resolution

The Intent API may expose resolution state.

For example:

GET /intents/{intent_id}

could return:

{
  "id": "int_123",
  "state": "RESOLVING"
}

Resolution remains governed by the Intent domain.

⸻

12. Ambiguity

Ambiguity is a first-class state.

Example:

"Send $500 to John."

If the actor has:

John Smith
John Doe
John Williams

the Intent is not executable yet.

The correct transition is:

RESOLVING
    ↓
AMBIGUOUS
    ↓
CLARIFICATION_REQUIRED

⸻

13. Clarification

The API should support clarification as a continuation of the same Intent.

Conceptually:

POST /intents/{intent_id}/clarifications

User:

"John from accounting."

Noema then updates the existing Intent state.

It should not create an unrelated Intent unless the interaction explicitly represents a new request.

⸻

14. Clarification Is Not Failure

A clarification request means:

Noema cannot safely determine the intended execution path.

It does not mean:

the Intent failed.

This distinction is important.

⸻

15. Clarification Is Deterministic

The model may identify ambiguity probabilistically.

Noema’s response must be deterministic once the relevant evidence and policy are evaluated.

Model:
"John Smith is probably intended."
Noema:
"Two Johns match. Clarification required."

Noema must not turn probabilistic confidence into implicit authorization.

⸻

16. Confidence

The Intent API may expose confidence information where useful.

However:

Model confidence is evidence about interpretation, not permission to execute.

For example:

intent confidence = 0.92

does not imply:

execute = true

⸻

17. Confidence and Determinism

The conceptual boundary is:

Probabilistic Model
        ↓
Interpretation
        ↓
Evidence
        ↓
Deterministic Resolution Policy
        ↓
Resolved / Clarify / Reject

The Intent API exposes the resulting Intent state.

⸻

18. Intent Input

Intent input may originate from:

natural language
structured API request
voice transcription
UI interaction
event
workflow
another agent
enterprise application

The canonical Intent model should remain independent of the input channel.

⸻

19. Input vs Intent

The original input should be preserved separately from the resolved Intent.

Input:
"Can you move some money to John?"
Resolved Intent:
transfer_money

This allows Noema to retain provenance.

⸻

20. Intent Provenance

An Intent should be able to reference:

source
channel
actor
timestamp
original input
derived context
resolution evidence

This allows the Intent to be reconstructed and audited.

⸻

21. Actor

Every Intent should have an actor or initiating principal where applicable.

Intent
   ↓
Actor

The Actor model is defined in ontology/actor.md.

The Intent API should reference the Actor rather than redefine the Actor ontology.

⸻

22. Context

Intent interpretation may require Context.

Intent
   │
   ├── Actor
   ├── Context
   └── Input

Context may include:

current resource
conversation
session
location
time
enterprise state
previous decisions

The Context API remains responsible for context retrieval and management.

⸻

23. Intent and Context

Context helps answer:

"What does the user mean?"

It does not automatically answer:

"Is the user authorized?"

That remains a Trust concern.

⸻

24. Intent Composition

A single user request may contain multiple intents.

Example:

"Book me a flight to London and add it to my calendar."

This may resolve into:

Intent A:
book_flight
Intent B:
add_calendar_event

The Intent API should support composite intent structures.

⸻

25. Parent and Child Intents

Conceptually:

intent_100
   ├── intent_101
   └── intent_102

The parent represents the composite objective.

Children represent independently resolvable objectives.

⸻

26. Intent Relationships

Intent relationships may include:

contains
depends_on
precedes
conflicts_with
derived_from
clarifies
supersedes

These relationships should remain explicit.

⸻

27. Intent Supersession

A user may change their mind.

Example:

"Transfer $500."
then:
"Actually, make it $300."

The system should preserve the original Intent history while representing the updated Intent semantics.

Possible relationship:

intent_2
  supersedes
intent_1

⸻

28. Intent Cancellation

A user may cancel an unresolved Intent:

"Never mind."

The Intent API should be able to transition it to:

CANCELLED

This should not automatically cancel an already-executing Action unless the execution semantics explicitly connect the two.

⸻

29. Intent vs Action Cancellation

These are separate:

Intent cancellation
      ≠
Execution cancellation

An Intent may be cancelled before execution.

Once an Action has begun, cancellation becomes an Execution concern.

⸻

30. Intent Resolution Result

A resolved Intent should provide enough semantic structure to construct an Executable Intent.

Conceptually:

{
  "intent_id": "int_123",
  "state": "RESOLVED",
  "goal": "issue_replacement_card",
  "entities": {
    "card": "card_456"
  },
  "constraints": {},
  "context": {}
}

⸻

31. Resolved Does Not Mean Executable

This distinction is critical.

RESOLVED

means:

Noema understands the intended objective sufficiently.

It does not necessarily mean:

the requested operation is authorized and safe to perform.

Therefore:

RESOLVED
   ↓
Executable Intent
   ↓
Trust

⸻

32. Executable Intent

The Intent API may produce or reference an Executable Intent.

An Executable Intent contains sufficient semantic specificity to construct one or more Actions.

For example:

Goal:
replace card
Target:
card_456
Reason:
lost
Constraints:
standard replacement

⸻

33. Executable Intent Boundary

The transition should be explicit:

Ambiguous Intent
       ↓
Resolution
       ↓
Resolved Intent
       ↓
Executable Intent

Noema should not silently treat every resolved natural-language interpretation as executable.

⸻

34. Intent Constraints

Intent may contain constraints expressed by the user.

Example:

"Transfer $500 to John, but don't use my savings account."

The Intent may contain:

amount = 500
recipient = John
excluded_resource = savings_account

These constraints must survive resolution into the appropriate downstream model.

⸻

35. Intent vs Policy

A user constraint:

"Don't use my savings account."

is part of Intent.

An enterprise policy:

"Transfers above $10,000 require approval."

is Policy.

These are different semantic sources.

User Constraint
        +
Enterprise Policy
        ↓
Trust Evaluation

⸻

36. Intent Goal

Every Intent should ultimately identify the desired goal or outcome class.

Example:

goal:
replace_card

The goal is not necessarily identical to the Action used to accomplish it.

⸻

37. Intent Outcome

Intent may describe a desired Outcome.

Example:

"I want my card replaced."

Desired Outcome:

replacement_card_exists

The Action might be:

issue_replacement_card

This reinforces:

Intent → desired outcome
Action → mechanism

⸻

38. Intent and Outcome

The relationship is:

Intent
  ↓
Desired Outcome
  ↓
Action
  ↓
Execution
  ↓
Observed Outcome

The observed Outcome may differ from the desired Outcome.

⸻

39. Intent State

The API should expose canonical Intent state.

Possible states:

RECEIVED
INTERPRETING
RESOLVING
AMBIGUOUS
CLARIFICATION_REQUIRED
RESOLVED
EXECUTABLE
REJECTED
CANCELLED
SUPERSEDED

The exact state machine remains defined by intent-lifecycle.md.

⸻

40. Intent State Must Be Explicit

The API must not force consumers to infer state from missing fields.

Bad:

{
  "intent": {}
}

Better:

{
  "state": "CLARIFICATION_REQUIRED",
  "clarification": {}
}

State is part of the canonical contract.

⸻

41. Intent Rejection

Some intents should be rejected.

Examples:

unsupported capability
malformed request
impossible request
disallowed request
insufficient information

However, insufficient information should generally produce clarification rather than rejection when clarification can resolve the ambiguity.

⸻

42. Clarification vs Rejection

Ambiguous but resolvable
        ↓
CLARIFY
Impossible / unsupported / disallowed
        ↓
REJECT

This distinction should remain explicit.

⸻

43. Intent Expiration

Some intents may become stale.

Example:

"Use today's exchange rate to transfer..."

If the Intent remains unresolved for a long period, the relevant Context may need to be refreshed.

An Intent should therefore support expiration semantics where required.

⸻

44. Intent Context Refresh

Before resolving an Intent, Noema may refresh context.

Intent
   ↓
Context API
   ↓
Fresh context
   ↓
Resolution

This prevents stale information from becoming canonical interpretation.

⸻

45. Intent History

Intent history should preserve significant transitions.

Example:

RECEIVED
   ↓
RESOLVING
   ↓
CLARIFICATION_REQUIRED
   ↓
CLARIFIED
   ↓
RESOLVED
   ↓
EXECUTABLE

The API should allow this history to be reconstructed.

⸻

46. Intent Events

Intent state transitions may produce events:

intent.received
intent.resolving
intent.ambiguous
intent.clarification_required
intent.clarified
intent.resolved
intent.rejected
intent.cancelled
intent.superseded

These events belong to the Event Model but originate from Intent lifecycle changes.

⸻

47. Intent API and Event Model

The distinction:

Intent API
    ↓
request / inspect / mutate Intent lifecycle

while:

Event Model
    ↓
observe Intent lifecycle changes

⸻

48. Intent API and Context API

The Context API supplies information required to interpret intent.

Intent API
     │
     └──→ Context API

Context retrieval should not require the Intent API to duplicate the entire Context model.

⸻

49. Intent API and Action API

The relationship is:

Intent API
    ↓
Intent
    ↓
Executable Intent
    ↓
Action API

The Action API should not need to interpret raw user language.

⸻

50. Intent API and Trust Engine

The boundary is:

Intent
   ↓
Resolution
   ↓
Executable Intent
   ↓
Trust

Trust evaluates whether the executable intent can safely become executable Actions.

⸻

51. Intent API and Execution API

The Intent API should not directly control execution.

Intent API
    ↓
Executable Intent
    ↓
Trust
    ↓
Action
    ↓
Execution API

This separation prevents the conversational interface from becoming an execution bypass.

⸻

52. API Idempotency

Submitting the same Intent request multiple times should not unintentionally create duplicate logical Intents where idempotency is required.

Conceptually:

idempotency_key

can be associated with submission.

This is especially important for clients operating over unreliable networks.

⸻

53. Intent Correlation

Intent should be correlatable with downstream objects:

intent_id
   ↓
executable_intent_id
   ↓
action_id
   ↓
execution_id
   ↓
outcome_id

This creates an end-to-end execution journey.

⸻

54. Conversation Correlation

Multiple messages may contribute to the same Intent.

Conversation
   │
   ├── message 1
   ├── message 2
   ├── clarification
   └── message 3
          ↓
       Intent

The Intent should preserve this provenance without becoming identical to the conversation itself.

⸻

55. Intent from Another Agent

Intent need not originate from a human.

Another system may submit:

{
  "goal": "renew_card",
  "actor_id": "user_123"
}

The same semantic pipeline should apply:

Intent
 ↓
Resolution
 ↓
Executable Intent
 ↓
Trust

The source channel does not remove the need for Trust.

⸻

56. Structured Intent

The API may accept structured intent directly.

Example:

{
  "goal": "transfer_money",
  "amount": 500,
  "recipient": "user_456"
}

Structured input reduces interpretation ambiguity but does not eliminate:

authorization
policy
risk
preconditions

⸻

57. Natural Language Intent

Natural language may contain incomplete or ambiguous information.

Example:

"Send some money to John."

The Intent API should preserve uncertainty rather than inventing:

amount
recipient
account
currency

⸻

58. Model-Assisted Interpretation

An LLM or other model may assist in producing an Intent representation.

Conceptually:

Raw Input
   ↓
Model
   ↓
Candidate Intent
   ↓
Validation / Resolution
   ↓
Canonical Intent

The model is not itself the canonical source of truth.

⸻

59. Model Output Is Untrusted Input

Model-generated intent representations must be validated.

The API should not assume:

valid JSON
=
valid Intent

or:

high model confidence
=
safe interpretation

⸻

60. Intent Validation

Validation should establish:

required fields
schema correctness
entity references
constraint consistency
context validity
supported goal

before the Intent advances toward execution.

⸻

61. Intent Ambiguity

Ambiguity can occur at multiple levels:

goal ambiguity
entity ambiguity
parameter ambiguity
constraint ambiguity
context ambiguity
temporal ambiguity
authorization-relevant ambiguity

The API should preserve the specific ambiguity rather than simply returning:

"ambiguous": true

⸻

62. Clarification Question

A clarification should be targeted at the unresolved semantic dimension.

Bad:

"Can you clarify?"

Better:

"Which John do you mean: John Smith or John Doe?"

The clarification mechanism should minimize unnecessary user interaction.

⸻

63. Clarification Resolution

After the user responds:

"John Smith."

Noema should merge the clarification into the existing Intent context.

Intent
  +
Clarification
  ↓
Updated Intent
  ↓
Resolution

⸻

64. Multiple Clarifications

An Intent may require multiple clarification rounds.

Intent
 ↓
Clarification 1
 ↓
Clarification 2
 ↓
Clarification 3
 ↓
Resolved

Each clarification should remain part of the Intent history.

⸻

65. Clarification Limits

Repeated clarification may indicate:

insufficient context
poor integration
unsupported intent
contradictory constraints

The system should eventually transition to an appropriate terminal state rather than asking indefinitely.

⸻

66. Contradictory Intent

Example:

"Send $500, but don't send more than $300."

This is not merely ambiguity.

It is a constraint conflict.

The Intent API should expose:

CONFLICTING_CONSTRAINTS

or the equivalent canonical state rather than silently choosing one interpretation.

⸻

67. Intent Modification

Users may modify an unresolved Intent.

Example:

"Actually, make that $300."

The system should preserve the modification history.

Original:
$500
Updated:
$300

⸻

68. Intent Version

An Intent may therefore have semantic versions:

intent_123@1
intent_123@2
intent_123@3

The exact representation is implementation-specific, but historical resolution should remain reconstructable.

⸻

69. Intent Immutability

Past Intent states should generally be append-only from an audit perspective.

The current Intent may change.

The historical record should not be rewritten.

⸻

70. Intent Security

The API must protect:

intent data
actor identity
context
enterprise information
clarification history

Access should be scoped to the actor, tenant, and authorized system.

⸻

71. Intent Ownership

Noema owns the lifecycle of the Intent representation.

The enterprise may own:

accounts
customers
balances
permissions
resources

Noema should reference these rather than claiming ownership.

⸻

72. Intent Persistence

An Intent should remain durable across:

process restarts
model changes
clarification delays
execution delays
integration failures

The semantic journey must not exist solely in transient model context.

⸻

73. Intent Observability

Consumers should be able to determine:

what was requested
who requested it
how it was interpreted
what was ambiguous
what clarification occurred
what was resolved
what executable intent resulted
what Action was eventually produced

This is central to Noema’s auditability.

⸻

74. Intent API Operations

Conceptually, the API may support:

Create Intent
Get Intent
List Intents
Submit Clarification
Resolve Intent
Cancel Intent
Supersede Intent
Get Intent History
Get Intent Events
Get Executable Intent

Not every operation needs to be externally exposed.

⸻

75. Commands Are Requests

Operations such as:

resolve
cancel
supersede

are requests against the Intent lifecycle.

They must still respect canonical state transitions.

A caller cannot arbitrarily force:

CLARIFICATION_REQUIRED → EXECUTABLE

without satisfying the required resolution conditions.

⸻

76. Invalid State Transitions

For example:

REJECTED → EXECUTING

should be impossible through the Intent API.

Likewise:

CLARIFICATION_REQUIRED → EXECUTABLE

without the required clarification should be rejected.

⸻

77. Intent API and Deterministic State

The API should expose explicit states rather than relying on model interpretation at read time.

A client should receive:

{
  "state": "CLARIFICATION_REQUIRED"
}

rather than needing to ask an LLM:

"Is this intent ready?"

⸻

78. Intent API and Trust Boundary

The complete semantic path is:

             USER
              │
              ▼
         INTENT API
              │
              ▼
       INTENT RESOLUTION
              │
       ┌──────┴──────┐
       │             │
       ▼             ▼
   CLARIFY        RESOLVED
                     │
                     ▼
             EXECUTABLE INTENT
                     │
                     ▼
                  TRUST
                     │
                     ▼
                  ACTION
                     │
                     ▼
                EXECUTION

This separation is fundamental to Noema.

⸻

79. Canonical Intent Invariants

Invariant 1

An Intent represents a desired objective, not an execution command.

Invariant 2

Intent identity is distinct from Action identity.

Invariant 3

Intent resolution must preserve uncertainty where uncertainty remains.

Invariant 4

Ambiguity is a first-class state.

Invariant 5

Clarification is distinct from failure.

Invariant 6

Model confidence does not constitute authorization.

Invariant 7

Resolved does not automatically mean authorized.

Invariant 8

Resolved does not automatically mean executable.

Invariant 9

Intent constraints must remain distinguishable from enterprise Policy.

Invariant 10

Intent cancellation does not automatically cancel an executing Action.

Invariant 11

Intent history must remain reconstructable.

Invariant 12

Clarifications belong to the Intent lifecycle.

Invariant 13

Contradictory constraints must not be silently resolved by guessing.

Invariant 14

Model-generated Intent representations must be validated before becoming canonical.

Invariant 15

The Intent API must not directly bypass the Trust Engine.

Invariant 16

The Intent API must not directly execute external side effects.

Invariant 17

Intent state transitions must be explicit and deterministic.

Invariant 18

Original user input and canonical Intent representation must remain distinguishable.

Invariant 19

Intent must remain independent of the input channel.

Invariant 20

Historical Intent states must not be silently rewritten.

⸻

80. Canonical Mental Model

                         INPUT
                           │
                           ▼
                     ┌───────────┐
                     │ INTENT API│
                     └─────┬─────┘
                           │
                    Raw Intent
                           │
                           ▼
                     Interpretation
                           │
                           ▼
                       Resolution
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
             Ambiguous             Resolved
                │                     │
                ▼                     ▼
          Clarification        Executable Intent
                │                     │
                └──────────┬──────────┘
                           │
                           ▼
                         TRUST
                           │
                           ▼
                         ACTION
                           │
                           ▼
                       EXECUTION

⸻

81. Final Definition

The Intent API is Noema’s boundary for receiving and managing human or system intent. It preserves the distinction between raw input, interpreted intent, ambiguity, clarification, resolved intent, and executable intent while preventing probabilistic interpretation from becoming implicit authorization or execution.

The key architectural rule is:

The Intent API determines and exposes what the requester is trying to accomplish; it does not decide whether Noema is permitted to perform it, and it does not perform it.

And the critical transition is:

Intent
   ↓
Resolved Intent
   ↓
Executable Intent
   ↓
Trust
   ↓
Action
   ↓
Execution

That boundary is what keeps Noema from becoming “an LLM that calls APIs.”