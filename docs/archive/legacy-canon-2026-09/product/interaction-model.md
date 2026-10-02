> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Interaction Model

Status: Foundational
Version: 0.2
Domain: Product
Canonical Path: product/interaction-model.md

⸻

1. Definition

The Interaction Model defines how humans and other authorized participants communicate with Noema, how those interactions affect Intent and execution state, and how Noema communicates execution requirements, progress, intervention requests, and verified outcomes.

The Interaction Model answers:

“How does a participant express or trigger Intent, how does Noema interact with that participant during execution, and how are resulting outcomes communicated?”

Noema is not primarily a conversational interface.

It is an intent-driven execution system in which Interaction is the mechanism through which a participant:

* expresses Intent;
* provides or resolves Context;
* resolves ambiguity;
* satisfies confirmation or authorization requirements;
* receives execution status;
* responds to execution interruptions;
* modifies or cancels an Intent where permitted;
* receives verified Outcomes.

Conceptually:

Participant
     │
     ▼
 Interaction
     │
     ▼
   Intent
     │
     ▼
   Noema
     │
     ├── Context
     ├── Evidence
     ├── Trust
     ├── Policy
     ├── Action
     └── Execution
              │
              ▼
       Enterprise Systems
              │
              ▼
           Outcome
              │
              ▼
         Interaction
              │
              ▼
         Participant

Interaction therefore exists on both sides of execution:

Intent In
   ↓
Execution
   ↓
Outcome Out

⸻

2. Purpose

The purpose of the Interaction Model is to establish the semantic relationship between:

* Participant
* Interaction
* Session
* Intent
* Context
* Evidence
* Trust
* Policy
* Action
* Execution
* Enterprise Systems
* Outcome
* Human Intervention

The model establishes that Interaction is not equivalent to:

* chat;
* UI;
* API requests;
* prompts;
* messages;
* notifications;
* voice.

These are interaction mechanisms or representations.

Interaction is the broader semantic process through which an authorized participant communicates with and participates in a Noema execution lifecycle.

⸻

3. Core Principle

Noema should optimize for Intent completion and trustworthy outcome, not conversation completion.

A conversation may end without an Action being executed.

An Action may be executed without a long conversation.

An execution may require multiple interactions.

Therefore:

Conversation ≠ Interaction
Interaction ≠ Intent
Interaction ≠ Execution
Execution ≠ Conversation

The relevant product objective is:

Participant Intent
       ↓
Correct Interpretation
       ↓
Required Resolution
       ↓
Trusted Execution
       ↓
Verified Outcome
       ↓
Appropriate Communication

⸻

4. Interaction as a Semantic Event

An Interaction is a participant-facing event that may affect or observe the Noema execution lifecycle.

An Interaction may:

* introduce an Intent;
* provide Context;
* provide Evidence about participant intent;
* answer a clarification;
* confirm an Action;
* reject a proposed Action;
* modify an Intent;
* request cancellation;
* satisfy an approval requirement;
* provide information required for execution;
* respond to an intervention request;
* observe execution progress;
* receive an Outcome.

Therefore, Interaction is not merely transport.

It is a semantic event within the execution lifecycle.

⸻

5. Interaction vs Intent

Intent represents what a participant wants to accomplish.

Interaction represents the exchange through which that Intent is:

* expressed;
* clarified;
* confirmed;
* modified;
* authorized;
* observed;
* completed;
* or terminated.

Therefore:

Interaction
     ↓
Intent

but:

Interaction ≠ Intent

A single Intent may involve multiple Interactions.

Interaction 1
     ↓
Intent
     ↓
Interaction 2
     ↓
Clarification
     ↓
Interaction 3
     ↓
Confirmation
     ↓
Execution
     ↓
Interaction 4
     ↓
Outcome

⸻

6. Interaction vs Conversation

Conversation is one interaction modality.

Noema may support:

* Chat
* Voice
* Structured UI
* Forms
* Buttons
* API
* Webhook
* Event
* Workflow Trigger
* Approval Interface
* Operator Interface

The semantic model must therefore remain independent of conversational presentation.

A conversation may contain multiple Interactions.

An Interaction may also exist without a conversation.

⸻

7. Interaction Modalities

Noema may support multiple interaction modalities.

Examples include:

* Natural Language
* Chat
* Voice
* Structured UI
* Forms
* Buttons
* API
* Webhook
* Event
* Workflow Trigger
* Human Approval
* Operator Intervention
* Notification

Different modalities may represent the same semantic Intent.

For example:

Natural Language:
"Freeze my card."
Structured UI:
[Freeze Card]
API:
freeze_card(card_id)
Voice:
"Freeze the card ending in 1234."

The representation differs.

The semantic Intent may be equivalent.

⸻

8. Interaction Boundary

Interaction is the boundary between participant communication and Noema’s semantic execution model.

Conceptually:

External Participant
        │
        ▼
    Interaction
        │
        ▼
      Intent
        │
        ▼
      Noema

Noema should translate interaction into explicit semantic state.

Interface-specific representations must not become execution state directly.

For example:

"Yes"

is not independently executable authorization.

It must be bound to sufficient context, Intent, Action, principal, and applicable requirements.

⸻

9. Participant

A Participant is an authorized actor capable of initiating, influencing, observing, approving, or intervening in a Noema execution lifecycle.

Participants may include:

* End User
* Employee
* Customer
* Application
* API Client
* Workflow
* Enterprise System
* Event Source
* Approver
* Operator
* Administrator
* Noema itself, where Policy explicitly permits system-initiated interaction

Participant identity and authority must be represented explicitly where consequential interaction occurs.

⸻

10. Human Participant

The Human is a primary source of Intent in many Noema interactions.

The Human may:

* express Intent;
* provide Context;
* resolve ambiguity;
* confirm an Action;
* reject a proposed Action;
* modify an Intent;
* provide missing information;
* approve an escalation;
* intervene in execution;
* request cancellation;
* acknowledge an Outcome.

The Human is therefore an active participant in the execution lifecycle.

⸻

11. Participant Authority

Participant identity does not by itself establish authority.

Noema must distinguish:

Who is participating?
        ↓
What authority does the participant possess?
        ↓
What Action does that authority permit?
        ↓
Under what Policy?

A participant may be authenticated while still being unauthorized to perform a particular Action.

⸻

12. Interaction Does Not Directly Mutate Execution State

Participants communicate with Noema through Interactions.

They do not directly mutate authoritative Noema execution state.

For example:

Human:
"Send the invoice."

does not directly establish:

execution.status = SUCCEEDED

Noema must establish execution state through the execution lifecycle.

Similarly:

Human:
"The payment is refunded."

does not establish:

payment.status = REFUNDED

The relevant enterprise System of Record remains authoritative.

⸻

13. Interaction State

Interaction State describes the state of the interaction mechanism.

Examples include:

RECEIVED
PROCESSING
AWAITING_RESPONSE
RESPONSE_SENT
DELIVERED
ACKNOWLEDGED
EXPIRED
CANCELLED
FAILED

Interaction State must remain distinct from Intent State and Execution State.

⸻

14. Intent State

Intent State describes the semantic state of the participant’s requested outcome.

Examples include:

EXPRESSED
AMBIGUOUS
CLARIFYING
RESOLVED
AUTHORIZED
READY
EXECUTING
PAUSED
COMPLETED
REJECTED
CANCELLED

Interaction may cause an Intent State transition.

It does not define the state arbitrarily.

⸻

15. Execution State

Execution State describes what Noema has established about execution.

Examples include:

NOT_STARTED
READY
RUNNING
WAITING
SUCCEEDED
FAILED
PARTIAL
UNKNOWN
RECONCILING
COMPENSATING
ESCALATED
CANCELLED

Interaction must not collapse these states into conversational language that changes their meaning.

⸻

16. Interaction, Intent, and Execution State Must Remain Distinct

These models are related but must not be conflated.

Interaction State
        ↓
may affect
        ↓
Intent State
        ↓
may authorize / produce
        ↓
Execution State
        ↓
produces
        ↓
Outcome

For example:

Interaction:
"Yes, proceed."
Interaction State:
RECEIVED
Intent State:
AUTHORIZED
Execution State:
NOT_STARTED

A confirmation does not mean that execution has succeeded.

⸻

17. Clarification

Clarification is an Interaction used to resolve material uncertainty.

Example:

User:
"Cancel the subscription."
Noema:
"Which subscription?"
User:
"The business plan."

The clarification may transition:

AMBIGUOUS
    ↓
CLARIFYING
    ↓
RESOLVED

Clarification is therefore part of deterministic Intent Resolution, not merely conversational UX.

⸻

18. Material Ambiguity

Not all ambiguity requires interaction.

Noema should determine whether ambiguity is:

* irrelevant;
* resolvable from authoritative Context;
* resolvable from existing Evidence;
* clarification-required;
* policy-sensitive;
* execution-blocking.

If material ambiguity remains unresolved:

AMBIGUOUS

remains a valid state.

Noema must not convert unresolved ambiguity into execution merely to reduce interaction count.

⸻

19. Interaction and Confidence

Model confidence may inform whether additional Interaction is useful.

However:

Confidence ≠ Authorization
Confidence ≠ Trust
Confidence ≠ Confirmation
Confidence ≠ Identity
Confidence ≠ Execution

A high-confidence model interpretation does not independently authorize a consequential Action.

Trust, Policy, authorization, and Action Contract requirements remain authoritative.

⸻

20. Interaction and Trust

Trust determines whether an Intent can proceed toward execution.

Interaction may satisfy explicit Trust requirements.

For example:

Intent
  ↓
Trust Evaluation
  ↓
Confirmation Required
  ↓
Interaction
  ↓
Confirmation
  ↓
Trust Evaluation
  ↓
Execute

Interaction is therefore one mechanism through which Trust requirements may be fulfilled.

It does not replace the Trust decision.

⸻

21. Interaction and Authorization

Authorization must not be inferred merely because a participant requests an Action.

For example:

User:
"Refund payment 123."

does not establish:

User authorized to refund payment 123

Noema may need to establish:

* participant identity;
* resource identity;
* authority;
* delegation;
* organizational scope;
* applicable Policy;
* Action-specific permissions.

⸻

22. Interaction and Identity

An Interaction may identify its initiating principal through:

* authenticated session;
* enterprise identity provider;
* delegated identity;
* API credential;
* service identity;
* workflow identity;
* explicit identity selection.

Identity must be grounded sufficiently for the requested Action.

Ambiguous identity must trigger deterministic resolution rather than guessing.

⸻

23. Interaction and Context

Interactions may provide or reference Context.

Example:

User:
"Use the account we discussed earlier."

Noema must determine whether referenced Context is:

* relevant;
* current;
* authoritative;
* authorized;
* sufficiently specific;
* still applicable to the current Intent.

Context does not automatically become executable truth.

⸻

24. Interaction and Evidence

An Interaction may provide Evidence about participant communication.

For example:

User:
"Yes, refund the $500 payment."

may provide Evidence of explicit confirmation.

However:

Interaction
   ↓
Evidence about participant communication

is distinct from:

Enterprise System
   ↓
Evidence about Business State

A participant’s statement does not independently establish enterprise state.

⸻

25. Interaction and Action

Interaction may result in an Action being:

* proposed;
* clarified;
* confirmed;
* authorized;
* executed;
* reported.

The Interaction itself is not the Action.

For example:

Interaction:
"Freeze my card."
Intent:
freeze_card
Action:
freeze_card(card_id)

The semantic Action remains subject to Trust, Policy, Preconditions, and Action Contract requirements.

⸻

26. Interaction and Planning

Some Intents require planning before execution.

Example:

User:
"Close my account and make sure all pending refunds are handled."

Noema may construct:

Identify Account
      ↓
Retrieve Pending Refunds
      ↓
Resolve Refund Actions
      ↓
Execute Refunds
      ↓
Verify Refund Outcomes
      ↓
Close Account
      ↓
Verify Account State

Interaction may occur during planning when ambiguity, authorization, Policy, or execution requirements demand participant input.

⸻

27. Interaction and Execution

Interaction must not directly bypass the execution boundary.

The execution path remains:

Interaction
     ↓
Intent
     ↓
Context / Evidence
     ↓
Trust / Policy
     ↓
Action Contract
     ↓
Execution
     ↓
Enterprise System

This separation prevents conversational input from becoming an uncontrolled execution mechanism.

⸻

28. Explicit Confirmation

Some Actions require explicit confirmation before execution.

Example:

Intent:
Transfer $20,000
Trust:
Confirmation Required
Interaction:
"You're about to transfer $20,000 to Account 123. Confirm?"
Participant:
"Confirm."

Confirmation is an explicit Interaction event.

It must be bound to the relevant Intent or Action.

Passive continuation or unrelated conversational content must not be treated as confirmation.

⸻

29. Confirmation Binding

Consequential confirmation should include sufficient binding information.

Conceptually:

Confirmation
     │
     ├── intent_id
     ├── action_id
     ├── principal
     ├── timestamp
     ├── target
     └── relevant parameters

This prevents:

"Yes"

from being incorrectly reused as authorization for a different Action.

⸻

30. Confirmation Is Not Permanent Authorization

Confirmation may become stale.

For example:

Intent:
Transfer $10,000
Confirmed
    ↓
Enterprise State Changes
    ↓
Precondition Invalidated

Noema may need to revalidate before execution.

Therefore:

Confirmation ≠ Permanent Authorization

Confirmation remains subject to applicable Trust, Policy, freshness, and execution requirements.

⸻

31. Reconfirmation

If material execution conditions change, Noema may require renewed Interaction.

Conceptually:

Intent
  ↓
Confirmed
  ↓
Enterprise State Changes
  ↓
Precondition Invalidated
  ↓
Revalidation
  ↓
Reconfirmation / Replan / Reject

This prevents stale confirmation from authorizing materially different execution.

⸻

32. Interaction and Planning Changes

A participant may modify an Intent before or during execution where permitted.

Example:

User:
"Send $500."
User:
"Actually, send $700."

Noema must determine whether the second Interaction represents:

* modification of the existing Intent;
* a new Intent;
* an incompatible change requiring re-resolution;
* a change requiring renewed authorization or confirmation.

The resulting semantic state must remain explicit.

⸻

33. Interaction and Cancellation

A participant may request cancellation.

Example:

User:
"Cancel that."

Noema must resolve:

Which Intent?
Which Action?
What is its current execution state?
Is cancellation still possible?
What does Policy permit?

An Action that has already become irreversible may not be cancellable.

Cancellation therefore remains an execution decision, not merely a conversational command.

⸻

34. Interaction and Execution Progress

Noema may expose execution progress through Interaction.

Examples:

"Your refund request was submitted."
"Waiting for the payment provider."
"Refund confirmed."

These communications must correspond to actual Noema or enterprise observations.

Generated narrative must not create execution state.

⸻

35. Interaction and Outcome

An Outcome should be communicated according to established execution state.

Example:

Execution:
SUCCEEDED
Interaction:
"Your card has been frozen."

The communication should be grounded in the verified Action Outcome.

Noema should not claim success merely because an Action was attempted.

⸻

36. Interaction and Failure

Failures may require additional Interaction.

Noema may communicate:

* what failed;
* whether execution was attempted;
* whether the outcome is known;
* whether retry is permitted;
* whether reconciliation is required;
* whether human intervention is required;
* what next actions are available.

The communication must preserve distinctions such as:

FAILED

versus:

UNKNOWN

versus:

PARTIAL

⸻

37. Interaction and Unknown Outcomes

An external write may time out after the enterprise system receives the request.

Noema must not automatically tell the participant:

"The payment failed."

if failure has not been established.

Instead:

Execution
    ↓
Outcome = UNKNOWN
    ↓
Reconciliation
    ↓
Verified State
    ↓
Interaction

Participant-facing communication must remain consistent with the established execution state.

⸻

38. Interaction and Human Intervention

Human intervention is distinct from ordinary participant interaction.

A user may provide Intent.

An operator may be required to resolve an execution exception.

Example:

User Intent
    ↓
Execution
    ↓
Enterprise Conflict
    ↓
Human Intervention
    ↓
Resolution
    ↓
Execution Continues

The operator’s:

* identity;
* authority;
* intervention;
* decision;
* timestamp;
* relationship to the affected Intent

should be represented where required.

⸻

39. Interaction and Compound Intent

A Compound Intent may produce multiple Interaction points.

Example:

"Refund the payment and close the account."
        ↓
Resolve Payment
        ↓
Confirm Refund
        ↓
Execute Refund
        ↓
Verify Refund
        ↓
Close Account
        ↓
Verify Account

Interaction may occur between stages when required by:

* ambiguity;
* Trust;
* Policy;
* authorization;
* failure;
* approval;
* recovery.

⸻

40. Interaction and Long-Running Execution

An Interaction does not necessarily end when execution begins.

Long-running Actions may generate multiple Interaction events.

Example:

Intent
  ↓
Execution Started
  ↓
Waiting
  ↓
External Event
  ↓
Execution Resumed
  ↓
Completed
  ↓
Outcome Communicated

The participant may observe relevant transitions through an appropriate interaction channel.

⸻

41. Interaction Continuity

Noema should preserve continuity between related Interactions.

Example:

Interaction 1:
"Refund my last payment."
Interaction 2:
"The $500 one."
Interaction 3:
"Yes, do it."

These Interactions may belong to the same Intent lifecycle.

Continuity must be established semantically rather than assumed solely from temporal proximity.

A subsequent message does not automatically belong to a previous Intent.

⸻

42. Interaction Session

An Interaction Session may group related Interactions.

Conceptually:

Interaction Session
    │
    ├── Interaction
    ├── Interaction
    ├── Clarification
    ├── Confirmation
    ├── Approval
    └── Outcome

A Session provides continuity and organizational context.

It does not automatically establish semantic authority over every Interaction within it.

⸻

43. Interaction Session vs Intent Lifecycle

A Session may contain:

* one Intent;
* multiple related Intents;
* unrelated Interactions;
* notifications;
* approvals;
* operator interventions.

Therefore:

Session ≠ Intent

Intent membership must be established explicitly enough for consequential execution.

⸻

44. Interaction and Enterprise State

Interaction is not authoritative enterprise state.

For example:

User:
"The payment is refunded."

does not establish:

payment.status = REFUNDED

Where enterprise state matters, Noema must obtain authoritative Evidence from the relevant enterprise system.

⸻

45. Interaction and Canonical Data

Interaction may provide references to Canonical Data.

Example:

User:
"Refund payment 123."

The Interaction supplies:

payment_id = 123

The enterprise System of Record establishes:

* whether payment 123 exists;
* its current state;
* whether it is eligible;
* what other canonical properties apply.

Interaction provides participant intent.

Enterprise systems establish authoritative Business State.

⸻

46. Interaction and Data Boundaries

Noema should expose only information necessary and authorized for the Interaction.

For example:

User:
"What's the status of my refund?"

The response should contain only information permitted by:

* identity;
* authorization;
* Policy;
* privacy requirements;
* organizational scope;
* data minimization requirements.

Interaction must not become a channel for uncontrolled enterprise data disclosure.

⸻

47. Interaction and Explainability

Noema should communicate relevant execution decisions without exposing hidden model reasoning or unnecessary implementation details.

For example:

"Your request requires approval because transfers above $10,000 require a second approver."

This communicates the applicable Policy result.

It does not require exposing private chain-of-thought or internal model reasoning.

⸻

48. Interaction and Policy

Policy may determine how Noema must interact with a participant.

Policy may define:

* when confirmation is required;
* when clarification is required;
* what information may be disclosed;
* who may approve;
* when escalation is required;
* when reconfirmation is required;
* when execution must be rejected;
* which interaction channels may be used.

Therefore:

Policy
   ↓
Interaction Requirements

is part of the execution model.

⸻

49. Interaction and Risk

Higher-risk Actions may require stronger interaction controls.

For example:

Lower Risk
    ↓
Direct Execution
Higher Risk
    ↓
Explicit Confirmation
Higher Risk + Additional Authority
    ↓
Confirmation + Approval
Critical / Exceptional
    ↓
Human Intervention

The exact thresholds are Policy-defined.

Interaction implements those requirements; it does not define them independently.

⸻

50. Interaction and Determinism

Interaction must not become a mechanism for concealing probabilistic decisions.

For example:

"I think you probably mean Account 123."

is not deterministic resolution.

Instead:

Ambiguity
   ↓
Clarification
   ↓
Explicit Selection
   ↓
Resolved Intent

Interaction should convert unresolved uncertainty into explicit information where possible.

⸻

51. Interaction and Model Output

The model may generate candidate interpretations or candidate responses.

Those outputs are not automatically authoritative Interaction State.

Conceptually:

Model
  ↓
Candidate Interpretation / Response
  ↓
Noema Validation
  ↓
Semantic State
  ↓
Interaction

Noema owns the resulting semantic state.

The model does not independently establish:

* authorization;
* confirmation;
* execution;
* enterprise state;
* Outcome.

⸻

52. Interaction and Structured UI

Structured interfaces may represent the same semantic Interaction as natural language.

For example:

Natural Language:
"Refund the $500 payment."
Structured UI:
Payment: $500
Date: Aug 26
[Refund]

Both may resolve to:

Intent:
refund_payment

The semantic model should remain interface-independent.

⸻

53. Interaction and API Consumers

External applications may interact with Noema programmatically.

Example:

Application
    ↓
Intent API
    ↓
Noema

A machine-originated Interaction remains subject to:

* identity;
* authorization;
* Intent semantics;
* Trust;
* Policy;
* Action Contracts;
* execution controls.

API interaction is therefore another Interaction modality, not a bypass around the model.

⸻

54. Interaction and Events

Events may trigger or participate in Noema execution.

Example:

Enterprise Event
      ↓
Noema
      ↓
Intent / Execution State

Events differ from human Interactions because they are machine-generated observations or triggers.

They must retain:

* source;
* timestamp;
* provenance;
* event identity;
* relevant version information.

An event must not be treated as equivalent to a human authorization unless Policy explicitly establishes such authority.

⸻

55. Interaction and Notifications

Notifications are output forms of Interaction.

Examples include:

* Email
* Push Notification
* SMS
* Webhook
* Dashboard Update
* Chat Message
* In-application notification

A notification should represent established Noema or enterprise state.

It must not imply an execution outcome that has not been established.

⸻

56. Interaction and Proactive Behavior

Noema may initiate Interaction when explicitly permitted by Policy and system design.

Example:

Upcoming Policy Expiration
        ↓
Noema
        ↓
Participant Notification
        ↓
Participant Confirmation
        ↓
Execution

Proactive Interaction must respect:

* identity;
* authorization;
* consent where applicable;
* Policy;
* data boundaries;
* notification permissions;
* execution requirements.

Proactive behavior does not create independent authority to execute consequential Actions.

⸻

57. Interaction and Interruptions

Execution may require interruption.

Example:

Executing
   ↓
Approval Required
   ↓
Paused
   ↓
Interaction
   ↓
Approval
   ↓
Resume

The interruption should be represented explicitly.

A paused execution is not necessarily a failure.

⸻

58. Interaction and Recovery

When execution fails or becomes uncertain, Interaction may support recovery.

Example:

Execution Failed / Unknown
        ↓
Recovery Determination
        ↓
Interaction
        ↓
Retry / Reconcile / Modify / Escalate / Cancel

Recovery options remain governed by:

* Action Contract;
* Policy;
* Trust;
* Integration semantics;
* execution state.

Interaction does not independently authorize recovery.

⸻

59. Interaction and Compensation

If an executed Action requires compensation, Noema may interact with a participant where appropriate.

Example:

Action A
  ↓
Succeeded
Action B
  ↓
Failed
Compensation Required
  ↓
Interaction
  ↓
Human Decision

Not every compensation requires participant interaction.

Policy and execution semantics determine whether human participation is required.

⸻

60. Interaction and Multi-Actor Execution

Enterprise execution may involve multiple actors.

Example:

Requester
    ↓
Noema
    ↓
Approver
    ↓
Noema
    ↓
Enterprise System

The Interaction Model must preserve actor identity and authority throughout the execution lifecycle.

The requester and approver are not necessarily the same principal.

Approval must therefore be bound to:

* the approving principal;
* the relevant Intent or Action;
* applicable parameters;
* authorization scope;
* timestamp;
* Policy requirements.

⸻

61. Interaction and Organizational Boundaries

Interactions must respect organizational boundaries.

For example:

Employee
   ↓
Business Unit A

must not automatically expose:

Business Unit B

data or capabilities.

Interaction permissions must therefore be evaluated within the relevant organizational scope.

⸻

62. Interaction and Enterprise Ownership

Noema may mediate Interaction with enterprise systems.

It does not become the owner of those systems’ Business State.

Conceptually:

Participant
    ↓
Interaction
    ↓
Noema
    ↓
Enterprise System
    ↓
Business State

The enterprise remains authoritative for resulting Business State.

⸻

63. Interaction as an Execution Surface

Noema’s product surface is not limited to a chat window.

The execution surface may include:

* Chat
* Voice
* Dashboard
* Approval UI
* API
* Webhook
* Notification
* Embedded Application
* Operator Console

The common abstraction is not the interface.

It is:

Interaction
    ↓
Intent
    ↓
Trust / Policy
    ↓
Action
    ↓
Execution
    ↓
Verified Outcome

⸻

64. Interaction Delivery

The interaction mechanism is responsible for delivering participant-facing information through the appropriate channel.

Delivery may involve:

* synchronous response;
* asynchronous notification;
* polling;
* webhook;
* event subscription;
* dashboard state;
* approval request.

Delivery status must remain distinct from semantic Outcome.

For example:

Notification Delivered

does not imply:

Action Succeeded

⸻

65. Interaction Expiry

Some Interactions have validity windows.

Examples include:

* confirmation;
* approval request;
* authentication challenge;
* temporary clarification request;
* recovery decision.

An expired Interaction must not automatically remain valid indefinitely.

For consequential Interactions, expiry should be governed by Policy and the relevant execution contract.

⸻

66. Interaction Integrity

Consequential Interactions should be attributable and tamper-resistant.

For example:

"Confirm transfer."

should be associated with sufficient context:

principal
intent
action
amount
target
timestamp
confirmation context

A generic:

"Yes"

must not be treated as authorization without sufficient contextual binding.

⸻

67. Interaction Provenance

Noema should preserve where an Interaction originated.

Possible sources include:

Human
Application
API
Workflow
Event
Operator
System

Provenance may affect:

* interpretation;
* authorization;
* Trust;
* Policy;
* auditability;
* execution semantics.

⸻

68. Interaction Security

Interactions may contain sensitive information.

Noema should apply appropriate:

* authentication;
* authorization;
* encryption;
* access control;
* data minimization;
* retention;
* redaction;
* secure logging.

Interaction history must not become an uncontrolled repository of enterprise data.

⸻

69. Interaction Auditability

Consequential Interactions should be auditable.

Relevant records may include:

interaction_id
session_id
participant
participant_identity
source
modality
timestamp
intent_id
intent_version
action_id
confirmation
authorization
execution_id
resulting_state

The exact information retained depends on Policy, privacy requirements, and applicable retention obligations.

⸻

70. Interaction and Outcome Truth

Participant-facing communication must preserve the distinction between:

Requested
Attempted
Succeeded
Failed
Unknown
Partially Executed
Reconciled

Noema must not use interaction language to collapse these states into a misleading simplified narrative.

⸻

71. Interaction and Enterprise Events

Enterprise events may provide information about execution outcomes.

For example:

Payment System
      ↓
payment.refunded
      ↓
Event Infrastructure
      ↓
Noema
      ↓
Outcome Verification
      ↓
Interaction

An event provides Evidence.

Where required, authoritative state should still be verified according to the relevant Action and Integration contracts.

⸻

72. Interaction and State Freshness

Interaction-derived information may become stale.

For example:

Participant:
"Use account 123."
Later:
Account permissions change.

Noema must not assume that prior Interaction remains sufficient for current execution.

Freshness requirements depend on:

* Action risk;
* Policy;
* Context;
* enterprise state;
* time elapsed;
* confirmation requirements.

⸻

73. Interaction and Re-Resolution

A previously resolved Intent may require re-resolution if material information changes.

Conceptually:

Resolved Intent
      ↓
Material State Change
      ↓
Revalidation
      ↓
Re-resolution / Reconfirmation / Reject

Previous Interaction history is Evidence.

It is not an immutable authorization to execute under materially changed conditions.

⸻

74. Interaction and Privacy

Interaction must respect data boundaries.

Noema should not expose:

* unnecessary personal information;
* unrelated enterprise information;
* information outside participant authority;
* hidden credentials;
* sensitive implementation details.

The interaction surface should expose the minimum information necessary for the participant to understand and participate in the relevant execution.

⸻

75. Interaction and Least Privilege

Interaction capabilities should follow least privilege.

A participant authorized to:

View Payment

is not automatically authorized to:

Refund Payment

A participant authorized to:

Approve Payment

is not necessarily authorized to:

Modify Payment

Interaction capabilities must therefore correspond to actual authority.

⸻

76. Interaction and Enterprise Ownership

Noema may retain Interaction and execution history necessary for its own execution model.

It must not silently transform participant interaction into ownership of enterprise Business State.

Therefore:

Enterprise Canonical State
        +
Noema Interaction / Execution State

may coexist without creating competing authority.

⸻

77. Interaction Model

Conceptually:

Interaction {
    interaction_id
    session_id
    participant
    participant_identity
    modality
    source
    timestamp
    input
    referenced_intent
    referenced_action
    context
    evidence
    confirmation
    authorization
    provenance
    resulting_state
    delivery_state
}

This is a semantic model rather than a requirement for a literal database table.

⸻

78. Interaction Relationships

Interaction
│
├── initiated_by → Participant
├── belongs_to → Session
├── expresses → Intent
├── references → Context
├── provides → Evidence
├── resolves → Ambiguity
├── requests → Action
├── confirms → Intent / Action
├── authorizes → Intent / Action
├── influences → Trust
├── satisfies → Policy Requirement
├── observes → Execution
├── communicates → Outcome
├── triggers → Intervention
└── may_modify → Intent

⸻

79. Interaction Lifecycle

Conceptually:

Created
   ↓
Received
   ↓
Authenticated / Attributed
   ↓
Interpreted
   ↓
Bound to Intent / Execution
   ↓
Processed
   ↓
Responded
   ↓
Delivered
   ↓
Completed / Expired

Not every Interaction traverses every state.

The lifecycle depends on modality and purpose.

⸻

80. Interaction Invariants

Invariant 1

Interaction is the semantic exchange through which authorized participants communicate with and participate in Noema execution.

Invariant 2

Interaction is not equivalent to conversation, UI, API, notification, or any single transport mechanism.

Invariant 3

Intent and Interaction are distinct concepts.

Invariant 4

Interaction State, Intent State, and Execution State must remain distinct.

Invariant 5

Interaction must not directly bypass Intent, Trust, Policy, Action Contract, or Execution boundaries.

Invariant 6

Model-generated responses are not automatically authoritative Interaction State.

Invariant 7

Material ambiguity must be resolved explicitly rather than hidden through probabilistic inference.

Invariant 8

Model confidence does not constitute authorization, Trust, confirmation, or execution.

Invariant 9

Participant requests do not automatically establish enterprise Business State.

Invariant 10

Enterprise state must be grounded against authoritative enterprise sources where required.

Invariant 11

Consequential confirmation must be bound to the relevant Intent or Action.

Invariant 12

A generic confirmation must not be reused for an unrelated Action.

Invariant 13

Confirmation does not remain permanently valid when material execution conditions change.

Invariant 14

Interaction may influence Intent State but does not directly define execution Outcome.

Invariant 15

Execution outcomes communicated through Interaction must reflect established execution state.

Invariant 16

Unknown execution outcomes must not be communicated as confirmed success or failure.

Invariant 17

Partial execution must remain distinguishable from complete failure.

Invariant 18

Interaction provenance must be preserved where required for Trust, Policy, authorization, and Auditability.

Invariant 19

Interactions must respect identity, authorization, privacy, tenant, and organizational boundaries.

Invariant 20

Interaction history must not become an uncontrolled source of enterprise truth.

Invariant 21

Human intervention must be distinguished from ordinary participant interaction.

Invariant 22

Machine-generated Interactions must preserve their source and provenance.

Invariant 23

Different interaction modalities may represent the same semantic Intent.

Invariant 24

Noema should optimize for Intent completion and trustworthy Outcome rather than conversation completion.

Invariant 25

Interaction may pause, resume, modify, clarify, confirm, cancel, or terminate participation in an Intent lifecycle according to Policy and execution state.

Invariant 26

Confirmation and approval must be bound to the relevant principal, Intent or Action, and applicable execution parameters.

Invariant 27

Expired or stale Interaction authorization must not be treated as permanently valid.

Invariant 28

Interaction delivery status must not be interpreted as Action execution status.

Invariant 29

Participant-facing communication must preserve the distinction between requested, attempted, succeeded, failed, unknown, partial, and reconciled execution states.

Invariant 30

Interaction may provide Evidence about participant communication but does not independently establish enterprise Business State.

Invariant 31

Context obtained through Interaction must remain subject to relevance, authority, freshness, and authorization requirements.

Invariant 32

Interaction must not expose enterprise information beyond what is necessary and authorized.

Invariant 33

API, event, workflow, and machine-originated Interactions remain subject to identity, authorization, Trust, Policy, and execution controls.

Invariant 34

Proactive Interaction does not create independent authority to execute consequential Actions.

Invariant 35

A previous Interaction may become insufficient when material Context, Policy, authorization, or enterprise state changes.

Invariant 36

Noema may mediate Interaction with enterprise systems without becoming the owner of their Business State.

Invariant 37

Interaction must not be used to conceal probabilistic execution decisions.

Invariant 38

The semantic Interaction model must remain independent of any specific interface or transport mechanism.

Invariant 39

Interaction should provide sufficient continuity to support multi-step Intent resolution without assuming that every subsequent participant message belongs to the previous Intent.

Invariant 40

Consequential Interaction records must retain sufficient provenance and binding information to reconstruct the participant’s role in the execution lifecycle.

Invariant 41

Interaction must not independently reinterpret or invent enterprise Actions.

Invariant 42

Interaction is part of the execution surface, but it is not itself the execution authority.

⸻

81. Final Definition

The Interaction Model defines the semantic exchange through which humans and other authorized participants express Intent, provide Context, resolve uncertainty, satisfy Trust and Policy requirements, confirm or modify Actions, observe execution, provide intervention, and receive verified Outcomes from Noema.

The fundamental relationship is:

PARTICIPANT
      │
      ▼
 INTERACTION
      │
      ▼
    INTENT
      │
      ▼
CONTEXT / EVIDENCE
      │
      ▼
 TRUST / POLICY
      │
      ▼
    ACTION
      │
      ▼
  EXECUTION
      │
      ▼
ENTERPRISE SYSTEM
      │
      ▼
 VERIFIED OUTCOME
      │
      ▼
 INTERACTION
      │
      ▼
PARTICIPANT

The architectural rule is:

Interaction is the participant-facing surface of Noema’s intent-to-execution lifecycle. It may provide information, resolve uncertainty, satisfy explicit execution requirements, and communicate verified state, but it must never bypass the semantic, trust, authorization, policy, action, or execution boundaries that make Noema trustworthy.