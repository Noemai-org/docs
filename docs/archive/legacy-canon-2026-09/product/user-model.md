> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

# User Model

Status: Foundational
Version: 0.2
Domain: Product
Canonical Path: product/user-model.md

⸻

## 1. Definition

The User Model defines how Noema represents and reasons about the people and machine principals that participate in Intent-driven enterprise execution.

The User Model answers:

“Who is participating in an interaction, what role do they have in the execution, and how does that identity relate to the Intent, authority, Action, and execution being performed?”

A User is a participant in the Noema product.

A User is not merely:

* a chat user
* an account in Noema
* an email address
* an employee record
* an authenticated session
* a permission set
* a service credential

These concepts may contribute to a User’s execution context, but they are not interchangeable.

Conceptually:

Participant
     │
     ▼
Principal
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
Authorization
     │
     ▼
Trust
     │
     ▼
Action
     │
     ▼
Execution

The User Model provides the participant and attribution semantics required by this lifecycle.

⸻

## 2. Purpose

The purpose of the User Model is to establish a consistent semantic representation of participants across:

* Interaction
* Intent
* Context
* State
* Identity
* Authorization
* Trust
* Action
* Execution
* Human Intervention
* Auditability

The model must allow Noema to distinguish:

Who is participating?

from:

What does this participant want?

and:

What Principal is acting?

and:

What authority does that Principal possess?

and:

What Action is Noema permitted to execute?

and:

What technical identity actually executes the enterprise operation?

These are related questions but different concerns.

⸻

## 3. Core Principle

Identity, Intent, Authority, and Trust are separate dimensions.

For example:

User:
Jane Doe

Intent:
"Refund payment 123."

Identity:
Jane Doe / employee_id 4821

Authority:
May refund qualifying payments within an enterprise-defined scope

Requested Action:
refund_payment(123)

Trust:
ALLOW

The fact that Jane expressed an Intent does not establish that she is authorized to perform the resulting Action.

Likewise, the fact that a Noema service identity can technically invoke an enterprise capability does not establish that Jane may use that capability.

Therefore:

User ≠ Principal ≠ Identity ≠ Authority ≠ Intent ≠ Trust

⸻

## 4. User as Participant

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

A User may occupy different roles in different executions.

For example:

User
  ├── requester in Execution A
  ├── confirmer in Execution B
  └── approver in Execution C

Role is contextual to participation and must not be treated as a permanent property that determines all authority.

⸻

## 5. User vs Principal

The term Principal represents an entity that can be authenticated, attributed, and potentially authorized by an enterprise environment.

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
    ├── Agent
    └── System

Noema must not assume that every Principal is a User.

Conversely, when a User initiates an Intent, Noema must preserve the underlying Principal relationship required for authorization and auditability.

⸻

## 6. User vs Enterprise Identity

Noema may maintain a product-level representation of a User.

The enterprise may maintain the authoritative identity.

For example:

Noema User
    │
    ▼
Identity Reference
    │
    ▼
Enterprise Identity
    │
    ▼
employee_id = 4821

Noema should reference enterprise identity rather than creating an independent identity authority that competes with the enterprise System of Record.

Noema may maintain mappings and cached representations where required for execution, but authoritative enterprise identity semantics remain with the relevant identity authority.

⸻

## 7. Identity Resolution

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

Mappings must preserve:

* source
* authority
* tenant
* scope
* validity
* provenance

An identifier discovered through model interpretation is not authoritative identity.

Identity resolution must therefore distinguish:

Candidate Identity

from:

Verified Identity.

⸻

## 8. Identity Is Not Inferred Authority

Knowing who a User is does not establish what they may do.

For example:

Identity:
employee_id = 4821

does not imply:

Can refund payments.

Authorization must be evaluated separately.

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
   +
Current State
   ↓
Authorization

Business authorization may additionally depend on the fully resolved enterprise state of the target operation.

Technical capability access is therefore not equivalent to business authority.

⸻

## 9. User and Intent

A User is often the source of an Intent.

Example:

User
  ↓
"I need to cancel the subscription."
  ↓
Intent

The resulting Intent should preserve its initiating participant or Principal reference.

This relationship is important for:

* authorization
* auditability
* accountability
* clarification
* confirmation
* execution
* provenance

The Intent should reference the relevant participant or Principal context rather than embedding the entire User object.

⸻

## 10. User and Interaction

Interactions occur between Noema and participants.

Example:

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

All interactions may contribute to one Intent lifecycle.

The interaction sequence must remain distinguishable from the resulting Intent.

Conceptually:

User
  ↓
Interaction
  ↓
Intent
  ↓
Interaction
  ↓
Intent Version
  ↓
Trust

An interaction is evidence about participation and Intent.

It is not automatically an authorization decision.

⸻

## 11. User Context

User identity contributes to Context.

Relevant Context may include:

* authenticated identity
* organizational membership
* role
* authorized scope
* active session
* delegated authority
* relevant prior interaction state
* device or channel context where Policy requires it
* relevant execution history
* candidate entity resolutions

Context should be purpose-bound.

Noema should not treat every attribute associated with a User as relevant to every Intent.

More User Context is not automatically better.

⸻

## 12. User Context Is Not User Truth

A User Context may contain information associated with a participant.

It does not automatically establish enterprise Business State.

For example:

User Context:
customer_id = 123

does not by itself establish:

customer.status = ACTIVE

The latter should be grounded in the appropriate enterprise authority.

Similarly:

User Context:
frequently_used_account = A

does not establish:

Intent target = Account A.

Context can support interpretation.

It does not silently become enterprise truth.

⸻

## 13. User and State

Noema may reconstruct enterprise State relevant to a User’s Intent.

State may include:

* account state
* transaction state
* subscription state
* authorization state
* workflow state
* execution state
* resource state
* policy-relevant conditions

State must be distinguished by epistemic status where required.

Examples:

KNOWN
INFERRED
AMBIGUOUS
UNAVAILABLE
STALE
CONTRADICTORY
UNKNOWN
UNAUTHORIZED

A User statement may provide evidence.

It does not automatically establish State.

⸻

## 14. User and Trust

Trust evaluates whether Noema may safely proceed with the requested execution.

User-related Trust inputs may include:

* Principal identity
* authentication
* authorization
* delegation
* organizational scope
* Intent
* resolved Resource
* current State
* evidence
* risk
* confirmation
* Policy
* execution constraints

Conceptually:

Principal
  +
Intent
  +
Resolved Resource
  +
Current State
  +
Authority
  +
Policy
  ↓
Trust Decision

Trust is contextual.

A User does not possess a permanent global Trust state.

⸻

## 15. Trust Outcomes

Trust decisions must be explicit and enumerated.

Canonical outcomes are:

ALLOW
CLARIFY
CONFIRM
WAIT
ESCALATE
REJECT
UNKNOWN

Noema must not expose or rely upon a hidden state such as:

probably_execute

or:

probably_allowed

The model may generate candidate interpretations.

The Trust system determines whether execution may proceed.

If material uncertainty remains:

UNKNOWN

or another appropriate explicit outcome must be represented rather than silently converted into execution.

⸻

## 16. Authentication

Authentication establishes that a participant is associated with a particular identity.

Conceptually:

Credential
    ↓
Authentication
    ↓
Identity
    ↓
Principal

Authentication does not establish:

Authorization.

Authorization does not automatically establish:

Permission for every Action.

These remain separate decisions.

Credentials themselves must not become model-derived facts.

Noema should treat principals as established by the appropriate identity/authentication layer, not extracted from model prose.

⸻

## 17. Authorization

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
   +
Current State
   ↓
Authorization Decision

Noema may consume or evaluate enterprise authorization information but must not silently grant authority that the enterprise has not established.

Authorization should attach to the specific consequential operation rather than merely to general access to a tool or capability.

⸻

## 18. Business Authorization

Noema must distinguish technical authorization from business authorization.

Technical authorization asks:

Can this Principal invoke this capability?

Policy authorization asks:

Does this parameterization satisfy the applicable static Policy?

Business authorization asks:

Given the fully resolved business Action, target, current State, and relevant enterprise conditions, should this operation be permitted to become real?

Therefore:

Capability Access
        +
Policy Authorization
        +
Business Authorization
        =
Governed Execution Eligibility

A technically authorized call against the wrong resolved Resource is still unsafe.

Authorization must therefore be evaluated against the fully resolved Action and target.

⸻

## 19. User Roles

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

Noema must not infer unrestricted authority from a role label alone.

⸻

## 20. User Scope

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

Principal
  +
Scope
  +
Action
  +
Resource
  ↓
Authorization

Scope is part of the authorization context and must not be discarded merely because the User identifier is known.

⸻

## 21. User and Organizational Boundaries

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

Organizational membership is contextual enterprise information, not a universal authorization shortcut.

⸻

## 22. User and Tenant Boundaries

In multi-tenant environments:

Tenant A
   └── User 123

Tenant B
   └── User 123

may contain overlapping local identifiers.

Tenant scope is therefore part of identity context.

A User identifier should not be treated as globally meaningful unless the relevant authority explicitly defines it as such.

Tenant boundaries must be preserved across:

* identity
* context
* data
* evidence
* Intent
* Actions
* executions
* audit records

⸻

## 23. User and Delegation

A User may act on behalf of another Principal.

Example:

Executive
   ↓ delegates
Assistant
   ↓
Intent:
"Approve this invoice."

Delegation must be explicit.

Noema should preserve, where relevant:

acting_principal
delegated_principal
delegation_scope
delegation_authority
delegation_validity

Delegation must be evaluated under the applicable enterprise authority and Policy.

⸻

## 24. Delegation Is Not Identity Substitution

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
* non-repudiation

The system must preserve both the acting Principal and the Principal on whose behalf the action occurs where applicable.

⸻

## 25. User and Approval

A User may act as an approver.

The approver may be different from the requester.

Requester
    ↓
Intent
    ↓
Trust
    ↓
Approval Required
    ↓
Approver
    ↓
Approval
    ↓
Trust Re-evaluation
    ↓
Execution

The identity and authority of the approver must be independently established.

Approval is an event bound to a specific Intent or Action context.

⸻

## 26. User and Confirmation

Confirmation is a statement by a User or authorized Principal that may satisfy a Policy requirement.

Example:

Noema:
"Transfer $20,000 to Account 123?"

User:
"Confirm."

The confirmation must be bound to the relevant Intent or Action.

A generic:

"Yes"

must not be treated as authorization outside its established context.

Confirmation is evidence of a participant decision.

It is not, by itself, proof of authority.

⸻

## 27. Confirmation Is Not Authorization

A User may confirm an Action they are not authorized to perform.

Therefore:

Confirmation

does not replace:

Authorization.

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

Confirmation may satisfy a Policy requirement only after the relevant identity and authority conditions have been established.

⸻

## 28. User and Ambiguity

A User may provide information required to resolve ambiguity.

Example:

User:
"Refund John's payment."

Noema:
"Which John?"

User:
"John Smith in Finance."

The second interaction provides additional Intent information.

It does not automatically establish that the identified John is the correct enterprise Resource.

That identity must still be grounded where required.

Material ambiguity must remain an explicit state.

Noema must never use User familiarity or model confidence as a substitute for authoritative resolution.

⸻

## 29. User and Model Interpretation

The model may interpret User input.

For example:

User:
"Send the invoice to Sarah."

Model:
candidate recipient = Sarah Johnson

This is a candidate interpretation.

Noema must validate the relevant identity, Resource, authority, and Policy before consequential execution.

Therefore:

User Input
   ↓
Model Interpretation
   ↓
Candidate Intent
   ↓
Schema Validation
   ↓
Context / State
   ↓
Noema Resolution
   ↓
Trust

Model-generated identity candidates are never authoritative merely because their confidence is high.

⸻

## 30. User and Intent Versioning

An Intent admitted into consequential processing must be treated as an explicit semantic object.

The User Model must therefore support:

intent_id
intent_version
principal
created_at
supersedes
provenance

A material change to an Intent must create a new version rather than silently mutate the previous Intent.

Example:

Intent v1:
"Transfer $5,000."

User:
"Actually, make it $7,000."

Intent v2:
"Transfer $7,000."

Intent v2 supersedes Intent v1.

The original request remains part of the causal history.

⸻

## 31. User and Natural Language

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
Agent-generated proposal

The underlying participant semantics must remain consistent across modalities.

⸻

## 32. User and Structured Interaction

A User may interact through structured controls.

Example:

Invoice:
INV-123

Action:
[Approve]

The interaction may produce the same semantic Action as:

"Approve invoice INV-123."

The User Model remains unchanged.

The interaction modality must not change the underlying identity, authority, attribution, or Trust semantics.

⸻

## 33. User and Machine Participants

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

Noema must not invent a human User when a machine Principal actually originated the Intent.

⸻

## 34. User-Initiated vs System-Initiated Intent

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
* notification

A system-generated Intent should not be represented as if a human explicitly requested it.

Likewise, an external AI agent proposal must preserve the identity of the initiating agent and, where applicable, the human or system Principal represented by that agent.

⸻

## 35. User and External Agents

Noema may receive an Action proposal from an external enterprise agent.

Example:

Enterprise Agent
       ↓
Proposed Action
       ↓
Noema
       ↓
Context + State
       ↓
Trust
       ↓
Execute / Reject / Escalate

In this mode, the external agent is an input to Noema’s governed execution boundary.

The agent’s model output is not itself authorization.

Noema must independently evaluate:

* Principal
* authority
* Intent
* Resource
* State
* Policy
* risk
* capability
* execution constraints

The same User Model must therefore support both human-originated Intent and agent-originated Action proposals.

⸻

## 36. Acting Principal vs Execution Principal

The Principal requesting an Action and the technical identity executing the enterprise API call may differ.

Example:

Acting Principal:
Jane Doe

Execution Principal:
Noema Service Identity

The distinction is essential.

The service identity’s technical ability to call an API does not mean every User may use that capability.

Noema must enforce the acting Principal’s authority independently.

Conceptually:

Acting Principal
       ↓
Authorization
       ↓
Trust
       ↓
Noema Execution Principal
       ↓
Enterprise Capability

The technical Execution Principal must never silently replace the originating Principal for authorization or audit purposes.

⸻

## 37. User and Service Identity

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

This is a core confused-deputy protection.

Technical capability is not business permission.

⸻

## 38. User and Capability Boundaries

A User may only cause execution through capabilities that Noema is explicitly permitted to invoke.

A capability must be:

* registered
* typed
* bounded
* policy-aware
* attributable
* executable under defined conditions

Noema must not infer that because an enterprise API exists, every User may invoke it.

Likewise:

Capability Exists

does not imply:

User May Invoke Capability.

The authorization decision remains contextual.

⸻

## 39. User and Data Access

A User may be authorized to perform an Action without being authorized to view every piece of data involved in that Action.

Therefore:

Action Authorization

and:

Data Access

must remain independently evaluated where required.

A User’s ability to:

refund payment

does not necessarily imply the ability to view:

full customer profile.

Noema should not expose protected information merely because that information is useful to the model.

⸻

## 40. User and Minimum Necessary Context

Noema should use the minimum User information necessary for the current Intent and Action.

For example:

Refund Payment

may require:

employee identity
authorization scope
payment reference

It may not require unrelated personal attributes.

The User Model should therefore support:

* data minimization
* purpose limitation
* scoped retrieval
* redaction
* tenant isolation

Minimum necessary visibility is a product requirement, not merely a privacy preference.

⸻

## 41. User and Privacy

User information may be sensitive.

Noema should apply appropriate:

* access control
* minimization
* purpose limitation
* retention
* redaction
* audit
* isolation

User identity data should not be replicated across the platform without a legitimate execution or governance purpose.

Credentials must not be placed in model context merely because the User is authenticated.

⸻

## 42. User and Auditability

Consequential actions should preserve sufficient attribution.

An audit record may need to establish:

who initiated the Intent
who interpreted or proposed it
who confirmed it
who approved it
who intervened
what Action executed
under which authority
under which Policy
against what evidence
through which capability
under which technical execution identity
with which result

The audit trail should preserve causal relationships rather than merely recording a model trace.

⸻

## 43. User and Provenance

Participant-related evidence must be attributable.

Examples:

User Statement
→ evidence from user interaction

Identity Provider
→ verified identity

Enterprise Authorization
→ authority evidence

Approval
→ approval event

Execution Service
→ technical execution identity

Enterprise System
→ execution result or Business State evidence

Provenance must preserve the source and role of evidence.

Model assertions must not be presented as equivalent to authoritative enterprise evidence.

⸻

## 44. User and Execution History

A User may have multiple historical Interactions and Executions.

History can provide useful Context.

However:

historical behavior ≠ authorization

historical behavior ≠ current Intent

historical behavior ≠ current Business State

Past behavior may assist interpretation but must not silently override current explicit Intent, current authority, current Policy, or authoritative enterprise data.

⸻

## 45. User and Personalization

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

## 46. User and Historical Context

Historical Context may help resolve references such as:

"the account we discussed yesterday."

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

If material ambiguity remains:

CLARIFY
or:
ESCALATE

must remain available.

⸻

## 47. User and Risk

The same Action may have different risk depending on:

* Principal
* Resource
* amount
* scope
* organizational authority
* current State
* Policy
* execution conditions

For example:

Principal A
→ transfer $1,000
→ allowed

Principal B
→ transfer $1,000
→ approval required

Risk is therefore evaluated in context rather than solely by Action type.

User familiarity or historical behavior must not independently reduce risk classification.

⸻

## 48. User and Trust State

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
State
  +
Policy

produces a Trust evaluation.

The result applies to that execution context.

It should not automatically be generalized to every future Action.

Canonical Trust outcomes include:

ALLOW
CLARIFY
CONFIRM
WAIT
ESCALATE
REJECT
UNKNOWN

⸻

## 49. User and Human Intervention

A User may become an intervention participant when Noema requires additional human action.

Examples:

Clarification
Approval
Conflict Resolution
Exception Handling
Recovery Decision

The role being performed should be explicit.

A requester acting as a requester is not automatically an authorized operator.

Similarly, an approver is not automatically authorized to perform the underlying Action unless enterprise authority establishes that authority.

⸻

## 50. User Roles in an Execution

One execution may contain multiple User or Principal roles.

Example:

Requester
    ↓
Noema
    ↓
Approver
    ↓
Noema
    ↓
Operator
    ↓
Enterprise System

Noema should preserve these relationships.

Conceptually:

Execution
    │
    ├── initiated_by → Requester
    ├── proposed_by → Agent or Principal
    ├── confirmed_by → Confirmer
    ├── approved_by → Approver
    ├── executed_by → Execution Principal
    └── intervened_by → Operator

where applicable.

⸻

## 51. User and Outcome

The User may receive the Outcome of an execution.

For example:

Execution:
SUCCEEDED

User:
"Your refund has been completed."

The communicated Outcome must correspond to established execution and verification state.

A User-facing response is not itself the source of truth for the Outcome.

⸻

## 52. User and Failure

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

A timeout must not automatically be translated into failure.

Noema should verify the enterprise state before deciding whether a retry, recovery, escalation, or other action is appropriate.

⸻

## 53. User and Cancellation

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

The User Model records who requested cancellation.

The Execution Model determines whether cancellation is operationally possible.

⸻

## 54. User and Modification

A User may modify an Intent before execution.

Example:

User:
"Transfer $5,000."

User:
"Actually, make it $7,000."

Noema must determine whether the second interaction modifies the existing Intent or creates a new Intent version.

Any material modification may require renewed:

* resolution
* authorization
* Trust
* confirmation
* approval

Material changes must not silently inherit clearance from the previous version.

⸻

## 55. User and Confirmation Expiry

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

## 56. User and Account

A Noema product account may represent a User’s relationship with Noema.

It may contain:

noema_user_id
identity_reference
tenant
preferences
product configuration
lifecycle state

The Noema account must not be confused with enterprise accounts.

For example:

Noema User Account

is distinct from:

Enterprise Bank Account

or:

Enterprise Customer Account.

The enterprise remains authoritative for Business State associated with enterprise accounts.

⸻

## 57. User and Enterprise Resource

A User may own, manage, access, or be associated with an enterprise Resource.

Examples:

Employee → Expense Account
Manager → Department
Customer → Subscription
Agent → Support Ticket

These relationships must be established by authoritative enterprise data or explicit trusted configuration.

Noema should not invent ownership relationships from conversational assumptions.

A User statement such as:

"That's my account"

is evidence requiring appropriate grounding, not automatically authoritative ownership.

⸻

## 58. User and Resource Scope

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

The authorization check must bind to the resolved Resource before consequential execution.

⸻

## 59. User and Enterprise Identity Changes

Enterprise identity may change.

Examples:

Employee transferred
Role changed
Department changed
Account disabled
Employment terminated

Noema should rely on current authoritative identity and authorization information where required.

Historical execution records should preserve the identity and authority context relevant at the time of execution.

A historical User state must not be rewritten merely because current enterprise identity differs.

⸻

## 60. User and Identity Lifecycle

A User may move through states such as:

INVITED
ACTIVE
SUSPENDED
DEACTIVATED

These are product-level states.

Enterprise identity lifecycle may have different states.

Noema should not assume that product state and enterprise identity state are identical.

A product-level ACTIVE state does not itself establish enterprise authorization.

⸻

## 61. User State vs Execution State

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

Current User State may, however, affect whether a new execution may proceed under current Policy.

⸻

## 62. User Model

Conceptually:

User {
    user_id
    principal_reference
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

Authorization, enterprise identity, State, and Business State remain separate concerns.

⸻

## 63. User Participation Model

Conceptually:

Participation {
    principal
    role
    scope
    intent
    interaction
    execution
    authority
    provenance
}

Possible roles include:

REQUESTER
CONFIRMER
APPROVER
OPERATOR
INTERVENOR
OBSERVER
PROPOSER

A single User or Principal may occupy different roles across different executions.

The role must be interpreted within the relevant execution context.

⸻

## 64. User Relationships

User
│
├── has → Identity
├── maps_to → Principal
├── belongs_to → Tenant
├── belongs_to → Organization
├── participates_in → Interaction
├── expresses → Intent
├── provides → Context
├── may_confirm → Action
├── may_approve → Execution
├── may_intervene_in → Execution
└── receives → Outcome

Principal
│
├── may_be → User
├── may_be → Service
├── may_be → Application
├── may_be → Agent
└── may_be → System

Participation
│
├── identifies → Principal
├── assigns → Role
├── constrains → Scope
└── attributes → Execution Activity

⸻

## 65. User Model and Trust

The User Model provides identity and participation context.

The Trust Model determines whether the requested execution may proceed.

Therefore:

User
  ↓
Principal / Identity / Context
  ↓
Intent + Resource + State
  ↓
Authorization
  ↓
Trust
  ↓
Action

The User Model must not embed the final Trust decision as an intrinsic property of the User.

Trust belongs to an execution context.

⸻

## 66. User Model and Enterprise Identity

The relationship is:

Noema User
      │
      ▼
Principal / Identity Reference
      │
      ▼
Enterprise Identity Authority

Noema may cache identity information where appropriate, but authoritative identity semantics remain with the enterprise authority.

Identity mappings must preserve provenance and tenant scope.

A cached identity must not silently become authoritative after the underlying enterprise identity has changed.

⸻

## 67. User Model and Permissions

Permissions belong to the enterprise authorization model.

The User Model may reference the permissions relevant to a current execution.

It should not become a second independent permission system.

Therefore:

User / Principal
   ↓
Enterprise Authorization
   ↓
Permission
   ↓
Trust
   ↓
Enterprise Action

rather than:

User
   ↓
Noema Permission
   ↓
Enterprise Action

unless Noema is explicitly configured by the enterprise as part of the authoritative authorization architecture.

⸻

## 68. User Model and Interaction Model

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

Principal establishes who is acting.

These must remain distinct.

⸻

## 69. User Model and Intent Model

The Intent Model answers:

“What does the participant want to accomplish?”

The User Model answers:

“Who is participating in that Intent?”

Therefore:

User / Principal
    │
    └── expresses → Intent

The Intent should not contain the entire User object.

It should reference the relevant Principal or identity context.

A canonical Intent representation may include a principal reference and authentication context, while detailed User data remains outside the Intent unless required.

⸻

## 70. User Model and Execution Model

The Execution Model answers:

“What happened while performing the Action?”

The User Model provides:

“Who initiated, confirmed, approved, proposed, or intervened in that execution?”

Therefore:

Execution
    │
    ├── initiated_by
    ├── proposed_by
    ├── confirmed_by
    ├── approved_by
    ├── executed_by
    └── intervened_by

where applicable.

This attribution must remain intact even when the technical execution identity differs from the initiating Principal.

⸻

## 71. User Model and Auditability

Auditability requires attribution without requiring excessive personal data.

A consequential record should be able to establish:

Principal
Role
Intent
Intent Version
Action
Resource
Time
Authority
Policy
Evidence
Execution Principal
Outcome

The audit system should preserve the minimum information required to establish accountability and reconstruct execution.

Causal audit should answer:

Who acted?

What did they request or approve?

What was resolved?

What authority applied?

What Action occurred?

What system performed it?

What happened afterward?

⸻

## 72. User Model and Security Boundary

A User is a security-relevant participant but is not itself the complete security boundary.

Security decisions should consider:

Principal
Identity
Authentication
Authorization
Action
Resource
Scope
Policy
State
Risk
Evidence

Noema must avoid simplifying this into:

User = Trusted.

The security boundary must survive:

* model error
* prompt injection
* forged context
* stale identity
* confused-deputy attempts
* malicious enterprise content
* replay
* privilege escalation
* cross-tenant access attempts

External systems and model outputs must be treated as untrusted inputs until validated by the appropriate controls.

⸻

## 73. User Model and Confused-Deputy Protection

The User Model must support Noema’s protection against confused-deputy execution.

The critical distinction is:

Technical Capability
       ≠
Business Authority

For example:

Noema Service Identity
       ↓
Can technically invoke refund API

does not imply:

Every Noema User
       ↓
May refund any payment

The authorization path must preserve:

Acting Principal
       +
Action
       +
Resolved Resource
       +
Scope
       +
Policy
       +
Current State
       ↓
Trust Decision

Only after the Trust decision is cleared may Noema execute through the technical Execution Principal.

⸻

## 74. User Model and Product Modes

The User Model must work across both Noema deployment modes.

### Mode 1 — Full-Stack Execution Platform

Human participant
       ↓
Interaction
       ↓
Intent
       ↓
Context / State
       ↓
Trust
       ↓
Action
       ↓
Execution

In this mode, Noema may own the complete path from human expression through verified enterprise outcome.

### Mode 2 — Independent Trust Boundary

Enterprise Agent
       ↓
Proposed Action
       ↓
Noema Principal / Context Resolution
       ↓
State
       ↓
Trust
       ↓
Action
       ↓
Execution

In this mode, an enterprise agent may generate the proposal, but Noema remains the independent consequential-action trust boundary.

The User Model must therefore preserve the distinction between:

human participant
agent Principal
acting Principal
enterprise Principal
execution Principal

regardless of which component generated the initial request.

⸻

## 75. User Model and Product Experience

The User Model allows Noema to provide a coherent experience across different interaction surfaces.

The same User may interact through:

Chat
Dashboard
Mobile App
Voice
API-connected Application
Approval Interface
Enterprise Agent

The underlying identity and execution relationship should remain consistent.

Changing the interface must not change:

* Principal
* authority
* Intent semantics
* Policy
* Trust requirements
* Action semantics
* attribution

⸻

## 76. User Model and Product Personalization

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
* resolved Resource

unless explicitly defined by Policy.

⸻

## 77. User Model and AI Personalization

Historical User behavior may help the model generate better candidates.

For example:

User frequently works with Account A.

This may inform candidate generation.

It must not become:

User probably means Account A.
Therefore execute.

Material ambiguity still requires deterministic resolution.

AI personalization can improve candidate generation.

It cannot redefine authority or enterprise truth.

⸻

## 78. User Model and Accountability

Noema must preserve the distinction between:

requested_by

and:

proposed_by

and:

confirmed_by

and:

approved_by

and:

executed_by

and:

intervened_by

These may all refer to different Principals.

This distinction becomes particularly important in enterprise environments and in Mode 2, where an external agent may propose an Action that Noema independently governs and executes.

⸻

## 79. User Model and Non-Repudiation

For high-consequence operations, Noema may need sufficient evidence that a particular Principal performed a particular interaction or approval.

This may require:

* authenticated identity
* timestamp
* Intent binding
* Intent Version
* Action binding
* confirmation
* authorization evidence
* Policy evidence
* execution provenance

The exact requirements are determined by enterprise Policy and risk.

Noema should not claim stronger non-repudiation than the underlying evidence supports.

⸻

## 80. User Model and Revocation

Authorization can change after an Intent has been created.

For example:

Intent Created
     ↓
User Role Revoked
     ↓
Execution Attempted
     ↓
Authorization Re-evaluated

Noema must evaluate whether authorization remains valid under the applicable Policy.

Creation of an Intent does not necessarily grant permanent authority to execute it.

Where Policy requires current authorization, Noema must revalidate it at the consequential execution boundary.

⸻

## 81. User Model and Long-Running Execution

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

If Policy requires re-authentication or renewed authorization during a long-running execution, that requirement must be enforced explicitly.

⸻

## 82. User Model and Re-Authentication

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

A successful re-authentication establishes identity evidence.

It does not independently establish authorization for the Action.

⸻

## 83. User Model and Human Trust

Noema should not infer trustworthiness from behavioral familiarity alone.

Examples such as:

"She has done this before."

"He usually approves these."

"This is the same device."

do not automatically establish current authorization.

Current enterprise identity, authority, evidence, State, and Policy remain authoritative.

Historical familiarity may inform interpretation or risk signals but must not bypass Trust controls.

⸻

## 84. User Model and State Changes

A User may begin an Intent under one enterprise state and reach execution under another.

Example:

User
  ↓
Intent Created
  ↓
Account Active
  ↓
Account Suspended
  ↓
Execution Attempt

Noema must evaluate the current relevant State at the execution boundary where Policy requires it.

A previously valid User context does not freeze enterprise State.

Likewise, a User’s confirmation does not freeze all enterprise conditions.

⸻

## 85. User Model and Unknown State

Noema must preserve uncertainty when the enterprise state cannot be established.

Examples:

Payment status:
UNKNOWN

Identity mapping:
UNKNOWN

Authorization:
UNKNOWN

Resource resolution:
AMBIGUOUS

A User should not be told that an Action succeeded or failed merely because the technical response is inconclusive.

Unknown state may result in:

WAIT
CLARIFY
ESCALATE
UNKNOWN

according to the applicable Trust and execution semantics.

⸻

## 86. User Model and Verification

The User Model records who should receive or participate in the resulting Outcome.

Verification determines whether the expected enterprise outcome actually occurred.

Therefore:

User
  ↓
Intent
  ↓
Action
  ↓
Execution
  ↓
Verification
  ↓
Outcome
  ↓
User

A User-facing statement must be grounded in the verified Outcome.

The User Model must not become the source of enterprise execution truth.

⸻

## 87. User Model Invariants

### Invariant 1

A User is a product participant, not merely an authentication credential.

### Invariant 2

User, Principal, Identity, Authority, and Intent are distinct concepts.

### Invariant 3

Authentication does not establish authorization.

### Invariant 4

Identity does not establish permission for every Action.

### Invariant 5

A User expressing an Intent does not automatically authorize its execution.

### Invariant 6

Noema must preserve the initiating Principal for consequential execution.

### Invariant 7

Acting Principal and technical Execution Principal may differ and must remain distinguishable.

### Invariant 8

Service credentials must not become an authority bypass for Users.

### Invariant 9

Enterprise identity remains authoritative for enterprise identity semantics.

### Invariant 10

Noema must not silently create a competing enterprise identity authority.

### Invariant 11

Authorization must be evaluated in the relevant Principal, Action, Resource, Scope, State, and Policy context.

### Invariant 12

User roles do not automatically imply unrestricted permissions.

### Invariant 13

Tenant and organizational boundaries must be preserved.

### Invariant 14

Delegation must be explicit and auditable.

### Invariant 15

Delegated identity must not be represented as identity substitution.

### Invariant 16

Requester, proposer, confirmer, approver, operator, and intervenor roles must remain distinguishable.

### Invariant 17

Confirmation does not replace authorization.

### Invariant 18

Confirmation must be bound to the relevant Intent or Action.

### Invariant 19

Historical User behavior may assist interpretation but must not establish current authorization.

### Invariant 20

Personalization must not silently alter consequential execution semantics.

### Invariant 21

User-provided information does not automatically establish enterprise Business State.

### Invariant 22

User identity does not establish ownership or access to an enterprise Resource without authoritative grounding.

### Invariant 23

User State and Execution State must remain distinct.

### Invariant 24

Product User State and enterprise identity lifecycle state must remain distinguishable.

### Invariant 25

Authorization may change during the lifecycle of an Intent.

### Invariant 26

Intent creation does not necessarily grant permanent execution authority.

### Invariant 27

Long-running execution must preserve sufficient Principal attribution even when the initiating session ends.

### Invariant 28

Unknown or ambiguous identity must be resolved deterministically before consequential execution.

### Invariant 29

Model-generated identity candidates are not authoritative identity.

### Invariant 30

Noema must preserve sufficient identity and participation provenance for consequential auditability.

### Invariant 31

User information should be minimized according to the purpose of the current execution.

### Invariant 32

A User does not possess an intrinsic global Trust state; Trust is contextual to the requested execution.

### Invariant 33

A User’s ability to perform one Action does not imply authority for another Action.

### Invariant 34

Noema must distinguish who requested an Action from who technically executed it.

### Invariant 35

The User Model must remain separate from the enterprise authorization system unless explicitly defined as part of that authority.

### Invariant 36

Technical capability access does not imply business authority.

### Invariant 37

Authorization must attach to the fully resolved consequential Action and Resource.

### Invariant 38

Noema must not allow a service identity to substitute for the originating Principal in authorization decisions.

### Invariant 39

Trust outcomes must be explicit and enumerated.

### Invariant 40

Material uncertainty must not be converted into implicit permission to execute.

### Invariant 41

A material Intent modification must create a new Intent version rather than silently mutating the admitted Intent.

### Invariant 42

Intent versions must preserve causal linkage to the prior version.

### Invariant 43

A User confirmation belongs to a specific Intent or Action context and may become stale when material conditions change.

### Invariant 44

Current enterprise State may supersede historical User Context where authoritative State is required.

### Invariant 45

Unknown enterprise State must remain explicitly represented and must not be fabricated into certainty.

### Invariant 46

User-facing Outcome communication must be grounded in verified execution state.

### Invariant 47

A timeout must not automatically be represented as a failed enterprise operation.

### Invariant 48

Noema must distinguish human Principals from machine Principals.

### Invariant 49

System- or agent-initiated Intent must not be represented as human-initiated without evidence.

### Invariant 50

External agent output is an untrusted proposal until it passes Noema’s applicable governance controls.

### Invariant 51

The User Model must support both Noema’s full-stack execution mode and independent trust-boundary mode.

### Invariant 52

Interface modality must not alter identity, authority, attribution, or Trust semantics.

### Invariant 53

User information must not be replicated or exposed beyond the purpose of the current execution.

### Invariant 54

Enterprise Business State remains authoritative for enterprise resources even when Noema maintains execution state about operations affecting them.

### Invariant 55

The User Model must preserve sufficient provenance to reconstruct who participated in consequential execution and in what role.

⸻

## 88. Final Definition

The User Model defines how Noema represents participants in Intent-driven enterprise execution and preserves the relationship between identity, Principal, participation, authority, Intent, Action, and execution.

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
 CONTEXT + STATE
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
 VERIFICATION
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

Or, in an agent-mediated execution:

Human / System Principal
          │
          ▼
      Agent / Service
          │
          ▼
    Proposed Action
          │
          ▼
        Noema
          │
          ▼
 Context + State + Authority
          │
          ▼
         Trust
          │
          ▼
       Execution
          │
          ▼
      Verification
          │
          ▼
        Outcome

The architectural rule is:

Noema must know who is participating, what Principal is acting, what authority applies, what role each participant performs, and what evidence establishes those facts without conflating identity with authorization, confirmation with authority, technical capability with business permission, historical behavior with current trust, or model interpretation with authoritative enterprise truth.

The User Model therefore provides the participant and attribution semantics around Noema’s stable execution core:

Intent
  ↓
Context / State
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

The model may interpret.

The enterprise establishes identity and authority.

Noema governs consequential execution.