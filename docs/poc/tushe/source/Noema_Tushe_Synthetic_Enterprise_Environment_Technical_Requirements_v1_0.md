NOEMA × TUSHE




Synthetic Enterprise
Environment

Technical Requirements & Acceptance
Specification




Version 1.0
Prepared by Noema for the Tushe team




CONFIDENTIAL — FOR THE TUSHE TEAM
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                           Technical Requirements & Acceptance Specification · v1.0




Contents
What We Are Asking For, in One Paragraph . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

1. Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

2. Design principles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

3. Synthetic enterprise architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

4. Domain model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5

5. State models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

6. Unknown outcomes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

7. Deterministic chaos / failure injection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

8. Scenario engine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

9. Controlled time . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

10. Events & webhooks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

11. Idempotency & concurrency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9

12. Identity, authorization & business policy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

13. Nigerian payment-rail semantics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

14. Evidence, reconciliation & timeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

15. Ground truth, control plane & isolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

16. Synthetic data & test isolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

17. API & integration contract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

18. Audit, provenance & observability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

19. Access & mutation boundary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

20. Non-functional requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15

21. Required deliverables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

22. Acceptance criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16

23. Minimum scenario pack for initial readiness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

24. What we’d like Tushe to confirm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

25. Readiness sign-off . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

Appendix A — Example composite scenario . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19

Appendix B — Glossary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20




Confidential — for the Tushe team                                                                                           Page 2
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                            Technical Requirements & Acceptance Specification · v1.0




What We Are Asking For, in One Paragraph
We would like to use the Tushe platform as a synthetic enterprise environment — a controlled, realistic stand-in for a live
fintech’s transaction and operations landscape that we can integrate against and test repeatedly. We are not asking for a
customer-facing banking product or a polished demo. We are asking for an environment that behaves like real enterprise
infrastructure behaves on its bad days: multiple systems that don’t always agree, state that arrives late, events that duplicate or
go missing, outcomes that can’t be read off a single response, and failures we can reproduce on demand. This document
describes exactly what that environment must do, and how we will jointly confirm it is ready.


   THE ONE PRINCIPLE BEHIND EVERYTHING HERE

   The environment must make shortcuts fail.
   It should not be possible to determine the correct outcome of a transaction by reading one convenient status field.
   Independent evidence has to exist across systems, some of it delayed or conflicting, so that the true outcome must be
   investigated and reconciled rather than simply read. If a clean happy-path API were enough, we wouldn’t need Tushe
   for this. Making that difficulty real, controllable, and repeatable is the whole job.


A short note on why this matters to us: our software’s entire purpose is to act safely and correctly against messy enterprise
reality. We can only prove it does that if we test it somewhere the mess is genuine but controlled. That is the role we’re asking
Tushe to play. Everything below serves that single goal — nothing more, nothing less.

Requirements are tagged P0 (required before we begin integration) or P1 (required before serious end-to-end testing).
Where a capability isn’t native to Tushe today, we’re glad to discuss an agreed control hook rather than assume it must be
rebuilt — see §24.



1. Scope

Tushe provides — the synthetic enterprise substrate:
 • A realistic synthetic financial domain and its underlying state.
 • Independent representations of the same business event across several logical systems.
 • Controlled asynchronous processing, delayed outcomes, and state transitions.
 • Deterministic, reproducible failure conditions — natively, or through agreed control hooks.
 • A privileged, isolated ground-truth view for testing and acceptance.
 • Controllable time, events, scenarios, seed data, reset, and replay.
 • Versioned, documented API and event contracts.
 • Enough diagnostics to tell a simulator defect apart from an injected fault or an integration bug.
Explicitly not required — please don’t build these:
 • A consumer-facing banking or mobile application.
 • A complete core-banking product beyond the domains named here.
 • A general workflow, reporting, or automation suite.
 • Any real customer data, production credentials, or production integrations.




Confidential — for the Tushe team                                                                                            Page 3
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                              Technical Requirements & Acceptance Specification · v1.0



The discipline cuts both ways: depth in a small number of domains is far more valuable to us than shallow coverage of many
banking features.



2. Design principles

 PRINCIPLE                          WHAT IT MEANS FOR THE BUILD


 Not CRUD-only                      Model state, lifecycle, events, failure, and reconciliation — not just request/response.

 Multi-system                       Represent one business event independently across the relevant domains.

 Controlled inconsistency           Configured systems may deliberately disagree, without the environment losing authoritative
                                    ground truth.

 Deterministic                      A named scenario plus a seed must reproduce the same material behaviour every time.

 Ground truth is sacred             Authoritative internal state is kept separate from what an ordinary client can observe.

 Isolation                          Control and ground-truth capabilities are never reachable with ordinary integration credentials.

 Synthetic realism                  Realistic Nigerian fintech/payment semantics, with entirely synthetic data.

 Safe mutation                      Money-moving capabilities exist for realism but are independently gated and off by default
                                    (§19).

 Observable to us                   Requests, transitions, events, and injected faults are traceable in privileged diagnostics.




3. Synthetic enterprise architecture
The environment must expose the following logical domains. They may share physical infrastructure internally, as long as each
one’s state and behaviour is independently observable and controllable.

 LOGICAL DOMAIN                     MINIMUM RESPONSIBILITY


 Customer / Identity                Synthetic customers, identity/KYC state, risk tier, customer-to-account relationships.

 Accounts / Ledger                  Accounts, balances, holds, and strict double-entry postings.

 Transaction Service                Business transaction lifecycle, references, status, and history.

 Payment Switch / Rail              An independent downstream processing state, with its own reference and response semantics.

 Beneficiary / Name Enquiry         Beneficiary records and account-name validation, including ambiguity and mismatch.

 Settlement                         Settlement lifecycle, including delayed and batched settlement and its evidence.

 Events / Webhooks                  Asynchronous state-change events and their delivery behaviour.

 Case / Dispute                     Operational complaint/dispute records and their lifecycle.

 Policy / Authorization             Roles, capabilities, business restrictions, and approval requirements.



Confidential — for the Tushe team                                                                                                 Page 4
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                               Technical Requirements & Acceptance Specification · v1.0




 LOGICAL DOMAIN                       MINIMUM RESPONSIBILITY


 Audit / Provenance                   Immutable record of material state changes with causal metadata.


SE-01               Independent system state
 P0                 Ledger, transaction, switch, settlement, and beneficiary/credit state must be independently queryable.

SE-02               Cross-system divergence
 P0                 The environment must support configured cases where two or more systems report different states for the same
                    business event.

SE-03               Correlation
 P0                 A business event must be traceable across system-specific identifiers via a shared correlation/reference model.

SE-04               No forced convergence
 P0                 A change in one system must not automatically make every other system synchronously consistent, unless the
                    scenario is configured that way.




4. Domain model

4.1 Customers & Identity
Synthetic customer IDs and stable identity references; profile and status; configurable KYC state and timestamps; synthetic
BVN/NIN-style identifiers where useful (never real ones); risk tier and restrictions; customer-to-account relationships; and the
ability to hold duplicate, partial, stale, or ambiguous identity records.


4.2 Accounts & Balances
Account ID, owning customer, status, and currency; ledger balance and available balance; pending amounts and holds; account
restrictions and status changes; account transaction history; and multiple accounts per customer.


4.3 Ledger

LED-01              Double-entry integrity
 P0                 Every authoritative posting maintains balanced debit/credit entries.

LED-02              Ledger metadata
 P0                 Entries carry entry ID, transaction/reference ID, account ID, direction, amount, currency, posting timestamp,
                    sequence/version, and correlation reference.

LED-03              Pending & compensating entries
 P1                 Support holds, pending postings, releases, reversals, and compensating entries.

LED-04              Partial / uncertain posting
 P0                 Support a controlled scenario where one leg posts and another is delayed or uncertain, while ground truth remains
                    known.




Confidential — for the Tushe team                                                                                                   Page 5
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                   Technical Requirements & Acceptance Specification · v1.0




LED-05                Money representation
 P0                   Integer minor units (kobo for NGN) or exact decimal arithmetic. Floating-point money is not acceptable.

LED-06                Fees & net amounts
 P1                   Support configurable fees/charges so that gross, fee, and net amounts can be reconciled against each other.



4.4 Cross-system references
A single transaction should be able to carry or link, as applicable: a client/request reference, a transaction-service ID, a ledger
posting reference, a switch/session reference, an RRN-style reference, a settlement reference, a beneficiary-credit reference, a
case/dispute reference, and event IDs. Discovering that these all describe one underlying event is exactly the kind of work the
environment needs to make necessary.



5. State models
Transaction, settlement, beneficiary credit, case, and dispute are separate lifecycles. They must not be collapsed into one flat
transaction status, because several of them are legitimately true at the same time — a transaction can be PROCESSING while
settlement is PENDING and beneficiary credit is UNKNOWN.

 LIFECYCLE                    MINIMUM STATES


 Transaction                  CREATED | INITIATED | SUBMITTED | PROCESSING | SUCCESSFUL | FAILED                             | REJECTED
                              | TIMED_OUT | EXECUTION_OUTCOME_UNKNOWN | DUPLICATE | PARTIAL


 Settlement                   NOT_REQUIRED      | PENDING     | SETTLED     | FAILED     | REVERSED      | UNKNOWN


 Beneficiary credit           NOT_APPLICABLE       | PENDING     | CREDITED     | NOT_CREDITED       | UNKNOWN


 Case / resolution            NOT_OPEN | OPEN | INVESTIGATING              | AWAITING_EXTERNAL_RESPONSE           | ACTION_REQUIRED
                              | ESCALATED | RESOLVED | CLOSED


 Dispute                      NONE    | OPEN    | UNDER_REVIEW       | UPHELD     | REJECTED     | RESOLVED



STM-01                Transition contract
 P0                   Document the legal transitions, terminal states, and the trigger (time or event) for each lifecycle.

STM-02                State invariants
 P0                   Document which states must never coexist in authoritative state (e.g. a transaction cannot be both SUCCESSFUL
                      and REJECTED in the same authoritative version).

STM-03                Transition history
 P0                   Historical transitions must be queryable with timestamps and causal metadata.




Confidential — for the Tushe team                                                                                                    Page 6
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                 Technical Requirements & Acceptance Specification · v1.0




6. Unknown outcomes
This is the single most important behaviour in the environment, so we’re calling it out on its own.

UNK-01              Post-commit unknown
 P0                 Support the case where an operation commits internally but the initiating request returns a timeout, 5xx, or
                    disconnect, so the client never learns the outcome.

UNK-02              Pre-commit uncertainty
 P0                 Support failures where no commit occurred but the client still receives an ambiguous transport-level failure.

UNK-03              Evidence retrieval
 P0                 Expose enough independent evidence to investigate an unknown outcome — without revealing privileged ground
                    truth.

UNK-04              Never normalise
 P0                 The environment must not silently convert an unknown transport outcome into a confirmed success or failure.
                    “Unknown” has to survive as a real, observable condition.




7. Deterministic chaos / failure injection
Controlled fault injection is a first-class requirement. Randomness alone is not sufficient — every important failure must be
reproducible from a scenario ID and seed. Native support is preferred; where a behaviour is better implemented at the edge, a
stable control hook that permits deterministic injection is acceptable.

 FAILURE CLASS                        REQUIRED EXAMPLES


 Transport                            Timeout, disconnect, connection reset, 502/503/504, delayed response.

 Application                          Validation failure, authorization failure, conflict, 429/rate limit, dependency unavailable.

 State                                Stale read, missing record, duplicate record, contradictory state, partial state.

 Execution                            Commit-then-timeout, partial execution, silent success, silent failure, recovery timeout.

 Events                               Duplicate, missing, delayed, out-of-order, replayed, malformed, stale-version.

 Identity                             Ambiguous match, duplicate identity, stale identity, name mismatch.

 Policy / auth                        Authorization denied, approval required, stale authorization, policy change mid-flight.


CHA-01              Scenario ID
 P0                 Every controlled run has a unique scenario/run identifier.

CHA-02              Deterministic seed
 P0                 Fault generation supports a seed; the same scenario + seed reproduces the same material fault sequence.

CHA-03              Scripted faults
 P0                 Support explicit scripts such as commit then return 504, drop event X, deliver event Y twice, return stale state for N
                    seconds.



Confidential — for the Tushe team                                                                                                    Page 7
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                 Technical Requirements & Acceptance Specification · v1.0




CHA-04              Scoped faults
 P1                 Faults can be applied at the system, endpoint, transaction, request, event, or scenario level.

CHA-05              Hidden injection
 P0                 Injected conditions are visible in privileged diagnostics but never disclosed to the ordinary integration client as a
                    shortcut.

CHA-06              Fault trace
 P0                 Diagnostics record what was injected, when, against what target, the configured behaviour, and the actual
                    underlying outcome.




8. Scenario engine
Named, reproducible scenarios — not manual reconstruction of failures each time.

SCN-01              Scenario definition
 P0                 A scenario defines initial state, the resources involved, injected faults, the event schedule, timing, the authoritative
                    outcome, and the invariants that must hold.

SCN-02              Reset & replay
 P0                 A scenario can be reset and replayed with no manual database intervention.

SCN-03              Composite failures
 P0                 Scenarios can combine multiple simultaneous or ordered faults; real incidents rarely arrive one at a time.

SCN-04              Authoritative outcome
 P0                 Each scenario retains the authoritative final state needed to grade a run.


The concrete starting set is listed in §23.



9. Controlled time
Financial systems are temporal, and we can’t wait real hours for settlement or reversal windows during testing.

TIM-01              Virtual clock
 P0                 Provide a controllable simulated clock or an equivalent deterministic time mechanism.

TIM-02              Freeze & advance
 P0                 The control plane can freeze and advance simulated time.

TIM-03              Temporal metadata
 P0                 Expose the relevant timestamps where applicable: occurred, processed, posted, settled, delivered, observed.

TIM-04              Scheduled transitions
 P0                 Delayed settlement, delayed credit, and event delivery must be schedulable and replayable against the simulated
                    clock.




Confidential — for the Tushe team                                                                                                     Page 8
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                Technical Requirements & Acceptance Specification · v1.0




10. Events & webhooks

EVT-01              Event schema
 P0                 Events carry event ID, type, aggregate/resource ID, version/sequence where applicable,
                    occurred/published/delivered timestamps, correlation ID, causation ID, and payload.

EVT-02              Duplicate delivery
 P0                 Support both the same event delivered twice and the same business effect represented by two different event IDs.

EVT-03              Ordering
 P0                 Support deliberate reordering while retaining sequence information.

EVT-04              Loss, delay, replay
 P0                 Support dropped, delayed, and replayed events, including a late event arriving after a later case state.

EVT-05              Authenticity
 P1                 Where webhooks are used, provide HMAC signing or equivalent, with documented replay protection.

EVT-06              Delivery history
 P0                 Privileged diagnostics expose delivery attempts and outcomes.




11. Idempotency & concurrency

IDP-01              Idempotency contract
 P0                 Define key scope, enforcement, persistence, and required behaviour for every state-mutating endpoint.

IDP-02              Same key, same payload
 P0                 A repeated equivalent request must not create a second business effect.

IDP-03              Same key, different payload
 P0                 A different request under the same key returns a deterministic conflict.

IDP-04              Retry after timeout
 P0                 Support the case where the first request may already have committed before the timeout, and a retry then arrives
                    with the same key.

IDP-05              Different keys, same operation
 P0                 Support controlled duplicate-business-operation scenarios.

IDP-06              Retention
 P0                 Document idempotency-key TTL/retention and persistence.

CON-01              Concurrency control
 P1                 Support versioning / optimistic concurrency (e.g. version or ETag) so stale mutations can be detected.

CON-02              Concurrent modification
 P0                 Provide scenarios where a resource changes between our read and our subsequent operation.




Confidential — for the Tushe team                                                                                                Page 9
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                Technical Requirements & Acceptance Specification · v1.0




12. Identity, authorization & business policy
The environment must distinguish technical authentication (is this a valid credential?) from business authorization (is this actor
actually allowed to do this, at this amount, under this policy?).

 CAPABILITY                           REQUIRED BEHAVIOUR


 Principal                            Synthetic users/services with stable identity.

 Role                                 Configurable role / organisational assignment.

 Capability                           Explicit action-level permissions.

 Resource scope                       Authorization tied to customer / account / transaction / tenant.

 Amount threshold                     Rules that depend on transaction value.

 Approval                             Actions that require an additional approval step.

 Restrictions                         Account / customer / transaction restrictions that block an otherwise valid operation.

 Policy version                       Rules that are versioned and time-aware.

 Stale authorization                  Authority that changes between observation and execution.

 IAM instability                      Injected 401/403 that is distinguishable, in privileged diagnostics, from genuine configuration.


AUTH-01             Business authorization
 P0                 Support cases where authentication succeeds but business authority is insufficient.

AUTH-02             Approval states
 P1                 Support pending, granted, rejected, and expired approvals.

AUTH-03             Policy mutation
 P0                 Policy versions and effective times are queryable and reproducible, including a policy that changes during an
                    in-flight scenario.

AUTH-04             Tenant / resource isolation
 P0                 Cross-tenant and cross-resource access fails deterministically and is testable.




Confidential — for the Tushe team                                                                                                 Page 10
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                Technical Requirements & Acceptance Specification · v1.0




13. Nigerian payment-rail semantics
Because this environment models a Nigerian fintech, it should reflect Nigerian payment concepts rather than generic
international abstractions.

 • NUBAN-style account numbers and bank identifiers, using synthetic values.
 • Name Enquiry / account-name validation around transfer initiation.
 • NIP-style transfer and session references, and RRN-style identifiers where applicable.
 • A documented response-code taxonomy that clearly separates success, pending, rejected, and timeout/unknown/retryable
   conditions.
 • Interbank transfer processing and settlement behaviour.
 • Debited-but-not-credited scenarios, with configurable auto-reversal / reconciliation windows.
 • Failed transaction, duplicate debit, erroneous transfer, reversal, and dispute cases.
 • NGN throughout, at kobo-level precision.

NG-01               Rail semantics
 P0                 Payment-rail behaviour follows the agreed Nigerian model and is documented in the API/event contract.

NG-02               Reference propagation
 P0                 Session/reference identifiers stay traceable across transaction, switch, settlement, ledger, and event records.

NG-03               Response taxonomy
 P0                 Codes clearly distinguish a confirmed failure from an unresolved outcome, and are stable and documented.




14. Evidence, reconciliation & timeline

REC-01              Transaction history
 P0                 Provide a chronological history of material transaction state changes.

REC-02              Timeline
 P0                 Provide a timeline correlating request, ledger posting, switch interaction, settlement, beneficiary credit, and event
                    delivery.

REC-03              Evidence by source
 P0                 Expose source-specific records without collapsing them into one synthesised answer.

REC-04              Reconciliation surface
 P0                 Provide machine-readable access to the records needed to compare transaction, ledger, switch, settlement, and
                    beneficiary state.

REC-05              Preserve contradictions
 P0                 Conflicting source records remain independently retrievable; the environment must not “resolve” them for us.




Confidential — for the Tushe team                                                                                                 Page 11
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                               Technical Requirements & Acceptance Specification · v1.0



Illustrative timeline for one transaction:

 TIME              SOURCE                              OBSERVED EVENT


 10:00:01          Transaction service                 Request received

 10:00:02          Ledger                              Debit committed

 10:00:31          API                                 Client response timed out

 10:00:34          Payment switch                      Accepted

 10:00:37          Events                              Webhook delivered

 10:01:02          Settlement                          Pending

 10:03:15          Beneficiary                         Credit not yet confirmed




15. Ground truth, control plane & isolation
Non-negotiable. The environment must maintain authoritative ground truth separately from the ordinary integration surface.
Ground truth exists for testing and acceptance only, and must never be reachable with ordinary integration credentials.
Without a trusted, isolated way to ask “what actually happened?”, we cannot objectively grade a run — this is as important as
the chaos engine itself.

GT-01               Authoritative state
 P0                 Maintain authoritative internal state for actual commits, events, and scenario configuration.

GT-02               Privileged oracle
 P0                 Provide a privileged read that establishes the actual underlying outcome, independent of whatever response the
                    integration client received.

GT-03               No ordinary-client access
 P0                 Ordinary integration credentials cannot reach ground-truth or control-plane endpoints.

GT-04               Run trace
 P0                 Ground truth shows the actual sequence of state changes and injected conditions for a run.

GT-05               Export
 P1                 Ground-truth state, event history, and scenario metadata are exportable in machine-readable form.


Control-plane capabilities P0: create/load a scenario · seed/reset the environment · set and reproduce a seed · configure a
fault profile · freeze/advance the clock · schedule/drop/delay/reorder events · snapshot · restore · replay · inspect ground truth
· export run artefacts.




Confidential — for the Tushe team                                                                                              Page 12
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                Technical Requirements & Acceptance Specification · v1.0




16. Synthetic data & test isolation

DATA-01             Synthetic only
 P0                 No production customer, account, identity, transaction, or credential data.

DATA-02             Deterministic seed data
 P0                 Seed datasets for customers, accounts, transactions, beneficiaries, settlements, events, and cases.

DATA-03             Scale tiers
 P1                 At least small, medium, and large datasets, enough for realistic histories and concurrent activity.

DATA-04             Adversarial data
 P0                 Fixtures or generation for duplicate customers, similar/ambiguous names, multiple matching accounts, repeated
                    amounts, stale records, and conflicting metadata — enough that a trivial single-record lookup is never sufficient.

DATA-05             Isolation
 P0                 Parallel developer/CI runs must not corrupt one another’s state.

DATA-06             Reset
 P0                 An environment can be reset to a known baseline without manual database work.




17. API & integration contract
Exact URL paths can be agreed jointly; the capabilities below are what we need.

 DOMAIN                               MINIMUM CAPABILITIES


 Customer                             Get customer; list accounts; get identity/KYC; get risk/restrictions.

 Account                              Get account; balances; ledger; holds/pending; account transactions.

 Transaction                          Get transaction; query/search; history/timeline; linked events & references.

 Beneficiary                          Name enquiry/resolve; match quality; ambiguity outcomes.

 Switch                               Independent downstream switch transaction/reference state.

 Settlement                           Settlement state/history and delayed-settlement behaviour.

 Case / Dispute                       Create/query/update a case or dispute; retrieve linked evidence.

 Evidence / Audit                     Transaction-linked evidence, audit history, and state transitions.

 Reconciliation                       Source-specific records to compare transaction / ledger / switch / settlement / beneficiary.

 Events                               Delivery/subscription plus event detail and delivery metadata.


API-01              OpenAPI
 P0                 A complete, machine-readable OpenAPI specification.




Confidential — for the Tushe team                                                                                                Page 13
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                Technical Requirements & Acceptance Specification · v1.0




API-02              Versioning
 P0                 A defined versioning and backward-compatibility policy for the POC window.

API-03              Error contract
 P0                 Documented HTTP status, business error codes, retryability, and known/unknown outcome semantics.

API-04              Correlation
 P0                 Request ID and correlation ID propagate across API, event, and audit records.

API-05              Pagination & filtering
 P1                 Documented, stable pagination and query semantics for large histories.


For every mutating operation, please document: authentication/authorization, request/response schema, error schema,
idempotency, side effects, correlation IDs, timeout/latency behaviour, retry safety, and how success can be verified.



18. Audit, provenance & observability

AUD-01              Immutable audit
 P0                 Append-only or tamper-evident records of material state changes.

AUD-02              Transition provenance
 P0                 Each record captures actor, actor type, request ID, correlation ID, causation ID, source system, previous and new
                    state, and timestamps.

AUD-03              Policy provenance
 P1                 Record the applicable policy/version for policy-governed actions.

AUD-04              Event provenance
 P0                 Link events to the causal request or state transition.

AUD-05              Audit query
 P0                 Retrieve by transaction, account, customer, case, and correlation/reference ID.

OBS-01              Diagnostic visibility
 P0                 Privileged diagnostics distinguish domain behaviour, injected fault, infrastructure error, and client error — so we
                    can always answer “was that our bug, or the simulator?”

OBS-02              Fault visibility
 P0                 Diagnostics expose the injected fault, the actual outcome, and event delivery history.

OBS-03              Latency
 P1                 Capture request/event latency and the relevant configured vs actual timestamps.




Confidential — for the Tushe team                                                                                                 Page 14
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                Technical Requirements & Acceptance Specification · v1.0




19. Access & mutation boundary
Please read this one carefully — it governs what our integration credentials may do. The environment may fully support
money-moving operations (reversals, credits, compensating entries) for realism and for later phases. For the initial phase,
however, the credentials we integrate with must be restricted to reads, investigation, and non-monetary case operations.
Money-moving operations must be independently gated and off by default for our integration, enabled only by explicit written
agreement.

MUT-01              Independent permissioning
 P0                 Financial-mutation capabilities are permissioned separately from read/investigation capabilities.

MUT-02              Simulation integrity
 P0                 Any supported reversal, credit, or compensating behaviour is represented consistently across ledger and audit
                    state.

MUT-03              Initial read-first access
 P0                 Our initial credentials are constrained to the agreed non-monetary capability set.

MUT-04              Preview capability
 P1                 Where feasible, provide non-mutating eligibility/preview operations for financial actions (i.e. “would this be
                    allowed, and what would it do?” without doing it).




20. Non-functional requirements

 AREA                                 REQUIREMENT


 Reliability                          The environment stays stable while it simulates downstream unreliability.

 Determinism                          Named scenarios and seeds are replayable.

 Latency                              Normal and degraded latency profiles are configurable; exact values agreed for the POC
                                      workload.

 Concurrency                          Concurrent transactions and isolated parallel test runs are supported.

 Data volume                          Histories are large enough to exercise pagination and reconciliation.

 Availability                         Available across the agreed POC testing window.

 Observability                        Simulator faults are diagnosable independently of injected faults.

 Compatibility                        API and event contracts are stable within the agreed POC version.




Confidential — for the Tushe team                                                                                                    Page 15
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                               Technical Requirements & Acceptance Specification · v1.0




21. Required deliverables

 DELIVERABLE                         MINIMUM CONTENT


 Synthetic environment               An accessible environment with the agreed domains, behaviour, and seeded data.

 OpenAPI specification               A versioned, machine-readable REST contract.

 Event specification                 Schemas, delivery semantics, and the authenticity mechanism.

 State model                         Separate lifecycle diagrams with transitions, triggers, and invariants.

 Scenario pack                       The agreed initial adversarial scenarios, with reproducible configuration.

 Control-plane API                   Scenario, seed, clock, fault, reset, snapshot/replay, and diagnostics.

 Ground-truth interface              Privileged authoritative state and run-artefact access, isolated from ordinary integration.

 Seed datasets                       Deterministic synthetic data at the agreed scale tiers.

 Credentials                         Least-privilege integration credentials, separate from control/diagnostic credentials.

 Runbook                             Setup, reset, scenario execution, troubleshooting, and known limitations.

 Acceptance evidence                 Evidence that all P0 acceptance criteria (§22) have been demonstrated.




22. Acceptance criteria
The environment is ready for meaningful integration once these are demonstrated in a joint session. All are P0.

 ID         TEST                    HOW WE CHECK                                        PASS CONDITION

 AT-01      Deterministic replay    Run the same scenario twice with the same           Material fault sequence and authoritative
                                    seed.                                               outcome reproduce.

 AT-02      Ground-truth            Attempt ground-truth access with ordinary           Access denied.
            isolation               credentials.

 AT-03      Post-commit             Run commit-then-timeout.                            Client sees ambiguity; privileged oracle
            timeout                                                                     confirms the actual outcome.

 AT-04      Stale state             Write, then read under a stale-state profile.       Read returns the configured prior version;
                                                                                        authoritative state stays correct.

 AT-05      Event loss              Drop a configured event.                            State changes; event absent from normal
                                                                                        delivery; diagnostics show the drop.

 AT-06      Duplicate event         Duplicate a configured event.                       Configured duplicate deliveries occur and are
                                                                                        traceable.

 AT-07      Out-of-order event      Reorder configured events.                          Events arrive in the configured order with
                                                                                        sequence metadata intact.




Confidential — for the Tushe team                                                                                                  Page 16
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                 Technical Requirements & Acceptance Specification · v1.0




 ID         TEST                      HOW WE CHECK                                       PASS CONDITION

 AT-08      Cross-system              Configure ledger/switch/settlement                 Each source stays independently queryable
            conflict                  disagreement.                                      and contradictory.

 AT-09      Ambiguous                 Run an ambiguous name enquiry.                     Multiple/conflicting candidates returned; no
            beneficiary                                                                  silent auto-selection.

 AT-10      Idempotency               Reuse a key with a different payload.              Deterministic conflict; no unintended second
            conflict                                                                     effect.

 AT-11      Retry after timeout       Time out the first request, retry the same key.    Configured business-effect semantics
                                                                                         reproduce deterministically.

 AT-12      Authorization             Use an authenticated but unauthorized              Action denied, with a traceable reason.
            boundary                  principal.

 AT-13      Policy mutation           Change policy during a scenario.                   Both policy versions and their effective times
                                                                                         are traceable.

 AT-14      Concurrent update         Modify a resource between read and                 Stale/concurrent mutation detected as
                                      mutation.                                          documented.

 AT-15      Time control              Freeze, then advance the clock.                    Scheduled transitions fire according to
                                                                                         simulated time.

 AT-16      Reset & replay            Reset, then replay a named scenario.               No manual reconstruction required.

 AT-17      Ground-truth              Export a completed run.                            Machine-readable scenario/state/event
            export                                                                       artefacts are produced.

 AT-18      Mutation isolation        Attempt a monetary mutation with initial           Denied unless explicitly enabled.
                                      credentials.

 AT-19      Audit completeness        Inspect a material transition.                     Actor / request / correlation / state /
                                                                                         timestamp metadata all present.

 AT-20      Simulator                 Trigger an injected fault and a genuine            Privileged diagnostics tell them apart.
            diagnostics               platform error separately.




23. Minimum scenario pack for initial readiness

 #       SCENARIO                              REQUIRED CONDITION


 1       Normal successful transfer            Relevant systems converge normally.

 2       Failed before commit                  No financial mutation occurs.

 3       Commit then timeout                   Authoritative commit occurs; client outcome is unknown.

 4       Debited / not credited                Originating debit established; beneficiary credit absent or pending.

 5       Duplicate webhook                     Same logical event delivered multiple times.



Confidential — for the Tushe team                                                                                                  Page 17
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                                Technical Requirements & Acceptance Specification · v1.0




 #      SCENARIO                           REQUIRED CONDITION


 6      Missing webhook                    State changes without the expected event.

 7      Out-of-order webhook               Events arrive out of causal order.

 8      Stale read                         Read returns a prior version after a successful write.

 9      Contradictory evidence             Independent systems report different outcomes.

 10     Delayed settlement                 Outcome established while settlement stays pending.

 11     Beneficiary ambiguity              Name/account resolution returns multiple or conflicting matches.

 12     Duplicate submission               Repeated request tests deduplication.

 13     Recovery uncertainty               A recovery/retry operation itself becomes unknown.

 14     Unauthorized principal             Authentication succeeds; business authority is insufficient.

 15     Approval required                  Action requires an additional approval.

 16     Policy changed                     Applicable rule changes mid-scenario.

 17     Concurrent modification            State changes between read and mutation.

 18     Malformed / stale event            Event is invalid or references an old version.

 19     Impossible state                   A controlled invariant violation is introduced.

 20     Composite failure                  Several independent faults occur in one scenario.




24. What we’d like Tushe to confirm
So we can plan realistically, please respond to each item with Supported / Requires extension / Not supported, plus a short
implementation note where useful.

 • Which of the logical domains (§3) exist natively today?
 • Which failure/chaos behaviours (§7) are available natively?
 • Which behaviours would need custom work or a control hook?
 • Can you provide an isolated, privileged ground-truth read path (§15)?
 • Can you provide deterministic scenario IDs and seeded, replayable execution (§7–8)?
 • Can you provide a controllable virtual clock (§9)?
 • Can you expose independent ledger, transaction, switch, settlement, and beneficiary state (§3)?
 • Can you preserve cross-system inconsistencies without normalising them (§14)?
 • Can you provide event loss / delay / duplication / reordering controls (§10)?
 • Can you provide reset / snapshot / restore / replay (§8, §15)?
 • Can you provide isolated environments for parallel testing (§16)?
 • What are the expected delivery dates for the P0 capabilities?


Confidential — for the Tushe team                                                                                               Page 18
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                             Technical Requirements & Acceptance Specification · v1.0



 • What known limitations should we document before integration?
We’re very open to using existing Tushe capabilities wherever they already fit — the aim is to get to a reliable, reproducible
environment quickly, not to have you rebuild things you already do well. Where something isn’t native, we’d rather hear that
early and design an agreed hook together than discover it mid-integration.



25. Readiness sign-off
The environment is accepted for integration when:

 • All P0 requirements are implemented, or explicitly accepted as agreed exceptions.
 • All P0 acceptance tests (§22) pass.
 • The minimum scenario pack (§23) is executable and reproducible.
 • OpenAPI and event specifications are delivered and versioned.
 • Integration credentials are isolated from control-plane and ground-truth capabilities.
 • Synthetic data, reset, and replay are operational.
 • Known limitations and unsupported behaviours are documented.



Appendix A — Example composite scenario
Illustrative only — this shows the level of control we need, not a required internal syntax.


   COMMIT_THEN_TIMEOUT_WITH_DELAYED_CREDIT

   A transfer is initiated. The ledger debit commits. The initiating API returns a timeout. The payment switch records
   acceptance. The expected success event is delayed. Beneficiary credit is delayed. Settlement remains pending. A
   duplicate event is later delivered. The control plane retains the exact configured sequence, timing, and authoritative
   outcome, so the whole run can be reset and replayed identically.




Confidential — for the Tushe team                                                                                            Page 19
NOEMA × TUSHE | SYNTHETIC ENTERPRISE ENVIRONMENT                              Technical Requirements & Acceptance Specification · v1.0




Appendix B — Glossary

 TERM                               MEANING


 Synthetic enterprise               A controlled, entirely synthetic representation of interconnected financial enterprise systems
                                    and their state.

 Observable state                   State available through the ordinary integration interfaces.

 Ground truth                       Authoritative internal state, retained for testing/acceptance and isolated from ordinary
                                    integration access.

 Control plane                      The privileged interface used to configure scenarios, faults, time, reset/replay, and diagnostics.

 Unknown outcome                    A condition where the business effect of an attempted operation cannot be established from
                                    the initiating response alone.

 Scenario                           A named, reproducible combination of initial state, actions, timing, and injected conditions.

 Fault injection                    The controlled introduction of a transport, state, event, authorization, or execution failure.

 Business invariant                 A condition that must remain true in authoritative enterprise state.




 This document defines the minimum environment we need in order to use Tushe as our synthetic enterprise substrate.
                                 We’re looking forward to building this with you.




Confidential — for the Tushe team                                                                                                Page 20
