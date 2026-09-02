Commercial Wedge

Status: Foundational
Version: 0.1
Domain: Product
Canonical Path: product/commercial-wedge.md

⸻

1. Definition

A Commercial Wedge is the smallest concrete enterprise problem through which Noema can demonstrate meaningful customer value while exercising its core intent-to-execution capabilities.

The Commercial Wedge answers:

“What specific enterprise problem gives a customer a reason to adopt Noema?”

Noema is a general-purpose intent execution system.

However, enterprises do not adopt general-purpose infrastructure merely because the abstraction is technically valuable.

They adopt it because a specific problem is:

* expensive
* repetitive
* operationally painful
* difficult to automate safely
* dependent on multiple systems
* governed by enterprise policy
* suitable for measurable improvement

The Commercial Wedge provides the initial entry point.

It is not the boundary of the Noema platform.

⸻

2. Purpose

The purpose of the Commercial Wedge is to connect Noema’s architectural capabilities to a concrete enterprise problem.

Without a wedge:

Noema
   ↓
General infrastructure
   ↓
"What should we use it for?"

With a wedge:

Enterprise Problem
       ↓
Commercial Wedge
       ↓
Noema
       ↓
Measurable Outcome

The wedge therefore provides:

* initial customer value
* product validation
* architectural validation
* an adoption entry point
* a path toward broader workflow expansion

⸻

3. Commercial Wedge vs Product

The Commercial Wedge is not the Noema product.

For example:

Card Renewal

may be an initial Commercial Wedge.

Noema is not therefore:

A card-renewal product

The underlying Noema capability is:

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

The workflow demonstrates the capability.

The capability enables additional workflows.

Therefore:

Wedge ≠ Product

⸻

4. The Wedge Must Represent a Real Problem

A Commercial Wedge must correspond to an actual enterprise workflow.

It should not be created merely because:

* an API exists
* an LLM can perform the task
* the workflow is technically interesting
* the workflow makes a good demo
* automation is possible

The problem must exist independently of Noema.

A valid wedge begins with:

Existing Enterprise Pain
        ↓
Existing Operational Cost
        ↓
Existing Workflow
        ↓
Noema Opportunity

⸻

5. Frequency

A strong Commercial Wedge should occur frequently enough to create meaningful cumulative cost.

High-frequency workflows create opportunities to reduce:

* human handling time
* operational workload
* response time
* support volume
* repetitive actions
* processing cost

A theoretically valuable workflow with negligible frequency may not provide sufficient commercial leverage.

⸻

6. Pain

The workflow should contain meaningful operational friction.

Examples include:

* repeated manual work
* system switching
* policy lookup
* identity resolution
* approval coordination
* exception handling
* repetitive data entry
* slow execution
* operational errors

The greater the existing friction, the stronger the economic justification for Noema.

⸻

7. Intent-Native Workflows

The strongest Commercial Wedge begins with human intent.

Example:

“I need a replacement for my expired card.”

The enterprise systems may require:

customer_id
card_id
replacement_reason
eligibility
authorization
delivery_address

The user does not necessarily provide these as structured parameters.

Noema exists between:

Human Intent

and:

Executable Enterprise Action

⸻

8. Structured Automation vs Intent Execution

A workflow that already has a deterministic structured interface may not require Noema.

For example:

POST /cards/123/replace

is already executable.

The difficult problem may instead be:

"Replace my card."

because Noema must determine:

* which user
* which card
* whether replacement is intended
* whether replacement is permitted
* why replacement is required
* whether additional information is necessary
* whether execution is safe

The Commercial Wedge should expose this difference.

⸻

9. Multi-System Requirement

A strong Commercial Wedge commonly crosses multiple enterprise systems.

Example:

Identity System
      ↓
Customer System
      ↓
Card System
      ↓
Risk System
      ↓
Policy System
      ↓
Execution System

This creates the coordination problem that Noema is designed to solve.

A workflow completely contained within one simple system may provide insufficient differentiation.

⸻

10. Enterprise Context

The workflow should require enterprise context beyond the user’s immediate utterance.

For example:

"I need a replacement card."

may require:

User Identity
Card Identity
Card State
Account State
Eligibility
Policy
Risk
Organization
Permissions

Noema resolves the context necessary to turn intent into an executable action.

⸻

11. Ambiguity

A strong Commercial Wedge should contain legitimate ambiguity.

Examples:

"Replace my card."

Which card?

"Send it to my office."

Which office?

"Cancel the account."

Which account?

Ambiguity should not be treated as a failure of the system.

It is part of the workflow.

Noema should determine whether ambiguity is:

* irrelevant
* resolvable
* clarification-required
* policy-sensitive
* execution-blocking

⸻

12. Ambiguity Must Not Become Guessing

The Commercial Wedge must preserve Noema’s core determinism principle.

If the system cannot establish the intended action with sufficient certainty:

Ambiguity
    ↓
Clarification

not:

Ambiguity
    ↓
Best Guess
    ↓
Execution

The commercial value of the wedge must not be achieved by weakening Noema’s Trust model.

⸻

13. Policy Sensitivity

A strong Commercial Wedge should involve enterprise rules.

Examples:

Eligibility
Authorization
Limits
Approval requirements
Risk thresholds
Organizational policy
Regulatory constraints

The same intent may produce different execution paths depending on policy.

Therefore:

Intent
  +
Context
  +
Policy
  ↓
Executable Decision

⸻

14. Authorization

The workflow should provide meaningful authorization boundaries where appropriate.

For example:

User requests:
"Increase the transfer limit."

Noema may need to establish:

Who is the actor?
Which account?
What authority does the actor have?
What limit applies?
Is additional approval required?

Authorization should be evaluated explicitly rather than inferred from intent alone.

⸻

15. Risk

A Commercial Wedge becomes more valuable when incorrect execution has meaningful consequences.

Examples:

* financial transactions
* account changes
* access changes
* customer operations
* sensitive data operations
* organizational actions

The greater the consequence of an incorrect action, the more valuable deterministic Trust becomes.

⸻

16. Execution Complexity

The workflow should require more than interpreting the user’s request.

It should require a complete execution lifecycle.

Conceptually:

Intent
   ↓
Resolution
   ↓
Context
   ↓
Trust
   ↓
Planning
   ↓
Action
   ↓
Execution
   ↓
Validation
   ↓
Outcome

The wedge should therefore test the complete Noema execution model.

⸻

17. Measurable Outcome

The Commercial Wedge must have measurable outcomes.

Potential measurements include:

* execution time
* human handling time
* automation rate
* escalation rate
* failure rate
* error rate
* cost per execution
* completion rate
* customer response time

The customer should be able to compare:

Before Noema

with:

After Noema

⸻

18. Economic Value

The wedge must create sufficient economic value to justify adoption.

The value may come from:

Less manual work
+
Faster execution
+
Fewer errors
+
Lower operational cost
+
Higher automation
+
Reduced support burden

The precise economic model depends on the enterprise and workflow.

The principle remains:

The wedge must solve a problem worth paying to solve.

⸻

19. The Wedge Must Require Noema

A Commercial Wedge should demonstrate capabilities that are difficult to reproduce safely with ordinary automation.

A useful test is:

Can this workflow be reliably solved with:
one API call
+
fixed parameters
+
deterministic business logic?

If yes, the workflow may not be a strong Noema wedge.

A stronger candidate requires:

Intent
+
Context
+
Ambiguity
+
Policy
+
Authorization
+
Risk
+
Execution

⸻

20. Wedge as Architectural Proof

The Commercial Wedge should validate Noema’s architecture.

A successful wedge should exercise relevant components such as:

Intent Model
      ↓
Context
      ↓
Evidence
      ↓
Trust Engine
      ↓
Action Contract
      ↓
Execution
      ↓
Postcondition
      ↓
Outcome

The workflow therefore becomes an empirical test of the architecture.

⸻

21. Wedge vs Demo

A demo demonstrates possibility.

A Commercial Wedge demonstrates value.

These are not equivalent.

Demo
→ "Noema can do this."
Commercial Wedge
→ "This problem is expensive enough that we should use Noema."

The wedge must therefore exist in a real operational environment or closely represent one.

⸻

22. Wedge vs Feature

A feature is a capability within a product.

A Commercial Wedge is a customer-facing problem.

For example:

Action Contracts
→ Feature / primitive
Ambiguity Resolution
→ Feature / primitive
Card Replacement Workflow
→ Commercial Wedge

The wedge combines multiple Noema capabilities to solve an enterprise problem.

⸻

23. Reusable Primitives

The implementation of the wedge should produce reusable primitives.

For example:

Initial Workflow
      ↓
Identity Resolution
      ↓
Ambiguity Handling
      ↓
Policy Evaluation
      ↓
Action Contracts
      ↓
Execution

These capabilities should then be reusable by subsequent workflows.

This is critical to preventing the wedge from becoming bespoke automation.

⸻

24. Wedge Expansion

A successful wedge should create a path to adjacent workflows.

For example:

Card Renewal
      ↓
Card Operations
      ↓
Account Operations
      ↓
Customer Operations
      ↓
Broader Enterprise Operations

The exact expansion path depends on the enterprise.

The underlying principle is:

Each additional workflow should reuse an increasing amount of the existing Noema execution substrate.

⸻

25. Enterprise Boundary

The Commercial Wedge must preserve Noema’s ownership boundaries.

Noema should not become the System of Record for enterprise Business State merely to simplify the first workflow.

For example:

Enterprise
→ owns account state
Noema
→ owns intent and execution state

The wedge must work within this boundary.

⸻

26. Enterprise Systems

The Commercial Wedge should integrate with existing enterprise systems rather than require their replacement.

Conceptually:

Enterprise Systems
      ↑
      │
    Noema
      ↑
      │
Human Intent

Noema coordinates execution across the enterprise environment.

It does not require the enterprise to migrate its underlying systems of record.

⸻

27. Noema State

Noema may maintain canonical state concerning:

* Intent
* Trust
* Action
* Execution
* Intervention
* Outcome

The enterprise remains authoritative for its own business state.

Therefore:

Enterprise Canonical State
          +
Noema Execution State

can coexist without creating competing authority.

⸻

28. Failure Handling

The Commercial Wedge should expose realistic failure conditions.

Examples:

System unavailable
Action rejected
Timeout
Partial execution
State changed
Authorization expired
Policy changed
External dependency failed

Noema must demonstrate that failure does not automatically become uncontrolled retry or uncontrolled autonomy.

⸻

29. Human Intervention

Some workflows will legitimately require human intervention.

A strong Commercial Wedge should demonstrate that Noema can transition into:

Execute
Clarify
Escalate
Reject

rather than requiring every workflow to be fully autonomous.

Human intervention is therefore compatible with the Commercial Wedge.

It is not evidence that the automation failed.

⸻

30. Outcome Verification

The wedge should include observable postconditions.

Example:

Action:
replace_card
Expected:
card.status = REPLACEMENT_REQUESTED

Noema should verify the relevant enterprise state where required.

The wedge therefore demonstrates:

Intent
   ↓
Action
   ↓
Execution
   ↓
Verified Outcome

rather than merely:

Intent
   ↓
API Call

⸻

31. Auditability

Consequential workflows should provide sufficient execution history to answer:

What did the user request?
What did Noema understand?
What context was used?
What evidence was available?
What policy was evaluated?
Why was the action permitted?
What action was executed?
What happened?

This makes the Commercial Wedge demonstrate enterprise-grade execution rather than merely automation.

⸻

32. Data Boundaries

The wedge should require only the data necessary for execution.

For example:

Card Replacement

may require:

customer_id
card_id
card_status
eligibility
delivery information

It should not require unrelated enterprise data merely because Noema can technically access it.

The wedge must therefore preserve:

Least Privilege
+
Purpose Limitation
+
Data Minimization

⸻

33. Commercial Wedge and Trust

The Commercial Wedge provides a practical environment in which Noema’s Trust Engine demonstrates value.

The relationship is:

Commercial Problem
      ↓
Intent
      ↓
Context
      ↓
Trust
      ↓
Execution
      ↓
Business Outcome

Trust is not an independent product feature.

It is part of what makes Noema’s execution commercially valuable.

⸻

34. Commercial Wedge and Determinism

The wedge must preserve deterministic execution decisions.

The model may be probabilistic.

The final execution decision must not be.

Therefore:

Model
  ↓
Interpretation
  ↓
Deterministic Trust
  ↓
Execute / Clarify / Escalate / Reject

The wedge must never depend on:

"probably correct"

as a sufficient execution condition.

⸻

35. Commercial Wedge and Intent

The wedge should begin with human Intent and terminate in a measurable Outcome.

Conceptually:

Human Intent
      ↓
Executable Intent
      ↓
Trusted Action
      ↓
Enterprise Execution
      ↓
Outcome

This provides a concrete demonstration of Noema’s core thesis.

⸻

36. Commercial Wedge and Action Contracts

The wedge should execute through explicit Action Contracts.

An Action Contract defines the requirements for performing an enterprise action.

Conceptually:

Action
  +
Inputs
  +
Preconditions
  +
Authorization
  +
Policy
  +
Postconditions

This prevents the commercial implementation from becoming an opaque model-driven automation layer.

⸻

37. Commercial Wedge and Enterprise Ownership

The wedge must preserve the principle:

Noema executes on enterprise state; it does not silently become the owner of enterprise state.

For example:

Payment System
→ owns payment status
Noema
→ determines and records the execution journey

This distinction must remain intact even when commercial pressure favors shortcuts.

⸻

38. Wedge Selection Criteria

A candidate Commercial Wedge should be evaluated across:

Pain
Frequency
Intent
Ambiguity
Context
Policy
Authorization
Risk
System Coordination
Measurable Outcome
Economic Value
Reusability

A candidate that scores highly across these dimensions is more likely to demonstrate Noema’s differentiated value.

⸻

39. Wedge Failure Conditions

A candidate should not be considered a strong Commercial Wedge when:

* the workflow is trivial;
* one deterministic API call solves the problem;
* no meaningful intent interpretation is required;
* no meaningful enterprise context is required;
* ambiguity does not exist;
* policy has little relevance;
* authorization is irrelevant;
* failure has negligible consequences;
* the economic value is insignificant;
* the workflow cannot generalize;
* the workflow requires Noema to own enterprise Business State.

Such workflows may still be useful engineering exercises.

They are not necessarily strong commercial wedges.

⸻

40. Smallest Real Problem

The Commercial Wedge should be the smallest real problem that proves the largest meaningful part of Noema’s thesis.

This means:

Minimize
    Workflow Scope
Maximize
    Noema Capability Demonstrated

The wedge should not attempt to solve an entire enterprise domain.

It should solve one sufficiently valuable workflow end-to-end.

⸻

41. Commercial Wedge and Platform Expansion

The intended progression is:

One Painful Workflow
        ↓
Reusable Noema Primitives
        ↓
Adjacent Workflows
        ↓
Multiple Enterprise Domains
        ↓
Enterprise Intent Execution Layer

The commercial wedge is therefore the first point of entry into a larger platform.

⸻

42. Wedge Validation

A Commercial Wedge is validated when:

1. A real enterprise problem is confirmed.
2. The current workflow has measurable cost or friction.
3. Users naturally express the desired outcome as Intent.
4. The workflow requires meaningful enterprise Context.
5. Ambiguity exists in consequential cases.
6. Policy or authorization affects execution.
7. Multiple enterprise capabilities or systems participate.
8. Noema can determine whether execution is permitted.
9. Noema can execute through Action Contracts.
10. Outcomes can be verified.
11. Exceptions can be handled safely.
12. Business value can be measured.
13. The resulting primitives can support additional workflows.

⸻

43. Commercial Wedge Invariants

Invariant 1

The Commercial Wedge must correspond to a real enterprise problem.

Invariant 2

The Commercial Wedge must provide measurable customer value.

Invariant 3

The Commercial Wedge is an entry point into Noema, not the definition of Noema.

Invariant 4

A workflow should not qualify as a strong wedge merely because it can be automated.

Invariant 5

The wedge should exercise meaningful Noema capabilities.

Invariant 6

Ambiguity must not be resolved through unsafe guessing merely to improve automation rates.

Invariant 7

The wedge must preserve Noema’s deterministic Trust boundary.

Invariant 8

The wedge must preserve enterprise ownership of Business State.

Invariant 9

Enterprise Systems of Record remain authoritative for their respective domains.

Invariant 10

Noema should execute through explicit Action Contracts.

Invariant 11

Consequential execution must remain subject to authorization, policy, and risk requirements.

Invariant 12

The wedge should support observable and verifiable outcomes.

Invariant 13

Failure and human intervention must be valid execution states.

Invariant 14

The wedge should produce reusable capabilities rather than isolated bespoke automation.

Invariant 15

The wedge should provide a credible path toward additional enterprise workflows.

Invariant 16

The smallest useful wedge is preferred over an unnecessarily broad initial product scope.

Invariant 17

Commercial pressure must not cause Noema to violate its architectural boundaries.

Invariant 18

The strongest wedge demonstrates both customer value and architectural differentiation.

⸻

44. Final Definition

A Commercial Wedge is the smallest real enterprise problem through which Noema can demonstrate measurable customer value while exercising its core intent, context, trust, action, and execution capabilities.

The fundamental relationship is:

Enterprise Problem
       ↓
Commercial Wedge
       ↓
Human Intent
       ↓
Context
       ↓
Trust
       ↓
Action Contract
       ↓
Execution
       ↓
Verified Outcome
       ↓
Measurable Value

The wedge gets Noema into the enterprise.

The underlying execution primitives create the reusable platform.

Therefore:

The Commercial Wedge is not what Noema is. It is the concrete problem through which the enterprise discovers why Noema needs to exist.