Identity

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: 06-enterprise/identity.md

⸻

1. Definition

Identity is the authoritative representation of the humans, agents, services, and enterprise entities participating in or affected by an Intent and its execution.

Identity answers:

Who is acting, on whose behalf, and which enterprise subject, resource, or account is involved?

Identity is foundational because Noema cannot safely resolve Intent, evaluate Trust, or execute Actions without establishing the relevant identities.

⸻

2. Purpose

Noema operates in environments containing many forms of identity:

Human
Agent
Service
Application
Organization
Customer
Employee
Account
Resource

These identities must not be collapsed into one generic concept.

For example:

Human:
Alice
Agent:
Noema
Enterprise subject:
Alice's employee identity
Resource:
Alice's corporate account

Each has a different role in the execution journey.

⸻

3. Core Principle

Noema may reason about identity, but the enterprise remains authoritative for identity and authorization.

Noema should not independently decide that:

"this person is Alice"

when the enterprise Identity Provider or authoritative system says otherwise.

⸻

4. Identity vs Actor

These concepts are related but distinct.

Identity

Answers:

Who or what is this?

Actor

Answers:

Who or what is performing this operation?

For example:

Identity:
alice@company.com
Actor:
Alice acting through Noema

The same identity may participate in multiple Actions.

⸻

5. Identity vs Subject

A subject is the entity an Action concerns.

Example:

Actor:
Alice
Subject:
Bob
Action:
update Bob's account

Therefore:

Actor ≠ Subject

unless they happen to be the same entity.

⸻

6. Identity Types

Noema should conceptually support at least:

Human Identity
Agent Identity
Service Identity
Application Identity
Organization Identity
External Identity
Enterprise Resource Identity

The exact enterprise taxonomy is configurable.

⸻

7. Human Identity

A Human Identity represents a person recognized by the enterprise.

Examples:

employee_id
customer_id
user_id
email identity
directory identity

Noema should reference the enterprise identity rather than inventing a competing identity.

⸻

8. Agent Identity

An AI agent can be an Actor.

For example:

Human:
Alice
Agent:
Support Agent
Action:
refund payment

The audit trail must preserve both the human principal and the agent that performed the operation.

⸻

9. Agent Does Not Become Human

An agent identity must remain distinguishable from the human identity it represents or acts for.

Principal:
Alice
Delegated Agent:
Noema Support Agent

This distinction is necessary for:

* authorization
* auditability
* accountability
* policy
* risk

⸻

10. Service Identity

Enterprise services can also act.

Example:

Actor:
billing-service
Action:
issue_refund

Noema must be able to represent service identities when they initiate or participate in execution.

⸻

11. Application Identity

An application may be the initiating client.

Example:

Application:
Customer Portal
User:
Alice
Agent:
Noema
Action:
change_address

These identities should remain distinguishable.

⸻

12. Delegation

Noema frequently operates through delegation.

Human
  ↓
authorizes
  ↓
Agent
  ↓
performs
  ↓
Action

The identity model must preserve the delegation chain.

⸻

13. Principal Chain

A useful canonical representation is:

Principal
    ↓
Delegator
    ↓
Agent / Service
    ↓
Action

For example:

Alice
  ↓
authorized
  ↓
Noema Agent
  ↓
freeze_card

This allows an enterprise to answer:

Who ultimately authorized this Action?

⸻

14. Authentication vs Identity

Authentication establishes:

The presented credentials correspond to this identity.

Identity represents:

The enterprise subject associated with that identity.

Noema should consume authoritative authentication results rather than implement identity verification as an ad hoc inference problem.

⸻

15. Authentication Is Not Authorization

These must remain separate.

Authentication:
"Who are you?"
Authorization:
"Are you allowed to do this?"

A successfully authenticated identity does not automatically have permission to perform an Action.

⸻

16. Identity and Authorization

The canonical relationship is:

Identity
   ↓
Authorization
   ↓
Action permission

Example:

Identity:
alice
Role:
finance_manager
Authorization:
may_approve_invoice

The enterprise authorization system remains authoritative.

⸻

17. Identity and Trust

Identity is one of the inputs to Trust.

Actor Identity
      +
Action
      +
Context
      +
Policy
      +
Authorization
      ↓
Trust Decision

An unknown or insufficiently established identity may prevent execution.

⸻

18. Identity Confidence

Identity should not be treated as binary when the underlying enterprise system provides varying assurance.

Conceptually:

Identity:
Alice
Assurance:
HIGH

or:

Identity:
possible Alice
Assurance:
LOW

However, confidence or assurance must not be invented by the model.

It should come from an authoritative identity or authentication mechanism.

⸻

19. Identity Resolution

Users may refer to identities indirectly.

Example:

“Send this to John.”

Noema may discover:

John Smith
John Doe
John Williams

This is an identity resolution problem.

The model may generate candidates.

It must not silently select an identity when the distinction is consequential and unresolved.

⸻

20. Identity Ambiguity

Identity ambiguity is a first-class Noema state.

Example:

User:
"Transfer money to John."
Candidates:
John Smith
John Doe
Result:
AMBIGUOUS

Noema should transition to:

CLARIFICATION_REQUIRED

rather than guessing.

⸻

21. Identity Resolution Evidence

Identity resolution may use:

name
email
employee ID
customer ID
relationship
organization
conversation context
enterprise directory
historical context

The reliability of each source should be considered.

⸻

22. Identity Evidence

For consequential operations, Noema should distinguish:

authoritative identity

from:

inferred identity

Example:

Enterprise Directory:
employee_id = 12345
name = Alice Smith

is stronger than:

Model inference:
"This sounds like Alice."

⸻

23. Identity Mapping

Enterprise systems frequently use different identifiers.

For example:

Identity Provider:
user_123
CRM:
contact_847
Billing:
customer_551
HR:
employee_991

Noema may need to understand that these identifiers refer to the same enterprise subject.

This mapping must be grounded in authoritative enterprise relationships.

⸻

24. Identity Federation

An enterprise may use multiple identity providers.

Corporate IdP
     ↓
Customer IdP
     ↓
Partner IdP
     ↓
External Identity

Noema should preserve the source and authority of the identity it receives.

⸻

25. Identity Provenance

An identity used in a consequential Action should be traceable to its source.

Conceptually:

Identity
   ↓
Identity Provider
   ↓
Authentication / Assertion
   ↓
Actor

This is important for auditability.

⸻

26. Identity Lifecycle

Identities change over time.

Examples:

employee:
ACTIVE → SUSPENDED → TERMINATED
customer:
ACTIVE → CLOSED
service:
ACTIVE → REVOKED

Noema must account for lifecycle state when determining whether an identity may participate in execution.

⸻

27. Identity Freshness

An identity that was valid yesterday may no longer be valid today.

For example:

09:00
Alice has manager privileges
10:00
Alice leaves the organization
10:05
privileges revoked

A stale identity or authorization observation should not be treated as current when the Action is consequential.

⸻

28. Identity Revocation

Revocation should propagate through the enterprise’s authoritative identity and authorization mechanisms.

Noema should not depend solely on a cached identity state when revocation could materially affect execution.

⸻

29. Identity and Business State

Identity may itself be represented in Business State.

For example:

Employee:
Alice
Department:
Finance
Status:
ACTIVE
Role:
Manager

Noema consumes these facts from authoritative enterprise systems.

⸻

30. Identity and Resources

Resources may belong to or be controlled by identities.

Example:

Identity:
Alice
Resource:
Corporate Card #123
Relationship:
OWNS

Noema can use that relationship when determining whether an Action targets the correct resource.

⸻

31. Identity and Ownership

Ownership is not necessarily the same as identity.

Example:

Actor:
Alice
Resource:
Company Account
Owner:
Acme Corporation

Alice may be authorized to operate on the account without being its owner.

⸻

32. Identity and Organizational Relationships

Enterprise identity often includes relationships such as:

reports_to
manages
member_of
owns
delegated_to
authorized_for

These relationships may be relevant to Trust.

⸻

33. Organizational Identity

Noema should support organizational principals.

Example:

Actor:
Finance Department
Resource:
Corporate Treasury Account

A department may act through individual humans or services.

⸻

34. Service-to-Service Identity

Enterprise Actions may involve:

Noema
  ↓
Billing Service
  ↓
Payment Service

Each service should have an identifiable principal.

This enables:

authentication
authorization
audit
accountability

⸻

35. Identity and Capability

Capability answers:

What can this integration or system do?

Identity answers:

Who is requesting or performing it?

Therefore:

Identity + Capability + Authorization

may be required before an Action can execute.

⸻

36. Identity and Policy

Policy can constrain Actions based on identity.

Example:

Policy:
Only Finance Managers may approve invoices above $10,000.

Trust evaluates:

Actor:
Alice
Identity:
Finance Manager
Action:
approve invoice $25,000
Policy:
applicable

⸻

37. Identity and Risk

Identity can influence risk.

Examples:

newly created identity
privileged identity
external identity
service identity
high-risk actor

Risk systems may provide relevant signals to Trust.

Noema should not invent risk classifications merely from identity labels.

⸻

38. Identity and Intent

Intent frequently contains identity references.

Example:

“Give John access to the repository.”

Noema must determine:

Which John?
Which repository?
What level of access?

Identity resolution is therefore often part of Intent resolution.

⸻

39. Identity and Action

An Action should preserve the relevant actor identity.

Example:

Action:
grant_access
Actor:
Alice
Target:
John
Resource:
Repository X

This relationship is critical for authorization and auditability.

⸻

40. Identity and Execution

Execution should preserve the identity under which the enterprise operation is performed.

Example:

Initiating Principal:
Alice
Noema Agent:
Noema Support Agent
Execution Principal:
service_account_42

These may be different identities.

The distinction must not be lost.

⸻

41. Impersonation

If Noema operates using an enterprise mechanism such as impersonation:

Alice
  ↓
Noema
  ↓
impersonates
  ↓
service / delegated identity

the original principal and effective execution identity should both be represented.

⸻

42. Delegated Authorization

Delegation should be explicit.

Alice
  ↓
delegates
  ↓
Noema Agent
  ↓
Action

The system should be able to determine:

who delegated
what was delegated
to whom
for what scope
for how long

⸻

43. Identity Scope

Identity authority may be scoped.

For example:

Alice
may manage:
Department A
but not:
Department B

Identity alone therefore does not establish authorization.

Scope must be evaluated.

⸻

44. Identity Context

Relevant identity context may include:

identity ID
identity type
organization
role
relationships
authentication status
authorization scope
delegation
assurance
lifecycle state

Only relevant information should be provided to the current operation.

⸻

45. Identity Data Boundary

Identity information is enterprise data and therefore follows data-boundaries.md.

Noema should not expose:

private identity attributes
credentials
secrets
unnecessary personal information

merely because they are technically available.

⸻

46. Identity and Privacy

Identity may contain sensitive personal information.

Noema should follow:

minimum necessary disclosure
purpose limitation
access control
retention policy
tenant isolation

when processing identity data.

⸻

47. Identity and Model Context

The model should receive only identity information necessary for Intent resolution.

For example:

User:
"Email Sarah."
Relevant:
Sarah's candidate identities
Not necessarily:
Sarah's complete HR profile

⸻

48. Model Cannot Establish Identity

An LLM may identify a candidate.

It cannot, by itself, establish an authoritative enterprise identity.

Model:
"Probably Sarah Smith."
Enterprise Identity System:
authoritative identity = sarah_123

Only the latter establishes identity for consequential execution.

⸻

49. Identity Collision

Two identities may share:

name
email alias
display name
department

Therefore matching on a single human-readable attribute may be insufficient.

Where identity ambiguity affects execution:

AMBIGUOUS

should be treated as a valid outcome.

⸻

50. Identity Mismatch

If the identity represented in Context differs from the identity used at execution:

Context:
Alice
Execution:
Bob

Noema should not silently proceed.

The mismatch should trigger appropriate validation or Trust behavior.

⸻

51. Identity Change During Execution

An identity may become invalid while an execution is in progress.

Example:

Execution started
      ↓
user access revoked
      ↓
execution still running

Whether execution should continue depends on enterprise policy and Action semantics.

The event should be observable and auditable.

⸻

52. Identity and Human-in-the-Loop

When a human approves an Action:

Action
  ↓
ESCALATE
  ↓
Alice approves
  ↓
Execution

the approval must be associated with Alice’s authoritative identity.

A generic:

approved = true

is insufficient for high-consequence operations.

⸻

53. Identity and Auditability

Auditability must answer:

Who initiated the Intent?
Who was the intended subject?
Who authorized the Action?
Which agent performed it?
Which service executed it?
Who intervened?

Identity provides the foundation for these answers.

⸻

54. Identity and Non-Repudiation

For high-consequence Actions, the enterprise may require strong evidence that a particular principal performed or authorized an operation.

Noema should preserve relevant identity and authorization evidence without claiming stronger assurance than the underlying identity system provides.

⸻

55. Identity Authority Hierarchy

Where identity information comes from multiple sources, authority should be explicit.

Example:

Primary:
Enterprise Identity Provider
Secondary:
HR directory
Derived:
Noema identity mapping

Noema should not arbitrarily override the authoritative source.

⸻

56. Identity Resolution Across Systems

Noema may maintain mappings such as:

Canonical Identity:
person_123
HR:
employee_456
CRM:
contact_789
Billing:
customer_101

Such mappings are integration knowledge, not necessarily authoritative identity ownership.

⸻

57. Identity Mapping Must Be Auditable

If a consequential Action depends on a cross-system mapping:

CRM customer_789
      ↓
mapped to
      ↓
canonical identity person_123

the mapping should have sufficient provenance to explain why the systems were considered equivalent.

⸻

58. Identity and Tenant Isolation

Identity must always be interpreted within the correct enterprise/tenant boundary.

Tenant A:
user_123
Tenant B:
user_123

The identifiers may be identical while referring to different principals.

Therefore identity should be scoped appropriately.

⸻

59. Identity and External Actors

External actors may participate in enterprise workflows.

Examples:

partner
vendor
customer
contractor
external service

Their identity must remain distinguishable from internal enterprise identities.

⸻

60. Identity and Capability Discovery

When discovering enterprise capabilities, Noema may encounter requirements such as:

only administrators may invoke this capability

The capability describes the operation.

Identity and authorization determine whether the current principal can use it.

⸻

61. Identity Failure

If identity cannot be established sufficiently for a consequential operation:

Identity:
UNKNOWN

Noema should not guess.

Possible policy-defined outcomes:

CLARIFY
AUTHENTICATE
ESCALATE
REJECT

⸻

62. Identity Ambiguity vs Authentication Failure

These are distinct.

Identity ambiguity

"Which John?"

Multiple valid identities may match.

Authentication failure

"Who is making this request cannot be established."

These should not collapse into the same state.

⸻

63. Identity Revocation vs Authorization Failure

These are also distinct.

Identity:
Alice — revoked
Authorization:
would otherwise permit Action

The revoked identity should not be treated as merely lacking a permission.

The identity lifecycle itself has changed.

⸻

64. Identity as a Trust Input

The canonical Trust relationship is:

                 Identity
                    │
                    ▼
              Authorization
                    │
Action ─────────────┼───────────── Policy
                    │
                  Context
                    │
                    ▼
               Trust Engine
                    │
                    ▼
                 Decision

Identity is therefore foundational but not sufficient.

⸻

65. Canonical Identity Chain

Human / System
      │
      ▼
Authenticated Identity
      │
      ▼
Enterprise Principal
      │
      ▼
Delegation / Representation
      │
      ▼
Actor
      │
      ▼
Action
      │
      ▼
Execution

Every stage should preserve the relevant identity relationships.

⸻

66. Canonical Invariants

Invariant 1

Identity answers who or what a principal is; Actor answers who or what performs an Action.

Invariant 2

The enterprise remains authoritative for identity.

Invariant 3

Authentication and authorization must remain distinct.

Invariant 4

Identity alone does not establish permission to perform an Action.

Invariant 5

Human principals and agents acting on their behalf must remain distinguishable.

Invariant 6

Delegation must preserve the original principal.

Invariant 7

Effective execution identity must be distinguishable from initiating identity where they differ.

Invariant 8

Model inference must not establish authoritative identity.

Invariant 9

Consequential identity ambiguity must not be silently resolved by guessing.

Invariant 10

Identity mappings across enterprise systems must have sufficient provenance.

Invariant 11

Identity lifecycle and revocation must be considered for consequential execution.

Invariant 12

Identity information must remain tenant-scoped.

Invariant 13

Identity data must respect enterprise data boundaries and privacy requirements.

Invariant 14

Identity used in Trust decisions must be attributable to an authoritative source where possible.

Invariant 15

Human approvals must be associated with the authoritative identity of the approving principal.

Invariant 16

Identity mismatch between resolution, Trust, and execution must be detectable.

Invariant 17

External actors and internal enterprise principals must remain distinguishable.

Invariant 18

Identity ambiguity and authentication failure must remain separate conditions.

Invariant 19

Identity revocation must not be treated as an ordinary permission denial.

Invariant 20

The audit trail must preserve the principal chain necessary to establish who initiated, authorized, performed, and was affected by consequential execution.

⸻

67. Final Definition

Identity is the authoritative representation of the principals participating in an enterprise execution journey. Noema uses identity to establish actors, subjects, delegation, authorization context, and accountability, while relying on enterprise identity systems as the authority for who those principals are.

The essential relationship is:

                 WHO?
                  │
               Identity
                  │
                  ▼
              CAN THEY?
             Authorization
                  │
                  ▼
              SHOULD IT?
                Trust
                  │
                  ▼
              WHAT TO DO?
                Action
                  │
                  ▼
              DO IT
              Execution

And for agentic execution:

Human Principal
      ↓
Delegation
      ↓
AI Agent
      ↓
Action
      ↓
Enterprise System

Noema may act on behalf of a principal, but it must never erase the principal behind the agent.