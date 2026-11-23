# DEC-2026-11-23 · Architect rulings A554 to A560 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 23 Nov 2026, who commits them. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 23 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Rulings A554 to A560 (§1), every one Interim. |
| **Supersedes** | **A555 changes** where the candidate ranker lives (a Go port in Trust, with parity vectors); it amends PERD §22.1's [REC] note. **A559 and A560 answer** the questions A555 left open (A559: whether the Python ranker stays and which implementation is authoritative; A560: the Rank row's owner and the numeric semantics). The PERD stays unedited until the Founders adopt the change request and a new PERD version is made (§2). **A557 widens** #912 (the intake refuses an empty or malformed decline id as well as the adapter). **A556 splits** A550 (§1). Otherwise nothing; per ruling, in §1. |
| **Amends** | Nothing in the SoT, the PERD or the plan, as written. A555's PERD change goes through `CR-2026-11-23-A555-perd-22-1-ranker-placement` (draft). |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 23 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A554 to A560
- Decision: §1
- Rationale and evidence: the Architect's message of 23 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-01, INV-06, INV-14, INV-21, INV-29; AGENT-15, AGENT-16, AGENT-25; REQ-AMB-003, REQ-TRU-010; PERD §22.1, §32; AGENTS §5, §8
- Supersedes: see the Supersedes row above
- Migration notes: none from this record. A554 reads key announcements from existing migrations and adds none. A555's pack members and A559/A560's threshold data are a separate pack PR with the AGENT-15 steps (a version bump and a migration note).

## 1. The rulings

### A554 (interim, lane 5).

C1 writes the task card and builds it. The settings mirror the orchestrator and edge pattern, required together, with absence being a named gap:

- **Settings:** `NOEMA_EXECUTION_DSN_DIR` (the per-tenant `execution_rw__<tenant>` login), `NOEMA_OUTCOME_DSN_DIR` (`outcome_rw__<tenant>`), and `NOEMA_EXECUTION_KEY_DIR` with `NOEMA_EXECUTION_KEY_MAX_ACTIVE` for the receipt signer.
- **Files:** mode 0400, owner 65532, with identity names taken from the migrations' key announcements.
- If the code differs, C1 raises a CONFLICT block. IL adds the mounts.

### A555 (interim, candidate ranker).

C2's recommendation (a) is accepted. A Go port of the ranker lives in Trust, with shared golden vectors proving parity with the Python ranker. This keeps Trust independent of the model deployable's availability. It amends PERD §22.1's [REC] note, so the Steward drafts the change request. C2 adds the pack members in a separate pack PR with the AGENT-15 steps.

### A556 (interim, A550 split).

- **Payment kinds:** C2 builds the explainer's facts source now. Case kinds return UNKNOWN until C1's lane 5 provides a Record reader for receipt, plan and SLA.
- **Version tokens:** the target version token becomes a mapped field in the pack mapping, owned by C2.
- **`--base-url`:** Voice pins it to a Founder-supplied allowlist host in the settings file, as SR asked.

### A557 (interim, noema#912).

Widening into the intake is approved: the intake refuses an empty or malformed decline id, and so does the adapter. The `rnaRequest` change to `NOT_AUTHORIZED` is confirmed. The stale comment at `ports_t13_t15.go:144` is fixed after #903 merges. Agents read the red CI job and push the green in the same turn, without waiting for the Architect.

### A558 (interim).

The work-in-progress cap stays suspended until G1 passes (A317).

### A559 (interim, the Python ranker and which implementation is authoritative).

1. **Does the Python ranker stay in production?** Only if it has a caller. The Trust T7 ranking uses the Go port. C2 says whether `understanding/resolution/ranking.py` has any production caller. If it has none, it stops being a production code path and stays only as the reference implementation that generates the parity vectors. If it has a caller, that caller may use it only for a non-authoritative ordering, for example to present options.
2. **Which implementation is authoritative if they differ?** The Go port in Trust. Model-service output is untrusted data (INV-02), and Trust never accepts a ranking it did not compute itself. A difference is a failing parity test, never a runtime choice.

### A560 (interim, the Rank row and the numeric semantics).

3. **The Rank row's owner column.** The PERD row changes from "Understanding" to "Trust (deterministic code, no model)", with a note that Understanding keeps a non-authoritative reference. This goes in the PERD change request, which stays a draft until the Founder adopts it. Nothing in the PERD itself is edited in place.
4. **Numeric semantics.**
   - Scores are integer basis points, using floor division, never floating point, in both implementations (A462).
   - The thresholds keep their values, expressed in the same unit: the 0.35 margin is 3500 and the 0.70 floor is 7000. They live in pack or limits data, never in code constants (AGENT-16).
   - Where rounding could matter, it rounds against acting: a score that is uncertain falls below the floor and ends in CLARIFY.
   - The parity vectors cover just below, exactly at and just above both thresholds, in a single shared vector file that both test suites load. A change to either implementation needs the file to pass in both.

## 2. What the Steward did, and where the rulings are silent

- **noema#892 and A542.** noema#892 is already merged (11:43 UTC, 23 Nov 2026), as `DEC-2026-11-23-architect-rulings-a542-a553` records. The empty-`DeclinedRequestID` fix is noema#912 (open at last check), which A557 widens into the intake. **A542 closes when #912 merges** with its test, not before.
- **A554 (traceability).** The Steward changes no Compose value and no setting; IL adds the mounts, and SR reads the new key directories and logins (secrets paths). What the sources establish: the signing identities `core-execution` and `core-outcome` are announced in `services/core/migrations/0013_receipt_signature.sql` (`noema_sig.signing_identity`; key ids have the shape `<identity>.ed25519.<n>`), and `execution_rw` is named in that migration's header. The migrations do **not** state mode 0400 or owner 65532: those come from A518 (mode exactly 0400, owner the core user) and A553 (uid 65532 is the core's runtime user), enforced by the shared key-file reader (noema#884). The `__<tenant>` login suffix is the Architect's wording; the Steward did not find a migration that creates those per-tenant logins, so C1 confirms the names against the code, and a difference is C1's CONFLICT block (AGENT-27).
- **A555 and PERD §22.1.** The PERD text says "**Ranking is deterministic code in the model service, not a model call [REC]**", and the lifecycle table gives the Rank stage to "Understanding (deterministic code, no model)". A555 decides this much and no more: a Go port of the ranker lives in Trust, with shared golden vectors proving parity with the Python ranker, so Trust does not depend on the model deployable's availability; and it amends PERD §22.1's [REC] note. The merged PERD is not edited. The Steward drafted `CR-2026-11-23-A555-perd-22-1-ranker-placement` (Draft, Proposed, owner the Architect), which stays Draft until the Architect resolves what A555 leaves open.
- **A555's open questions are answered by A559 and A560 (Interim).** The Go port in Trust is the only authoritative ranker; the Python ranker is a production path only if C2 reports a caller (non-authoritative ordering only), otherwise the parity reference (A559). The Rank row's owner column, the numeric semantics (integer basis points, floor division, 3500 and 7000 as pack or limits data, rounding against acting) and the single shared vector file are set (A560). The thresholds keep their values; only their representation changes. A560 cites A462 for "never floating point". C2 says in its PR whether `understanding/resolution/ranking.py` has a production caller; the Steward does not look for one. The relation between A546 ("where the PERD places it") and A555 is settled by A559 and A560: Trust computes the authoritative ranking, and Understanding keeps a non-authoritative reference.
- **The change request stays a Draft, and the PERD stays at v1.28.** `CR-2026-11-23-A555-perd-22-1-ranker-placement` now carries the answers (§2 of the CR). It leaves Draft only when the Founder adopts it; then a new PERD version file is made, with a decision record, and `requirements-index.csv` is regenerated. Until then A555, A559 and A560 govern (the A448 pattern). The Rank row's note "Understanding keeps a non-authoritative reference" (A560) goes into that PERD version.
- **A556.** Payment kinds, version tokens and `--base-url` are C2's, C1's lane 5 and Voice's. "Case kinds return UNKNOWN" is the safe default until lane 5's Record reader exists. The Founder supplies the `--base-url` allowlist host; no host is recorded here.
- **A557.** noema#912's widening is C1's and EL's. The stale comment at `ports_t13_t15.go:144` is **not yet fixed**: EL fixes it after #903 merges, and that is follow-up evidence to check later, not a fact now. The "agents push the green in the same turn" rule is the Architect's instruction to agents; the Steward reads it as covering a red CI job on the agent's own PR, never a skipped or weakened test (AGENTS §8).
- **A556 and noema#891 (EL's note).** noema#891 dropped `VersionToken` from `cmd/core`'s `RouteDecision` while `workflows.RouteGrantRequest` kept it and the issuer still refuses an empty token. Once C2 maps the version token in the pack, the issuer's source is the pack mapping; EL checks that when it lands.
- **A558.** The WIP cap of AGENTS §3 (4 open PRs per driving founder, 2 of them P0) stays suspended until G1 passes, as A317 set; no cap is enforced in the interim. AGENTS.md §3 step 3 still states the limit as a start condition (EL's note); the Steward does not edit AGENTS.md in this PR. A one-line note there, or the committed A317, is a small separate PR that EL reviews.
- **Task status (`tasks.csv`).** Unchanged: it moves only on merged evidence, and nothing new has merged against a done-when since UND-17.
- **Migration ledger on noema#183** is unchanged: 0037 stays reserved.
- **Next free ruling: A561.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A340 (A316 and A328 withdrawn) | |
| `DEC-2026-11-20-*` records | A358 to A362, A380 to A485 (A467: no text) | |
| `DEC-2026-11-21-*` and `DEC-2026-11-22-architect-rulings-a518-a524` | A489 to A492, A502 to A517, A518 to A529 | |
| `DEC-2026-11-23-architect-rulings-a530-a533`, `-a534-a540`, `-a542-a553` | A530 to A533; A534 to A540 (A541 noted in the third); A542 to A553 | |
| This record | A554 to A560 | |
| Withdrawn, never recorded | A493 to A501 | |
| Named without text | A467 (blank); A537 lane contents beyond lane 5 | **A561** |
