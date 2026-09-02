Determinism

Status: Foundational
Version: 0.1
Domain: Trust
Canonical Path: trust/determinism.md

⸻

1. Definition

Determinism is Noema’s requirement that decisions at the execution boundary be governed by explicit, reproducible rules and authoritative state rather than uncontrolled probabilistic inference.

Determinism does not mean that every component of Noema must be deterministic.

It means:

Probabilistic interpretation may enter the system; ungoverned probability must not be the final authority for consequential execution.

⸻

2. The Core Distinction

Noema explicitly separates:

Probabilistic
    ↓
Model interpretation
    ↓
Candidate Intent
    ↓
Resolution
    ↓
Deterministic
    ↓
Trust decision
    ↓
Execution

The Model may estimate.

Noema must decide.

⸻

3. Why Determinism Exists

Large language models are probabilistic systems.

Given the same expression, a Model may produce different:

interpretations
entities
Resources
Actions
parameters
reasoning paths

This is acceptable during interpretation.

It becomes dangerous when those variations can directly produce different consequential side effects.

Example:

User:
"Cancel my card."

Two cards exist:

Card#123
Card#456

A Model may choose Card#123 today and Card#456 tomorrow.

Noema must not allow sampling variance to determine which card is cancelled.

⸻

4. Determinism Is a Trust Property

Trust exists at the point where Noema decides:

“This Intent is sufficiently established and permitted to cross the execution boundary.”

Therefore the Trust Engine should produce decisions from:

resolved Intent
authoritative evidence
explicit rules
authorization
policy
risk
capability
constraints

rather than:

Model confidence
alone

⸻

5. Determinism Does Not Mean “No AI”

Noema is not a rule engine that happens to contain an LLM.

The Model remains valuable for:

language understanding
semantic interpretation
entity extraction
candidate generation
intent composition
contextual inference
clarification generation

The distinction is:

Model:
"What could this mean?"
Noema:
"What can we establish that it means?"
Trust:
"May this established Intent proceed?"

⸻

6. Deterministic Boundary

Noema should have a clearly defined deterministic boundary.

Conceptually:

              HUMAN INPUT
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
          │     NOEMA        │
          │   Resolution     │
          │   Trust          │
          └────────┬─────────┘
                   │
             Canonical Intent
                   │
                   ▼
             Trust Decision
                   │
          ┌────────┴────────┐
          │                 │
        Reject           Execute

The exact implementation can evolve.

The invariant should not.

⸻

7. Deterministic Does Not Mean Predictable From the User’s Sentence Alone

A decision may depend on changing authoritative state.

Example:

User:
"Cancel my active subscription."

At 10:00:

Subscription#123 = Active

At 12:00:

Subscription#123 = Cancelled

The result may legitimately differ because the authoritative state changed.

Determinism means:

Given the same relevant inputs and state, the decision procedure produces the same result.

⸻

8. Determinism Is Input-Relative

A decision is deterministic relative to its defined inputs.

Conceptually:

Decision =
    f(
        Intent,
        Actor,
        Context,
        Authoritative State,
        Rules,
        Policies,
        Capabilities
    )

If any material input changes, the decision may legitimately change.

⸻

9. Reproducibility

A deterministic decision should be reproducible.

If Noema records:

Intent version
Actor
Context
Evidence
Authorization rules
Policy versions
Capability version
Decision
timestamp

then the decision should be explainable and, where state permits, reproducible.

⸻

10. Determinism vs Model Confidence

Confidence is not determinism.

Example:

Model:
Interpretation A = 99%
Interpretation B = 1%

This is still probabilistic.

Determinism requires something like:

Evidence:
B is impossible under authoritative state.

Then:

A = resolved

The distinction is:

Probability:
"What is likely?"
Determinism:
"What is established?"

⸻

11. Confidence Must Not Become Permission

A particularly dangerous architecture is:

if model.confidence > 0.9:
    execute()

Noema should reject this design.

A high confidence score does not establish:

correctness
authorization
policy compliance
resource identity
safety

⸻

12. Determinism and Ambiguity

Material ambiguity is a failure of deterministic resolution.

Example:

Card#123
Card#456

Both satisfy:

“Renew my card.”

Noema cannot deterministically establish the target.

Therefore:

AMBIGUOUS

The correct response is clarification, not probabilistic selection.

⸻

13. Determinism and Resolution

Resolution is where Noema converts:

candidate meaning

into:

canonical meaning

where sufficient evidence exists.

This makes resolution one of the principal deterministic mechanisms of Noema.

⸻

14. Determinism and Authorization

Authorization must be deterministic.

For example:

Actor:
User#123
Intent:
DeleteProject(Project#456)
Rule:
Project admins may delete projects.
Relationship:
User#123 → admin_of → Project#456

Result:

ALLOWED

The Model should not be asked whether User#123 “seems authorized.”

⸻

15. Determinism and Policy

Policy evaluation should also be governed by explicit rules.

Example:

Transaction:
₦20,000,000
Policy:
Transactions > ₦10,000,000 require secondary approval.

Result:

SECONDARY_APPROVAL_REQUIRED

A Model may help identify the transaction or policy category.

It should not decide the policy outcome through free-form judgment.

⸻

16. Determinism and Capability

Capability determination should rely on explicit declarations.

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

No Model guess should turn an unsupported operation into a supported one.

⸻

17. Determinism and Execution Contracts

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

This is a major architectural consequence of deterministic Trust.

⸻

18. Execution Must Not Reinterpret Intent

Once Noema has established:

DeleteProject(Project#456)

the executor should not receive:

"Delete the project."

and independently decide which project that means.

It should receive the canonical target:

Project#456

This prevents probabilistic reinterpretation from re-entering the execution boundary.

⸻

19. Determinism and Consumer-Side Execution

The execution consumer should receive sufficient information to perform the Action without semantic guessing.

Conceptually:

{
    actor: User#123,
    action: DeleteProject,
    resource: Project#456,
    authorization: allowed,
    constraints: [...],
    provenance: [...]
}

The consumer executes the contract.

It does not reinterpret the Actor’s language.

⸻

20. Determinism and Idempotency

Determinism and idempotency are different.

Determinism

Same relevant inputs → same decision.

Idempotency

Repeated execution of the same request does not produce unintended additional effects.

A Trust Engine may be deterministic while execution is not idempotent.

Both properties matter.

⸻

21. Determinism and Concurrency

A deterministic decision does not imply deterministic concurrent execution.

Example:

Trust:
ALLOWED
Concurrent:
Another system changes the Resource.

Noema therefore needs explicit handling of:

stale state
race conditions
version conflicts
optimistic concurrency
transaction boundaries

where relevant.

⸻

22. Determinism and Time

Time is an input.

If a policy says:

Deployments allowed:
09:00–17:00 UTC

then the current time must be an authoritative input to the decision.

The system should not rely on an LLM interpreting:

“It’s probably still within working hours.”

⸻

23. Determinism and External State

External state can change.

Therefore deterministic evaluation should specify which state snapshot it used.

Example:

Authorization evaluated against:
PolicyVersion = 17
ResourceVersion = 42
ActorPermissionsVersion = 9

This improves reproducibility.

⸻

24. Decision Snapshots

For consequential decisions, Noema should conceptually be able to construct a decision snapshot.

Decision Snapshot
├── Intent
├── Actor
├── Resources
├── Context
├── Evidence
├── Authorization
├── Policies
├── Capabilities
├── Constraints
└── Decision

The exact storage mechanism is an implementation concern.

The semantic requirement is traceability.

⸻

25. Determinism and Provenance

A deterministic decision without provenance can still be difficult to trust.

Noema should preserve:

what was decided
why it was decided
which evidence was used
which rules applied
which version of those rules applied

This creates an auditable trust chain.

⸻

26. Determinism and Explainability

Explainability should not mean exposing hidden Model reasoning.

It means being able to provide the decision basis.

For example:

“The request was blocked because the Actor does not have project.delete permission for this project.”

This is sufficient.

Noema does not need to expose an internal chain-of-thought.

⸻

27. Determinism and Uncertainty

Noema should explicitly represent unresolved uncertainty rather than converting it into arbitrary values.

Bad:

Destination = probably Account#123

Good:

Destination =
    AMBIGUOUS
    Candidates:
        Account#123
        Account#456

Uncertainty should become a typed system state.

⸻

28. Determinism and Clarification

When deterministic resolution is impossible, clarification is the correct transition.

Probabilistic interpretation
          ↓
Insufficient evidence
          ↓
Clarification
          ↓
New Actor input
          ↓
Deterministic resolution

Clarification is therefore not a failure of Noema.

It is a deterministic response to unresolved uncertainty.

⸻

29. Determinism and Human Input

Human clarification is itself an input.

Example:

Noema:
Which account?
Actor:
The savings account.

The Actor’s explicit response becomes evidence.

Resolution can then establish:

Account#Savings

Noema is deterministic because the ambiguity has been resolved by explicit evidence.

⸻

30. Determinism and Intent Evolution

An Intent may evolve through multiple states:

Candidate
    ↓
Partially Resolved
    ↓
Clarified
    ↓
Resolved
    ↓
Authorized
    ↓
Executable

Determinism does not mean the system must decide everything in one pass.

It means each commitment should be governed by explicit evidence and rules.

⸻

31. Determinism Does Not Mean Static

Noema can be dynamic and still deterministic.

For example:

10:00:
User is authorized.
11:00:
Authorization revoked.
11:01:
Same Intent submitted.

Different result:

10:00 → ALLOWED
11:01 → DENIED

because the relevant state changed.

That is still deterministic.

⸻

32. Determinism and Distributed Systems

In a distributed environment, Noema must account for:

eventual consistency
stale reads
replication lag
clock skew
duplicate events
concurrent updates

Determinism therefore requires defining which source and version of state is authoritative for each decision.

⸻

33. Authoritative State

Every material decision should identify its authoritative source where practical.

Example:

Resource ownership:
CRM
Authorization:
Policy Engine
Payment state:
Payment Service
Account balance:
Ledger

Noema should not create competing authoritative copies of business truth merely to make decisions easier.

⸻

34. Determinism and Business State

Noema owns:

Intent State
Trust State
Execution Decision

The business system owns:

Business State

Therefore:

Business State
      ↓
Evidence
      ↓
Noema Decision

rather than:

Noema
      ↓
invented Business State

⸻

35. Determinism and Ontology

The Ontology provides canonical semantics.

For example:

Action:
TransferFunds
Resource:
BankAccount
Actor:
Customer
Outcome:
FundsTransferred

This reduces semantic drift.

The Model can map language into the Ontology.

Noema can then reason over canonical concepts rather than free-form text.

⸻

36. Determinism and Canonical Vocabulary

A canonical vocabulary allows different natural-language expressions to converge:

"send money"
"move funds"
"transfer cash"

may all map to:

TransferFunds

Once canonicalized, deterministic rules can operate on the same semantic representation.

⸻

37. Determinism and Typed Intent

A typed Intent reduces ambiguity.

Conceptually:

TransferFunds {
    actor: Actor
    source: Account
    destination: Account
    amount: Money
    constraints: [...]
}

The Model fills candidate fields.

Resolution establishes their values.

Trust evaluates the typed object.

Execution receives the typed contract.

⸻

38. Determinism and Validation

Before execution, Noema should validate:

Intent structure
required fields
field types
relationships
constraints
authorization
policy
capability

A malformed Intent should not reach execution.

⸻

39. Determinism and Composition

Composite Intents should retain deterministic semantics.

Example:

"Refund the payment and close the account."

Noema should establish:

RefundPayment(Payment#123)
AND
CloseAccount(Account#456)

before execution.

Each child Intent may have separate:

authorization
policy
capability
risk

The parent should not hide those differences.

⸻

40. Determinism and Partial Failure

Suppose:

RefundPayment → Allowed
CloseAccount → Denied

Noema must not automatically execute both.

Composite execution semantics must explicitly define whether:

partial execution
rollback
compensation
precondition failure

is allowed.

Deterministic Trust requires these semantics to be explicit.

⸻

41. Determinism and Side Effects

Noema’s deterministic decision should happen before consequential side effects.

Interpret
   ↓
Resolve
   ↓
Validate
   ↓
Authorize
   ↓
Policy
   ↓
Trust
   ↓
Execute
   ↓
Side Effect

This ordering reduces the possibility that uncertainty enters after execution has begun.

⸻

42. Determinism and Retry

Retries must not cause a different semantic interpretation.

Given:

Intent#789

a retry should operate on the same canonical Intent unless the system explicitly creates a new Intent version.

The Model should not reinterpret the original request on every retry.

⸻

43. Determinism and Identities

Identity resolution should produce canonical identifiers.

Example:

"my savings account"
        ↓
Account#123

Once resolved:

Account#123

should be carried through the execution pipeline.

The executor should not resolve “my savings account” again.

⸻

44. Determinism and Natural Language

Natural language is inherently under-specified.

Noema should not attempt to eliminate this fact.

Instead:

Natural Language
      ↓
Probabilistic Interpretation
      ↓
Deterministic Semantic Commitment

This is the architectural role of the Ontology, Intent Model, Resolution, and Trust Engine.

⸻

45. Deterministic Failure

A deterministic system must be able to say:

"I cannot establish this safely."

instead of inventing an answer.

Examples:

AMBIGUOUS
MISSING_INFORMATION
UNAUTHORIZED
POLICY_BLOCKED
UNSUPPORTED
UNVERIFIABLE

These are successful deterministic outcomes.

⸻

46. Fail Closed

For consequential Actions:

When required Trust information cannot be established, Noema should fail closed rather than infer permission or semantic certainty.

Conceptually:

Unknown
  ↓
Do not execute

This is especially important for:

financial actions
destructive actions
security actions
privacy-sensitive actions
external communications
production changes

⸻

47. Determinism and Graceful Degradation

Failing closed does not mean producing a useless system.

Noema can transition into a recoverable state:

AMBIGUOUS
    ↓
Clarification
UNVERIFIED
    ↓
Request verification
UNAUTHORIZED
    ↓
Request appropriate authorization
POLICY_BLOCKED
    ↓
Request approval

The system remains useful without guessing.

⸻

48. Determinism and Trust Levels

Noema may eventually support different Trust requirements based on risk.

For example:

Low risk:
standard resolution
Medium risk:
stronger evidence
High risk:
explicit confirmation
Critical:
multi-party authorization

This does not weaken determinism.

It defines different deterministic thresholds for different consequences.

⸻

49. Explicit Confirmation

Confirmation may be appropriate for high-impact Actions.

Example:

“You’re about to transfer ₦10,000,000 from Account A to Account B. Confirm?”

The confirmation becomes explicit Actor evidence.

This is different from the Model deciding:

"the user probably intended this."

⸻

50. Determinism and Confirmation

Confirmation should confirm a canonical Intent, not raw language.

Bad:

“Do you want me to proceed?”

Good:

“Transfer ₦10,000,000 from Account A to Account B?”

The Actor confirms the exact semantic object that will cross the execution boundary.

⸻

51. Determinism and Execution Contracts

The final execution contract should be a deterministic artifact.

Conceptually:

ExecutionContract {
    intent_id
    actor
    action
    resources
    parameters
    constraints
    authorization
    policy_status
    capability
    trust_decision
    provenance
}

The contract represents what Noema has decided may happen.

⸻

52. Consumer Responsibility

The execution consumer should:

validate contract
enforce contract
execute Action
report result

It should not:

reinterpret natural language
choose ambiguous Resources
invent missing parameters
override Trust

This keeps the deterministic boundary intact.

⸻

53. Determinism and Enforcement

A deterministic decision is useless if downstream systems can ignore it.

Therefore:

Trust decisions must be enforceable, not merely advisory.

If Noema says:

DENIED

the execution path must not nevertheless perform the Action.

⸻

54. Determinism and External Systems

External systems may still enforce their own rules.

If Noema says:

ALLOWED

but the downstream system says:

DENIED

execution must fail safely.

Noema’s authorization decision is not a replacement for domain-level enforcement.

⸻

55. Deterministic Trust Does Not Guarantee Successful Execution

A valid deterministic decision can still lead to:

network failure
provider failure
concurrency conflict
resource unavailable
timeout
downstream rejection

These are execution failures.

They do not imply that the Trust decision was non-deterministic.

⸻

56. Decision vs Outcome

Noema must distinguish:

Trust Decision:
ALLOWED

from:

Execution Outcome:
FAILED

The former says the Intent was trusted to proceed.

The latter says execution did not successfully produce the intended Business Outcome.

⸻

57. Determinism and Observability

For consequential Actions, Noema should expose enough metadata to reconstruct the decision path.

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

⸻

58. Determinism and Versioning

Rules change.

Policies change.

Capabilities change.

Therefore decisions should be associated with versions where material.

Example:

Policy:
expense-approval-v4
Authorization:
role-model-v7
Capability:
refund-v2

This makes historical decisions interpretable.

⸻

59. Deterministic Rule Changes

When a rule changes:

v1:
Managers may approve ≤ $10,000
v2:
Managers may approve ≤ $5,000

the same Intent may produce different decisions under different rule versions.

That does not violate determinism.

The relevant input changed.

⸻

60. Determinism and Audit

A Trust decision should be capable of answering:

“Why did Noema allow this?”

or:

“Why did Noema refuse this?”

The answer should be grounded in:

canonical Intent
Actor
authoritative state
rules
policy
evidence
decision

not:

“The Model thought it was safe.”

⸻

61. Determinism and Explainable Rejection

Rejection is also a valid deterministic outcome.

Example:

Intent:
DeleteProductionDatabase
Result:
DENIED
Reason:
Actor lacks production.admin authorization.

The system has behaved deterministically even though it did not execute.

⸻

62. Determinism as a System Property

Determinism is not merely a function property.

It must exist across the architecture:

Ontology
   ↓
Intent
   ↓
Resolution
   ↓
Trust
   ↓
Execution Contract
   ↓
Consumer

Each layer should avoid introducing uncontrolled semantic reinterpretation.

⸻

63. Canonical Invariants

Invariant 1

Probabilistic Model output may propose meaning but must not be the final authority for consequential execution.

Invariant 2

Material ambiguity must not be resolved through probability alone.

Invariant 3

Trust decisions must be based on explicit evidence, rules, and authoritative state.

Invariant 4

Given the same relevant inputs and state, a Trust decision should be reproducible.

Invariant 5

Unknown must not silently become allowed.

Invariant 6

Deterministic failure is preferable to probabilistic execution when required evidence is unavailable.

Invariant 7

The execution boundary must receive canonical semantics rather than raw natural language.

Invariant 8

Executors must not reinterpret an already-resolved Intent.

Invariant 9

Decision provenance must be sufficient to explain material Trust decisions.

Invariant 10

Business State remains authoritative within the domain systems that own it.

Invariant 11

Changes in authoritative state or rule versions may legitimately produce different decisions.

Invariant 12

Determinism does not guarantee successful execution; Trust and execution outcomes must remain distinct.

⸻

64. Canonical Trust Flow

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
                                  │
                                  ▼
                           Authorization
                                  │
                                  ▼
                              Policy
                                  │
                                  ▼
                            Capability
                                  │
                                  ▼
                              Risk
                                  │
                                  ▼
                         Deterministic Trust
                                  │
                         ┌────────┴────────┐
                         │                 │
                       Deny              Allow
                         │                 │
                         ▼                 ▼
                       Stop        Execution Contract
                                           │
                                           ▼
                                       Consumer
                                           │
                                           ▼
                                       Execution

⸻

65. The Noema Boundary

The architectural principle can be reduced to:

The Model may suggest.
Noema must establish.
Trust must decide.
The executor must obey the decision.

That is the practical meaning of deterministic Trust.

⸻

66. Final Definition

Determinism is the architectural property by which Noema ensures that semantic commitment, Trust decisions, and execution authorization are governed by explicit evidence, authoritative state, and reproducible rules rather than uncontrolled probabilistic inference.

The shortest canonical formulation is:

Noema may use probability to understand the Actor; it must not use probability alone to decide what is allowed to happen.