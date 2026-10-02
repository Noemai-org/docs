> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Postconditions

Status: Foundational
Version: 0.1
Domain: Execution
Canonical Path: execution/postconditions.md

⸻

1. Definition

A postcondition is an explicit, evaluable condition that must be established after an Action or execution step for the expected semantic effect of that Action to be recognized.

Postconditions answer:

“What must be established after this Action for its expected effect to be considered satisfied?”

They therefore form a semantic verification boundary between execution and Outcome.

Action
   ↓
Execution
   ↓
Observation
   ↓
Evidence / Reconciliation
   ↓
Postcondition Evaluation
   ↓
Outcome

A postcondition describes what must be established. It does not itself establish that the condition is true.

⸻

2. Core Principle

Execution completion does not imply Action success.

An executor can report:

process exited successfully

while the intended business effect did not occur.

Noema therefore distinguishes:

Execution completed
        ≠
Postcondition satisfied
        ≠
Enterprise Business State established

Execution establishes what happened to the execution attempt.

Postcondition evaluation determines whether the required semantic effect has been established from sufficient evidence.

⸻

3. Why Postconditions Exist

Consider:

Action:
activate_card(card_123)

The external API returns:

HTTP 200

This establishes a transport or execution signal.

It does not necessarily establish:

card_123.status = ACTIVE

A postcondition provides the semantic criterion for determining whether the intended effect was established.

Execution Signal
      +
Sufficient Evidence
      ↓
Postcondition Evaluation
      ↓
Semantic Outcome

⸻

4. Execution vs Effect

The canonical distinction is:

Execution

Did the Action attempt complete according to its execution semantics?

Effect

Was the intended semantic effect established?

Postconditions primarily concern the second question.

Execution
   │
   ├── execution status
   │
   └── observations
          ↓
       Evidence
          ↓
  Postcondition Evaluation
          ↓
       Outcome

Execution status remains distinct from Outcome.

⸻

5. Preconditions vs Postconditions

These concepts must remain distinct.

Precondition

What must be true before an Action can execute.

Example:

account.status = ACTIVE

Postcondition

What must be established after the Action executes.

Example:

card.status = ACTIVE

Therefore:

Precondition
    ↓
Trust / Execution Admission
    ↓
Action
    ↓
Execution
    ↓
Postcondition Evaluation

A postcondition must not be treated as a precondition merely because the same state appears in both.

⸻

6. Postconditions Are Not Predictions

A Planner may produce:

expected_postcondition:
card.status = ACTIVE

This is an expected condition, not an observed fact.

The system must subsequently obtain sufficient evidence.

Expected:
card.status = ACTIVE
Observed:
card.status = ACTIVE
Therefore:
postcondition = SATISFIED

The observation must remain distinguishable from the expectation.

⸻

7. Expected vs Observed

Noema should explicitly distinguish:

* Expected Postcondition
* Observation
* Evidence
* Reconciled State
* Postcondition Evaluation

Example:

Expected:
balance = ₦100,000
Observed:
balance = ₦100,000

The equality may establish satisfaction only if:

* the Resource is correctly bound;
* the observation is sufficiently authoritative;
* freshness requirements are satisfied;
* relevant concurrency has been considered;
* the observation is applicable to the specific Action;
* the postcondition evaluation rules permit the observation to establish the condition.

Expected state must never be promoted into observed state merely because the Action was planned to produce it.

⸻

8. Postcondition Evaluation

Conceptually:

evaluate(
    postcondition,
    evidence,
    reconciled_state,
    evaluation_context
)

may produce:

SATISFIED
NOT_SATISFIED
UNKNOWN

UNKNOWN is first-class.

Noema must not convert insufficient evidence into success.

The exact mapping from postcondition evaluation to Outcome belongs to the Outcome model and applicable Action Contract semantics.

⸻

9. Unknown Is Not Failure

Suppose:

Action:
charge_customer

The provider times out.

Noema cannot determine whether the charge occurred.

The postcondition:

transaction.status = COMPLETED

cannot currently be established.

The correct evaluation may therefore be:

UNKNOWN

not:

FAILED

and certainly not:

SUCCESS

UNKNOWN means the truth of the postcondition has not been sufficiently established.

It does not assert that the postcondition is false.

⸻

10. Postconditions and Evidence

Postconditions depend on evidence.

Action
 ↓
Execution
 ↓
Observation
 ↓
Evidence
 ↓
State Reconciliation where required
 ↓
Postcondition Evaluation
 ↓
Outcome

Evidence may come from:

* enterprise database state;
* authoritative API response;
* enterprise event;
* provider confirmation;
* resource inspection;
* transaction reference;
* execution record;
* human confirmation;
* other explicitly permitted evidence sources.

The evidence must be sufficient for the specific postcondition being evaluated.

⸻

11. Evidence Quality

Not all evidence has the same authority.

For example:

Executor:
"payment succeeded"

may be weaker than:

Payment provider:
transaction_123 = SETTLED

The authoritative source depends on the Resource and claim being evaluated.

The canonical Evidence model defines evidence provenance, authority, freshness, conflict, and applicability.

Postcondition evaluation must not treat every execution response as equally authoritative.

⸻

12. Postconditions Are Domain-Semantic

A technical success signal is not necessarily a semantic postcondition.

Example:

HTTP 201

is a transport-level result.

The semantic postcondition might be:

user.account.status = ACTIVE

Noema evaluates the semantic condition rather than assuming that a transport-level success establishes it.

⸻

13. Postcondition Types

Postconditions can describe different kinds of effects.

State

card.status = ACTIVE

Existence

invoice_123 EXISTS

Non-existence

reservation_123 DOES_NOT_EXIST

Relationship

user_123 OWNS card_456

Value

balance = ₦100,000

Event

refund_settled event observed

External Confirmation

provider confirms shipment

The type and evaluation semantics must be explicit.

⸻

14. State Postconditions

A state postcondition specifies the expected state of a Resource.

Example:

Action:
suspend_account(account_123)
Postcondition:
account_123.status = SUSPENDED

The state must be evaluated against an identified Resource and an observation with sufficient authority and freshness.

⸻

15. Existence Postconditions

Some Actions create Resources.

Example:

Action:
create_invoice
Postcondition:
invoice_123 EXISTS

Existence alone may be insufficient.

A stronger postcondition might be:

invoice_123 EXISTS
invoice_123.status = ISSUED
invoice_123.amount = ₦500,000

The Action Contract must define which conditions are required.

⸻

16. Non-Existence Postconditions

Deletion or cancellation may require proving absence.

Example:

Action:
delete_customer(customer_123)
Postcondition:
customer_123 DOES_NOT_EXIST

This is stronger than:

DELETE request returned 204

A successful deletion request does not by itself establish the required business-state condition.

Non-existence can be difficult to establish in eventually consistent systems and may therefore require reconciliation or an explicit observation window.

⸻

17. Relationship Postconditions

Some Actions modify relationships.

Example:

Action:
assign_user_to_team
Postcondition:
user_123 ∈ team_456.members

The relevant relationship must be bound to the correct Resources and evaluated against authoritative or sufficiently authoritative state.

⸻

18. Quantitative Postconditions

Actions may produce measurable values.

Example:

Action:
transfer ₦100,000

Possible postconditions:

source.balance =
    previous_balance - ₦100,000
destination.balance =
    previous_balance + ₦100,000

Multiple postconditions may therefore be required to establish correctness.

For financial or otherwise consequential state, evaluation must use the enterprise system that is authoritative for the relevant balances or transaction state.

⸻

19. Temporal Postconditions

Some effects must occur within a temporal boundary.

Example:

Action:
send_otp
Postcondition:
otp_delivery.confirmed within 30 seconds

Temporal semantics must be explicit where timing affects correctness.

The relevant timestamps may include:

* Action time;
* execution time;
* event occurrence time;
* effective time;
* observation time;
* receipt time;
* evaluation time.

A timestamp alone does not establish authority.

⸻

20. Composite Postconditions

An Action may have multiple required conditions.

Example:

Action:
issue_card

Postconditions:

card exists
card.status = ACTIVE
card.owner = customer_123
card.type = REPLACEMENT

The Action should not be considered fully successful merely because one condition holds.

The contract must define whether the composite condition is conjunctive, disjunctive, conditional, or otherwise structured.

⸻

21. Conjunctive Postconditions

A composite postcondition may require:

P1 AND P2 AND P3

Example:

card.exists
AND
card.status = ACTIVE
AND
card.owner = customer_123

All required predicates must be satisfied.

If one cannot be established, the composite result cannot be represented as fully satisfied.

⸻

22. Disjunctive Postconditions

Some Actions may permit alternative valid outcomes.

Example:

shipment.status = DELIVERED
OR
shipment.status = PICKUP_AVAILABLE

The Action Contract must explicitly define whether these states satisfy the same expected semantic objective.

Noema must not infer that two different states are equivalent merely because both appear operationally acceptable.

⸻

23. Conditional Postconditions

A postcondition may depend on the actual Action branch.

Example:

if payment.method = CARD:
    card_transaction.status = SETTLED
if payment.method = BANK_TRANSFER:
    transfer.status = CONFIRMED

The applicable postcondition must be determined from admitted execution semantics and actual execution path.

A model must not select a postcondition merely because it appears plausible.

⸻

24. Postcondition Scope

Postconditions may apply to:

* a single Action;
* an Action Instance;
* a Plan step;
* a composite Action;
* an entire Plan;
* a workflow.

The scope must be explicit.

A Plan-level postcondition must not be treated as automatically satisfied because individual Actions completed.

⸻

25. Action-Level Postconditions

Example:

Action:
create_customer
Postcondition:
customer exists

This establishes the immediate semantic effect expected from the Action.

The postcondition must remain associated with the specific Action Instance and Resource involved.

⸻

26. Plan-Level Postconditions

A Plan may have a higher-level postcondition.

Example:

Plan:
renew_card
Final postcondition:
customer has an active replacement card

The Plan-level condition may depend on several Action-level postconditions.

verify
   ↓
issue
   ↓
activate
   ↓
Final Postcondition

The final condition must be evaluated against actual observations, not inferred from the presence of the preceding Actions in the Plan.

⸻

27. Postconditions and Outcomes

Postconditions provide inputs for determining Outcome.

Postconditions
       ↓
Evaluation
       ↓
┌───────────────┬──────────────────┬─────────┐
│ SATISFIED     │ NOT_SATISFIED    │ UNKNOWN │
└───────────────┴──────────────────┴─────────┘
       ↓                 ↓               ↓
   Outcome           Failure or       Reconcile /
   semantics         other defined     Wait /
                     semantics         Intervene

The exact Outcome taxonomy belongs to execution/outcome.md.

Postcondition evaluation does not itself define enterprise Business State.

⸻

28. Postconditions Do Not Define the User’s Intent

Intent:

"Get me a replacement card."

Postcondition:

replacement_card.status = ACTIVE

The postcondition operationalizes the expected semantic effect.

It does not redefine the Intent.

The Intent Object remains the canonical representation of the requested semantic goal.

⸻

29. Postconditions and Planning

Planning may define expected postconditions for Actions where necessary.

Example:

Plan:
issue_card
Expected:
card.status = ISSUED

The Plan expresses what should result from the Action.

Execution and verification later determine whether the condition was actually established.

A planned postcondition is therefore an expectation, not a fact.

⸻

30. Postconditions and Action Contracts

An Action Contract may contain:

action
inputs
preconditions
authorization requirements
idempotency
postconditions
verification requirements

Conceptually:

ActionContract {
    action
    inputs
    preconditions
    postconditions
    verification
}

The exact schema remains defined in contracts/action-contract.md.

Postconditions must be explicit enough for deterministic evaluation.

⸻

31. Postconditions and Idempotency

Postconditions are important for determining whether a retry is necessary.

Example:

Action:
activate_card

After a timeout:

Execution:
UNKNOWN

Noema checks the authoritative Resource state:

card.status = ACTIVE

If the postcondition is satisfied, another execution attempt is unnecessary.

The canonical relationship is:

Idempotency
+
State Reconciliation
+
Postcondition Verification

This prevents uncertain execution from becoming an unsafe duplicate Action.

⸻

32. Postconditions and State Reconciliation

When execution state is uncertain:

Execution:
UNKNOWN

Noema may reconcile the relevant enterprise state.

UNKNOWN
   ↓
Observe authoritative systems
   ↓
Hard Schema Validation / Admission
   ↓
State Reconciliation
   ↓
Reconciled State / Fact Status
   ↓
Evaluate Postcondition
   ↓
SATISFIED / NOT SATISFIED / UNKNOWN

State Reconciliation is therefore a first-class part of postcondition verification.

It is not merely an integration implementation detail.

⸻

33. Postconditions and Compensation

If required postconditions cannot be satisfied:

Action
 ↓
Partial Effect
 ↓
Postcondition Evaluation
 ↓
Required condition not established

the execution system may need compensation.

Example:

create_order       → SUCCESS
reserve_inventory  → SUCCESS
charge_payment     → FAILURE

The system may evaluate compensation Actions according to explicit compensation semantics.

Compensation must not be inferred as the inverse of the original Action.

See execution/compensation.md.

⸻

34. Postcondition Failure

A postcondition failure means:

The Action did not establish the required semantic effect.

It does not necessarily mean the Action had no effect.

Example:

Expected:
balance = ₦100,000
Observed:
balance = ₦80,000

The Action may have partially changed the state.

The execution record must preserve the observations and evidence used to establish the result.

The enterprise system remains authoritative for the underlying Business State.

⸻

35. Partial Satisfaction

For composite postconditions:

P1 = TRUE
P2 = TRUE
P3 = FALSE

the result is not full satisfaction.

Possible evaluation state:

PARTIALLY_SATISFIED

may be represented where supported by the Outcome or postcondition model.

Otherwise:

NOT_SATISFIED

must preserve which predicates were satisfied, which were not, and which remained unknown.

Partial satisfaction must not be silently converted into full success.

⸻

36. Postcondition Drift

A postcondition may be satisfied immediately and later become false because another system changes the Resource.

Example:

Action:
activate_card
Postcondition:
card.status = ACTIVE

At T1:

ACTIVE

At T2:

BLOCKED

The original Action may still have succeeded.

Therefore postcondition evaluation must have a defined observation time and semantic observation window.

Later Resource changes do not retroactively rewrite the historical result of the Action.

⸻

37. Temporal Truth

The canonical interpretation is:

Postcondition P
was satisfied
at observation time T

rather than:

P is permanently true

This distinction matters for mutable Resources.

A postcondition evaluation establishes a temporally scoped claim based on the evidence available at that time.

⸻

38. Postcondition Observation Window

Some postconditions require a defined observation window.

Example:

Action:
send_email
Postcondition:
delivery.confirmed within 5 minutes

The system should not evaluate the condition indefinitely.

The Action Contract or relevant execution semantics should define:

* start of the observation window;
* end of the observation window;
* accepted evidence;
* polling or event strategy;
* treatment of timeout;
* transition to UNKNOWN where the condition cannot be established.

⸻

39. Eventual Postconditions

Some effects are asynchronous.

Example:

Action:
provision_server

The API may return:

provisioning_started

while the actual postcondition is:

server.status = READY

The system may therefore need:

* polling;
* event subscription;
* callback;
* provider confirmation;
* State Reconciliation.

An accepted request is not necessarily a satisfied postcondition.

⸻

40. Synchronous vs Asynchronous Postconditions

Synchronous

Action
 ↓
Execution
 ↓
Response / Observation
 ↓
Postcondition Evaluation

Asynchronous

Action
 ↓
Accepted
 ↓
Wait
 ↓
External state changes
 ↓
Event / Observation
 ↓
State Reconciliation where required
 ↓
Postcondition Evaluation

The Execution Model must distinguish these cases.

⸻

41. Postcondition Evidence Must Be Authoritative or Sufficiently Authoritative

A postcondition should ideally be evaluated against the authoritative source for the relevant claim.

For example:

Payment Provider

rather than:

Noema local cache

when the provider owns the payment state.

However, authority is claim-specific.

An enterprise system may be authoritative for one claim and merely evidentiary for another.

Postcondition evaluation must therefore preserve:

claim
source
authority
scope
freshness
observation

⸻

42. Cached State

Cached state may be stale.

Therefore:

cache:
status = ACTIVE

does not necessarily establish:

authoritative state:
status = ACTIVE

unless the cache has an explicit authority and freshness guarantee sufficient for the evaluation.

Recency alone does not create authority.

⸻

43. Fact Status

Postcondition evaluation must remain distinct from Fact Status.

Fact Status describes the status of a particular claim or fact:

VERIFIED
UNVERIFIED
STALE
CONFLICTED
UNKNOWN

These values do not replace postcondition evaluation.

For example:

Fact Status:
VERIFIED
Postcondition:
NOT_SATISFIED

can be valid if the verified state establishes that the expected condition is false.

Likewise:

Fact Status:
UNKNOWN

may cause the postcondition evaluation to remain:

UNKNOWN

Fact Status is not Evidence, Execution Status, Outcome, or Postcondition Result.

⸻

44. Postcondition Evaluation Must Be Deterministic

Given:

same postcondition
+
same relevant evidence
+
same reconciled state
+
same evaluation rules
+
same evaluation context

Noema should produce the same result.

Conceptually:

P(state, evidence, rules) → SATISFIED / NOT_SATISFIED / UNKNOWN

The evaluation must not depend on model improvisation.

⸻

45. LLMs and Postconditions

An LLM may assist with:

* extracting structured information from unstructured evidence;
* mapping provider terminology to canonical terminology;
* identifying candidate evidence;
* organizing evidence for review.

However, model interpretation must not independently establish a consequential postcondition where deterministic evaluation is required.

Preferred:

LLM
 ↓
Candidate Evidence / Mapping
 ↓
Hard Schema Validation / Admission
 ↓
Evidence / Reconciliation
 ↓
Deterministic Postcondition Evaluator

Model confidence is not Fact Status and is not sufficient authority for a consequential postcondition.

⸻

46. Hard Schema Validation and Admission

External responses, provider messages, events, model-generated mappings, and other inputs are not canonical merely because they contain fields resembling the expected postcondition.

Before such information can participate as canonical structured input to evaluation, it must pass the relevant schema validation and admission boundary.

External / Model Input
        ↓
Hard Schema Validation
        ↓
Semantic / Admission Checks
        ↓
Evidence / Observation
        ↓
Reconciliation
        ↓
Postcondition Evaluation

Persistence of an unvalidated response does not make it authoritative.

The model cannot bypass this boundary.

⸻

47. Postcondition Normalization

Different systems may express equivalent state differently.

Example:

"active"
"ACTIVE"
"enabled"

Noema may normalize these representations where the canonical ontology explicitly defines them as equivalent.

The equivalence must be deterministic and canonical.

Noema must not infer semantic equivalence merely because two values appear similar.

⸻

48. Postcondition Contradictions

Evidence may conflict.

Example:

Provider A:
ACTIVE
Provider B:
SUSPENDED

Noema must not arbitrarily select one.

The relevant claim may become:

Fact Status = CONFLICTED

and the postcondition may consequently remain:

UNKNOWN

until the conflict is resolved or an authoritative source establishes the required state.

Where the conflict cannot be safely resolved, Trust or execution control may require escalation.

⸻

49. Postcondition Staleness

Evidence may be too old to establish a current postcondition.

Example:

Last known state:
ACTIVE at 10:00
Current evaluation:
12:00

If the Resource can change between those times, the evidence may be insufficient.

The result may therefore be:

UNKNOWN

rather than:

SATISFIED

Freshness requirements must be claim-specific and Action-specific.

⸻

50. Postcondition and Resource Ownership

The system must know which Resource the postcondition refers to.

Example:

balance = ₦100,000

is insufficient without identifying:

account_123.balance

Canonical postconditions should bind to specific Resource identities or explicitly defined Resource scopes.

The Resource identity used during postcondition evaluation must be traceable to the resolved Action Instance.

⸻

51. Postcondition and Resolved Identity

For consequential Actions, postcondition evaluation must preserve the identity context of the Action.

Relevant identity may include:

* Intent version;
* actor;
* principal;
* delegated identity;
* Action identity;
* Action Instance;
* target Resource;
* scope;
* resolution identity;
* execution identity.

This prevents an observation about one Resource or execution context from being incorrectly attributed to another.

⸻

52. Postcondition and Concurrency

Concurrent Actions may affect the same Resource.

Example:

Action A:
set status ACTIVE
Action B:
set status BLOCKED

If both execute concurrently, postcondition evaluation must account for ordering, versions, causality, and Resource state.

A postcondition should not be interpreted without its relevant execution and observation context.

Where supported, enterprise atomic operations, resource versions, conditional writes, transactions, or equivalent concurrency controls should establish the relevant semantics.

⸻

53. Postcondition and Causality

Noema should distinguish:

Action caused state S

from:

state S happened sometime after Action

For consequential workflows, establishing causality may require:

* execution ID;
* Action Instance ID;
* event ID;
* transaction ID;
* provider reference;
* resource version;
* timestamps;
* correlation ID.

Temporal adjacency alone does not establish causality.

⸻

54. Postcondition and Auditability

A postcondition evaluation should preserve:

* postcondition definition;
* postcondition version;
* Intent version;
* Action and Action Instance identity;
* execution identity;
* target Resource;
* observation time;
* observed value;
* evidence source;
* evidence identity;
* Fact Status where applicable;
* reconciliation identity where applicable;
* evaluation result;
* evaluation rules/version;
* relevant contract, policy, graph, capability, integration, and system versions.

This allows Noema to explain the deterministic basis for an Outcome without exposing private model chain-of-thought.

⸻

55. Postcondition Versioning

Postcondition semantics may evolve.

Therefore evaluations must be associated with the semantic version of the Action Contract, Action definition, or evaluation rule that defined the condition.

Example:

postcondition_version = 2

Historical evaluations must remain interpretable under the semantics that existed when they were evaluated.

A later postcondition definition must not silently rewrite a historical Outcome.

Relevant versions may include:

Intent Version
Action Version
Action Contract Version
Policy Version
Trust Version
EAG / Capability Version
Integration Version
System / Provider Version
Postcondition / Evaluation Rule Version

⸻

56. Intent Version Lineage

Consequential postcondition evaluations must retain the exact immutable Intent Object version that produced the Action.

Once an Intent is admitted to Trust, it is immutable.

If clarification or another material change alters the semantic request:

Intent v1
   ↓
supersedes
Intent v2

The new version must be evaluated independently.

A postcondition for an Action derived from Intent v1 must not be silently reassigned to Intent v2.

⸻

57. Postcondition Failure Handling

When a required postcondition is not satisfied:

Action
 ↓
Postcondition FALSE

the system may:

* retry;
* reconcile;
* replan;
* compensate;
* request human intervention;
* terminate.

The correct path depends on:

* Action Contract;
* execution state;
* idempotency;
* current enterprise state;
* failure semantics;
* applicable policy;
* Trust requirements;
* compensation rules.

No universal recovery path should be inferred.

⸻

58. Postcondition Evaluation Does Not Automatically Trigger Retry

A failed or unknown postcondition does not mean:

retry immediately

For example:

Action:
create_payment
Postcondition:
payment.status = SETTLED

If the current state is:

PROCESSING

the correct response may be:

WAIT
RECONCILE
VERIFY

rather than issuing another payment.

Retry must preserve Action identity and idempotency semantics where the retry represents the same semantic Action.

A materially different Action requires a new Action identity and corresponding execution/idempotency lineage.

⸻

59. Postconditions and Human Confirmation

Some domains may permit human confirmation as evidence.

Example:

Action:
physical_delivery
Postcondition:
recipient confirms receipt

Human evidence must still be evaluated according to the Evidence and Trust models.

Human confirmation does not automatically override stronger contradictory evidence.

The identity and authority of the confirming party must be established where consequential.

Human confirmation is evidence; it is not inherently authoritative merely because a human supplied it.

⸻

60. Postcondition Hierarchy

Complex workflows can contain nested postconditions.

Action
   ↓
Action Postcondition
   ↓
Plan Postcondition
   ↓
Intent Outcome

Example:

activate_card
    ↓
card.status = ACTIVE
    ↓
replacement_card.available = TRUE
    ↓
customer's card renewal objective established

Each level has distinct semantics.

A higher-level postcondition must not be inferred solely from the existence of lower-level Actions.

⸻

61. Postconditions and Trust

Postconditions do not replace Trust.

Trust determines whether a resolved Action path may proceed under applicable authority, policy, evidence, and constraints.

Postconditions determine whether the expected semantic effect was subsequently established.

Therefore:

Trust EXECUTE
        ≠
Execution Success
        ≠
Postcondition SATISFIED
        ≠
Enterprise Business State permanently established

EXECUTE means the Action path satisfied the applicable Trust conditions at the decision point.

It does not guarantee that the Action will succeed.

⸻

62. Postconditions and the Enterprise System of Record

When a postcondition concerns enterprise Business State, the enterprise System of Record remains authoritative for that state.

Noema may:

* observe the state;
* reconcile observations;
* evaluate postconditions;
* retain execution-domain evidence;
* record the resulting Outcome.

Noema must not create a shadow canonical Business State merely to satisfy a postcondition.

Enterprise System of Record
          ↓
      Observation
          ↓
 State Reconciliation
          ↓
 Reconciled Claim
          ↓
 Postcondition Evaluation

Noema’s local record of a satisfied postcondition is an execution-domain record of what was established, not ownership of the underlying enterprise fact.

⸻

63. Read-Only Postconditions

Postconditions are not limited to write operations.

A read-only Action can have consequential postconditions.

Example:

Action:
retrieve_account_security_state

Postcondition:

account.security_state = VERIFIED

The Action may not mutate Business State, but establishing or exposing protected information can still be consequential.

Such evaluation may therefore require Trust, authorization, data-boundary enforcement, and auditability.

⸻

64. Planner and Postcondition Boundaries

The Planner may propose expected postconditions and select strategies that can establish them.

It cannot:

* invent Actions;
* invent capabilities;
* invent Resources;
* grant authority;
* modify Action Contract semantics;
* bypass Trust;
* declare an expected postcondition satisfied;
* treat model inference as authoritative evidence.

Planning is bounded by:

Enterprise Action Graph
Capability Registry
Action Registry / Model
Action Contracts
Policies
Enterprise state and constraints

The Planner defines a strategy.

Execution and verification establish whether the strategy produced the expected effect.

⸻

65. Security Boundary

User input, model output, retrieved enterprise text, tool responses, provider responses, and external messages are untrusted until admitted through the relevant deterministic boundaries.

The model must not have:

* enterprise credentials;
* unrestricted database access;
* unrestricted HTTP access;
* unrestricted provider access;
* authority to declare postconditions satisfied.

No free-form model output may directly establish a consequential postcondition or trigger execution.

The canonical path is:

Untrusted Input
      ↓
Hard Schema Validation / Admission
      ↓
Bounded Evidence / Observation
      ↓
State Reconciliation
      ↓
Deterministic Evaluation

⸻

66. Replay and Historical Evaluation

Replay of an execution, event, observation, or postcondition evaluation is non-executing by default.

Replay must not:

* recreate side effects;
* create a new business occurrence;
* silently alter historical Outcome;
* replace historical evidence with current evidence.

A historical postcondition evaluation remains associated with its original:

* Intent version;
* Action;
* execution;
* observation;
* evidence;
* reconciliation;
* evaluation rules;
* semantic versions.

A modern reevaluation is a distinct operation with its own provenance.

⸻

67. Operational Memory

Postcondition evaluations may contribute to Operational Memory.

Operational Memory may retain:

* historical evaluations;
* failed conditions;
* verification patterns;
* reconciliation history;
* recovery history;
* execution context.

Operational Memory is not:

* enterprise Business State;
* an authoritative source for current Resource state;
* a replacement for Evidence;
* a replacement for State Reconciliation;
* generic model memory.

Historical postcondition satisfaction must not be treated as current truth without an applicable freshness and authority basis.

⸻

68. Canonical Verification Flow

The canonical postcondition flow is:

Admitted Intent
      ↓
Resolved Action / Resource
      ↓
Deterministic Trust
      ↓
Action Contract
      ↓
Execution
      ↓
Observation
      ↓
Hard Schema Validation / Admission
      ↓
State Reconciliation
      ↓
Evidence / Fact Status
      ↓
Postcondition Evaluation
      ↓
SATISFIED / NOT SATISFIED / UNKNOWN
      ↓
Outcome

When the result is UNKNOWN:

UNKNOWN
   ↓
State Reconciliation
   ↓
Re-evaluate
   ↓
SATISFIED
   or
NOT SATISFIED
   or
UNKNOWN

Only after sufficient evidence establishes the relevant condition can the semantic result be classified accordingly.

⸻

69. Causal Audit Chain

For consequential Actions, the postcondition record should participate in the causal chain:

Source of Intent
      ↓
Intent Version
      ↓
Intent Resolution
      ↓
Resolved Actor / Action / Resource
      ↓
State Reconciliation / Context
      ↓
Trust Decision
      ↓
Action Contract
      ↓
Execution
      ↓
Observation
      ↓
Evidence
      ↓
State Reconciliation
      ↓
Postcondition Evaluation
      ↓
Outcome

The chain must preserve the relationship between the requested semantic goal, the attempted Action, the evidence observed afterward, and the conclusion reached by the deterministic evaluator.

⸻

70. Postcondition Invariants

Invariant 1

Execution completion does not imply postcondition satisfaction.

Invariant 2

A postcondition must be explicitly defined and evaluable.

Invariant 3

A postcondition must be evaluated against evidence, observation, or reconciled state sufficient for the specific condition.

Invariant 4

Expected state must not be represented as observed state.

Invariant 5

Missing evidence must not be interpreted as success.

Invariant 6

UNKNOWN must remain distinct from NOT_SATISFIED.

Invariant 7

Postconditions must reference the relevant Resource or Resource scope explicitly.

Invariant 8

Composite postconditions must define whether conditions are conjunctive, disjunctive, conditional, or otherwise structured.

Invariant 9

Temporal postconditions must define their observation window where timing matters.

Invariant 10

Postcondition evaluation must use authoritative or sufficiently authoritative evidence for the relevant claim.

Invariant 11

Fact Status must remain distinct from Evidence, Execution Status, Postcondition Result, and Outcome.

Invariant 12

Postcondition evaluation must be deterministic given the same relevant inputs and evaluation rules.

Invariant 13

Postcondition satisfaction at one point in time does not imply permanent satisfaction.

Invariant 14

Postcondition failure does not automatically imply retry.

Invariant 15

An UNKNOWN postcondition must not trigger an unprotected consequential retry.

Invariant 16

State Reconciliation must be used where current enterprise state cannot otherwise be established with sufficient authority and freshness.

Invariant 17

Postcondition evaluations must be auditable.

Invariant 18

Plan-level postconditions must not be inferred solely from planned Actions.

Invariant 19

Postconditions must not redefine or silently alter the underlying Intent.

Invariant 20

Consequential postcondition evaluations must preserve the exact immutable Intent version associated with the Action.

Invariant 21

Resolved actor, Action, Resource, target, scope, and resolution identity must remain traceable through postcondition evaluation where consequential.

Invariant 22

Trust EXECUTE does not establish postcondition satisfaction or execution success.

Invariant 23

A model must not independently establish a consequential postcondition when deterministic evaluation is required.

Invariant 24

Unvalidated external, provider, event, or model-generated information must not become canonical evaluation input merely through persistence.

Invariant 25

A cache or historical observation must not be treated as current authoritative state without applicable authority and freshness guarantees.

Invariant 26

Conflicting evidence must not be resolved by arbitrary source selection.

Invariant 27

Postcondition evaluation must account for Resource identity and relevant concurrency semantics.

Invariant 28

Temporal correlation alone must not be treated as causal proof.

Invariant 29

A postcondition result must not rewrite the authoritative enterprise Business State.

Invariant 30

Enterprise Business State remains authoritative to the relevant enterprise System of Record.

Invariant 31

A retry representing the same semantic Action must preserve the relevant Action and idempotency identity.

Invariant 32

A materially changed Action must not reuse the semantic identity of the original Action merely because its purpose is similar.

Invariant 33

Compensation is a distinct governed Action and must have its own postcondition semantics.

Invariant 34

Replay must not recreate business side effects or silently alter historical postcondition evaluations.

Invariant 35

Operational Memory may preserve postcondition history but must not become the authority for current enterprise state.

Invariant 36

Read-only Actions may require postcondition verification and Trust when their effects or information exposure are consequential.

Invariant 37

The Planner may propose expected postconditions but cannot declare them satisfied or invent the capabilities required to establish them.

Invariant 38

Postcondition semantics must be versioned where their meaning can change.

Invariant 39

Historical postcondition evaluations must remain interpretable under the semantic versions used when they were established.

Invariant 40

Noema must never convert uncertainty about a postcondition into a claim of success merely to complete an execution path.

⸻

71. Canonical Mental Model

                         ACTION
                           │
                           ▼
                       EXECUTION
                           │
                           ▼
                       OBSERVATION
                           │
                           ▼
              HARD SCHEMA VALIDATION / ADMISSION
                           │
                           ▼
                  STATE RECONCILIATION
                           │
                           ▼
                  EVIDENCE / FACT STATUS
                           │
                           ▼
                POSTCONDITION EVALUATION
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
         SATISFIED    NOT SATISFIED   UNKNOWN
             │             │             │
             ▼             ▼             ▼
          OUTCOME       RECOVERY      RECONCILE /
                            │          WAIT /
                            │          INTERVENE
                            │
                            ▼
                         OUTCOME

At the workflow level:

Source of Intent
       ↓
Intent Version
       ↓
Resolution
       ↓
Trust
       ↓
Plan
       ↓
Action
       ↓
Execution
       ↓
Observation
       ↓
Reconciliation
       ↓
Postconditions
       ↓
Evidence
       ↓
Evaluation
       ↓
Outcome

The critical distinction is:

Expected Effect
      ≠
Observed State
      ≠
Established Postcondition
      ≠
Outcome
      ≠
Enterprise Business State

⸻

72. Final Definition

A postcondition is an explicit, versioned, evaluable statement of the state or effect that must be established after an Action or execution step for its expected semantic effect to be recognized.

Postconditions are evaluated against sufficient evidence, observations, and, where necessary, reconciled enterprise state. They may resolve to SATISFIED, NOT_SATISFIED, or UNKNOWN, with the resulting interpretation governed by the applicable Action, Execution, Outcome, Trust, and recovery semantics.

The core invariant is:

Noema never treats “the executor said it completed” as equivalent to “the intended effect occurred.”

An Action becomes semantically successful only when the applicable postconditions are established by sufficient, appropriately authoritative evidence. Uncertainty remains uncertainty until deterministic verification or State Reconciliation establishes otherwise.