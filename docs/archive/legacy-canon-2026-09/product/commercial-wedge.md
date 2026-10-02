Commercial Wedge

Status: Foundational
Version: 0.2
Domain: Product
Canonical Path: product/commercial-wedge.md

⸻

1. Definition

A Commercial Wedge is the smallest concrete enterprise problem through which Noema can demonstrate meaningful customer value while exercising a material portion of its intent-to-execution architecture.

The Commercial Wedge answers:

What specific enterprise problem gives a customer a reason to adopt Noema?

Noema is a general-purpose intent execution system. The Commercial Wedge is therefore not the definition of Noema and does not constrain the platform to a single workflow or industry.

It is the concrete entry point through which the platform’s capabilities become commercially demonstrable.

A valid wedge connects:

Enterprise Problem
       ↓
Commercial Wedge
       ↓
Noema Capabilities
       ↓
Execution
       ↓
Verified Outcome
       ↓
Customer Value

⸻

2. Purpose

The purpose of the Commercial Wedge is to establish a concrete relationship between Noema’s architectural capabilities and an enterprise problem that is sufficiently valuable to solve.

Without a wedge:

Noema
   ↓
General Infrastructure
   ↓
"What should we use it for?"

With a wedge:

Enterprise Pain
      ↓
Concrete Workflow
      ↓
Noema
      ↓
Measurable Improvement

The wedge therefore provides:

* an initial customer problem;
* a concrete adoption entry point;
* an environment in which Noema’s architecture can be validated;
* measurable operational and economic outcomes;
* a path toward adjacent workflows.

⸻

3. Commercial Wedge Is Not Noema

The wedge must remain distinct from the underlying platform.

For example:

Card Replacement

may be a Commercial Wedge.

That does not make Noema:

A Card Replacement Product

The underlying Noema capability remains:

Human Intent
      ↓
Intent Resolution
      ↓
Context
      ↓
Trust
      ↓
Action
      ↓
Execution
      ↓
Outcome

The wedge is the problem through which these capabilities are exercised.

Therefore:

Commercial Wedge ≠ Noema Product
Commercial Wedge ≠ Noema Architecture
Commercial Wedge = Concrete Enterprise Entry Point

⸻

4. Real Enterprise Problem

A Commercial Wedge must correspond to a real enterprise workflow or a validated representation of one.

It should not be selected merely because:

* an API exists;
* an LLM can perform the task;
* the workflow is technically interesting;
* the workflow makes a compelling demo;
* automation is possible.

The problem should exist independently of Noema.

The basic sequence is:

Existing Enterprise Problem
          ↓
Existing Operational Friction
          ↓
Existing Workflow
          ↓
Noema Opportunity

The wedge therefore begins with the customer’s problem rather than with a Noema feature looking for a use case.

⸻

5. Frequency

Frequency is one dimension of wedge value.

A workflow that occurs frequently can create cumulative operational cost through:

* human handling time;
* repetitive actions;
* system switching;
* support volume;
* processing delays;
* operational errors.

Frequency alone does not establish wedge quality.

A low-frequency workflow may still be commercially meaningful where each occurrence has sufficiently high consequence or value.

Therefore:

Commercial Value
≠ Frequency Alone

Frequency must be evaluated together with pain, consequence, economic value, and Noema differentiation.

⸻

6. Operational Pain

The workflow should contain meaningful operational friction.

Relevant forms of friction include:

* repeated manual work;
* system switching;
* policy lookup;
* identity resolution;
* approval coordination;
* repetitive data entry;
* exception handling;
* slow execution;
* operational errors;
* fragmented enterprise systems.

The wedge should make the existing cost or friction observable enough to establish a meaningful baseline.

⸻

7. Intent-Native Workflow

A particularly relevant Commercial Wedge begins with a human expression of desired outcome rather than an already structured enterprise command.

Example:

“I need a replacement for my expired card.”

The enterprise may require:

customer_id
card_id
replacement_reason
eligibility
authorization
delivery_address

The user may provide none of these explicitly.

Noema operates between:

Human Intent
      ↓
Executable Enterprise Action

The wedge is particularly relevant where the transformation requires semantic resolution, contextual grounding, deterministic authorization, and safe execution.

⸻

8. Structured Automation vs Intent Execution

A workflow that already has a complete deterministic interface may provide limited evidence of Noema’s differentiated value.

For example:

POST /cards/123/replace

may already represent a directly executable operation.

The harder problem may be:

“Replace my card.”

Noema may need to establish:

* which actor is requesting the operation;
* which Resource is intended;
* what the user means;
* whether the requested operation is supported;
* whether the Resource is eligible;
* whether the Actor has the required Authority;
* which Policy and Constraints apply;
* whether additional information is required;
* whether execution can safely proceed.

The Commercial Wedge should expose this distinction where it exists.

⸻

9. Multi-System Coordination

A strong wedge may cross multiple enterprise systems.

For example:

Identity System
      ↓
Customer System
      ↓
Resource System
      ↓
Risk System
      ↓
Policy / Authorization Systems
      ↓
Execution System
      ↓
Verification / System of Record

The value is not simply the number of integrations.

The relevant question is whether Noema must coordinate information and execution across existing enterprise boundaries in order to safely fulfill the Intent.

A workflow contained entirely within one simple deterministic interface may provide less evidence of this capability.

⸻

10. Enterprise Context

The workflow should require enterprise context beyond the user’s immediate utterance where the problem naturally demands it.

For example:

“I need a replacement card.”

may require:

Actor Identity
Resource Identity
Resource State
Account State
Eligibility
Policy
Authority
Organization / Tenant
Risk Context
Execution Preconditions

Noema’s role is to resolve the context necessary for a trustworthy execution decision.

⸻

11. Ambiguity

A commercially relevant intent workflow may contain legitimate ambiguity.

Examples:

“Replace my card.”

Which card?

“Send it to my office.”

Which office?

“Cancel the account.”

Which account?

Ambiguity is not inherently a system failure.

The system must determine whether an ambiguity is:

* irrelevant to execution;
* resolvable from authoritative context;
* clarification-required;
* policy-sensitive;
* execution-blocking.

⸻

12. Ambiguity Must Not Become Guessing

The Commercial Wedge must preserve Noema’s deterministic execution boundary.

The system must not convert unresolved ambiguity into execution merely to increase automation rates.

The intended pattern is:

Ambiguity
    ↓
Resolution
    ↓
Resolved
    │
    └── unresolved → Clarification / Escalation

not:

Ambiguity
    ↓
Best Guess
    ↓
Execution

Commercial success must not depend on weakening the Trust boundary.

⸻

13. Policy Sensitivity

A relevant Commercial Wedge should expose enterprise Policy where Policy materially affects execution.

Examples include:

* eligibility;
* approval requirements;
* organizational rules;
* transaction limits;
* regulatory constraints;
* risk thresholds;
* data-access restrictions.

Conceptually:

Intent
  +
Context
  +
Policy
  +
Authority
  +
State
  ↓
Trust Decision

Policy remains a governing semantic concept rather than being reduced to arbitrary workflow logic.

⸻

14. Authorization

Where the workflow has meaningful permission boundaries, Authority must be evaluated explicitly.

Example:

“Increase the transfer limit.”

Noema may need to establish:

Actor
Resource
Requested Operation
Authority
Applicable Scope
Policy
Required Approval

The existence of an Intent does not establish Authority.

Likewise, access to a Resource does not automatically establish authority to perform every operation against it.

⸻

15. Risk and Consequence

Commercial relevance may increase where incorrect execution has meaningful consequences.

Examples include:

* financial transactions;
* account changes;
* access changes;
* sensitive data operations;
* customer operations;
* organizational actions.

The purpose is not to maximize risk.

Rather, consequential workflows make the distinction between:

Model Interpretation

and:

Deterministic Execution Decision

particularly important.

⸻

16. Execution Complexity

The wedge should demonstrate the relevant execution lifecycle rather than merely language interpretation.

Where applicable:

Intent
   ↓
Resolution
   ↓
Context
   ↓
Evidence
   ↓
Trust
   ↓
Planning
   ↓
Action Contract
   ↓
Execution
   ↓
Verification
   ↓
Outcome

Not every wedge requires every stage in identical form.

The Commercial Wedge should exercise the stages that are materially required by the actual enterprise workflow.

⸻

17. Measurable Outcome

A wedge must permit meaningful measurement.

Potential measurements include:

* execution time;
* human handling time;
* automation rate;
* clarification rate;
* escalation rate;
* failure rate;
* error rate;
* completion rate;
* cost per execution;
* customer response time;
* exception rate.

The baseline should be established before claiming improvement.

Conceptually:

Baseline Workflow
       ↓
Measurement
       ↓
Noema Workflow
       ↓
Measurement
       ↓
Comparable Outcome

⸻

18. Economic Value

The wedge must address a problem with sufficient economic significance for the target customer.

Potential sources of value include:

Less Manual Work
       +
Faster Execution
       +
Fewer Errors
       +
Higher Appropriate Automation
       +
Lower Operational Cost
       +
Reduced Support Burden

The precise economic model is customer- and workflow-specific.

The foundational principle is:

The wedge must solve a problem whose value can be demonstrated in economic or operational terms.

⸻

19. Noema Differentiation

A Commercial Wedge should provide a meaningful opportunity to demonstrate why Noema is required rather than ordinary deterministic automation.

A useful diagnostic is:

Can the workflow be reliably completed through:
One deterministic interface
+
Known parameters
+
Fixed business logic
+
No material intent ambiguity
+
No material context resolution
+
No consequential Trust decision?

If so, the workflow may still be useful, but it provides weaker evidence of Noema’s differentiated capability.

A more representative wedge may require a combination of:

Intent
+
Context
+
Resource Resolution
+
State
+
Ambiguity
+
Policy
+
Authority
+
Evidence
+
Action
+
Verification

Not every dimension is mandatory. The relevant requirement is that the workflow exercise capabilities that are genuinely difficult to reduce to simple deterministic automation.

⸻

20. Wedge as Architectural Proof

The Commercial Wedge provides an empirical environment in which portions of Noema’s architecture can be tested.

For example:

Intent
   ↓
Context
   ↓
Evidence
   ↓
Resource / State Resolution
   ↓
Trust
   ↓
Action Contract
   ↓
Execution
   ↓
Postcondition Verification
   ↓
Outcome

A successful implementation therefore demonstrates more than that Noema can call an enterprise API.

It demonstrates that Noema can safely move from human Intent to verified enterprise execution under real operating conditions.

⸻

21. Wedge vs Demo

A demo demonstrates technical possibility.

A Commercial Wedge demonstrates a real customer problem and measurable value.

Demo
→ "Noema can do this."
Commercial Wedge
→ "This enterprise problem is sufficiently valuable to solve through Noema."

A demo may be synthetic.

A wedge should be grounded in an actual customer workflow, operational evidence, or a validated representation of one.

⸻

22. Wedge vs Feature

A feature or primitive is a capability within the Noema platform.

Examples:

Action Contracts
→ Platform Primitive
Ambiguity Resolution
→ Platform Capability
Policy Evaluation
→ Platform Capability
Card Replacement Workflow
→ Commercial Wedge

The wedge combines Noema capabilities to address a customer problem.

Therefore:

Primitive
   ↓
Capabilities
   ↓
Workflow
   ↓
Commercial Wedge

⸻

23. Reusable Primitives

The wedge should produce reusable platform capabilities rather than isolated bespoke automation.

For example:

Initial Workflow
      ↓
Identity Resolution
      ↓
Resource Resolution
      ↓
Ambiguity Handling
      ↓
Policy Evaluation
      ↓
Authority Evaluation
      ↓
Action Contracts
      ↓
Execution
      ↓
Outcome Verification

Where these capabilities generalize beyond the initial workflow, they should become reusable Noema primitives.

This prevents the wedge from becoming a collection of customer-specific scripts.

⸻

24. Wedge Expansion

A successful wedge may establish an expansion path into adjacent workflows.

For example:

Card Operation
      ↓
Additional Card Operations
      ↓
Account Operations
      ↓
Customer Operations
      ↓
Broader Enterprise Operations

The exact path is enterprise-specific.

The platform principle is:

Each subsequent workflow should reuse an increasing amount of the existing Noema execution substrate where the underlying semantics are shared.

Expansion should therefore follow demonstrated customer need rather than an assumption that every adjacent workflow must be built.

⸻

25. Enterprise System Boundaries

The Commercial Wedge must preserve the distinction between Noema’s execution state and enterprise Business State.

Noema should not become the System of Record merely to simplify implementation of the initial workflow.

For example:

Enterprise System
→ owns Account State
Noema
→ owns Intent / Trust / Action / Execution / Outcome state

Where an enterprise system is authoritative for a domain fact, Noema should resolve against that authority rather than silently creating a competing source of truth.

⸻

26. Enterprise Systems

The wedge should generally operate with existing enterprise systems rather than require their replacement.

Conceptually:

Human Intent
      ↓
    Noema
      ↓
Enterprise Systems

Noema coordinates intent resolution and execution across the enterprise environment.

It does not require migration of every underlying System of Record into Noema.

⸻

27. Noema Execution State

Noema may maintain canonical state concerning its own execution lifecycle, including:

* Intent;
* resolution;
* Trust decision;
* Action;
* execution;
* intervention;
* Outcome;
* verification.

The enterprise remains authoritative for its own business state.

Therefore:

Enterprise Canonical Business State
              +
Noema Canonical Execution State

can coexist without creating competing authority.

⸻

28. Failure Handling

A real Commercial Wedge must include realistic failure conditions.

Examples:

* enterprise system unavailable;
* Action rejected;
* timeout;
* authorization expired;
* Policy changed;
* Resource State changed;
* external dependency failed;
* partial execution;
* postcondition not satisfied.

The wedge should demonstrate controlled failure behavior rather than assuming successful execution.

In particular:

Failure
  ≠
Uncontrolled Retry

and:

Action Accepted
  ≠
Intent Satisfied

where postcondition verification shows otherwise.

⸻

29. Human Intervention

Human intervention is a legitimate execution state.

Depending on the workflow, Noema may need to:

Execute
Clarify
Escalate
Reject

A Commercial Wedge should demonstrate appropriate transitions between these states where required.

Human intervention is therefore not inherently evidence of failed automation.

The relevant question is whether Noema can determine when autonomous execution is inappropriate and route the case accordingly.

⸻

30. Outcome Verification

The wedge should establish observable postconditions where the workflow requires them.

Example:

Action:
replace_card
Expected Postcondition:
card.status = REPLACEMENT_REQUESTED

Noema should verify the relevant authoritative enterprise state where required.

The intended sequence is:

Intent
   ↓
Action
   ↓
Execution
   ↓
Verification
   ↓
Outcome

rather than:

Intent
   ↓
API Call
   ↓
Assumed Success

⸻

31. Auditability

Consequential workflows should preserve sufficient execution history to answer:

* What did the user request?
* What Intent was resolved?
* Which Resource was identified?
* What Context was used?
* What Evidence was available?
* Which Policy applied?
* Which Authority was established?
* Why was execution permitted or blocked?
* Which Action was executed?
* What happened?
* What Outcome was observed?
* Did the resulting state satisfy the intended postcondition?

Auditability is therefore part of the wedge’s enterprise viability, not merely a reporting feature.

⸻

32. Data Boundaries

The wedge should require only the data necessary for the workflow.

For example, a card-replacement workflow may require:

customer_id
card_id
card_state
eligibility
delivery_information

It should not require unrelated enterprise data merely because that data is technically accessible.

The wedge should therefore preserve:

Least Privilege
+
Purpose Limitation
+
Data Minimization

Data access should remain bounded by the requirements of the workflow.

⸻

33. Commercial Wedge and Trust

The Commercial Wedge provides the concrete environment in which Noema’s Trust model demonstrates practical value.

Conceptually:

Commercial Problem
       ↓
Intent
       ↓
Context
       ↓
Evidence
       ↓
Trust
       ↓
Action
       ↓
Execution
       ↓
Verified Outcome

Trust is therefore not an isolated commercial feature.

It is part of the mechanism through which Noema converts uncertain human requests into controlled enterprise execution.

⸻

34. Commercial Wedge and Determinism

The Model may be probabilistic in its interpretation.

The final execution decision must be grounded in canonical Noema semantics.

Model
  ↓
Interpretation / Proposal
  ↓
Canonical Resolution
  ↓
Deterministic Trust Evaluation
  ↓
Execute / Clarify / Escalate / Reject

The wedge must not depend on:

“Probably correct.”

as a sufficient condition for consequential execution.

⸻

35. Commercial Wedge and Intent

The wedge should begin with a human Intent and terminate in an observable Outcome.

Human Intent
      ↓
Resolved Intent
      ↓
Trusted Action
      ↓
Enterprise Execution
      ↓
Verified Outcome

This gives the customer a concrete demonstration of Noema’s central proposition:

Human intent can be converted into controlled enterprise execution without treating model interpretation as authority to act.

⸻

36. Commercial Wedge and Action Contracts

Where execution is supported by Action Contracts, the wedge should use explicit contracts rather than opaque model-generated operations.

Conceptually:

Action Contract
├── Action
├── Inputs
├── Preconditions
├── Required Authority
├── Applicable Policy
├── Constraints
└── Expected Postconditions

This provides a deterministic boundary between:

Intent Interpretation

and:

Enterprise Execution

The wedge should demonstrate that distinction in practice.

⸻

37. Commercial Wedge and Enterprise Ownership

The fundamental ownership boundary is:

Noema executes against enterprise state.
Noema does not silently become the owner of enterprise business state.

For example:

Payment System
→ authoritative for payment status
Noema
→ authoritative for its execution journey

The commercial implementation must preserve this distinction even where creating a shadow copy of enterprise state would appear operationally convenient.

⸻

38. Wedge Selection Dimensions

Candidate wedges should be assessed across relevant dimensions:

Dimension	Question
Pain	Is there meaningful operational friction?
Frequency	Does the workflow occur often enough to matter, or is each occurrence sufficiently consequential?
Intent	Does the workflow naturally begin with human intent?
Ambiguity	Are there meaningful ambiguities that require resolution?
Context	Is enterprise context necessary?
Resource	Must Noema identify or operate on consequential Resources?
State	Does current or historical State affect execution?
Policy	Do enterprise rules materially affect execution?
Authority	Are permission boundaries meaningful?
Evidence	Does execution depend on authoritative evidence?
Coordination	Does the workflow cross enterprise capabilities or systems?
Risk	Are incorrect actions consequential enough to require controlled execution?
Outcome	Can completion and postconditions be observed?
Economic Value	Can customer value be measured?
Reusability	Can the resulting capabilities support adjacent workflows?

These dimensions are selection criteria, not a universal scoring formula.

Different enterprises will weight them differently.

⸻

39. Wedge Failure Conditions

A candidate may provide weak evidence for the Noema Commercial Wedge when:

* the workflow is trivial;
* one deterministic API call solves the problem;
* the necessary parameters are already known;
* no meaningful Intent interpretation is required;
* no meaningful enterprise Context is required;
* Resource resolution is unnecessary;
* State does not materially affect execution;
* ambiguity is absent or inconsequential;
* Policy has little relevance;
* Authority is irrelevant;
* failure has negligible consequences;
* the economic value is insignificant;
* the workflow cannot generalize beyond bespoke implementation;
* Noema must own enterprise Business State to make the workflow work.

Such workflows may still be valuable engineering exercises or product features.

They simply provide less evidence for the specific commercial thesis represented by the wedge.

⸻

40. Smallest Real Problem

The Commercial Wedge should be the smallest real problem that demonstrates a meaningful portion of Noema’s thesis.

Conceptually:

Minimize
    Workflow Scope
Maximize
    Meaningful Noema Capability Demonstrated

The goal is not to automate an entire enterprise domain at launch.

The goal is to solve one sufficiently valuable workflow end-to-end while establishing reusable infrastructure.

⸻

41. Commercial Wedge and Platform Expansion

The intended progression is:

One Real Enterprise Problem
          ↓
Commercial Wedge
          ↓
Reusable Noema Primitives
          ↓
Adjacent Workflows
          ↓
Multiple Enterprise Domains
          ↓
Broader Intent Execution Layer

The wedge is therefore the first commercial boundary, not the final product boundary.

⸻

42. Wedge Validation

A Commercial Wedge is sufficiently validated when evidence establishes that:

1. A real enterprise problem exists.
2. The existing workflow has measurable cost, friction, delay, risk, or other material consequence.
3. Users naturally express the desired outcome as Intent, where applicable.
4. The workflow requires meaningful enterprise Context.
5. Resource or Entity resolution matters where applicable.
6. State materially affects execution where applicable.
7. Policy or Authority affects execution where applicable.
8. Multiple enterprise capabilities or systems participate where applicable.
9. Noema can establish whether execution is permitted.
10. Noema can execute through explicit Action Contracts where applicable.
11. Relevant postconditions can be verified.
12. Exceptions can be handled safely.
13. Human intervention can occur where appropriate.
14. Customer value can be measured against a baseline.
15. Reusable Noema capabilities emerge from the implementation.
16. Adjacent workflow expansion is supported by demonstrated customer need.

Validation is therefore evidence-based rather than determined by whether the workflow makes an impressive demonstration.

⸻

43. Commercial Wedge Invariants

Invariant 1

The Commercial Wedge must correspond to a real enterprise problem.

Invariant 2

The Commercial Wedge must provide measurable customer value or establish a credible path to measuring it.

Invariant 3

The Commercial Wedge is an entry point into Noema, not the definition of Noema.

Invariant 4

A workflow does not become a Commercial Wedge merely because it can be automated.

Invariant 5

The wedge should exercise meaningful Noema capabilities.

Invariant 6

Ambiguity must not be converted into unsafe execution merely to increase automation.

Invariant 7

The wedge must preserve the deterministic Trust boundary.

Invariant 8

The wedge must preserve enterprise ownership of Business State.

Invariant 9

Enterprise Systems of Record remain authoritative for their respective domains.

Invariant 10

Consequential execution should use explicit Action Contracts or equivalent deterministic execution boundaries.

Invariant 11

Consequential execution remains subject to applicable Policy, Authority, Constraints, State, and Evidence.

Invariant 12

The wedge should produce observable and verifiable Outcomes where the workflow requires them.

Invariant 13

Failure, clarification, escalation, rejection, and human intervention are valid execution states where appropriate.

Invariant 14

The wedge should produce reusable capabilities rather than isolated bespoke automation.

Invariant 15

Expansion beyond the initial wedge should follow demonstrated customer need and reuse the existing execution substrate where appropriate.

Invariant 16

The smallest useful initial workflow is preferred over unnecessarily broad product scope.

Invariant 17

Commercial pressure must not cause Noema to violate its architectural ownership, Trust, or execution boundaries.

Invariant 18

The strongest wedges demonstrate both customer value and meaningful Noema differentiation.

⸻

44. Canonical Commercial Wedge Model

The Commercial Wedge can be represented as:

Enterprise Problem
        │
        ▼
Commercial Wedge
        │
        ▼
Human Intent
        │
        ▼
Intent Resolution
        │
        ├──────────► Context
        │
        ├──────────► Evidence
        │
        ├──────────► Resource
        │
        └──────────► State
                    │
                    ▼
              Trust Evaluation
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       Execute   Clarify   Escalate
          │
          ▼
     Action Contract
          │
          ▼
      Execution
          │
          ▼
     Verification
          │
          ▼
       Outcome
          │
          ▼
    Measurable Value

The exact path depends on the workflow.

The important property is that the wedge demonstrates a controlled transition from enterprise problem to verified value.

⸻

45. Final Definition

A Commercial Wedge is the smallest real enterprise problem through which Noema can demonstrate measurable customer value while exercising the relevant portions of its intent, context, resolution, Trust, action, execution, and verification capabilities.

The fundamental relationship is:

Enterprise Problem
       ↓
Commercial Wedge
       ↓
Human Intent
       ↓
Resolution
       ↓
Context + Evidence + Resource + State
       ↓
Trust
       ↓
Action Contract
       ↓
Execution
       ↓
Verified Outcome
       ↓
Measurable Customer Value

The wedge gets Noema into the enterprise.

The reusable execution primitives create the broader platform.

Therefore:

The Commercial Wedge is not what Noema is. It is the concrete enterprise problem through which the customer discovers the value of Noema’s intent-to-execution architecture.