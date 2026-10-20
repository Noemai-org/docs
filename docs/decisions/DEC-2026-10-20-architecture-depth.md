# DEC-2026-10-20 · Architecture depth: nine decisions from the architecture review

| | |
|---|---|
| **Status** | Accepted by the Founders on 20 October 2026 (recorded by sending the build prompt "Noema_Architecture_Depth_Build_Prompt" to the coding agents). The Technical Co-Founder confirms by approving the pull request that adds this record |
| **Date** | 20 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | The founder question set of 20 October 2026 ("what is specified, what is built, what is missing, and what makes it win") |
| **Amends** | PERD §64.2, §19.1, REQ-AMB-003, REQ-AMB-004, REQ-AUD-005, §27.3 and §36.1 (PERD v1.11) |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the Founders (see the table above)
- Date: 20 October 2026
- Closes: the question set listed above
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: the architecture review of 20 October 2026 ("Noema_Architecture_Review_2026-10-20"), whose §9 is the source of the wording in §1
- Affected requirement IDs / SoT sections: PERD §64.2, §19.1, REQ-AMB-003, REQ-AMB-004, REQ-AUD-005, §27.3 (tests), §36.1 (Temporal row). No SoT change. The requirement count stays 153
- Migration notes: PERD v1.11 is a new file; v1.10 stays unchanged. The `noema` repository follows in the T1 to T6 pull requests of the build prompt
- Supersedes: None. Each decision tightens or adds; none loosens an invariant

---

## 1. The decisions

Quoted exactly as worded in §9 of the review.

| ID | Decision |
|---|---|
| D1 | PERD §64.2 is the normative skeleton depth. Every listed sub-package exists as a real package with its responsibility, allowed imports and prohibitions. |
| D2 | `services/model/harness/` is added as the single path to `providers/`, with the responsibilities in §6.1. |
| D3 | `services/model/understanding/pipeline/` holds stateless pure-function DAGs; no stateful agent framework; Temporal in core is the only workflow state. |
| D4 | REQ-AMB-004 is extended: when one attribute's values uniquely partition the candidates, the clarification asks by that attribute (deterministic, maximum information gain, pack-template wording), falling back to the option list. |
| D5 | The recipient feature in REQ-AMB-003 is a composed matcher (aliases, transliteration, phonetic keys, token order) whose data lives in the pack's Intent Taxonomy. Weights and thresholds are unchanged. |
| D6 | Record chain heads are checkpointed, signed and exported outside Postgres on a schedule; reconstruction must replay decisions bit for bit. |
| D7 | Spend-and-dispatch acceptance adds crash-point injection at every step boundary, deterministic simulation testing, and linearizability checking of mock-case histories. |
| D8 | Temporal write activities run with `MaximumAttempts: 1`. Read activities retry with bounded backoff. |
| D9 | Decision models (Jev, OpenAI Decisions API, Microsoft-Decision-1) become a provider class behind a single `harness.decide()` interface, eligible only for the six enumerated understanding tasks in §6.4. Each task's provider is chosen by a benchmark bake-off measuring accuracy and per-language calibration. Versions are pinned, abstention is always offered, data is synthetic only until data terms are reviewed, and confidence is never authority. |

"§6.1" and "§6.4" in D2 and D9 refer to the sections of the review of that number. PERD v1.11 writes their content into §19.1 and the notes after its table, so the PERD does not point at a document outside the repository.

## 2. What PERD v1.11 changes

| Decision | Where in PERD v1.11 |
|---|---|
| D1, D2, D3 | §64.2 layout (`services/model/harness/`, `services/model/understanding/pipeline/`, `services/core/internal/predicate/`); §19.1 rows for `harness` and `pipeline`; the `providers` row (only `harness` may call it) |
| D4 | REQ-AMB-004: ask by attribute |
| D5 | REQ-AMB-003: the recipient matcher |
| D6 | REQ-AUD-005: checkpoints and bit-for-bit replay |
| D7 | §27.3: the spend-and-dispatch acceptance |
| D8 | §36.1, Temporal row |
| D9 | §19.1: the `harness` row and the note after the table |

## 3. Values taken from the build prompt

The build prompt that records these decisions adds one figure and one scope that the review does not state. They are written into PERD v1.11 and tagged `[ADOPTED DEC-2026-10-20]`:

- deterministic simulation testing runs at least **10,000 seeded interleavings in CI** (D7);
- the `internal/predicate` package under core holds the predicate language of SoT §43.7 (D1).

## 4. What this does not change

- Every invariant, gate and requirement. The 153 requirements stay.
- The margin, the floor and every confidence threshold. They move only through a benchmark run and a founder decision (AGENT-16, REQ-AGT-005).
- The comparison arms (REQ-BEN-007), which are built only after Noema passes its own gates, and the held-out layer (REQ-BEN-003, REQ-AGT-004), which no agent touches.
- No decision model is adopted for any task by this record. D9 makes them eligible; the bake-off and a later founder decision choose.

## Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Approved | 20 Oct 2026 | Written instruction to the coding agents (the build prompt) |
| Technical Co-Founder | Confirms | Date of approval | Approving review on the pull request that adds this record |
