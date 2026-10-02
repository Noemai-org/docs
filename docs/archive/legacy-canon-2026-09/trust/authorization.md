> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Authorization

Status: Foundational
Version: 0.2
Domain: Trust
Canonical Path: trust/authorization.md

⸻

1. Definition

Authorization is the deterministic evaluation of whether an Actor is permitted to cause a specific Intent to be executed against its intended Resources within a given Context.

Authorization answers:

“Is this Actor allowed to cause this Intent?”

It does not answer:

“What does the Actor mean?”

That is Intent Resolution.

It does not answer:

“Can the system technically perform it?”

That is Capability.

It does not answer:

“Should this Intent execute under all applicable conditions?”

That is the broader Trust decision.

Therefore:

Intent Resolution
        ↓
Authorization
        ↓
Policy / Trust
        ↓
Execution

Authorization establishes authority. It does not establish executability or successful execution.

⸻

2. Authorization in Noema

Authorization is a deterministic component of Noema’s Trust system.

The conceptual sequence is:

Actor Expression
      ↓
Candidate Intent
      ↓
Intent Resolution
      ↓
Canonical Intent
      ↓
Authorization
      ↓
Capability / Policy / Preconditions
      ↓
Trust Decision
      ↓
Action
      ↓
Execution

The exact evaluation order may vary by implementation.

The semantic dependency does not:

Authorization must evaluate a sufficiently resolved Intent against the authority applicable to the Actor, Resource, and Context.

⸻

3. Core Principle

Authorization is evaluated against the resolved Intent, not against raw Actor language or an unvalidated Model interpretation.

Example:

Actor:

“Delete the production database.”

The Model may produce:

DeleteDatabase(Database#production)

Noema must establish that this is the canonical Intent before evaluating whether the Actor may cause it.

Then authorization asks:

Can Actor#123 cause
DeleteDatabase(Database#production)?

Authorization must not become the mechanism through which Noema determines what the Actor meant.

⸻

4. Authorization Is Actor-Specific

Authorization is relational.

The same Intent may be authorized for one Actor and denied for another.

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
    Applicable Authority

Therefore:

DeleteProject(Project#123)

does not inherently mean:

ALLOWED

or:

DENIED

The result depends on who is attempting the Intent and under which authority and conditions.

⸻

5. Authorization Is Not Authentication

These concepts must remain separate.

Authentication establishes:

Who is the Actor?

Authorization establishes:

What is that Actor permitted to cause?

Example:

Authentication:
Actor = User#123
Authorization:
User#123 may delete Project#456

Authentication establishes identity.

Authorization evaluates authority.

A successfully authenticated Actor is not necessarily authorized for a particular Intent.

⸻

6. Authorization Is Not Intent Resolution

Consider:

“Delete the project.”

Two projects exist:

Project#A
Project#B

The Intent is ambiguous.

Noema must not ask:

“Which project is the Actor authorized to delete?”

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

Authorization consumes the resolved target.

It must not select a target merely because that target is authorized.

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

The system must preserve what the Actor actually requested.

Actor Intent
      ↓
Resolve
      ↓
Authorize that Intent

not:

Actor Intent
      ↓
Find something authorized
      ↓
Execute

⸻

8. Authorization Is Not Policy

Authorization and Policy are related but distinct.

Authorization:

Is this Actor permitted to cause this Intent?

Policy:

Under what rules, conditions, limits, or organizational constraints may this Intent proceed?

Example:

Actor:
Manager#123
Intent:
ApproveExpense($50,000)
Authorization:
ALLOWED

But Policy may require:

Expense > $25,000
→ Requires CFO approval

Therefore:

Authorization = ALLOWED
Policy = REQUIRES_APPROVAL
Trust = BLOCKED_PENDING_APPROVAL

Authorization does not by itself establish that all Trust conditions are satisfied.

⸻

9. Authorization Is Intent-Specific

Permissions should not be evaluated only at the Resource level.

Example:

Actor:
User#123
Resource:
Account#456

This does not establish whether the Actor may:

ViewAccount
EditAccount
TransferFunds
CloseAccount
DeleteAccount

Authorization should evaluate the relationship between the Actor and the specific Intent.

Therefore:

Actor
+
Action
+
Resource
+
Applicable Scope
+
Conditions

is more meaningful than a generic statement such as:

Actor owns Resource

⸻

10. Resource-Scoped Authorization

Many authorization decisions are Resource-scoped.

Example:

Actor:
User#123
Intent:
DeleteProject(Project#456)

The authorization question becomes:

Can User#123 delete Project#456?

not merely:

Can User#123 delete projects?

This distinction is particularly important in systems with:

* multiple Resources
* multi-tenancy
* organizational boundaries
* delegated authority
* resource-specific permissions

⸻

11. Capability vs Authorization

Capability and Authorization are complementary.

Capability:

Can the system perform this Intent?

Authorization:

Is this Actor allowed to cause this Intent?

Example:

Capability:
DeleteProject ✓
Authorization:
User#123 → DENIED

The system supports the Action, but the Actor is not permitted to cause it.

Conversely:

Capability:
DeleteProject ✗
Authorization:
User#123 → ALLOWED

The Actor has authority, but the system cannot execute the Intent.

Therefore:

Authorized ≠ Executable

and:

Executable Capability ≠ Authorized

⸻

12. Authorization Inputs

Authorization may require:

* Actor
* Principal
* Canonical Intent
* Action
* Resource
* Entity
* Tenant
* Organization
* Environment
* Role
* Relationship
* Scope
* Credential claims
* Delegation
* Ownership
* Applicable authorization rules
* Current authorization state
* Temporal Context
* Relevant Preconditions

The exact set depends on the domain.

The semantic requirement is that the authorization decision be grounded in sufficient authoritative information.

⸻

13. Authorization Output

Authorization should produce an explicit machine-readable decision.

At minimum:

ALLOWED
DENIED

A richer authorization system may also represent:

CONDITIONAL
REQUIRES_DELEGATION
REQUIRES_APPROVAL
UNDETERMINED

These states must not be collapsed into a generic Boolean when doing so would lose important semantic distinctions.

In particular:

UNDETERMINED ≠ DENIED

and:

CONDITIONAL ≠ ALLOWED_WITHOUT_CONDITIONS

⸻

14. Unknown Must Not Become Allowed

If Noema cannot establish authorization:

Authorization:
UNDETERMINED

must not silently become:

ALLOWED

For consequential Actions, the default should be fail-closed.

Conceptually:

Authorization Unknown
        ↓
Do Not Execute

The appropriate next state may be:

CLARIFY
ESCALATE
REJECT

depending on why authorization could not be established and what Policy requires.

⸻

15. Authorization Must Be Deterministic

Noema’s Trust system must not rely on Model probability to determine authorization.

Bad:

Model:
“User probably has permission.”

Good:

Authorization Rule:
User#123 ∈ Project#456.admins

Therefore:

ALLOWED

Authorization should be grounded in explicit rules, claims, relationships, delegation records, ownership records, or authoritative authorization systems.

⸻

16. Model Role in Authorization

The Model may help identify:

* Actor
* Intent
* Resource
* Action
* relevant parameters

But it should not be the final authority on authorization.

Conceptually:

Model
  ↓
Candidate Interpretation
  ↓
Intent Resolution
  ↓
Canonical Intent
  ↓
Authorization System
  ↓
Decision

The Model proposes semantic candidates.

The Trust system evaluates authority.

⸻

17. Authorization Sources

Authorization may be derived from:

* role-based permissions
* resource ownership
* access-control lists
* relationship-based permissions
* attribute-based rules
* tenant membership
* delegation
* service-issued credentials
* organizational hierarchy
* domain authorization services
* explicit grants
* explicit denials

Noema does not require a single authorization model.

The canonical concern is:

The authorization decision must be grounded in an authoritative source applicable to the relevant Actor, Intent, Resource, and Context.

⸻

18. Role-Based Authorization

Example:

Actor:
User#123
Role:
Admin
Intent:
DeleteUser(User#456)

Authorization rules may establish:

Admin → DeleteUser

Result:

ALLOWED

Roles are one mechanism for establishing authority.

They are not the definition of authorization itself.

⸻

19. Resource Ownership

Ownership can establish authorization where applicable.

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

Ownership must be established by authoritative domain state.

It must not be inferred merely because a Resource appears in the Actor’s Context or because the Actor says:

“That is my project.”

⸻

20. Relationship-Based Authorization

Authorization can depend on relationships between ontology entities.

Example:

User#123
   │
   └── member_of → Organization#ABC
                       │
                       └── owns → Project#456

A rule may establish:

OrganizationMember
    → ViewProject

Noema should evaluate the actual authoritative relationship rather than infer permission from names or conversational Context.

⸻

21. Attribute-Based Authorization

Authorization may depend on Attributes.

Example:

Actor.department = Finance
Intent.amount = $5,000
Resource.region = EU

Rule:

Finance users may approve expenses
under $10,000

Result:

ALLOWED

Attributes used in authorization decisions must come from trusted and applicable sources.

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

Even if the Actor has a broad:

DeleteProject

permission within Tenant A, cross-tenant access must not be inferred as authorized.

Tenant context is part of the authorization boundary.

⸻

23. Scope

Authorization may be scoped by:

* Resource
* Tenant
* Organization
* Environment
* Region
* Workspace
* Project
* Operation
* Time
* Data boundary

Example:

User#123
may delete projects
within Workspace#A

does not imply:

User#123
may delete projects
within Workspace#B

Authorization scope must be explicit enough to prevent authority from silently expanding beyond its intended boundary.

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

Therefore authorization may depend on Temporal Context and the validity period of the applicable authority.

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

* who delegated the authority
* who received the authority
* what authority was delegated
* which Actions are covered
* which Resources are covered
* what scope applies
* when the delegation is valid
* under what conditions the delegation may be exercised

Delegation must not be inferred from conversational claims alone.

⸻

26. Delegation Chain

A delegated Action may involve a chain:

Principal
    ↓
Delegator
    ↓
Actor
    ↓
Intent

The authorization system must preserve enough provenance to determine whether the chain is valid.

Where multiple delegation levels exist, each link must remain within the authority granted by the preceding link.

Conceptually:

Principal
   ↓
Delegation A
   ↓
Delegate
   ↓
Delegation B
   ↓
Actor
   ↓
Intent

The existence of a delegation chain does not itself establish authorization.

⸻

27. Authorization and Human Actors

The Actor may be:

human

or:

agent
service
system
organization
other authorized ontology entity

Noema should treat Actor as an ontology-level concept rather than assuming every Actor is human.

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

The human’s authority must not automatically be inherited without an explicit delegation or authorization mechanism.

⸻

29. Delegation Is Not Identity Impersonation

If:

User#123

delegates:

Agent#456

authority to:

CreateInvoice

the Agent does not become semantically identical to User#123.

The authorization record should preserve:

Principal:
User#123
Actor:
Agent#456
Delegation:
CreateInvoice

This distinction is essential for auditability, attribution, and revocation.

⸻

30. Authorization and Context

Context can influence authorization, but Context is not itself authority.

Example:

Context:
Actor is currently in the office.

This does not automatically establish:

Actor may access payroll.

unless an authoritative authorization rule explicitly makes that Context relevant.

Context supplies facts.

Authorization rules determine whether those facts establish authority.

⸻

31. Authorization and Trust Context

Trust evaluation may depend on contextual signals such as:

* location
* device
* session
* authentication strength
* time
* risk level
* transaction state
* organizational context

These may contribute to authorization where the applicable domain rules explicitly define their relevance.

Noema must not invent authorization semantics from contextual signals merely because they appear correlated with authority.

⸻

32. Step-Up Authorization

Some Intents may require stronger authorization than others.

Example:

ViewBalance
    → normal authenticated session
Transfer₦5,000,000
    → step-up authentication

The Actor may already possess general authority while the specific Intent requires an additional authorization condition.

Conceptually:

Authorization:
CONDITIONAL
Condition:
StepUpAuthentication

The condition must be satisfied before the Intent may cross the applicable execution boundary.

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

Therefore:

Authorization ≠ Approval

⸻

34. Authorization and Policy

Policy can impose additional constraints beyond authorization.

Example:

Authorization:
ALLOWED
Policy:
Transactions > $10,000 require approval

Result:

Trust:
BLOCKED_PENDING_APPROVAL

The Actor remains authorized.

The Intent is not yet permitted to proceed because another applicable condition has not been satisfied.

Therefore:

Authorization ≠ Policy ≠ Trust

⸻

35. Authorization and Risk

Authorization answers whether an Actor has authority.

Risk may determine whether additional Trust conditions are required.

Example:

Actor:
Authorized
Risk:
High
Trust:
Step-up authentication required

The Actor did not necessarily become unauthorized.

The execution requirements became stricter because the Action carries greater consequence.

Authorization and Risk should therefore remain distinct dimensions.

⸻

36. Authorization and Ambiguity

Authorization must not resolve ambiguity.

Example:

Intent:
DeleteProject(ProjectA | ProjectB)
Actor:
Authorized for ProjectA
Not authorized for ProjectB

Noema must not choose ProjectA merely because it is authorized.

Correct:

Intent:
AMBIGUOUS
Authorization:
NOT YET DETERMINABLE

After clarification:

DeleteProject(ProjectA)

then:

Authorization:
ALLOWED

Authorization evaluates the selected Intent.

It does not select the Intent.

⸻

37. Authorization and Resolution

Authorization should consume the result of Intent Resolution.

Conceptually:

Candidate Intent
      ↓
Intent Resolution
      ↓
Canonical Intent
      ↓
Authorization

If resolution is incomplete:

Authorization:
UNDETERMINED

rather than:

DENIED

The reason matters.

An unresolved Resource is not evidence that the Actor lacks permission.

⸻

38. Denied vs Not Yet Determinable

DENIED

means:

Noema has sufficient information and determines that the Actor is not permitted to cause this Intent.

UNDETERMINED

means:

Noema cannot yet establish whether the Actor is permitted because a required prerequisite is missing, unresolved, stale, or unavailable.

Example:

Target Resource:
UNKNOWN

The system cannot yet evaluate authorization against the intended Resource.

These states must not be conflated.

⸻

39. Authorization Preconditions

A valid authorization decision may require:

* resolved Actor
* resolved Intent
* resolved Resource
* known Tenant
* known Organizational boundary
* current authorization state
* applicable authorization rules
* valid delegation where applicable
* required contextual attributes

If required inputs are missing:

AUTHORIZATION_UNDETERMINED

may be more accurate than:

DENIED

The resulting Trust state should then be determined by the reason for the missing prerequisite.

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

Authorization must be reconstructable from authoritative evidence and the applicable authorization rule.

⸻

41. Authorization Auditability

Noema should be able to answer:

* Who attempted the Intent?
* What Intent was attempted?
* Against which Resource?
* Under which authorization Context?
* Which authority was evaluated?
* Which rule was applied?
* Which evidence supported the decision?
* What was the result?
* When was the decision made?
* Which version of the authorization rule applied?

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

A stale authorization decision must not automatically be reused when the Action requires current authorization.

Authorization freshness requirements are domain-specific.

Where required, Noema should revalidate authorization against current authoritative state.

⸻

43. Authorization and TOCTOU

Authorization can be affected by time-of-check versus time-of-use conditions.

Example:

Check:
Actor authorized
Then:
Permission revoked
Then:
Execute

For high-impact Actions, Noema or the execution boundary may require authorization to be revalidated immediately before the side effect.

This is particularly important for:

* delete
* transfer
* publish
* deploy
* revoke
* terminate
* permission changes

Conceptually:

Authorization Check
       ↓
Execution Preparation
       ↓
Authorization Revalidation
       ↓
Side Effect

The exact implementation depends on the execution architecture.

⸻

44. Authorization and Execution

Authorization does not execute the Intent.

It produces an authorization result that becomes an input to Trust and the execution boundary.

Conceptually:

Intent
  ↓
Authorization
  ↓
ALLOWED
  ↓
Trust
  ↓
Capability
  ↓
Execution

Authorization does not establish that execution succeeded.

It establishes that the Actor is permitted to cause the Intent, subject to the remaining Trust requirements.

⸻

45. Authorization Must Be Enforced at the Execution Boundary

A UI check is insufficient.

A Model response is insufficient.

A conversational statement is insufficient.

The final Action boundary must enforce the applicable authorization requirements.

Conceptually:

Noema Trust
      ↓
Authorized Intent
      ↓
Execution Contract
      ↓
Consumer / Business System
      ↓
Side Effect

The consuming business system should also enforce its own authorization guarantees where appropriate.

Noema authorization must not be treated as a replacement for domain-system security controls.

⸻

46. Defense in Depth

Noema should not assume that a single authorization layer is sufficient.

A mature architecture may have:

Noema Authorization
        +
Business-System Authorization
        +
Infrastructure Authorization

Each layer protects a different boundary.

Noema establishes whether the Intent is authorized within the Noema execution journey.

The business system remains responsible for enforcing its own domain security guarantees.

⸻

47. Authorization and Business State

Business systems remain authoritative for their own state.

For example:

Business System:
User#123 owns Project#456

Noema may consume that fact as authorization evidence.

Noema should not independently invent:

User#123 owns Project#456

because a conversational statement asserted it.

This maintains the separation:

Noema:
Intent + Trust
Business System:
Business State

⸻

48. Authorization and Intent State

Authorization should not mutate Business State.

For example:

Intent:
DeleteProject(Project#456)
Authorization:
ALLOWED

does not mean:

Project#456:
Deleted

It means:

The Intent is authorized to proceed,
subject to the remaining Trust and execution requirements.

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
TRUST EVALUATION
    ↓
EXECUTION

A denied Intent may become:

DENIED

without ever executing.

Authorization status must not be confused with Business State.

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

The denial should remain distinguishable from:

Intent ambiguity
Capability absence
Policy blocking
Execution failure
Execution uncertainty

⸻

51. Information Disclosure

Authorization failures themselves can reveal sensitive information.

Example:

“You are not authorized to access Account #987.”

This may reveal that Account #987 exists.

Therefore authorization responses should respect applicable information-disclosure policies.

Possible response:

“You do not have permission to perform that operation.”

rather than exposing protected Resource existence.

The authorization decision and the external response are related but distinct concerns.

⸻

52. Authorization Error Semantics

Noema should distinguish:

UNAUTHENTICATED

from:

FORBIDDEN

where useful.

Conceptually:

Unauthenticated

The Actor’s identity or authentication context is insufficiently established.

Forbidden

The Actor is known but lacks authority for the requested Intent.

Exact terminology may depend on protocol and implementation.

The ontology should preserve the semantic distinction even if a specific API uses different status codes.

⸻

53. Authorization and Least Privilege

Noema should follow the principle of least privilege.

An Actor should receive only the authority necessary to cause the authorized Intent.

An Agent authorized to:

CreateInvoice

should not automatically receive:

DeleteCustomer
TransferFunds
ModifyPermissions

Authorization should therefore be as narrow as the domain permits.

⸻

54. Authorization Scope Should Be Narrow

A useful conceptual authorization representation is:

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
Global Permission

The narrower representation is easier to audit, safer to delegate, and less likely to create unintended authority expansion.

⸻

55. Conditional Authorization

Some permissions depend on explicit conditions.

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

Conditional authority should remain distinguishable from unconditional authorization.

⸻

56. Authorization Conditions Must Be Deterministic

Authorization conditions should be evaluated using explicit, authoritative facts.

Bad:

Model:
“This seems like a legitimate refund.”

Better:

Payment.status = settled
Payment.amount = $500
Actor.role = SupportAgent

Then:

Rule:
SupportAgent may refund settled payments under $1,000.

Therefore:

ALLOWED

The Model may assist in identifying the relevant facts, but it must not replace the rule evaluation.

⸻

57. Authorization and External Authorization Systems

Noema may delegate authorization evaluation to an external policy engine or domain authorization service.

For example:

Noema
   ↓
Authorization Request
   ↓
Authorization Service
   ↓
Decision

The important requirement is that the returned decision be authoritative for the relevant domain and sufficiently attributable for the Trust record.

Noema need not own every authorization rule.

It must preserve the provenance and applicability of the authority it relies upon.

⸻

58. Authorization as a Typed Decision

Conceptually:

AuthorizationDecision {
    actor
    principal
    intent
    resource
    scope
    decision
    conditions
    evidence
    authority
    policy_version
    evaluated_at
}

Possible decisions include:

ALLOWED
DENIED
CONDITIONAL
UNDETERMINED

The concrete implementation can evolve independently.

The semantic distinctions should remain stable.

⸻

59. Authorization Invariants

Invariant 1

Authorization is evaluated against a sufficiently resolved Intent.

Invariant 2

Authorization is Actor-specific.

Invariant 3

Authorization must not rewrite or substitute the Actor’s Intent.

Invariant 4

Model confidence cannot establish authorization.

Invariant 5

Unknown or undetermined authorization must not silently become allowed.

Invariant 6

Authorization must be grounded in authoritative rules or evidence.

Invariant 7

Capability availability does not imply authorization.

Invariant 8

Authorization does not imply Policy approval or complete Trust.

Invariant 9

Authorization does not mutate Business State.

Invariant 10

Authorization decisions for consequential Actions must be enforceable at the execution boundary.

Invariant 11

Authorization must respect Tenant, Resource, Organizational, Data, and Scope boundaries.

Invariant 12

Authorization decisions should be attributable and auditable.

Invariant 13

Authorization must not resolve material Intent ambiguity.

Invariant 14

Authorization must distinguish denial from inability to determine authority.

Invariant 15

Delegated authorization must preserve the Principal, Actor, delegation scope, and applicable conditions.

Invariant 16

Authorization must not be inferred solely from conversational claims or Model output.

Invariant 17

Authorization may require revalidation when relevant authority, Context, or state becomes stale or changes.

Invariant 18

Authorization does not imply successful Execution.

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
              Load Authority Rules
                       │
                       ▼
              Evaluate Conditions
                       │
              ┌────────┴────────┐
              │                 │
           Allowed            Denied
              │                 │
              ▼                 ▼
       Trust Evaluation        Stop
              │
              ▼
          Execution

If a required prerequisite is missing:

Missing prerequisite
        │
        ▼
AUTHORIZATION_UNDETERMINED
        │
        ▼
Resolve / Clarify / Escalate

The exact resulting Trust state depends on the cause of the missing prerequisite and applicable Policy.

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

The Intent can now proceed to the remaining Trust evaluation.

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

The Tenant boundary prevents authority from being assumed across organizational boundaries.

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

Principal
    ↓
Delegation
    ↓
Actor
    ↓
Intent

⸻

64. Example: Authorized but Policy-Blocked

Intent:

TransferFunds($100,000)

Authorization:

ALLOWED

Policy:

Transfers > $50,000 require second approval.

Trust:

BLOCKED_PENDING_APPROVAL

The system must not claim:

UNAUTHORIZED

The Actor is authorized.

An additional Trust condition remains unsatisfied.

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

Authorization is one mechanism through which Noema evaluates whether a resolved Intent is permitted to become an execution candidate.

Conceptually:

Resolved Intent
      │
      ├── Ambiguity
      ├── Authorization
      ├── Policy
      ├── Capability
      ├── Preconditions
      ├── Freshness
      └── Risk
             │
             ▼
        Trust Decision

The Trust system should not collapse these dimensions into one opaque score.

Each dimension should remain semantically distinguishable.

⸻

67. Why Noema Needs Authorization

Without explicit authorization semantics, an agentic system can conflate:

“I understand what you want.”

with:

“I am allowed to do it.”

These are fundamentally different claims.

Noema must preserve the distinction.

The Model may identify an Intent.

Intent Resolution may establish what the Actor wants.

Authorization establishes whether the Actor may cause that Intent.

Trust determines whether all applicable conditions permit the Intent to cross the execution boundary.

Therefore:

Understanding
    ≠
Authority
    ≠
Capability
    ≠
Trust
    ≠
Execution

⸻

68. Final Definition

Authorization is the deterministic, Actor-specific evaluation of whether a sufficiently resolved Intent may be caused to execute against its intended Resources under the applicable authority, scope, delegation, and conditions.

Authorization does not:

* interpret Intent
* resolve ambiguity
* provide Capability
* substitute one Intent for another
* approve Policy requirements
* establish complete Trust
* mutate Business State
* guarantee successful Execution

The shortest canonical formulation is:

Resolution establishes what the Actor wants. Authorization establishes whether the Actor may cause it.

And the architectural rule is:

Resolve the Intent.
Preserve the Intent.
Authorize that Intent.
Do not substitute a different Intent merely because it is authorized.