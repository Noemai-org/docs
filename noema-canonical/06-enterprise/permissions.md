Permissions

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: 06-enterprise/permissions.md

⸻

1. Definition

Permissions define the operations an identity or principal is allowed to perform on enterprise resources under specified organizational, contextual, and policy constraints.

Permissions answer:

“Is this principal permitted to perform this operation on this resource in this context?”

They are one of the enterprise facts that Noema consumes when evaluating Trust.

Permissions are not the same as Intent, Capability, Role, Policy, or Trust.

⸻

2. Purpose

Noema needs permissions to determine whether a proposed Action can legitimately cross the enterprise boundary.

The conceptual flow is:

Intent
   ↓
Intent Resolution
   ↓
Action
   ↓
Permission Evaluation
   ↓
Trust
   ↓
Execution

However, Noema should not assume that possession of a permission alone makes an Action executable.

Other constraints may still apply:

Policy
Resource State
Organizational Scope
Risk
Preconditions
Approval Requirements
Data Boundaries

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

The effective authority may instead be:

refund_payment
+
Finance / Nigeria
+
≤ $5,000
+
active account
+
approved payment state

⸻

4. Permission vs Capability

These concepts must remain distinct.

Capability

Describes:

What the enterprise system can do.

Example:

cancel_subscription

Permission

Describes:

Who is allowed to invoke that capability under defined conditions.

Example:

Alice
→ permitted to cancel subscriptions

Therefore:

Capability ≠ Permission

⸻

5. Permission vs Role

A Role groups organizational responsibility or authority.

Example:

Role:
Finance Manager

A permission may be associated with that role:

Finance Manager
→ approve_invoice

But Noema should not assume the role itself is sufficient evidence of permission unless the enterprise authorization system establishes that relationship.

⸻

6. Permission vs Authorization

Authorization is the process or decision of determining whether an operation is allowed.

Permission is one of the facts that may contribute to that decision.

Permission
    +
Resource
    +
Context
    +
Policy
    ↓
Authorization Decision

⸻

7. Permission vs Trust

Trust is broader than permission.

A principal may have permission while the Action remains unsafe or unresolved.

Example:

Permission:
transfer_funds = allowed
Intent:
"Transfer $50,000 to John."
Problem:
multiple Johns identified

The permission is valid, but Intent ambiguity prevents safe execution.

Therefore:

Permission ≠ Trust

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

⸻

9. Principal

A permission must identify its subject.

The principal may be:

human
service
application
agent
role
group
organization
delegated identity

Where possible, the effective principal should resolve to a concrete identity or explicitly defined non-human principal.

⸻

10. Human Permissions

Example:

Alice
→ approve_invoice
→ Finance / Nigeria

Noema consumes this authorization information rather than inventing it.

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

because their authority and audit semantics may differ.

⸻

12. Agent Permissions

AI agents may also operate under explicit permissions.

Example:

Noema Agent
→ cancel_subscription
→ Customer Support

An agent should not inherit unrestricted human authority simply because a human initiated the Intent.

⸻

13. Delegated Permissions

A principal may delegate authority.

Example:

Alice
   ↓ delegates
Noema
   ↓
refund_payment

The delegation should preserve:

delegator
delegate
permission
scope
constraints
validity

Delegation must not silently expand authority.

⸻

14. Permission Scope

Permissions may be scoped by:

organization
legal entity
region
department
team
project
resource
resource type
tenant
environment

Example:

Permission:
approve_invoice
Scope:
Acme Nigeria Ltd.

This does not imply authority over:

Acme UK Ltd.

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

Resource-level permissions are often the strongest form of authorization evidence because they minimize scope.

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

Therefore permission evaluation may require enterprise Context.

⸻

18. Conditional Permissions

Example:

Permission:
refund_payment
Condition:
amount <= $1,000

Then:

Refund $500
→ permitted
Refund $5,000
→ not permitted under this permission

The permission itself has not changed; the Action falls outside its constraint.

⸻

19. Temporal Permissions

Permissions may be time-bound.

Example:

Alice
→ production_access
Valid:
August 1 → August 31

After expiration:

Permission:
inactive

Noema must not rely on stale authorization data for consequential operations.

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

Noema should preserve the source representation rather than collapsing everything into a simplistic boolean where the distinction matters.

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

Noema should retain the provenance of the effective permission when possible.

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

This makes Trust decisions auditable.

⸻

25. Effective Permission

The effective permission is the permission actually applicable to the current Action.

Example:

Principal:
Alice
Permission:
approve_invoice
Scope:
Nigeria Finance
Action:
approve Invoice #123

The effective permission exists only if the Action satisfies all relevant constraints.

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

the resulting authority is the effective authority.

This is preferable to treating permissions as additive without boundaries.

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

An explicit deny must not be overridden merely because another permission says “allow.”

Noema should defer to the enterprise authorization semantics rather than impose its own deny precedence universally.

⸻

28. Permission Revocation

Permissions can be revoked.

Example:

Alice
→ approve_invoice

is revoked at:

14:00

A cached permission from:

13:30

may no longer be sufficient for a consequential execution at:

14:15

Freshness requirements therefore matter.

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

Noema should validate relevant permissions when required by risk or policy.

⸻

30. Permission Freshness

Permission data should have associated provenance and freshness where practical.

Conceptually:

Permission
   ├── source
   ├── observed_at
   ├── expires_at
   └── version

A high-risk Action may require fresher authorization evidence than a low-risk Action.

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

Result:

REJECT

⸻

32. Permission and Preconditions

Permissions establish authority.

Preconditions establish whether execution can occur given current state.

Permission
→ may you do it?
Precondition
→ can it be done now?

Both may be required.

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

⸻

34. Permission and Risk

The existence of permission does not eliminate risk.

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

⸻

35. Permission and Ambiguity

Ambiguity can prevent permission from being meaningfully evaluated.

Example:

“Delete the old customer account.”

If there are three possible accounts:

Account A
Account B
Account C

Noema cannot reliably determine which resource the permission applies to.

The correct response may be:

CLARIFY

rather than guessing.

⸻

36. Permission and Intent Resolution

Intent resolution should produce enough structure to evaluate permissions.

Natural Language
      ↓
Intent
      ↓
Target Resource
      ↓
Requested Action
      ↓
Permission Evaluation

If the target resource remains unresolved, authorization may be impossible to establish deterministically.

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

Organizational scope therefore acts as an important authorization constraint.

⸻

38. Permission and Data Boundaries

A permission to perform an Action does not necessarily imply permission to expose all data required to perform it.

For example:

Permission:
approve_invoice

does not automatically imply access to:

employee payroll information

Data access must remain separately governed.

⸻

39. Permission and Agents

Noema should operate under explicit agent authority.

Conceptually:

Human Principal
      ↓
Delegation
      ↓
Noema
      ↓
Permission
      ↓
Action

The delegation should define the maximum authority Noema can exercise.

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
policy-defined outcome

such as:

REJECT
ESCALATE
CLARIFY

⸻

41. Permission Inference

Noema must distinguish explicit permission from inferred permission.

Explicit

IAM:
Alice → approve_invoice

Inferred

Alice is a Finance Manager
therefore probably can approve invoices

The second is not sufficient authorization evidence unless the enterprise’s authorization model explicitly defines that relationship.

⸻

42. Model Confidence Is Not Permission

A model may produce:

Alice probably has authority to approve this.

This is not a permission.

Noema must not transform:

model confidence

into:

enterprise authorization

⸻

43. Permission Evidence

Permission evidence may come from:

IAM
RBAC
ABAC
PBAC
ACL
OAuth scopes
service credentials
delegation records
enterprise policy engines

Noema should preserve the source semantics.

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

Noema’s Context model should be capable of carrying the attributes necessary for enterprise authorization.

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
ALLOW / DENY

Noema should consume the decision and its relevant evidence rather than reconstructing the enterprise’s entire authorization system unnecessarily.

⸻

47. Permission Decision

A permission evaluation may result in:

ALLOW
DENY
UNKNOWN

Where the enterprise authorization system itself returns an uncertain or unavailable result, Noema should not reinterpret that as:

ALLOW

⸻

48. Authorization Unavailability

If the authorization provider is unavailable:

Noema
   ↓
authorization check
   ↓
timeout

the result is not necessarily:

DENY

nor:

ALLOW

It may be:

AUTHORIZATION_UNKNOWN

Policy determines whether execution can continue.

For high-risk operations, fail-closed behavior will often be appropriate.

⸻

49. Permission and Trust Decision

A simplified Trust evaluation may look like:

Intent
   ↓
Resolved Action
   ↓
Identity
   ↓
Permission
   ↓
Organizational Scope
   ↓
Policy
   ↓
Resource State
   ↓
Risk
   ↓
Trust Decision

The permission is one component of a larger deterministic decision.

⸻

50. Permission and Execution

Execution should carry the authorization context that justified the Action where appropriate.

Example:

Execution
├── principal
├── permission evidence
├── organizational scope
├── policy version
├── action
└── resource

This enables post-execution auditability.

⸻

51. Permission and Auditability

A consequential execution should be able to answer:

Who was authorized?
What permission allowed it?
Where did that permission come from?
What scope applied?
What constraints applied?
When was the permission observed?
Was delegation involved?
Was authorization revalidated?

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

Permission must be evaluated for each Action.

Permission for:

refund_balance

does not automatically imply:

close_account

⸻

53. Permission and Compensation

Compensating Actions require their own authorization.

Example:

Original:
create_transfer
Compensation:
cancel_transfer

Noema must not assume:

permission(create_transfer)

implies:

permission(cancel_transfer)

⸻

54. Permission and Human Intervention

When escalation is required:

Noema
   ↓
Human Approver
   ↓
Approval
   ↓
Permission / Authorization
   ↓
Execution

The approval should be attributable to the approving principal and their organizational authority.

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

The chain should not create more authority than the original principal possessed.

⸻

57. Maximum Delegated Authority

A useful invariant is:

Delegated Authority
≤
Delegator's Effective Authority

Noema must not gain capabilities through delegation that the delegator could not legitimately grant.

⸻

58. Permission Boundary

The permission boundary is where:

Enterprise Authorization

meets:

Noema Trust

Conceptually:

Enterprise
    │
    │ "This principal may perform X."
    ▼
Permission Evidence
    │
    ▼
Noema Trust
    │
    ├── Context
    ├── Policy
    ├── Risk
    ├── Preconditions
    └── Intent Resolution
    │
    ▼
Execution Decision

⸻

59. Canonical Permission Model

                    Principal
                        │
                        ▼
                    Permission
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       Action        Resource        Scope
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                    Constraints
                        │
                        ▼
                     Validity
                        │
                        ▼
                  Authorization
                        │
                        ▼
                  Noema Trust

⸻

60. Canonical Invariants

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

Permissions must have an identifiable principal.

Invariant 7

Permissions may be constrained by organizational scope.

Invariant 8

Permissions may be constrained by resource scope.

Invariant 9

Permissions may be constrained by time, environment, resource state, or other enterprise attributes.

Invariant 10

Explicit enterprise authorization takes precedence over model inference.

Invariant 11

Model confidence must never be treated as permission evidence.

Invariant 12

Noema must not silently escalate privileges.

Invariant 13

Delegation must not expand beyond the delegator’s effective authority.

Invariant 14

Compensating Actions require appropriate authorization independently of the original Action.

Invariant 15

Permissions may become stale and must be revalidated where policy or risk requires.

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

⸻

61. Final Definition

Permissions are enterprise-defined expressions of authority that establish which principals may perform particular operations on particular resources within particular scopes and constraints.

For Noema:

Permission
    ↓
is evidence
    ↓
Authorization
    ↓
is an input
    ↓
Trust
    ↓
supports
    ↓
Execution

The key distinction is:

The enterprise decides who is allowed to do what. Noema determines whether a specific Intent, under the available evidence and enterprise constraints, can safely become an executable Action.

This keeps authorization where it belongs while making permissions a first-class input into Noema’s deterministic Trust model.