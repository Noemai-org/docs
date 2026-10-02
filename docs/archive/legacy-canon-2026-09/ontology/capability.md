> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Capability

Status: Foundational Draft
Version: 0.2
Domain: Ontology
Canonical Path: ontology/capability.md

⸻

1. Definition

A Capability is an explicit, bounded, registered ability of a system, service, component, or execution environment to perform a defined operation.

A Capability answers:

What operation is this execution environment explicitly able to perform?

A Capability does not answer:

* Who is authorized to invoke it?
* Whether a particular Intent is valid or trusted?
* Whether a particular Action should be performed?
* Whether the resolved Target is authorized for the current Actor or Principal?
* Whether applicable Policy permits the operation?
* Whether execution should occur?
* Whether execution will succeed?
* What business Outcome will result?

Those concerns belong to other Noema concepts.

The fundamental relationship is:

Intent
   ↓
Action
   ↓
Capability
   ↓
Execution
   ↓
Verification
   ↓
Outcome

A Capability is therefore part of Noema’s consequence boundary.

A Capability is not an open-ended instruction to a model, a generic permission to interact with a system, or an arbitrary interface through which the model may cause effects.

It is a known, bounded operation whose semantics, parameters, target requirements, authorization requirements, side effects, verification behavior, and execution constraints are explicitly established.

Noema must never treat arbitrary HTTP, arbitrary SQL, arbitrary code execution, or an arbitrary model-generated tool definition as a Capability.

The POC establishes the same boundary structurally: no capability outside the registered set may be invocable, and no monetary capability may exist in a callable state. NOEMA POC Specification_1.pdf

⸻

2. Capability Is Not Action

An Action represents an operation Noema proposes or intends to perform in pursuit of an Intent.

A Capability represents the explicit system ability through which that operation may be performed.

For example:

Action:
RequestCardRenewal
Capability:
banking.cards.renew

The distinction is:

Action
"What operation should be performed?"
Capability
"What registered operation is the system explicitly able to perform?"

An Action may require one or more Capabilities.

A Capability may support multiple Actions where their semantics, parameters, authorization requirements, and execution contracts permit.

The existence of an Action does not create a Capability.

The existence of a Capability does not require Noema to select or invoke it.

The Action is therefore a proposed or approved operation, while the Capability is the bounded executable ability through which an approved operation can be realized.

⸻

3. Capability Is Not Authority

A system may expose a Capability without a particular Actor or Principal being authorized to invoke it.

For example:

Capability:
banking.accounts.investigate
Actor A:
Technically authorized
Actor B:
Not technically authorized

Technical access is only one layer of authorization.

Noema must distinguish at least:

Technical Authorization
        ↓
Can this Principal invoke this Capability?
Policy Authorization
        ↓
Does this parameterization satisfy applicable Policy?
Business Authorization
        ↓
Given the fully resolved Target and current state,
should the enterprise permit this specific Action?

These layers must not be collapsed into Capability availability.

Therefore:

Capability ≠ Authority
Capability ≠ Permission
Capability ≠ Business Authorization

A technically authorized Actor may still be prohibited from causing a particular Action against a particular Target.

This distinction is central to Noema’s confused-deputy protection. The POC explicitly tests a case where an Actor is technically authorized to use an investigation capability but is not authorized for one of the candidate transactions; authorization must be evaluated against the specific resolved entity rather than against general capability access. NOEMA POC Specification MD.md

⸻

4. Capability Is Not Permission

Permission is the result of an authorization relationship evaluated in context.

Capability is an explicit ability exposed by an execution environment.

Conceptually:

System
  │
  └── exposes ─────► Capability
Principal / Actor
  │
  └── may satisfy ─► Authorization
Authorization
  │
  └── permits ─────► Specific Action + Target

Noema must evaluate Capability availability and authorization independently.

A Capability must never be interpreted as a general permission to “use the tool.”

Authorization is specific to the Actor or Principal, Action, and resolved Target.

Therefore:

Capability exists
        ≠
Actor is permitted
        ≠
Action is permitted
        ≠
Target is authorized

This distinction is essential to preventing confused-deputy failures.

Noema’s governing principle is that authorization is specific to actor, action, and target rather than a general permission to use a capability. Noema Master Company Document FINAL.pdf

⸻

5. Capability Is Not Trust

The existence of a Capability does not make a proposed Action trustworthy.

For example:

Capability:
payments.transfer.create
Proposed Action:
Transfer funds to Account B

The Capability establishes that the underlying system technically exposes an operation capable of performing that class of action.

It does not establish:

* that the Actor intended the operation;
* that the Target is correct;
* that the Actor is authorized for that Target;
* that applicable Policy permits the operation;
* that current enterprise state supports the operation;
* that the operation is within Noema’s allowed execution boundary;
* that required evidence exists;
* that additional approval is unnecessary;
* that the model’s proposal is trustworthy;
* that execution should occur;
* that the resulting Outcome will be successful.

Capability is therefore an execution-boundary primitive, not a Trust Decision.

The Trust Engine evaluates identity, authority, policy, risk, state consistency, ambiguity, and related evidence before consequential execution. The POC explicitly defines Trust as a deterministic decision system and requires consequential execution to receive its clearance. Noema Master Company Document FINAL.pdf

⸻

6. Capability Is Not Implementation

A Capability describes a system ability at the semantic level.

It should not be defined merely as:

POST /api/v1/cards/renew

That is an implementation interface.

The semantic Capability is:

banking.cards.renew

The concrete API, RPC method, SDK call, function, connector, or service endpoint through which the Capability is exposed belongs to the integration and contract layers.

This distinction permits Noema to remain interface-agnostic while preserving explicit execution boundaries.

A Capability may therefore have multiple implementation bindings across environments without changing its semantic identity, provided the bindings satisfy the applicable contract and compatibility requirements.

The same semantic Capability may be backed by different enterprise implementations across customers or deployment environments.

Noema’s core reasoning and Trust components should not depend directly on a particular external transport mechanism.

⸻

7. Capability Has an Owner

A Capability must have an identifiable source and owner.

The source may be:

* an enterprise system;
* a SaaS application;
* a service;
* a database-backed application;
* an internal Noema component;
* an external API;
* a physical system exposed through software;
* another execution environment.

For example:

Owner:
Banking Platform
Capability:
banking.cards.renew

The underlying system remains responsible for the actual business operation and authoritative business state.

Noema may discover, register, govern, consume, and orchestrate a Capability without becoming the owner of the underlying business state.

Systems of record remain authoritative.

Noema reconstructs and coordinates; it does not create authoritative business truth by inference.

This is consistent with the broader Noema architecture: enterprise systems remain the systems of record while Noema establishes the governed relationship among intent, state, authority, policy, execution, verification, and outcome. Noema Master Company Document FINAL.pdf

⸻

8. Capability Has a Semantic Identity

A Capability must have a stable semantic identity independent of its transport mechanism.

Examples:

banking.cards.status.read
banking.cards.renew
crm.customer.update
payments.transfer.create
notifications.email.send

The naming convention is not itself normative.

The important principle is:

A Capability must be addressable as an explicit semantic operation rather than only as an implementation-specific endpoint.

Capability identity must be stable enough to support:

* Action planning;
* authorization;
* policy evaluation;
* contract validation;
* versioning;
* audit;
* verification;
* capability discovery;
* benchmark assertions;
* provenance.

Semantic identity must remain distinguishable from implementation version and deployment-specific binding.

⸻

9. Capability Is Explicitly Registered

A Capability becomes part of Noema’s executable boundary only when it has been explicitly registered and validated.

The model must never construct an arbitrary executable call.

The model may propose a structured Action referencing a Capability, but the proposal must resolve against the finite Capability Registry.

Conceptually:

Model Proposal
      ↓
Schema Validation
      ↓
Known Capability?
      │
      ├── No → Reject / Block
      │
      └── Yes
            ↓
      Capability Validation
            ↓
      Trust / Authorization / Policy
            ↓
      Action Plan
            ↓
      Execution

Nothing outside the registered Capability set is invokable.

This is a structural execution boundary, not merely a prompt instruction.

The POC explicitly makes “no capability outside the registered set is ever invocable” an architectural invariant. NOEMA POC Specification_1.pdf

The registry therefore operates as a positive allowlist for executable capabilities.

⸻

10. Capability Has a Typed Contract

A Capability must be sufficiently defined that its invocation can be validated deterministically.

At the ontology level, relevant semantics include:

Capability
├── identity
├── semantic business meaning
├── owner
├── parameter schema
├── target semantics
├── preconditions
├── required authorization layer
├── policy requirements
├── side effects
├── expected outcome schema
├── verification strategy
├── retry semantics
├── recovery semantics
├── risk classification
├── audit requirements
├── implementation binding
├── version
├── availability
└── provenance

The executable representation belongs in:

11-contracts/

The Capability ontology defines what must be semantically known about the operation.

The contract defines how those requirements are enforced at the execution boundary.

The POC requires typed, versioned contracts at component boundaries and requires canonical schemas, including the capability registry, to exist before implementation depends on them.  

⸻

11. Capability Has Inputs

A Capability may require structured inputs.

For example:

Capability:
payments.transfer.create
Inputs:
- source_account
- destination_account
- amount
- currency

Inputs must have defined types and semantics.

Noema must distinguish between:

Validated Capability Input

and:

Model-generated Proposal

Model-generated values remain untrusted until validated against the relevant:

* schema;
* Context;
* Target;
* authority;
* Policy;
* Action contract;
* Capability contract.

Free-form model output must never be concatenated directly into a Capability invocation.

The schema gate exists before the model’s proposal can enter an execution pathway. The POC explicitly requires that no free-form model output reaches execution. NOEMA POC Specification_1.pdf

⸻

12. Capability Has a Target Contract

Where a Capability operates on a business resource, its Target semantics must be explicit.

For example:

Capability:
LOOKUP_TRANSACTION
Target:
Transaction TX88213

Capability availability does not establish authorization for every possible Target.

The authorization relationship must be evaluated against the specific resolved entity.

Therefore:

Capability
     +
Actor / Principal
     +
Action
     +
Resolved Target
     +
Context
     +
Policy
     ↓
Authorization Decision

A Capability that is technically available to an Actor must not be usable to access an unauthorized account, transaction, beneficiary, tenant, employee, customer, or other business resource.

This target binding is a core control against the confused-deputy problem.

The POC explicitly requires authorization against the specific resolved entity rather than general capability authorization. NOEMA POC Specification MD.md

⸻

13. Capability Has Preconditions

A Capability may only be valid under particular conditions.

For example:

Capability:
banking.cards.renew
Preconditions:
- card exists
- card is eligible for renewal
- required identity verification is satisfied

Capability-level Preconditions describe conditions required by the underlying operation.

They may differ from Action-level Preconditions.

An Action may impose additional conditions based on the particular:

* Intent;
* Actor;
* Target;
* Context;
* Policy;
* enterprise state;
* evidence.

A Capability precondition is therefore not merely an implementation check.

It is part of the semantic execution boundary.

A precondition may be evaluated at registration, planning, authorization, or execution time depending on whether it represents static capability semantics or dynamic enterprise state.

⸻

14. Capability Has Policy Requirements

A Capability may identify applicable Policy requirements.

For example:

Capability:
payments.refund.create
Policy Requirements:
- applicable refund policy
- threshold rules
- approval requirements

Policy requirements are not equivalent to authorization.

The Capability identifies what policy constraints apply to the operation.

The Policy system evaluates the relevant versioned Policy against the concrete request and Context.

For consequential decisions, the governing Policy version must be reconstructable.

A Capability must therefore not embed mutable Policy assumptions in a way that prevents Noema from determining which Policy governed an execution decision.

The POC requires every Trust Decision to record the exact Policy version that governed it, including cases where Policy changes between admission and execution.  

⸻

15. Capability Has Side Effects

A Capability may be:

Read-only

It observes information without intentionally changing business state.

Examples:

LOOKUP_TRANSACTION
LOOKUP_ACCOUNT
LOOKUP_TRANSACTION_HISTORY
QUERY_SWITCH_STATUS
QUERY_SETTLEMENT_STATUS
LOOKUP_BENEFICIARY

Non-monetary mutating

It changes non-monetary operational state.

Examples:

CREATE_ESCALATION_TICKET
LOG_COMPLIANT_COMPLAINT_REFERENCE
ROUTE_TO_INTERNAL_OWNER
RECORD_INVESTIGATION_EVIDENCE

External-effecting

It causes an effect in an external system.

Examples:

SendEmail
CreateExternalTicket
UpdateCustomer

Monetary

It changes or attempts to change monetary state.

Examples:

TRANSFER_FUNDS
REVERSE_TRANSACTION
ADJUST_BALANCE
INITIATE_REFUND

Side-effect classification is semantically important because it influences:

* authorization;
* Policy;
* risk;
* approval;
* confirmation;
* idempotency;
* verification;
* recovery;
* audit;
* execution eligibility.

Side-effect classification must not itself determine whether an Action is authorized or trusted.

For the POC, monetary capabilities are architecturally prohibited from callable execution. The POC’s safety invariant explicitly requires that no monetary capability exist in a callable state anywhere in the codebase. NOEMA POC Specification_1.pdf

⸻

16. Prohibited Capabilities Are Explicit

A prohibited operation should not merely be absent from the registry where a positive safety assertion is required.

For the POC, prohibited monetary capabilities are explicitly represented with a PROHIBITED classification and hard-coded rejection.

The POC registry therefore distinguishes:

ALLOWED
LOOKUP_TRANSACTION
LOOKUP_ACCOUNT
LOOKUP_TRANSACTION_HISTORY
QUERY_SWITCH_STATUS
QUERY_SETTLEMENT_STATUS
LOOKUP_BENEFICIARY
RECONCILE_TRANSACTION_STATE
EVALUATE_SLA_STATUS
CREATE_ESCALATION_TICKET
LOG_COMPLIANT_COMPLAINT_REFERENCE
ROUTE_TO_INTERNAL_OWNER
RECORD_INVESTIGATION_EVIDENCE

from:

PROHIBITED
TRANSFER_FUNDS
REVERSE_TRANSACTION
ADJUST_BALANCE
INITIATE_REFUND

The prohibited entries exist as explicit, testable refusals rather than undocumented omissions.

For the POC:

No monetary capability exists in a callable state anywhere in the codebase.

This is a structural safety invariant, not a model instruction. The POC explicitly makes a prohibited financial movement an automatic catastrophic failure condition.  

⸻

17. Capability Has Risk Characteristics

Capabilities may have different risk profiles.

For example:

Low:
LOOKUP_TRANSACTION
Higher:
CREATE_ESCALATION_TICKET
Prohibited:
TRANSFER_FUNDS

Risk is not itself a Capability.

It is a property used to determine the controls required before the Capability can be invoked.

Risk characteristics may influence:

* authorization;
* evidence requirements;
* human approval;
* confirmation;
* Policy;
* Trust thresholds;
* execution controls;
* verification;
* audit requirements;
* recovery behavior.

The Capability ontology must preserve risk classification without allowing risk classification itself to substitute for authorization or Trust evaluation.

Risk therefore informs control selection; it does not grant authority.

⸻

18. Capability Has an Authorization Boundary

A Capability may define which authorization layer or authority requirement applies.

For example:

Capability:
investigate.transaction
Required:
Technical Authorization
Policy Authorization
Business Authorization

The Capability does not itself grant authorization.

Instead, it establishes what authorization must be satisfied before invocation.

Noema must distinguish:

Technical Authorization
Can the Principal invoke this Capability?
Policy Authorization
Does the proposed parameterization comply with Policy?
Business Authorization
Given the fully resolved Target and current enterprise state,
should this particular Action be permitted?

The third layer is particularly important where technically valid access could otherwise be used against the wrong business entity or state.

Authorization therefore remains a contextual decision rather than an intrinsic property of the Capability.

⸻

19. Capability Availability Is Runtime State

A registered Capability is not necessarily available for execution at all times.

Possible states include:

REGISTERED
AVAILABLE
UNAVAILABLE
DEGRADED
DEPRECATED
REVOKED
UNKNOWN

Availability is runtime state.

Capability identity is semantic state.

Therefore:

Capability exists
        +
Capability currently unavailable
        ↓
Action cannot currently execute

Noema must not infer availability merely from registration.

Availability failures must be distinguished from:

* authorization failures;
* Policy failures;
* invalid Actions;
* invalid Targets;
* unavailable dependencies;
* execution uncertainty.

A Capability may remain semantically registered while temporarily unavailable.

Conversely, availability must never be interpreted as permission.

⸻

20. Capability Discovery

Noema must have a controlled mechanism for determining which Capabilities exist.

Capability discovery may occur through:

* explicit registration;
* configuration;
* integration manifests;
* API schemas;
* service metadata;
* Capability Registries;
* runtime discovery;
* typed tool definitions.

Discovery is not equivalent to trust.

Retrieved capability metadata, tool descriptions, enterprise text, and model-generated definitions must not automatically become executable authority.

The canonical rule is:

A Capability becomes executable only through Noema’s trusted registration and validation boundary.

Noema must not assume a Capability exists merely because:

* a model can describe how an operation might be performed;
* an endpoint exists;
* a tool description was retrieved;
* enterprise content contains instructions;
* an external system advertises an operation.

The difference between discovery and registration is therefore itself a security boundary.

⸻

21. Capability Registration

A Capability registration should establish, at minimum:

identity
semantic business meaning
owner
parameter schema
target semantics
preconditions
required authorization layer
policy requirements
side effects
expected outcome schema
verification strategy
retry semantics
recovery semantics
risk classification
audit requirements
implementation binding
version
status
provenance

The registration itself should be versioned and governed.

A registration is part of Noema’s execution-boundary configuration.

Changes to registered Capabilities must therefore be:

* auditable;
* versioned;
* distinguishable from ordinary runtime state;
* subject to appropriate validation;
* capable of being reconstructed for historical execution decisions.

The capability registry is one of the canonical schemas that the POC freezes early because every downstream component depends upon it. NOEMA POC Specification_1.pdf

⸻

22. Capability Versioning

Capabilities may evolve.

A change may affect:

* input semantics;
* output semantics;
* Target semantics;
* Preconditions;
* authorization requirements;
* Policy requirements;
* side effects;
* verification;
* retry behavior;
* recovery behavior;
* risk classification;
* implementation behavior.

Capability identity and implementation version must therefore remain distinguishable.

A semantic change must not be hidden behind an implementation deployment that preserves the same apparent Capability without compatibility analysis.

Versioning must permit Noema to determine which Capability definition governed an execution.

Versioning and compatibility rules belong in:

11-contracts/versioning.md

A Capability version is not itself a new conceptual Capability unless the semantic identity has materially changed according to the applicable versioning rules.

⸻

23. Capability and Action Selection

When Noema resolves an Intent into an Action, it must determine whether an appropriate registered Capability exists.

Conceptually:

Intent
  ↓
Candidate Action
  ↓
Capability Registry
  ↓
Known Capability?
  │
  ├── No → Cannot execute
  │
  └── Yes
       ↓
   Validate Capability
       ↓
   Validate Action
       ↓
   Evaluate Authority / Policy / Trust

Noema must not invent a Capability to satisfy an Intent.

If no suitable Capability exists, Noema may:

* request clarification;
* explain that the operation is unavailable;
* propose an alternative;
* escalate;
* terminate the workflow;

depending on Context and Policy.

The Capability Registry therefore functions as a positive execution boundary.

The model can propose operations, but executable operations must resolve to known, registered Capabilities.

The POC explicitly requires prohibited requests such as refunds, reversals, or transfers to resolve to PROHIBITED rather than reaching a monetary system. NOEMA POC Specification MD.md

⸻

24. Capability and the Model

The model is not the authority that defines executable Capabilities.

A model may:

* identify a relevant registered Capability;
* propose an Action referencing it;
* construct candidate parameters;
* suggest an Action sequence;
* explain possible alternatives.

But:

Model Proposal
      ↓
Schema Validation
      ↓
Known Capability
      ↓
Noema Validation
      ↓
Trust / Authorization / Policy
      ↓
Canonical Action
      ↓
Action Contract
      ↓
Execution

The model has:

zero credentials
zero direct system access
no authority to create executable Capabilities

Model output is untrusted data.

If the model is:

* compromised;
* hallucinating;
* manipulated;
* subjected to prompt injection;
* given malicious enterprise content;

the execution boundary must remain structurally intact.

The security model must not depend on model confidence.

This follows the core Noema principle that probabilistic intelligence may propose while consequential execution remains deterministic. Noema Master Company Document FINAL.pdf

⸻

25. Capability and Tool Responses

A tool response is evidence, not an instruction.

A Capability may return:

* business data;
* state;
* identifiers;
* events;
* execution results;
* errors;
* status information.

However, text returned by a Capability must not be interpreted as executable instructions merely because it came from an enterprise system.

For example:

Capability Response
        ↓
Structured Result
        ↓
Evidence / State
        ↓
Noema Evaluation

not:

Capability Response
        ↓
New Instructions
        ↓
Arbitrary Tool Invocation

Enterprise content and tool output may contain malicious or instruction-like text.

Such content must remain data unless independently validated through the appropriate Noema control path.

This boundary is explicitly part of Noema’s security posture: retrieved enterprise text and tool responses are untrusted inputs, while tool responses serve as evidence rather than instructions. Noema Master Company Document FINAL.pdf

⸻

26. Capability and Minimum-Necessary Access

Capability scope must respect the principle of minimum necessary visibility and minimum necessary capability.

Noema should obtain:

enough capability and data to resolve and execute the authorized workflow, and no more than necessary.

Capability access should therefore support:

* principal-scoped reads;
* target-scoped access;
* tenant isolation;
* data minimization;
* redaction;
* short-lived credentials;
* controlled connector access.

A Capability must not become a standing unrestricted feed into an enterprise system.

The enterprise system remains the source of truth, while Noema obtains only the information and operations necessary for the current investigation or execution path.

This is consistent with the Master Document’s minimum-necessary-visibility principle and its stated requirements for principal-scoped reads, data minimization, redaction, short-lived credentials, and tenant isolation. Noema Master Company Document FINAL.pdf

⸻

27. Capability and Bounded Autonomy

Capabilities define a fundamental part of Noema’s autonomous operating boundary.

Conceptually:

Autonomous Operation
    ⊆
Registered Capabilities
    ∩
Granted Authority
    ∩
Applicable Policy
    ∩
Resolved Intent
    ∩
Current Context
    ∩
Required Evidence

Autonomy cannot extend beyond the explicit Capability Registry.

A system cannot autonomously perform an operation for which no registered Capability exists.

Likewise, the existence of a Capability does not make autonomous execution permissible.

Bounded autonomy therefore depends on the intersection of:

* explicit Capability;
* valid Action;
* target-bound authority;
* applicable Policy;
* current enterprise state;
* execution contract;
* verification requirements.

The objective is not maximum autonomous action.

It is autonomous execution inside a defensible safety envelope.

Noema’s broader architecture explicitly describes autonomous operation as bounded by registered capabilities, authority, policy, current state, and verification rather than by model capability alone. Noema Master Company Document FINAL.pdf

⸻

28. Capability and the Action Graph

Capabilities are executable primitives within the Action Graph.

The Action Graph is not merely a diagram.

It is an executable structure whose nodes carry:

* Preconditions;
* required evidence;
* authority requirement;
* Policy requirement;
* expected Outcome schema;
* verification method;
* failure path;
* recovery or escalation path.

Conceptually:

Intent
  ↓
Resolve User
  ↓
Identify Account
  ↓
Resolve Target
  ↓
Query Registered Capabilities
  ↓
Evaluate State / Policy / Authority
  ↓
Action Plan
  ↓
Registered Capability
  ↓
Execution
  ↓
Verification
  ↓
Audit

Each executable node must reference a registered Capability rather than an arbitrary tool or endpoint.

The POC architecture explicitly separates the Action Graph, Execution Controller, Verification, Recovery, and Audit components, with typed contracts between them. NOEMA POC Specification_1.pdf

⸻

29. Capability and Planner

The Planner converts an approved Intent and reconstructed state into a deterministic ActionPlan.

The ActionPlan references only registered Capabilities.

Conceptually:

Approved Intent
      +
Reconstructed State
      ↓
Planner
      ↓
Deterministic ActionPlan
      ├── required capabilities
      ├── preconditions
      ├── dependencies
      ├── connector selection
      ├── cost / risk estimate
      ├── parallelization strategy
      ├── compensation strategy
      └── success criteria

For compound workflows, the Planner may construct a coherent plan containing multiple Capability-backed Actions.

The Planner must not introduce an unregistered Capability merely because it would make the plan easier to execute.

Plans must remain deterministic and benchmarkable.

The POC’s component contract explicitly passes TrustDecision(ALLOW) to the Planner and then an ActionPlan to Execution, preserving the boundary between Trust, planning, and execution. NOEMA POC Specification_1.pdf

⸻

30. Capability and Execution

The Execution Controller invokes only approved, registered Capabilities.

The execution pathway must be structurally separated from model generation.

Conceptually:

Model
  ↓
Proposal
  ↓
Schema Gate
  ↓
Noema Core
  ↓
Trust Decision
  ↓
ActionPlan
  ↓
Approved Capability
  ↓
Execution Controller
  ↓
Enterprise System

The model must never directly invoke an enterprise Capability.

The Execution Controller must revalidate the conditions required for execution immediately before the consequential operation.

This includes relevant:

* authorization;
* Target;
* Policy;
* state;
* Preconditions;
* execution constraints.

where those conditions may have become stale.

Stale authorization must not be treated as current authorization.

The POC explicitly requires the execution pathway to remain separated from free-form model output and requires execution conditions to be governed by typed contracts. NOEMA POC Specification_1.pdf

⸻

31. Capability and Idempotency

A Capability that may produce consequential side effects must define retry and idempotency semantics.

Relevant properties include:

naturally idempotent
explicitly idempotent
non-idempotent
unknown

For consequential execution, Noema must use an idempotency mechanism appropriate to the Capability.

The POC requires:

* client-generated idempotency keys created before the call;
* unique execution_attempt_id distinct from intent_id;
* deduplication of duplicate submissions and webhooks;
* bounded retry budgets;
* retry only after appropriate verification;
* no blind resend after timeout.

A timeout must produce:

EXECUTION_OUTCOME_UNKNOWN

not an assumed failure and not an automatic retry.

The valid path out of that state is a fresh verification read.

The POC explicitly defines timeout as neither success nor failure and requires verification before further action. NOEMA POC Specification MD.md

⸻

32. Capability and Verification

A Capability that produces consequential effects must define how its result can be verified.

For example:

Capability:
CREATE_ESCALATION_TICKET
Expected Outcome:
Ticket exists
Verification:
Query escalation system for ticket existence

The invocation response is not necessarily the business Outcome.

Therefore:

Capability Invocation
       ↓
Execution Result
       ↓
Verification
       ↓
Observed Enterprise State
       ↓
Outcome

An HTTP success response, SDK success response, or model assertion must not be treated as proof of business success.

After a write, Noema must verify the actual resulting enterprise state against the expected Outcome.

This follows the Noema invariant that execution must be verifiable against the real outcome rather than inferred from a success code. Noema Master Company Document FINAL.pdf

⸻

33. Capability Failure

A Capability may fail independently of the Action that requested it.

For example:

Action:
CreateEscalationTicket
Capability:
CREATE_ESCALATION_TICKET
Failure:
Escalation service unavailable

The distinction is:

Invalid Action
       ≠
Valid Action + Capability Failure

Capability failure may result from:

* timeout;
* explicit rejection;
* dependency unavailability;
* malformed response;
* silent success response;
* downstream failure;
* authorization failure;
* Policy service failure;
* execution uncertainty.

Failure handling belongs to execution and recovery semantics, but Capability ontology must preserve enough semantics for those systems to distinguish these conditions.

The POC’s failure-injection framework explicitly includes timeout, silent-200, malformed response, dependency unavailability, authorization failure, and Policy conflict as reproducible fault classes. NOEMA POC Specification_1.pdf

⸻

34. Capability and Unknown Outcomes

A Capability invocation may leave the resulting business state unknown.

For example:

Capability Invocation
       ↓
Timeout
       ↓
EXECUTION_OUTCOME_UNKNOWN

Noema must not infer:

timeout = failure

or:

timeout = success

The Capability’s verification strategy determines how the state can be resolved.

This is particularly important for operations whose side effects may have committed before the response was received.

The Capability therefore participates in the recovery semantics for execution uncertainty rather than defining timeout as an automatic failure.

The POC explicitly requires a timeout to transition into EXECUTION_OUTCOME_UNKNOWN and then verify actual enterprise state before further action. NOEMA POC Specification MD.md

⸻

35. Capability and External Systems

A Capability may be backed by an external system.

For example:

Noema
   │
   │ consumes
   ▼
Capability:
banking.cards.status.read
   │
   │ backed by
   ▼
Banking API
   │
   ▼
Banking System

The external system remains authoritative for the business state it owns.

Noema should interact through adapter or connector boundaries so that the underlying implementation can change without requiring the Intent Engine, Trust Engine, or Action Graph to depend directly on a particular external interface.

The POC explicitly requires enterprise integrations to sit behind adapter interfaces so mock implementations can later be replaced by real enterprise adapters without changing the core reasoning and Trust components. Noema Master Company Document FINAL.pdf

A Capability therefore represents the semantic operation exposed to Noema, while the adapter represents the implementation binding to the external system.

⸻

36. Capability and Business State

A Capability may read or mutate business state.

However:

Capability:
"What can be done?"
Business State:
"What is currently true?"

These must remain distinct.

A Capability may retrieve state without owning it.

A Capability may modify state without becoming the authoritative source of that state.

For example:

Capability:
LOOKUP_TRANSACTION
Authoritative State:
Banking Ledger

Noema may reconstruct state from multiple enterprise sources, but the enterprise systems remain authoritative for their respective domains.

Where authoritative sources disagree, Noema must represent the conflict rather than allowing a Capability response to silently overwrite the reconstructed state.

The Master Document explicitly defines state reconstruction as the process of assembling authoritative truth from enterprise systems that may disagree, be stale, or be incomplete. Noema Master Company Document FINAL.pdf

⸻

37. Capability and Provenance

Noema should maintain provenance for every registered Capability.

Relevant provenance may include:

Capability Owner
Registration Source
Integration
Schema Source
Version
Implementation Binding
Discovery Source
Registration Time
Last Verification
Policy / Authorization Metadata

Capability provenance allows Noema to answer:

Where did this Capability come from, what does it mean, and why does Noema believe it is executable?

Capability provenance must be distinguishable from model-generated explanations.

“The model selected this tool” is not sufficient provenance for why an executable Capability exists.

Provenance must describe the governed origin and registration of the executable boundary, not merely the event that caused a model to reference it.

⸻

38. Capability and Audit

Consequential Capability use must be reconstructable.

The audit record should allow Noema to establish:

* which Actor / Principal was involved;
* which Intent was being pursued;
* which Action was selected;
* which Capability was invoked;
* which Target was resolved;
* which authority applied;
* which Policy version governed the decision;
* what evidence supported the decision;
* what execution attempt occurred;
* what was observed afterward;
* how the Outcome was verified.

Audit is therefore not equivalent to recording:

agent called get_transaction()

The relevant requirement is causal reconstruction of the business decision and consequence.

The POC requires consequential decisions to be reconstructable from the audit store alone, and its benchmark explicitly includes expected audit events as part of each fixture.  

⸻

39. Capability and Security Boundaries

Capability is one of the principal security boundaries in Noema.

The security boundary is:

User
  ↓
Model / Intent Engine
  ↓
Schema Validation Gate
  ↓
Noema Core
  ↓
Trust / Authorization / Policy
  ↓
Registered Capability
  ↓
Execution Controller
  ↓
Enterprise System

The model has:

No credentials
No direct enterprise access
No arbitrary execution authority
No ability to create executable Capabilities

Security controls include:

* Capability allowlisting;
* typed Capability definitions;
* server-side authorization;
* Target-bound authorization;
* schema validation;
* minimum-necessary access;
* tenant isolation;
* short-lived credentials;
* execution-gate revalidation;
* deterministic human approval where required;
* idempotency;
* audit protection;
* explicit prohibited Capabilities.

These controls must continue to hold even if the model is compromised or enterprise content contains malicious instructions.

Noema’s security posture explicitly treats model output, enterprise text, retrieved content, and tool responses as untrusted while requiring allowlisted, typed capabilities and executor-side revalidation. Noema Master Company Document FINAL.pdf

⸻

40. Capability and Prompt Injection

Capability metadata, enterprise text, retrieved documents, and tool responses must be treated as data rather than trusted instructions.

Indirect prompt injection must not be able to expand the Capability boundary.

For example:

Enterprise Record
      ↓
Retrieved Content
      ↓
Model
      ↓
"Call arbitrary endpoint"

must not produce:

Arbitrary Execution

Instead:

Model Proposal
      ↓
Schema Gate
      ↓
Capability Registry
      ↓
Unknown / Unregistered Capability
      ↓
Reject

The execution boundary must therefore be enforced independently of model behavior.

This is directly aligned with Noema’s threat model, which treats indirect prompt injection in enterprise content and malicious tool output as adversarial conditions rather than hypothetical edge cases. Noema Master Company Document FINAL.pdf

⸻

41. Capability and Bounded Recovery

Capability execution semantics must define how failures are handled.

Relevant recovery behavior may include:

Timeout
    ↓
Verify actual state
    ↓
Decide whether continuation is safe
Explicit rejection
    ↓
Terminal failure
    ↓
No retry unless contract permits it
Dependency unavailable
    ↓
Bounded backoff
    ↓
Escalate if recovery budget exhausted
Policy service unavailable
    ↓
Fail closed
    ↓
ESCALATE

A Capability must not define a recovery strategy that can create duplicate or uncontrolled consequences.

Recovery budgets must be bounded.

No case should be silently dropped.

The POC explicitly includes recovery from worker retry, process restart, duplicate webhook, timeout after a committed side effect, network interruption, intent change, and abandon-and-resume conditions in its adversarial catalogue. NOEMA POC Specification_1.pdf

⸻

42. Capability Availability vs Authorization

Noema must preserve the distinction between:

Capability Unavailable

and:

Capability Available
+
Actor Unauthorized

and:

Capability Available
+
Actor Technically Authorized
+
Policy Permitted
+
Target Unauthorized

and:

Capability Available
+
Authorization Satisfied
+
Business State Does Not Permit Action

and:

Capability Available
+
Authorization Satisfied
+
Policy Satisfied
+
Target Valid
+
State Valid
+
Execution Failure

and:

Capability Invocation
+
Outcome Cannot Yet Be Determined

These represent different failure or decision categories.

They must remain separately observable for:

* Trust;
* recovery;
* audit;
* explanation;
* benchmarking;
* operational diagnosis.

The POC’s failure taxonomy separately distinguishes AUTHORITY, POLICY, STATE_CONFLICT, EXECUTION_UNCERTAINTY, SECURITY, and other intervention categories. NOEMA POC Specification PDF.pdf

⸻

43. Capability and Enterprise Ownership

Noema should not unnecessarily recreate capabilities already provided by mature enterprise infrastructure.

Where identity, Policy, durability, observability, or execution infrastructure already provides a reliable primitive, Noema should interoperate with it rather than rebuilding it without a concrete reason.

Noema’s responsibility is to establish the governed relationship among:

Intent
State
Authority
Policy
Action
Capability
Execution
Verification
Outcome
Provenance

It does not need to own every underlying infrastructure primitive.

This preserves the distinction between Noema as an execution-governance layer and the enterprise systems that own their respective capabilities and business state.

The broader architecture explicitly positions Noema as a trusted execution layer between sources of Intent and enterprise systems that carry out consequential actions, rather than as a replacement for those systems. Noema Master Company Document FINAL.pdf

⸻

44. Capability Ontology

At the conceptual level:

Capability
├── identity
├── semantic business meaning
├── owner
├── target semantics
├── parameter schema
├── preconditions
├── required authorization layer
├── policy requirements
├── side effects
├── expected outcome schema
├── verification strategy
├── retry semantics
├── recovery semantics
├── risk classification
├── audit requirements
├── implementation binding
├── availability
├── version
└── provenance

This is an ontology-level representation.

It is intentionally not the final implementation schema.

The executable representation belongs in:

11-contracts/

The ontology establishes the semantic identity and boundaries.

The contract layer establishes executable representation and validation.

The integration layer establishes concrete bindings.

The Execution Controller remains responsible for actually invoking the approved Capability.

⸻

45. Canonical Capability Lifecycle

A Capability may conceptually move through states such as:

DISCOVERED
   ↓
REGISTERED
   ↓
VALIDATED
   ↓
AVAILABLE
   ↓
INVOKABLE

Alternative states include:

UNAVAILABLE
DEGRADED
DEPRECATED
REVOKED
UNKNOWN
PROHIBITED

A Capability must not become invokable merely because it was discovered.

Conceptually:

Discovered
   ↓
Registration
   ↓
Semantic / Contract Validation
   ↓
Authorization / Security Review
   ↓
Registered
   ↓
Available
   ↓
Invokable

PROHIBITED is a distinct positive boundary condition where an operation is known but must not execute.

A Capability may therefore be known to Noema while simultaneously being:

* unavailable;
* revoked;
* deprecated;
* prohibited.

Lifecycle state must remain distinguishable from semantic identity.

⸻

46. Canonical Distinctions

Noema must preserve the following distinctions:

Capability
"What operation is this system explicitly able to perform?"
Action
"What operation is proposed or intended?"
Authority
"Who is permitted to cause it?"
Technical Authorization
"Can this Principal invoke this Capability?"
Policy Authorization
"Does this parameterization satisfy the applicable Policy?"
Business Authorization
"Given the resolved Target and current state,
should this specific Action be permitted?"
Contract
"Under what explicit terms may the operation execute?"
Availability
"Can the registered Capability currently be invoked?"
Execution
"What attempt was made?"
Verification
"What evidence establishes what actually happened?"
Outcome
"What actually happened as a consequence?"

These concepts are related but must not be collapsed into a single abstraction.

In particular:

Capability ≠ Action
Capability ≠ Authority
Capability ≠ Permission
Capability ≠ Trust
Capability ≠ Contract
Capability ≠ Availability
Capability ≠ Execution
Capability ≠ Verification
Capability ≠ Outcome

This separation is necessary for Noema to determine not merely whether an operation is technically possible, but whether a specific consequential operation should be permitted and whether the resulting enterprise state actually reflects the intended Outcome.

⸻

47. Core Invariants

Invariant 1

A Capability represents an explicit, bounded ability of a registered system or execution environment to perform a defined operation.

Invariant 2

Capability does not imply Authority.

Invariant 3

Capability does not imply Permission.

Invariant 4

Capability does not imply Trust.

Invariant 5

Capability availability does not imply authorization.

Invariant 6

Authorization must be evaluated against the specific Actor / Principal, Action, and resolved Target where applicable.

Invariant 7

Technical authorization does not establish business authorization.

Invariant 8

A model-generated tool call or tool definition does not automatically constitute a Noema Capability.

Invariant 9

Noema must not invent Capabilities to satisfy an Intent.

Invariant 10

Nothing outside the registered Capability boundary may be invokable.

Invariant 11

Prohibited consequential Capabilities may be represented explicitly as prohibited rather than merely omitted where a positive safety assertion is required.

Invariant 12

Capability semantics must be distinguishable from transport or implementation mechanisms.

Invariant 13

Capabilities must have typed, versioned execution semantics sufficient for deterministic boundary validation.

Invariant 14

Capabilities with consequential side effects require explicit authorization, Policy, idempotency, verification, recovery, and audit semantics.

Invariant 15

A Capability must define or reference the semantics required to determine whether its execution result can be verified.

Invariant 16

A timeout must not be interpreted as success or failure solely from the Capability invocation response.

Invariant 17

Capability failures must be distinguishable from invalid Actions.

Invariant 18

Capability availability must be distinguishable from Capability existence.

Invariant 19

An Agent cannot acquire Authority merely by discovering or invoking a Capability.

Invariant 20

Model output, retrieved content, enterprise text, and tool responses must not be allowed to expand the executable Capability boundary.

Invariant 21

Credentials must remain outside model context and direct model execution paths.

Invariant 22

Arbitrary HTTP and arbitrary SQL are not Capabilities.

Invariant 23

Capability access must follow minimum-necessary visibility and applicable tenant / Principal scoping.

Invariant 24

The authoritative business state associated with a Capability remains owned by the relevant system of record.

Invariant 25

Noema must revalidate relevant execution conditions at the execution gate when authorization, Target, Policy, or state may have become stale.

Invariant 26

Capability use in consequential workflows must be causally reconstructable through audit and provenance.

Invariant 27

Noema’s autonomous operating boundary cannot exceed the explicitly registered Capabilities available to it.

Invariant 28

Capability existence never guarantees execution success or business Outcome.

Invariant 29

Capability discovery does not make a Capability executable.

Invariant 30

Capability availability, authorization, Policy satisfaction, Action validity, execution success, and Outcome verification must remain independently observable.

Invariant 31

A Capability response is evidence or execution data, not executable authority.

Invariant 32

A Capability binding must not grant the model direct credentials or direct enterprise access.

Invariant 33

For consequential Capability invocations, idempotency and retry semantics must be explicit rather than inferred.

Invariant 34

An uncertain execution outcome must be resolved through verification rather than assumption or blind retry.

Invariant 35

The enterprise system remains authoritative for the business state it owns; Capability invocation does not transfer ownership of that state to Noema.

These invariants express the architectural boundary established across the Noema Master Document and POC: probabilistic model output proposes, registered capabilities constrain what can execute, Trust governs whether execution may proceed, and verification establishes what actually happened.  

⸻

48. Relationship to Other Canonical Domains

This document defines the ontology of Capability.

Related definitions live in:

01-ontology/
├── actor.md
├── intent.md
├── action.md
├── context.md
├── policy.md
├── constraint.md
├── authority.md
├── outcome.md
└── state.md

Trust and authorization semantics involving Capabilities belong primarily in:

03-trust/

Capability execution semantics belong in:

04-execution/

Capability registration, schemas, typed interfaces, compatibility, and contracts belong in:

11-contracts/

External system and connector mappings belong in:

06-enterprise/

Reference Capability implementations belong in:

09-reference-workflows/

The separation is intentional.

The Capability ontology defines what executable ability exists.

The Authority and Trust domains determine whether it may be exercised in the present case.

The Action domain defines what operation Noema proposes or approves.

The Execution domain defines how an approved Capability invocation is attempted.

The Verification domain establishes what actually happened.

The Outcome domain represents the resulting business consequence.

The Enterprise domain identifies the external systems that own the underlying capabilities and authoritative state.

The Contract domain defines the typed executable boundaries connecting these concerns.

⸻

49. Canonical Summary

A Capability is an explicit, bounded, semantically defined ability of a registered system or execution environment to perform a particular operation.

It establishes:

what can technically be done.

It does not establish:

* who may do it;
* whether the Actor is authorized;
* whether the Target is authorized;
* whether Policy permits it;
* whether the Action is trusted;
* whether execution should occur;
* whether execution will succeed;
* what business Outcome will result.

The canonical relationship is:

ACTOR / PRINCIPAL
        │
        │ may satisfy
        ▼
AUTHORIZATION
        │
        │ permits specific
        ▼
ACTION
        │
        │ references
        ▼
REGISTERED CAPABILITY
        │
        │ executed through
        ▼
EXECUTION
        │
        │ verified against
        ▼
ENTERPRISE STATE
        │
        ▼
OUTCOME

The execution boundary is:

MODEL PROPOSAL
      ↓
SCHEMA VALIDATION
      ↓
REGISTERED CAPABILITY?
      ↓
ACTION VALIDATION
      ↓
TARGET-BOUND AUTHORIZATION
      ↓
POLICY
      ↓
TRUST DECISION
      ↓
EXECUTION GATE REVALIDATION
      ↓
CAPABILITY EXECUTION
      ↓
VERIFICATION
      ↓
AUDIT / PROVENANCE

The model may propose.

The Capability Registry defines what executable operations exist.

Noema validates whether the proposed Action resolves to a registered Capability.

Authority, Policy, Context, evidence, and Trust determine whether that specific operation may proceed.

The Execution Controller performs only the approved, bounded operation.

The enterprise system remains authoritative for the resulting business state.

Verification establishes the actual consequence rather than inferring it from the invocation response.

Audit and provenance preserve the causal chain.

The resulting architecture is therefore:

Probabilistic Intelligence
        │
        │ proposes
        ▼
Deterministic Noema Boundary
        │
        ├── Intent
        ├── Context
        ├── State
        ├── Authority
        ├── Policy
        ├── Trust
        ├── Action
        ├── Registered Capability
        ├── Contract
        └── Execution Gate
                │
                ▼
        Enterprise System
                │
                ▼
           Verification
                │
                ▼
             Outcome

Noema’s Capability model prevents the probabilistic reasoning layer from becoming an unrestricted execution layer.

The model may propose.

The Registry defines what exists.

Noema determines what may be invoked.

The Execution Controller invokes only the explicitly permitted Capability.

The enterprise system remains authoritative for the resulting business state.

Verification establishes what actually happened.

Audit establishes why the consequential operation occurred and under which Actor, Intent, Action, Target, authority, Policy, evidence, Capability, execution attempt, and observed Outcome.

That is the Capability boundary: explicit, registered, typed, bounded, target-aware, policy-aware, authorization-aware, verifiable, auditable, and incapable of expanding merely because a model requests something outside it.