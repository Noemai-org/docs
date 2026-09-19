# AI Harness
Status: Foundational
Version: 0.1
Domain: AI
Canonical Path: ai/ai-harness.md
⸻
## 1. Definition
The AI Harness is the controlled execution environment through which Noema uses probabilistic AI capabilities while preserving the deterministic boundaries of the Noema system.
The AI Harness provides the interface between:
- AI models
- model context
- prompts and instructions
- tools and retrieval mechanisms
- candidate outputs
- deterministic Noema components
The AI Harness exists to ensure that probabilistic model behavior remains bounded, observable, replaceable, and subordinate to Noema’s canonical semantic and Trust boundaries.
The AI Harness may enable a model to:
- interpret natural language
- propose candidate Intents
- extract entities
- identify ambiguity
- generate clarification requests
- retrieve relevant information
- reason over provided context
- propose Actions
- construct candidate plans
- produce structured outputs
- assist with other bounded reasoning tasks
The AI Harness does not itself establish Trust, authorize Actions, or execute business-side effects.
The central principle is:
> The AI Harness enables probabilistic intelligence; it does not grant probabilistic intelligence authority.
⸻
## 2. Purpose
The purpose of the AI Harness is to provide a stable system boundary around model invocation.
Without a Harness, model usage can become distributed across application code, prompts, agents, tools, and integrations, making it difficult to establish:
- which model was used
- what context was provided
- what instructions governed the invocation
- what tools were available
- what output was produced
- what model version generated the output
- whether the output was accepted
- how the output influenced downstream state
- whether the invocation was reproducible or auditable
The AI Harness centralizes these concerns.
Conceptually:
```text
Noema
  │
  ▼
AI Harness
  │
  ├── Model
  ├── Instructions
  ├── Context
  ├── Tools
  ├── Retrieval
  ├── Structured Output
  └── Invocation Provenance
  │
  ▼
Candidate AI Result
  │
  ▼
Deterministic Noema Components

The Harness therefore provides controlled access to AI rather than allowing AI to become an uncontrolled architectural dependency.

⸻

3. The AI Boundary

Noema contains both probabilistic and deterministic components.

The AI Harness belongs on the probabilistic side of the boundary.

                    PROBABILISTIC
                         │
                         ▼
                 ┌───────────────┐
                 │  AI HARNESS   │
                 │               │
                 │ Model         │
                 │ Context       │
                 │ Retrieval     │
                 │ Reasoning     │
                 │ Generation    │
                 └───────┬───────┘
                         │
                  Candidate Result
                         │
                         ▼
                 ┌───────────────┐
                 │  DETERMINISTIC│
                 │    NOEMA      │
                 │               │
                 │ Validation    │
                 │ Trust         │
                 │ Policy        │
                 │ Authorization │
                 │ Contracts     │
                 └───────┬───────┘
                         │
                         ▼
                    Execution

The Harness must not blur this boundary.

A model-generated result is an input to deterministic Noema processing.

It is not itself a deterministic decision.

⸻

4. AI Output Is a Candidate

The output of an AI invocation should be treated as a candidate result until accepted by the appropriate deterministic component.

Examples include:

Candidate Intent
Candidate Entity
Candidate Context
Candidate Clarification
Candidate Action
Candidate Plan
Candidate Tool Selection
Candidate Structured Result

The canonical progression is:

Model Output
    ↓
Candidate
    ↓
Deterministic Processing
    ↓
Accepted / Rejected / Requires Clarification

The AI Harness must not represent model output as authoritative merely because it conforms to a requested schema.

Structural conformity is not semantic validity.

Semantic validity is not Trust.

Trust is not execution.

⸻

5. AI Harness Responsibilities

The AI Harness is responsible for controlled model invocation and its associated provenance.

Its responsibilities include, where applicable:

* model selection
* model invocation
* instruction management
* context assembly
* input normalization
* output normalization
* structured output handling
* tool availability
* retrieval coordination
* invocation limits
* timeout handling
* retry behavior
* model metadata
* invocation provenance
* output capture
* error classification
* resource accounting
* policy enforcement specific to AI invocation

The exact implementation may vary.

The architectural responsibility remains stable:

The Harness controls how Noema invokes AI.

⸻

6. What the AI Harness Does Not Own

The AI Harness does not own:

* canonical Intent semantics
* final Intent validation
* Trust decisions
* authorization decisions
* business policy authority
* enterprise business state
* execution authority
* business-side effects
* authoritative execution outcomes

For example:

The AI Harness may propose:

Action = TRANSFER
Amount = ₦50,000
Recipient = customer_123

The Harness does not decide:

TRANSFER IS AUTHORIZED

That determination belongs to the appropriate deterministic Trust and authorization mechanisms.

Similarly, the Harness does not execute the transfer.

⸻

7. Model Independence

Noema should not make the canonical architecture dependent on a particular AI model provider.

The AI Harness should provide an abstraction through which different models can be invoked.

Conceptually:

AI Harness
    │
    ├── Model A
    ├── Model B
    ├── Model C
    └── Future Model

A model may change because of:

* capability requirements
* cost
* latency
* availability
* performance
* deployment environment
* policy
* version changes

The surrounding Noema semantics should remain stable.

Therefore:

Noema Intent Semantics
        ≠
Specific Model Implementation

⸻

8. Model Versioning

Every consequential AI invocation should identify the model version used.

Conceptually:

model_provider
model_name
model_version
invocation_version

Where the provider does not expose a stable version identifier, the Harness should retain the strongest available identifier.

This allows Noema to distinguish:

same Intent
different model version
different candidate result

from:

same Intent
same model version
different context

Model provenance is therefore part of AI observability.

⸻

9. Invocation Contract

An AI invocation should be represented as a structured request.

Conceptually:

AIInvocation {
    invocation_id
    model
    instructions
    input
    context
    tools
    output_schema
    constraints
    timeout
    provenance
}

The exact schema belongs to implementation specifications.

The canonical principle is that an AI invocation must be inspectable as a bounded operation rather than an opaque call to an external model.

⸻

10. Context

The AI Harness may provide contextual information to a model.

Context may include:

* conversation state
* Intent state
* relevant entities
* retrieved documents
* system state
* prior outputs
* available capabilities
* policy information
* temporal information
* evidence
* tool results

However:

Context provided to a model is not automatically authority.

A model receiving authorization information does not thereby acquire authorization authority.

A model receiving business data does not become the owner of that business data.

The distinction between context and authority must remain explicit.

⸻

11. Context Provenance

Context supplied to a model should be traceable where material to downstream decisions.

Conceptually:

Context Item
    ├── source
    ├── source version
    ├── timestamp
    ├── freshness
    └── relevance

This is particularly important where model output subsequently contributes to Intent resolution or Trust evaluation.

Noema should be able to establish what information the model was given when it produced a consequential candidate result.

⸻

12. Prompt and Instruction Control

Instructions supplied to models are part of the AI invocation environment.

The Harness should therefore treat instructions as controlled inputs rather than incidental strings.

Where consequential, the system should retain:

* instruction identity
* instruction version
* applicable system instructions
* task instructions
* relevant configuration
* invocation timestamp

A change in instructions can change model behavior.

Therefore instruction versions may be necessary for reconstructing historical AI decisions.

⸻

13. Structured Output

Where an AI result feeds deterministic Noema components, structured output should be preferred over unconstrained natural-language output.

For example:

{
    action: "TRANSFER",
    recipient: "customer_123",
    amount: 50000,
    currency: "NGN"
}

However:

structured output
    ≠
validated output

A model may produce syntactically valid structured data containing:

* invalid values
* missing semantics
* unsupported entities
* contradictory fields
* fabricated references

Therefore structured output must proceed through deterministic validation.

⸻

14. Schema Conformance

The Harness may enforce output schema conformance.

For example:

Model
  ↓
Schema Validation
  ↓
Candidate Result

Schema validation establishes structural conformity.

It does not establish:

* truth
* authorization
* policy compliance
* Trust
* execution eligibility

Therefore:

Schema Valid
    ≠
Semantically Valid
    ≠
Trusted
    ≠
Executable

⸻

15. AI and Intent Resolution

AI may assist in interpreting human language into a candidate Intent.

Conceptually:

Human Expression
       ↓
AI Harness
       ↓
Candidate Intent
       ↓
Intent Resolution
       ↓
Validation
       ↓
Trust

The model may propose:

Action
Actor
Object
Parameters
Constraints
Desired Outcome

The canonical Intent system remains responsible for establishing the resulting semantic representation.

The model must not silently define canonical Intent semantics.

⸻

16. AI and Ambiguity

The AI Harness may identify ambiguity.

For example:

"Send the report to John."

The model may identify:

Multiple possible recipients

The correct downstream result may be:

WAITING_FOR_CLARIFICATION

The model must not resolve material ambiguity by guessing merely because one interpretation appears probable.

Probability may help identify ambiguity.

It does not authorize the system to ignore it.

⸻

17. AI and Clarification

The AI Harness may generate candidate clarification questions.

For example:

"Which John should receive the report?"

The clarification request should then become part of the deterministic Noema lifecycle.

Ambiguous Intent
      ↓
Candidate Clarification
      ↓
Clarification Request
      ↓
Actor Response
      ↓
Updated Intent
      ↓
Validation

The model generates the question.

Noema owns the resulting state transition.

⸻

18. AI and Validation

The AI Harness may assist with candidate generation and normalization.

It must not be the authoritative validator for consequential conditions.

The canonical architecture is:

AI
 ↓
Candidate Intent
 ↓
Deterministic Validation
 ↓
Trust

not:

AI
 ↓
"I believe this Intent is valid."
 ↓
Trust

Validation remains governed by explicit rules and authoritative evidence.

⸻

19. AI and Trust

The AI Harness does not determine Trust.

The relationship is:

AI Output
    ↓
Evidence / Candidate Interpretation
    ↓
Validation
    ↓
Trust Evaluation

AI output may contribute information to a Trust evaluation.

It must not silently become the Trust decision itself.

For example:

Model confidence = 0.99

does not imply:

Trust = READY

Similarly:

Model confidence = 0.60

does not necessarily imply:

Trust = BLOCKED

Trust depends on deterministic requirements and evidence.

⸻

20. AI and Authorization

Authorization must remain outside model authority.

The model may identify that an Action requires authorization.

The model may retrieve or reference authorization information if explicitly permitted.

But the authoritative authorization decision must come from the appropriate deterministic authorization mechanism.

Therefore:

AI:
"Authorization appears relevant."
Authorization System:
"Authorization is granted."
Trust Engine:
"All Trust conditions are satisfied."

The model does not become the authorization authority.

⸻

21. AI and Policy

Models may interpret policy text or identify potentially applicable policies.

However, where a policy is authoritative, its execution semantics must be represented through deterministic mechanisms.

The model may assist with:

Policy discovery
Policy interpretation
Candidate policy matching

The system must establish:

Policy applicability
Policy satisfaction
Policy violation

through authoritative rules or policy evaluation mechanisms.

⸻

22. AI and Tools

The AI Harness may expose tools to a model.

Tools may include:

* retrieval
* search
* calculation
* data lookup
* system queries
* bounded operations

Tool availability does not imply unrestricted execution authority.

A tool should have an explicit contract defining:

* identity
* inputs
* outputs
* permissions
* side effects
* constraints
* failure behavior
* provenance requirements

The model may select or request a tool.

The Harness and downstream deterministic systems must enforce whether that tool invocation is permitted.

⸻

23. Read Tools and Write Tools

Noema should distinguish between tools that observe state and tools that mutate state.

Conceptually:

Read Tool
    ↓
Observe
Write Tool
    ↓
Change Business State

Write-capable tools require stronger controls because they can cross the execution boundary.

A model selecting a write tool must not itself constitute authorization to perform the write.

The write must proceed through the canonical Trust and execution mechanisms.

⸻

24. Tool Calls Are Not Automatically Actions

A model-generated tool call should not automatically be treated as a canonical Noema Action.

For example:

Model:
call transfer_money(...)

does not mean:

Noema:
execute transfer

Instead:

Model Tool Proposal
       ↓
Action / Contract Resolution
       ↓
Validation
       ↓
Trust
       ↓
Execution Contract
       ↓
Consumer Acceptance
       ↓
Execution

This preserves the distinction between model behavior and system authority.

⸻

25. AI and Planning

The AI Harness may support planning.

A model may produce:

Step 1
Step 2
Step 3

or:

Candidate Plan

A plan is not automatically an execution authorization.

Each consequential Action must remain subject to the applicable:

* validation
* policy
* authorization
* capability
* constraint
* Trust
* contract

requirements.

Planning therefore remains subordinate to execution governance.

⸻

26. AI and Memory

AI may receive information from prior interactions or stored context.

Such information must not automatically become authoritative.

Memory should be treated as contextual evidence with explicit provenance and applicable freshness.

For example:

Previous conversation:
"Use John's account."

does not necessarily establish that a later transfer should use John’s account.

The current Intent and applicable evidence determine whether the information remains relevant.

⸻

27. AI and External Knowledge

The Harness may provide retrieved external information to a model.

The system should distinguish:

Retrieved information

from:

Authoritative evidence

Retrieval may provide useful context.

It does not automatically establish truth for consequential decisions.

Where an authoritative system exists, Noema should prefer the authoritative source for the relevant predicate.

⸻

28. Hallucination Boundary

Model-generated information must be treated as potentially unverified unless supported by authoritative evidence.

The Harness should therefore make it possible to distinguish:

Model-generated claim

from:

Externally established fact

A model must not be allowed to silently manufacture:

* entity identities
* authorization
* account state
* policy state
* execution outcomes
* system responses
* evidence

Noema should prefer explicit uncertainty over fabricated certainty.

⸻

29. Uncertainty

AI outputs may contain uncertainty.

The Harness may capture model-specific uncertainty signals where available.

However, these signals are not themselves Trust predicates unless explicitly incorporated into a deterministic rule.

For example:

Model confidence = 0.82

may be recorded as provenance.

It does not automatically mean:

Trust = 82%

Noema Trust is not a probability score.

⸻

30. Retries

AI invocations may fail for technical reasons.

The Harness may retry an invocation where permitted.

However, retries must not silently change semantic authority.

A retry should be understood as:

technical re-invocation

not:

new evidence that makes an Intent trusted

A different model response must still pass through the same deterministic downstream controls.

For consequential operations, retry behavior should be bounded and observable.

⸻

31. Model Fallback

The Harness may support model fallback.

For example:

Primary Model
     ↓ unavailable
Fallback Model

A fallback model may produce a different candidate result.

Therefore the resulting candidate must be evaluated according to the same canonical Noema requirements.

Model fallback must not bypass:

* validation
* Trust
* authorization
* policy
* contracts

⸻

32. AI Failure States

The Harness should distinguish relevant invocation failures.

Examples include:

MODEL_UNAVAILABLE
MODEL_TIMEOUT
MODEL_RATE_LIMITED
INVALID_MODEL_OUTPUT
SCHEMA_VALIDATION_FAILED
TOOL_FAILURE
CONTEXT_UNAVAILABLE
RETRIEVAL_FAILURE
TOKEN_LIMIT_EXCEEDED
INVOCATION_CANCELLED

These technical states should not automatically be translated into business-level Trust decisions without explicit semantics.

For example:

Model unavailable

does not necessarily mean:

Intent denied

It may instead require:

WAITING

or another appropriate lifecycle state.

⸻

33. AI Invocation Idempotency

AI invocations are generally not guaranteed to produce identical outputs even with identical inputs.

Therefore the Harness must not assume:

same prompt
=
same model output

Deterministic behavior must be enforced where required by the downstream Noema components, not assumed from model behavior.

If reproducibility is required for a particular workflow, the relevant model configuration, context, instructions, and invocation metadata should be preserved.

⸻

34. AI and Deterministic Components

The AI Harness should be treated as one component in a larger pipeline.

A canonical architecture is:

Human Expression
       ↓
AI Harness
       ↓
Candidate Interpretation
       ↓
Intent Resolution
       ↓
Validation
       ↓
Trust Engine
       ↓
Action / Execution Contract
       ↓
Execution Consumer
       ↓
Outcome

The AI Harness does not replace the deterministic layers.

It supplies probabilistic capabilities to them.

⸻

35. AI Harness and State

The Harness may maintain invocation state.

Examples include:

REQUESTED
RUNNING
COMPLETED
FAILED
CANCELLED
TIMED_OUT

These are AI invocation states.

They must not be confused with:

* Intent state
* Trust state
* Execution state
* Business state

Noema should preserve these distinctions.

⸻

36. AI Harness and Trust State

An AI invocation may influence the information available to Trust evaluation.

For example:

AI invocation
    ↓
candidate recipient identified
    ↓
Validation
    ↓
Trust Evaluation

But:

AI invocation = Trust evaluation

is incorrect.

The Trust State Machine remains authoritative for Trust lifecycle transitions.

⸻

37. AI Harness and Execution Boundary

The AI Harness must not silently cross the execution boundary.

If a model is capable of invoking a write-capable tool, the Harness must ensure that the invocation remains subject to the applicable Noema execution controls.

The conceptual boundary is:

AI Proposal
     ↓
Deterministic Governance
     ↓
Execution Contract
     ↓
Consumer Acceptance
     ↓
Execution

The model cannot bypass this boundary merely because a tool is technically available.

⸻

38. Observability

Consequential AI invocations should be observable.

Where applicable, Noema should retain:

* invocation ID
* model identity
* model version
* instruction version
* input reference
* context references
* tool references
* output reference
* timestamp
* latency
* token/resource usage
* error state
* downstream decision reference

The exact retention policy depends on security, privacy, and regulatory requirements.

The principle is:

Noema should be able to determine what AI invocation produced a consequential candidate result.

⸻

39. Provenance

AI provenance should establish the relationship between:

Intent
  ↓
AI Invocation
  ↓
Candidate Result
  ↓
Validation
  ↓
Trust
  ↓
Action

A downstream decision should be traceable to the relevant AI output where that output materially contributed to the decision.

This does not require retaining private model chain-of-thought.

It requires retaining sufficient decision provenance.

⸻

40. Privacy and Data Minimization

The AI Harness should provide only the context required for the model’s task.

Noema should avoid exposing unnecessary:

* personal data
* credentials
* secrets
* business records
* unrelated context
* authorization material
* sensitive system information

Context should therefore be:

Relevant
Scoped
Purpose-bound
Traceable

The Harness should not treat “more context” as universally better.

⸻

41. Secrets

Secrets must not be exposed to models unless explicitly required and permitted by the architecture.

Examples include:

* credentials
* API keys
* private tokens
* signing keys
* passwords
* session secrets

Where a model needs to cause an authenticated operation, authentication should be performed by the system rather than by exposing credentials to the model.

The model should request a capability.

The system should provide the controlled mechanism for invoking it.

⸻

42. Prompt Injection and Untrusted Input

Natural-language content supplied to the model must be treated as potentially untrusted.

This includes:

* user input
* retrieved documents
* web content
* emails
* files
* external system text
* tool output

Untrusted content must not automatically override higher-priority instructions or system constraints.

The Harness should therefore preserve explicit separation between:

System Instructions
Developer / Application Instructions
Task Context
Untrusted Content
Tool Results

The exact hierarchy depends on implementation, but the architectural principle is stable:

Data supplied to a model is not automatically authority over the model.

⸻

43. Tool Output Is Untrusted Input

Tool results may contain arbitrary or malicious text.

Therefore:

Tool Output
    ≠
System Instruction

and:

Retrieved Document
    ≠
Noema Policy

The Harness must preserve the distinction between data and authority.

⸻

44. AI Resource Governance

AI invocation consumes resources.

The Harness may enforce:

* token limits
* time limits
* concurrency limits
* cost limits
* invocation limits
* model-specific quotas
* context limits

Resource limits should be explicit and observable.

Resource exhaustion must produce a defined technical state rather than silently degrading semantic correctness.

⸻

45. AI Safety Boundaries

The AI Harness should enforce the technical constraints necessary to prevent model behavior from bypassing canonical Noema controls.

In particular, the Harness must not allow model output to silently:

* modify Trust state
* grant authorization
* modify policy
* declare evidence authoritative
* mutate business state outside an approved execution path
* redefine canonical Intent semantics
* bypass execution contracts

The Harness is therefore a control boundary, not merely an API wrapper around a model.

⸻

46. AI Evaluation

AI capabilities should be evaluated independently from Trust decisions.

Evaluation may measure:

* interpretation accuracy
* entity extraction accuracy
* ambiguity detection
* clarification quality
* structured output conformance
* retrieval quality
* tool selection
* latency
* cost
* failure rate
* robustness

These measurements describe AI performance.

They do not constitute Trust decisions.

A model with a high evaluation score is not thereby authorized to execute Actions.

⸻

47. Regression Testing

Changes to:

* models
* prompts
* instructions
* retrieval
* context construction
* tools
* schemas
* AI configuration

may alter AI behavior.

The Harness should therefore support repeatable evaluation against representative test cases.

A regression suite may establish:

Input
    ↓
AI Harness
    ↓
Expected Candidate Characteristics

This allows changes to be detected before deployment.

⸻

48. AI Evaluation vs Canonical Validation

These must remain distinct.

AI evaluation asks:

How well did the model perform?

Canonical validation asks:

Is this Intent valid under Noema’s rules?

For example:

AI Evaluation:
95% recipient extraction accuracy
Validation:
recipient reference = INVALID

The second result governs the Intent lifecycle.

AI performance metrics do not override deterministic validation.

⸻

49. AI Evaluation vs Trust

Likewise:

AI Evaluation:
high model reliability
Trust:
authorization denied

The Trust result remains:

BLOCKED

AI quality does not override authority.

⸻

50. Replacement Principle

The AI Harness should allow models to be replaced without redesigning the canonical Noema architecture.

Conceptually:

Model A
   ↓
AI Harness
   ↓
Canonical Noema

can become:

Model B
   ↓
AI Harness
   ↓
Canonical Noema

without changing:

* Intent semantics
* Validation semantics
* Trust semantics
* Action contracts
* Execution boundaries

This makes AI an implementation dependency rather than a canonical semantic dependency.

⸻

51. Multiple Models

Noema may use different models for different tasks.

For example:

Model A → interpretation
Model B → retrieval synthesis
Model C → clarification generation
Model D → planning

The use of multiple models must not create multiple competing semantic authorities.

The canonical Noema representation remains the common boundary.

Multiple Models
       ↓
Canonical Intent / Context / Candidate Results
       ↓
Deterministic Noema

⸻

52. Model Specialization

A model may be selected according to task requirements.

Possible dimensions include:

* latency
* context capacity
* reasoning capability
* language support
* structured output capability
* cost
* availability

Model selection is an implementation concern.

The canonical semantics should not depend on which model happened to be selected.

⸻

53. AI and Human Intervention

AI may determine that clarification or escalation is appropriate.

However, the lifecycle transition belongs to Noema.

For example:

AI:
"Insufficient information to identify recipient."
Noema:
WAITING_FOR_CLARIFICATION

The AI identifies the problem.

Noema owns the state.

Similarly:

AI:
"Potential policy conflict."
Noema:
EVALUATING
        ↓
WAITING_FOR_APPROVAL

The model does not directly mutate Trust state.

⸻

54. AI Cancellation

AI invocations may be cancelled when:

* the Intent changes materially
* the request is withdrawn
* the required context becomes invalid
* a timeout is reached
* a policy prevents continued processing
* the result is no longer required

Cancellation should be represented explicitly.

A cancelled AI invocation must not produce a stale candidate that is silently treated as current.

⸻

55. Stale AI Results

AI results may become stale.

For example:

T1:
AI identifies account balance = ₦100,000
T2:
Balance changes
T3:
AI result is consumed

The old AI output must not automatically be treated as current evidence.

Where freshness matters, Noema should revalidate relevant predicates against authoritative sources.

AI output is contextual and time-bound unless explicitly established otherwise.

⸻

56. AI and Concurrency

Multiple AI invocations may operate concurrently.

For example:

Intent
 ├── Interpretation
 ├── Retrieval
 └── Clarification generation

The Harness should associate each invocation with the relevant Intent version or lifecycle context.

If the Intent changes materially, prior invocation results may become obsolete.

Noema must avoid applying a result generated for an earlier Intent version to a later materially different Intent.

⸻

57. Intent Version Association

Where AI output contributes to Intent processing, the output should be associated with the Intent version against which it was generated.

Conceptually:

Intent v1
   ↓
AI Invocation A
   ↓
Candidate Result A

If the Intent becomes:

Intent v2

then:

Candidate Result A

must not automatically be assumed valid for v2.

This supports deterministic lifecycle management and provenance.

⸻

58. AI Result Acceptance

The Harness may return a candidate result.

The receiving Noema component determines whether that result is accepted.

Conceptually:

AI Result
   ↓
Schema Check
   ↓
Semantic Validation
   ↓
Accept / Reject / Clarify

Acceptance is therefore not implicit in generation.

⸻

59. No Hidden AI Side Effects

AI invocation should not produce untracked business-side effects.

A model may generate:

"Send the email."

but generation itself must not send the email.

Business-side effects must occur through explicit execution mechanisms.

This ensures that:

Generation

and:

Execution

remain distinct operations.

⸻

60. AI as an Internal Capability

Noema may use AI internally without exposing AI-specific semantics to external consumers.

For example:

External Consumer
        ↓
Canonical Intent API
        ↓
Noema
        ↓
AI Harness

The consumer should not need to know which model was used to establish the canonical Intent.

This preserves abstraction boundaries.

⸻

61. AI Harness and Canonical Contracts

The Harness should expose stable contracts to Noema components.

A conceptual contract may be:

InvokeAI(
    task,
    context,
    constraints,
    output_schema
)
→ AIResult

The exact implementation contract is defined elsewhere.

The canonical requirement is that AI invocation be explicit and inspectable.

⸻

62. AI Result Contract

A conceptual AI result may contain:

AIResult {
    invocation_id
    status
    output
    model
    model_version
    provenance
    usage
    errors
}

Where relevant, the result may additionally contain:

uncertainty
tool_calls
citations
context_references

These fields are implementation-level concepts and may evolve.

⸻

63. Deterministic Post-Processing

Where AI output affects consequential Noema state, deterministic post-processing should establish:

* schema validity
* reference validity
* semantic validity
* applicable constraints
* evidence requirements
* state transition eligibility

The model cannot skip this layer.

⸻

64. The AI Harness as a Containment Boundary

The AI Harness should be considered a containment boundary around probabilistic computation.

Inside the boundary:

Model behavior
Prompting
Retrieval
Reasoning
Generation
Tool selection

Outside the boundary:

Canonical Intent
Validation
Trust
Authorization
Execution Contracts
Business Systems

The boundary prevents probabilistic behavior from silently becoming system authority.

⸻

65. Fundamental AI Invariants

The following invariants apply to the AI Harness.

Invariant 1

AI output is not automatically authoritative.

Invariant 2

Model confidence is not Trust.

Invariant 3

Structured model output is not semantic validation.

Invariant 4

The AI Harness does not grant authorization.

Invariant 5

The AI Harness does not own business truth.

Invariant 6

Model-generated Actions are candidates until accepted by deterministic Noema mechanisms.

Invariant 7

AI must not silently bypass execution contracts.

Invariant 8

Material AI inputs and outputs must be traceable where they affect consequential decisions.

Invariant 9

Untrusted model or tool content must not override system authority.

Invariant 10

AI results associated with stale Intent versions must not silently affect newer Intent versions.

Invariant 11

AI failure must not be interpreted as authorization or Trust.

Invariant 12

Model replacement must not require changing canonical Intent or Trust semantics.

Invariant 13

Business-side effects must occur through explicit execution mechanisms.

Invariant 14

AI-generated uncertainty must not be converted into deterministic authority without an explicit rule.

Invariant 15

No AI invocation may silently modify canonical Trust state.

⸻

66. Canonical AI Flow

The canonical AI relationship is:

Human Expression
       ↓
AI Harness
       ↓
Candidate Interpretation
       ↓
Intent Resolution
       ↓
Validation
       ↓
Trust Evaluation
       ↓
Action Selection
       ↓
Execution Contract
       ↓
Execution Consumer
       ↓
Outcome

At any stage where the model or surrounding system cannot establish sufficient grounds to continue:

Clarification
Waiting
Blocking
Human Intervention

may occur.

The AI Harness does not determine these states by itself.

It supplies information to the components that do.

⸻

67. Canonical Mental Model

The AI Harness can be reduced to four responsibilities:

1. Invoke probabilistic intelligence.
2. Bound the information and tools available to that intelligence.
3. Record the provenance of consequential AI computation.
4. Return candidate results to deterministic Noema components.

Therefore:

AI may propose.
AI may interpret.
AI may retrieve.
AI may reason.
AI may plan.
Noema must validate.
Noema must establish Trust.
Noema must enforce authority.
Noema must govern execution.

⸻

68. Final Definition

The AI Harness is Noema’s controlled boundary for invoking probabilistic AI capabilities, providing models with bounded context, instructions, tools, and resources while preserving deterministic control over Intent validation, Trust, authorization, contracts, and execution.

The core invariant is:

Noema may use probabilistic intelligence to understand and propose, but probabilistic model output must never silently become deterministic authority over Intent, Trust, authorization, or business execution.

