Identity

Status: Foundational
Version: 0.1
Domain: Enterprise
Canonical Path: enterprise/identity.md

⸻

1. Definition

Identity is the authoritative representation of the humans, agents, services, applications, organizations, and enterprise entities participating in or affected by an Intent and its execution.

Identity answers:

Who or what is this, who is acting, on whose behalf, and which enterprise subject, resource, or account is involved?

Identity is foundational because Noema cannot safely resolve Intent, evaluate Trust, or execute Actions without establishing the relevant identities and relationships.

The enterprise remains authoritative for enterprise identity. Noema consumes and reconciles identity representations; it does not become the enterprise’s identity authority.

⸻

2. Purpose

Noema operates in environments containing many forms of identity:

* Human
* Agent
* Service
* Application
* Organization
* Customer
* Employee
* Account
* Resource
* External Principal

These identities must not be collapsed into one generic concept.

For example:

Human:
Alice
Agent:
Noema Support Agent
Enterprise Principal:
Alice's employee identity
Resource:
Alice's corporate account

Each has a different role in the execution journey.

⸻

3. Core Principle

Noema may reason about identity, but the enterprise remains authoritative for identity and authorization.

Noema should not independently decide that:

“This person is Alice.”

when the enterprise Identity Provider or other authoritative system says otherwise.

Model inference may produce candidate identity matches, but it cannot establish authoritative enterprise identity.

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

The same identity may participate in multiple Actions, while an Action may have multiple relevant principals in its execution chain.

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

A subject may be a human, organization, account, resource, transaction, or other enterprise entity.

⸻

6. Identity Types

Noema should conceptually support at least:

* Human Identity
* Agent Identity
* Service Identity
* Application Identity
* Organization Identity
* External Identity
* Enterprise Resource Identity

The exact enterprise taxonomy is configurable.

Identity type must not be used as a substitute for authorization.

⸻

7. Human Identity

A Human Identity represents a person recognized by the enterprise.

Examples:

* employee ID
* customer ID
* user ID
* email identity
* directory identity

Noema should reference the enterprise identity rather than inventing a competing identity.

A human-readable name is not, by itself, sufficient to establish identity for consequential execution.

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

The audit trail must preserve both the human principal and the agent that performed the operation where the agent is acting on the human’s behalf.

The agent’s identity must remain distinct from the principal it represents.

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
* revocation

Noema must never collapse an agent action into a human action merely because the agent was delegated authority by that human.

⸻

10. Service Identity

Enterprise services can also act.

Example:

Actor:
billing-service
Action:
issue_refund

Noema must be able to represent service identities when they initiate or participate in execution.

Service identity is distinct from the human or application that caused the service invocation.

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

The application through which an Intent entered Noema is not necessarily the Actor that ultimately executes the enterprise operation.

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

Delegation must include sufficient scope and temporal information where required by enterprise policy.

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

It also allows the enterprise to distinguish the initiating principal from the effective execution identity.

⸻

14. Authentication vs Identity

Authentication establishes that presented credentials or authentication assertions correspond to an identity under the applicable authentication system.

Identity represents the enterprise subject associated with that identity.

Noema should consume authoritative authentication results rather than implement identity verification as an ad hoc inference problem.

Authentication evidence may have an assurance level, lifecycle, issuer, scope, and validity period.

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
Alice
Role:
finance_manager
Authorization:
may_approve_invoice

The enterprise authorization system remains authoritative.

Identity establishes the principal. Authorization determines whether that principal has the relevant permission within the applicable scope and policy.

⸻

17. Identity and Trust

Identity is one of the inputs to Trust.

Actor Identity
      +
Action
      +
Resolved Target
      +
Context
      +
Policy
      +
Authorization
      ↓
Trust Decision

An unknown, revoked, stale, or insufficiently established identity may prevent execution.

Identity does not itself produce a Trust decision.

⸻

18. Identity Assurance

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

However, assurance must not be invented by the model.

It should come from an authoritative identity, authentication, or verification mechanism.

Assurance is also distinct from authorization and Fact Status.

⸻

19. Identity Resolution

Users may refer to identities indirectly.

Example:

"Send this to John."

Noema may discover:

John Smith
John Doe
John Williams

This is an identity resolution problem.

The model may generate candidates.

It must not silently select an identity when the distinction is consequential and unresolved.

Resolved identity should include sufficient provenance and resolution context.

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

Noema should transition to a clarification-required state rather than guessing.

For consequential execution, an unresolved identity must prevent the system from binding the wrong principal or target.

⸻

21. Identity Resolution Evidence

Identity resolution may use:

* name
* email
* employee ID
* customer ID
* relationship
* organization
* conversation context
* enterprise directory
* historical context

The reliability and authority of each source should be considered.

Model-generated candidate matching is evidence for resolution, not authoritative identity by itself.

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

Evidence supporting identity should preserve source, authority, observation time, and applicable scope where relevant.

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

A mapping maintained by Noema is integration knowledge unless the enterprise explicitly establishes it as authoritative.

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

Federation does not eliminate the need to establish:

* issuer
* subject
* assurance
* scope
* validity
* applicable tenant
* authorization

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
Identity Resolution
   ↓
Actor

This is important for auditability.

Provenance should preserve enough information to establish why the identity was accepted without requiring private model chain-of-thought.

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

Lifecycle state is enterprise Business State and must be obtained from authoritative enterprise sources.

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

Freshness is claim- and decision-specific. Recency alone does not establish authority.

⸻

28. Identity Revocation

Revocation should propagate through the enterprise’s authoritative identity and authorization mechanisms.

Noema should not depend solely on a cached identity state when revocation could materially affect execution.

A previously valid Trust Decision may require re-evaluation if identity or authorization is revoked before execution.

⸻

29. Identity and Business State

Identity may itself be represented in enterprise Business State.

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

Noema may retain an observation of these values, but the retained representation does not become authoritative Business State.

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

Ownership is an enterprise relationship and must be grounded in authoritative enterprise data.

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

Therefore:

Identity ≠ Ownership

and:

Authorization ≠ Ownership

⸻

32. Identity and Organizational Relationships

Enterprise identity often includes relationships such as:

* reports_to
* manages
* member_of
* owns
* delegated_to
* authorized_for

These relationships may be relevant to Trust.

Relationships must remain distinguishable from identity attributes and should carry appropriate authority and temporal semantics.

⸻

33. Organizational Identity

Noema should support organizational principals.

Example:

Actor:
Finance Department
Resource:
Corporate Treasury Account

A department may act through individual humans or services.

The organizational principal and the effective human or service actor should remain distinguishable.

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

* authentication
* authorization
* audit
* accountability
* incident investigation

The service identity must not erase the initiating principal when delegation exists.

⸻

35. Identity and Capability

Capability answers:

What can this integration or system do?

Identity answers:

Who is requesting or performing it?

Therefore:

Identity + Capability + Authorization

may be required before an Action can execute.

Capability availability does not imply that the current Actor is authorized to use it.

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

The policy and authorization sources remain enterprise-controlled.

⸻

37. Identity and Risk

Identity can influence risk.

Examples:

* newly created identity
* privileged identity
* external identity
* service identity
* high-risk actor

Risk systems may provide relevant signals to Trust.

Noema should not invent risk classifications merely from identity labels.

Identity-derived risk signals must remain distinguishable from authoritative identity facts.

⸻

38. Identity and Intent

Intent frequently contains identity references.

Example:

"Give John access to the repository."

Noema must determine:

* Which John?
* Which repository?
* What level of access?

Identity resolution is therefore often part of Intent resolution.

Unresolved identity must remain explicit rather than being silently converted into a guessed canonical identity.

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

The Action must use a resolved identity for consequential execution where the identity is material to authorization or targeting.

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

Execution provenance should preserve the relationship between the initiating principal, delegated agent, and effective enterprise execution identity.

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

Impersonation must not be treated as identity substitution in the audit record.

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

* who delegated
* what was delegated
* to whom
* for what scope
* for how long
* under which policy or authorization mechanism

Delegation does not automatically expand beyond the authority granted by the delegating principal.

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

Scope may include:

* tenant
* organization
* resource
* action
* data
* time
* geographic or regulatory boundary

where applicable.

⸻

44. Identity Context

Relevant identity context may include:

* identity ID
* identity type
* organization
* role
* relationships
* authentication status
* authorization scope
* delegation
* assurance
* lifecycle state
* issuer
* tenant

Only relevant information should be provided to the current operation.

Identity Context is subject to the same Data Boundaries that govern other enterprise data.

⸻

45. Identity Data Boundary

Identity information is enterprise data and therefore follows enterprise/data-boundaries.md.

Noema should not expose:

* private identity attributes
* credentials
* secrets
* unnecessary personal information

merely because they are technically available.

Identity data must remain subject to purpose limitation, least privilege, tenant isolation, retention, and authorization.

⸻

46. Identity and Privacy

Identity may contain sensitive personal information.

Noema should follow:

* minimum necessary disclosure
* purpose limitation
* access control
* retention policy
* tenant isolation

when processing identity data.

Privacy requirements do not replace authorization; both must be satisfied.

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

The model must not receive identity attributes merely because they are available.

⸻

48. Model Cannot Establish Identity

An LLM may identify a candidate.

It cannot, by itself, establish an authoritative enterprise identity.

Model:
"Probably Sarah Smith."
Enterprise Identity System:
authoritative identity = sarah_123

Only the applicable authoritative enterprise mechanism establishes identity for consequential execution.

Model confidence is not identity assurance.

⸻

49. Identity Collision

Two identities may share:

* name
* email alias
* display name
* department

Therefore matching on a single human-readable attribute may be insufficient.

Where identity ambiguity affects execution:

AMBIGUOUS

should remain an explicit resolution state.

⸻

50. Identity Mismatch

If the identity represented in Context differs from the identity used at execution:

Context:
Alice
Execution:
Bob

Noema should not silently proceed.

The mismatch should trigger appropriate validation or Trust behavior.

The relevant identity version, resolution, and execution identity should remain auditable.

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

The identity change should be observable and auditable.

For consequential operations, current identity or authorization state may require revalidation before further execution.

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

The approval should preserve the principal, authorization context, timestamp, and relevant decision scope.

⸻

53. Identity and Auditability

Auditability must answer:

* Who initiated the Intent?
* Who was the intended subject?
* Who authorized the Action?
* Which agent performed it?
* Which service executed it?
* Who intervened?
* Which identity was effective at execution?

Identity provides the foundation for these answers.

The audit trail should preserve the principal chain without requiring private model reasoning.

⸻

54. Identity and Non-Repudiation

For high-consequence Actions, the enterprise may require strong evidence that a particular principal performed or authorized an operation.

Noema should preserve relevant identity and authorization evidence without claiming stronger assurance than the underlying identity system provides.

Non-repudiation is therefore a property of the applicable enterprise identity, authentication, authorization, and audit mechanisms, not something Noema can infer from a model output.

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

Different sources may be authoritative for different identity claims, so authority must remain claim-specific where necessary.

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

Such mappings are integration knowledge unless the enterprise explicitly establishes them as authoritative identity relationships.

A mapping may support resolution without becoming a new enterprise identity authority.

⸻

57. Identity Mapping Must Be Auditable

If a consequential Action depends on a cross-system mapping:

CRM customer_789
      ↓
mapped to
      ↓
canonical identity person_123

the mapping should have sufficient provenance to explain why the systems were considered equivalent.

Relevant provenance may include:

* source systems
* source identifiers
* mapping rule
* evidence
* effective time
* mapping version
* authority

⸻

58. Identity and Tenant Isolation

Identity must always be interpreted within the correct enterprise and tenant boundary.

Tenant A:
user_123
Tenant B:
user_123

The identifiers may be identical while referring to different principals.

Therefore identity should be scoped appropriately.

Tenant identity is not implied merely by the identifier itself.

⸻

59. Identity and External Actors

External actors may participate in enterprise workflows.

Examples:

* partner
* vendor
* customer
* contractor
* external service

Their identity must remain distinguishable from internal enterprise identities.

External identity must also retain its issuer, authority, scope, and relationship to the enterprise where relevant.

⸻

60. Identity and Capability Discovery

When discovering enterprise capabilities, Noema may encounter requirements such as:

Only administrators may invoke this capability.

The capability describes the operation.

Identity and authorization determine whether the current principal can use it.

Capability discovery must not be treated as permission discovery.

⸻

61. Identity Failure

If identity cannot be established sufficiently for a consequential operation:

Identity:
UNKNOWN

Noema should not guess.

Possible policy-defined responses include:

CLARIFY
AUTHENTICATE
ESCALATE
REJECT

AUTHENTICATE is an identity-control action or workflow state, not a fifth Trust outcome.

Where Trust must produce a canonical decision, its outcomes remain:

EXECUTE
CLARIFY
ESCALATE
REJECT

⸻

62. Identity Ambiguity vs Authentication Failure

These are distinct.

Identity ambiguity

“Which John?”

Multiple valid identities may match.

Authentication failure

“Who is making this request cannot be established.”

The principal itself cannot sufficiently be established.

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

Revocation may require revalidation of an existing Trust Decision or execution path.

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

Trust evaluates identity together with resolved Action, target, Context, evidence, authorization, policy, and other applicable conditions.

⸻

65. Identity and Resolved Target

Identity resolution must not be separated from target resolution when the two interact.

For example:

"Send money to John."

requires resolution of:

* Actor
* intended recipient
* destination account
* relevant resource
* applicable authorization

A resolved human identity does not automatically establish the correct enterprise resource.

Consequential execution requires sufficiently resolved Actor, Action, Target/Resource, and scope.

⸻

66. Canonical Identity Chain

The canonical relationship is:

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
Execution Principal
      │
      ▼
Enterprise Execution

Every stage should preserve the relevant identity relationships.

Where the effective execution identity differs from the initiating principal, both must remain identifiable.

⸻

67. Identity and Intent Versioning

Consequential identity resolution should preserve the exact Intent Object version under which the identity was resolved.

For example:

Intent v1
  ↓
"Send money to John"
  ↓
John = person_123
  ↓
Trust
  ↓
Execution

If clarification or material change produces a new Intent:

Intent v2
supersedes v1

the new identity resolution must be associated with the new Intent version.

Noema must not silently mutate the historical identity binding of an admitted Intent.

⸻

68. Planner and Identity Boundaries

The Planner may select among permitted execution paths but cannot create or expand identity authority.

The Planner cannot:

* invent an identity
* invent delegation
* invent authorization
* change the effective principal
* bypass identity resolution
* select an unauthorized principal
* treat model confidence as identity assurance

Planner decisions remain bounded by the resolved identity, Enterprise Action Graph, Capability Registry, Action Contracts, Trust Decision, and applicable enterprise policies.

⸻

69. Identity and Data Boundaries

Identity data is subject to the same hard data boundaries as other enterprise data.

Identity information may be used only where:

* the source is permitted
* the Actor is authorized
* the purpose is valid
* the tenant is correct
* the information is relevant
* the sensitivity permits the use

Identity cannot be used as a mechanism for discovering unrelated protected information.

⸻

70. Identity and State Reconciliation

Identity-related state may require reconciliation when multiple enterprise observations exist.

Example:

Identity Provider:
Alice = ACTIVE
HR:
Alice = TERMINATED

Noema must not silently select one.

State Reconciliation should determine the applicable claim based on:

* source authority
* temporal validity
* scope
* freshness
* enterprise reconciliation rules

The resulting claim should carry explicit Fact Status.

Identity reconciliation does not make Noema the identity authority.

⸻

71. Identity and Causal Audit

For consequential execution, the causal audit should be capable of representing:

Intent
  ↓
Intent Version
  ↓
Identity Source
  ↓
Authentication / Assertion
  ↓
Identity Resolution
  ↓
Resolved Actor / Subject
  ↓
Authorization
  ↓
Trust Decision
  ↓
Action
  ↓
Execution Principal
  ↓
Execution
  ↓
Verification
  ↓
Outcome

This provides causal traceability without requiring private model chain-of-thought.

⸻

72. Canonical Invariants

Invariant 1

Identity answers who or what a principal is; Actor answers who or what performs an Action.

Invariant 2

The enterprise remains authoritative for enterprise identity.

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

Identity data must respect enterprise Data Boundaries and privacy requirements.

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

Invariant 21

Identity and enterprise resource identity must remain distinguishable.

Invariant 22

Identity mappings maintained by Noema must not silently become enterprise identity authority.

Invariant 23

Identity assurance must come from an authoritative authentication or identity mechanism and must not be invented by the model.

Invariant 24

Identity resolution must preserve sufficient source, authority, temporal, and scope information for consequential operations.

Invariant 25

A resolved identity does not automatically resolve the correct enterprise target or resource.

Invariant 26

Consequential execution requires sufficiently resolved Actor, Action, Target/Resource, and scope.

Invariant 27

Identity lifecycle changes may invalidate previously established execution conditions and may require Trust revalidation.

Invariant 28

Identity-related observations from different sources must not be silently merged when their claims conflict.

Invariant 29

Identity claims must remain distinguishable from Evidence, Context, Business State, and Fact Status.

Invariant 30

The Planner cannot create, expand, or substitute identity authority.

Invariant 31

The model cannot create delegation, authorization, or effective execution identity through generated output.

Invariant 32

Identity information must cross Data Boundaries according to authorization, purpose, tenant, sensitivity, and policy.

Invariant 33

An admitted Intent’s historical identity binding must remain associated with its exact Intent version.

Invariant 34

Material changes to identity-relevant Intent must produce a new Intent version rather than silently mutating historical semantics.

Invariant 35

The initiating principal, delegated agent, and effective execution principal must remain distinguishable when they differ.

Invariant 36

Identity failure must remain distinguishable from identity ambiguity, authorization failure, and identity revocation.

Invariant 37

Identity used for consequential execution must be sufficiently current for the relevant claim and operation.

Invariant 38

Identity is a Trust input, not a Trust decision.

Invariant 39

Identity does not itself establish enterprise Business State ownership or authority.

Invariant 40

Identity provenance must support causal auditability without requiring retention of private model chain-of-thought.

⸻

73. Final Definition

Identity is the authoritative representation of the principals and enterprise entities participating in an enterprise execution journey.

Noema uses identity to establish Actors, Subjects, delegation, authorization context, accountability, and effective execution principals, while relying on enterprise identity systems as the authority for who those principals are.

The essential relationship is:

                 WHO?
                  │
               Identity
                  │
                  ▼
            AUTHENTICATED?
                  │
                  ▼
            AUTHORIZED?
                  │
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
Authentication
      ↓
Delegation / Authorization
      ↓
AI Agent
      ↓
Action
      ↓
Effective Execution Principal
      ↓
Enterprise System

Noema may act on behalf of a principal, but it must never erase the principal behind the agent, confuse identity with authorization, or allow model inference to become authoritative enterprise identity.