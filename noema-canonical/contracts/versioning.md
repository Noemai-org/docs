Contract Versioning

Status: Foundational
Version: 0.1
Domain: Contracts
Canonical Path: contracts/versioning.md

⸻

1. Definition

Contract Versioning is the canonical mechanism by which Noema evolves its contracts while preserving semantic integrity, compatibility, auditability, and historical interpretability.

Versioning ensures that changes to the meaning, structure, constraints, lifecycle, or behavior of a contract do not silently invalidate existing contract instances or alter the interpretation of historical execution journeys.

⸻

2. Purpose

Contract Versioning exists to ensure that Noema can evolve without breaking:

* active executions
* stored intent state
* trust decisions
* integrations
* event streams
* audit records
* historical interpretation
* replay
* recovery
* reconciliation

The primary goal is not merely API compatibility.

The primary goal is:

Preserve the meaning of the execution journey across change.

⸻

3. Core Question

Contract Versioning answers:

How can Noema change a contract without changing what existing contract instances meant?

A version therefore represents a semantic contract boundary, not merely a software release number.

⸻

4. Versioning Is Semantic

A contract version describes a supported semantic definition.

Contract v1
      ↓
meaning M1
Contract v2
      ↓
meaning M2

If M2 changes the interpretation of an existing field, state, transition, or invariant, the change must be treated as a semantic change even if the serialized structure remains valid.

⸻

5. Versioning Is Not Deployment Versioning

A software deployment version and a contract version are different concepts.

Application v42
    ≠
Intent Contract v2

An application may deploy many times without changing its contract.

A contract may change even when the underlying implementation changes only minimally.

⸻

6. Versioning Is Not Database Migration

Database migrations describe changes to persistence structures.

Contract versioning describes changes to externally meaningful semantics.

Database Schema
    ↓
Persistence Structure
Contract Version
    ↓
Semantic Agreement

A database migration may support a contract migration, but it does not define the contract itself.

⸻

7. Versioned Contract Families

The foundational Noema contract families include:

Intent Contract
Context Contract
Trust Contract
Action Contract
Execution Contract
Event Contract

Each contract family must have independently managed versions.

⸻

8. Contract Identity

A contract instance should identify the contract family and version that governed it.

Conceptually:

contract_type
contract_version

For example:

contract_type = intent
contract_version = 0.1

This allows historical instances to be interpreted according to the semantics under which they were created.

⸻

9. Version Immutability

Once a contract version is published and used by consequential system behavior, its meaning must be immutable.

A version may be:

* active
* deprecated
* retired

but its historical definition must not be silently rewritten.

v1
│
├── Active
├── Deprecated
└── Retired
Meaning remains unchanged.

⸻

10. Why Immutability Matters

Consider:

Execution created under Action Contract v1

If v1 is later modified, the same execution could acquire a different interpretation when inspected later.

That would break:

* auditability
* reproducibility
* debugging
* legal defensibility
* recovery
* incident analysis

Therefore historical contract versions must remain stable.

⸻

11. Version Lifecycle

A contract version follows a controlled lifecycle:

DRAFT
  ↓
VALIDATED
  ↓
PUBLISHED
  ↓
ACTIVE
  ↓
DEPRECATED
  ↓
RETIRED

Not every implementation must expose all states operationally, but the lifecycle semantics must remain explicit.

⸻

12. Draft

A DRAFT version is under development.

It may be:

* incomplete
* under review
* tested internally
* incompatible with the current active version

Draft versions must not govern production consequential execution unless explicitly permitted by environment policy.

⸻

13. Validated

A VALIDATED version has passed the required contract checks.

Validation may include:

* schema validation
* semantic validation
* invariant validation
* compatibility analysis
* state-transition analysis
* integration compatibility
* migration analysis

Validation does not necessarily mean the version is production-active.

⸻

14. Published

A PUBLISHED version has been formally registered as an available contract version.

Publication makes the version discoverable to components that need to support it.

⸻

15. Active

An ACTIVE version is permitted for new applicable contract instances.

There may be more than one active version where controlled compatibility or migration requires it.

However, the applicable version must always be deterministic.

⸻

16. Deprecated

A DEPRECATED version remains interpretable but should no longer be selected for new contract instances unless explicitly required.

Deprecated versions may remain necessary for:

* active executions
* historical state
* replay
* recovery
* migration
* backward compatibility

⸻

17. Retired

A RETIRED version is no longer permitted for new usage.

Retirement must not mean historical deletion.

Historical instances must remain interpretable for as long as required by Noema’s retention and audit policies.

⸻

18. Semantic Compatibility

Compatibility must be evaluated semantically.

Two contract versions may be structurally compatible while semantically incompatible.

For example:

v1:
"account_id" identifies customer's primary account
v2:
"account_id" identifies any account accessible to the user

The same field exists.

The meaning changed.

This is therefore a semantic breaking change.

⸻

19. Compatibility Classes

Contract changes should be classified as:

NON-BREAKING
CONDITIONALLY COMPATIBLE
BREAKING

The classification must consider both structure and semantics.

⸻

20. Non-Breaking Changes

Examples may include:

* adding optional metadata
* adding non-consequential descriptive fields
* adding new enumerated values where consumers are explicitly designed to tolerate them
* clarifying documentation without changing semantics

A change is non-breaking only when existing valid behavior remains valid and interpretable.

⸻

21. Conditionally Compatible Changes

Some changes are compatible only when participating components satisfy additional requirements.

Examples:

new optional capability
new event type
new policy metadata
new context source

Consumers may need to explicitly declare support.

⸻

22. Breaking Changes

Breaking changes include:

* changing field meaning
* removing required semantics
* changing state-transition rules
* changing authorization meaning
* changing outcome semantics
* changing identity semantics
* changing required evidence
* changing action parameters incompatibly
* changing event meaning
* changing trust decision semantics

Breaking changes require a new contract version.

⸻

23. Structural Versus Semantic Change

Every proposed change should be evaluated across two dimensions:

Structural Change
        +
Semantic Change

Examples:

Field renamed
→ structural + potentially semantic
Field retained but meaning changed
→ semantic
New optional metadata
→ structural, potentially non-breaking
Trust outcome meaning changed
→ semantic breaking

⸻

24. Version Scope

A version must identify what exactly has changed.

Versioning may apply to:

* contract family
* contract schema
* lifecycle semantics
* policy binding
* event semantics
* state machine
* integration compatibility

Noema should avoid using one generic version number to hide materially different version dimensions.

⸻

25. Contract Version Versus Policy Version

Contract and policy versions are separate.

Contract Version
→ defines the contract
Policy Version
→ defines applicable decision rules

For example:

Trust Contract v2
Policy v7

A Trust Decision should preserve both where applicable.

⸻

26. Contract Version Versus Model Version

Model versions are also separate.

Model vX
    ↓
candidate interpretation
Intent Contract vY
    ↓
canonical semantic representation

A model upgrade must not silently redefine the semantics of an existing contract version.

⸻

27. Contract Version Versus Integration Version

Provider integrations may have their own versions.

Action Contract v2
      ↓
Integration Adapter v8
      ↓
Provider API v4

These version dimensions must remain distinct.

Provider API changes must not automatically redefine canonical Noema Actions.

⸻

28. Version Pinning

Consequential operations should reference the contract versions under which they were created or authorized.

Conceptually:

Intent
→ Intent Contract v2
Trust Decision
→ Trust Contract v2
→ Policy v7
Action
→ Action Contract v3
Execution
→ Execution Contract v2

This prevents future contract changes from retroactively altering an active execution.

⸻

29. Version Resolution

When creating a new contract instance, Noema must deterministically resolve which contract version applies.

Resolution may depend on:

* tenant
* organization
* environment
* workflow
* integration
* capability
* effective date
* policy
* explicit compatibility configuration

The selected version must be recorded.

⸻

30. Effective Dates

Contract versions may have explicit validity periods.

v1
valid until T1
v2
valid from T1

Temporal versioning prevents ambiguity about which contract definition applies at a given time.

⸻

31. Version Precedence

If multiple versions could apply, precedence must be deterministic.

Potential precedence dimensions include:

explicit workflow configuration
        >
tenant configuration
        >
organization configuration
        >
environment default
        >
platform default

The exact precedence is a product and architecture decision.

The important invariant is that version selection cannot depend on probabilistic model judgment.

⸻

32. Cross-Contract Compatibility

Contracts do not evolve independently.

For example:

Intent Contract v2
       ↓
Action Contract v3
       ↓
Execution Contract v2

A new Intent version must be evaluated against the Action versions capable of consuming it.

Likewise, Action and Execution versions must remain semantically compatible.

⸻

33. Compatibility Matrix

Noema should maintain a compatibility matrix for contract families.

Conceptually:

                 Intent   Context   Trust   Action   Execution   Event
Intent v1          ✓         ✓
Intent v2          ✓         ✓
Context v1                    ✓        ✓
Context v2                    ✓        ✓
Trust v1                              ✓        ✓
Trust v2                              ✓        ✓
Action v1                                      ✓        ✓
Action v2                                      ✓        ✓

The matrix identifies supported combinations.

Unsupported combinations must fail deterministically.

⸻

34. Contract Negotiation

Where multiple versions are supported across a boundary, components may negotiate or select a compatible version.

Negotiation must be deterministic.

For example:

Consumer supports:
v1, v2
Provider supports:
v2, v3
Selected:
v2

The selected version must be recorded where it affects semantics.

⸻

35. Consumer-Driven Compatibility

A contract producer should not assume that every consumer automatically supports the newest version.

Consumers should declare supported versions where appropriate.

Consumer:
supports v1, v2
Producer:
offers v2, v3

The system must select an explicitly compatible version.

⸻

36. Version Migration

Migration is the controlled movement from one contract version to another.

Conceptually:

v1
 ↓
Migration / Translation
 ↓
v2

Migration must preserve semantic meaning.

A migration that changes meaning is not a transparent migration; it is a semantic transformation and must be treated accordingly.

⸻

37. Contract Translation

Sometimes different contract versions cannot be directly reused and require translation.

For example:

Intent v1
    ↓
Translator
    ↓
Intent v2

The translation must preserve:

* intent
* scope
* constraints
* provenance
* uncertainty
* relevant identity
* semantic outcome

It must not silently manufacture missing information.

⸻

38. Lossy Migration

Some migrations may lose information.

If information loss affects semantics, the migration must explicitly represent it.

For example:

v1:
specific account target
v2:
generic account target

The migration cannot silently discard the specific target and claim semantic equivalence.

⸻

39. Historical Interpretation

Historical contract instances must be interpreted using the contract version under which they were created.

Historical Intent
       ↓
Intent Contract v1

not:

Historical Intent
       ↓
Current Intent Contract v4

unless an explicit migration has occurred and its effects are recorded.

⸻

40. Active Execution Versioning

An active Execution must retain the contract versions relevant to its lifecycle.

A deployment must not silently move an execution from:

Execution Contract v1

to:

Execution Contract v2

merely because v2 became active.

Migration must be explicit.

⸻

41. In-Flight Executions

When a new contract version becomes active, existing executions may continue under their original contract version unless policy explicitly requires migration.

This prevents mid-execution semantic changes.

Execution started under v1
        ↓
v2 becomes active
        ↓
Execution continues under v1

⸻

42. Event Versioning

Events require particular care because they may persist for long periods.

An Event should identify its event schema or contract version.

event_type
event_version

Historical events must remain interpretable after producers and consumers evolve.

⸻

43. Event Evolution

Changing the meaning of an existing event is generally a breaking semantic change.

For example:

ExecutionCompleted v1:
transport completed
ExecutionCompleted v2:
business outcome verified

These are materially different meanings.

They should not share an indistinguishable semantic version.

⸻

44. Trust Versioning

Trust contracts require especially strict versioning because they govern consequential authorization.

A Trust Contract change may affect:

* required evidence
* permissions
* risk thresholds
* ambiguity rules
* escalation requirements
* confirmation requirements
* decision precedence

Such changes must be explicitly versioned and attributable.

⸻

45. Action Versioning

Action Contracts must preserve the exact executable semantics used by an execution.

A change to:

* parameters
* target semantics
* preconditions
* idempotency behavior
* expected outcomes
* side-effect semantics

may require a new Action Contract version.

⸻

46. Execution Versioning

Execution Contract versions govern execution semantics such as:

* state transitions
* retries
* timeout behavior
* verification
* recovery
* cancellation
* reconciliation

Changing these semantics can affect active operations and therefore requires controlled rollout.

⸻

47. Intent Versioning

Intent Contract versions must preserve semantic interpretation.

Changes to:

* intent types
* parameter meaning
* target resolution
* ambiguity rules
* outcome semantics

may require a new Intent Contract version.

Historical intents must remain interpretable under their original semantics.

⸻

48. Context Versioning

Context Contract versions must preserve the meaning of contextual inputs.

Changes may include:

* identity semantics
* scope semantics
* temporal interpretation
* evidence references
* context precedence
* required contextual fields

A context version must not silently reinterpret historical trust decisions.

⸻

49. Contract Version and Provenance

Every consequential contract instance should preserve provenance sufficient to establish:

which version was used
who or what selected it
when it was selected
which configuration applied
which predecessor version existed
whether migration occurred

Version metadata is part of execution provenance.

⸻

50. Contract Version and Auditability

An auditor should be able to answer:

Which exact contract semantics governed this decision?

For example:

Intent Contract: 2
Context Contract: 1
Trust Contract: 3
Policy: 7
Action Contract: 2
Execution Contract: 1
Event Contract: 4

This should be reconstructable from persisted state.

⸻

51. Contract Version and Reproducibility

Given:

historical input
contract versions
policy versions
relevant context
evidence

Noema should be able to reconstruct the decision path to the extent required by its audit and operational guarantees.

Reproducibility does not necessarily mean re-executing the operation.

It means being able to understand how the original decision was produced.

⸻

52. Contract Version and Replay

Replay must use the appropriate historical contract versions unless the replay is explicitly intended as a migration or simulation.

Historical Event
      ↓
Historical Contract Version
      ↓
Replay

Current contract versions must not silently reinterpret historical events during replay.

⸻

53. Contract Version and Recovery

Recovery of an existing execution should normally operate under the execution’s established contract semantics.

If migration is required:

Existing Execution
      ↓
Migration Evaluation
      ↓
Explicit Migration
      ↓
New Contract Version

The migration must be recorded.

⸻

54. Contract Version and Reconciliation

Reconciliation may occur after a contract version has changed.

The reconciliation process must still understand the original Action and Execution semantics.

A newer contract version must not cause historical execution to be interpreted incorrectly.

⸻

55. Contract Deprecation

Deprecation should be deliberate and observable.

A deprecated version should specify:

* deprecation date
* replacement version
* migration guidance
* remaining supported use
* retirement conditions

Deprecation must not invalidate active historical state.

⸻

56. Contract Retirement

Retirement removes a version from normal new-instance creation.

Before retirement, Noema should establish that:

* active executions no longer depend on it
* required migrations are complete
* historical interpretation remains possible
* required archives remain available
* compatibility obligations are satisfied

Retirement is therefore an operational state, not destruction of semantic history.

⸻

57. Contract Registry

Noema should maintain a canonical registry containing at least:

contract_type
version
status
effective_from
effective_until
compatibility
successor_version
predecessor_version
schema_reference
semantic_definition

The registry is the authoritative source for contract version metadata.

⸻

58. Version Governance

Contract changes should require controlled governance.

A change should document:

* reason for change
* affected contracts
* semantic impact
* compatibility impact
* migration strategy
* rollout strategy
* rollback strategy
* affected integrations
* historical implications

The more consequential the contract, the stronger the governance requirement.

⸻

59. Version Change Process

The canonical process is:

PROPOSE
   ↓
CLASSIFY CHANGE
   ↓
ANALYZE COMPATIBILITY
   ↓
UPDATE CONTRACT
   ↓
VALIDATE
   ↓
DEFINE MIGRATION
   ↓
PUBLISH
   ↓
ROLLOUT
   ↓
OBSERVE
   ↓
DEPRECATE OLD VERSION
   ↓
RETIRE WHEN SAFE

No breaking version should be introduced without understanding its impact on active state.

⸻

60. Rollout Strategy

Contract versions may be introduced through:

* tenant-by-tenant rollout
* organization-by-organization rollout
* environment rollout
* workflow rollout
* integration rollout
* feature-gated rollout

The selected strategy must preserve deterministic version selection.

⸻

61. Rollback

Rollback must distinguish between:

application rollback

and:

contract semantic rollback

A deployment can be rolled back without automatically reverting persisted contract instances.

Previously created instances must retain their original semantic version.

⸻

62. Contract Version and Tenancy

Different tenants may temporarily use different contract versions.

For example:

Tenant A → v2
Tenant B → v1

This is valid only when explicitly supported.

The tenant-specific selection must be deterministic and recorded.

⸻

63. Contract Version and Environment

Different environments may support different contract versions.

Development → v3
Staging     → v3
Production  → v2

This may be useful during controlled rollout.

Production behavior must never accidentally inherit an unreleased contract version.

⸻

64. Contract Version and Integrations

Integrations should explicitly declare which Action and Execution Contract versions they support where necessary.

For example:

Integration A
→ Action Contract v1, v2
Integration B
→ Action Contract v2

Noema must not send a contract version to an integration that cannot correctly interpret it.

⸻

65. Contract Version and AI Models

A model upgrade must not silently upgrade contract semantics.

For example:

Model v1
→ Intent Contract v1
Model v2
→ Intent Contract v1

may be entirely valid.

The model can improve interpretation while the canonical Intent Contract remains unchanged.

Conversely, changing the Intent Contract should not require a model change unless the semantic requirements actually demand it.

⸻

66. Versioning and Determinism

Version selection is itself a deterministic operation.

The system must never allow the model to decide:

"Which contract version should I use?"

based on probabilistic preference.

Contract selection must follow explicit configuration and policy.

⸻

67. Versioning and Unknown State

If Noema cannot establish which contract version applies, it must not guess.

The state should be represented as unresolved or invalid according to the applicable contract-management policy.

Unknown Contract Version
        ↓
STOP / CLARIFY / ESCALATE

The system must not execute under an arbitrary version.

⸻

68. Versioning and Compatibility Failure

If two required components cannot agree on a compatible contract version, execution must stop or follow an explicit fallback policy.

Producer → v3
Consumer → v1
No compatible version
        ↓
FAIL DETERMINISTICALLY

Silent semantic downgrade is prohibited.

⸻

69. Versioning and Data Migration

Contract migration may require persistence migration.

However:

Data Migration
    ≠
Semantic Migration

Both must be explicitly planned when both are required.

Persistence transformations must preserve the semantics of the contract instance.

⸻

70. Versioning and Backward Interpretation

Noema should preserve the ability to interpret supported historical versions.

This may require:

* versioned schemas
* migration adapters
* archived contract definitions
* compatibility libraries
* event upcasters
* historical policy references

The implementation may change.

The historical meaning must remain accessible.

⸻

71. Versioning and Forward Compatibility

Where possible, contracts should be designed so that consumers can safely tolerate non-breaking future additions.

Examples include:

* optional metadata
* unknown non-consequential fields
* extensible event metadata

Forward compatibility must never come at the cost of semantic ambiguity.

⸻

72. Versioning and Observability

Version identifiers should appear in operational telemetry where relevant.

For example:

intent_id
intent_contract_version
trust_contract_version
policy_version
action_contract_version
execution_contract_version
event_contract_version

This makes version-related failures diagnosable.

⸻

73. Versioning and Testing

Every new contract version should be tested against:

* schema validity
* semantic invariants
* compatibility matrix
* migration paths
* historical fixtures
* active workflows
* integrations
* event consumers
* recovery paths
* replay behavior

Contract tests must include negative cases.

⸻

74. Versioning and Security

A contract version change can alter security semantics.

Examples:

new permission requirement
new identity semantics
new tenant boundary
new evidence requirement

Security-impacting contract changes must receive explicit review.

A structurally compatible change can still be security-breaking.

⸻

75. Versioning and Trust

Trust Contract changes are particularly sensitive because they may alter whether an operation can proceed.

Therefore any Trust version change must identify:

* affected policies
* affected actions
* changed evidence requirements
* changed permission requirements
* changed ambiguity handling
* changed escalation rules
* affected tenants
* affected active executions

⸻

76. Versioning and Execution Safety

Noema must prefer semantic continuity over forced adoption of the newest contract.

An active execution should not be migrated merely because a newer version exists.

Migration requires explicit compatibility and safety analysis.

⸻

77. Reference Versioning Model

Conceptually:

                    CONTRACT REGISTRY
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          Intent v1     Intent v2    Intent v3
              │            │            │
              └────────────┼────────────┘
                           │
                     Compatibility
                           │
                           ▼
                     Action Versions
                           │
                           ▼
                   Execution Versions
                           │
                           ▼
                     Event Versions

The registry defines which combinations are supported.

⸻

78. Historical Version Model

Conceptually:

                 CURRENT
                   │
              Contract v3
                   │
        ┌──────────┴──────────┐
        │                     │
   New Instances        Existing Instances
                              │
                              ▼
                         Contract v1
                              │
                              ▼
                       Historical Meaning

Current versions govern new state.

Historical versions preserve old meaning.

⸻

79. Contract Version Invariants

Invariant 1

Every consequential contract instance identifies the contract version that governed it.

Invariant 2

Published contract versions are immutable in meaning.

Invariant 3

Contract versioning is distinct from application deployment versioning.

Invariant 4

Contract versioning is distinct from database schema versioning.

Invariant 5

Compatibility must be evaluated semantically, not only structurally.

Invariant 6

Breaking semantic changes require a new contract version.

Invariant 7

Historical contract instances remain interpretable under their original semantics.

Invariant 8

A new contract version must not silently reinterpret historical state.

Invariant 9

Version selection must be deterministic.

Invariant 10

Model confidence must never determine contract version selection.

Invariant 11

Contract and policy versions remain distinct.

Invariant 12

Contract and model versions remain distinct.

Invariant 13

Contract and integration versions remain distinct.

Invariant 14

Active executions retain the contract semantics under which they were created unless explicit migration occurs.

Invariant 15

In-flight executions must not silently switch contract versions.

Invariant 16

Contract migration must preserve semantic meaning or explicitly represent semantic transformation.

Invariant 17

Lossy migration must never silently discard consequential information.

Invariant 18

Contract translation must preserve provenance.

Invariant 19

Event versions must preserve historical event meaning.

Invariant 20

Trust contract changes must be explicitly versioned.

Invariant 21

Action contract changes affecting executable semantics must be explicitly versioned.

Invariant 22

Execution contract changes affecting lifecycle semantics must be explicitly versioned.

Invariant 23

Intent contract changes affecting interpretation semantics must be explicitly versioned.

Invariant 24

Context contract changes affecting resolution or trust semantics must be explicitly versioned.

Invariant 25

Unsupported contract combinations must fail deterministically.

Invariant 26

Noema must not silently downgrade to an incompatible contract version.

Invariant 27

Unknown applicable contract versions must not result in guessed execution.

Invariant 28

Deprecated versions remain interpretable for supported historical state.

Invariant 29

Retirement does not erase required historical contract definitions.

Invariant 30

Contract registry metadata must identify supported versions and lifecycle status.

Invariant 31

Contract version changes must undergo compatibility analysis.

Invariant 32

Contract version changes must account for active executions.

Invariant 33

Contract version changes must account for recovery and replay.

Invariant 34

Contract version changes must account for integration compatibility.

Invariant 35

Contract version changes affecting security semantics require explicit security evaluation.

Invariant 36

Contract version identifiers must remain available for audit and observability.

Invariant 37

Rollback of application code does not automatically rewrite persisted contract versions.

Invariant 38

Tenant- or environment-specific contract versions must be explicitly configured.

Invariant 39

Contract evolution must preserve the distinction between Noema execution-domain authority and enterprise business-state authority.

Invariant 40

Versioning must preserve the historical meaning of the Noema execution journey.

⸻

80. Final Definition

Contract Versioning is the controlled evolution of Noema’s semantic agreements without silently changing the meaning of existing state, decisions, executions, or events.

A contract version establishes a stable semantic boundary for:

structure
semantics
constraints
invariants
lifecycle
authority
compatibility

The canonical model is:

Contract
   ↓
Version
   ↓
Validation
   ↓
Publication
   ↓
Deterministic Selection
   ↓
Contract Instance
   ↓
Historical Preservation

New versions may change the system.

They must not rewrite history.

The governing principle is:

A contract version may evolve Noema’s future behavior, but it must never silently change the meaning of its past.

Contract versioning therefore protects the integrity of the entire Noema execution journey—from Intent through Context, Trust, Action, Execution, Events, and Outcome—by ensuring that every consequential state remains tied to the semantic rules under which it was created.