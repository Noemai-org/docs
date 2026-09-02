Human Intervention

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/human-intervention.md

⸻

1. Definition

Human Intervention is the explicit transition of an execution, trust decision, or recovery process into a controlled human decision boundary when Noema cannot safely or deterministically proceed autonomously.

Human intervention is not an execution failure by itself.

It is a controlled safety mechanism.

The fundamental principle is:

Noema cannot safely decide
        ↓
Do not guess
        ↓
Preserve state
        ↓
Escalate to authorized human
        ↓
Record human decision
        ↓
Resume, reject, modify, or terminate

⸻

2. Core Principle

Human intervention exists to resolve states that cannot be safely resolved through deterministic system policy.

It must not become a general-purpose escape hatch for uncertainty that should instead be resolved through better system design.

⸻

3. Why Human Intervention Exists

Noema is designed around bounded autonomy.

Some situations cannot be safely resolved automatically.

Examples:

high-risk financial action
ambiguous business state
irreconcilable execution
policy exception
unusual security event
legal or regulatory exception
irreversible operation
conflicting authoritative evidence

When the system cannot establish a safe deterministic transition:

STOP

is preferable to:

GUESS

⸻

4. Human Intervention Is Not Model Judgment

An LLM may identify that a situation appears unusual.

It must not independently decide:

"Human approval is probably needed."

for consequential workflows unless that transition is defined by deterministic policy.

The canonical path is:

Evidence
   ↓
Policy
   ↓
Deterministic condition
   ↓
Human Intervention Required

⸻

5. Human Intervention Boundary

The conceptual boundary is:

                 NOEMA
                    │
              deterministic
               evaluation
                    │
          ┌─────────┴─────────┐
          │                   │
       RESOLVE             ESCALATE
          │                   │
          ▼                   ▼
     EXECUTION          HUMAN REVIEW
                              │
                              ▼
                       HUMAN DECISION
                              │
                              ▼
                    DETERMINISTIC RESUME

The human becomes a decision participant, not an uncontrolled replacement for the system.

⸻

6. Human Intervention vs Clarification

These are different mechanisms.

Clarification

The system needs information from the Intent originator.

"What account do you want to use?"

Human Intervention

The system needs an authorized decision-maker or operator to resolve an execution, trust, policy, or operational condition.

"This refund exceeds the automatic approval limit.
Manager approval required."

Therefore:

Clarification ≠ Human Intervention

⸻

7. Human Intervention vs Manual Execution

Human intervention does not necessarily mean the human performs the Action.

Example:

Human:
Approve refund.
Consumer:
Execute refund.

The human provides the decision.

The execution system performs the Action.

This preserves the Action Contract and execution boundary.

⸻

8. Human Intervention vs Human-in-the-Loop

Human-in-the-loop is a broad architectural pattern.

Human intervention is a specific Noema semantic state:

automatic execution cannot safely continue
        ↓
authorized human decision required

Not every human-in-the-loop interaction constitutes Human Intervention.

⸻

9. Intervention Trigger

An intervention should be created only when a deterministic condition requires it.

Possible triggers:

RISK_THRESHOLD_EXCEEDED
POLICY_EXCEPTION
EXECUTION_UNKNOWN
CONFLICTING_EVIDENCE
IRREVERSIBLE_ACTION
MANUAL_APPROVAL_REQUIRED
RECOVERY_EXHAUSTED
SECURITY_REVIEW_REQUIRED
BUSINESS_EXCEPTION

The canonical taxonomy may evolve.

⸻

10. Risk-Based Intervention

Risk may determine that human approval is required.

Example:

Action:
transfer ₦50,000,000
Policy:
automatic execution permitted ≤ ₦10,000,000

Result:

HUMAN_INTERVENTION_REQUIRED

This is a deterministic policy outcome.

⸻

11. Policy-Based Intervention

A policy may explicitly require human approval.

Example:

Action:
delete enterprise account
Policy:
enterprise account deletion requires administrator approval

The system transitions to:

PENDING_HUMAN_REVIEW

⸻

12. Unknown Execution

Human intervention may be required when reconciliation cannot establish whether an Action occurred.

Example:

Payment request
    ↓
Provider timeout
    ↓
UNKNOWN
    ↓
Provider reconciliation unavailable
    ↓
HUMAN REVIEW

The human may inspect the authoritative system or initiate a controlled recovery procedure.

⸻

13. Conflicting Evidence

Suppose:

Payment Service:
REFUNDED

while:

Payment Provider:
NOT_REFUNDED

Noema must not arbitrarily choose one.

Possible transition:

CONFLICTING_EVIDENCE
        ↓
HUMAN_INTERVENTION

⸻

14. Intervention Object

Conceptually:

HumanIntervention {
    intervention_id
    subject
    reason
    required_role
    priority
    status
    created_at
    expires_at
    decision
}

The exact persistence schema is implementation-specific.

⸻

15. Intervention Identity

Each intervention requires a stable identifier:

intervention_id

This provides a durable reference for:

decision
audit
notifications
escalation
resolution

⸻

16. Intervention Subject

The intervention must identify what requires human attention.

Possible subjects:

intent
action
action_contract
execution
failure
compensation
trust_decision
policy_exception

Example:

subject_type = EXECUTION
subject_id = exec_123

⸻

17. Intervention Reason

The reason must be machine-readable.

Example:

reason_code:
RECOVERY_EXHAUSTED

with human-readable context:

Three execution attempts failed because the external
payment provider remained unavailable.

⸻

18. Required Human Authority

Not every human can resolve every intervention.

The intervention may require:

role
permission
scope
organization
resource ownership
approval level

Example:

refund > ₦10m
    ↓
finance_manager

The system must verify that the responding human possesses the required authority.

⸻

19. Human Identity

A human decision must be attributable.

At minimum:

actor_id
timestamp
decision

should be recorded.

For stronger auditability:

identity
role
authorization context
authentication method
reason

may also be retained.

⸻

20. Human Intervention Is Authorized Action

A human decision is itself consequential.

Therefore:

Human decision
     ↓
Authorization
     ↓
Recorded decision
     ↓
Execution / recovery

A human must not bypass Noema’s control boundaries merely because the intervention exists.

⸻

21. Intervention States

A conceptual lifecycle is:

CREATED
   ↓
PENDING
   ↓
CLAIMED
   ↓
IN_REVIEW
   ↓
DECIDED
   ↓
RESOLVED

Possible terminal states include:

REJECTED
EXPIRED
CANCELLED
ESCALATED

⸻

22. CREATED

The system has determined that human intervention is required.

No human has yet been assigned.

⸻

23. PENDING

The intervention is available for an authorized reviewer.

⸻

24. CLAIMED

A human has taken ownership of the intervention.

This prevents multiple operators from unknowingly making independent decisions.

⸻

25. IN_REVIEW

The reviewer is actively evaluating:

intent
action
trust
policy
evidence
execution state
business state
failure
recovery options

⸻

26. DECIDED

The authorized human has made a decision.

The decision must be recorded immutably.

⸻

27. RESOLVED

The system has successfully applied the human decision.

For example:

Human:
APPROVE
System:
issued execution contract
Execution:
SUCCESS
Intervention:
RESOLVED

⸻

28. Decision Types

A foundational decision model may include:

APPROVE
REJECT
RETRY
CANCEL
COMPENSATE
ESCALATE
REQUEST_INFORMATION

The available decisions should be constrained by the intervention type.

⸻

29. Approval

Approval authorizes the next predefined Action or execution transition.

Example:

Human:
APPROVE_REFUND
System:
issue approved execution

Approval does not mean:

the human manually executed the refund

unless the workflow explicitly defines it that way.

⸻

30. Rejection

The human determines that the proposed execution should not continue.

Human:
REJECT
Execution:
not performed / terminated

The rejection reason should be recorded where required.

⸻

31. Retry Decision

A human may authorize another execution attempt.

Example:

Attempt 1:
TIMEOUT
Attempt 2:
TIMEOUT
Human review:
RETRY
Attempt 3:
EXECUTING

The retry remains subject to Action and contract semantics.

⸻

32. Cancellation Decision

The human may request cancellation where cancellation is supported.

The system must still determine whether cancellation is technically possible.

Human:
CANCEL
System:
attempt cancellation

Human approval does not override physical execution reality.

⸻

33. Compensation Decision

A human may authorize compensation where automatic recovery is unavailable or prohibited.

Example:

Inventory reservation:
SUCCESS
Payment:
FAILURE
Automatic compensation:
not permitted
Human:
APPROVE_RELEASE_RESERVATION

The resulting compensation should still be executed through the canonical execution mechanism.

⸻

34. Escalation

A human reviewer may lack sufficient authority.

Example:

support_agent
    ↓
finance_manager
    ↓
risk_committee

Escalation should preserve the same intervention lineage.

It should not create an unrelated case.

⸻

35. Request Information

The reviewer may determine that additional information is necessary.

This should be distinguished from user clarification.

Example:

Human reviewer:
"Need proof of transaction ownership."

The workflow can then transition into a defined information-gathering state.

⸻

36. Human Decision Is Not an Intent

A human decision such as:

APPROVE

is not itself the original user Intent.

It is a control decision over an existing workflow.

This distinction prevents semantic contamination between:

user intent

and:

operational governance

⸻

37. Human Decision Is Not an Override of Reality

A human cannot establish that an external Action succeeded merely by selecting:

APPROVE

Approval establishes permission for the next transition.

The external system still determines whether execution succeeds.

⸻

38. Human Decision and Trust

Human intervention may change the authorization context.

Example:

Automatic policy:
DENIED
Human with required authority:
APPROVE_EXCEPTION

The resulting execution must receive an explicit authorization record.

The system must never silently convert:

DENIED

into:

AUTHORIZED

without recording the governing exception.

⸻

39. Human Override

An override is permissible only when the policy model explicitly supports it.

An override must record:

original decision
override decision
authorized actor
authority basis
reason
timestamp
scope

A human override is therefore an auditable policy event.

⸻

40. No Silent Overrides

The following is prohibited:

Trust:
DENIED
Operator:
manually flips database flag
Execution:
proceeds

The canonical system must instead record:

Trust:
DENIED
Exception:
APPROVED_BY_AUTHORIZED_ACTOR
Execution:
AUTHORIZED

⸻

41. Intervention Evidence

A reviewer should receive sufficient evidence to make the decision.

Depending on the case:

Intent
Action
Action Contract
Trust decision
Policy evaluation
Risk assessment
Execution history
Failure history
Business-state evidence
Relevant audit history

Evidence should be bounded by authorization.

⸻

42. Evidence Does Not Become Truth Because a Human Sees It

Human review does not eliminate evidence requirements.

A reviewer cannot legitimately conclude:

"Looks successful."

when the system requires authoritative evidence.

The decision must be grounded in available evidence.

⸻

43. Human Intervention and Determinism

Human intervention is compatible with deterministic Noema architecture.

The deterministic system defines:

when intervention is required
who may decide
what decisions are permitted
what evidence is presented
what transitions each decision enables

The human supplies:

the decision

The system then deterministically applies it.

⸻

44. Human Intervention and the LLM

The LLM may assist with:

summarizing evidence
explaining failures
organizing context
presenting relevant information

But it should not secretly determine:

whether the human approved
whether policy allows an override
whether execution may continue

Those remain deterministic decisions.

⸻

45. Human Intervention and Auditability

Every intervention should create an auditable chain:

Trigger
   ↓
Evidence
   ↓
Policy
   ↓
Intervention
   ↓
Reviewer
   ↓
Decision
   ↓
System transition
   ↓
Execution
   ↓
Outcome

This is especially important for regulated or high-consequence workflows.

⸻

46. Human Intervention and Time

Interventions may have deadlines.

Example:

expires_at:
2026-08-26T12:00:00Z

Expiration should produce a deterministic transition:

PENDING
   ↓
EXPIRED

The system should not leave interventions indefinitely unresolved.

⸻

47. Expired Intervention

An expired intervention may result in:

cancel execution
escalate
re-evaluate
terminate
request new approval

The appropriate behavior must be policy-defined.

⸻

48. Intervention Priority

Interventions may have priority:

CRITICAL
HIGH
NORMAL
LOW

Priority determines operational handling.

It does not determine authorization.

⸻

49. Intervention Queue

A human review system may expose:

pending interventions
assigned reviewer
priority
age
deadline
required authority
subject
reason

The UI is implementation-specific.

The semantic intervention record is canonical.

⸻

50. Claiming and Concurrency

Two humans must not unknowingly resolve the same intervention.

Therefore claiming should be concurrency-safe.

Example:

Reviewer A → CLAIM
Reviewer B → CLAIM

Only one should successfully acquire the intervention unless the policy explicitly supports collaborative review.

⸻

51. Multi-Party Approval

Some Actions may require multiple approvals.

Example:

finance_manager
      +
security_manager
      ↓
execution authorized

The intervention model should support approval requirements without collapsing multiple decisions into one actor.

⸻

52. Approval Quorum

A policy may require:

2 of 3 authorized approvers

The system should evaluate quorum deterministically.

Example:

A → APPROVE
B → APPROVE
C → PENDING

Result:

QUORUM_SATISFIED

if policy requires 2 of 3.

⸻

53. Separation of Duties

Certain workflows may prohibit the same person from:

requesting
approving
executing

the same consequential Action.

Human intervention must respect separation-of-duties policies.

⸻

54. Human Intervention and Execution

The canonical relationship is:

Execution
    ↓
requires intervention
    ↓
Human Decision
    ↓
Execution resumes

or:

Execution
    ↓
requires intervention
    ↓
Human Decision
    ↓
Compensation

or:

Execution
    ↓
requires intervention
    ↓
Human Decision
    ↓
Termination

⸻

55. Intervention Does Not Rewrite Execution

Suppose:

Attempt 1:
FAILURE

A human approves retry.

The history remains:

Attempt 1:
FAILURE
Human:
RETRY
Attempt 2:
SUCCESS

The intervention becomes another causal event.

⸻

56. Intervention and Compensation

When compensation requires approval:

Original Execution
      ↓
Failure
      ↓
Compensation Required
      ↓
Human Intervention
      ↓
Approval
      ↓
Compensation Contract
      ↓
Compensation Execution

The compensation must retain lineage to the original execution.

⸻

57. Intervention and Reconciliation

For an UNKNOWN execution:

UNKNOWN
   ↓
RECONCILIATION

should normally precede human intervention.

Human intervention is appropriate when:

automatic reconciliation fails

or:

evidence remains contradictory

This prevents unnecessary human workload.

⸻

58. Intervention and Recovery Exhaustion

Automatic recovery may be bounded:

retry_count = 3

After exhaustion:

RECOVERY_EXHAUSTED
       ↓
HUMAN_INTERVENTION

The system should not retry indefinitely merely because no human has responded.

⸻

59. Intervention Closure

An intervention should close only when its required decision and resulting system transition have been completed.

Example:

Human:
APPROVE
Execution:
SUCCESS
Intervention:
RESOLVED

Not:

Human:
APPROVE
Intervention:
RESOLVED
Execution:
still pending

unless the intervention explicitly represents only the approval step.

⸻

60. Intervention Record Immutability

The historical decision should not be overwritten.

If a correction is required:

Original decision
    ↓
Correction / subsequent decision

rather than mutating the historical record.

This preserves audit integrity.

⸻

61. Intervention Invariants

Invariant 1

Human intervention is a controlled system state, not an informal escape hatch.

Invariant 2

Human intervention must be triggered by explicit deterministic conditions.

Invariant 3

Human intervention is distinct from user clarification.

Invariant 4

Human intervention does not automatically mean the human performs the Action.

Invariant 5

Human decisions must be attributable to an authorized actor.

Invariant 6

Human approval does not establish that an external Action succeeded.

Invariant 7

Human overrides must be explicitly represented and auditable.

Invariant 8

A human cannot silently bypass Trust or Policy.

Invariant 9

Human decisions must operate within defined authority boundaries.

Invariant 10

Human intervention must preserve execution history.

Invariant 11

Unknown execution should be reconciled automatically where possible before escalating to a human.

Invariant 12

Interventions must have deterministic lifecycle states.

Invariant 13

Interventions may expire and must have defined expiration behavior where appropriate.

Invariant 14

Concurrent reviewers must not unknowingly resolve the same intervention.

Invariant 15

Multi-party approval requirements must be evaluated deterministically.

Invariant 16

Human intervention must preserve causal lineage from trigger through final Outcome.

⸻

62. Canonical Mental Model

                 EXECUTION
                     │
                     ▼
            Deterministic Policy
                     │
              ┌──────┴──────┐
              │             │
           PROCEED        ESCALATE
              │             │
              ▼             ▼
          EXECUTION    HUMAN INTERVENTION
                            │
                     ┌──────┴──────┐
                     │             │
                  APPROVE        REJECT
                     │             │
                     ▼             ▼
                 EXECUTION      TERMINATE
                     │
                     ▼
                  OUTCOME

For uncertainty:

EXECUTION
    ↓
UNKNOWN
    ↓
RECONCILIATION
    ↓
┌───────────────┐
│               │
SUCCESS      FAILURE
│               │
▼               ▼
OUTCOME      RECOVERY
                │
                ▼
        HUMAN INTERVENTION
        when automation
        cannot safely continue

⸻

63. Final Definition

Human Intervention is the controlled, auditable mechanism through which Noema transfers a workflow into authorized human decision-making when deterministic policy and available evidence cannot safely produce the next autonomous transition.

The core invariant is:

When Noema cannot safely determine the next consequential transition, it must stop rather than guess. Human intervention provides an explicit decision boundary: the system determines when intervention is required, who is authorized to decide, what decisions are permissible, and how those decisions affect execution; the human supplies the decision, and Noema records and applies it deterministically.