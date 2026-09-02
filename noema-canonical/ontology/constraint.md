A constraint narrows the set of permissible interpretations or executions; it does not tell Noema how to satisfy the Intent.

Constraint

Status: Foundational Draft
Version: 0.1
Domain: Ontology
Canonical Path: ontology/constraint.md

⸻

1. Definition

A Constraint is a condition, boundary, or restriction that limits the set of permissible interpretations, Actions, or Executions associated with an Intent.

A Constraint answers:

What must, must not, or may not be violated?

Examples:

"Book a flight under $500."
"Only use the corporate card."
"Do not send an SMS."
"The transfer must not exceed $10,000."
"Use the customer's existing account."
"The meeting must occur before Friday."

A Constraint narrows what is acceptable.

It does not necessarily specify the exact Action required to satisfy the Intent.

⸻

2. Constraint in the Noema Model

A Constraint exists around the Intent-to-Action lifecycle.

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

Constraints may therefore apply at different stages.

⸻

3. Constraint Is Not Intent

An Intent expresses what the Actor wants to accomplish.

A Constraint limits how that objective may be satisfied.

Intent:
"Book me a flight to London."
Constraint:
"Do not spend more than $800."

The Intent defines the objective.

The Constraint defines a boundary.

Therefore:

Intent defines the objective; Constraint restricts the permissible solution space.

⸻

4. Constraint Is Not Preference

A Preference expresses a desirable characteristic.

A Constraint establishes a boundary that must be respected.

For example:

Preference:
"I prefer a morning flight."
Constraint:
"The flight must depart before 12:00."

The first may be negotiable.

The second is binding unless explicitly changed or removed.

Noema must not silently convert a Preference into a Constraint.

⸻

5. Constraint Is Not Policy

A Policy is a rule imposed by a governing authority or system.

A Constraint is a specific boundary applicable to an Intent, Action, Resource, or Execution.

For example:

Policy:
"Employees may only book economy-class flights."
Constraint:
"Book economy class."

The Policy establishes the governing rule.

The Constraint represents the applicable restriction in the current interaction.

A Policy may therefore generate or impose Constraints.

Policy
   │
   │ applies
   ▼
Constraint

But the two concepts must remain distinct.

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

⸻

7. Constraint Is Not Capability

Capability answers:

What can the system do?

Constraint answers:

What limits what may be done?

For example:

Capability:
payments.transfer.create
Constraint:
amount <= $10,000

The Capability enables the operation.

The Constraint limits its permissible parameters.

⸻

8. Constraint Is Not Condition

A Condition describes something that may determine whether a particular rule, transition, or operation applies.

A Constraint is the resulting boundary that must be respected.

For example:

Condition:
Customer is a premium member.
Constraint:
Premium customers may receive discounts up to 20%.

Conditions may therefore participate in determining which Constraints apply.

The detailed semantics of Conditions should remain separate from Constraint semantics.

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

External Environment

"Airport must be within 50 km."

The source of a Constraint should be preserved.

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

⸻

11. Constraint Types

Constraints may take different semantic forms.

11.1 Value Constraint

Restricts a value.

amount <= $10,000
age >= 18
quantity <= 100

⸻

11.2 Temporal Constraint

Restricts time.

Execute before Friday.
Do not execute between 22:00 and 06:00.

⸻

11.3 Spatial Constraint

Restricts location.

Only vendors within Lagos.
Pickup must occur within 10 km.

⸻

11.4 Resource Constraint

Restricts which Resources may be affected.

Only modify the customer's primary account.

⸻

11.5 Actor Constraint

Restricts which Actors may participate.

Only a Finance Manager may approve this Action.

⸻

11.6 Capability Constraint

Restricts which Capabilities may be used.

Only use approved payment providers.

⸻

11.7 Sequence Constraint

Restricts ordering.

Identity verification must occur before payment.

⸻

11.8 Cardinality Constraint

Restricts quantity.

Maximum 3 retries.
At least 2 approvals required.

⸻

11.9 State Constraint

Restricts execution based on state.

Card must be active.
Subscription must not already be cancelled.

⸻

11.10 Side-Effect Constraint

Restricts effects.

Do not send external notifications.
Do not modify billing information.

⸻

12. Hard and Soft Constraints

Not every restriction has the same semantic force.

Noema should distinguish between:

Hard Constraint

A boundary that must not be violated.

amount <= $10,000

Violation means the candidate Action or Execution is invalid.

Soft Constraint

A desirable boundary that may be relaxed under explicitly permitted circumstances.

Prefer flights under $500.

However, Noema should avoid treating “soft constraint” as an excuse for silently violating user requirements.

The relaxation of a soft constraint should itself be explicit.

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

The precedence rules belong to the relevant Trust and Policy specifications.

⸻

14. Constraint Conflict

Two Constraints conflict when they cannot simultaneously be satisfied.

Example:

Constraint A:
amount <= $500
Constraint B:
amount >= $1,000

The constraint set is unsatisfiable.

Noema should represent this explicitly.

It must not silently choose one constraint.

Possible outcomes include:

UNSATISFIABLE
REQUIRES_CLARIFICATION
REQUIRES_OVERRIDE

depending on applicable policy.

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

UNKNOWN is not SATISFIED.

If Noema cannot establish that a Constraint is satisfied, it must not treat uncertainty as compliance when the Constraint is material to execution.

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

⸻

17. Constraint and Trust

Constraints are an input to Noema’s deterministic Trust decision.

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

A material Constraint violation should prevent progression toward Execution unless an explicit override mechanism exists.

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

⸻

19. Constraint and Natural Language

Natural-language input may contain implicit Constraints.

For example:

“Find me a hotel in London, but nothing over £150 a night.”

The semantic representation should separate:

Intent:
Find a hotel in London.
Constraint:
price_per_night <= £150

This separation allows Noema to reason over the Intent and Constraint independently.

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

⸻

21. Constraint Provenance

Every material Constraint should have provenance.

Conceptually:

Constraint
   │
   ├── source
   ├── authority
   ├── scope
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

The provenance establishes why the Constraint exists.

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

These constraints may come from the underlying system.

Noema must respect them even when the user’s Intent itself does not specify them.

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

Not every category will exist in every interaction.

Noema must determine applicability explicitly.

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
* applicable policy

A model must not silently relax a Constraint to make an Action executable.

⸻

29. Constraint Override

An Override is an explicit authorization to bypass or modify an applicable Constraint.

Override requires:

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

⸻

30. Constraint and Human Clarification

When Noema cannot determine how to satisfy a material Constraint, it should transition into a deterministic clarification state.

For example:

User:
"Book the cheapest flight, but don't make it too inconvenient."
Noema:
Constraint "inconvenient" is not sufficiently defined.

Noema should not invent a definition such as:

Maximum 2 stops.
Maximum 8 hours.

unless that definition is supported by explicit context or policy.

Instead:

Constraint
   ↓
Insufficiently specified
   ↓
Clarification Required

This is a fundamental Noema behavior.

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
├── status
├── provenance
└── relaxation / override rules

This is an ontology-level model, not the final storage schema.

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

The distinction between unknown and violated is critical.

⸻

36. Constraint Precedence

When multiple Constraints apply, Noema must establish their precedence through explicit rules.

Possible dimensions include:

Source Authority
Specificity
Scope
Temporal Validity
Policy Hierarchy
Explicit Override

However, these dimensions must not be resolved by an implicit “most reasonable” model judgment.

Precedence must be defined by the applicable Policy and Trust model.

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

The correct response depends on the authority and policy governing the interaction.

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

and:

Unknown
        ≠
Satisfied

⸻

39. Core Invariants

Invariant 1

A Constraint limits the permissible solution space of an Intent, Action, or Execution.

Invariant 2

A Constraint does not define the Intent itself.

Invariant 3

A Constraint must not be silently treated as a Preference.

Invariant 4

A Policy and the Constraint derived from that Policy are distinct concepts.

Invariant 5

A Capability does not override a Constraint.

Invariant 6

Authority does not automatically remove Constraints.

Invariant 7

Material Constraints must be explicitly evaluable before execution.

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

Constraints are therefore one of the fundamental mechanisms through which Noema converts an open-ended human objective into a bounded, deterministic execution space.

The most important rule is:

Noema may reason within a Constraint, but it must never silently reason a material Constraint away.