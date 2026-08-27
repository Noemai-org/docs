For user-model.md, the key distinction is between the human participant, their enterprise identity, their authority, and the Intent they express. The User Model should not become another identity/permissions document; those remain in 06-enterprise.

User Model

Status: Foundational
Version: 0.1
Domain: Product
Canonical Path: 08-product/user-model.md

⸻

1. Definition

The User Model defines how Noema represents and reasons about the people and machine principals that participate in Intent-driven enterprise execution.

The User Model answers:

“Who is participating in an interaction, what role do they have in the execution, and how does that identity relate to the Intent and Action being performed?”

A User is a participant in the Noema product.

A User is not merely:

* a chat user
* an account in Noema
* an email address
* an employee record
* an authenticated session
* a permission set

These concepts may contribute to a User’s execution context, but they are not interchangeable.

Conceptually:

Participant
     │
     ▼
Identity
     │
     ▼
User Context
     │
     ▼
Intent
     │
     ▼
Trust
     │
     ▼
Action
     │
     ▼
Execution

⸻

2. Purpose

The purpose of the User Model is to establish a consistent semantic representation of participants across:

* Interaction
* Intent
* Identity
* Context
* Authorization
* Trust
* Action
* Execution
* Human Intervention
* Auditability

The model must allow Noema to distinguish:

Who is speaking?

from:

What does this person want?

and:

What is this person authorized to do?

and:

What Action is Noema permitted to execute?

These are related questions but different concerns.

⸻

3. Core Principle

Identity, Intent, and Authority are separate dimensions.

For example:

User:
Jane Doe
Intent:
"Refund payment 123."
Identity:
Jane Doe / employee_id 4821
Authority:
Can refund payments up to $5,000
Requested Action:
refund_payment(123)
Trust:
ALLOW

The fact that Jane expressed an Intent does not establish that she is authorized to perform the resulting Action.

Therefore:

User ≠ Identity ≠ Authority ≠ Intent

⸻

4. User as Participant

A User participates in the Noema execution lifecycle.

A User may:

* express Intent
* provide Context
* answer clarification
* confirm an Action
* reject a proposal
* modify an Intent
* approve an Action
* receive an Outcome
* intervene in execution

The User is therefore an actor in the product lifecycle.

⸻

5. User vs Principal

The term Principal represents an entity that can be authenticated and authorized by an enterprise environment.

A Principal may be:

Human
Service
Application
Agent
Operator
System

A User generally represents the human-facing product participant.

Therefore:

Principal
    │
    ├── Human User
    ├── Service
    ├── Application
    └── System

Noema should not assume that every Principal is a User.

⸻

6. User vs Enterprise Identity

Noema may maintain a product-level representation of a User.

The enterprise may maintain the authoritative identity.

For example:

Noema User
    │
    ▼
Enterprise Identity
    │
    ▼
employee_id = 4821

Noema should reference enterprise identity rather than creating an independent identity that competes with the enterprise System of Record.

⸻

7. Identity Resolution

A User may be represented differently across systems.

Example:

Noema:
user_id = N-123
Identity Provider:
subject = auth0|84921
HRIS:
employee_id = 4821
CRM:
agent_id = 774

Noema may maintain mappings between these identifiers.

The mappings should preserve source and authority.

⸻

8. Identity Is Not Inferred Authority

Knowing who a User is does not establish what they may do.

For example:

Identity:
employee_id = 4821

does not imply:

Can refund payments

Authorization must be evaluated separately.

Conceptually:

Identity
   +
Requested Action
   +
Resource
   +
Scope
   +
Policy
   ↓
Authorization

⸻

9. User and Intent

A User is often the source of an Intent.

Example:

User
  ↓
"I need to cancel the subscription."
  ↓
Intent

The resulting Intent should preserve its initiating participant.

This relationship is important for:

* authorization
* auditability
* accountability
* clarification
* confirmation
* execution

⸻

10. User and Interaction

Interactions occur between Noema and participants.

Example:

User
  │
  ├── Interaction
  │
  ├── Interaction
  │
  └── Interaction

Multiple interactions may contribute to one Intent.

User:
"Refund my last payment."
Noema:
"Which payment?"
User:
"The $500 payment."
Noema:
"Confirm refund?"
User:
"Yes."

All three user interactions may belong to the same Intent lifecycle.

⸻

11. User and Context

User identity contributes to Context.

Relevant Context may include:

* authenticated identity
* organizational membership
* role
* location or scope where authorized
* active session
* delegated authority
* relevant prior interaction state

Context should be purpose-bound.

Noema should not treat every attribute associated with a User as relevant to every Intent.

⸻

12. User Context Is Not User Truth

A User Context may contain information associated with a participant.

It does not automatically establish enterprise Business State.

For example:

User Context:
customer_id = 123

does not by itself establish:

customer.status = ACTIVE

The latter should be grounded in the appropriate enterprise authority.

⸻

13. User and Trust

Trust evaluates whether Noema may safely proceed with the requested execution.

User-related Trust inputs may include:

* identity
* authentication
* authorization
* delegation
* organizational scope
* Intent
* risk
* confirmation
* relevant Policy

Conceptually:

User
  ↓
Identity
  ↓
Authorization
  ↓
Trust
  ↓
Action

Trust must not be reduced to identity alone.

⸻

14. Authentication

Authentication establishes that a participant is associated with a particular identity.

Conceptually:

Credential
    ↓
Authentication
    ↓
Identity

Authentication does not establish:

Authorization

and authorization does not automatically establish:

Permission for every Action

These remain separate decisions.

⸻

15. Authorization

Authorization determines whether a Principal may perform a specific operation within a defined scope.

Conceptually:

Principal
   +
Action
   +
Resource
   +
Scope
   +
Policy
   ↓
Authorization Decision

Noema may consume or evaluate enterprise authorization information but must not silently grant authority that the enterprise has not established.

⸻

16. User Roles

A User may have one or more enterprise roles.

Examples:

Employee
Manager
Finance Officer
Administrator
Support Agent
Approver
Operator

Roles may contribute to authorization.

However:

Role ≠ Permission

and:

Role ≠ Authority for Every Resource

Authorization remains contextual.

⸻

17. User Scope

A User may operate within one or more scopes.

Examples:

Tenant
Organization
Business Unit
Department
Region
Legal Entity
Resource Group

An Action may be permitted within one scope but prohibited within another.

Therefore:

User
  +
Scope
  +
Action

must be considered together.

⸻

18. User and Organizational Boundaries

Users may belong to organizational structures.

Example:

Organization
    │
    ├── Finance
    │     ├── Alice
    │     └── Bob
    │
    └── Operations
          └── Carol

Noema should preserve enterprise-defined organizational boundaries.

A User’s membership in one organizational unit must not automatically grant access to another.

⸻

19. User and Tenant Boundaries

In multi-tenant environments:

Tenant A
   └── User 123
Tenant B
   └── User 123

may contain overlapping local identifiers.

Tenant scope is therefore part of identity context.

A User identifier should not be treated as globally meaningful unless the authority explicitly defines it as such.

⸻

20. User and Delegation

A User may act on behalf of another Principal.

Example:

Executive
   ↓ delegates
Assistant
   ↓
Intent:
"Approve this invoice."

Delegation must be explicit.

Noema should preserve:

acting_principal
delegated_principal
delegation_scope
delegation_authority

where relevant.

⸻

21. Delegation Is Not Identity Substitution

If Alice acts on behalf of Bob:

Alice
  ↓
acting for Bob

Noema should not represent the interaction simply as:

Bob

The distinction matters for:

* authorization
* auditability
* accountability
* Policy
* approval

⸻

22. User and Approval

A User may act as an approver.

The approver may be different from the requester.

Requester
    ↓
Intent
    ↓
Approval Required
    ↓
Approver
    ↓
Approval
    ↓
Execution

The identity and authority of the approver must be independently established.

⸻

23. User and Confirmation

Confirmation is a statement by a User or authorized Principal that may satisfy a Policy requirement.

Example:

Noema:
"Transfer $20,000 to Account 123?"
User:
"Confirm."

The confirmation must be bound to the relevant Intent or Action.

A generic:

"Yes"

should not be treated as authorization outside its established context.

⸻

24. Confirmation Is Not Authorization

A User may confirm an Action they are not authorized to perform.

Therefore:

Confirmation

does not replace:

Authorization

The execution path remains:

Identity
   ↓
Authorization
   ↓
Confirmation where required
   ↓
Trust
   ↓
Execution

⸻

25. User and Ambiguity

A User may provide information required to resolve ambiguity.

Example:

User:
"Refund John's payment."
Noema:
"Which John?"
User:
"John Smith in Finance."

The second interaction provides additional Intent information.

It does not automatically establish that the identified John is the correct enterprise resource.

That identity must still be grounded where required.

⸻

26. User and Model Interpretation

The model may interpret User input.

For example:

User:
"Send the invoice to Sarah."
Model:
candidate recipient = Sarah Johnson

This is a candidate interpretation.

Noema must validate the relevant identity and authority before consequential execution.

Therefore:

User Input
   ↓
Model Interpretation
   ↓
Candidate Intent
   ↓
Noema Resolution
   ↓
Trust

⸻

27. User and Natural Language

Natural language is one way a User expresses Intent.

For example:

"Move my meeting to Friday."

The product should transform this into structured semantic state.

The User Model should not depend on natural language.

A User may express the same Intent through:

Chat
Voice
Button
Form
API
Workflow

⸻

28. User and Structured Interaction

A User may interact through structured controls.

Example:

Invoice:
INV-123
Action:
[Approve]

The interaction may produce the same semantic Action as:

"Approve invoice INV-123."

The User Model remains unchanged.

⸻

29. User and Machine Participants

Not every Intent originates from a human.

For example:

Scheduled Workflow
       ↓
Intent
       ↓
Noema

The initiating entity may be a:

Service
Application
Workflow
Agent
System

The User Model must therefore coexist with the broader Principal model.

⸻

30. User-Initiated vs System-Initiated Intent

Noema should distinguish:

Human-Initiated

from:

System-Initiated

Intent.

This distinction may affect:

* authorization
* Policy
* auditability
* interaction
* approval
* escalation

A system-generated Intent should not be represented as if a human explicitly requested it.

⸻

31. User and Action

A User may initiate an Action indirectly through Intent.

User
  ↓
Intent
  ↓
Action
  ↓
Execution

The User is not necessarily the technical caller of the enterprise API.

Noema may execute the Action using enterprise credentials or service identities while preserving the User as the originating principal.

⸻

32. Acting Principal vs Execution Principal

The principal requesting an Action and the technical identity executing the API call may differ.

Example:

Acting Principal:
Jane Doe
Execution Principal:
Noema Service Identity

The distinction is essential.

The service identity’s technical ability to call an API does not mean every User may use that capability.

Noema must enforce the User’s authority independently.

⸻

33. User and Service Identity

Enterprise systems may receive requests under Noema’s service identity.

Conceptually:

User
  ↓
Noema
  ↓
Service Identity
  ↓
Enterprise API

Noema must preserve the originating User and authorization context so that service credentials do not become an authority bypass.

⸻

34. User and Data Access

A User may be authorized to perform an Action without being authorized to view every piece of data involved in that Action.

Therefore:

Action Authorization

and:

Data Access

must remain independently evaluated where required.

A User’s ability to:

refund payment

does not necessarily imply the ability to view:

full customer profile

⸻

35. User and Minimum Necessary Context

Noema should use the minimum User information necessary for the current Intent and Action.

For example:

Refund Payment

may require:

employee identity
authorization scope
payment reference

It may not require unrelated personal attributes.

The User Model should therefore support data minimization.

⸻

36. User and Privacy

User information may be sensitive.

Noema should apply appropriate:

* access control
* minimization
* purpose limitation
* retention
* redaction
* audit
* isolation

User identity data should not be replicated across the platform without a legitimate purpose.

⸻

37. User and Auditability

Consequential actions should preserve sufficient attribution.

An audit record may need to establish:

who initiated the Intent
who confirmed it
who approved it
who intervened
what Action executed
under which authority
with which result

This allows Noema to reconstruct responsibility across the execution lifecycle.

⸻

38. User and Execution History

A User may have multiple historical Interactions and Executions.

History can provide useful Context.

However:

historical behavior ≠ authorization

and:

historical behavior ≠ current Intent

Past behavior may assist interpretation but must not silently override current explicit Intent or Policy.

⸻

39. User and Personalization

Noema may personalize interactions using appropriate User Context.

Examples:

preferred language
interface preference
notification preference
frequently used resources

Personalization must not alter consequential execution semantics without explicit Policy.

For example:

User usually refunds Payment A

must not cause:

"Refund my payment"

to automatically target Payment A when multiple payments are possible.

⸻

40. User and Historical Context

Historical Context may help resolve references such as:

"the account we discussed yesterday"

But historical Context should not automatically override authoritative enterprise data.

The resolution path remains:

Historical Context
      ↓
Candidate Reference
      ↓
Enterprise Grounding
      ↓
Resolved Resource

where required.

⸻

41. User and Risk

The same Action may have different risk depending on:

* User
* resource
* amount
* scope
* organizational authority
* history
* Policy

For example:

User A
→ transfer $1,000
→ allowed
User B
→ transfer $1,000
→ approval required

Risk is therefore evaluated in context rather than solely by Action type.

⸻

42. User and Trust State

A User does not have a permanent global Trust state.

Trust is contextual.

For example:

User
  +
Intent
  +
Action
  +
Resource
  +
Context
  +
Policy

produces a Trust evaluation.

The result applies to that execution context.

It should not automatically be generalized to every future Action.

⸻

43. User and Human Intervention

A User may become an intervention participant when Noema requires additional human action.

Examples:

Clarification
Approval
Conflict Resolution
Exception Handling
Recovery Decision

The role being performed should be explicit.

A requester acting as a requester is not automatically an authorized operator.

⸻

44. User Roles in an Execution

One execution may contain multiple User roles.

Example:

Requester
    ↓
Noema
    ↓
Approver
    ↓
Operator
    ↓
Noema

Noema should preserve these relationships.

Conceptually:

Execution
    │
    ├── initiated_by → Requester
    ├── approved_by → Approver
    └── intervened_by → Operator

⸻

45. User and Outcome

The User may receive the Outcome of an execution.

For example:

Execution:
SUCCEEDED
User:
"Your refund has been completed."

The communicated Outcome must correspond to established execution state.

A User-facing response is not itself the source of truth for the Outcome.

⸻

46. User and Failure

If an execution fails, Noema should communicate an appropriate failure state.

For example:

Action:
refund_payment
Outcome:
FAILED
User:
"The refund could not be completed."

If the outcome is unknown:

Outcome:
UNKNOWN

the User should not be told that the operation definitely failed or succeeded.

⸻

47. User and Cancellation

A User may request cancellation.

Cancellation must be evaluated against the current execution state.

For example:

Executing
   ↓
User requests cancellation
   ↓
Cancellation Policy
   ↓
Cancel / Reject / Continue

A User request cannot retroactively cancel an irreversible Action.

⸻

48. User and Modification

A User may modify an Intent before execution.

Example:

User:
"Transfer $5,000."
User:
"Actually, make it $7,000."

Noema must determine whether the second interaction modifies the existing Intent or creates a new one.

Any material modification may require renewed Trust evaluation.

⸻

49. User and Confirmation Expiry

A User’s confirmation may become stale when material execution conditions change.

For example:

User confirms transfer
        ↓
Account state changes
        ↓
Precondition changes
        ↓
Revalidation required

The User Model therefore cannot treat confirmation as a permanent property of the User.

Confirmation belongs to a particular Intent or Action context.

⸻

50. User and Account

A Noema product account may represent a User’s relationship with Noema.

It may contain:

noema_user_id
identity_reference
tenant
preferences
product configuration

The Noema account must not be confused with enterprise accounts.

For example:

Noema User Account

is distinct from:

Enterprise Bank Account

or:

Enterprise Customer Account

⸻

51. User and Enterprise Resource

A User may own, manage, access, or be associated with an enterprise Resource.

Examples:

Employee → Expense Account
Manager → Department
Customer → Subscription
Agent → Support Ticket

These relationships must be established by authoritative enterprise data or explicit trusted configuration.

Noema should not invent ownership relationships from conversational assumptions.

⸻

52. User and Resource Scope

A User’s authority may vary by Resource.

For example:

User:
Alice
Account A:
Can refund
Account B:
Cannot refund

Therefore:

User Permission

may require resource-specific evaluation.

⸻

53. User and Enterprise Identity Changes

Enterprise identity may change.

Examples:

Employee transferred
Role changed
Department changed
Account disabled
Employment terminated

Noema should rely on current authoritative identity and authorization information where required.

Historical execution records should preserve the identity context relevant at the time.

⸻

54. User and Identity Lifecycle

A User may move through states such as:

INVITED
ACTIVE
SUSPENDED
DEACTIVATED

These are product-level states.

Enterprise identity lifecycle may have different states.

Noema should not assume that product state and enterprise identity state are identical.

⸻

55. User State vs Execution State

User State describes the participant.

Execution State describes an execution.

They must remain distinct.

User:
ACTIVE
Execution:
FAILED

does not mean the User failed.

Likewise:

User:
SUSPENDED

does not retroactively change the historical execution result.

⸻

56. User Model

Conceptually:

User {
    user_id
    identity_reference
    tenant
    organizational_scope
    roles
    preferences
    lifecycle_state
    created_at
    updated_at
}

This is a semantic model rather than a requirement for a literal database schema.

Authorization, enterprise identity, and Business State remain separate concerns.

⸻

57. User Participation Model

Conceptually:

Participation {
    principal
    role
    scope
    intent
    interaction
    execution
    authority
}

Possible roles include:

REQUESTER
CONFIRMER
APPROVER
OPERATOR
INTERVENOR
OBSERVER

A single User may occupy different roles across different executions.

⸻

58. User Relationships

User
│
├── has → Identity
├── belongs_to → Tenant
├── belongs_to → Organization
├── participates_in → Interaction
├── expresses → Intent
├── provides → Context
├── confirms → Action
├── approves → Execution
├── intervenes_in → Execution
└── receives → Outcome

Principal
│
├── may_be → User
├── may_be → Service
├── may_be → Application
└── may_be → System

⸻

59. User Model and Trust

The User Model provides identity and participation context.

The Trust Model determines whether the requested execution may proceed.

Therefore:

User
  ↓
Identity / Context
  ↓
Trust
  ↓
Action

The User Model must not embed the final Trust decision as an intrinsic property of the User.

⸻

60. User Model and Enterprise Identity

The relationship is:

Noema User
      │
      ▼
Identity Reference
      │
      ▼
Enterprise Identity Authority

Noema may cache identity information where appropriate, but authoritative identity semantics remain with the enterprise authority.

⸻

61. User Model and Permissions

Permissions belong to the enterprise authorization model.

The User Model may reference the permissions relevant to a current execution.

It should not become a second independent permission system.

Therefore:

User
   ↓
Enterprise Authorization
   ↓
Permission

rather than:

User
   ↓
Noema Permission
   ↓
Enterprise Action

unless explicitly configured as an enterprise authorization layer.

⸻

62. User Model and Interaction Model

The Interaction Model describes the exchange.

The User Model describes the participant.

Therefore:

User
   ↓
Interaction
   ↓
Intent

Interaction is the event or exchange.

User is the participant.

Intent is the desired outcome.

These must remain distinct.

⸻

63. User Model and Intent Model

The Intent Model answers:

“What does the participant want to accomplish?”

The User Model answers:

“Who is participating in that Intent?”

Therefore:

User
    │
    └── expresses → Intent

The Intent should not contain the entire User object.

It should reference the relevant Principal or identity context.

⸻

64. User Model and Execution Model

The Execution Model answers:

“What happened while performing the Action?”

The User Model provides:

“Who initiated, confirmed, approved, or intervened in that execution?”

Therefore:

Execution
    │
    ├── initiated_by
    ├── confirmed_by
    ├── approved_by
    └── intervened_by

where applicable.

⸻

65. User Model and Auditability

Auditability requires attribution without requiring excessive personal data.

A consequential record should be able to establish:

Principal
Role
Action
Intent
Time
Authority
Outcome

The audit system should preserve the minimum information required to establish accountability and reconstruct execution.

⸻

66. User Model and Security Boundary

A User is a security-relevant participant but is not itself the security boundary.

Security decisions should consider:

Principal
Identity
Authentication
Authorization
Action
Resource
Scope
Policy
Risk

Noema must avoid simplifying this into:

User = Trusted

⸻

67. User Model and Product Experience

The User Model allows Noema to provide a coherent experience across different interaction surfaces.

The same User may interact through:

Chat
Dashboard
Mobile App
Voice
API-connected Application
Approval Interface

The underlying identity and execution relationship should remain consistent.

⸻

68. User Model and Product Personalization

Personalization may affect:

* presentation
* notification method
* language
* interface preferences
* non-consequential defaults

Personalization must not silently alter:

* authorization
* Policy
* Action parameters
* enterprise Business State
* Trust requirements

unless explicitly defined by Policy.

⸻

69. User Model and AI Personalization

Historical User behavior may help the model generate better candidates.

For example:

User frequently works with Account A.

This may inform candidate generation.

It must not become:

User probably means Account A.
Therefore execute.

Material ambiguity still requires deterministic resolution.

⸻

70. User Model and Accountability

Noema must preserve the distinction between:

requested_by

and:

executed_by

and:

approved_by

and:

intervened_by

These may all refer to different principals.

This distinction becomes particularly important in enterprise environments.

⸻

71. User Model and Non-Repudiation

For high-consequence operations, Noema may need sufficient evidence that a particular Principal performed a particular interaction or approval.

This may require:

* authenticated identity
* timestamp
* intent binding
* action binding
* confirmation
* authorization evidence

The exact requirements are determined by enterprise Policy and risk.

⸻

72. User Model and Revocation

Authorization can change after an Intent has been created.

For example:

Intent Created
     ↓
User Role Revoked
     ↓
Execution Attempted

Noema must evaluate whether the authorization remains valid under the applicable Policy.

Creation of an Intent does not necessarily grant permanent authority to execute it.

⸻

73. User Model and Long-Running Execution

A long-running execution may outlive the User’s current session.

For example:

User
  ↓
Intent
  ↓
Execution
  ↓
User disconnects
  ↓
Execution continues

Noema must preserve the originating Principal and authorization context required by the execution Policy.

Session termination should not automatically erase execution accountability.

⸻

74. User Model and Re-Authentication

Some Actions may require stronger authentication or renewed authentication.

For example:

Intent
  ↓
High-Risk Action
  ↓
Re-authentication Required
  ↓
User
  ↓
Trust
  ↓
Execute

The requirement is Action- and Policy-dependent.

It should not be assumed for every interaction.

⸻

75. User Model and Human Trust

Noema should not infer trustworthiness from behavioral familiarity alone.

Examples such as:

"She has done this before."
"He usually approves these."
"This is the same device."

do not automatically establish current authorization.

Current enterprise identity, authority, evidence, and Policy remain authoritative.

⸻

76. User Model Invariants

Invariant 1

A User is a product participant, not merely an authentication credential.

Invariant 2

User, Principal, Identity, Authority, and Intent are distinct concepts.

Invariant 3

Authentication does not establish authorization.

Invariant 4

Identity does not establish permission for every Action.

Invariant 5

A User expressing an Intent does not automatically authorize its execution.

Invariant 6

Noema must preserve the initiating Principal for consequential execution.

Invariant 7

Acting Principal and technical Execution Principal may differ and must remain distinguishable.

Invariant 8

Service credentials must not become an authority bypass for Users.

Invariant 9

Enterprise identity remains authoritative for enterprise identity semantics.

Invariant 10

Noema must not silently create a competing enterprise identity authority.

Invariant 11

Authorization must be evaluated in the relevant Action, Resource, Scope, and Policy context.

Invariant 12

User roles do not automatically imply unrestricted permissions.

Invariant 13

Tenant and organizational boundaries must be preserved.

Invariant 14

Delegation must be explicit and auditable.

Invariant 15

Delegated identity must not be represented as identity substitution.

Invariant 16

Requester, confirmer, approver, operator, and intervenor roles must remain distinguishable.

Invariant 17

Confirmation does not replace authorization.

Invariant 18

Confirmation must be bound to the relevant Intent or Action.

Invariant 19

Historical User behavior may assist interpretation but must not establish current authorization.

Invariant 20

Personalization must not silently alter consequential execution semantics.

Invariant 21

User-provided information does not automatically establish enterprise Business State.

Invariant 22

User identity does not establish ownership or access to an enterprise Resource without authoritative grounding.

Invariant 23

User State and Execution State must remain distinct.

Invariant 24

Product User State and enterprise identity lifecycle state must remain distinguishable.

Invariant 25

Authorization may change during the lifecycle of an Intent.

Invariant 26

Intent creation does not necessarily grant permanent execution authority.

Invariant 27

Long-running execution must preserve sufficient principal attribution even when the initiating session ends.

Invariant 28

Unknown or ambiguous identity must be resolved deterministically before consequential execution.

Invariant 29

Model-generated identity candidates are not authoritative identity.

Invariant 30

Noema must preserve sufficient identity and participation provenance for consequential auditability.

Invariant 31

User information should be minimized according to the purpose of the current execution.

Invariant 32

A User does not possess an intrinsic global Trust state; Trust is contextual to the requested execution.

Invariant 33

A User’s ability to perform one Action does not imply authority for another Action.

Invariant 34

Noema must distinguish who requested an Action from who technically executed it.

Invariant 35

The User Model must remain separate from the enterprise authorization system unless explicitly defined as part of that authority.

⸻

77. Final Definition

The User Model defines how Noema represents participants in Intent-driven enterprise execution and preserves the relationship between identity, participation, authority, and execution.

The fundamental relationship is:

USER / PRINCIPAL
        │
        ▼
     IDENTITY
        │
        ▼
    INTERACTION
        │
        ▼
      INTENT
        │
        ▼
 AUTHORIZATION
        │
        ▼
      TRUST
        │
        ▼
      ACTION
        │
        ▼
    EXECUTION
        │
        ▼
     OUTCOME

Multiple participants may enter the lifecycle:

Requester
    │
    ▼
  Intent
    │
    ▼
Approver
    │
    ▼
 Execution
    │
    ▼
 Operator
    │
    ▼
 Outcome

The architectural rule is:

Noema must know who is participating, what authority they possess, and what role they are performing without conflating identity with authorization, confirmation with authority, or historical behavior with current trust.