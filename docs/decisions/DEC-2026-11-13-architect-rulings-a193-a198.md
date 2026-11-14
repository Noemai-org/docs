# DEC-2026-11-13 · Architect rulings A193 to A198 (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect on 13 Nov 2026, relayed to the Repo Steward, who commits them; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 13 November 2026 |
| **Owner** | Principal Architect (the rulings); Founder and Technical Co-Founder (the merge) |
| **Decides** | Six rulings, A193 to A198 (§1). Each states what it supersedes. |
| **Closes** | The questions on noema#536 (A193), noema#457, #468 and #492 (A194), noema#511 (A195), the order of the masking and re-freeze PRs (A196), the question on noema#472 and Trust decision re-evaluation (A197), and the order of the compile and replay work (A198). |
| **Supersedes** | Per ruling, in §1. In short: A195 revises A192; A198 withdraws an earlier instruction ("run UND-05 now"). |
| **Amends** | Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 13 November 2026
- Closes: the questions named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A193 to A198
- Decision: §1
- Rationale and evidence: the Architect's message of 13 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: INV-02, INV-12, INV-21; AGENT-14, AGENT-15, AGENT-29; REQ-SEC-003, REQ-AUD-001, REQ-INT-001; SoT §0.4
- Migration notes: none by this record. The two contract defects of A193 go in one contract-fix pull request by their owners (AGENT-15)
- Supersedes: see the Supersedes row above

---

## 1. The rulings, exactly as given

| ID | Ruling | Supersedes |
|---|---|---|
| **A193** (interim) | **The 7 exemptions in the append guard (#536).**<br>Accepted:<br>• idempotency key `idk_v1_` + 64 hex, and grant nonce;<br>• `/sig/value` as 64 hex or base64 of at least 32 bytes;<br>• algorithm names `ed25519` and `x25519`;<br>• a lowercase UUID;<br>• core-minted `<prefix>_<ULID>` IDs, including `case_` and `obx_`.<br>`/external_ack` and `/target_ref` (one token of at most 64 characters, no space): accepted for the POC only.<br>• They appear on audit and ops surfaces only, never on the customer overlay or in arms.<br>• A debt entry says that before the pilot they get an adapter-declared shape, or a masked reference plus hash.<br>UUID risk: an all-digit UUID could carry a long number. This is logged as debt, and C2 adds a tiny gateway rule refusing an all-digit request ID after #531.<br>Two contract defects: `IdempotencyKeyId` doesn't fit the real key, and `RequestId` is `req_`-typed while the gateway uses UUIDs. They go into one contract-fix PR (AGENT-15).<br>Order: #531 first, then #536 merges main and drops its duplicate gateway commit. | Nothing committed. It fixes the exemptions that **A184** ("except by type") leaves open. |
| **A194** (interim) | **One masking definition.**<br>• The limit value (4) comes from `masking-limits.v1`.<br>• The digit and separator definition lives in one Go package, `record/payloadguard`, imported by #457, #492 and #536. The Python harness reads the same limit file.<br>• No new contract shape, no Founder approval needed. | Nothing committed. It places the one definition that **A184** requires. |
| **A195** (interim) | **A192 revised.**<br>• No new metric or telemetry package, and no new logger before the redactor (#457) lands.<br>• A model repeating identity fields is a gate refusal with a fixed reason code, recorded in the existing refusal path.<br>• Telemetry is a later task, with a debt entry. | **A192** (a metric and a log now; a Record event only if an existing kind fits). The "no contract bump before G1" line of A192 stands. |
| **A196** (interim) | **Harness masking order.** #468 (EL's code half) first, then #538 (BO's re-freeze), then a follow-up that refuses the old config member. #521 holds until #468 merges, so it gets one push. | Nothing committed. It orders the work of **A162** (the harness masking re-freeze, merged in docs#158). |
| **A197** (interim) | **A186 confirmed.** A WAIT re-evaluated on an unchanged snapshot returns the stored WAIT, by design. A re-evaluation must build a new snapshot from new evidence. EL adds a test that new evidence gives a new snapshot and a new decision. | Nothing. It confirms **A186**. |
| **A198** (interim) | **Live compile run before replay.**<br>Withdrawn: my earlier "run UND-05 now". C2 found that bench-live runs the model-selection bake-off, not the compile acceptance, and the compile route doesn't exist yet.<br>Right order: compile route, then a live compile acceptance run in a new bench-live mode (IL and C2), then recorded replay for G1. | The Architect's earlier instruction to run UND-05 now (withdrawn by the Architect). It sequences the work of **A188** (recorded replay). |

The Architect's instruction to the Steward, which this pull request follows: record A193 to A198 in a new pull request after docs#169 merges; docs#168 merges as is; prepare the SoT v1.12 branch for the Founder to commit; plan v1.19 after docs#166 merges (six rows, EDG-02 Done on noema#496); file an OD for the TypeScript target and debt for `external_ack`, `target_ref` and the UUID risk; record the protection on docs#38 once the Founder posts it; close the five governance issues with links to the Security Reviewer's retro reads and noema#530; record the device holder when named; update noema#183; OD-P-92: the Founder's approval is given.

## 2. What the Steward did where the rulings are silent

- **Order of the records.** This pull request was opened after docs#169 (A183 to A192) merged, as asked. Next free ruling: **A199**.
- **OD-P-88 to OD-P-91 adopted.** As the Architect asked (recorded in `DEC-2026-11-13-architect-rulings-a183-a192`, §2), their register Status lines now say "adopted as written" and that the default is in force from the SoT v1.12 edit. This pull request carries that change instead of a separate one (one fewer open pull request); it touches nothing else in those entries.
- **Debt entered (A193, A195).** DEBT-30 (`external_ack` and `target_ref` accepted for the POC, with the pilot removal condition of A193), DEBT-31 (the all-digit UUID risk and the gateway rule after noema#531) and DEBT-32 (no telemetry for a model repeating identity fields until the later task). Owners are the Steward's defaults from the rulings (C1, C2, EL); they may correct them.
- **OD filed (AGENT-14).** OD-P-93, the TypeScript codegen target of noema#523 (EL's PR, which says it needs an [OPEN] entry and the Founders' approval). **The Steward files it; the Founders approve it.** The default is the one in the PR: an in-repository, standard-library-only generator scoped by `tools/codegen/ts.json`.
- **A196 and the register.** noema#538 re-freezes the two harness configs and its freeze record must name the hash of `masking-limits.v1` (`DEC-2026-11-12-harness-masking-refreeze`, §1 item 4).
- **A198 and the task rows.** The change request `CR-2026-11-13-A188-task-rows` has UND-14 (the compile route) and UND-15 (the recorded-replay provider). **A198 adds a step between them: a live compile acceptance run in a new bench-live mode (IL and C2).** It has no task row. The Steward has not invented one; the question for the Architect is whether plan v1.19 adds a seventh row (proposed ID UND-16, owners IL and C2, Needs UND-14, and UND-15 then Needs UND-16). Until answered, plan v1.19 carries the six rows and UND-15's Needs stay as the change request has them.
- **The SoT v1.12 branch** `docs/OPS-09-sot-v1.12-intron` (based on `main` before docs#169; the Founders commit it, and it merges cleanly or with a README-only merge) holds the edit exactly as drafted, with the Appendix D row, the version lines and the regenerated register. It is not a pull request: the Founders commit it (AGENTS §11).
- **Governance issues.** Closed with links to the Security Reviewer's retro reads and noema#530 where the Architect named them; where a read is missing the issue stays open and says why.

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records (merged) | A41 to A192 (A183 to A192 in docs#169) | |
| This record | A193 to A198 | **A199** |
