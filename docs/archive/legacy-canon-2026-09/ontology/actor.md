> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Actor

Status: Foundational
Version: 0.3
Domain: Ontology
Canonical Path: ontology/actor.md

⸻

1. Definition

An Actor is an entity that participates in Noema’s intent-to-action lifecycle.

An Actor may:

* originate or express an Intent
* be represented by an Intent
* be the Principal on whose authority an Action is evaluated
* act on behalf of another Actor
* approve or authorize an operation
* propose an Action
* execute an Action where explicitly authorized and within an execution boundary
* receive or be affected by an Outcome
* observe relevant state where permitted

An Actor may be:

* a human
* an organization
* an organizational unit
* a service
* an external system
* an automated agent
* another software component
* a delegated representative acting on behalf of another Actor

Therefore:

An Actor is the canonical ontology-level representation of who or what participates in a Noema interaction.

Actor does not by itself establish:

* identity
* authentication
* authority
* authorization
* capability
* permission
* ownership
* delegation
* execution authority

Those properties must be established through their respective authoritative systems, contracts, and relationships.

The existence of an Actor is therefore a participation fact, not an authorization decision.

⸻

2. Actor Is Not Identity

Identity establishes who or what an entity is within an identity system.

Actor establishes who or what is participating in a Noema interaction.

These concepts are related but distinct.

Conceptually:

Identity
│
│ establishes
▼
Authenticated Principal
│
│ participates as
▼
Actor
│
├── expresses Intent
├── acts on behalf of another Actor
├── may be subject to Authority
└── participates in Actions

Authentication and identity systems establish the identity or Principal presented to Noema.

Noema must not infer the authoritative Principal from:

* model-generated text
* user-provided claims that have not been authenticated
* retrieved enterprise content
* tool responses
* inferred language alone
* Action parameters supplied by a Model
* claims contained in untrusted Context

The canonical Principal used for authorization must originate from the appropriate identity and authentication boundary.

Therefore:

Identity establishes recognition.

Authentication establishes an authenticated Principal.

Actor establishes participation.

Principal establishes the authenticated subject against which authority and authorization may be evaluated.

The detailed identity and authentication model is defined separately.

⸻

3. Actor Is Not Principal

Principal and Actor are related but must not be collapsed.

A Principal is the authenticated subject whose identity is authoritative for an authorization context.

An Actor is an ontology-level participant in the workflow.

In simple cases they may refer to the same entity.

For example:

Principal:
Customer #123

Actor:
Customer #123

But they may differ in more complex workflows.

For example:

Principal:
Customer #123

Delegate Actor:
Support Agent #456

Action:
RequestCardReplacement

The Support Agent is the Actor performing the operation.

The Customer may remain the Principal whose authority, interests, or objective are represented by the operation.

Noema must preserve this distinction wherever it affects:

* authorization
* delegation
* accountability
* target scope
* policy
* audit
* execution

A Principal is therefore not simply another name for Actor.

⸻

4. Actor Is Not Authority

An Actor may possess or exercise Authority, but Actor and Authority are not the same concept.

Actor
│
│ may be subject to
▼
Authority
│
│ contributes to authorization
▼
Action + Target + Context
│
▼
Authorization Decision

The existence of an Actor does not imply permission to perform an Action.

For example:

Actor:
Customer Support Agent

Possible Authority:
May investigate customer transaction exceptions within assigned support scope.

This does not automatically imply authority to:

* access every customer’s records
* modify account ownership
* move money
* issue unrestricted credits
* invoke every available Capability
* act outside the delegated or organizational scope

Authority is scoped, bounded, and contextual.

Therefore:

Actor ≠ Authority

Identity does not imply Authority.

Actor status does not imply Permission.

Capability does not imply Authority.

Authority must be evaluated in relation to the specific Action, Target, Context, and applicable Policy.

⸻

5. Actor Is Not Intent

An Actor participates in an Intent.

The Intent represents the objective.

The Actor represents the participant.

Actor
│
│ originates / expresses / represents
▼
Intent

For example:

Actor:
Customer

Intent:
“Where is my money?”

The Actor and Intent remain separate concepts even when a human directly expresses the Intent.

An Intent may also originate from an agent or another system.

Therefore:

The source of an Intent is an Actor relationship.

The Intent itself is the objective being represented.

The Actor’s identity or authority must not be inferred merely from the semantic content of the Intent.

⸻

6. Actor Is Not User

A human user is one possible type of Actor.

However, Noema must not define Actor as synonymous with User.

For example:

Human
│
└── Actor

Organization
│
└── Actor

Agent
│
└── Actor

Service
│
└── Actor

External System
│
└── Actor

This distinction is necessary because Noema may receive Intent from:

* humans
* personal agents
* enterprise agents
* automated services
* other systems

The Actor ontology therefore cannot depend on a human-centric definition of participation.

⸻

7. Actor Types

At the ontology level, Noema recognizes several broad categories of Actor.

7.1 Human Actor

A human individual participating directly in a Noema workflow.

Examples:

Customer
Employee
Administrator
Support Agent
Manager

A human Actor may be the Initiator, Principal, Delegate, Approver, Beneficiary, Executor, or Observer depending on the workflow.

These roles describe participation; they do not establish authority.

⸻

7.2 Organizational Actor

An organization or organizational unit participating in a workflow.

Examples:

Company
Department
Team
Business Unit

An organizational Actor may own resources, hold authority, originate Intent, or be the beneficiary of an Outcome.

Organizational membership alone must not be treated as sufficient authorization.

Where organizational authority affects execution, the relevant relationship and scope must be established from the authoritative source.

⸻

7.3 System Actor

A software system participating in the Intent, Action, or Outcome lifecycle.

Examples:

CRM
Banking System
Payment Processor
Identity Provider
Notification Service
Enterprise Workflow System

A System Actor may:

* provide authoritative state
* provide a Capability
* receive an Action
* execute an Action
* return evidence
* participate in an Outcome

A System Actor does not automatically become the Principal merely because it executes an Action.

Likewise, the existence of a system integration does not establish that every Actor may invoke every Capability exposed by that system.

⸻

7.4 Agent Actor

An automated agent participating in a Noema workflow.

An Agent Actor may:

* interpret Intent
* propose Actions
* construct structured Action parameters
* select among permitted alternatives
* execute permitted Actions
* monitor execution
* request clarification
* escalate to a human

However:

Agent capability does not create Agent authority.

An Agent Actor must operate within explicitly bounded:

* Authority
* Capability
* Policy
* Action Contracts
* Trust boundaries
* execution permissions
* target scope

An Agent must not authorize itself.

The ability to reason, plan, or call tools does not establish permission to cause a consequential Action.

Model-generated assertions about an Agent’s authority are not authoritative merely because they appear in a proposed Action or plan.

⸻

7.5 Delegated Actor

A Delegated Actor performs an operation on behalf of another Actor.

For example:

Principal:
Customer

Delegate:
Support Agent

Action:
RequestCardReplacement

Delegation must preserve:

* Principal
* Delegate
* delegated Authority
* permitted Actions
* Target scope
* conditions
* duration
* effective time
* expiration
* revocation state
* provenance

A Delegate must not be treated as the Principal merely because the Delegate performs the Action.

⸻

8. Principal and Delegate

Where delegation exists, Noema must distinguish between:

Principal

The Actor whose authority, interests, or objective are represented.

Delegate

The Actor performing an operation on behalf of the Principal.

Conceptually:

Principal
│
│ delegates bounded authority
▼
Delegation
│
▼
Delegate
│
│ proposes / performs
▼
Action

Delegation does not transfer unlimited authority.

The effective authority of the Delegate remains bounded by:

* delegated scope
* permitted Actions
* Target scope
* applicable Policy
* temporal validity
* revocation state
* execution constraints

The authenticated identity of the Delegate must remain attributable separately from the Principal.

A Delegate’s assertion that it is acting on behalf of a Principal is not sufficient evidence of delegation.

⸻

9. Actor and Authorization

Authorization answers whether a particular Principal or Actor is permitted to cause a particular Action against a particular resolved Target under particular Context and applicable Policy.

Noema must not model authorization as:

Actor
↓
“may use tool”

Instead:

Authenticated Principal / Actor
+
Action
+
Resolved Target
+
Current Context
+
Applicable Authority
+
Applicable Policy
+
Relevant Business State
↓
Authorization Decision

Authorization is therefore target-bound and context-dependent.

The authorization decision must apply to the actual Action being considered for execution, not merely to a Capability in the abstract.

The same Actor may be authorized for one Target and unauthorized for another.

The same Actor may be authorized at one point in time and unauthorized later because:

* authority changed
* policy changed
* resource ownership changed
* delegation expired
* the session expired
* the Target changed
* the relevant business state changed
* additional approval became required
* the applicable authorization scope changed

Authorization therefore cannot be reduced to a static Actor-to-Capability relationship.

⸻

10. Authorization Layers

Noema must preserve the distinction between different authorization questions.

10.1 Technical Authorization

Question:

Can this Principal or Actor invoke this Capability at all?

Example:

“User A may invoke transaction-investigation capability.”

This concerns technical access such as:

* identity permissions
* IAM
* OAuth scopes
* service-level access controls
* Capability invocation rights

Technical authorization does not establish business authorization.

A technically authorized invocation may still be rejected because the specific Action, Target, Context, or business state is not authorized.

⸻

10.2 Policy Authorization

Question:

Does the proposed Action parameterization satisfy the applicable Policy rules?

Example:

“User A may investigate transactions up to ₦5,000,000.”

Policy authorization may consider:

* Actor
* Principal
* Action
* Target
* parameters
* thresholds
* roles
* organizational rules
* regulatory requirements
* Policy version
* effective time

Policy authorization does not by itself establish that the Action is correct for the resolved business Target.

⸻

10.3 Business Authorization

Question:

Given the fully resolved Target and reconstructed current state, should the enterprise permit this specific Action now?

Example:

“Given the resolved transaction, ownership, dispute history, switch state, settlement state, and current SLA state, should this case be routed or acted upon now?”

Business authorization may depend upon:

* the actual resolved entity
* authoritative enterprise state
* current Context
* applicable Policy
* Actor / Principal
* Action semantics
* Target relationship

This is the authorization layer that prevents technically valid but semantically wrong execution.

⸻

11. Target-Bound Authorization

Authorization must bind to the specific resolved Target.

It must never be sufficient to establish:

“The Actor may invoke this Capability.”

Instead, Noema must establish:

“This Principal is authorized to cause this Action against this specific resolved Target under the current Context and applicable rules.”

Conceptually:

Principal
│
├── technically authorized for Capability?
│
├── authorized under applicable Policy?
│
├── authorized for specific Target?
│
└── authorized given current business state?
│
▼
Target-Bound Authorization

This prevents confused-deputy failures.

Example:

Two transactions exist:

Transaction A:
Owned by the requesting customer.

Transaction B:
Owned by another customer.

The requesting Actor may be technically authorized to invoke a transaction-investigation Capability.

That does not authorize investigation of Transaction B.

Noema must never resolve an ambiguous request to an unauthorized Target merely because the Actor has general Capability access.

Target resolution and authorization therefore remain coupled at the consequential execution boundary.

⸻

12. Actor and Context

Actor information is one component of Intent and Action Context.

Context may include:

* authenticated Principal
* Actor type
* organizational membership
* resource ownership
* delegation
* current session
* target relationship
* geographic or organizational scope
* temporal conditions
* current enterprise state
* applicable Policy
* risk conditions
* approval state
* authorization state

For example:

Intent:
“Where is my money?”

Actor:
Customer #123

Relevant Context:

* authenticated Principal = Customer #123
* candidate transactions exist
* one candidate belongs to Customer #123
* another candidate belongs to another customer
* current transaction state is reconstructed from multiple systems

Actor information therefore affects authorization and interpretation.

But Actor information alone is never sufficient to establish the complete decision.

Where Context materially affects authorization or execution, its authoritative source, timestamp, freshness, and provenance must be retained as required by the relevant contract.

⸻

13. Actor and Authentication

Authentication establishes the Principal presented to Noema.

Authentication may establish:

* identity
* session validity
* credential validity
* authentication strength
* identity-provider assertions

Authentication does not by itself establish:

* Intent
* Authority
* Capability
* Policy compliance
* Target ownership
* Business authorization
* Trustworthiness of Model output
* permission to execute a particular Action

Conceptually:

Authentication
↓
Principal Established
↓
Actor Participation Established
↓
Authority Evaluated
↓
Target-Bound Authorization
↓
Policy / Business Authorization
↓
Action May Be Considered
↓
Execution-Gate Revalidation
↓
Execute or Refuse / Escalate

Successful authentication must never be treated as automatic authorization.

⸻

14. Actor and Untrusted Inputs

Noema must distinguish authoritative Actor information from untrusted claims about Actors.

The following must be treated as untrusted inputs unless independently validated:

* Model-generated claims about identity
* Model-generated claims about authority
* retrieved enterprise text
* user-provided identity assertions
* tool responses
* external textual instructions
* inferred ownership claims
* Agent-generated Principal identifiers
* Actor metadata supplied solely by a Model

In particular:

The Model must not be permitted to establish the Principal used for authorization by writing a Principal identifier into a proposed Action.

The authoritative Principal comes from the identity and authentication boundary.

Similarly, a Model cannot grant authority to itself or another Actor by asserting that authority exists.

Enterprise data may provide evidence about Actor relationships, but the relevant relationship must be established from the authoritative enterprise source before it is used as an execution authorization fact.

Untrusted content must never become authoritative merely because Noema retrieved, stored, or passed it through another component.

⸻

15. Actor and Capability

Actor and Capability answer different questions.

Actor:
Who or what is participating?

Capability:
What operation can a system perform?

A Capability belongs to the system or execution environment exposing it.

An Actor may be authorized to invoke a Capability.

But:

Capability availability ≠ Actor authority.

Technical access ≠ business authorization.

Conceptually:

Actor / Principal
│
│ may be authorized to invoke
▼
Capability
│
│ bounded operation
▼
Action
│
│ against
▼
Resolved Target

Capability access must therefore remain independently evaluable from Actor authority.

A registered Capability is an executable possibility, not an authorization grant.

⸻

16. Actor and Action

An Action represents an operation.

An Actor represents a participant.

An Action may therefore have multiple associated Actors.

For example:

Action:
InvestigateTransaction

Actors:

Principal:
Customer

Requester:
Customer

Executor:
Noema-controlled execution component

Target:
Specific Transaction

Observer:
Authorized Support Agent

Each relationship has a different semantic meaning.

Noema must not reduce these relationships to a single “user” field.

Action authorization must be evaluated against the relevant Principal / Actor and the fully resolved Target.

The Action itself must preserve the identity references necessary to reconstruct these relationships without making the Action authoritative for those relationships.

⸻

17. Actor Roles

An Actor may occupy different roles within an Intent or Action lifecycle.

Possible roles include:

Initiator

The Actor that originates the Intent.

Requester

The Actor or Principal presenting the request to Noema.

Principal

The authenticated Actor whose authority or interests are represented in an authorization context.

Delegate

An Actor acting on behalf of a Principal.

Beneficiary

The Actor intended to receive the benefit or result.

Approver

An Actor whose approval is required before execution.

Executor

The Actor or system that performs an Action.

Observer

An Actor permitted to observe relevant state without being authorized to modify it.

Target Owner

The Actor or organization with an authoritative ownership relationship to the Target.

These roles describe participation and relationships.

They do not define Actor identity.

The same Actor may occupy multiple roles.

A role must not be treated as proof of authority.

⸻

18. Actor and Delegation

Delegation permits one Actor to authorize another Actor to act on its behalf within an explicitly bounded scope.

A Delegation should establish:

* Principal
* Delegate
* delegated Authority
* permitted Actions
* Target scope
* Context restrictions
* effective time
* expiration
* revocation state
* provenance
* issuing authority where applicable

Conceptually:

Principal
│
│ grants bounded delegation
▼
Delegation
├── permitted Actions
├── Target scope
├── conditions
├── effective time
├── expiration
├── revocation
└── provenance
│
▼
Delegate

Delegation must not be inferred merely because one Actor claims to represent another.

The effective authority of a Delegate is the intersection of the delegated authority and all other applicable constraints.

Conceptually:

Effective Delegate Authority

Delegated Authority
∩
Applicable Policy
∩
Target Scope
∩
Temporal Validity
∩
Execution Constraints

A delegation that has expired or been revoked must not authorize consequential execution.

⸻

19. Actor and Agentic Systems

An Agent Actor may operate on behalf of a human, organization, or another system.

For example:

Principal:
Customer

Agent:
Enterprise Service Agent

Proposed Action:
Investigate Transaction

Noema must preserve:

* who the Principal is
* which Agent proposed or performed the Action
* what authority the Agent possesses
* what Capability the Agent attempted to invoke
* which Target was resolved
* which Policy governed the decision
* what Context was considered
* what evidence supported the authorization
* what actually happened

An Agent does not inherit unrestricted authority from the Principal merely because it is acting on the Principal’s behalf.

Likewise, an Agent’s ability to access a Capability does not establish that the Agent is authorized to use it for the current Target.

Bounded agency therefore requires:

Principal
+
Agent
+
Delegated / Effective Authority
+
Action
+
Target
+
Policy
+
Context
+
Evidence
↓
Authorization / Trust Decision
↓
Permitted Action

The Agent’s proposal is evidence of what the Agent proposed.

It is not authoritative evidence that the Principal, Target, or Action is authorized.

⸻

20. Actor and Noema

Noema may participate in a workflow, but Noema must distinguish between:

* Noema as infrastructure
* Noema-controlled execution components
* enterprise systems
* external agents
* human Actors
* organizational Actors
* the Principal whose Intent is being represented

For example:

Customer
│
│ Intent
▼
Noema
│
│ governed execution
▼
Enterprise System

Noema is the trust and execution intermediary.

It does not become the Principal merely because it:

* interprets an Intent
* selects an Action
* invokes a Capability
* orchestrates execution
* records an Outcome

Likewise, an internal Noema component is not automatically an independent Actor merely because it performs a technical step.

Actor attribution should be reserved for semantically meaningful participation.

Noema must not acquire authority merely by being the intermediary through which an Action passes.

⸻

21. Actor and Business State

Actors may be represented in enterprise systems.

Examples:

Customer
Employee
Account Owner
Administrator
Supplier
Policy Holder
Case Owner

The enterprise system of record remains authoritative for the relevant business identity and relationship.

Noema may reconstruct and retain the minimum information required for:

* Intent resolution
* authorization
* Action planning
* execution
* verification
* audit

Noema must not silently become a competing source of truth for enterprise identity or ownership.

A reconstructed Actor relationship must therefore retain, where material to a decision:

* authoritative source
* source version where applicable
* observation timestamp
* freshness
* relevant evidence
* provenance

A previously observed Actor relationship must not automatically be treated as current when the relationship may have changed.

⸻

22. Actor and Data Minimization

Actor information must be handled according to the principle of minimum necessary visibility.

Noema should know enough about an Actor to:

* resolve the relevant Intent
* establish the applicable Principal
* evaluate authorization
* execute permitted Actions
* verify the Outcome
* preserve necessary accountability

Noema should not require unrestricted access to an Actor’s enterprise data merely because that data exists.

Where appropriate, Actor-related access should be:

* principal-scoped
* tenant-scoped
* purpose-scoped
* capability-scoped
* minimally disclosed

Sensitive information must not be exposed merely because an Actor has initiated an otherwise valid request.

Authorization to perform a Capability does not automatically authorize disclosure of all data reachable through that Capability.

⸻

23. Actor and Cross-Tenant / Cross-Account Boundaries

Actor authorization must respect organizational and resource boundaries.

An Actor authenticated in one tenant or account must not automatically receive access to another tenant or account.

Similarly:

Actor A
│
├── owns Resource A
│
└── does not own Resource B

Authorization for Resource A must not be generalized to Resource B.

Cross-tenant or cross-account access attempts are authorization/security events and must be handled explicitly.

Target resolution must preserve tenant and account boundaries.

A Capability that can technically access multiple tenants does not thereby authorize an Actor to cross those boundaries.

⸻

24. Actor and Stale Authorization

Actor authorization is time-sensitive.

An authorization decision made earlier must not automatically remain valid at execution time if relevant conditions may have changed.

For consequential Actions, Noema must revalidate the material authorization conditions at the execution boundary.

Conceptually:

Authorization
↓
Action Planning
↓
Time passes
↓
Authority / Policy / Delegation / Target / State may change
↓
Execution-Gate Revalidation
↓
Execute or Refuse / Escalate

Therefore:

Previously authorized ≠ currently authorized.

Execution must not rely blindly on stale authorization state.

Where material authorization inputs have freshness requirements, the authorization record should retain the authoritative source, version where applicable, and evaluation time.

⸻

25. Actor and Approval

Some Actions may require explicit approval from another Actor.

For example:

Principal:
Customer

Requester:
Support Agent

Approver:
Support Manager

Action:
High-impact Account Operation

Approval is a separate participation relationship.

The existence of an Approver role does not mean approval has occurred.

Noema must distinguish:

Approval Required

from

Approval Granted

from

Approval Validated

from

Approval Expired or Revoked

An approval must be bound to the relevant Action and, where material, Target, parameters, scope, and Policy context.

An approval for one Action must not automatically authorize a different Action or materially different Target.

High-impact Actions may require deterministic human approval before execution.

⸻

26. Actor and Outcome

An Outcome may involve multiple Actors.

For example:

Action:
Investigate Transaction

Principal:
Customer

Executor:
Noema-controlled execution component

Beneficiary:
Customer

External System:
Banking System

Outcome:
Transaction state reconstructed and complaint routed.

The Actor that executes an Action is therefore not necessarily:

* the Actor that originated the Intent
* the Principal
* the Target Owner
* the Beneficiary
* the Approver

These distinctions must survive through the execution and audit lifecycle.

An Outcome must not attribute business effect to an Actor merely because that Actor proposed or initiated an Action.

The relevant enterprise system establishes authoritative business state.

⸻

27. Actor Attribution and Provenance

Noema must be able to establish who or what participated in a consequential operation.

Actor provenance may include:

* authenticated identity provider
* enterprise directory
* session
* Principal identifier
* delegation record
* authorization decision
* Policy version
* application or Agent identity
* Capability invoked
* Action identifier
* Target identifier
* execution attempt
* relevant enterprise evidence
* authorization evaluation time

The provenance record must distinguish:

Who requested?

Who was represented?

Who was authorized?

Who acted?

What system executed?

Against which Target?

Under which authority?

Under which Policy?

Using what evidence?

At what point in time?

Actor attribution must not depend on hidden Model reasoning.

“The model said so” is not sufficient provenance.

Likewise, a Model-generated Actor identifier is not sufficient evidence of identity or authorization.

⸻

28. Actor and Security

Actor handling is part of Noema’s security boundary.

Relevant threats include:

* malicious user
* stolen session
* privilege escalation
* confused deputy
* forged Principal
* forged Context
* cross-account access
* cross-tenant access
* insider misuse
* compromised Agent
* prompt injection
* malicious tool output
* forged delegation
* stale authorization
* authorization applied to the wrong Target

Controls include:

* authenticated Principal establishment
* target-bound authorization
* server-side authorization
* Capability allowlisting
* Policy evaluation
* execution-gate revalidation
* delegation controls
* tenant isolation
* minimum-necessary access
* Actor attribution
* audit/provenance
* authoritative-state validation

The security model must remain safe even if Model output is manipulated.

No trusted authorization fact may be created solely by an untrusted Model, retrieved document, or tool response.

⸻

29. Actor Lifecycle

Actor lifecycle and participation state must not be confused.

An enterprise identity may have states such as:

IDENTIFIED
ACTIVE
SUSPENDED
REVOKED
EXPIRED
UNKNOWN

A delegation may have states such as:

PENDING
ACTIVE
EXPIRED
REVOKED
UNKNOWN

A participation relationship within a Noema workflow may independently have states such as:

REQUESTING
REPRESENTED
ACTING
APPROVING
OBSERVING
COMPLETED
REMOVED

These states describe different things.

For example:

An Actor may have an ACTIVE enterprise identity while its Delegation is EXPIRED.

Likewise, an authenticated Actor may participate in an Intent while lacking authority for the resulting Action.

Noema must not collapse these states into a single Actor lifecycle.

⸻

30. Multiple Actors

An Intent or Action may involve multiple Actors.

Example:

Intent:
“Resolve this transaction issue.”

Actors:

Initiator:
Customer

Principal:
Customer

Delegate:
Support Agent

Approver:
Support Manager

Executor:
Enterprise Service

Target Owner:
Customer

Beneficiary:
Customer

Observer:
Authorized Operations Analyst

Noema must preserve these distinctions.

A workflow must not be reduced to a single “user” identity when multiple participants materially affect:

* authorization
* execution
* accountability
* disclosure
* ownership
* outcome

Each material Actor relationship should be independently attributable.

⸻

31. Actor and Evidence

Actor-related claims that materially affect execution must be grounded in authoritative or appropriately trusted evidence.

Examples:

Claim:
“This customer owns the account.”

Required basis:
Authoritative enterprise ownership record.

Claim:
“This support agent may act for the customer.”

Required basis:
Valid delegation / authorization record.

Claim:
“This agent may invoke this Capability.”

Required basis:
Technical authorization and Capability Registry.

Claim:
“This Action is permitted for this Target.”

Required basis:
Target-bound authorization, Policy, Context, and relevant enterprise state.

Model confidence is not a substitute for Actor evidence.

Where evidence is stale, contradictory, incomplete, or unavailable, Noema must not silently treat the Actor relationship as established.

⸻

32. Actor and the Decision Order

Where Actor information materially affects execution, Noema should conceptually evaluate:

Identity / Authentication
↓
Principal Establishment
↓
Authority / Delegation
↓
Target Resolution
↓
Target-Bound Authorization
↓
Policy
↓
State Sufficiency
↓
Risk / Confirmation
↓
Final Trust Decision
↓
Execution-Gate Revalidation

An earlier failure must prevent inappropriate downstream processing.

For example:

If the Principal is unauthorized for the relevant account, Noema must reject the request before resolving and exposing unauthorized account details merely to produce a more helpful clarification.

Target resolution must not be used as a mechanism for discovering information that the Actor is not authorized to receive.

The exact Trust Decision state machine is defined outside this ontology document.

⸻

33. Actor and Execution Authority

Actor participation must remain separate from execution authority.

An Actor may:

* request an Action
* propose an Action
* authorize an Action where explicitly empowered
* perform an Action where explicitly authorized
* observe an Action

But none of these relationships automatically establishes execution authority.

The execution boundary must independently validate:

* authenticated Principal / Actor
* Action identity and semantics
* resolved Target
* Capability
* effective Authority
* applicable Policy
* required approvals
* preconditions
* relevant state
* freshness requirements
* execution constraints

Conceptually:

Actor
↓
Proposed / Requested Action
↓
Target Resolution
↓
Authorization
↓
Policy
↓
Trust Decision
↓
Execution-Gate Revalidation
↓
Execution

Possession of an Action object, authorization record, delegation record, or Capability reference must not itself grant execution authority.

⸻

34. Effective Authority

Where multiple sources of authority apply, Noema must distinguish individual authority sources from the effective authority available for a specific Action.

Effective Authority is contextual.

Conceptually:

Effective Authority

Principal Authority
∩
Delegated Authority
∩
Organizational Scope
∩
Target Scope
∩
Temporal Validity
∩
Applicable Policy
∩
Execution Constraints

Therefore:

Authority exists
≠
Action is authorized

and:

Action is authorized
≠
Execution remains authorized at a later time

The effective authority used for a consequential decision must be attributable to the authoritative sources evaluated at that decision point.

⸻

35. Actor and Policy

Policy may constrain what an Actor or Principal may cause.

Policy does not redefine the Actor.

For example:

Actor:
Support Agent

Policy:
Support agents may investigate customer transactions within assigned accounts.

The Policy establishes a rule governing the Actor’s possible Actions.

It does not convert:

Support Agent

into:

Authorized Principal for every customer.

Policy evaluation must therefore remain distinct from Actor identity and from the Action itself.

A Policy decision must be evaluated against the relevant Actor / Principal, Action, Target, parameters, and applicable state.

Policy version and effective period must be retained where they materially affect authorization.

⸻

36. Actor and Target Ownership

Ownership is an enterprise relationship, not an intrinsic property of an Actor.

For example:

Actor:
Customer #123

Target:
Account #A

Enterprise relationship:
Customer #123 owns Account #A

Noema must not infer ownership merely because:

* the Actor claims ownership
* the Intent uses possessive language
* the Model selected the Target
* a previous Action referenced the Target
* the Actor has technical access to the Target

Where ownership materially affects authorization, Noema must obtain it from the authoritative enterprise source or another explicitly trusted authority.

Ownership may also be distinct from:

* access
* administrative responsibility
* beneficiary status
* delegation
* operational control

These relationships must not be collapsed.

⸻

37. Actor and Identity Changes

Actor-related authorization may become invalid when identity conditions change.

Relevant events may include:

* credential revocation
* session expiration
* account suspension
* role change
* organizational transfer
* delegation revocation
* employment termination
* tenant change
* ownership change
* policy change

For consequential execution, material changes must be reflected through execution-gate revalidation.

Noema must not treat a previously authenticated or authorized Actor as permanently authorized.

⸻

38. Actor and External Agents

An external Agent may propose an Action to Noema without possessing Noema execution authority.

For example:

External Agent
↓
Proposed Action
↓
Noema
↓
Resolve Principal / Target / State
↓
Evaluate Authority / Policy / Trust
↓
Bounded Execution
↓
Verification
↓
Audit

The external Agent’s identity must remain distinct from:

* the Principal
* the Delegate
* the Noema execution component
* the enterprise system
* the Target Owner

Noema must independently determine whether the proposed Action may become executable.

The external Agent’s claim that it is acting for a Principal is not itself sufficient evidence of delegated authority.

⸻

39. Actor and Audit

Every consequential Actor relationship must be reconstructible from the audit record.

The audit record should establish:

WHO REQUESTED
WHO WAS REPRESENTED
WHO WAS AUTHORIZED
WHO APPROVED
WHO ACTED
WHAT ACTION
WHAT TARGET
WHAT AUTHORITY
WHAT DELEGATION
WHAT POLICY
WHAT EVIDENCE
WHAT EXECUTION ATTEMPT
WHAT RESULT
WHAT WAS VERIFIED

The audit record must distinguish:

* Actor identity
* Principal identity
* Delegate identity
* execution identity
* enterprise system identity
* authorization source
* authorization decision

An entry such as:

“Agent performed operation”

is insufficient where the distinction between Agent, Principal, Delegate, and Executor is material.

⸻

40. Actor and Deterministic Governance

Actor participation may originate in probabilistic or untrusted system output.

Governance of Actor identity and authority must not.

Conceptually:

Probabilistic / Untrusted Input
│
▼
Candidate Actor Claim
│
▼
Identity / Authentication Boundary
│
▼
Authoritative Principal
│
▼
Authority / Delegation
│
▼
Target-Bound Authorization
│
▼
Trust / Policy
│
▼
Execution

The Model may propose relationships.

The authoritative system establishes identity.

The governance boundary determines effective authority.

The execution boundary enforces the resulting decision.

⸻

41. Actor Invariants

Invariant 1

An Actor is a participant in the intent-to-action lifecycle, not merely a user account.

Invariant 2

Identity does not imply Authority.

Invariant 3

Authentication establishes a Principal; it does not by itself establish authorization.

Invariant 4

Actor does not imply Permission.

Invariant 5

Capability does not imply Authority.

Invariant 6

Authorization is specific to the Principal / Actor, Action, Target, relevant Context, and applicable Policy.

Invariant 7

Technical authorization, policy authorization, and business authorization must remain distinguishable.

Invariant 8

Target-bound authorization must prevent confused-deputy execution and unauthorized resource resolution.

Invariant 9

A Model must never establish the authoritative Principal from Model-generated prose or Action parameters.

Invariant 10

Model output, retrieved content, and tool responses are untrusted inputs until validated through the appropriate boundary.

Invariant 11

An Agent does not receive authority merely because it can reason, plan, or invoke a Capability.

Invariant 12

Delegation must preserve the distinction between Principal and Delegate.

Invariant 13

Actor roles describe participation and must not be confused with Actor identity.

Invariant 14

The same Actor may occupy multiple roles within an Intent or workflow.

Invariant 15

An Action may have multiple Actors associated with it.

Invariant 16

The Actor executing an Action is not necessarily the Actor whose Intent initiated it.

Invariant 17

Previously valid authorization must not be assumed to remain valid when relevant conditions may have changed; consequential execution requires appropriate revalidation.

Invariant 18

Actor information that materially affects authorization, execution, or disclosure must have appropriate provenance.

Invariant 19

Noema must not expose information about an unauthorized Target merely because an Actor is technically authorized to invoke a general Capability.

Invariant 20

Noema must not become the authoritative owner of an Actor’s enterprise identity merely because it orchestrates Actions involving that Actor.

Invariant 21

Actor-related access should follow minimum-necessary visibility and appropriate tenant, principal, and scope boundaries.

Invariant 22

Actor attribution must survive through consequential execution and audit.

Invariant 23

Intelligence does not create authority.

Invariant 24

Possession of an Action, Capability reference, delegation record, or authorization record does not by itself grant execution authority.

Invariant 25

Effective authority is bounded by the Principal, delegation, Target scope, Policy, temporal validity, and execution constraints applicable to the specific Action.

Invariant 26

Authorization must bind to the fully resolved Target; general Capability authorization is insufficient.

Invariant 27

Material authorization conditions must be revalidated at the execution boundary when they may have changed.

Invariant 28

A Model, retrieved document, or tool response cannot become an authoritative source of identity, authority, delegation, ownership, or authorization merely through ingestion.

Invariant 29

Approval required, approval granted, and approval validated are distinct states.

Invariant 30

An approval or authorization for one Action or Target must not silently authorize a materially different Action or Target.

Invariant 31

Actor attribution must distinguish the requesting Actor, represented Principal, Delegate, Approver, Executor, and relevant enterprise System Actor where those distinctions materially affect accountability.

Invariant 32

Enterprise identity, ownership, and Actor relationships remain authoritative to their appropriate enterprise or security systems.

⸻

42. Canonical Actor Model

At the conceptual level:

Actor
├── identity reference
├── principal relationship
├── type
├── roles
├── relationships
├── authority references
├── delegation relationships
├── organizational context
├── tenant / scope context
├── provenance
└── participation

Participation may include:

Actor
├── initiator
├── requester
├── principal
├── delegate
├── beneficiary
├── approver
├── executor
├── target owner
└── observer

These are conceptual ontology relationships.

They are not an implementation schema.

Authority references must not themselves be interpreted as proof of current authorization without evaluating their scope, validity, Target, Action, Policy, and current conditions.

⸻

43. Canonical Distinctions

Noema must preserve the following distinctions:

Identity
“Who or what is this entity?”

Authentication
“Has the entity been established through the appropriate authentication boundary?”

Principal
“Which authenticated subject is authoritative for this authorization context?”

Actor
“Who or what is participating?”

Role
“How is the Actor participating?”

Authority
“What may this Actor / Principal cause within its bounded scope?”

Capability
“What operation can the system perform?”

Authorization
“Is this Actor / Principal permitted to cause this Action against this Target under this Context and applicable Policy?”

Delegation
“Who is acting on whose behalf, under what bounded authority?”

Intent
“What does the Actor want to accomplish?”

Action
“What operation can advance that Intent?”

Target
“What specific entity or resource is the Action directed toward?”

Outcome
“What actually happened?”

Provenance
“What evidence establishes why this Actor, Action, Target, and decision were used?”

These concepts are related but must not be collapsed.

⸻

44. Relationship to Other Canonical Domains

This document defines the ontology of Actor.

Related definitions live in:

01-ontology/
├── intent.md
├── action.md
├── context.md
├── capability.md
├── policy.md
├── constraint.md
├── state.md
└── outcome.md

Identity and authentication semantics belong to the relevant enterprise and security specifications.

Authority and authorization semantics belong primarily in:

03-trust/
06-enterprise/

Delegation and execution semantics belong in:

04-execution/
11-contracts/

Actor provenance and accountability interact with:

07-audit/

Capability registration and bounded invocation interact with:

02-capabilities/
11-contracts/

The Actor ontology establishes the semantic relationships among these domains; the respective contracts and execution systems establish their machine-enforceable behavior.

⸻

45. Canonical Summary

An Actor is an entity that participates in Noema’s intent-to-action lifecycle.

An Actor may be human, organizational, system-based, agentic, or delegated.

Actor identity, Principal status, authority, capability access, authorization, ownership, delegation, and participation role are distinct concepts.

The authoritative Principal must come from the appropriate identity and authentication boundary.

Authorization must bind the relevant Principal / Actor to the specific Action and fully resolved Target under the current Context, applicable Policy, effective Authority, and relevant enterprise state.

Technical Capability access is not sufficient for business authorization.

Agents may act on behalf of Principals, but their authority remains explicitly bounded.

Delegation must preserve who is represented and who is actually acting.

Authorization and authority must be sufficiently fresh at the point of consequential execution.

Model output, retrieved content, and tool responses cannot establish authoritative identity, authority, ownership, delegation, or authorization merely by asserting those facts.

Noema must maintain sufficient Actor provenance to reconstruct:

who intended,
who requested,
who was represented,
who was authorized,
who delegated,
who approved,
who acted,
what was acted upon,
under what authority,
under what policy,
using what evidence,
and what ultimately happened.

The Actor ontology therefore exists to preserve the identity, authority, delegation, and accountability structure around consequential execution without turning Noema itself into the authoritative owner of enterprise identity or business state.

The canonical relationship is:

ACTOR
│
├── participates in ───► INTENT
│
├── may represent ─────► PRINCIPAL
│
├── may exercise ──────► AUTHORITY
│
├── may invoke ────────► CAPABILITY
│
├── may request / propose ─► ACTION
│                              │
│                              └── against ───► TARGET
│
├── may delegate / be ─► DELEGATION
│
├── may approve ───────► ACTION
│
└── may receive ───────► OUTCOME

with governance:

PRINCIPAL
+
DELEGATE / AGENT
+
EFFECTIVE AUTHORITY
+
ACTION
+
RESOLVED TARGET
+
CURRENT CONTEXT
+
POLICY
+
ENTERPRISE STATE
↓
AUTHORIZATION / TRUST
↓
EXECUTION-GATE REVALIDATION
↓
EXECUTION
↓
VERIFICATION
↓
OUTCOME
↓
AUDIT