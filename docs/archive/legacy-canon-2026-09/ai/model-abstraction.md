Model Abstraction

Status: Foundational
Version: 0.1
Domain: AI
Canonical Path: ai/model-abstraction.md

⸻

1. Definition

Model Abstraction defines the architectural boundary through which Noema interacts with AI models without making any particular model, provider, or model family part of Noema’s core semantic architecture.

Noema should be able to use, evaluate, replace, or combine different AI models while preserving the canonical Intent, Validation, Trust, Contract, and Execution layers.

The core principle is:

Noema depends on model capabilities, not on the identity of a particular model.

Conceptually:

                 Noema
                   │
                   ▼
           Model Abstraction
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
      Model A    Model B    Model C
        │          │          │
     Provider   Provider   Provider

The model is replaceable.

The Noema semantic architecture is not.

⸻

2. Purpose

The Model Abstraction exists to prevent model-specific behavior from becoming coupled to Noema’s canonical architecture.

It provides a stable interface for AI capabilities such as:

* intent generation
* intent interpretation
* entity extraction
* classification
* summarization
* reasoning
* planning
* clarification generation
* structured output generation
* retrieval-assisted reasoning
* other bounded AI tasks

The exact capabilities supported by a deployment may vary.

The abstraction should remain sufficiently general to accommodate different model technologies and providers.

⸻

3. Core Principle

Noema must not define its semantic architecture around:

* one model provider
* one model family
* one model architecture
* one inference API
* one prompting format
* one context-window size
* one tool-calling protocol

Instead:

Noema Semantic Contract
        ↓
Model Abstraction
        ↓
Model Adapter
        ↓
Specific Model / Provider

The adapter translates between Noema’s model interface and the provider-specific interface.

⸻

4. Model Abstraction vs AI Harness

The Model Abstraction and AI Harness are related but distinct.

The Model Abstraction defines:

How Noema conceptually interfaces with an AI model.

The AI Harness defines:

How Noema controls and operates AI inference within the system.

Conceptually:

Noema
  │
  ▼
AI Harness
  │
  ▼
Model Abstraction
  │
  ▼
Model Adapter
  │
  ▼
AI Model

The exact implementation architecture may differ, but the responsibilities should remain distinguishable.

⸻

5. Model Abstraction Does Not Define Trust

The model abstraction must not contain the authoritative Trust model.

A model may return:

confidence = 0.94

but this does not establish:

trust = READY

Likewise, a model may classify an Intent as:

safe

without establishing Noema’s Trust state.

Trust remains a separate deterministic concern.

Therefore:

Model Output
     ≠
Trust Decision

⸻

6. Model Abstraction Does Not Define Intent

The abstraction may support generation or interpretation of Intents, but it does not become the owner of the canonical Intent ontology.

The canonical Intent representation is defined elsewhere.

A model adapter may translate model output into that representation.

It must not redefine the meaning of:

* Actor
* Objective
* Action
* Resource
* Context
* Constraint
* Desired Outcome
* Intent State
* other canonical Intent concepts

The model participates in Intent processing.

Noema owns the semantic contract.

⸻

7. Model Abstraction Does Not Execute Actions

A model interface must not be treated as an execution interface.

For example:

generate()
reason()
classify()
extract()

are AI capabilities.

They are not equivalent to:

transfer_money()
cancel_account()
issue_card()

Business Actions belong to the Capability and Execution layers.

Where a model can invoke tools, tool execution must remain governed by Noema’s execution boundary.

⸻

8. Provider Independence

Noema should avoid embedding provider-specific assumptions in canonical components.

Provider-specific concerns should be isolated behind adapters.

Conceptually:

Noema Model Request
        │
        ▼
Provider Adapter
        │
        ▼
Provider API
        │
        ▼
Provider Model

A change from one provider to another should not require changing:

* the Intent ontology
* Trust semantics
* Validation semantics
* Action Contracts
* canonical state definitions

unless the underlying architectural requirements have genuinely changed.

⸻

9. Model Adapter

A Model Adapter translates between the canonical model interface and a specific model provider.

Conceptually:

ModelAdapter {
    generate(...)
    classify(...)
    embed(...)
    ...
}

The exact interface should be determined by the capabilities Noema actually requires.

An adapter may handle:

* provider authentication
* provider-specific request formats
* response formats
* tool schemas
* structured output formats
* token limits
* provider-specific errors
* provider-specific configuration
* provider-specific streaming

These concerns should remain outside the canonical semantic layer.

⸻

10. Capability-Oriented Model Interface

Noema should reason about model capabilities rather than assuming that every model supports every operation.

Examples of model capabilities include:

TEXT_GENERATION
STRUCTURED_OUTPUT
CLASSIFICATION
EMBEDDING
VISION
AUDIO_TRANSCRIPTION
TOOL_USE
LONG_CONTEXT
REASONING

A deployment may expose only a subset.

The model abstraction should therefore allow Noema to determine whether a model supports the capability required for a particular AI task.

⸻

11. Model Capability Is Not Business Capability

The term “capability” exists at multiple architectural layers and must not be conflated.

A model capability might be:

STRUCTURED_OUTPUT

A business capability might be:

TRANSFER_FUNDS

The first describes what an AI model can compute.

The second describes what an external system can do.

Therefore:

AI Capability
     ≠
Business Capability

The model abstraction must preserve this distinction.

⸻

12. Model Selection

Noema may select different models for different tasks.

For example:

Intent Generation
    → Model A
Classification
    → Model B
Document Extraction
    → Model C

Model selection may consider:

* required capability
* latency
* cost
* context requirements
* quality requirements
* availability
* deployment constraints
* data handling requirements
* evaluation results

The selection mechanism must not redefine canonical Intent or Trust semantics.

⸻

13. Model Selection Is Not Trust Selection

Selecting a model does not select the Trust outcome.

For example:

Model A → candidate Intent
Model B → candidate Intent

does not imply:

Model A → trusted
Model B → untrusted

Both outputs must be processed according to the same authoritative downstream rules.

A model may affect the quality of a candidate.

It does not receive authority to determine execution eligibility.

⸻

14. Model Configuration

A model invocation may include configuration such as:

* temperature
* token limits
* structured output schema
* sampling configuration
* tool availability
* context limits
* response format
* reasoning configuration
* provider-specific parameters

These are inference concerns.

Material configuration should be captured in provenance where necessary to reconstruct an AI-generated result.

⸻

15. Canonical vs Provider-Specific Configuration

Noema should distinguish between:

Canonical configuration

Configuration required by the Noema AI contract.

Examples:

required output schema
task type
allowed tools
required provenance

Provider-specific configuration

Configuration required by a particular model provider.

Examples:

provider-specific parameter
API-specific option
provider-specific response format

Provider-specific configuration should remain isolated from canonical semantics wherever possible.

⸻

16. Structured Output

Where Noema requires machine-readable AI output, the Model Abstraction should support structured output.

Conceptually:

Model Request
    +
Output Schema
    ↓
Structured Model Response

The schema should be derived from the canonical task contract.

For example, Intent Generation may require a Candidate Intent schema.

The model’s adherence to the schema does not establish semantic validity.

The result must still pass deterministic Validation.

⸻

17. Model Output

A model response should conceptually distinguish:

ModelOutput {
    content
    structured_result
    metadata
    usage
    provenance
    status
}

The exact schema is implementation-dependent.

The important principle is that model output should not be treated as an unstructured string when a downstream deterministic component requires a typed result.

⸻

18. Model Metadata

Relevant model metadata may include:

* provider
* model identifier
* model version
* invocation identifier
* timestamp
* configuration
* capability set
* usage information

This metadata supports:

* evaluation
* debugging
* reproducibility
* cost analysis
* auditing
* model comparison
* incident investigation

⸻

19. Model Versioning

Model behavior may change between versions.

Therefore a consequential AI result should be attributable to the model version that produced it.

Conceptually:

model:
    provider/model
version:
    version-id
generation:
    generation-id

This is particularly important when reconstructing why a Candidate Intent or other AI-derived artifact was produced.

⸻

20. Model Replacement

Replacing a model should not require redesigning Noema’s semantic architecture.

For example:

Model A
   ↓
Model Abstraction

may become:

Model B
   ↓
Model Abstraction

without changing:

* Intent semantics
* Validation rules
* Trust state
* Action contracts
* execution boundaries

However, changing model behavior may require re-evaluation of AI-dependent components.

Model replacement is therefore operationally possible but not semantically invisible.

⸻

21. Model Evaluation Before Replacement

A replacement model should be evaluated against the AI tasks for which it will be used.

Relevant dimensions may include:

* Intent generation accuracy
* schema adherence
* ambiguity preservation
* hallucination rate
* extraction accuracy
* latency
* cost
* failure rate
* context utilization
* robustness

The appropriate evaluation depends on the task.

A model must not be considered interchangeable merely because it exposes a compatible API.

⸻

22. Semantic Compatibility

API compatibility is not semantic compatibility.

Two models may both support:

generate()

while producing materially different results.

Therefore:

Interface compatibility
     ≠
Behavioral compatibility
     ≠
Semantic compatibility

Noema should evaluate model behavior at the task level.

⸻

23. Model Routing

Noema may route different requests to different models.

Conceptually:

AI Task
  │
  ▼
Model Router
  │
  ├── Model A
  ├── Model B
  └── Model C

Routing may depend on:

* task
* capability
* context size
* latency requirements
* cost constraints
* availability
* evaluation results
* deployment policy

Routing must not bypass the AI Harness or downstream deterministic controls.

⸻

24. Fallback Models

A fallback model may be used when the primary model is unavailable.

Example:

Primary Model
     │
     ├── available → use
     │
     └── unavailable
              ↓
        Fallback Model

A fallback model’s output remains subject to the same downstream controls.

Availability recovery must not silently change the Trust semantics of an Intent.

If the fallback produces a materially different Intent, that Intent must be evaluated accordingly.

⸻

25. Model Failure

The abstraction must represent model failure explicitly.

Examples include:

* unavailable model
* timeout
* rate limit
* malformed output
* provider failure
* unsupported capability
* context limit
* safety refusal
* infrastructure failure

Model failure must not be interpreted as successful generation.

Nor should it silently become:

READY

The appropriate lifecycle state depends on the surrounding Intent and system conditions.

⸻

26. Retry Semantics

Retries may recover transient model failures.

However, retries should remain observable.

A retry may result in a different probabilistic output.

Therefore a retry should not be treated as equivalent to a deterministic re-evaluation.

Where the resulting candidate differs materially, the downstream lifecycle must process the new candidate appropriately.

⸻

27. Streaming

The Model Abstraction may support streaming responses where useful.

Streaming is an interaction and transport concern.

A partially generated response must not be treated as an authoritative Intent or Action.

For consequential processing:

Partial Model Output
        ↓
Complete / Parse
        ↓
Validate
        ↓
Process

The execution boundary must not be crossed based solely on an incomplete model stream.

⸻

28. Tool Use

Some models may support tool use.

The Model Abstraction may represent tool-use requests and responses.

However, tool invocation must remain governed by Noema’s authority architecture.

Conceptually:

Model
  ↓
Tool Proposal
  ↓
Noema Control Boundary
  ↓
Authorization / Trust / Contract
  ↓
Tool Execution

The model cannot grant itself permission to use a consequential capability.

⸻

29. Context Management

The Model Abstraction may receive context assembled by the AI Harness.

Context may include:

* user expression
* Intent history
* retrieved evidence
* relevant business state
* system instructions
* task constraints
* schema definitions

The abstraction should not assume that all available context is authoritative.

Context provenance must remain available where material.

⸻

30. Context Window Limitations

Different models may support different context limits.

Noema should treat context capacity as a model capability constraint rather than allowing provider-specific limitations to leak into canonical semantics.

If required context cannot be supplied:

Model Capability / Context Constraint
        ↓
AI Task Cannot Be Reliably Performed

The system must not silently omit material context merely to satisfy the model’s limitations.

⸻

31. Data Boundaries

The Model Abstraction must respect the data boundaries established by Noema.

Not all Intent context should necessarily be provided to every model.

The AI Harness and surrounding policy controls should determine:

* what data may be sent
* to which model
* under what conditions
* for what task
* with what retention requirements

The model provider must not become the implicit owner of Noema’s data merely because the data was supplied for inference.

⸻

32. Privacy and Sensitive Context

Where sensitive information is present, model access should be constrained according to applicable system and organizational policy.

The Model Abstraction should support the ability to distinguish:

required context

from:

unnecessary context

Noema should avoid sending information to a model merely because it is available.

Context minimization is part of the model boundary.

⸻

33. Provenance

A model invocation should be attributable where required.

Conceptually:

ModelInvocation {
    invocation_id
    model_id
    model_version
    task
    input_reference
    context_reference
    configuration
    timestamp
    result_reference
}

The exact schema may evolve.

The canonical requirement is that consequential AI-derived artifacts should be reconstructable to the model invocation that produced them.

⸻

34. Observability

The Model Abstraction should support operational observability.

Relevant signals may include:

* invocation count
* latency
* failures
* retries
* token or resource usage
* model selection
* output validation failures
* fallback frequency
* task-level evaluation results

Observability should support system operation without turning private model reasoning into an architectural dependency.

⸻

35. No Hidden Authority

The Model Abstraction must not contain hidden authority mechanisms.

For example, a model response must not implicitly establish:

authorized = true

merely because the provider returned a successful response.

Likewise:

tool_call = transfer_money

must not itself constitute authorization to execute the transfer.

Model output is an input to Noema’s control system.

It is not the control system.

⸻

36. Model Confidence

If a model provides confidence information, Noema may preserve it as model metadata.

However, confidence must not become an implicit execution threshold unless an explicit canonical specification defines how it participates in a deterministic process.

Even then, confidence would be one input to that rule rather than equivalent to Trust.

The default principle is:

Model confidence
      ↓
Evidence about model behavior

not:

Model confidence
      ↓
Authority

⸻

37. Model Abstraction and Determinism

AI inference itself may be nondeterministic.

The Model Abstraction therefore does not require every invocation to produce identical output.

Instead, it must preserve the deterministic boundaries around AI output.

Conceptually:

Probabilistic Model
        ↓
Model Output
        ↓
Deterministic Parsing
        ↓
Validation
        ↓
Trust

Noema’s authoritative state transitions must remain governed by explicit rules.

⸻

38. Model Abstraction and Evaluation

Every model used in a consequential Noema workflow should be evaluable independently of the production Trust system.

The evaluation layer may measure:

* task accuracy
* schema conformance
* robustness
* hallucination
* ambiguity handling
* latency
* cost
* failure characteristics
* consistency

Evaluation results describe model performance.

They do not become Trust decisions.

⸻

39. Multiple Models

Noema may use multiple models within one Intent lifecycle.

For example:

Intent Generation
      ↓
Model A
Entity Resolution Assistance
      ↓
Model B
Clarification Generation
      ↓
Model C

Each model’s output should remain attributable to its respective invocation.

Noema should not assume that one model’s output validates another model’s output.

Deterministic components remain responsible for establishing canonical state.

⸻

40. Model Chaining

Model outputs may be supplied as inputs to subsequent models.

For example:

Model A
  ↓
Candidate Intent
  ↓
Model B
  ↓
Candidate Clarification

This can improve AI workflows but increases the importance of provenance and output boundaries.

A model-generated artifact should remain distinguishable from authoritative facts and deterministic system state throughout the chain.

⸻

41. Model Consensus

Multiple models may independently produce candidate interpretations.

Conceptually:

Model A → Candidate A
Model B → Candidate B
Model C → Candidate C

Agreement may provide useful evidence about generation quality.

However, model consensus is not inherently authoritative.

Three models agreeing on an incorrect interpretation does not make that interpretation true.

Where semantic certainty is consequential, Noema must rely on authoritative evidence, deterministic rules, or clarification as appropriate.

⸻

42. Provider Failure and Business Failure

A model-provider failure must remain distinct from an execution failure.

For example:

Model unavailable

is not:

Payment execution failed

Similarly:

Model generated invalid output

is not:

External system rejected the transaction

Noema should preserve these distinctions in state and provenance.

⸻

43. Model Abstraction Contract

Conceptually:

Model(
    task,
    input,
    context,
    configuration
)
→ ModelResult

The contract should define:

* accepted task types
* supported inputs
* context requirements
* output format
* model metadata
* failure semantics
* provenance
* capability requirements

The exact API is an implementation concern.

The canonical abstraction is the separation between Noema semantics and provider-specific inference.

⸻

44. Example

Intent Generation requires a model capable of structured output.

Noema requests:

Task:
    INTENT_GENERATION
Schema:
    CandidateIntent
Context:
    authorized_context

The model provider returns:

CandidateIntent {
    action: TRANSFER
    recipient: John
    amount: 50000
}

The Model Abstraction records:

model:
    model-A
version:
    vX
invocation:
    invocation-123

The result then enters:

Intent Resolution
        ↓
Validation
        ↓
Trust

The model itself does not establish that the transfer is authorized or executable.

⸻

45. Example: Provider Replacement

Initial deployment:

Intent Generation
    ↓
Model A

Later:

Intent Generation
    ↓
Model B

The canonical Intent schema remains unchanged.

The Validation layer remains unchanged.

The Trust State Machine remains unchanged.

The Execution Contract remains unchanged.

Only the model adapter and relevant AI evaluation may change.

This is the intended architectural property of the abstraction.

⸻

46. Example: Fallback

Primary model:

Model A

becomes unavailable.

Noema routes the task to:

Model B

Model B generates a Candidate Intent.

The candidate does not inherit the authority of the failed Model A invocation.

It must proceed through the same downstream lifecycle:

Candidate
   ↓
Resolution
   ↓
Validation
   ↓
Trust

⸻

47. Anti-Patterns

The following patterns violate the Model Abstraction boundary.

47.1 Provider-Coupled Canon

Embedding a specific provider’s API directly into canonical Intent or Trust semantics.

47.2 Model-As-Authority

Treating a model’s confidence or response as authorization.

47.3 Model-As-System-of-Record

Treating model memory or generated values as authoritative business state.

47.4 Direct Model Execution

Allowing model output to invoke consequential Actions without the Noema execution boundary.

47.5 Hidden Provider Semantics

Allowing provider-specific behavior to silently alter canonical Intent semantics.

47.6 API Compatibility Assumption

Assuming that two models are interchangeable because they expose similar APIs.

47.7 Silent Fallback

Switching models without recording the model responsible for a consequential AI-derived artifact.

⸻

48. Model Abstraction Invariants

Invariant 1

Noema’s canonical semantics must not depend on a specific model provider.

Invariant 2

Model capability and business capability are distinct.

Invariant 3

Model output is not Trust.

Invariant 4

Model confidence is not authorization.

Invariant 5

Model output must not directly execute consequential Actions.

Invariant 6

Provider-specific behavior must remain behind an adapter boundary.

Invariant 7

Consequential model outputs must be attributable to the model and relevant version.

Invariant 8

Model replacement must preserve the canonical Noema semantic interfaces.

Invariant 9

API compatibility does not establish semantic compatibility.

Invariant 10

Model failures must remain distinct from business execution failures.

Invariant 11

Fallback models remain subject to the same downstream controls.

Invariant 12

Model consensus does not independently establish truth.

Invariant 13

Model-generated information must remain distinguishable from authoritative external state.

Invariant 14

AI inference may be probabilistic; authoritative Noema state transitions must remain deterministic.

Invariant 15

The Model Abstraction must not silently create authority that is not defined elsewhere in Noema.

⸻

49. Canonical Architecture

The canonical relationship is:

                         Noema
                           │
             ┌─────────────┴─────────────┐
             │                           │
       Canonical Semantics          AI Harness
             │                           │
     ┌───────┼────────┐                  ▼
     │       │        │          Model Abstraction
  Intent  Validation Trust              │
                                         ▼
                                  Model Adapter(s)
                                         │
                           ┌─────────────┼─────────────┐
                           ▼             ▼             ▼
                        Model A       Model B       Model C

The important boundary is:

Noema Semantics
      ≠
Model Implementation

The abstraction allows AI to participate without allowing model implementation details to become canonical Noema semantics.

⸻

50. Canonical Mental Model

Model Abstraction can be reduced to four questions:

1. What AI capability does Noema require?
2. Which model can provide that capability?
3. How is the model invocation isolated from canonical Noema semantics?
4. How is the model output passed back into deterministic Noema processing?

Which produces:

AI Requirement
      ↓
Capability
      ↓
Model Selection
      ↓
Model Adapter
      ↓
Model
      ↓
Model Output
      ↓
Validation / Resolution / Trust

⸻

51. Final Definition

Model Abstraction is the architectural boundary that allows Noema to use interchangeable AI models and providers while preserving stable canonical semantics for Intent, Validation, Trust, Authority, Capability, Contracts, and Execution.

The central invariant is:

Noema may change the model without changing what Noema means by Intent, Trust, Authority, or Execution. The model supplies probabilistic computation; Noema retains semantic and execution authority.