Authorization

Status: Foundational
Version: 0.1
Domain: Trust
Canonical Path: trust/authorization.md

⸻

1. Definition

Authorization is the deterministic evaluation of whether an Actor is permitted to cause a specific Intent to be executed within a given Context.

Authorization answers:

“Is this Actor allowed to cause this Intent?”

It does not answer:

“What does the Actor mean?”

That is Intent Resolution.

It does not answer:

“Can the system technically perform it?”

That is Capability.

It does not answer:

“Should this Intent be executed under all applicable rules?”

That is the broader Trust decision.

⸻

2. Authorization in Noema

Authorization is one component of Noema’s Trust Engine.

The conceptual sequence is:

Actor Expression
      ↓
Candidate Intent
      ↓
Intent Resolution
      ↓
Canonical Intent
      ↓
Capability
      ↓
Authorization
      ↓
Policy
      ↓
Trust Decision
      ↓
Execution

The exact evaluation order may vary by implementation, but authorization must operate on a sufficiently resolved Intent.

⸻

3. Core Principle

Authorization is evaluated against the resolved Intent, not against the Actor’s raw language or the Model’s interpretation.

For example:

User:
"Delete the production database."

The Model may produce:

DeleteDatabase(Database#production)

Noema must first establish that this is in fact the canonical Intent.

Only then should authorization ask:

Can Actor#123 perform DeleteDatabase(Database#production)?

⸻

4. Authorization Is Actor-Specific

Authorization is relational.

The same Intent can be:

authorized

for one Actor and:

unauthorized

for another.

Conceptually:

Authorization =
    Actor
    +
    Intent
    +
    Resource
    +
    Context
    +
    Applicable authorization rules

Therefore:

DeleteProject(Project#123)

does not inherently mean:

Allowed

or:

Denied

Authorization depends on who is attempting the Action and under what conditions.

⸻

5. Authorization Is Not Authentication

These concepts must remain separate.

Authentication

Who is the Actor?

Authorization

What is that Actor allowed to do?

Example:

Authentication:
Actor = User#123

Then:

Authorization:
User#123 may delete Project#456

Authentication establishes identity.

Authorization establishes permission.

⸻

6. Authorization Is Not Intent Resolution

Consider:

“Delete the project.”

Two projects exist.

Project#A
Project#B

The Intent is ambiguous.

Noema should not ask:

“Which project are you authorized to delete?”

That would allow authorization to resolve semantic ambiguity.

Instead:

Intent Resolution
    ↓
Which project?
    ↓
Project#A
    ↓
Authorization
    ↓
Is Actor allowed to delete Project#A?

⸻

7. Authorization Must Not Rewrite Intent

This is a critical invariant.

Suppose:

Actor:
User#123
Intent:
DeleteProject(Project#A)
Authorization:
DENIED

Noema must not transform the Intent into:

DeleteProject(Project#B)

because Project B happens to be authorized.

That would be a different Intent.

The system must preserve what the Actor asked for.

⸻

8. Authorization Is Not Policy

Authorization and Policy overlap but are not identical.

Authorization

Is this Actor permitted to perform this Intent?

Policy

Under what rules, conditions, limits, or organizational constraints may this Intent proceed?

For example:

Actor:
Manager#123
Intent:
ApproveExpense($50,000)
Authorization:
Allowed

But Policy may require:

Expense > $25,000
→ Requires CFO approval

Therefore:

Authorization = ALLOWED
Policy = REQUIRES_APPROVAL
Trust = BLOCKED_PENDING_APPROVAL

⸻

9. Authorization Is Intent-Specific

Permissions should not be evaluated only at the Resource level.

For example:

Actor:
User#123
Resource:
Account#456

does not tell us whether the Actor can:

ViewAccount
EditAccount
TransferFunds
CloseAccount
DeleteAccount

Authorization should evaluate the relationship between the Actor and the specific Intent.

⸻

10. Resource-Scoped Authorization

Many authorization decisions are resource-scoped.

Example:

Actor:
User#123
Intent:
DeleteProject(Project#456)

The authorization question becomes:

Can User#123 delete Project#456?

not merely:

Can User#123 delete projects?

This distinction becomes important in multi-tenant and resource-isolated systems.

⸻

11. Capability vs Authorization

These concepts are complementary.

Capability

Can the system perform this Intent?

Authorization

Is this Actor allowed to cause it?

Example:

Capability:
DeleteProject ✓
Authorization:
User#123 → DENIED

The Action is technically supported but not permitted.

Conversely:

Capability:
DeleteProject ✗
Authorization:
User#123 → ALLOWED

The Actor has permission, but the system cannot execute the Intent.

Therefore:

Authorized ≠ Executable

⸻

12. Authorization Inputs

Authorization may require:

Actor
Canonical Intent
Action
Resource
Entity
Tenant
Role
Relationship
Scope
Context
Credential claims
Delegation
Ownership
Applicable authorization rules
Current authorization state

The exact set depends on the domain.

⸻

13. Authorization Output

Authorization should produce an explicit decision.

At minimum:

ALLOWED
DENIED

In richer systems:

ALLOWED
DENIED
CONDITIONAL
REQUIRES_DELEGATION
REQUIRES_APPROVAL
UNKNOWN

Noema should avoid treating an unavailable authorization decision as permission.

⸻

14. Unknown Must Not Become Allowed

If Noema cannot establish authorization:

Authorization:
UNKNOWN

must not become:

ALLOWED

The default behavior for consequential Actions should be fail-closed.

Conceptually:

Unknown
   ↓
Do not execute

⸻

15. Authorization Must Be Deterministic

Noema’s Trust Engine should not rely on Model probability to determine authorization.

Bad:

Model:
"User probably has permission."

Good:

Authorization rule:
User#123 ∈ Project#456.admins

Therefore:

ALLOWED

Authorization should be grounded in explicit rules, claims, relationships, or authoritative authorization systems.

⸻

16. Model Role in Authorization

The Model may help identify:

Actor
Intent
Resource
Action

but it should not be the final authority on authorization.

Conceptually:

Model
  ↓
Candidate Intent
  ↓
Noema Resolution
  ↓
Authorization System
  ↓
Decision

The Model proposes.

The Trust Engine decides.

⸻

17. Authorization Sources

Authorization may be derived from:

role-based permissions
resource ownership
ACLs
relationship-based permissions
attribute-based rules
tenant membership
delegation
service-issued credentials
organizational hierarchy
domain authorization services
explicit grants

Noema should not prescribe a single authorization model.

The canonical concern is:

The decision must be grounded in an authoritative authorization source.

⸻

18. Role-Based Authorization

Example:

Actor:
User#123
Role:
Admin
Intent:
DeleteUser(User#456)

Authorization rules may state:

Admin → DeleteUser

Result:

ALLOWED

Roles are one mechanism, not the definition of authorization itself.

⸻

19. Resource Ownership

Ownership can provide authorization.

Example:

Actor:
User#123
Resource:
Project#456
Owner:
User#123

Rule:

Owner → EditProject

Result:

ALLOWED

Ownership must not be assumed merely because a Resource appears in the Actor’s Context.

It must be established by authoritative domain state.

⸻

20. Relationship-Based Authorization

Authorization can depend on relationships.

Example:

User#123
   │
   └── member_of → Organization#ABC
                       │
                       └── owns → Project#456

A rule may establish:

OrganizationMember
    → ViewProject

Noema should evaluate the actual relationship rather than infer permission from names or conversational context.

⸻

21. Attribute-Based Authorization

Authorization may depend on attributes.

Example:

Actor.department = Finance
Intent.amount = $5,000
Resource.region = EU

Rule:

Finance users may approve expenses
under $10,000

Result:

ALLOWED

The attributes used in such decisions must come from trusted sources.

⸻

22. Tenant Boundaries

In multi-tenant systems, authorization must respect tenant isolation.

Example:

Actor:
User#123
Tenant:
Tenant#A
Intent:
DeleteProject(Project#999)
Project:
Tenant#B

Even if the Actor has a broad DeleteProject permission, cross-tenant access should not be inferred as authorized.

Tenant context is part of the authorization boundary.

⸻

23. Scope

Authorization may be scoped by:

resource
tenant
organization
environment
region
workspace
project
operation
time

Example:

User#123
may delete projects
within Workspace#A

does not imply:

User#123
may delete projects
within Workspace#B

⸻

24. Temporal Authorization

Authorization may be time-dependent.

Example:

Actor:
Contractor#123
Permission:
DeployProduction
Valid:
09:00–17:00 UTC

At:

18:00 UTC

the same Intent may be denied.

Therefore authorization may depend on temporal Context.

⸻

25. Delegated Authorization

An Actor may act on behalf of another Actor.

Example:

User#123
    ↓ delegated_by
Manager#456

Intent:

ApproveExpense($10,000)

Authorization must establish:

Who delegated the authority?
What authority was delegated?
For which Resources?
For which Actions?
For what duration?
Under what conditions?

Delegation should not be inferred from conversational claims alone.

⸻

26. Delegation Chain

A delegated Action may have a chain:

Principal
   ↓
Delegate
   ↓
Actor
   ↓
Intent

The authorization system must preserve enough provenance to determine whether the delegation is valid.

⸻

27. Authorization and Human Actors

The Actor may be:

human

or another authorized agent/service.

Noema should treat the Actor as an ontology-level entity rather than assuming every Actor is a human.

The authorization semantics remain:

Actor → permitted to cause Intent

⸻

28. Authorization and Agents

An AI Agent may have authorization independent of the human who initiated the interaction.

Example:

Human#123
    ↓ delegates
Agent#456
    ↓
DeleteProject(Project#789)

Noema should establish whether:

Agent#456

has authority to perform the specific Intent.

The human’s authority should not automatically be inherited without an explicit delegation mechanism.

⸻

29. Delegation Is Not Identity Impersonation

If:

User#123

delegates:

Agent#456

authority to:

CreateInvoice

the Agent should not become semantically identical to User#123.

The authorization record should preserve:

Principal:
User#123
Actor:
Agent#456
Delegation:
CreateInvoice

This distinction is important for auditability.

⸻

30. Authorization and Context

Context can influence authorization, but Context is not itself authority.

Example:

Context:
Actor is currently in the office.

This should not automatically mean:

Actor may access payroll.

unless an authoritative authorization rule establishes that relationship.

⸻

31. Authorization and Trust Context

Trust decisions may depend on contextual signals:

location
device
session
authentication strength
time
risk level
transaction history

These may contribute to authorization decisions where the domain explicitly defines them.

⸻

32. Step-Up Authorization

Some Intents may require stronger authorization than others.

Example:

ViewBalance
    → normal session
Transfer₦5,000,000
    → step-up authentication

The Actor may be generally authorized while the specific Intent requires additional verification.

Conceptually:

Authorization:
CONDITIONAL
Condition:
StepUpAuthentication

⸻

33. Approval Is Not Authorization

Approval and authorization should remain conceptually distinct.

Example:

User#123
is authorized to submit expense
Manager#456
must approve expense

The submitter’s authorization does not imply approval.

Likewise, approval does not necessarily establish that the original Actor was authorized to initiate the Intent.

⸻

34. Authorization and Policy

Policy can impose additional constraints.

Example:

Authorization:
ALLOWED
Policy:
Transactions > $10,000 require approval

Result:

Trust:
BLOCKED_PENDING_APPROVAL

This reinforces:

Authorization ≠ Policy ≠ Trust

⸻

35. Authorization and Risk

Authorization answers whether an Actor has permission.

Risk may determine whether the system should require additional conditions.

Example:

Actor:
Authorized
Risk:
High
Trust:
Step-up authentication required

The Actor did not become unauthorized.

The execution requirements became stricter.

⸻

36. Authorization and Ambiguity

Authorization must not resolve ambiguity.

Example:

Intent:
DeleteProject(ProjectA | ProjectB)
Actor:
Authorized for ProjectA
Not authorized for ProjectB

Noema must not choose ProjectA simply because it is authorized.

Correct:

Intent:
AMBIGUOUS
Authorization:
NOT YET EVALUABLE

After clarification:

DeleteProject(ProjectA)

then:

Authorization:
ALLOWED

⸻

37. Authorization and Resolution

Authorization should consume the result of resolution.

Candidate Intent
      ↓
Resolution
      ↓
Canonical Intent
      ↓
Authorization

If resolution is incomplete:

Authorization:
NOT YET DETERMINABLE

rather than:

DENIED

This distinction matters.

⸻

38. Denied vs Not Yet Determinable

Denied

Noema has sufficient information and determines:

Actor may not perform this Intent.

Not Yet Determinable

Noema lacks a prerequisite.

Example:

Target Resource:
Unknown

The system cannot yet evaluate authorization.

These states should not be conflated.

⸻

39. Authorization Preconditions

A valid authorization decision may require:

resolved Actor
resolved Intent
resolved Resource
known tenant
current authorization state
applicable rules

If required inputs are missing:

AUTHORIZATION_UNDETERMINED

may be more accurate than DENIED.

⸻

40. Authorization Decision Provenance

A material authorization decision should be explainable.

Example:

Decision:
ALLOWED
Actor:
User#123
Intent:
DeleteProject(Project#456)
Evidence:
User#123 ∈ Project#456.admins
Rule:
Project administrators may delete projects.
Policy version:
v3

The exact representation may vary.

The principle is:

Trust decisions must be explainable from authoritative evidence.

⸻

41. Authorization Auditability

Noema should be able to answer:

Who attempted the Intent?
What Intent was attempted?
Against which Resource?
Under which authorization context?
Which rule was evaluated?
What evidence supported the decision?
What was the result?
When was the decision made?

This is essential for consequential enterprise workflows.

⸻

42. Authorization Freshness

Authorization state can change.

Example:

09:00
User#123 = ProjectAdmin
09:05
Role revoked
09:10
DeleteProject(Project#456)

A stale authorization decision should not be reused when the domain requires current authorization.

Authorization freshness requirements are domain-specific.

⸻

43. Authorization and TOCTOU

Authorization can be affected by time-of-check vs time-of-use problems.

Example:

Check:
Actor authorized
Then:
Permission revoked
Then:
Execute

For high-impact Actions, Noema or the execution boundary may require authorization to be revalidated immediately before the side effect.

This is particularly important for:

delete
transfer
publish
deploy
revoke
terminate

⸻

44. Authorization and Execution

Authorization does not execute the Intent.

It produces a Trust input or decision:

ALLOWED

Execution then occurs through the appropriate Capability.

Conceptually:

Intent
  ↓
Authorization
  ↓
ALLOWED
  ↓
Capability
  ↓
Execution

⸻

45. Authorization Must Be Enforced at the Execution Boundary

A UI check is insufficient.

A Model response is insufficient.

A conversational statement is insufficient.

The final Action boundary should enforce authorization.

Conceptually:

Noema Trust
      ↓
Authorized Intent
      ↓
Execution Contract
      ↓
Consumer / System
      ↓
Side Effect

The actual business system should also enforce its own authorization guarantees where appropriate.

⸻

46. Defense in Depth

Noema should not assume that one authorization layer is sufficient.

A mature architecture may have:

Noema Trust Authorization
        +
Business-System Authorization
        +
Infrastructure Authorization

Each protects a different boundary.

⸻

47. Authorization and Business State

Business systems remain authoritative for their own state.

For example:

Postgres:
User#123 owns Project#456

Noema may consume that fact.

Noema should not independently invent:

User#123 owns Project#456

because a conversational statement said so.

This maintains the separation:

Noema:
Intent + Trust
Business System:
Business State

⸻

48. Authorization and Intent State

Authorization should not mutate business state.

For example:

Intent:
DeleteProject(Project#456)
Authorization:
ALLOWED

does not mean:

Project#456:
Deleted

It means the Intent is permitted to proceed to execution.

Execution produces the Business State transition.

⸻

49. Authorization and Intent Lifecycle

A useful lifecycle relationship is:

UNRESOLVED
    ↓
RESOLVED
    ↓
AUTHORIZATION EVALUATION
    ↓
AUTHORIZED
    ↓
EXECUTION

A denied Intent may become:

DENIED

without ever executing.

Authorization status should not be confused with Business State.

⸻

50. Authorization Failure

Authorization denial should be explicit.

Example:

Intent:
DeleteProject(Project#456)
Authorization:
DENIED
Reason:
Actor lacks project.admin permission.

No side effect should occur.

⸻

51. Information Disclosure

Authorization failures themselves can reveal sensitive information.

Example:

“You are not authorized to access Account #987.”

This may reveal that Account #987 exists.

Therefore authorization responses should respect information-disclosure policies.

Possible response:

“You do not have permission to perform that operation.”

rather than exposing protected Resource existence.

⸻

52. Authorization Error Semantics

Noema should distinguish:

UNAUTHORIZED

from:

FORBIDDEN

where useful.

Conceptually:

Unauthorized

The Actor’s identity/authentication is insufficient.

Forbidden

The Actor is known but lacks permission.

Exact terminology may depend on protocol and implementation.

The ontology should preserve the semantic distinction even if the API uses different status codes.

⸻

53. Authorization and Least Privilege

Noema should follow the principle of least privilege:

An Actor should receive only the authority necessary to perform the authorized Intent.

An Agent authorized to:

CreateInvoice

should not automatically receive:

DeleteCustomer
TransferFunds
ModifyPermissions

⸻

54. Authorization Scope Should Be Narrow

A useful authorization representation is:

Actor
+
Action
+
Resource
+
Scope
+
Conditions

rather than:

Actor
+
global permission

The narrower representation is easier to audit and safer to delegate.

⸻

55. Conditional Authorization

Some permissions depend on conditions.

Example:

User#123
may refund Payment#456
IF:
amount < $1,000
AND
payment.status = settled

Result:

ALLOWED

only while those conditions hold.

⸻

56. Authorization Conditions Must Be Deterministic

Conditions should be evaluated using explicit facts.

Bad:

Model:
"This seems like a legitimate refund."

Better:

Payment.status = settled
Payment.amount = $500
Actor.role = SupportAgent

Then:

Rule:
SupportAgent may refund settled payments under $1,000.

⸻

57. Authorization and External Authorization Systems

Noema may delegate authorization evaluation to an external policy engine or domain service.

For example:

Noema
   ↓
Authorization Request
   ↓
Authorization Service
   ↓
Decision

The important requirement is that the returned decision be authoritative for the relevant domain.

Noema need not own every authorization rule.

⸻

58. Authorization as a Typed Decision

Conceptually:

AuthorizationDecision {
    actor
    intent
    resource
    decision
    conditions
    evidence
    policy_version
    evaluated_at
}

Possible:

decision =
    ALLOWED
    DENIED
    CONDITIONAL
    UNDETERMINED

The concrete implementation can evolve independently.

⸻

59. Authorization Invariants

Invariant 1

Authorization is evaluated against a resolved Intent.

Invariant 2

Authorization is Actor-specific.

Invariant 3

Authorization must not rewrite or substitute the Actor’s Intent.

Invariant 4

Model confidence cannot establish authorization.

Invariant 5

Unknown authorization must not silently become allowed.

Invariant 6

Authorization must be grounded in authoritative rules or evidence.

Invariant 7

Capability availability does not imply authorization.

Invariant 8

Authorization does not imply Policy approval.

Invariant 9

Authorization does not mutate Business State.

Invariant 10

Authorization decisions for consequential Actions must be enforceable at the execution boundary.

Invariant 11

Authorization must respect tenant, Resource, and scope boundaries.

Invariant 12

Authorization decisions should be auditable and attributable.

⸻

60. Canonical Authorization Flow

                 Canonical Intent
                       │
                       ▼
                 Identify Actor
                       │
                       ▼
                Identify Resource
                       │
                       ▼
               Establish Context
                       │
                       ▼
              Load Authorization Rules
                       │
                       ▼
                Evaluate Conditions
                       │
             ┌─────────┴─────────┐
             │                   │
          Allowed              Denied
             │                   │
             ▼                   ▼
       Trust Evaluation        Stop
             │
             ▼
          Execution

If required information is missing:

             Missing prerequisite
                    │
                    ▼
          AUTHORIZATION_UNDETERMINED
                    │
                    ▼
            Resolve / Clarify

⸻

61. Example: Project Deletion

Actor:

User#123

Intent:

DeleteProject(Project#456)

Authoritative relationship:

User#123
    └── admin_of → Project#456

Authorization rule:

ProjectAdmin → DeleteProject

Decision:

ALLOWED

The Intent can now proceed to the broader Trust evaluation.

⸻

62. Example: Wrong Tenant

Actor:

User#123

Intent:

DeleteProject(Project#999)

Project:

Tenant#B

Actor:

Tenant#A

Decision:

DENIED

Even if:

User#123

has a generic project deletion role within Tenant A.

⸻

63. Example: Delegated Agent

Principal:

User#123

Actor:

Agent#456

Delegation:

Agent#456
may create invoices
for Tenant#A
until 18:00

Intent:

CreateInvoice(Invoice#789)

Authorization:

ALLOWED

The authorization provenance should preserve:

Principal → Agent → Intent

⸻

64. Example: Authorized but Policy-Blocked

Intent:

TransferFunds($100,000)

Authorization:

ALLOWED

Policy:

Transfers > $50,000 require second approval.

Trust:

CONDITIONAL

The system must not claim:

UNAUTHORIZED

The Actor is authorized; an additional Trust condition remains.

⸻

65. Example: Clear Intent, No Capability

Intent:

TeleportPerson(London)

Authorization:

ALLOWED

Capability:

UNSUPPORTED

Result:

NOT EXECUTABLE

Again:

Authorization ≠ Capability

⸻

66. Relationship to the Trust Engine

Authorization is one of the mechanisms through which Noema converts a resolved Intent into a trusted execution candidate.

Conceptually:

Resolved Intent
      │
      ├── Ambiguity
      ├── Authorization
      ├── Policy
      ├── Capability
      └── Risk
             │
             ▼
        Trust Decision

The Trust Engine should not collapse these dimensions into one opaque score.

⸻

67. Why Noema Needs Authorization

Without explicit authorization semantics, an agentic system can conflate:

"I understand what you want"

with:

"I am allowed to do it."

These are fundamentally different claims.

Noema exists partly to enforce that distinction.

The Model can identify an Intent.

Noema must establish whether that Intent may cross the execution boundary.

⸻

68. Final Definition

Authorization is the deterministic, Actor-specific evaluation of whether a resolved Intent may be caused to execute against its intended Resources under the applicable authority, scope, delegation, and conditions. Authorization does not interpret Intent, provide Capability, approve Policy, or mutate Business State.

The shortest canonical formulation is:

Resolution establishes what the Actor wants. Authorization establishes whether the Actor may cause it.