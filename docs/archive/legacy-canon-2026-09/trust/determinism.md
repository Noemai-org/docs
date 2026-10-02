Determinism

Status: Foundational
Version: 0.2
Domain: Trust
Canonical Path: trust/determinism.md

⸻

1. Definition

Determinism is Noema’s requirement that semantic commitments and Trust decisions at the execution boundary be governed by explicit, reproducible rules and authoritative state rather than uncontrolled probabilistic inference.

Determinism does not mean that every component of Noema must be deterministic.

It means:

Probabilistic interpretation may enter the system; uncontrolled probability must not be the final authority for consequential commitment or execution.

The Model may generate candidate meanings.

Noema must establish which meaning is sufficiently grounded.

Trust must determine whether the resulting Intent may proceed.

⸻

2. The Core Distinction

Noema explicitly separates probabilistic interpretation from deterministic commitment:

Probabilistic
    ↓
Model Interpretation
    ↓
Candidate Intent
    ↓
Resolution
    ↓
Deterministic
    ↓
Trust Decision
    ↓
Execution Contract
    ↓
Execution

The Model may estimate.

Resolution establishes.

Trust decides.

The executor executes the established contract.

⸻

3. Why Determinism Exists

Large language models are probabilistic systems.

Given the same expression, a Model may produce different:

* interpretations
* entities
* Resources
* Actions
* parameters
* candidate relationships
* contextual inferences

This is acceptable during interpretation.

It becomes dangerous when those variations can directly produce different consequential side effects.

Example:

Actor:
"Cancel my card."
Cards:
Card#123
Card#456

A Model may select Card#123 in one inference and Card#456 in another.

Noema must not allow sampling variance to determine which card is cancelled.

The ambiguity must instead become an explicit Trust condition.

⸻

4. Determinism Is a Trust Property

Trust exists at the point where Noema determines:

“This Intent is sufficiently established and permitted to cross the execution boundary.”

Therefore Trust should derive its decision from:

* resolved Intent
* Actor
* Context
* Evidence
* authoritative enterprise state
* Identity
* Authorization
* Policy
* Preconditions
* Capability
* Risk
* temporal constraints
* organizational boundaries
* Data Boundaries
* applicable freshness requirements

rather than:

Model confidence alone

Trust is therefore a deterministic decision boundary, not a probability threshold.

⸻

5. Determinism Does Not Mean “No AI”

Noema is not a rule engine that happens to contain an LLM.

The Model remains valuable for:

* language understanding
* semantic interpretation
* entity extraction
* candidate generation
* candidate Intent construction
* contextual inference
* Intent composition
* clarification generation

The distinction is:

Model:
"What could this mean?"
Resolution:
"What interpretation can be established from the available evidence?"
Trust:
"May this established Intent proceed?"

Determinism constrains commitment, not interpretation.

⸻

6. The Deterministic Boundary

Noema should maintain a clearly defined boundary between probabilistic interpretation and deterministic commitment.

Conceptually:

                 ACTOR EXPRESSION
                       │
                       ▼
                ┌─────────────┐
                │    MODEL    │
                │ probabilistic│
                └──────┬──────┘
                       │
                Candidate Intent
                       │
                       ▼
              ┌──────────────────┐
              │      NOEMA       │
              │   Resolution     │
              │   Trust          │
              └────────┬─────────┘
                       │
                Canonical Intent
                       │
                       ▼
                 Trust Decision
                       │
             ┌─────────┴─────────┐
             │                   │
         Non-executable       EXECUTE
             │                   │
             ▼                   ▼
   CLARIFY / ESCALATE /      Action
        REJECT                 │
                               ▼
                           Execution

The implementation may evolve.

The boundary must remain explicit.

⸻

7. Deterministic Does Not Mean Predictable From the Actor’s Sentence Alone

A decision may depend on changing authoritative state.

Example:

Actor:

"Cancel my active subscription."

At 10:00:

Subscription#123 = ACTIVE

At 12:00:

Subscription#123 = CANCELLED

The resulting decision may legitimately differ because the authoritative state changed.

Determinism means:

Given the same defined inputs, state, Policy, and rule versions, the decision procedure produces the same result.

It does not mean:

The same natural-language expression must always produce the same decision regardless of changing state.

⸻

8. Determinism Is Input-Relative

A deterministic decision is deterministic relative to its defined inputs.

Conceptually:

Decision =
    f(
        Intent,
        Actor,
        Context,
        Evidence,
        Authoritative State,
        Authorization,
        Policy,
        Capability,
        Preconditions,
        Risk,
        Temporal State
    )

If a material input changes, the decision may legitimately change.

The relevant inputs must therefore be identifiable for consequential decisions.

⸻

9. Reproducibility

A deterministic Trust decision should be reproducible from its decision inputs where the underlying state remains available.

For consequential decisions, Noema should preserve sufficient information such as:

* Intent version
* Actor
* Target Resources
* Context
* Evidence
* Evidence provenance
* Authorization decision
* Authorization rule version
* Policy version
* Capability version
* relevant state versions
* freshness information
* Trust decision
* decision timestamp

This enables Noema to reconstruct why a decision occurred.

⸻

10. Determinism vs Model Confidence

Confidence is not determinism.

Example:

Model:
Interpretation A = 99%
Interpretation B = 1%

This remains probabilistic.

Deterministic resolution requires evidence capable of establishing that:

B is not a viable interpretation

For example:

Candidate A:
Card#123
Candidate B:
Card#456
Authoritative state:
Card#456 = CANCELLED
Intent:
"Renew my active card."

If the applicable semantics require an active card, Card#456 may be deterministically eliminated.

The distinction is:

Probability:
"What is likely?"
Deterministic resolution:
"What can be established?"
Trust:
"May the established Intent proceed?"

⸻

11. Confidence Must Not Become Permission

A dangerous architecture is:

if model.confidence > 0.9:
    execute()

Noema must not use this pattern as the basis for consequential execution.

A high confidence score does not independently establish:

* correctness
* identity
* Resource resolution
* authorization
* Policy compliance
* sufficient evidence
* required preconditions
* execution safety

Model confidence may be recorded as supporting metadata.

It is not a Trust decision.

⸻

12. Determinism and Ambiguity

Material ambiguity is a failure to establish a single sufficiently grounded interpretation.

Example:

Card#123
Card#456

Both satisfy:

"Renew my card."

If no authoritative evidence distinguishes them:

AMBIGUOUS

The correct transition is:

AMBIGUOUS
    ↓
CLARIFY

not:

AMBIGUOUS
    ↓
choose highest probability
    ↓
EXECUTE

Material ambiguity must therefore block execution.

⸻

13. Determinism and Resolution

Resolution is the process through which Noema converts:

Candidate meaning

into:

Canonical meaning

when sufficient evidence exists.

For example:

"my savings account"
        ↓
Resolution
        ↓
Account#123

Once established, the canonical identifier should be carried forward.

Resolution is therefore one of the principal mechanisms through which Noema establishes deterministic semantic state.

⸻

14. Determinism and Partial Resolution

An Intent may be deterministic in some dimensions while unresolved in others.

Example:

Objective:
RenewCard                    ✓
Actor:
User#123                     ✓
Resource:
Card#123 | Card#456          ✗
Outcome:
Card becomes active          ✓

Noema should preserve the resolved components.

The unresolved Resource remains explicitly ambiguous.

Therefore:

Intent
├── Objective = RenewCard
├── Actor = User#123
├── Resource = AMBIGUOUS
└── Outcome = Card becomes active

Determinism does not require discarding established information merely because another field remains unresolved.

⸻

15. Determinism and Authorization

Authorization must be deterministic.

Example:

Actor:
User#123
Intent:
DeleteProject(Project#456)
Relationship:
User#123 → admin_of → Project#456
Rule:
Project administrators may delete projects.

Result:

Authorization:
ALLOWED

The Model should not determine whether the Actor “seems authorized.”

Authorization must be grounded in authoritative rules, relationships, claims, or authorization services.

⸻

16. Determinism and Authorization Ambiguity

Authorization must not resolve semantic ambiguity.

Example:

Intent:
DeleteProject(ProjectA | ProjectB)
Actor:
Authorized for ProjectA
Not authorized for ProjectB

Noema must not conclude:

ProjectA

merely because it is authorized.

The correct state remains:

Intent:
AMBIGUOUS
Authorization:
NOT YET DETERMINABLE

After clarification:

DeleteProject(ProjectA)
        ↓
Authorization
        ↓
ALLOWED

Authorization evaluates the established Intent.

It must not substitute an executable Intent for the Actor’s actual Intent.

⸻

17. Determinism and Policy

Policy evaluation should be governed by explicit rules and authoritative inputs.

Example:

Transaction:
₦20,000,000
Policy:
Transactions > ₦10,000,000 require secondary approval.

Result:

SECONDARY_APPROVAL_REQUIRED

The Model may help identify:

* the transaction
* the Action
* relevant parameters
* candidate Policy categories

It should not independently determine the Policy outcome through free-form judgment.

⸻

18. Determinism and Capability

Capability determination should rely on explicit Capability definitions and applicable conditions.

Example:

Capability:
RefundPayment
Supported:
PaymentProvider = X
Currency = USD

Given:

PaymentProvider = X
Currency = NGN

the Capability may be:

UNSUPPORTED

Model confidence must not turn an unsupported operation into a supported one.

Capability is a system or execution property.

Authorization is an Actor authority property.

Trust evaluates both where applicable.

⸻

19. Determinism and Preconditions

Preconditions must be established before execution.

Example:

Action:
RetrieveStatement
Precondition:
Account.status = ACTIVE

If authoritative state establishes:

Account.status = ACTIVE

the precondition is satisfied.

If the required state cannot be established, Noema must not infer that the precondition is satisfied merely because it is probable.

The resulting Trust state depends on Policy and the nature of the missing condition:

CLARIFY
ESCALATE
REJECT

as applicable.

⸻

20. Determinism and Evidence

Deterministic decisions require evidence appropriate to the decision being made.

Evidence should be evaluated according to properties such as:

* source
* authority
* freshness
* relevance
* specificity
* integrity
* effective time
* version

For example:

Enterprise Identity System
        >
Customer assertion
        >
Model inference

This does not mean lower-authority evidence is useless.

It means evidence strength must be evaluated according to the Action and applicable Policy.

⸻

21. Determinism and Canonical Enterprise State

Noema should prefer authoritative enterprise systems for facts that belong to those systems.

Examples:

Account balance:
Ledger
Resource ownership:
Business system
Authorization:
Authorization service
Payment status:
Payment service

Noema should consume these facts as evidence rather than inventing competing business truth.

Conceptually:

Business System
      ↓
Authoritative State
      ↓
Evidence
      ↓
Noema Trust Decision

This preserves the distinction between:

Noema:
Intent + Trust + Execution Decision
Business System:
Business State

⸻

22. Determinism and Execution Contracts

The execution boundary should receive a structured, validated representation.

Conceptually:

Canonical Intent
      ↓
Trust Decision
      ↓
Execution Contract
      ↓
Consumer

The Consumer should not need to reinterpret the original natural language.

Example:

{
    actor: User#123,
    action: DeleteProject,
    resource: Project#456,
    authorization: ALLOWED,
    policy_status: SATISFIED,
    constraints: [...],
    provenance: [...]
}

The execution contract represents the semantic commitment already established by Noema.

⸻

23. Execution Must Not Reinterpret Intent

Once Noema has established:

DeleteProject(Project#456)

the executor should not receive:

"Delete the project."

and independently determine which project that means.

It should receive the canonical target:

Project#456

This prevents probabilistic semantic interpretation from re-entering the execution boundary.

⸻

24. Determinism and Consumer-Side Execution

The execution consumer should receive sufficient information to perform the Action without semantic guessing.

Conceptually:

ExecutionContract {
    actor
    action
    resources
    parameters
    constraints
    authorization
    policy_status
    capability
    provenance
}

The consumer should:

* validate the contract
* enforce the contract
* execute the Action
* report the result

The consumer should not:

* reinterpret natural language
* choose among ambiguous Resources
* invent missing parameters
* override Trust
* silently substitute a different Intent

⸻

25. Determinism and Enforcement

A deterministic Trust decision is insufficient if downstream systems can ignore it.

Therefore:

Trust decisions must be enforceable at the execution boundary, not merely advisory.

If Noema establishes:

REJECT

the execution path must not nevertheless perform the Action.

Likewise, an execution consumer should not silently replace:

DeleteProject(Project#456)

with another target.

⸻

26. Defense in Depth

Noema should not assume that a single authorization or enforcement layer is sufficient.

A mature architecture may contain:

Noema Trust
      +
Business-System Authorization
      +
Infrastructure Authorization

These layers may protect different boundaries.

Noema Trust establishes whether the Action is permitted to cross Noema’s execution boundary.

The business system may independently enforce domain authorization.

Infrastructure systems may enforce their own access controls.

These controls should reinforce rather than replace one another.

⸻

27. Determinism and Idempotency

Determinism and idempotency are distinct properties.

Determinism:

Same relevant inputs and state
        ↓
Same decision

Idempotency:

Repeated execution of the same operation
        ↓
No unintended additional effect

A Trust Engine may be deterministic while an Action is not idempotent.

Both properties may be required, but they must not be conflated.

⸻

28. Determinism and Concurrency

A deterministic Trust decision does not imply deterministic concurrent execution.

Example:

Trust:
EXECUTE
Concurrent event:
Resource state changes

Noema therefore needs explicit handling of conditions such as:

* stale state
* race conditions
* version conflicts
* optimistic concurrency
* transactional boundaries
* revalidation

where relevant.

A deterministic decision based on stale state is not equivalent to a current decision based on current state.

⸻

29. Determinism and Temporal State

Time is an input to deterministic evaluation when Policy or Action semantics depend on it.

Example:

Deployment allowed:
09:00–17:00 UTC

The decision must use an authoritative time reference.

The system must not rely on a Model interpreting:

"It is probably still within working hours."

Temporal constraints should be represented explicitly where they affect Trust.

⸻

30. Determinism and Temporal Validity

Trust and authorization decisions may become stale.

Example:

10:00
Account = ACTIVE
10:05
Account = CLOSED
10:10
Execution

A decision made at 10:00 must not automatically authorize execution at 10:10 if the Action requires current account state.

Noema may therefore require:

* freshness constraints
* version checks
* state revalidation
* authorization revalidation

before execution.

⸻

31. Determinism and Revalidation

When execution is delayed or relevant state changes, Trust may need to be evaluated again.

Conceptually:

Initial Trust
      ↓
Planning
      ↓
Delay / State Change
      ↓
Revalidation
      ↓
Execution

Revalidation should use:

* current applicable Policy
* current authoritative state
* current authorization
* required freshness constraints
* current Preconditions

A prior Trust decision should not be treated as permanently valid when its governing inputs have materially changed.

⸻

32. Determinism and Enterprise Events

Enterprise events may invalidate previously established conditions.

Example:

Account.status = ACTIVE
        ↓
account.closed

Noema should not blindly continue using stale Context.

Conceptually:

Enterprise Event
      ↓
Context Update
      ↓
Trust Re-evaluation

The exact mechanism may be event-driven, polling-based, version-based, or transactional.

The semantic requirement is that materially changed state can invalidate stale Trust assumptions.

⸻

33. Determinism and Conflicting Evidence

Evidence may conflict.

Example:

Identity System:
Customer → Account A
Profile Cache:
Customer → Account B

Noema must not resolve the conflict by:

* source counting
* Model preference
* whichever value was retrieved first

Instead it should determine:

* which source is authoritative
* whether the sources have different effective times
* whether one source is stale
* whether reconciliation is required

If authority cannot be established:

CLARIFY

or:

ESCALATE

according to Policy.

⸻

34. Determinism and Decision Snapshots

For consequential decisions, Noema should conceptually be able to construct a decision snapshot.

Decision Snapshot
├── Intent
├── Actor
├── Resources
├── Context
├── Evidence
├── Evidence Provenance
├── Authorization
├── Policies
├── Capabilities
├── Preconditions
├── Risk
├── Relevant State Versions
└── Decision

The exact storage mechanism is an implementation concern.

The semantic requirement is sufficient traceability to reconstruct the basis of the decision.

⸻

35. Determinism and Provenance

A deterministic decision without provenance may still be difficult to audit.

Noema should preserve, where material:

* what was decided
* why it was decided
* which evidence was used
* which source supplied the evidence
* which rules applied
* which Policy version applied
* which authorization state applied
* which Capability version applied
* when the decision was evaluated

This creates an auditable Trust chain.

⸻

36. Determinism and Explainability

Explainability does not require exposing hidden Model reasoning.

It means Noema should be able to provide the decision basis.

For example:

Decision:
REJECT
Reason:
Actor lacks project.delete authorization
for Project#456.
Authorization Rule:
Project administrators may delete projects.

This is sufficient to explain the decision basis.

Noema does not need to expose private Model reasoning or chain-of-thought.

⸻

37. Determinism and Uncertainty

Noema should explicitly represent unresolved uncertainty rather than converting it into arbitrary values.

Bad:

Destination = probably Account#123

Good:

Destination =
    AMBIGUOUS
Candidates:
    Account#123
    Account#456

Uncertainty that affects execution should become a typed semantic state.

Possible states include:

AMBIGUOUS
MISSING_INFORMATION
UNVERIFIED
UNDETERMINED

The exact state depends on the underlying condition.

⸻

38. Determinism and Clarification

When deterministic resolution is impossible, clarification is a valid deterministic transition.

Candidate Interpretation
          ↓
Insufficient Evidence
          ↓
AMBIGUOUS
          ↓
CLARIFY
          ↓
New Actor Evidence
          ↓
Resolution
          ↓
Canonical Intent

Clarification is therefore not a failure of Noema.

It is a deterministic response to unresolved material uncertainty.

⸻

39. Determinism and Human Evidence

Actor clarification is explicit evidence.

Example:

Noema:
Which account?
Actor:
The savings account.

The Actor’s response becomes new evidence.

If the evidence deterministically identifies:

Account#Savings

the Intent can be resolved.

The important distinction is that Noema did not guess.

The Actor supplied the missing semantic information.

⸻

40. Determinism and Minimal Clarification

Clarification should target the smallest unresolved material dimension.

Example:

Intent:
RenewCard
Cards:
Visa ending 1234
Mastercard ending 5678

Good:

Which card do you want to renew:
Visa ending in 1234 or Mastercard ending in 5678?

Bad:

Could you provide more information about what you want to do?

Determinism should therefore coexist with minimum necessary interaction.

⸻

41. Determinism and Intent Evolution

An Intent may evolve through multiple states:

Candidate
    ↓
Partially Resolved
    ↓
Ambiguous / Missing Information
    ↓
Clarified
    ↓
Resolved
    ↓
Authorized
    ↓
Trusted
    ↓
Executable

Determinism does not require resolving everything in one pass.

It requires that each transition be governed by explicit evidence and rules.

⸻

42. Determinism Does Not Mean Static

Noema can be dynamic and still deterministic.

Example:

10:00
User = ProjectAdmin
        ↓
Authorization = ALLOWED
11:00
Role revoked
        ↓
Authorization = DENIED

The same Intent may therefore produce different decisions at different times.

That does not violate determinism because the relevant authorization state changed.

⸻

43. Determinism and Distributed Systems

In a distributed environment, Noema must account for:

* eventual consistency
* stale reads
* replication lag
* clock skew
* duplicate events
* concurrent updates
* version conflicts

Determinism therefore requires defining which source and version of state is authoritative for each material decision.

Where a distributed source cannot provide sufficient certainty, Noema must not silently treat stale or conflicting state as current truth.

⸻

44. Determinism and Business State

Noema should not become the authoritative owner of business facts merely because it consumes them for Trust decisions.

Conceptually:

Business System
      ↓
Business State
      ↓
Evidence
      ↓
Noema
      ↓
Trust Decision

Rather than:

Business System
      ↓
Noema
      ↓
Invented Business State

For example, if the Ledger is authoritative for account balance, Noema should use the Ledger’s value as evidence.

A Model-generated balance does not become authoritative merely because it appears plausible.

⸻

45. Determinism and Ontology

The Ontology provides canonical semantics over which deterministic rules can operate.

For example:

Action:
TransferFunds
Resource:
BankAccount
Actor:
Customer
Outcome:
FundsTransferred

The Model can map natural language into candidate canonical concepts.

Noema can then evaluate those concepts using explicit semantics rather than continuing to reason over unconstrained natural language at the execution boundary.

⸻

46. Determinism and Canonical Vocabulary

A canonical vocabulary allows different natural-language expressions to converge on the same semantic object.

For example:

"send money"
"move funds"
"transfer cash"

may map to:

TransferFunds

Once canonicalized, deterministic rules can operate on the same semantic representation.

The canonical vocabulary therefore reduces semantic drift between interpretation, Trust, and execution.

⸻

47. Determinism and Typed Intent

A typed Intent reduces uncontrolled semantic variation.

Conceptually:

TransferFunds {
    actor: Actor
    source: Account
    destination: Account
    amount: Money
    constraints: [...]
}

The Model may populate candidate fields.

Resolution establishes their values.

Trust evaluates the established object.

Execution receives the canonical contract.

This creates a controlled progression from probabilistic interpretation to deterministic commitment.

⸻

48. Determinism and Validation

Before execution, Noema should validate:

* Intent structure
* required fields
* field types
* entity relationships
* Resource resolution
* constraints
* identity
* authorization
* Policy
* Capability
* Preconditions
* relevant freshness requirements

A malformed, materially ambiguous, unauthorized, unsupported, or otherwise untrusted Intent must not reach execution merely because a Model produced a plausible representation.

⸻

49. Determinism and Composition

Composite Intents should retain deterministic semantics.

Example:

"Refund the payment and close the account."

Noema should establish:

RefundPayment(Payment#123)
AND
CloseAccount(Account#456)

before execution.

Each child Intent may have separate:

* ambiguity
* authorization
* Policy
* Capability
* Preconditions
* risk
* Trust requirements

The parent must not hide these differences.

⸻

50. Determinism and Trust Isolation

Trust decisions must remain scoped to the specific Action and execution context.

For a Composite Intent:

Action A
    ↓
Trust A
Action B
    ↓
Trust B

Trust A must not automatically authorize Action B.

This prevents authorization, evidence, Policy satisfaction, or other Trust conditions from leaking across Action boundaries.

⸻

51. Determinism and Partial Failure

Suppose:

RefundPayment → EXECUTE
CloseAccount → REJECT

Noema must not automatically assume that both Actions can execute.

Composite execution semantics must explicitly define whether:

* partial execution
* rollback
* compensation
* dependency blocking
* precondition failure

is permitted.

Deterministic Trust requires these semantics to be explicit rather than inferred during execution.

⸻

52. Determinism and Side Effects

Trust decisions should occur before consequential side effects.

Preferred:

Interpret
   ↓
Resolve
   ↓
Validate
   ↓
Authorize
   ↓
Evaluate Policy
   ↓
Evaluate Preconditions
   ↓
Evaluate Capability
   ↓
Trust
   ↓
Execution Contract
   ↓
Execute
   ↓
Outcome

Not:

Interpret
   ↓
Start execution
   ↓
Discover ambiguity or authorization failure

The deterministic boundary must precede consequential commitment.

⸻

53. Determinism and Retry

Retries must not cause uncontrolled semantic reinterpretation.

Given:

Intent#789

a retry should operate on the same canonical Intent unless Noema explicitly creates a new Intent version.

The Model should not reinterpret the original Actor expression independently on every retry.

This preserves semantic identity across execution attempts.

⸻

54. Determinism and Identity

Identity resolution should produce canonical identifiers.

Example:

"my savings account"
        ↓
Account#123

Once established:

Account#123

should be carried through the execution pipeline.

The executor should not resolve:

"my savings account"

again.

This is especially important for:

* authorization
* auditability
* Resource targeting
* Policy evaluation
* execution contracts

⸻

55. Determinism and Natural Language

Natural language is inherently under-specified.

Noema should not attempt to eliminate that fact.

Instead:

Natural Language
      ↓
Probabilistic Interpretation
      ↓
Candidate Intent
      ↓
Deterministic Resolution
      ↓
Canonical Intent
      ↓
Trust
      ↓
Execution Contract

This is the architectural role of the Ontology, Intent Model, Resolution, and Trust Engine.

The goal is not deterministic language interpretation.

The goal is deterministic semantic commitment.

⸻

56. Deterministic Failure

A deterministic system must be able to say:

“I cannot establish this safely.”

without inventing an answer.

Examples include:

AMBIGUOUS
MISSING_INFORMATION
UNVERIFIED
UNDETERMINED
UNAUTHORIZED
POLICY_BLOCKED
UNSUPPORTED
STALE_CONTEXT
CONFLICTING_EVIDENCE

These are valid deterministic outcomes.

Failure to execute is not itself evidence of non-determinism.

⸻

57. Fail Closed

For consequential Actions:

When required Trust information cannot be established, Noema should fail closed rather than infer semantic certainty or permission.

Conceptually:

Unknown
  ↓
Do not execute

This is particularly important for:

* financial Actions
* destructive Actions
* security Actions
* privacy-sensitive Actions
* external communications
* production changes
* permission changes

Fail-closed behavior should remain subject to the applicable Policy and recovery path.

⸻

58. Determinism and Recoverable States

Failing closed does not mean producing a useless system.

Noema can transition into recoverable states:

AMBIGUOUS
    ↓
CLARIFY
UNVERIFIED
    ↓
REQUEST VERIFICATION
AUTHORIZATION_UNDETERMINED
    ↓
RESOLVE AUTHORITY
POLICY_BLOCKED
    ↓
REQUEST REQUIRED APPROVAL
CONFLICTING_EVIDENCE
    ↓
ESCALATE

The system remains useful without converting uncertainty into authorization.

⸻

59. Determinism and Risk

Different Actions may require different levels of evidence and revalidation.

For example:

Low-risk read
    → ordinary deterministic resolution
Higher-risk state change
    → stronger evidence / fresher state
High-impact financial Action
    → additional authorization or confirmation
Critical Action
    → stronger Policy controls / human review where required

These are not probabilistic Trust thresholds.

They are explicit Action-specific requirements.

⸻

60. Explicit Confirmation

Some Actions may require explicit Actor confirmation even after Intent, Authorization, Policy, and other Trust conditions have been satisfied.

Example:

"You’re about to transfer ₦10,000,000
from Account A to Account B.
Confirm?"

The confirmation becomes explicit Actor evidence for the canonical Intent.

This is different from the Model deciding:

"The Actor probably intended this."

⸻

61. Determinism and Confirmation

Confirmation should confirm the canonical semantic object that will cross the execution boundary.

Bad:

"Do you want me to proceed?"

Good:

"Transfer ₦10,000,000 from Account A to Account B?"

The Actor confirms the specific Action, Resources, and parameters.

The system should preserve the confirmation as provenance.

⸻

62. Determinism and Execution Contracts

The final execution contract should be a deterministic artifact.

Conceptually:

ExecutionContract {
    intent_id
    intent_version
    actor
    action
    resources
    parameters
    constraints
    authorization
    policy_status
    capability
    preconditions
    trust_decision
    provenance
}

The contract represents what Noema has established may happen.

It should contain enough canonical information for the consumer to execute without semantic reinterpretation.

⸻

63. Consumer Responsibility

The execution consumer should:

* validate the contract
* enforce the contract
* execute the Action
* report the execution result

It should not:

* reinterpret natural language
* choose ambiguous Resources
* invent missing parameters
* substitute a different Resource
* override Trust
* treat an absent authorization decision as authorization

The consumer therefore operates on an established semantic contract.

⸻

64. Determinism and External Systems

External systems may enforce their own rules.

If Noema establishes:

Trust:
EXECUTE

but the downstream system establishes:

DENIED

the execution must fail safely.

Noema’s Trust decision does not replace domain-level authorization or business-system enforcement.

Conversely, a downstream system’s successful execution does not retroactively prove that Noema’s original Trust decision was correct.

Trust and execution remain separate states.

⸻

65. Deterministic Trust Does Not Guarantee Successful Execution

A valid deterministic Trust decision can still be followed by:

* network failure
* provider failure
* timeout
* resource unavailability
* concurrency conflict
* downstream rejection
* infrastructure failure

These are execution conditions.

They do not imply that the preceding Trust decision was non-deterministic.

Conceptually:

Trust:
EXECUTE
Execution:
FAILED

is a valid state.

⸻

66. Decision vs Outcome

Noema must distinguish:

Trust Decision:
EXECUTE

from:

Execution Outcome:
FAILED

The Trust decision means:

The Intent was sufficiently grounded and permitted to proceed.

The Outcome means:

What happened when execution was attempted.

Trust does not claim successful execution.

⸻

67. Determinism and Unknown Execution

Execution may become uncertain after a valid Trust decision.

Example:

Trust:
EXECUTE
      ↓
Action
      ↓
Execution:
UNKNOWN

The Unknown execution state must not retroactively rewrite the Trust decision.

Instead, Noema should use the applicable execution recovery semantics, such as:

* reconciliation
* retry
* status inquiry
* escalation
* compensation

where supported.

This preserves the distinction between:

Trust state

and:

Execution state

⸻

68. Determinism and Observability

For consequential Actions, Noema should preserve enough metadata to reconstruct the decision path.

For example:

intent_id
resolution_id
authorization_id
policy_version
capability_version
decision_id
execution_id

This creates a trace across:

Intent
→ Resolution
→ Trust
→ Execution
→ Outcome

The identifiers should be associated with the relevant versions and evidence where required.

⸻

69. Determinism and Versioning

Rules change.

Policies change.

Capabilities change.

Authorization state changes.

Therefore material decisions should be associated with relevant versions.

Example:

Policy:
expense-approval-v4
Authorization:
role-model-v7
Capability:
refund-v2

This makes historical Trust decisions interpretable.

⸻

70. Deterministic Rule Changes

When a rule changes, the same Intent may produce a different decision under a different rule version.

Example:

Policy v1:
Managers may approve ≤ $10,000
Policy v2:
Managers may approve ≤ $5,000

The same Intent may therefore produce:

v1 → ALLOWED
v2 → REQUIRES_APPROVAL

This does not violate determinism.

The relevant Policy input changed.

Historical decisions should remain attributable to the rule version under which they were evaluated.

⸻

71. Determinism and Audit

A Trust decision should be capable of answering:

“Why did Noema allow this?”

or:

“Why did Noema refuse this?”

The answer should be grounded in:

* canonical Intent
* Actor
* Resource
* authoritative state
* Evidence
* Authorization
* Policy
* Capability
* Preconditions
* applicable constraints
* decision

not:

"The Model thought it was safe."

⸻

72. Determinism and Explainable Rejection

Rejection is a valid deterministic outcome.

Example:

Intent:
DeleteProductionDatabase
Trust:
REJECT
Reason:
Actor lacks production.admin authorization.

The system behaved deterministically even though it did not execute.

Rejection should therefore not be represented as Model failure or execution failure.

⸻

73. Determinism as a System Property

Determinism is not merely a property of one function.

It must be preserved across the architecture:

Ontology
   ↓
Intent
   ↓
Resolution
   ↓
Context
   ↓
Evidence
   ↓
Authorization
   ↓
Policy
   ↓
Capability
   ↓
Trust
   ↓
Execution Contract
   ↓
Consumer
   ↓
Execution

Each layer should avoid introducing uncontrolled semantic reinterpretation after the deterministic boundary has been crossed.

⸻

74. Determinism and Trust State

Trust decisions must be explicit and machine-readable.

Conceptually:

TrustDecision {
    decision
    reasons
    evidence
    policy
    evaluated_at
}

Possible Trust decisions are:

EXECUTE
CLARIFY
ESCALATE
REJECT

Additional intermediate states such as:

WAITING_FOR_CONFIRMATION

may exist in the broader execution lifecycle where Policy requires them.

They should not be confused with the four canonical Trust decisions.

⸻

75. Determinism and Action Scope

Determinism must be evaluated at the Action boundary.

A Trust decision for:

get_account_balance

must not automatically authorize:

create_complaint

even when both originate from the same Actor message.

Likewise:

Authorization A

must not automatically become:

Authorization B

This preserves Trust isolation.

⸻

76. Determinism and Data Boundaries

Deterministic Trust does not imply unrestricted access to data.

An Action may require:

account_id
account_status
balance

without requiring:

full_customer_profile
unrelated_transaction_history
private_metadata

Trust decisions should therefore be evaluated using the minimum data necessary within the applicable Data Boundary.

Deterministic evaluation must not become a justification for unnecessary data access.

⸻

77. Determinism and Organizational Boundaries

A deterministic decision must respect organizational and Resource boundaries.

For example:

Actor:
Tenant#A
Resource:
Tenant#B / Project#999

A known Resource identifier does not make cross-boundary access valid.

Trust must evaluate the applicable:

* tenant
* organization
* legal entity
* environment
* workspace
* ownership boundary

where relevant.

⸻

78. Determinism and Material Ambiguity

Determinism does not require eliminating every conceivable ambiguity.

It requires resolving or explicitly representing ambiguity that materially affects the Action.

For example:

Internal renderer:
A or B

may be irrelevant if both produce the same required Outcome.

But:

Payment:
#123 or #456

is material when the selected payment changes the Action.

Therefore deterministic commitment depends on semantic materiality, not merely the existence of multiple internal implementation choices.

⸻

79. Determinism and Intent Substitution

Noema must not choose an interpretation merely because it is:

* authorized
* executable
* easier to perform
* safer for the system
* more convenient
* more probable according to the Model

if the evidence does not establish that interpretation.

For example:

Actor:
"Delete the project."
Projects:
A
B
Actor authorized:
A only

Noema must not infer:

DeleteProject(A)

merely because A is executable.

The correct state remains:

AMBIGUOUS

until the Actor’s Intent is resolved.

This is a core deterministic boundary.

⸻

80. Determinism and Recovery

Deterministic systems should define how unresolved or failed states transition toward recovery.

Examples:

AMBIGUOUS
    ↓
CLARIFY
    ↓
RESOLVE
AUTHORIZATION_UNDETERMINED
    ↓
RESOLVE AUTHORITY
    ↓
AUTHORIZE
CONFLICTING_EVIDENCE
    ↓
RECONCILE / ESCALATE
STALE_CONTEXT
    ↓
REVALIDATE
    ↓
TRUST
EXECUTION_UNKNOWN
    ↓
RECONCILE
    ↓
OUTCOME

Recovery should not silently create a new semantic interpretation.

⸻

81. Determinism and Reconciliation

When execution becomes uncertain, reconciliation should use authoritative execution state where available.

For example:

Trust:
EXECUTE
Execution:
UNKNOWN
Provider:
Transaction status = SETTLED

Noema may establish the Outcome from authoritative provider state.

The original Trust decision remains:

EXECUTE

The execution state is resolved independently.

⸻

82. Determinism and Policy Changes During Execution

Policy may change after an initial Trust decision.

Noema should distinguish:

Policy under which Trust was evaluated

from:

Current Policy

For Actions that require revalidation, the current applicable Policy should be evaluated again before execution.

For Actions that have already crossed an explicitly defined commitment boundary, the system should follow the applicable execution semantics rather than retroactively rewriting historical Trust decisions.

The relevant behavior must be explicit.

⸻

83. Determinism and Human Intervention

Human intervention may be required when the deterministic automated boundary cannot establish sufficient Trust.

Example:

Conflicting Evidence
        ↓
Trust
        ↓
ESCALATE
        ↓
Human Review
        ↓
Updated Context / Evidence
        ↓
Re-evaluation

Human intervention does not mean the Model lacked sufficient confidence.

It means the defined automated Trust boundary requires an external resolution mechanism.

⸻

84. Canonical Invariants

Invariant 1

Probabilistic Model output may propose meaning but must not be the final authority for consequential execution.

Invariant 2

Material ambiguity must not be resolved through probability alone.

Invariant 3

Trust decisions must be based on explicit evidence, authoritative state, applicable Policy, and deterministic rules.

Invariant 4

Given the same relevant inputs, state, Policy, and rule versions, a Trust decision should be reproducible.

Invariant 5

Unknown must not silently become allowed.

Invariant 6

Deterministic failure is preferable to probabilistic execution when required evidence cannot be established.

Invariant 7

The execution boundary must receive canonical semantics rather than raw natural language.

Invariant 8

Executors must not reinterpret an already-resolved Intent.

Invariant 9

Decision provenance must be sufficient to explain material Trust decisions.

Invariant 10

Business State remains authoritative within the domain systems that own it.

Invariant 11

Changes in authoritative state, Policy, authorization, Capability, or relevant rule versions may legitimately produce different decisions.

Invariant 12

Determinism does not guarantee successful execution; Trust and execution outcomes must remain distinct.

Invariant 13

Authorization must evaluate the resolved Intent and must not resolve semantic ambiguity.

Invariant 14

Trust decisions must remain scoped to the specific Action and execution context.

Invariant 15

Trust for one Action must not automatically authorize another Action.

Invariant 16

Material Trust decisions may require revalidation when relevant state, Context, Policy, authorization, or freshness changes.

Invariant 17

Conflicting evidence must not be resolved through source counting or Model preference.

Invariant 18

Model confidence must never independently establish semantic resolution, authorization, Policy compliance, or execution permission.

Invariant 19

Deterministic commitment must occur before consequential side effects.

Invariant 20

Execution retries must not silently create a new semantic interpretation of the original Intent.

Invariant 21

Deterministic Trust must operate within applicable Data and Organizational Boundaries.

Invariant 22

A Trust decision of EXECUTE does not imply successful execution or successful Outcome.

Invariant 23

Execution uncertainty must not retroactively rewrite the original Trust decision.

Invariant 24

Noema must never substitute an interpretation merely because it is more authorized, more executable, more convenient, or more probable.

Invariant 25

The deterministic boundary must prevent uncontrolled probabilistic inference from becoming consequential execution.

⸻

85. Canonical Trust Flow

                    Actor Expression
                           │
                           ▼
                    Model Interpretation
                           │
                           ▼
                    Candidate Intent
                           │
                           ▼
                  Deterministic Resolution
                           │
                    ┌──────┴──────┐
                    │             │
                Ambiguous      Resolved
                    │             │
                    ▼             ▼
                 Clarify       Validate Intent
                    │             │
                    │             ▼
                    │       Identity / Context
                    │             │
                    │             ▼
                    │       Evidence / State
                    │             │
                    │             ▼
                    │       Authorization
                    │             │
                    │             ▼
                    │          Policy
                    │             │
                    │             ▼
                    │        Preconditions
                    │             │
                    │             ▼
                    │        Capability
                    │             │
                    │             ▼
                    │           Risk
                    │             │
                    │             ▼
                    │     Deterministic Trust
                    │             │
                    │      ┌──────┴──────┐
                    │      │             │
                    │   Non-Execute    EXECUTE
                    │      │             │
                    │      ▼             ▼
                    │ CLARIFY /      Execution
                    │ ESCALATE /       Contract
                    │ REJECT             │
                    │                    ▼
                    │                Consumer
                    │                    │
                    │                    ▼
                    │                Execution
                    │                    │
                    │                    ▼
                    │                 Outcome
                    │
                    └─── New Evidence / Context ──→ Resolution

The exact evaluation order may vary by implementation.

The semantic boundary must remain intact.

⸻

86. The Noema Boundary

The architectural principle can be reduced to:

The Model may suggest.
Resolution must establish.
Trust must decide.
The execution contract must preserve.
The executor must obey.

Or, more compactly:

Probability may enter through interpretation.
Deterministic evidence must govern commitment.
Trust decides whether commitment may cross the execution boundary.

⸻

87. Final Definition

Determinism is the architectural property by which Noema ensures that semantic commitment, Trust decisions, and execution authorization are governed by explicit evidence, authoritative state, applicable Policy, and reproducible rules rather than uncontrolled probabilistic inference.

The Model may interpret.

Resolution establishes the canonical semantic object.

Trust evaluates whether that established Intent is sufficiently grounded and permitted to proceed.

The execution boundary receives the canonical contract rather than raw natural language.

The shortest canonical formulation is:

Noema may use probability to understand the Actor; it must not use probability alone to decide what is allowed to happen.