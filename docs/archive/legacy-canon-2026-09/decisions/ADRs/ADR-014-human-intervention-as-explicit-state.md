ADR-014 — Human Intervention as Explicit State

Status: Accepted
Date: 2026-09-19
Decision Type: Foundational
Domain: Architecture / Trust / Autonomy
Canonical Path: decisions/ADRs/ADR-014-human-intervention-as-explicit-state.md

⸻

1. Decision

Noema shall represent human intervention as an explicit, machine-readable lifecycle state or state condition, rather than treating human involvement as an implicit conversational behavior or exceptional failure path.

When Noema cannot safely continue autonomously because a human decision, clarification, approval, confirmation, or intervention is required, that requirement must be represented explicitly.

The canonical principle is:

Human Intervention
        ↓
Explicit State
        ↓
Explicit Human Action
        ↓
Re-evaluation
        ↓
Continue / Wait / Block

Human intervention is therefore a first-class part of Noema’s control model.

⸻

2. Context

Noema is designed to operate across existing software systems while maintaining a deterministic boundary between probabilistic understanding and executable action.

Some Intents cannot safely proceed without additional human involvement.

Examples include:

* unresolved ambiguity
* missing information
* required approval
* required confirmation
* authorization that cannot be established
* elevated risk
* policy-mandated human review
* conflicting evidence
* unexpected execution conditions
* exceptions requiring human judgment

A system that treats these conditions merely as conversational interruptions loses important lifecycle information.

For example:

Model:
"Can you confirm?"

does not by itself establish a durable system state.

Noema must know:

Why is human intervention required?
What exactly is required?
Who may provide it?
What evidence will satisfy the requirement?
When did the requirement arise?
What happened after the human responded?

⸻

3. Problem Statement

Without an explicit representation of human intervention, implementations may collapse materially different conditions into generic states such as:

FAILED
PENDING
ERROR

This loses semantic information.

For example:

WAITING_FOR_APPROVAL

is materially different from:

BLOCKED_BY_POLICY

Likewise:

WAITING_FOR_CLARIFICATION

is materially different from:

FAILED_EXECUTION

Human intervention must therefore be represented as an explicit control condition.

⸻

4. Decision Principles

4.1 Human Intervention Is Not Failure

A requirement for human intervention does not necessarily indicate system failure.

For example:

Transfer > policy threshold
        ↓
Approval required
        ↓
WAITING_FOR_APPROVAL

The system has behaved correctly.

Similarly:

"Send it to John."
        ↓
Multiple Johns
        ↓
WAITING_FOR_CLARIFICATION

is not an execution failure.

⸻

4.2 Human Intervention Must Be Explicit

The system must represent the requirement rather than relying solely on a conversational exchange.

Conceptually:

Human Intervention Required
{
    type
    reason
    required_action
    eligible_actor
    evidence_required
    created_at
    expires_at
}

The exact schema belongs to the relevant canonical specifications.

⸻

4.3 Human Input Is Evidence

When a human supplies clarification, approval, confirmation, or other required information, the resulting input should become explicit evidence associated with the lifecycle.

It should not merely disappear into conversation history.

For example:

WAITING_FOR_APPROVAL
        ↓
approval.received
        ↓
EVALUATING

The approval is an auditable event.

⸻

5. Canonical Human Intervention States

Human intervention may be represented through specific waiting states rather than one generic state.

Canonical examples include:

WAITING_FOR_CLARIFICATION
WAITING_FOR_CONFIRMATION
WAITING_FOR_APPROVAL
HUMAN_INTERVENTION_REQUIRED

Other reason-specific states may be introduced where necessary.

The taxonomy should remain extensible.

⸻

6. Clarification

Clarification is required when Noema cannot establish sufficient semantic meaning.

Example:

Intent:
"Send the report to John."
Problem:
Multiple eligible recipients named John.
State:
WAITING_FOR_CLARIFICATION

Noema must not select a recipient merely because one appears statistically likely.

The human response supplies additional semantic information.

WAITING_FOR_CLARIFICATION
        ↓
clarification.received
        ↓
Intent updated
        ↓
Validation
        ↓
Trust Evaluation

⸻

7. Confirmation

Confirmation is appropriate when the Actor must explicitly acknowledge a consequential action.

Example:

Action:
Permanently delete account.
State:
WAITING_FOR_CONFIRMATION

A valid confirmation may allow the Intent to return to evaluation.

WAITING_FOR_CONFIRMATION
        ↓
confirmation.received
        ↓
EVALUATING
        ↓
READY

Confirmation must not be inferred from silence or unrelated conversational behavior unless an explicit policy defines such semantics.

⸻

8. Approval

Approval is distinct from confirmation.

Approval generally represents authorization from an Actor or role with the required governance authority.

Example:

Transfer:
₦10,000,000
Policy:
Secondary approval required.

The state becomes:

WAITING_FOR_APPROVAL

After approval:

approval.received
        ↓
EVALUATING
        ↓
READY

The Trust Engine must re-evaluate all other relevant conditions.

Approval alone does not guarantee readiness.

⸻

9. General Human Intervention

Some conditions cannot be represented adequately by clarification, confirmation, or approval.

Example:

Conflicting authoritative evidence
        ↓
HUMAN_INTERVENTION_REQUIRED

The human may need to determine how the situation should proceed.

Noema must not manufacture a resolution merely to avoid stopping.

⸻

10. Human Intervention and Trust

Human intervention is part of the Trust lifecycle but does not itself establish Trust.

For example:

WAITING_FOR_APPROVAL
        ↓
approval.received
        ↓
EVALUATING

The Trust Engine must still evaluate:

* authorization
* policy
* evidence
* capability
* constraints
* context
* freshness
* risk

Therefore:

Human Approval
≠
Automatic READY

The correct sequence is:

Human Action
    ↓
Evidence
    ↓
Re-evaluation
    ↓
Trust State

⸻

11. Human Intervention and Autonomy

Human intervention defines one of the boundaries of bounded autonomy.

Conceptually:

Autonomous Execution Permitted
              │
              ▼
      Conditions remain valid?
          ┌───┴───┐
         YES      NO
          │        │
          ▼        ▼
       Continue   Intervene

Noema should stop autonomous execution when a mandatory human condition arises.

Autonomy therefore includes the ability to stop and request human intervention.

⸻

12. Intervention Must Identify the Required Human Action

A human intervention state should identify what the human must do.

Examples:

WAITING_FOR_CLARIFICATION
required_action:
    identify recipient
WAITING_FOR_CONFIRMATION
required_action:
    confirm permanent deletion
WAITING_FOR_APPROVAL
required_action:
    approve transfer
HUMAN_INTERVENTION_REQUIRED
required_action:
    resolve conflicting account ownership evidence

This allows interfaces and downstream systems to render the appropriate intervention workflow.

⸻

13. Eligible Human Actor

Where applicable, Noema should identify who or what role may satisfy the intervention.

Examples:

eligible_actor:
    original Actor

or:

eligible_actor:
    Finance Approver

or:

eligible_actor:
    Compliance Officer

The eligibility requirement itself must be governed by explicit authorization and policy.

Noema must not accept arbitrary human input as satisfying a governance requirement.

⸻

14. Intervention Evidence

Human intervention should generate explicit evidence.

Conceptually:

Human Intervention
        │
        ├── actor
        ├── action
        ├── timestamp
        ├── response
        ├── authorization context
        └── provenance

For an approval:

approval.received
approver = actor_123
timestamp = T
approval_scope = transfer_456

The exact representation belongs to the approval and provenance specifications.

⸻

15. Re-Evaluation After Intervention

Noema must not assume that the human intervention resolves every relevant condition.

The canonical transition is:

WAITING
   ↓
Human action received
   ↓
EVALUATING
   ↓
WAITING / BLOCKED / READY

Not:

WAITING
   ↓
Human action
   ↓
READY

For example:

WAITING_FOR_APPROVAL
        ↓
Approval received
        ↓
Authorization expired
        ↓
BLOCKED

The human action may be valid while the overall Intent remains ineligible.

⸻

16. Human Intervention and Intent Mutation

Clarification may legitimately change the canonical Intent representation.

Example:

Before:
recipient = ambiguous
Human:
"John Smith at Acme."
After:
recipient = customer_482

The updated Intent must be validated again.

Human intervention must not silently mutate the Intent without provenance.

⸻

17. Human Intervention and Authority

Human involvement does not automatically confer authority.

For example:

Person A:
"Approve this payment."

does not establish valid approval if Person A is not an eligible approver.

The system must establish:

Human Identity
      +
Role / Authority
      +
Approval Scope
      +
Policy
      ↓
Valid Approval Evidence

⸻

18. Human Intervention Expiration

Some interventions may have temporal validity.

Examples:

approval expires at 14:00
confirmation expires at 15:00
clarification request expires after 24 hours

After expiration:

WAITING
   ↓
Intervention expired
   ↓
EVALUATING

The resulting state depends on current conditions.

It may become:

WAITING
BLOCKED
READY

as appropriate.

⸻

19. Revocation

Human decisions may sometimes be revoked.

Examples:

approval.received
        ↓
approval.revoked
        ↓
EVALUATING
        ↓
WAITING_FOR_APPROVAL

or:

confirmation.received
        ↓
confirmation.revoked
        ↓
BLOCKED / WAITING

The semantics depend on the applicable policy and execution state.

A revoked decision must not silently remain authoritative.

⸻

20. Human Intervention During Execution

Human intervention may also become necessary after execution has begun.

Example:

EXECUTING
    ↓
Unexpected external condition
    ↓
HUMAN_INTERVENTION_REQUIRED

This should be distinguished from a generic execution failure where appropriate.

For example:

Execution:
requires manual reconciliation

is materially different from:

Execution:
technical timeout

The execution state and intervention state should remain appropriately separated.

⸻

21. Human Intervention and Partial Execution

If intervention occurs during a composite Intent, Noema must preserve the state of each component.

Example:

A → COMPLETED
B → HUMAN_INTERVENTION_REQUIRED
C → WAITING

The system must not represent the entire Intent merely as:

FAILED

unless the canonical execution semantics explicitly define the composite operation as failed.

⸻

22. Intervention Routing

A human intervention requirement should be routable to the appropriate interface or workflow.

Possible interfaces include:

* chat
* application UI
* approval workflow
* operations console
* email
* API
* embedded enterprise interface

The presentation layer is not the canonical state.

The canonical state is:

Human intervention required

The interface is merely one mechanism for satisfying it.

⸻

23. No Conversational-Only Intervention

Noema must not depend exclusively on conversation history to determine whether a human intervention requirement has been satisfied.

Bad:

Conversation:
"Sure, do it."
System assumes:
confirmation = true

unless the canonical confirmation semantics explicitly establish that interpretation.

Good:

confirmation.received
confirmation_id
actor
scope
timestamp
provenance

The intervention becomes a structured lifecycle event.

⸻

24. Intervention and Auditability

Every material human intervention should be auditable.

The record should establish:

* why intervention was required
* which Intent was affected
* which state produced the requirement
* what action the human was asked to take
* who provided the intervention
* when it occurred
* what evidence was produced
* what state followed
* which Trust evaluation consumed the evidence

This creates a reconstructible lifecycle.

Example:

T0  EVALUATING
T1  WAITING_FOR_APPROVAL
T2  approval.requested
T3  approval.received
T4  EVALUATING
T5  READY

⸻

25. Intervention and Provenance

Human intervention must preserve provenance.

Conceptually:

InterventionRecord {
    intervention_id
    intent_id
    type
    requested_at
    completed_at
    actor
    action
    evidence
    authorization
    provenance
}

The exact schema remains implementation-specific.

⸻

26. Intervention and Unknown Conditions

Human intervention may be required because Noema cannot establish a mandatory condition.

Example:

Authorization service unavailable.

Noema must not ask a human to “approve” something merely to manufacture authorization unless policy explicitly defines that approval as a valid authorization path.

The distinction between:

UNKNOWN

and:

DENIED

must remain intact.

⸻

27. Intervention Must Not Become a Bypass

Human intervention must not become a generic escape hatch around deterministic controls.

Invalid:

Policy blocks Action
       ↓
Ask human
       ↓
Execute anyway

unless the policy explicitly defines a valid human override mechanism.

Where overrides exist, they must themselves be:

* explicitly authorized
* scoped
* auditable
* policy-governed
* represented as evidence
* subject to re-evaluation

⸻

28. Human Override

Where a system explicitly supports human override, the override should be modeled separately from ordinary approval.

Conceptually:

BLOCKED_BY_POLICY
        ↓
authorized override
        ↓
EVALUATING
        ↓
READY

The override does not erase the original block from history.

The provenance should retain:

original policy decision
override authority
override reason
override timestamp
resulting evaluation

⸻

29. Intervention State and Execution State

Human intervention should not be conflated with execution state.

For example:

Intent State:
RESOLVED
Trust State:
WAITING_FOR_APPROVAL
Execution State:
NOT_STARTED

Or:

Intent State:
EXECUTING
Intervention:
HUMAN_INTERVENTION_REQUIRED

This preserves the architectural separation between:

* semantic lifecycle
* Trust lifecycle
* execution lifecycle
* human intervention

⸻

30. State Transition Principles

Human intervention transitions must follow deterministic rules.

Example:

WAITING_FOR_APPROVAL
+
valid approval received
+
all other conditions satisfied
=
READY

Not:

approval received
=
READY

Likewise:

WAITING_FOR_CLARIFICATION
+
valid clarification received
=
EVALUATING

The updated Intent must then be validated and trusted.

⸻

31. Canonical Intervention Flow

                  Intent
                    │
                    ▼
                EVALUATING
                    │
             Human condition
               required
                    │
                    ▼
          ┌─────────────────────┐
          │ Human Intervention  │
          │      Required       │
          └──────────┬──────────┘
                     │
          ┌──────────┼───────────┐
          │          │           │
     Clarification Approval  Confirmation
          │          │           │
          └──────────┼───────────┘
                     │
                     ▼
              Evidence Received
                     │
                     ▼
                Re-evaluate
                     │
          ┌──────────┼───────────┐
          ▼          ▼           ▼
       WAITING     BLOCKED      READY

⸻

32. Canonical Invariants

Invariant 1

Human intervention is an explicit system state or state condition.

Invariant 2

Human intervention is not inherently a failure.

Invariant 3

Clarification, confirmation, approval, and intervention are semantically distinct.

Invariant 4

Human input must produce explicit evidence where it materially affects Trust.

Invariant 5

Human intervention does not automatically establish Trust.

Invariant 6

Human intervention does not automatically establish authorization.

Invariant 7

Human responses must be subject to applicable authorization and policy.

Invariant 8

A human intervention event should trigger re-evaluation of relevant conditions.

Invariant 9

Human intervention must not silently mutate Intent semantics.

Invariant 10

Human intervention requirements may expire or be revoked where applicable.

Invariant 11

Human override must not bypass policy unless explicitly authorized by policy.

Invariant 12

Human intervention must be auditable.

Invariant 13

Human intervention must preserve provenance.

Invariant 14

Unknown conditions must not be converted into valid authorization merely because a human is available.

Invariant 15

Human intervention may occur before or during execution and must remain distinguishable from execution outcome.

⸻

33. Consequences

Positive Consequences

This decision:

* makes human-in-the-loop behavior explicit
* improves auditability
* preserves deterministic lifecycle semantics
* prevents conversational interactions from becoming hidden authority
* supports approval and confirmation workflows
* provides a clean mechanism for bounded autonomy
* enables intervention routing across multiple interfaces
* makes human decisions reusable as structured evidence
* distinguishes governance conditions from execution failures

Costs

This decision introduces:

* additional lifecycle states
* intervention records
* routing requirements
* identity and authorization requirements for human actions
* additional re-evaluation
* more complex workflow handling

These costs are accepted because implicit human intervention would undermine Noema’s deterministic control model.

⸻

34. Relationship to Other ADRs

This decision reinforces:

* ADR-003 — Probabilistic / Deterministic Boundary
* ADR-004 — Deterministic Trust Evaluation
* ADR-005 — Explicit Execution Contracts
* ADR-006 — Capability / Permission Separation
* ADR-008 — Clarification Over Guessing
* ADR-010 — Trust State Machine
* ADR-011 — Intent State Separate from Execution State
* ADR-012 — Provenance and Auditability
* ADR-013 — Bounded Autonomy

The resulting control model is:

Probabilistic Understanding
          ↓
Deterministic Validation
          ↓
Deterministic Trust
          ↓
Human Intervention When Required
          ↓
Re-evaluation
          ↓
Bounded Autonomous Execution
          ↓
Explicit Execution Contract
          ↓
Outcome

⸻

35. Final Decision Statement

Noema adopts human intervention as an explicit state.

Whenever clarification, confirmation, approval, review, or human judgment is required for an Intent to proceed safely, Noema must represent that requirement explicitly and preserve the resulting human action as structured, auditable evidence.

The canonical rule is:

When Noema requires a human decision to proceed, the requirement must exist as explicit system state; the human response must become explicit evidence; and the Intent must be re-evaluated before execution continues.