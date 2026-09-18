Constraint

Status: Foundational Draft
Version: 0.2
Domain: Ontology
Canonical Path: ontology/constraint.md

A Constraint narrows the set of permissible interpretations, Actions, or Executions; it does not tell Noema how to satisfy the Intent.

⸻

1. Definition

A Constraint is an explicit condition, boundary, restriction, or limitation that narrows the set of permissible interpretations, Actions, or Executions associated with an Intent.

A Constraint answers:

What must, must not, or may not be violated?

Examples:

* “Book a flight under $500.”
* “Only use the corporate card.”
* “Do not send an SMS.”
* “The transfer must not exceed $10,000.”
* “Use the customer’s existing account.”
* “The meeting must occur before Friday.”

A Constraint narrows what is acceptable.

It does not necessarily specify the exact Action required to satisfy the Intent.

The fundamental distinction is:

Intent
"What does the Actor want to accomplish?"
Constraint
"What boundaries restrict how that objective may be satisfied?"

A Constraint therefore defines part of Noema’s permissible solution space.

It is not itself a plan, Action, Capability, Policy, Authority, or Trust decision.

⸻

2. Constraint in the Noema Model

A Constraint exists around the Intent-to-Action-to-Execution lifecycle.

Actor
  │
  ▼
Intent
  │
  ├── constrained by ──► Constraint
  │
  ▼
Trust
  │
  ▼
Action
  │
  ├── constrained by ──► Constraint
  │
  ▼
Execution
  │
  ├── constrained by ──► Constraint
  │
  ▼
Outcome

Constraints may therefore apply at different semantic stages.

A Constraint may originate before Action formation, be derived during resolution, be introduced by Policy or Capability semantics, or become relevant at execution time.

The existence of a Constraint does not determine how Noema satisfies it.

The Constraint narrows the permissible space; the Intent Engine, Trust system, Planner, and Execution system determine what can proceed within that space.

⸻

3. Constraint Is Not Intent

An Intent expresses what the Actor wants to accomplish.

A Constraint limits how that objective may be satisfied.

Example:

Intent:
"Book me a flight to London."
Constraint:
"Do not spend more than $800."

The Intent defines the objective.

The Constraint defines a boundary around the objective.

Therefore:

Intent defines the objective; Constraint restricts the permissible solution space.

A Constraint without an associated objective, Action, Resource, or Execution context may be semantically incomplete.

⸻

4. Constraint Is Not Preference

A Preference expresses a desirable characteristic.

A Constraint establishes a boundary that must be respected unless it is explicitly relaxable under applicable rules.

For example:

Preference:
"I prefer a morning flight."
Constraint:
"The flight must depart before 12:00."

The first may be negotiable.

The second is binding unless explicitly changed, relaxed, superseded, or overridden through an authorized mechanism.

Noema must not silently convert a Preference into a Constraint.

Likewise, Noema must not silently weaken a Constraint into a Preference merely because satisfying it is inconvenient.

⸻

5. Constraint Is Not Policy

A Policy is a rule imposed by a governing authority, organization, or system.

A Constraint is a specific boundary applicable to an Intent, Action, Resource, or Execution.

For example:

Policy:
"Employees may only book economy-class flights."
Constraint:
"Book economy class."

The Policy establishes the governing rule.

The Constraint represents the applicable restriction in the current interaction or execution context.

A Policy may therefore generate, impose, or determine applicable Constraints.

Policy
   │
   │ applies / derives
   ▼
Constraint

But the two concepts must remain distinct.

A Constraint should preserve its Policy provenance where the Constraint derives from Policy.

⸻

6. Constraint Is Not Authority

Authority answers:

Who is permitted to cause an Action?

Constraint answers:

What boundaries apply to the Action?

For example:

Actor:
Finance Manager
Authority:
May approve payments.
Constraint:
Payment must not exceed $50,000.

Possessing Authority does not remove Constraints.

Likewise, satisfying a Constraint does not establish that the Actor possesses the Authority required to perform the Action.

Authority and Constraint therefore participate independently in Noema’s decision model.

⸻

7. Constraint Is Not Capability

Capability answers:

What can the system explicitly perform?

Constraint answers:

What limits what may be interpreted, proposed, or performed?

For example:

Capability:
payments.transfer.create
Constraint:
amount <= $10,000

The Capability establishes an explicit system ability.

The Constraint limits its permissible use in the applicable context.

A Capability does not override a Constraint.

A Constraint does not create a Capability.

⸻

8. Constraint Is Not Condition

A Condition describes a fact or predicate that may determine whether a rule, transition, Constraint, or operation applies.

A Constraint is the resulting boundary that must be respected.

For example:

Condition:
Customer is a premium member.
Constraint:
Premium customers may receive discounts up to 20%.

Conditions may therefore participate in determining which Constraints apply.

The detailed semantics of Conditions should remain separate from Constraint semantics.

Noema must also preserve the distinction between:

Condition is true

and:

Constraint is satisfied

A true Condition does not itself establish Constraint satisfaction unless the applicable rule explicitly establishes that relationship.

⸻

9. Constraint Sources

Constraints may originate from different sources.

Actor

"Don't use my personal card."

Intent

"Under $500."

Policy

"Only approved vendors."

Authority

"Manager approval required above $10,000."

System

"Maximum transaction amount is $25,000."

Capability

"Destination account must be verified."

External Environment

"Airport must be within 50 km."

The source of a Constraint should be preserved.

Where multiple sources impose Constraints, their provenance and applicable precedence must remain reconstructable.

⸻

10. Constraint Scope

A Constraint may apply to different parts of the lifecycle.

Intent-level

Limits what may satisfy an Intent.

Intent:
"Find me a hotel."
Constraint:
"Under $200 per night."

Action-level

Limits a specific Action.

Action:
CreateRefund
Constraint:
Amount <= original transaction amount.

Execution-level

Limits how an Action may be executed.

Action:
SendNotification
Constraint:
Do not send outside business hours.

Resource-level

Limits what Resources may be affected.

Constraint:
Only modify accounts owned by the requesting organization.

Target-level

Limits which resolved Target may be acted upon.

Constraint:
Only act on the customer's verified account.

Scope must be explicit enough for Noema to determine where and when a Constraint applies.

⸻

11. Constraint Types

Constraints may take different semantic forms.

11.1 Value Constraint

Restricts a value.

amount <= $10,000
age >= 18
quantity <= 100

11.2 Temporal Constraint

Restricts time.

Execute before Friday.
Do not execute between 22:00 and 06:00.

11.3 Spatial Constraint

Restricts location.

Only vendors within Lagos.
Pickup must occur within 10 km.

11.4 Resource Constraint

Restricts which Resources may be affected.

Only modify the customer's primary account.

11.5 Actor Constraint

Restricts which Actors or Principals may participate.

Only a Finance Manager may approve this Action.

An Actor Constraint may overlap with Authority semantics; the governing Authority model remains authoritative for determining whether an Actor is actually permitted.

11.6 Capability Constraint

Restricts which Capabilities may be used.

Only use approved payment providers.

11.7 Sequence Constraint

Restricts ordering.

Identity verification must occur before payment.

11.8 Cardinality Constraint

Restricts quantity.

Maximum 3 retries.
At least 2 approvals required.

11.9 State Constraint

Restricts execution based on state.

Card must be active.
Subscription must not already be cancelled.

11.10 Side-Effect Constraint

Restricts effects.

Do not send external notifications.
Do not modify billing information.

11.11 Target Constraint

Restricts which resolved entity may be affected.

Only operate on the account resolved from the authenticated customer identity.

This is particularly important where technical access to a Capability does not establish authorization for every possible Target.

⸻

12. Hard and Soft Constraints

Not every restriction has the same semantic force.

Noema should distinguish between:

Hard Constraint

A boundary that must not be violated.

amount <= $10,000

Violation means the candidate Action or Execution is invalid unless an explicit and authorized override mechanism exists.

Soft Constraint

A desirable boundary that may be relaxed under explicitly permitted circumstances.

Prefer flights under $500.

However, Noema should avoid treating “soft constraint” as an excuse for silently violating user requirements.

The relaxation of a Soft Constraint should itself be explicit.

A Soft Constraint therefore remains a Constraint while active; its semantic force is different from that of a Hard Constraint.

⸻

13. Constraint Priority

Constraints may conflict.

For example:

User Constraint:
"Spend no more than $500."
Corporate Policy:
"Use approved vendors."
System Constraint:
"Minimum purchase is $600."

Noema must not resolve such conflicts through arbitrary model preference.

Conflict resolution must follow an explicit precedence model.

Conceptually:

Constraint A
Constraint B
Constraint C
     │
     ▼
Constraint Resolution
     │
     ├── satisfiable
     ├── conflict
     └── indeterminate

The precedence rules belong to the relevant Trust, Policy, Authority, and governance specifications.

Priority metadata must not itself be interpreted as authorization to violate a higher-order rule.

⸻

14. Constraint Conflict

Two or more Constraints conflict when they cannot simultaneously be satisfied within the same applicable scope and context.

Example:

Constraint A:
amount <= $500
Constraint B:
amount >= $1,000

The constraint set is unsatisfiable.

Noema should represent this explicitly.

It must not silently choose one Constraint.

Possible outcomes include:

UNSATISFIABLE
REQUIRES_CLARIFICATION
REQUIRES_OVERRIDE
ESCALATION_REQUIRED

depending on applicable Policy, Authority, and Trust semantics.

⸻

15. Constraint Satisfaction

A Constraint may be:

SATISFIED
VIOLATED
UNKNOWN
NOT_APPLICABLE
CONFLICTING

These states should remain distinct.

In particular:

UNKNOWN ≠ SATISFIED
UNKNOWN ≠ VIOLATED

If Noema cannot establish that a Constraint is satisfied, it must not treat uncertainty as compliance when the Constraint is material to the proposed Action or Execution.

A Constraint may only be evaluated as NOT_APPLICABLE when Noema has sufficient basis to establish that its scope does not include the current operation.

⸻

16. Constraint Evaluation

Conceptually:

Candidate Action
      │
      ▼
Applicable Constraints
      │
      ▼
Constraint Evaluation
      │
      ├── satisfied
      ├── violated
      ├── unknown
      └── conflict

Constraint evaluation should produce an explicit result.

It should not exist only as an implicit model judgment.

For material Constraints, the evaluation should identify the relevant evidence, state, source, and evaluation context necessary to reconstruct why the Constraint was considered satisfied, violated, or unknown.

⸻

17. Constraint and Trust

Constraints are an input to Noema’s deterministic Trust decision.

Conceptually:

Intent
  +
Context
  +
Evidence
  +
Authority
  +
Policy
  +
Constraints
       │
       ▼
     Trust

A material Constraint violation should prevent progression toward Execution unless an explicit override mechanism exists and is authorized.

Constraint satisfaction does not itself establish Trust.

Trust must consider the broader resolved Intent, Context, Evidence, Authority, Policy, Target, State, and other applicable controls.

⸻

18. Constraint and Ambiguity

A Constraint may itself be ambiguous.

For example:

"Keep it reasonably cheap."

The system cannot necessarily determine the exact boundary.

Noema should distinguish:

Constraint:
Known and evaluable
Constraint:
Known but not currently evaluable
Constraint:
Ambiguous
Constraint:
Conflicting

Ambiguity should not be silently converted into a precise numeric threshold by the model when that threshold materially affects execution.

Where the Constraint is material and insufficiently specified, Noema should transition to the appropriate clarification or escalation state rather than inventing a boundary.

⸻

19. Constraint and Natural Language

Natural-language input may contain explicit or implicit Constraints.

For example:

“Find me a hotel in London, but nothing over £150 a night.”

The semantic representation should separate:

Intent:
Find a hotel in London.
Constraint:
price_per_night <= £150

This separation allows Noema to reason over the Intent and Constraint independently.

The extracted Constraint remains a candidate semantic interpretation until validated according to the applicable Noema processing and trust controls.

⸻

20. Explicit vs Derived Constraints

Constraints may be:

Explicit

Directly stated by an Actor or source.

"Don't spend more than $500."

Derived

Logically obtained from another authoritative rule.

Policy:
Managers require approval for payments > $10,000.
Derived Constraint:
Approval required when amount > $10,000.

Derived Constraints must preserve their provenance.

Noema should be able to explain:

Why does this Constraint apply?

without exposing private model reasoning.

The explanation should identify the relevant source, rule, applicability conditions, and derivation where those are available.

⸻

21. Constraint Provenance

Every material Constraint should have provenance.

Conceptually:

Constraint
   │
   ├── source
   ├── authority
   ├── scope
   ├── subject
   ├── target
   ├── creation time
   ├── validity period
   └── derivation

For example:

Constraint:
amount <= $10,000
Source:
Corporate Payment Policy v3.2
Applied because:
Actor belongs to Finance Department.

The provenance establishes why the Constraint exists and why it was considered applicable.

Provenance must remain distinguishable from a model-generated explanation.

⸻

22. Constraint Lifecycle

Constraints may have their own lifecycle.

PROPOSED
   ↓
VALIDATED
   ↓
ACTIVE
   ↓
SATISFIED / VIOLATED
   ↓
EXPIRED / REMOVED

A Constraint may also become:

SUPERSEDED
REVOKED
CONFLICTING
UNKNOWN

Lifecycle state must not be confused with Constraint satisfaction.

For example:

ACTIVE + UNKNOWN

is materially different from:

EXPIRED + SATISFIED

The former remains applicable but cannot currently be evaluated; the latter is no longer applicable.

⸻

23. Constraint Temporal Validity

Some Constraints only apply during a specific period.

For example:

Constraint:
Promotional discount <= 30%
Valid:
2026-08-01 → 2026-08-31

Noema must evaluate temporal validity before applying the Constraint.

An expired Constraint must not continue to restrict execution merely because it remains stored.

Likewise, a future Constraint must not be treated as currently active merely because it has already been registered.

Temporal validity is distinct from lifecycle state.

⸻

24. Constraint and Delegation

Delegation may introduce additional Constraints.

For example:

Principal:
Finance Director
Delegate:
Finance Manager
Delegated Authority:
Approve expenses
Constraint:
Maximum approval amount = $25,000

The Delegate’s Authority is therefore bounded by the delegation’s Constraints.

Delegation does not automatically transfer all of the Principal’s Authority.

The provenance of delegated Constraints should identify the delegation from which the restriction derives.

⸻

25. Constraint and Capability

A Capability may impose operational Constraints.

For example:

Capability:
payments.transfer.create
Constraints:
- currency = USD
- amount <= $25,000
- destination must be verified

These Constraints may come from the underlying system or from the Capability’s registered contract.

Noema must respect them even when the user’s Intent itself does not specify them.

A Capability Constraint therefore participates in the Effective Constraint Set without becoming a general Policy or Authority decision.

⸻

26. Constraint and Action

An Action may have Constraints beyond those attached to the Intent.

Example:

Intent:
"Renew my card."
Intent Constraint:
"Use my existing address."
Action:
UpdateCardAddress
Action Constraint:
"Address must have been verified within the last 12 months."

The Action must satisfy both applicable Intent and Action Constraints.

Conceptually:

Intent Constraints
        +
Action Constraints
        +
Policy Constraints
        +
Capability Constraints
        ↓
Effective Constraint Set

Action formation must not remove or silently weaken applicable Intent Constraints.

⸻

27. Effective Constraint Set

The Effective Constraint Set is the collection of all applicable Constraints that must be satisfied for a particular Action or Execution.

Conceptually:

Effective Constraints =
Intent Constraints
+
Actor Constraints
+
Policy Constraints
+
Authority Constraints
+
System Constraints
+
Capability Constraints
+
Execution Constraints

Additional sources may exist where defined by the relevant ontology or contract.

Not every category will exist in every interaction.

Noema must determine applicability explicitly.

The Effective Constraint Set should be established before a consequential Action is permitted to execute.

⸻

28. Constraint Relaxation

A Constraint may sometimes be relaxed.

Relaxation must be explicit.

For example:

Original Constraint:
budget <= $500
Relaxation:
budget <= $600

The system should record:

* original Constraint
* new Constraint
* Actor requesting relaxation
* Authority permitting relaxation
* reason
* timestamp
* applicable Policy
* validity or scope of the relaxation

A model must not silently relax a Constraint to make an Action executable.

A relaxation changes the effective boundary and therefore must itself be governed and auditable.

⸻

29. Constraint Override

An Override is an explicit authorization to bypass, modify, or otherwise supersede an applicable Constraint.

Override requires, at minimum:

Actor
Authority
Constraint
Scope
Reason
Validity

For example:

Constraint:
Refund <= $500
Override:
Manager authorizes refund of $750.

The existence of an Override should be represented explicitly.

An Override does not imply that every Constraint may be overridden.

Whether a Constraint is overrideable must itself be determined by the applicable Policy, Authority, and governance model.

⸻

30. Constraint and Human Clarification

When Noema cannot determine how to satisfy a material Constraint, it should transition into a deterministic clarification state.

For example:

User:
"Book the cheapest flight, but don't make it too inconvenient."
Constraint:
"inconvenient" is not sufficiently defined.

Noema should not invent a definition such as:

Maximum 2 stops.
Maximum 8 hours.

unless that definition is supported by explicit Context, Policy, or another authoritative source.

Instead:

Constraint
   ↓
Insufficiently specified
   ↓
Clarification Required

This is a fundamental Noema behavior.

Clarification should seek only the information necessary to resolve the material ambiguity.

⸻

31. Constraint and Probabilistic Models

Models may extract candidate Constraints from natural language.

For example:

User:
"Nothing over $200."
Model:
price <= 200

The model may propose the semantic interpretation.

However:

The model’s confidence that a Constraint exists is not itself proof that the Constraint is valid.

Noema should validate material Constraints before relying on them for deterministic execution.

The model therefore contributes candidate semantic structure; it does not independently establish the governing Constraint.

⸻

32. Constraint and Bounded Autonomy

Constraints are one of the primary mechanisms through which Noema bounds autonomous behavior.

Intent
   │
   ▼
Candidate Actions
   │
   ▼
Constraints
   │
   ├── eliminate invalid Actions
   │
   ▼
Trust
   │
   ▼
Executable Action

An autonomous system must operate within the Effective Constraint Set.

Autonomy therefore cannot be treated as permission to optimize around Constraints.

Where a Constraint prevents execution, the autonomous system must remain within the resulting bounded state and follow the applicable clarification, escalation, or termination path.

⸻

33. Constraint and Outcome

The resulting Outcome should indicate material Constraint violations when they occur.

For example:

Constraint:
Refund <= $500
Actual Outcome:
Refund = $750

The Outcome must not be represented simply as successful.

It should capture the relevant violation and the mechanism by which the Constraint was overridden, if such an override was legitimate.

Where the violation itself indicates an execution anomaly, the Outcome should preserve that distinction rather than allowing ordinary success semantics to conceal it.

⸻

34. Constraint Model

Conceptually:

Constraint
├── identity
├── statement
├── type
├── source
├── scope
├── subject
├── target
├── operator
├── value
├── validity
├── priority
├── force
├── status
├── applicability
├── provenance
└── relaxation / override rules

This is an ontology-level model, not the final storage schema.

The executable representation belongs in the contract layer.

The ontology defines the semantic properties that must be represented; the implementation schema determines how those properties are encoded, validated, versioned, and enforced.

⸻

35. Constraint Evaluation Model

At a conceptual level:

Constraint
      │
      ▼
Is Applicable?
      │
      ├── No ───────► Not Applicable
      │
      └── Yes
           │
           ▼
     Can It Be Evaluated?
           │
       ┌───┴────┐
       │        │
      No       Yes
       │        │
       ▼        ▼
    UNKNOWN   Evaluate
                 │
          ┌──────┼──────┐
          ▼      ▼      ▼
      SATISFIED VIOLATED CONFLICT

The distinction between UNKNOWN and VIOLATED is critical.

Noema must not convert inability to establish satisfaction into a violation without evidence.

Likewise, it must not convert inability to establish satisfaction into satisfaction.

⸻

36. Constraint Precedence

When multiple Constraints apply, Noema must establish their precedence through explicit rules.

Possible dimensions include:

* Source Authority
* Specificity
* Scope
* Temporal Validity
* Policy Hierarchy
* Explicit Override
* Delegated Authority

However, these dimensions must not be resolved by an implicit “most reasonable” model judgment.

Precedence must be defined by the applicable Policy, Trust, Authority, and governance model.

Where precedence cannot be established deterministically, the conflict must remain explicit.

⸻

37. Constraint Conflict Resolution

When Constraints conflict, Noema should not silently optimize for the most likely interpretation.

Instead:

Conflict
   │
   ├── deterministic precedence exists
   │       │
   │       ▼
   │   Resolve conflict
   │
   └── no valid precedence
           │
           ▼
     Clarification /
     Escalation /
     Rejection

The correct response depends on the authority and Policy governing the interaction.

A model may explain the conflict or propose alternatives, but it must not independently establish a precedence rule that changes the effective execution boundary.

⸻

38. Canonical Distinctions

Noema must preserve these distinctions:

Constraint    ≠ Intent
Constraint    ≠ Preference
Constraint    ≠ Policy
Constraint    ≠ Authority
Constraint    ≠ Capability
Constraint    ≠ Condition
Constraint    ≠ Trust
Constraint    ≠ Permission

And:

Constraint Satisfaction
        ≠
Constraint Existence

And:

Unknown
        ≠
Satisfied

And:

Constraint Violation
        ≠
Capability Failure

And:

Constraint Applicability
        ≠
Constraint Satisfaction

A Constraint may exist but not apply.

A Constraint may apply but have unknown satisfaction.

A Constraint may be satisfied while the Action remains unauthorized.

These distinctions must remain explicit throughout the Noema model.

⸻

39. Core Invariants

Invariant 1

A Constraint limits the permissible solution space of an Intent, Action, or Execution.

Invariant 2

A Constraint does not define the Intent itself.

Invariant 3

A Constraint must not be silently treated as a Preference.

Invariant 4

A Policy and a Constraint derived from that Policy are distinct concepts.

Invariant 5

A Capability does not override a Constraint.

Invariant 6

Authority does not automatically remove Constraints.

Invariant 7

Material Constraints must be explicitly evaluable before consequential execution.

Invariant 8

Unknown Constraint satisfaction must not be treated as satisfaction.

Invariant 9

Constraint conflicts must be explicitly represented.

Invariant 10

Constraint relaxation must be explicit.

Invariant 11

Constraint overrides require appropriate Authority.

Invariant 12

Material Constraints must have sufficient provenance.

Invariant 13

A model must not silently invent material Constraint values.

Invariant 14

A model’s confidence does not establish Constraint validity.

Invariant 15

Noema must preserve the distinction between Constraint violation and Capability failure.

Invariant 16

The Effective Constraint Set must be determined before an Action is permitted to execute.

Invariant 17

A Constraint’s existence does not establish that it is applicable to the current Action or Execution.

Invariant 18

A Constraint’s applicability does not establish that it is satisfied.

Invariant 19

A Constraint may only be considered satisfied when the relevant evidence or authoritative state supports satisfaction.

Invariant 20

Noema must not silently weaken, remove, or relax a material Constraint to make an Action executable.

Invariant 21

Constraint precedence must be determined through explicit governing rules rather than implicit model preference.

Invariant 22

Derived Constraints must preserve their source and derivation provenance.

Invariant 23

Constraint lifecycle state must remain distinct from Constraint satisfaction state.

Invariant 24

Temporal validity must be evaluated before a time-bounded Constraint is treated as applicable.

Invariant 25

A Constraint override must not be assumed valid merely because an Actor requests or asserts it.

Invariant 26

Constraint evaluation must remain distinguishable from Trust evaluation.

Invariant 27

Constraint evaluation must remain distinguishable from Authorization evaluation.

Invariant 28

Constraint evaluation must remain distinguishable from Policy definition.

Invariant 29

Model-generated Constraint interpretations are proposals until validated through the applicable Noema controls.

Invariant 30

Noema must not allow probabilistic model behavior to silently expand the permissible execution space beyond the Effective Constraint Set.

⸻

40. Relationship to Other Canonical Domains

This document defines the ontology of Constraint.

Related concepts include:

01-ontology/
├── actor.md
├── action.md
├── capability.md
├── intent.md
├── context.md
├── policy.md
├── authority.md
├── state.md
├── outcome.md
└── provenance.md

Constraint evaluation and deterministic Trust belong primarily in:

03-trust/

Executable constraint representation belongs in:

11-contracts/

Business-specific constraints belong in:

06-enterprise/

Execution-time enforcement belongs in:

04-execution/

Policy semantics determine governing rules from which applicable Constraints may be derived.

Authority semantics determine who may create, satisfy, relax, or override Constraints where applicable.

Capability semantics define operational boundaries that may themselves impose Constraints.

State semantics provide authoritative facts against which State Constraints may be evaluated.

Outcome semantics record material Constraint violations and their consequences.

⸻

41. Canonical Summary

A Constraint is an explicit boundary that restricts the permissible interpretation, Action, or Execution associated with an Intent.

The central relationship is:

Intent
   │
   ├── constrained by ─────► Constraints
   │
   ▼
Candidate Actions
   │
   ├── constrained by ─────► Constraints
   │
   ▼
Trust
   │
   ▼
Execution
   │
   ├── constrained by ─────► Constraints
   │
   ▼
Outcome

Constraints are therefore one of the fundamental mechanisms through which Noema converts an open-ended human objective into a bounded, deterministic execution space.

The Effective Constraint Set may incorporate applicable boundaries originating from:

Intent
Actor
Policy
Authority
System
Capability
Execution
Context

but the source and semantics of those boundaries must remain distinguishable.

The canonical processing relationship is:

Natural Language / Source
          ↓
Candidate Constraint
          ↓
Semantic Validation
          ↓
Applicability
          ↓
Effective Constraint Set
          ↓
Constraint Evaluation
          ↓
Trust / Authority / Policy
          ↓
Action
          ↓
Execution Gate
          ↓
Execution
          ↓
Outcome / Verification

A Constraint may be:

SATISFIED
VIOLATED
UNKNOWN
NOT_APPLICABLE
CONFLICTING

and these states must not be collapsed.

Likewise:

Constraint
     ≠
Policy
Constraint
     ≠
Authority
Constraint
     ≠
Capability
Constraint
     ≠
Trust
Constraint
     ≠
Permission

The most important rule is:

Noema may reason within a Constraint, but it must never silently reason a material Constraint away.

A model may identify or propose a Constraint.

Noema validates its semantic representation and applicability.

The governing Policy and Authority determine applicable precedence and override conditions.

The Effective Constraint Set defines the boundaries within which Action planning may occur.

Execution must remain inside those boundaries unless an explicit, authorized, and auditable relaxation or override changes them.

And where a material Constraint cannot be established as satisfied, Noema must preserve that uncertainty rather than converting it into implicit compliance.

⸻

Outline of the substantive update

I preserved the original 41-section architecture and full coverage. The update is primarily a semantic tightening rather than a rewrite into a different document.

1. Sharpened the definition

The original definition was good, but I made the central ontology distinction more explicit:

Constraint = permissible-solution-space boundary

This gives Constraint a precise role relative to Intent and Action.

2. Strengthened the Constraint lifecycle boundary

The original model stopped largely at:

Intent → Trust → Action → Execution

The revised model makes it explicit that Constraints can remain relevant through:

Intent → Action → Execution → Outcome

This matters because a Constraint can be violated by an actual execution even if the candidate Action initially appeared compliant.

3. Added Target Constraint as an explicit semantic type

This is important for Noema because Target resolution is a distinct control boundary.

A constraint such as:

only act on the customer’s verified account

is not merely a generic Resource Constraint. It can materially constrain the resolved Target.

4. Tightened Constraint vs Authority

The original distinction was correct, but the revised version explicitly prevents the reverse confusion:

satisfying a Constraint does not establish Authority.

That prevents the ontology from accidentally turning constraints into an authorization mechanism.

5. Tightened Constraint vs Capability

The distinction is now explicitly bidirectional:

* Capability does not override Constraint.
* Constraint does not create Capability.

That keeps the Capability and Constraint ontologies orthogonal.

6. Strengthened UNKNOWN

The original correctly said:

UNKNOWN ≠ SATISFIED

I retained that and added:

UNKNOWN ≠ VIOLATED

This is important for deterministic execution because inability to establish compliance is not necessarily evidence of a violation.

7. Expanded provenance

Derived Constraints now explicitly retain their derivation source.

This supports the larger Noema requirement that the system be able to answer:

Why does this boundary apply?

without turning model reasoning into provenance.

8. Tightened lifecycle vs satisfaction

A Constraint can be:

ACTIVE + UNKNOWN

or:

EXPIRED + SATISFIED

Those are fundamentally different dimensions.

The revised document makes that distinction explicit.

9. Strengthened relaxation and override semantics

The original had both concepts, but the update makes clear that:

* not every Constraint is necessarily overrideable;
* overrideability itself is governed;
* a model cannot create an override merely by proposing one;
* changing the Constraint changes the effective execution boundary and therefore requires auditability.

10. Strengthened conflict handling

The revised document makes explicit that the model cannot resolve Constraint conflicts through a “reasonable” optimization.

If deterministic precedence does not exist:

Conflict
   ↓
Clarification / Escalation / Rejection

rather than model-selected compromise.

11. Expanded the invariant set

The original had 16 invariants.

The revised version has 30, primarily because several principles that were implicit in the body needed to become explicit ontology invariants:

* existence ≠ applicability
* applicability ≠ satisfaction
* lifecycle ≠ satisfaction
* derived Constraint ≠ source Policy
* Constraint evaluation ≠ Trust
* Constraint evaluation ≠ Authorization
* model interpretation ≠ validated Constraint
* material Constraints cannot be silently weakened
* precedence must be explicit
* temporal validity must be evaluated
* override validity must be independently established

12. Preserved the original conceptual boundary

Most importantly, I did not turn Constraint into a generic “rules” abstraction.

The document continues to preserve the distinction:

Intent
"What is wanted?"
Constraint
"What boundaries restrict it?"
Policy
"What governing rule establishes requirements?"
Authority
"Who may cause it?"
Capability
"What can the system explicitly do?"
Action
"What operation is proposed?"
Trust
"May this proposed operation proceed?"
Execution
"What was actually attempted?"
Outcome
"What actually happened?"

That separation is the important ontology work here.