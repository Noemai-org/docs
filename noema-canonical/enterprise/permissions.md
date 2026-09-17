Permissions

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/permissions.md

⸻

1. Definition

Permissions define the authority an identity, principal, service, application, agent, role, group, or delegated principal has to perform a defined operation on an enterprise resource within specified scope, constraints, and validity conditions.

Permissions answer:

“Is this principal permitted to perform this operation on this resource under the applicable enterprise authorization semantics?”

Permissions are enterprise-defined authorization inputs that Noema may consume when evaluating Trust.

Permissions are not the same as Intent, Capability, Role, Policy, Authorization, Trust, or Outcome.

⸻

2. Purpose

Noema needs permission information to determine whether a resolved Action may legitimately cross the enterprise execution boundary.

The conceptual flow is:

Source of Intent
      ↓
Intent Interpretation
      ↓
Hard Schema Validation / Admission
      ↓
Intent Resolution
      ↓
Resolved Actor / Action / Target
      ↓
Enterprise Authorization / Permission Evidence
      ↓
Context / State Reconciliation
      ↓
Deterministic Trust
      ↓
Action Contract
      ↓
Execution

Permission is one input into this process, not the complete decision.

Other constraints may still apply:

Permission
Policy
Organizational Scope
Resource State
Preconditions
Data Boundaries
Risk
Approval Requirements
Freshness
Temporal Constraints
Capability Availability

⸻

3. Core Principle

A permission is evidence of authority, not a universal guarantee of execution.

For example:

Permission:
refund_payment

does not necessarily mean:

refund any payment
at any time
for any amount

Effective authority may instead be constrained by:

refund_payment
+
Finance / Nigeria
+
amount <= $5,000
+
active account
+
eligible payment state
+
current authorization

The enterprise defines the semantics of that authority. Noema must not broaden them.

⸻

4. Permission vs Capability

These concepts must remain distinct.

Capability

A Capability describes an operation the enterprise system exposes or permits Noema to invoke through an explicit integration boundary.

Example:

cancel_subscription

Permission

A Permission describes whether a particular principal may exercise an operation under enterprise-defined conditions.

Example:

Alice
→ permitted to cancel subscription

Therefore:

Capability ≠ Permission

A capability can exist without a particular principal being permitted to use it.

A principal can have permission for an operation that Noema does not currently possess as an executable Capability.

Neither fact alone is sufficient for execution.

⸻

5. Permission vs Role

A Role groups organizational responsibility or authority according to enterprise-defined authorization semantics.

Example:

Role:
Finance Manager

A role may grant or contribute to a permission:

Finance Manager
→ approve_invoice

However, Noema must not infer permission merely because a principal appears to hold a particular role unless the enterprise authorization model establishes that relationship.

Role ≠ Permission

Membership and role assignment are inputs to authorization, not universal authorization guarantees.

⸻

6. Permission vs Authorization

Authorization is the process or decision by which an enterprise determines whether an operation is allowed.

Permission is one representation of authority that may contribute to that decision.

Conceptually:

Principal
    +
Action
    +
Resource
    +
Scope
    +
Context
    +
Enterprise Policy
    +
Authorization State
    ↓
Authorization Decision

An enterprise may implement this through RBAC, ABAC, PBAC, ACLs, a centralized policy engine, or another authorization model.

Noema should preserve the enterprise semantics rather than reducing them to a simplistic boolean when doing so would lose material meaning.

⸻

7. Permission vs Trust

Trust is broader than permission.

A principal may possess valid permission while an Action remains unsafe, ambiguous, unresolved, unavailable, or otherwise unsuitable for execution.

Example:

Permission:
transfer_funds = allowed
Intent:
"Transfer $50,000 to John."
Problem:
multiple Johns identified

The permission may be valid, but the target remains unresolved.

The Trust result may therefore be:

CLARIFY

Therefore:

Permission ≠ Trust

Trust evaluates the complete resolved execution condition.

⸻

8. Permission Model

A permission can be represented conceptually as:

Permission {
    principal
    action
    resource
    scope
    constraints
    validity
    source
    provenance
}

For example:

Principal:
Alice
Action:
approve_invoice
Resource:
Invoice
Scope:
Nigeria Finance
Constraint:
amount <= $10,000
Validity:
active
Source:
Enterprise Authorization System

This representation is conceptual. The canonical enterprise authorization representation remains defined by the enterprise system that owns the permission.

⸻

9. Principal

A Permission must identify its subject.

The principal may be:

human
service
application
agent
role
group
organization
delegated identity

Where consequential execution requires an effective principal, Noema must resolve and preserve the relevant identity or explicitly defined non-human principal.

The principal must not be inferred into authoritative authorization merely from model confidence.

⸻

10. Human Permissions

Example:

Alice
→ approve_invoice
→ Finance / Nigeria

Noema consumes this authorization information rather than inventing it.

For consequential Actions, the relevant principal, scope, authorization source, and applicable validity should be attributable.

⸻

11. Service Permissions

Enterprise services may have their own permissions.

Example:

billing-service
→ create_invoice

Noema must distinguish:

human principal

from:

service principal

because their authority, credential model, delegation semantics, and audit requirements may differ.

A service principal must not be treated as a human identity merely because it acts on behalf of one.

⸻

12. Agent Permissions

AI agents may operate under explicit enterprise-defined authority.

Example:

Noema Agent
→ cancel_subscription
→ Customer Support

An agent must not inherit unrestricted human authority merely because a human initiated the Intent.

Agent authority must be explicitly bounded by the applicable enterprise authorization and delegation model.

⸻

13. Delegated Permissions

A principal may delegate authority.

Example:

Alice
   ↓ delegates
Noema
   ↓
refund_payment

Delegation should preserve:

delegator
delegate
permission
scope
constraints
validity
purpose

Delegation must not silently expand authority.

Where delegation affects a consequential Action, the delegation relationship should be preserved in the authorization and causal audit record.

⸻

14. Permission Scope

Permissions may be scoped by:

tenant
organization
legal entity
region
department
team
project
resource
resource type
environment

Example:

Permission:
approve_invoice
Scope:
Acme Nigeria Ltd.

This does not imply authority over:

Acme UK Ltd.

Scope is part of the permission semantics and must be evaluated rather than discarded.

⸻

15. Resource-Level Permissions

Some permissions apply to a specific resource.

Example:

Alice
→ edit
→ Repository: payment-service

rather than:

Alice
→ edit
→ every repository

Resource-level permissions can provide narrowly scoped authorization evidence.

Noema must preserve the exact target resource when evaluating consequential authorization.

⸻

16. Resource-Type Permissions

A permission may apply to an entire resource class.

Example:

Alice
→ approve
→ Invoice

This may still be constrained by:

organization
amount
currency
region
status
resource ownership

A resource-type permission must not be interpreted as unrestricted authority over every instance of that resource type.

⸻

17. Permission Constraints

Permissions may contain conditions.

Examples:

amount <= $10,000
region = Nigeria
status = pending
business_unit = Finance
time < 18:00
environment = production

Permission evaluation may therefore require current enterprise Context and reconciled enterprise state.

⸻

18. Conditional Permissions

Example:

Permission:
refund_payment
Condition:
amount <= $1,000

Then:

Refund $500
→ permitted under this permission
Refund $5,000
→ outside this permission

The permission itself has not changed. The proposed Action falls outside its defined constraints.

⸻

19. Temporal Permissions

Permissions may be time-bound.

Example:

Alice
→ production_access
Valid:
August 1 → August 31

After expiration, the permission may no longer be applicable.

Noema must not rely on stale authorization information for consequential operations when current authorization is required by policy or risk.

Temporal validity must use the relevant enterprise-defined semantics. Recency alone does not establish authority.

⸻

20. Environment Permissions

Enterprise systems may separate:

development
staging
production

A principal may have:

production.read

without:

production.write

Noema must preserve environment scope when evaluating permissions.

A permission valid in one environment must not silently transfer to another.

⸻

21. Read vs Write Permissions

Permissions should distinguish observation from mutation.

Examples:

read_account
update_account
delete_account

A principal with:

read_account

cannot be assumed to have:

update_account

Read-only access can nevertheless be consequential when it exposes protected, regulated, privileged, or otherwise sensitive enterprise information.

Therefore:

read-only ≠ no Trust requirement

⸻

22. Permission Granularity

Permissions may exist at different granularities:

Resource
Resource Type
Action
Action Family
Organization
Tenant
System

The enterprise authorization system determines the semantics.

Noema should preserve the source representation where the distinction affects authorization, scope, auditability, or Trust evaluation.

⸻

23. Permission Inheritance

Permissions may be inherited through:

role
group
organization
team
parent resource

Example:

Alice
   ↓ member_of
Finance Managers
   ↓ grants
approve_invoice

Noema should retain the provenance of the effective permission where available.

An inherited permission must remain bounded by the enterprise authorization semantics that produced it.

⸻

24. Permission Provenance

For consequential Actions, Noema should be able to answer:

Why does this principal have this permission?

Possible answer:

Alice
→ member of Finance Managers
→ Finance Managers role grants approve_invoice
→ scope = Nigeria Finance
→ source = Enterprise IAM

Permission provenance supports causal auditability.

It must not be confused with private model reasoning.

⸻

25. Effective Permission

The effective permission is the authorization evidence applicable to the fully resolved Action at the relevant time and scope.

Example:

Principal:
Alice
Permission:
approve_invoice
Scope:
Nigeria Finance
Action:
approve Invoice #123

The effective permission exists only if the enterprise authorization semantics establish that this principal may perform this Action on this resource under the applicable constraints.

⸻

26. Permission Intersection

When multiple restrictions apply:

Role Permission
        ∩
Organizational Scope
        ∩
Resource Scope
        ∩
Policy
        ∩
Temporal Constraints
        ∩
Environment

the resulting authority is the authority applicable to the Action.

This is preferable to treating permissions as independently additive when the enterprise authorization model defines limiting intersections.

Noema must not impose a universal algebra on enterprise authorization semantics that the enterprise itself does not define.

⸻

27. Deny Semantics

Enterprise authorization systems may support explicit denial.

Example:

Alice
→ Finance Manager
→ approve_invoice = allowed
Explicit policy:
Alice cannot approve invoices
for Legal Entity X

An explicit deny must be handled according to the enterprise authorization semantics.

Noema should not impose a universal deny-precedence rule across all authorization systems. Where the enterprise authorization system returns a final decision, Noema should consume that decision and its relevant evidence.

⸻

28. Permission Revocation

Permissions can be revoked.

Example:

Alice
→ approve_invoice

is revoked at:

14:00

A cached permission observed at:

13:30

may no longer be sufficient for a consequential execution at:

14:15

Freshness and validity requirements therefore matter.

⸻

29. Permission Drift

Permission state may change independently of Noema.

Examples:

role removed
employee transferred
permission revoked
project closed
delegation expired
resource ownership changed
organizational scope changed

Noema should validate relevant permissions when required by policy, risk, action semantics, or freshness requirements.

Permission drift must not be silently ignored for consequential execution.

⸻

30. Permission Freshness

Permission evidence should have associated provenance and temporal information where practical.

Conceptually:

Permission
   ├── source
   ├── authority
   ├── observed_at
   ├── effective_from
   ├── expires_at
   └── version

Freshness is claim- and Action-specific.

A high-risk Action may require fresher authorization evidence than a low-risk Action.

Freshness does not substitute for authority:

recent ≠ authoritative

⸻

31. Permission and Business State

Permissions alone do not establish that an Action is valid.

Example:

Permission:
cancel_order = allowed
Business State:
order.status = already_shipped
Policy:
shipped orders cannot be cancelled

The Action may therefore produce:

REJECT

Permission establishes authority to perform an operation; it does not override enterprise business-state constraints.

⸻

32. Permission and Preconditions

Permissions establish authority.

Preconditions establish whether an Action may proceed against the current state.

Conceptually:

Permission
→ may this principal perform this Action?
Precondition
→ are the conditions for this execution currently satisfied?

Both may be required.

Preconditions should be evaluated against current, appropriately reconciled state.

⸻

33. Permission and Postconditions

Permission does not establish successful execution.

Example:

Permission:
refund_payment = allowed
Execution:
refund request submitted
Postcondition:
payment.refund_status = completed

The postcondition must be verified independently.

Permission ≠ Execution Success

The enterprise remains authoritative for the resulting business state.

⸻

34. Permission and Risk

The existence of permission does not eliminate execution risk.

Example:

Permission:
transfer_funds
Risk:
$2,000,000 transfer

Enterprise policy may require:

additional approval
dual control
human confirmation

Trust therefore considers more than permission.

Confirmation is a control requirement or precondition where applicable, not an additional Trust outcome.

⸻

35. Permission and Ambiguity

Ambiguity can prevent permission from being meaningfully evaluated.

Example:

"Delete the old customer account."

If there are three possible accounts:

Account A
Account B
Account C

Noema cannot reliably determine which resource the permission applies to.

The appropriate Trust result may therefore be:

CLARIFY

rather than guessing.

⸻

36. Permission and Intent Resolution

Intent resolution must produce enough structure to evaluate authorization deterministically.

Conceptually:

Source of Intent
      ↓
Candidate Intent
      ↓
Hard Schema Validation
      ↓
Admitted Intent
      ↓
Target Resolution
      ↓
Requested Action
      ↓
Permission / Authorization Evaluation

For consequential Actions, the actor, requested Action, exact target resource, and relevant scope must be resolved before authorization can be meaningfully evaluated.

An unresolved target must not be silently selected by the model.

⸻

37. Permission and Organizational Boundaries

Permissions must be evaluated in organizational context.

Example:

Permission:
approve_invoice
Organization:
Nigeria Finance

Action:

Invoice owned by Germany Finance

The permission may not apply.

Organizational scope therefore acts as an authorization constraint.

Organizational membership remains distinct from authorization.

⸻

38. Permission and Data Boundaries

A permission to perform an Action does not necessarily imply permission to expose every item of data required to perform it.

For example:

Permission:
approve_invoice

does not automatically imply access to:

employee payroll information

Data access remains separately governed by enterprise data boundaries, permissions, policies, and applicable Trust conditions.

Therefore:

Action Permission ≠ Universal Data Access

⸻

39. Permission and Agents

Noema should operate under explicit agent authority.

Conceptually:

Human Principal
      ↓
Delegation / Agent Authority
      ↓
Noema
      ↓
Permission / Authorization
      ↓
Action

The authority available to Noema must be explicitly bounded.

A human initiating an Intent does not automatically grant Noema all of that human’s permissions.

⸻

40. Permission Escalation

Noema must never silently escalate privileges.

Invalid behavior:

Action requires permission X
        ↓
No permission
        ↓
Noema finds permission Y
        ↓
attempts Action anyway

Instead:

permission unavailable
        ↓
deterministic Trust evaluation
        ↓
policy-defined outcome

Potential outcomes include:

REJECT
ESCALATE
CLARIFY

EXECUTE must not be produced merely because some unrelated permission exists.

⸻

41. Permission Inference

Noema must distinguish explicit authorization from inferred authorization.

Explicit:

IAM:
Alice → approve_invoice

Inferred:

Alice is a Finance Manager
therefore probably can approve invoices

The second is not sufficient authorization evidence unless the enterprise authorization model explicitly defines that relationship.

Model inference may generate a candidate mapping, but it cannot establish enterprise authority.

⸻

42. Model Confidence Is Not Permission

A model may produce:

Alice probably has authority to approve this.

This is not a permission.

Noema must never transform:

model confidence

into:

enterprise authorization

Model confidence is interpretation metadata, not Fact Status and not authority.

⸻

43. Permission Evidence

Permission evidence may come from:

IAM
RBAC
ABAC
PBAC
ACL
OAuth scopes
service authorization
delegation records
enterprise policy engines

Noema should preserve the source semantics and provenance.

Authentication credentials or tokens must not be treated as generic permission records, and model-generated claims must not become authoritative merely because they conform to a schema.

⸻

44. RBAC

In Role-Based Access Control:

User
 ↓
Role
 ↓
Permission

Example:

Alice
→ Finance Manager
→ approve_invoice

Noema may consume the resulting effective authorization.

The role relationship itself is not sufficient unless the enterprise authorization model defines it as granting the relevant permission.

⸻

45. ABAC

In Attribute-Based Access Control:

Principal Attributes
+
Resource Attributes
+
Action
+
Environment
→ Authorization Decision

Example:

Department = Finance
Region = Nigeria
Amount < $10,000

Noema’s Context model must be capable of carrying the attributes necessary to evaluate or transmit the enterprise authorization request.

These attributes must have appropriate provenance, authority, freshness, and Fact Status where applicable.

⸻

46. Policy-Based Authorization

Some enterprises centralize authorization in a policy engine.

In that architecture:

Noema
   ↓
Authorization Request
   ↓
Enterprise Policy Engine
   ↓
ALLOW / DENY / UNKNOWN

Noema should consume the enterprise decision and relevant evidence rather than unnecessarily reconstructing the enterprise’s entire authorization system.

Where the provider is authoritative for the requested authorization decision, Noema should preserve that authority relationship and the decision context.

⸻

47. Permission Decision

An enterprise authorization evaluation may produce:

ALLOW
DENY
UNKNOWN

These are authorization-provider semantics, not Noema’s canonical Trust outcomes.

Noema must not reinterpret:

UNKNOWN

as:

ALLOW

An authorization result of UNKNOWN must be handled according to Trust, policy, risk, and execution requirements.

⸻

48. Authorization Unavailability

If an authorization provider is unavailable:

Noema
   ↓
authorization check
   ↓
timeout

the result is not necessarily:

ALLOW

It is also not universally required to become:

DENY

The authorization state may be:

UNKNOWN

Policy and risk determine the resulting Trust outcome.

For high-risk operations, fail-closed behavior will often be appropriate.

A timeout is an execution/information condition, not itself a canonical Trust outcome.

⸻

49. Permission and Trust Decision

A simplified Trust evaluation may look like:

Admitted Intent
      ↓
Resolved Actor
      ↓
Resolved Action
      ↓
Resolved Target
      ↓
Permission / Authorization
      ↓
Organizational Scope
      ↓
Policy
      ↓
Reconciled Resource State
      ↓
Preconditions
      ↓
Risk
      ↓
Trust Decision

The canonical Trust outcomes are:

EXECUTE
CLARIFY
ESCALATE
REJECT

EXECUTE means the resolved path satisfies the applicable Trust conditions and is permitted to proceed.

It does not mean execution has succeeded.

⸻

50. Permission and Execution

Execution should carry the authorization context that justified the Action where appropriate.

Example:

Execution
├── intent_version
├── principal
├── effective_principal
├── permission_evidence
├── authorization_decision
├── organizational_scope
├── policy_version
├── action_contract_version
├── action
└── resource

This enables post-execution causal auditability.

Authorization evidence should not be silently mutated after execution. If current authorization changes later, the historical execution record remains historical.

⸻

51. Permission and Auditability

A consequential execution should be able to answer:

Who was authorized?
What Action was authorized?
What resource was targeted?
What permission or authorization decision supported it?
Where did that authority come from?
What organizational scope applied?
What constraints applied?
When was the authorization observed?
Was delegation involved?
Was authorization revalidated?
Which Intent version was evaluated?
Which policy and Action Contract versions applied?

This forms part of Noema’s causal audit trail.

⸻

52. Permission and Multi-Step Actions

A compound Intent may produce multiple Actions.

Example:

"Close the account and refund the remaining balance."

This may become:

Action A:
refund_balance
Action B:
close_account

Authorization must be evaluated for each consequential Action.

Permission for:

refund_balance

does not automatically imply permission for:

close_account

Each Action must retain its own authorization context.

⸻

53. Permission and Compensation

Compensating Actions require appropriate authorization independently of the original Action.

Example:

Original:
create_transfer
Compensation:
cancel_transfer

Noema must not assume:

permission(create_transfer)

implies:

permission(cancel_transfer)

Compensation remains governed execution and must be represented by an explicit Action Contract.

⸻

54. Permission and Human Intervention

When escalation is required:

Noema
   ↓
Human Approver
   ↓
Approval
   ↓
Authorization / Permission
   ↓
Action
   ↓
Execution

The approval should be attributable to the approving principal and their applicable organizational authority.

Approval is not itself a universal permission grant. Its effect is determined by enterprise policy and the applicable Action Contract.

⸻

55. Permission and Long-Running Execution

For long-running executions, permission validity may change.

Example:

10:00
permission = valid
12:00
permission revoked
13:00
execution resumes

Policy may require authorization revalidation before the final Action.

Revalidation should evaluate the current authorization state rather than rewriting the historical authorization decision.

⸻

56. Permission and Delegation Chains

Delegation may form a chain:

CEO
 ↓
VP Finance
 ↓
Finance Manager
 ↓
Noema

Noema should preserve the delegation chain where it affects authority.

The chain must not create more authority than the delegator could legitimately grant.

Where delegation is temporal, scoped, or purpose-specific, those constraints must remain attached to the effective authority.

⸻

57. Maximum Delegated Authority

A useful invariant is:

Delegated Authority
≤
Delegator's Effective Authority

Delegation may narrow authority but must not expand the authority available to the delegate beyond what the enterprise authorization model permits.

This applies recursively to delegation chains.

⸻

58. Permission Boundary

The permission boundary is where enterprise authorization semantics become an input to Noema’s deterministic Trust evaluation.

Conceptually:

Enterprise Authorization
          │
          │
          ▼
Permission / Authorization Evidence
          │
          ▼
Hard Schema Validation / Admission
          │
          ▼
State Reconciliation where required
          │
          ▼
Noema Trust
          │
     ┌────┼────┐
     ▼    ▼    ▼
  Context Policy Risk
     │    │    │
     └────┼────┘
          ▼
      Trust Decision
          │
          ▼
      Action Contract
          │
          ▼
       Execution

Noema does not become the enterprise authorization source of truth merely because it consumes permission information.

⸻

59. Permission Evidence and Fact Status

Permission evidence must be distinguished from Fact Status.

Fact Status describes the epistemic status of a relevant claim:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

For example:

Permission claim:
Alice may approve invoice #123
Evidence:
Enterprise IAM authorization response
Fact Status:
VERIFIED

A model confidence score is not a Fact Status.

Likewise:

Fact Status = UNKNOWN

must not be converted into:

Permission = ALLOW

Fact Status, Evidence, Permission, Authorization Decision, and Trust Decision are distinct concepts.

⸻

60. Permission and State Reconciliation

Permission-related enterprise state may change across multiple authoritative systems.

Examples include:

identity provider
HR system
IAM
policy engine
resource system
organization directory
delegation service

Where authorization depends on multiple observations, Noema may use State Reconciliation to establish the current relevant claims.

Conceptually:

Enterprise Authorization Sources
          ↓
Observations
          ↓
Hard Schema Validation / Admission
          ↓
State Reconciliation
          ↓
Reconciled Claims / Fact Status / Evidence
          ↓
Authorization Evaluation
          ↓
Trust

Reconciliation does not create enterprise authority. It determines which observed claims can currently be treated as reconciled inputs under the applicable authority model.

⸻

61. Permission and Unknown State

Unknown authorization state is first-class.

Examples:

authorization provider unavailable
delegation status unknown
permission expiration unknown
resource scope unresolved
conflicting authorization sources
current role membership unknown

Noema must not guess.

Depending on the Action and policy, an unknown authorization condition may lead to:

CLARIFY
ESCALATE
REJECT

or prevent execution until the required evidence becomes available.

EXECUTE must require the applicable authorization conditions to be established, not merely assumed.

⸻

62. Permission, Intent Versioning, and Immutability

Consequential authorization evaluation must reference the exact Intent Object version being evaluated.

Once an Intent is admitted to Trust, it is immutable.

If clarification or material change produces a new semantic request:

Intent v1
   ↓
CLARIFICATION
   ↓
Intent v2
   ↓
supersedes v1

The authorization evaluation for v1 must not silently become an authorization evaluation for v2.

Each material Intent version must be evaluated against its own resolved actor, Action, target, context, and applicable authorization conditions.

⸻

63. Permission and Resolved Identity

Permission evaluation requires the relevant actor and target identity to be resolved for consequential execution.

The authorization record should preserve, where applicable:

initiating_principal
effective_principal
delegator
delegate
actor
subject
target_resource
resolution_identity
resolution_version
scope

An agent acting on behalf of a human must not erase the human’s initiating identity or become indistinguishable from the human.

Identity resolution and authorization remain separate stages.

⸻

64. Permission and the Enterprise Action Graph

The Enterprise Action Graph may represent relationships such as:

Principal
   ↓
Organization
   ↓
Capability
   ↓
Action
   ↓
Resource

It may also represent policy, integration, workflow, and system relationships.

Graph relationships are useful for planning and authorization context, but graph representation alone does not establish enterprise authority.

The authority of a relationship depends on its source, provenance, scope, temporal validity, and enterprise semantics.

The Planner may use the graph only within the bounds of the Capability Registry, Action Contracts, and Trust decision.

⸻

65. Permission and Capability Registry

A Permission does not create a Noema Capability.

Conversely, a registered Capability does not establish that a particular principal is authorized to use it.

The execution boundary therefore requires both:

Enterprise Authorization
        +
Noema Capability / Action Contract
        +
Trust Conditions
        ↓
Permitted Execution Path

The Planner cannot:

invent a capability
invent a permission
invent authority
modify an Action Contract
bypass Trust

⸻

66. Permission and Security Boundary

Permission evaluation must be structurally separated from model authority.

The following are untrusted inputs until appropriately validated and admitted:

user input
model output
retrieved enterprise text
tool responses
external messages

The model must not receive credentials merely to determine authorization, and it must not directly invoke enterprise systems outside explicit capability and integration boundaries.

No free-form model output may become executable authorization.

The executor must revalidate applicable execution constraints rather than trusting model-generated claims.

⸻

67. Canonical Permission Model

                       Principal
                           │
                           ▼
                      Permission
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       Action           Resource          Scope
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                      Constraints
                           │
                           ▼
                        Validity
                           │
                           ▼
                  Source / Authority
                           │
                           ▼
                 Permission Evidence
                           │
                           ▼
             Authorization Evaluation
                           │
                           ▼
              State / Context Reconciliation
                           │
                           ▼
                    Noema Trust
                           │
                           ▼
                 Action Contract
                           │
                           ▼
                      Execution

⸻

68. Canonical Permission Chain

For a consequential Action, the causal chain should be representable as:

Source of Intent
      ↓
Intent Object Version
      ↓
Resolved Principal / Actor
      ↓
Resolved Action
      ↓
Resolved Target Resource
      ↓
Enterprise Authorization Source
      ↓
Permission / Authorization Observation
      ↓
Hard Schema Validation / Admission
      ↓
State Reconciliation where required
      ↓
Fact Status / Evidence
      ↓
Authorization Evaluation
      ↓
Policy / Scope / Preconditions
      ↓
Trust Decision
      ↓
Action Contract
      ↓
Execution
      ↓
Verification
      ↓
Outcome / Audit

This preserves the distinction between:

authority
evidence
authorization
Trust
execution
outcome

⸻

69. Canonical Invariants

Invariant 1

A permission is evidence of authority, not a guarantee of execution.

Invariant 2

Capability and permission are distinct.

Invariant 3

Role and permission are distinct.

Invariant 4

Permission and authorization decision are distinct.

Invariant 5

Permission and Trust are distinct.

Invariant 6

Permissions must have an identifiable principal or explicitly defined non-human subject.

Invariant 7

Permissions may be constrained by organizational scope.

Invariant 8

Permissions may be constrained by resource scope.

Invariant 9

Permissions may be constrained by time, environment, resource state, or other enterprise attributes.

Invariant 10

Explicit enterprise authorization takes precedence over model inference.

Invariant 11

Model confidence must never be treated as permission evidence or authority.

Invariant 12

Noema must not silently escalate privileges.

Invariant 13

Delegation must not expand beyond the delegator’s effective authority.

Invariant 14

Compensating Actions require appropriate authorization independently of the original Action.

Invariant 15

Permissions may become stale and must be revalidated where policy, risk, or Action semantics require.

Invariant 16

Authorization-provider failure must not be interpreted as authorization success.

Invariant 17

Permission provenance should be preserved for consequential Actions.

Invariant 18

Multi-step execution requires authorization for each consequential Action.

Invariant 19

Organizational membership does not automatically imply permission.

Invariant 20

A permission does not override business-state constraints, Preconditions, or enterprise Policy.

Invariant 21

Permission evidence must not be treated as authoritative merely because it has been persisted by Noema.

Invariant 22

Hard schema validation and admission must occur before externally supplied authorization data is used as canonical Noema input.

Invariant 23

Fact Status is distinct from Permission, Evidence, Authorization Decision, and Trust Decision.

Invariant 24

UNKNOWN authorization state must never be silently converted into ALLOW.

Invariant 25

Authority is claim-, resource-, scope-, temporal-, and source-specific; recency alone does not establish authority.

Invariant 26

Consequential authorization must evaluate the fully resolved actor, Action, target resource, and applicable scope.

Invariant 27

A material change to an admitted Intent creates a new Intent version and does not mutate the authorization evaluation of the prior version.

Invariant 28

A permission for one Action does not automatically authorize another Action.

Invariant 29

A permission to perform an Action does not automatically grant access to all data involved in that Action.

Invariant 30

A registered Capability does not imply principal authorization.

Invariant 31

Principal authorization does not create a Noema Capability.

Invariant 32

Planner selection cannot invent authority, permissions, capabilities, or Action Contract semantics.

Invariant 33

Trust EXECUTE does not imply successful enterprise execution or successful business state transition.

Invariant 34

Enterprise authorization remains enterprise-owned; Noema must not silently become the authorization source of truth.

Invariant 35

Delegation chains must preserve the initiating principal, effective principal, scope, constraints, and validity where they affect authority.

Invariant 36

Human approval does not automatically create unrestricted permission; its effect is determined by enterprise policy and the applicable Action Contract.

Invariant 37

Permission-related enterprise state may require State Reconciliation before consequential authorization can be evaluated.

Invariant 38

Historical authorization observations and decisions must remain distinguishable from current authorization state.

Invariant 39

Replay of authorization observations must not silently recreate authorization or execute an Action.

Invariant 40

Authorization evaluation must be reproducible from the relevant Intent version, principal resolution, authorization evidence, policy, scope, resource state, and applicable contract versions.

Invariant 41

No model-generated authorization claim may cross the Trust boundary as authoritative permission without an explicit enterprise authority source and deterministic admission.

Invariant 42

Read-only permission does not imply absence of Trust requirements when the requested observation is consequential.

Invariant 43

Permission constraints must not be silently discarded when converting enterprise authorization data into Noema Context or Trust inputs.

Invariant 44

A timeout or unavailable authorization source is an information condition and must be handled according to policy; it is not itself a canonical Trust outcome.

Invariant 45

Noema may consume enterprise authorization semantics, but it must not silently replace, broaden, or redefine them.

⸻

70. Final Definition

Permissions are enterprise-defined expressions of authority that establish which principals may perform particular operations on particular resources within particular scopes, constraints, environments, and validity conditions.

For Noema:

Enterprise Authorization
        ↓
Permission / Authorization Evidence
        ↓
Validation / Admission
        ↓
State Reconciliation where required
        ↓
Authorization Evaluation
        ↓
Deterministic Trust
        ↓
Action Contract
        ↓
Execution
        ↓
Verification
        ↓
Outcome

The key distinction is:

The enterprise defines who is authorized to perform what, under which conditions. Noema consumes that authority as an explicit, attributable input and determines whether a specific resolved Intent can safely and deterministically proceed through the Trust and execution boundary.

Noema does not invent permissions, infer authority from model confidence, silently escalate privileges, or replace the enterprise authorization source of truth.

The permission boundary therefore preserves a fundamental Noema separation:

Enterprise
→ defines authority and business authorization
Noema
→ validates, reconciles, evaluates, governs, executes, verifies, and audits the specific execution journey

This makes Permission a first-class enterprise input to deterministic Trust without collapsing Permission, Authorization, Trust, Execution, or Outcome into the same concept.