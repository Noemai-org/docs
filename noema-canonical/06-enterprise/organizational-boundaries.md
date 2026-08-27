Organizational Boundaries

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: 06-enterprise/organizational-boundaries.md

⸻

1. Definition

Organizational Boundaries define the organizational scope within which an Intent, Actor, Resource, Policy, Capability, and Execution are valid.

Enterprise authority is rarely flat.

An organization may contain:

Enterprise
├── Business Unit
├── Division
├── Department
├── Team
├── Region
├── Legal Entity
└── Project

An Actor may have authority in one part of that structure without having authority across the entire enterprise.

Noema must therefore understand organizational scope as an explicit constraint on execution.

⸻

2. Purpose

Organizational Boundaries prevent a valid identity or capability from being interpreted as having unrestricted enterprise authority.

For example:

Alice
└── Finance / Nigeria
    └── Accounts Payable

Alice may be authorized to approve invoices for:

Nigeria / Accounts Payable

without being authorized to approve:

US / Accounts Payable

Therefore:

Identity ≠ Organizational Authority

⸻

3. Core Principle

Authority is scoped by organizational context unless explicitly established otherwise.

Noema should evaluate:

Who is acting?
        +
Where does their authority apply?
        +
What resource is affected?
        +
What does policy permit?

before treating an Action as executable.

⸻

4. Organization as Enterprise Context

Organizational structure is part of the Context available to Trust.

Example:

Actor:
Alice
Organization:
Acme
Business Unit:
Payments
Department:
Finance
Region:
Nigeria

This context may materially affect authorization and policy evaluation.

⸻

5. Organizational Scope

A principal may have one or more scopes.

Examples:

Global
Regional
Business Unit
Department
Team
Project
Resource-specific

A scope should be explicit where it affects execution.

⸻

6. Global Authority

Some principals may legitimately have enterprise-wide authority.

Example:

Principal:
Global Security Administrator
Scope:
Enterprise

Noema should not infer global authority merely because an Actor has a powerful role.

The enterprise must establish the scope.

⸻

7. Local Authority

Most enterprise authority is narrower.

Example:

Principal:
Finance Manager
Scope:
West Africa Finance

An Action outside that scope may require:

CLARIFY
ESCALATE
REJECT

depending on policy.

⸻

8. Organizational Hierarchy

Noema may need to reason over hierarchical relationships:

Enterprise
   ↓
Region
   ↓
Business Unit
   ↓
Department
   ↓
Team
   ↓
Project

But hierarchy alone does not imply inherited authority.

For example:

Department Manager

does not automatically mean:

may modify every resource belonging to the department

unless enterprise policy establishes that relationship.

⸻

9. Organizational Membership

An identity may belong to multiple organizational units.

Example:

Alice
├── Finance
├── Risk Committee
└── Project Phoenix

Membership and authority are distinct.

Membership ≠ Authorization

⸻

10. Organizational Role

A role describes a function within the organization.

Examples:

Finance Manager
Project Administrator
Security Officer
HR Business Partner

A role may contribute to authorization, but the role itself does not necessarily define the complete permission set.

⸻

11. Role vs Scope

These must remain distinct.

Role:
Finance Manager
Scope:
Nigeria Finance

The same role may exist in several organizational scopes.

Alice:
Finance Manager → Nigeria
Bob:
Finance Manager → United States

Their authority may therefore differ.

⸻

12. Resource Ownership

Resources can belong to organizational units.

Example:

Resource:
Corporate Bank Account
Owner:
Nigeria Finance

An Actor’s ability to operate on that resource may depend on both:

Actor Scope
+
Resource Scope

⸻

13. Resource Organizational Scope

A resource should have an identifiable organizational context where relevant.

Example:

Invoice #4821
Legal Entity:
Acme Nigeria Ltd.
Department:
Procurement
Region:
Nigeria

This context can be necessary for Trust evaluation.

⸻

14. Actor–Resource Scope Matching

A simplified relationship is:

Actor Scope
     +
Resource Scope
     ↓
Policy Evaluation

For example:

Actor:
Finance / Nigeria
Resource:
Finance / Nigeria
Result:
potentially in scope

Whereas:

Actor:
Finance / Nigeria
Resource:
Finance / Germany
Result:
requires additional authorization

This is not itself an authorization decision; it is an important Trust input.

⸻

15. Legal Entity Boundaries

Enterprise organizations may contain multiple legal entities.

Example:

Acme Group
├── Acme Nigeria Ltd.
├── Acme UK Ltd.
└── Acme US Inc.

These entities may have separate:

accounts
employees
contracts
policies
regulatory obligations

Noema must not assume that group membership eliminates legal-entity boundaries.

⸻

16. Business Unit Boundaries

Business units may operate independently.

Example:

Acme
├── Payments
├── Logistics
├── Insurance
└── Retail

A capability available within Payments should not automatically become available within Retail.

⸻

17. Department Boundaries

Departments can define meaningful operational authority.

Examples:

Finance
HR
Legal
Engineering
Security
Operations

Policies may explicitly restrict Actions by department.

⸻

18. Team Boundaries

Team membership may further constrain access.

Example:

Engineering
└── Payments Team

An engineer belonging to:

Search Team

should not automatically gain authority over:

Payments Team resources

⸻

19. Project Boundaries

Projects may establish temporary organizational scopes.

Example:

Project Phoenix
├── Alice
├── Bob
└── Carol

Project membership may grant access to project resources without granting enterprise-wide authority.

⸻

20. Geographic Boundaries

Organizations may scope authority geographically.

Examples:

Nigeria
West Africa
EMEA
North America
Global

Geographic scope may affect:

authorization
policy
regulatory requirements
data residency
execution capabilities

⸻

21. Regulatory Boundaries

Organizational boundaries may correspond to regulatory jurisdictions.

For example:

Legal Entity:
Acme Nigeria Ltd.
Jurisdiction:
Nigeria

An Action may therefore be subject to different policies from an otherwise identical Action in another jurisdiction.

Noema should treat jurisdiction as enterprise-provided Context rather than infer legal authority itself.

⸻

22. Organizational Boundaries and Data

Organizational scope can constrain data visibility.

Example:

Finance / Nigeria

may access:

Nigeria financial records

but not necessarily:

Finance / Germany

Data boundaries therefore intersect organizational boundaries.

⸻

23. Organizational Boundaries and Identity

Identity establishes the principal.

Organizational boundaries establish where that principal belongs or operates.

Identity
   ↓
Organizational Membership
   ↓
Organizational Scope
   ↓
Authorization

⸻

24. Organizational Boundaries and Capability

A Capability describes an available operation.

Organizational scope may determine where that Capability can be exercised.

Example:

Capability:
approve_invoice
Scope:
Nigeria Finance

The existence of the Capability does not imply:

approve any invoice anywhere

⸻

25. Organizational Boundaries and Policy

Policy may explicitly encode organizational scope.

Example:

Policy:
Finance Managers may approve invoices
up to $10,000 within their assigned legal entity.

The relevant dimensions are:

Role
+
Amount
+
Organization
+
Legal Entity

⸻

26. Organizational Boundaries and Trust

Trust must consider organizational scope when scope affects risk or authorization.

Conceptually:

Identity
   +
Organization
   +
Resource
   +
Action
   +
Policy
   ↓
Trust

⸻

27. Organizational Boundaries and Intent

Users frequently omit organizational context.

Example:

“Approve the invoice.”

Noema may need to determine:

Which invoice?
Which legal entity?
Which department?
Which organizational scope?

If the organizational context is ambiguous and consequential:

CLARIFICATION_REQUIRED

may be necessary.

⸻

28. Organizational Ambiguity

Example:

Intent:
"Approve the Acme invoice."
Candidates:
Invoice A
→ Acme Nigeria Ltd.
Invoice B
→ Acme UK Ltd.

If the Actor’s authority differs across these entities, the ambiguity becomes a Trust concern.

Noema should not resolve it merely by choosing the most likely invoice.

⸻

29. Cross-Organizational Actions

Some Actions intentionally cross boundaries.

Example:

Nigeria Finance
       ↓
requests
       ↓
US Finance resource

Cross-boundary operations may require:

additional authorization
delegation
approval
policy evaluation
human intervention

depending on enterprise rules.

⸻

30. Organizational Delegation

Authority may be delegated across organizational boundaries.

Example:

Global Finance
      ↓
delegates
      ↓
Nigeria Finance

Delegation should specify:

delegator
delegate
scope
capability
constraints
duration

⸻

31. Temporary Organizational Scope

Authority may be temporary.

Example:

Alice
Scope:
Project Phoenix
Valid:
June 1 → September 30

Noema must consider temporal scope when evaluating an Action.

⸻

32. Acting Across Multiple Scopes

An Actor may legitimately operate across multiple organizational scopes.

Example:

Alice
Finance / Nigeria
Security / Global
Project Phoenix

Noema should identify which scope is relevant to the current Action rather than treating all memberships as one undifferentiated authority set.

⸻

33. Organizational Scope Must Be Action-Specific

The relevant scope depends on the Action.

Example:

Action:
approve invoice

may use:

Finance scope

while:

Action:
rotate security credential

may use:

Security scope

An Actor’s authority should therefore be evaluated relative to the requested Action.

⸻

34. Organizational Scope Is Not a Trust Score

Organizational information should not be reduced to:

trust = 0.93

Instead, it should be represented as structured evidence:

Actor:
Alice
Department:
Finance
Scope:
Nigeria
Resource:
Nigeria Finance
Relationship:
authorized_for

The Trust Engine then evaluates the evidence deterministically according to policy.

⸻

35. Organizational Boundary Violation

Potential violations include:

cross-department access
cross-legal-entity operation
cross-region access
cross-business-unit execution
cross-project access
expired delegation
invalid membership
out-of-scope resource

These should be detectable before execution.

⸻

36. Organizational Boundary vs Data Boundary

These concepts interact but are not identical.

Organizational Boundary

Defines:

Where authority applies.

Data Boundary

Defines:

What data may be accessed, processed, retained, or exposed.

Example:

Actor:
Finance / Nigeria
Data:
Nigeria customer financial records

Both boundaries must be satisfied.

⸻

37. Organizational Boundary vs Authorization

Organizational scope is an input to authorization, not necessarily authorization itself.

Organization:
Nigeria Finance
Role:
Manager
Capability:
approve_invoice
Authorization:
ALLOWED

The final authorization result must come from the enterprise’s authorization mechanism or policy evaluation.

⸻

38. Organizational Boundary vs Identity

Identity answers:

Who is Alice?

Organizational boundary answers:

Where does Alice have authority?

These should never be conflated.

⸻

39. Organizational Boundary vs Resource

Resources may themselves have organizational scope.

Resource
   ↓
belongs_to
   ↓
Organization

Noema may need this relationship to evaluate whether an Action is in scope.

⸻

40. Organizational Boundary vs Business State

Business State remains authoritative in enterprise systems.

For example:

Invoice:
legal_entity = Acme Nigeria Ltd.

Noema consumes that fact.

It does not redefine the organizational ownership of the invoice.

⸻

41. Organizational Boundary and Enterprise Action Graph

The Enterprise Action Graph may contain organizational relationships:

Organization
   ↓
owns
   ↓
Resource
Organization
   ↓
grants
   ↓
Capability
Identity
   ↓
member_of
   ↓
Organization

These relationships can contribute to Trust evaluation.

⸻

42. Organizational Boundary and Context

Relevant organizational context may include:

organization_id
business_unit
department
team
project
legal_entity
region
jurisdiction
membership
scope
delegation

Only relevant dimensions should be loaded for the current Intent.

⸻

43. Organizational Boundary and Model Context

The model may need organizational context to resolve references.

Example:

“Send this to our London team.”

Relevant context might be:

London Team
→ Engineering
→ UK

The model should not receive unrelated organizational data.

⸻

44. Organizational Boundary and Clarification

When organizational scope changes the possible execution path, ambiguity should become explicit.

Example:

“Move the account to our other company.”

If multiple legal entities are possible:

CLARIFY

rather than guessing.

⸻

45. Organizational Boundary and Human Intervention

Some cross-boundary operations may require human approval.

Example:

Actor:
Nigeria Finance Manager
Action:
transfer funds from US legal entity
Trust:
requires elevated approval
Result:
ESCALATE

The approving human’s identity and organizational scope must be recorded.

⸻

46. Organizational Boundary and Execution

Execution should preserve the organizational context under which the Action was authorized.

Example:

Action:
approve_invoice
Authorized Scope:
Nigeria Finance
Execution:
invoice_123

If the execution target changes to another organizational scope, the Action should be revalidated where required.

⸻

47. Organizational Boundary Changes During Execution

Organizations change.

Examples:

department reassignment
business-unit transfer
project closure
legal-entity restructuring
delegation expiration

Noema should not assume organizational Context remains permanently valid throughout a long-running execution.

For consequential Actions, policy may require revalidation.

⸻

48. Organizational Boundary and Long-Running Execution

For an execution that spans hours or days:

Intent
 ↓
Trust
 ↓
Waiting
 ↓
Approval
 ↓
Execution

organizational authority may change between stages.

The execution model should therefore distinguish:

authority observed at Trust time

from:

authority required at execution time

where the Action is sufficiently consequential.

⸻

49. Organizational Boundary Failure

If an Action falls outside the Actor’s organizational scope:

Actor Scope
     ↓
Resource Scope
     ↓
Mismatch

Noema must not compensate by:

guessing broader authority
using another identity
bypassing policy
using cached authorization

The correct outcome is policy-defined.

⸻

50. Cross-Boundary Data Leakage

Organizational boundaries also constrain data flow.

For example:

Nigeria HR

should not automatically expose employee records to:

US Sales

merely because both belong to the same enterprise.

Data access must satisfy both:

data policy
+
organizational scope

⸻

51. Organizational Isolation in Multi-Tenant Systems

In some deployments, organizational units may effectively function as tenant boundaries.

Noema should not assume:

same parent enterprise

means:

same operational authority

Tenant and organizational boundaries should remain explicit.

⸻

52. Organizational Boundary as a Constraint

A useful conceptual representation is:

Constraint:
organizational_scope
Subject:
Actor
Required Scope:
Finance / Nigeria
Observed Scope:
Finance / Nigeria
Result:
SATISFIED

or:

Required:
Finance / Germany
Observed:
Finance / Nigeria
Result:
NOT_SATISFIED

⸻

53. Organizational Scope as Evidence

Trust should be able to reference evidence such as:

Membership:
Alice ∈ Finance Nigeria
Delegation:
Alice → Project Phoenix
Resource ownership:
Invoice ∈ Nigeria Finance
Policy:
Finance Managers may approve within assigned entity

This makes organizational reasoning explainable.

⸻

54. Organizational Boundary and Auditability

A consequential execution should make it possible to answer:

Which organization did the Actor belong to?
Which organizational scope authorized the Action?
Which organization owned the resource?
Which policy permitted the operation?
Did the Action cross an organizational boundary?
Was additional approval required?

⸻

55. Canonical Organizational Relationship Model

                 Enterprise
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Business Unit   Legal Entity   Region
        │            │            │
        ▼            ▼            ▼
   Department      Resources     Policies
        │
        ▼
       Team
        │
        ▼
      Project
        │
        ▼
      Actor

These relationships form part of the enterprise context in which Intent is executed.

⸻

56. Canonical Authority Model

Identity
   │
   ▼
Organizational Membership
   │
   ▼
Organizational Scope
   │
   ├──────────────┐
   ▼              ▼
Capability      Resource Scope
   │              │
   └──────┬───────┘
          ▼
       Policy
          │
          ▼
         Trust
          │
          ▼
        Action

⸻

57. Canonical Invariants

Invariant 1

Organizational scope is an explicit part of enterprise Context where it affects execution.

Invariant 2

Identity does not imply enterprise-wide authority.

Invariant 3

Organizational membership does not automatically imply authorization.

Invariant 4

Role and organizational scope are separate concepts.

Invariant 5

A Capability does not imply unrestricted organizational scope.

Invariant 6

Resource ownership and Actor authority must be evaluated in their organizational context.

Invariant 7

Legal-entity boundaries must remain explicit where they affect authority, policy, or regulatory obligations.

Invariant 8

Cross-organizational Actions must be evaluated explicitly rather than treated as ordinary in-scope Actions.

Invariant 9

Delegated authority must preserve its organizational scope and duration.

Invariant 10

Temporary organizational authority must have an explicit validity period where applicable.

Invariant 11

An Actor may have multiple organizational scopes, but the relevant scope must be determined relative to the current Action.

Invariant 12

Organizational context must not be collapsed into a probabilistic model score.

Invariant 13

Organizational ambiguity that materially affects execution must transition into deterministic clarification or another policy-defined state.

Invariant 14

Organizational boundaries constrain data access as well as Action authorization.

Invariant 15

The model may use organizational Context for Intent resolution but cannot establish organizational authority by inference.

Invariant 16

Business State remains authoritative for organizational relationships represented in enterprise systems.

Invariant 17

Organizational authority may change during long-running execution and must be revalidated where policy requires.

Invariant 18

Noema must not bypass organizational boundaries through another identity, integration, cache, or inferred authority.

Invariant 19

Human intervention across organizational boundaries must preserve the approving principal and organizational scope.

Invariant 20

Audit records for consequential Actions must preserve the organizational scope under which the Action was authorized.

⸻

58. Final Definition

Organizational Boundaries define where enterprise authority applies. They connect identities, organizational memberships, resources, capabilities, policies, and legal or operational scopes so that Noema can determine whether an Intent and its resulting Actions are valid within the organization in which they occur.

The essential distinction is:

IDENTITY
Who are you?
      ↓
ORGANIZATION
Where do you belong?
      ↓
SCOPE
Where does your authority apply?
      ↓
RESOURCE
What organizational domain does it belong to?
      ↓
POLICY
What is permitted here?
      ↓
TRUST
Is this execution justified?
      ↓
ACTION
What should happen?
      ↓
EXECUTION
Perform it within the established boundary.

Noema should never interpret enterprise authority as a single global permission space. Authority has shape: organizational, temporal, resource, and policy boundaries. Those boundaries are part of the execution semantics.