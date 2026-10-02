Below is the updated execution.md, revised in the same architectural direction as the preceding actors.md and context.md: preserving the existing reference-workflow structure and terminology while tightening the boundaries between Action, Execution, Enterprise State, Evidence, Outcome, Trust, Policy, and the model.

# Execution
Status: Reference Workflow
Version: 0.1
Domain: Reference Workflows
Canonical Path: reference-workflows/customer-account-inquiry/execution.md
⸻
## 1. Definition
Execution is the controlled process through which Noema invokes an approved Action against an enterprise capability, observes what actually occurred, verifies the required result, and records the resulting execution state and Outcome.
Within the Customer Account Inquiry workflow, Execution begins only after:
Intent
   ↓
Resolution
   ↓
Context
   ↓
Trust
   ↓
Policy
   ↓
Action
   ↓
Preconditions
   ↓
Authorization
have established that the Action is permitted and ready to execute.
Execution is therefore distinct from:
Intent
Action Selection
Planning
Model Reasoning
Enterprise Business State
Outcome
Execution represents the transition from:
what the Customer wants
to:
what the enterprise system actually did
Conceptually:
INTENT
   ↓
ACTION
   ↓
EXECUTION
   ↓
ENTERPRISE CAPABILITY
   ↓
EVIDENCE
   ↓
VERIFICATION
   ↓
OUTCOME
⸻
## 2. Purpose
The purpose of Execution is to provide a deterministic, bounded, observable, recoverable, and auditable mechanism for carrying out approved Actions.
Execution must establish, where applicable:
which Action was executed
which Action version was used
against which Resource
under which Principal
within which tenant and organizational scope
with which validated inputs
through which enterprise capability
with which execution identity
with which attempts
with what enterprise response
with what Evidence
with what verification
and with what resulting Outcome
⸻
## 3. Core Principle
Noema must distinguish between:
intended execution
and:
actual execution.
For example:
Action:
retrieve_statement
does not establish:
Statement Retrieved
Likewise:
Action Invoked
does not necessarily establish:
Action Succeeded.
Therefore:
Action Selected
      ≠
Action Invoked
      ≠
Action Executed
      ≠
Action Succeeded
      ≠
Outcome Verified
Execution state must be established from execution evidence rather than model expectation.
⸻
## 4. Execution Boundary
The Execution Boundary is the point at which Noema commits an approved Action to an enterprise capability.
Before the boundary:
Intent
   ↓
Context
   ↓
Trust
   ↓
Policy
   ↓
Action
   ↓
Preconditions
   ↓
Authorization
At the boundary:
EXECUTION REQUEST
After the boundary:
Enterprise Behavior
   ↓
Response / Event / State Observation
   ↓
Evidence
   ↓
Verification
   ↓
Execution State
   ↓
Outcome
The boundary is therefore a semantic and operational boundary.
Once crossed, Noema must distinguish what it intended to request from what the enterprise system actually performed.
⸻
## 5. Execution Preconditions
Execution must not begin until all required Preconditions have been satisfied.
For example:
get_account_balance
Preconditions:
    principal authenticated
    principal resolved
    account resolved
    account within authorized scope
    required Context available
    Action permitted
    target environment resolved
Conceptually:
Action
  ↓
Preconditions
  ↓
Satisfied?
 ├── YES → Execute
 └── NO  → Block
Missing information is not equivalent to a satisfied Precondition.
A Precondition that cannot be evaluated must remain:
UNRESOLVED
rather than being interpreted as:
SATISFIED
⸻
## 6. Execution Authorization
Authorization must be established before the Execution Boundary is crossed.
Conceptually:
Principal
    +
Action
    +
Resource
    +
Scope
    +
Policy
    ↓
Authorization Decision
For example:
Customer A
    ↓
get_account_balance
    ↓
Account A
    ↓
Authorized
    ↓
Execute
while:
Customer A
    ↓
get_account_balance
    ↓
Account B
    ↓
Unauthorized
    ↓
Do Not Execute
Noema must not infer authorization from:
customer request
authentication alone
resource identifier presence
model confidence
prior successful access
Authorization remains a Policy-governed decision.
⸻
## 7. Execution Request
Once an Action is approved, Noema constructs an Execution Request from:
Action Contract
+
validated Context
+
authorization result
+
execution metadata
Conceptually:
ExecutionRequest {
    execution_id
    action_id
    action_version
    principal
    target
    scope
    inputs
    authorization
    idempotency_key
    correlation_id
    environment
}
The request should contain only the information required by the enterprise capability.
Noema must not pass the entire Context merely because it is available.
⸻
## 8. Execution Identity
Every logical Action execution must have a stable execution identifier.
Example:
execution_id = EXE-12345
The execution identifier allows Noema to correlate:
Action
Enterprise Request
Enterprise Response
Events
Attempts
Retries
Evidence
Verification
Outcome
Audit Record
The execution identifier belongs to Noema's Execution domain.
It must remain stable across retries of the same logical Action execution.
⸻
## 9. Correlation
Noema should preserve correlation across system boundaries.
Conceptually:
Noema
   ↓
execution_id
   ↓
Integration
   ↓
enterprise_request_id
   ↓
Enterprise API
   ↓
Enterprise System
Where supported, enterprise identifiers should be retained alongside the Noema execution identifier.
Correlation must support reconstruction of:
what Noema requested
when it requested it
which enterprise request represented it
what the enterprise system returned
what Noema subsequently concluded
⸻
## 10. Action Invocation
The Action is invoked through an Integration.
Action
   ↓
Action Contract
   ↓
Integration
   ↓
Enterprise API
   ↓
Enterprise System
The Integration translates the semantic Action into the enterprise-specific protocol.
For example:
get_account_balance
        ↓
enterprise balance capability
or:
retrieve_statement
        ↓
statement retrieval API
The enterprise API implementation is not itself the semantic Action.
The Action remains defined by its contract.
⸻
## 11. Execution Does Not Depend on Model Continuation
Once Execution begins, the LLM must not be responsible for maintaining execution correctness.
The execution layer controls:
request construction
input validation
authorization enforcement
timeouts
retry behavior
idempotency
response handling
state transitions
verification
reconciliation
audit records
The model may interpret execution results where permitted.
The model must not redefine:
execution status
authorization
enterprise Business State
verification result
Outcome
Execution correctness must not depend on the model continuing to reason correctly after invocation.
⸻
## 12. Execution State
An Action execution has an explicit lifecycle.
Conceptually:
PLANNED
   ↓
READY
   ↓
EXECUTING
   ↓
SUCCEEDED
or:
EXECUTING
   ↓
FAILED
or:
EXECUTING
   ↓
UNKNOWN
or:
EXECUTING
   ↓
CANCELLED
Additional states may exist where required by the broader Execution Model.
The state machine must be explicit.
Execution state must not be inferred from natural-language model output.
⸻
## 13. Execution State vs Business State
Execution State and enterprise Business State are distinct.
For example:
Noema:
execution.status = SUCCEEDED
does not necessarily mean:
enterprise.business_state = expected_state
For:
create_complaint
Noema may establish:
execution = SUCCEEDED
while the Support System remains authoritative for:
case.status
Therefore:
Execution State
      ≠
Enterprise Business State
Noema owns the former.
The appropriate enterprise system owns the latter.
⸻
## 14. Read Execution
Most Actions in this reference workflow are read operations.
Example:
get_account_balance
Execution:
Action
   ↓
Ledger Capability
   ↓
Canonical Balance
   ↓
Evidence
   ↓
Verification
   ↓
Outcome
The Action observes enterprise state.
Noema does not become the owner of the observed Business State.
⸻
## 15. Statement Retrieval Execution
For:
retrieve_statement
the execution flow is:
Intent
   ↓
Account + Period Resolution
   ↓
Context
   ↓
Trust
   ↓
Authorization
   ↓
retrieve_statement
   ↓
Statement System
   ↓
Statement Result
   ↓
Verification
   ↓
Outcome
The retrieved Statement remains an enterprise resource.
Noema records the execution and relevant Evidence but does not become authoritative for the Statement itself.
⸻
## 16. Transaction Search Execution
For:
search_transactions
the execution request may contain:
account_id
date_from
date_to
merchant
amount
status
transaction_type
The Transaction System performs the search within its authority boundary.
Noema records:
execution
request
response
Evidence
verification
Outcome
Returned transactions remain enterprise data.
⸻
## 17. Spending Summary Execution
For:
get_spending_summary
Execution may involve:
transaction data
       ↓
aggregation capability
       ↓
spending summary
The resulting summary must retain its semantic classification.
If calculated from underlying transactions:
summary = derived
It must not silently become:
canonical Business State.
Where the aggregation capability is itself authoritative for a defined reporting value, that authority must be established by enterprise Policy and System-of-Record definitions rather than assumed by Noema.
⸻
## 18. Complaint Creation Execution
create_complaint is the principal state-changing Action in this reference workflow.
Execution:
Customer Intent
      ↓
Complaint Context
      ↓
Trust
      ↓
Authorization
      ↓
create_complaint
      ↓
Support System
      ↓
Enterprise Result
      ↓
Verification
      ↓
Outcome
Noema records that it requested the creation and whether the required execution conditions were satisfied.
The Support System remains authoritative for the resulting Case.
A successful Noema execution does not permit Noema to invent Case state not established by the Support System.
⸻
## 19. Execution Inputs
Execution inputs must come from validated Action inputs.
For example:
search_transactions {
    account_id
    date_from
    date_to
}
Once the Action is approved, the execution layer should use the validated representation.
Inputs must not be reconstructed from model memory after validation.
This creates a boundary between:
semantic interpretation
and:
executable input.
⸻
## 20. Input Validation
Before invocation, inputs must satisfy the Action Contract.
Examples:
date_from <= date_to
account_id is valid
required fields exist
types are correct
enumerated values are valid
resource scope is valid
environment is valid
Invalid inputs must prevent execution.
Invalid Input
     ↓
Execution Blocked
The execution layer must not silently repair consequential inputs unless the Action Contract explicitly permits deterministic normalization.
⸻
## 21. Resource Validation
The target Resource must remain within the authorized scope.
For example:
principal = Customer A
account = Account A
is valid only when:
Customer A
    ↓
authorized_for
    ↓
Account A
Resource resolution and authorization must remain connected throughout execution.
A Resource identifier must not be treated as sufficient proof of ownership or authorization.
⸻
## 22. Execution and Canonical Data
When an Action requires authoritative enterprise state, Execution should use the appropriate System of Record.
Example:
get_account_balance
        ↓
Ledger
        ↓
Canonical Balance
Noema should not silently substitute:
model estimate
stale projection
untrusted cache
previously observed value
when the Action Policy requires current canonical state.
If an approved fallback exists, that fallback must be explicitly defined by Action and Policy rather than invented during execution.
⸻
## 23. Execution and Evidence
Execution produces or acquires Evidence.
For example:
Ledger Response
      ↓
Execution Evidence
Evidence should preserve, where available:
source
execution_id
action_id
resource
result
observed_at
response metadata
source version
enterprise request identifier
Evidence establishes what was observed.
It does not automatically establish that every proposition inferred from the response is canonical.
⸻
## 24. Execution and Postconditions
After execution, required Postconditions must be evaluated.
Example:
create_complaint
      ↓
Support System
      ↓
case_id
      ↓
Postcondition:
case exists
The Postcondition determines whether the required result has been established.
Conceptually:
Execution Result
      ↓
Postcondition
      ↓
Satisfied?
 ├── YES → Outcome established
 └── NO  → Failure / Unknown / Recovery
⸻
## 25. Execution Verification
Execution success must be based on sufficient Evidence and verification.
Possible verification levels include:
response received
resource returned
required fields present
business result accepted
authoritative state verified
enterprise event observed
postcondition satisfied
The required verification level depends on:
Action
Action Contract
Policy
risk
enterprise semantics
Noema must not apply a single verification rule to every Action.
⸻
## 26. Execution Success
An Action may be marked:
SUCCEEDED
when its contractually required execution and verification conditions have been satisfied.
A successful transport response alone does not universally establish successful business execution.
For example:
HTTP 200
may still contain:
business_status = rejected
Therefore:
Transport Success
      ≠
Business Success
Execution must evaluate the semantic result according to the Action Contract.
⸻
## 27. Execution Failure
Execution may fail because of:
invalid input
authorization rejection
enterprise rejection
network failure
timeout
service unavailable
dependency failure
verification failure
postcondition failure
policy violation
Failure should be classified according to the Action Contract.
Conceptually:
Failure
   ↓
Failure Policy
   ├── Retry
   ├── Recover
   ├── Reconcile
   ├── Escalate
   └── Reject
Failure classification must not be invented from an ambiguous model interpretation when enterprise evidence provides a more precise state.
⸻
## 28. Unknown Execution State
Noema must distinguish:
FAILED
from:
UNKNOWN.
Example:
Noema
   ↓
create_complaint
   ↓
Support System
   ↓
request sent
   ↓
network connection lost
Noema cannot safely conclude:
FAILED
because the Case may have been created.
The correct state may therefore be:
UNKNOWN
followed by:
reconciliation
verification
or human intervention.
UNKNOWN means:
Noema lacks sufficient evidence to establish the final execution state.
It does not mean:
the Action probably failed.
⸻
## 29. Execution Timeout
A timeout means Noema did not receive the required result within the defined execution window.
It does not necessarily mean the enterprise Action did not execute.
Therefore:
Timeout
   ↓
UNKNOWN
may be more correct than:
Timeout
   ↓
FAILED
depending on Action semantics.
Timeout handling must follow the Action Contract and Failure Policy.
⸻
## 30. Execution Retry
Retries are governed by the Action Contract and Policy.
For example:
temporary network failure
        ↓
retry permitted
while:
authorization denied
        ↓
retry prohibited
Retry decisions must be deterministic and Policy-driven.
A retry must not be treated as a new logical Action unless Policy explicitly defines it as such.
⸻
## 31. Execution Idempotency
Idempotency protects against duplicate execution.
For:
create_complaint
a retry could create duplicate Cases if the enterprise capability is not idempotent.
Therefore:
execution_id
      +
idempotency_key
should identify the logical operation where the enterprise capability supports idempotency.
Noema must not assume that network retries are harmless.
Where idempotency is unavailable for a state-changing Action, the Action Contract must define the safe recovery or reconciliation behavior.
⸻
## 32. Execution Attempt
A single logical Action execution may have multiple Attempts.
Execution
   ├── Attempt 1
   ├── Attempt 2
   └── Attempt 3
The logical execution remains the same.
Each Attempt should be separately observable.
Conceptually:
Attempt {
    execution_id
    attempt_number
    started_at
    ended_at
    request_reference
    result
    failure
}
An Attempt is therefore subordinate to the logical Execution.
⸻
## 33. Execution Ordering
For compound Intents, Actions may have dependencies.
Example:
resolve_account
      ↓
search_transactions
      ↓
get_spending_summary
An Action must not execute before its required dependencies are satisfied.
Execution ordering should therefore be determined by the validated Plan and Action dependencies.
Noema must not reorder dependent Actions merely because an alternative ordering appears plausible to the model.
⸻
## 34. Parallel Execution
Independent read Actions may be executed in parallel where Policy permits.
For example:
                ┌── get_account_balance
Intent ─────────┼── retrieve_statement
                └── search_transactions
Parallelism must not violate:
authorization
data boundaries
dependency ordering
rate limits
enterprise constraints
resource consistency requirements
Parallel execution does not remove the requirement for independent Action state and Evidence.
⸻
## 35. Execution Cancellation
An execution may be cancelled before completion when Policy permits.
Possible causes:
user cancellation
timeout policy
human intervention
upstream dependency failure
policy change
Cancellation semantics must distinguish:
not started
cancelled before invocation
invocation already sent
enterprise execution unknown
This distinction is particularly important for state-changing Actions.
Once an enterprise request has crossed the Execution Boundary, local cancellation cannot be assumed to cancel the enterprise operation.
⸻
## 36. Execution Recovery
Recovery may be required when an Action ends in an uncertain state.
Example:
create_complaint
      ↓
UNKNOWN
      ↓
query Support System
      ↓
case found
      ↓
SUCCEEDED
or:
case not found
      ↓
Policy determines whether retry is safe
Recovery must not blindly repeat an Action whose prior execution may have succeeded.
Recovery must use:
execution identity
attempt history
idempotency information
enterprise evidence
Action Contract
Policy
where applicable.
⸻
## 37. Reconciliation
Reconciliation compares Noema's Execution State with authoritative enterprise state.
Example:
Noema:
execution = UNKNOWN
Support System:
case_id = 84721
status = OPEN
Reconciliation may establish:
execution = SUCCEEDED
where the Action Contract permits that conclusion.
Reconciliation is therefore a mechanism for resolving execution uncertainty using authoritative enterprise evidence.
⸻
## 38. Execution and Human Intervention
Human intervention may be required when:
execution is UNKNOWN
enterprise systems conflict
authorization is unclear
Policy requires review
recovery is unsafe
required evidence cannot be obtained automatically
Conceptually:
Execution
    ↓
Uncertainty / Exception
    ↓
Human Intervention
    ↓
Decision
    ↓
Resume / Recover / Reject / Escalate
Human intervention is part of the execution lifecycle.
A human intervention must not silently rewrite historical execution facts.
The intervention should record:
who intervened
what authority applied
what information was reviewed
what decision was made
when the decision occurred
⸻
## 39. Execution and Data Boundaries
The execution layer must enforce the Action's data boundary.
Only required inputs should cross into an enterprise Integration.
For example:
search_transactions
        ↓
account_id
date_range
filters
not:
entire Context object
This prevents accidental propagation of:
unrelated customer data
internal metadata
unnecessary Evidence
other Resource information
unrelated execution state
across enterprise boundaries.
⸻
## 40. Execution and Temporal State
Execution should preserve the relevant temporal Context.
For example:
"last month"
must already be resolved into:
date_from
date_to
timezone
before execution.
The enterprise Integration should not independently reinterpret natural-language time expressions.
Temporal interpretation belongs to Intent Resolution and validated Action inputs unless the Action Contract explicitly delegates temporal resolution to an authoritative enterprise capability.
⸻
## 41. Execution and Environment
Execution must explicitly identify the target environment where environment separation exists.
Example:
environment = production
must not accidentally resolve to:
environment = staging
Environment is part of the Execution Boundary.
A Production Action must not be satisfied using Staging Context merely because the values appear plausible.
⸻
## 42. Execution and Tenancy
Execution must preserve tenant scope.
Example:
execution
    ↓
tenant = A
    ↓
account = 123
must never silently become:
tenant = B
account = 123
even where resource identifiers are identical.
Tenant scope must remain bound to the Execution and its target Resource.
⸻
## 43. Execution and Organizational Boundaries
Where applicable, Execution must preserve organizational scope.
For example:
tenant
    ↓
organization
    ↓
business_unit
    ↓
legal_entity
    ↓
account
The enterprise authorization model determines whether the Principal may access the Resource.
Noema must not collapse these boundaries during execution.
⸻
## 44. Execution Audit Record
A consequential Execution should produce an audit record containing sufficient information to reconstruct the execution.
Conceptually:
ExecutionRecord {
    execution_id
    action_id
    action_version
    principal
    target
    scope
    environment
    input_reference
    authorization_reference
    started_at
    completed_at
    attempts
    execution_state
    result
    outcome
    evidence_reference
    verification_reference
    policy_reference
    trust_reference
    failure
}
The exact persistence model is implementation-specific.
The audit record should preserve sufficient information to answer:
what was executed
under whose authority
against which Resource
using which Action version
with which inputs
through which capability
what occurred
what Evidence was obtained
how success or failure was established
⸻
## 45. Execution Provenance
Execution provenance should establish:
who initiated execution
what Action was executed
what version was used
what Resource was targeted
what scope applied
what inputs were supplied
what enterprise capability was invoked
what enterprise response was received
what verification occurred
what Outcome was established
Provenance should distinguish:
requester
executor
enterprise system
human intervenor
source of Evidence
These may be different Actors.
⸻
## 46. Execution Observability
Execution should expose operational signals such as:
latency
attempt count
failure rate
timeout rate
unknown outcomes
verification failures
reconciliation rate
enterprise dependency health
cancellation rate
Observability must not alter semantic Execution State.
It provides visibility into Execution.
Operational telemetry must not be treated as Evidence of Business State unless explicitly defined as such.
⸻
## 47. Execution and Customer Response
The Customer-facing response must be based on the verified Outcome.
For example:
Action
   ↓
Enterprise Result
   ↓
Verification
   ↓
Outcome
   ↓
Customer Response
Noema should not tell the Customer:
"Your complaint has been created."
until sufficient Evidence establishes that the Case creation requirement was satisfied.
Similarly:
"Your balance is ₦X"
should be grounded in the appropriate authoritative balance observation rather than model expectation or unsupported Context.
⸻
## 48. Execution and Model Interpretation
The model may assist in converting an established execution result into a natural-language response.
For example:
Verified Balance Result
      ↓
LLM
      ↓
Customer-facing explanation
But the model must not change:
execution.status
enterprise state
verification result
Outcome
Evidence classification
authorization result
The model explains established execution results.
It does not define them.
⸻
## 49. Execution and Compound Intent
For compound Intent:
"Show me my balance and last month's spending."
Noema may execute:
get_account_balance
        +
get_spending_summary
Each Action must have its own:
execution identity
execution state
inputs
attempts
Evidence
verification
Outcome
The overall Intent Outcome is derived from the individual Action Outcomes.
⸻
## 50. Partial Execution
Compound execution may produce partial success.
Example:
get_account_balance
    → SUCCEEDED
get_spending_summary
    → FAILED
The overall execution must not be represented as fully successful.
The result should preserve:
Action A → SUCCEEDED
Action B → FAILED
and the overall Intent Outcome should explicitly represent the partial result.
Partial success must remain distinguishable from:
complete success
complete failure
unknown execution
⸻
## 51. Execution State Machine
The reference lifecycle can be represented as:
                ┌───────────────┐
                │    PLANNED    │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │     READY     │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │   EXECUTING   │
                └───┬─────┬─────┘
                    │     │
             success│     │failure
                    │     │
                    ▼     ▼
              ┌────────┐ ┌────────┐
              │SUCCEEDED│ │ FAILED │
              └────────┘ └────────┘
                    │
                    │
             uncertain result
                    │
                    ▼
              ┌─────────┐
              │ UNKNOWN │
              └────┬────┘
                   │
                   ▼
             RECONCILIATION
                   │
             ┌─────┴─────┐
             ▼           ▼
         SUCCEEDED    FAILED /
                      ESCALATED
Additional states may be introduced where required by the broader Execution Model.
The state machine must preserve the distinction between:
execution state
and:
enterprise Business State.
⸻
## 52. Reference Execution Flows
### Balance Inquiry
Customer
   ↓
Intent
   ↓
Resolve Account
   ↓
Context
   ↓
Trust
   ↓
Authorization
   ↓
get_account_balance
   ↓
Execution
   ↓
Ledger
   ↓
Canonical Balance
   ↓
Evidence
   ↓
Verify
   ↓
Outcome
   ↓
Respond
### Statement Retrieval
Customer
   ↓
Intent
   ↓
Resolve Account + Period
   ↓
Context
   ↓
Trust
   ↓
Authorization
   ↓
retrieve_statement
   ↓
Execution
   ↓
Statement System
   ↓
Statement
   ↓
Evidence
   ↓
Verify
   ↓
Outcome
   ↓
Respond
### Transaction Search
Customer
   ↓
Intent
   ↓
Resolve Account + Filters
   ↓
Context
   ↓
Trust
   ↓
Authorization
   ↓
search_transactions
   ↓
Execution
   ↓
Transaction System
   ↓
Transactions
   ↓
Evidence
   ↓
Verify
   ↓
Outcome
   ↓
Respond
### Spending Summary
Customer
   ↓
Intent
   ↓
Resolve Account + Period
   ↓
Context
   ↓
Trust
   ↓
Authorization
   ↓
get_spending_summary
   ↓
Execution
   ↓
Transaction / Analytics Capability
   ↓
Summary
   ↓
Verify / Classify
   ↓
Outcome
   ↓
Respond
### Complaint
Customer
   ↓
Intent
   ↓
Resolve Customer + Related Resource
   ↓
Context
   ↓
Trust
   ↓
Authorization
   ↓
create_complaint
   ↓
Execution
   ↓
Support System
   ↓
Case
   ↓
Evidence
   ↓
Verify / Reconcile
   ↓
Outcome
   ↓
Respond
⸻
## 53. Execution Invariants
### Invariant 1
An Action must not execute before required Preconditions are satisfied.
### Invariant 2
Authorization must be established before the Execution Boundary is crossed.
### Invariant 3
Execution must operate on validated Action inputs.
### Invariant 4
Execution must target an explicitly resolved Resource and scope.
### Invariant 5
Action selection, Action invocation, Action execution, and Action success are distinct semantic states.
### Invariant 6
Noema must distinguish Execution State from enterprise Business State.
### Invariant 7
Execution success must be based on sufficient execution Evidence and required verification.
### Invariant 8
A timeout must not automatically be interpreted as business failure.
### Invariant 9
Unknown execution state must remain distinct from failure.
### Invariant 10
Retries must follow explicit Action Contract and Policy semantics.
### Invariant 11
State-changing Actions must have explicit idempotency or safe-recovery semantics.
### Invariant 12
A retry must not blindly duplicate an Action whose prior execution may have succeeded.
### Invariant 13
Postconditions must be evaluated according to the Action Contract.
### Invariant 14
Consequential Execution must retain sufficient provenance for audit and reconstruction.
### Invariant 15
Only the minimum required Context should cross an Integration boundary.
### Invariant 16
Execution must preserve tenant, organizational, resource, legal, and environment boundaries where applicable.
### Invariant 17
The model must not redefine Execution State after the Execution Boundary.
### Invariant 18
Model interpretation of an execution result must not alter the underlying Outcome.
### Invariant 19
Enterprise Systems remain authoritative for Business State within their defined authority boundaries.
### Invariant 20
Noema remains authoritative for its own Execution State.
### Invariant 21
Unknown execution outcomes must have an explicit recovery, reconciliation, or escalation path where applicable.
### Invariant 22
Human intervention must be represented as an explicit execution transition or state rather than an informal exception.
### Invariant 23
Compound executions must preserve the independent state and Outcome of each Action.
### Invariant 24
Partial execution success must remain distinguishable from complete success.
### Invariant 25
Customer-facing responses must reflect verified Outcomes rather than model expectations.
### Invariant 26
Execution identity must remain stable across Attempts belonging to the same logical Action execution.
### Invariant 27
Each execution Attempt must remain distinguishable from the logical Execution.
### Invariant 28
Transport-level success must not be treated as semantic business success without the required verification.
### Invariant 29
An enterprise response must not be treated as authoritative beyond the authority boundary of the producing system.
### Invariant 30
Noema must not silently substitute stale, inferred, or model-generated data for required canonical enterprise state.
### Invariant 31
Execution cancellation after invocation must not be represented as successful cancellation unless the enterprise system establishes that the underlying operation was cancelled.
### Invariant 32
Execution recovery must not rely on reconstruction from model memory.
### Invariant 33
Execution Evidence must remain distinguishable from interpretation derived from that Evidence.
### Invariant 34
The Execution layer must not silently broaden the Action's Context or data boundary.
### Invariant 35
An Execution Outcome must be established from what occurred and what can be verified, not from what was intended.
⸻
## 54. Final Definition
Execution is the controlled, deterministic, bounded, and auditable process by which Noema invokes an approved Action against an enterprise capability, observes what actually occurred, verifies the required result, records the execution journey, and establishes the resulting Outcome.
The fundamental relationship is:
INTENT
   │
   ▼
CONTEXT
   │
   ▼
TRUST + POLICY
   │
   ▼
ACTION
   │
   ▼
PRECONDITIONS
   │
   ▼
AUTHORIZATION
   │
   ▼
EXECUTION REQUEST
   │
   ▼
EXECUTION BOUNDARY
   │
   ▼
ENTERPRISE CAPABILITY
   │
   ▼
ENTERPRISE RESULT
   │
   ▼
EVIDENCE
   │
   ▼
VERIFICATION
   │
   ▼
POSTCONDITIONS
   │
   ▼
OUTCOME
   │
   ├── SUCCEEDED
   ├── FAILED
   ├── UNKNOWN
   └── PARTIAL
And the architectural rule is:
Noema must never confuse an intended Action with an executed Action, an executed Action with a successful Action, or a successful Action with an established Outcome.
Execution is established by what the enterprise system actually did, what Evidence was obtained, and what Noema can verify—not by what the model expected to happen.