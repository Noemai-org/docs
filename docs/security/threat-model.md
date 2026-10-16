# Threat model (POC)

> **Baseline assumption [SoT §47]:** the model can be manipulated, wrong, stale or compromised, and the consequence boundary must still hold. *A compromised model must not become a compromised enterprise execution plane.* Every external input is untrusted until it has been independently authorised and verified.

*Quoted from PERD §41 (opening paragraph), which quotes SoT §47.*

Source: [`../poc/perd/NOEMA_POC_PERD_v1.1.md`](../poc/perd/NOEMA_POC_PERD_v1.1.md) §42, lines 4040–4068. (Current PERD: see [README](../poc/perd/README.md).) The table is copied verbatim and is **Proposed** with the PERD ([DEC-2026-10-11-poc-perd-v1.1](../decisions/DEC-2026-10-11-poc-perd-v1.1.md)). If it disagrees with [SoT](../NOEMA_SOURCE_OF_TRUTH.md) §47, the SoT wins. PERD §42 introduces it as follows:

> The format follows the brief: for each threat, the attack, the asset at risk, the boundary it crosses, the expected behaviour, the mitigation, how it is detected, what is audited, and the test that proves it. The table extends SoT §47.3 and maps to OWASP ASI [SoT §47.2].

In the table, "US-" IDs are SoT user stories; "EC-", "PUS-" and "REQ-" IDs point to PERD edge cases, stories and requirements; "ASI" IDs are categories of the OWASP Top 10 for Agentic Applications (SoT §47.2). Test status is tracked in [`threat-to-test-map.md`](threat-to-test-map.md).

| ID | Threat | Attack | Asset | Boundary | Expected behaviour | Mitigation | Detection | Audit | Test |
|---|---|---|---|---|---|---|---|---|---|
| TM-01 | Malicious user | Floods requests; tries others' data | Availability; other customers' data | Interface → Noema | Throttled; not found | Authentication, target-bound authorisation, rate limits | Rate-limit and scope-violation counters | SECURITY_EVENT | EC-U05, EC-X01 |
| TM-02 | Compromised or wrong model (ASI01) | Emits a refund intent or a fake principal | Execution plane | Intent → action | REJECT or overwrite | No power to act; schema gate; principal overwrite; registry | `prohibited_attempt_total`; principal override events | DECISION_MADE | EC-X05, EC-X08, EC-X10 |
| TM-03 | Indirect prompt injection (ASI01, ASI06) | Instructions in narration, name or notes | Execution plane; explanation | Tool output → context | Treated as data; no prohibited attempt | Delimiting, caps, no instruction channel, registry | Injection detector (advisory) | SECURITY_EVENT | US-09, EC-X02..X04 |
| TM-04 | Malicious tool output or description (ASI02) | Adapter returns a crafted schema or "capability" | Registry | Tool output → context | Ignored | Capabilities come only from the signed pack; schema validation | Adapter contract tests | — | EC-X13 |
| TM-05 | Stolen session | Replays a token | Customer data | Interface | Short life; re-authentication for confirmation | 15-minute sessions; 5-minute freshness for ACCEPT | Anomalous token use | SESSION_VALIDATED | EC-U03 |
| TM-06 | Privilege escalation (ASI03) | "I'm an admin" in text; an ops role asked through the overlay | Control plane | Principal → capability | Ignored | Identity from authentication only; separate admin plane | — | SECURITY_EVENT | EC-X08 |
| TM-07 | Replay of grant or request | Re-submits a spent grant or request | Duplicate effect | Plan → tool | Rejected | Unique spend plus nonce; request deduplication | Constraint violations | GRANT_VOIDED | EC-X07, PUS-07 |
| TM-08 | Duplicate execution | Retry storms; duplicate events | Duplicate case | Execution → target | One effect | Key stored before the call; verify by key; budget | `duplicate_effect_total` | RECEIPT | US-05, US-06 |
| TM-09 | Policy tampering | Edits policy rows directly | Policy integrity | Control → data plane | Detected; not in force | Admin-only publish; checksum; Record event | Checksum mismatch on load | POLICY_PUBLISHED | Tamper test |
| TM-10 | Record tampering | Admin edits a Record row | Audit integrity | Outcome → audit | Detected; tenant writes stopped | Append-only role; hash chain; verification job | `record_chain_break_total` | SECURITY_EVENT | REQ-AUD-005 |
| TM-11 | Data leakage via the model | Prompts include PII; the provider retains it | PII | Core → model | Masked only | Minimisation; masking; provider terms (OD-05) | Prompt scanner | — | REQ-SEC-003 |
| TM-12 | Confused deputy (ASI03) | Vague phrase matches another's transaction | Other customers' data | Principal → capability | Never resolved | Principal-scoped candidates; target-bound authorisation | Leak scanner | — | US-07 |
| TM-13 | Stale authorisation | Acts after state or policy changed | Correctness | Policy → execution | Grant void | Revalidation; INV-26 | `grant_voided_total` | GRANT_VOIDED | US-19, US-20 |
| TM-14 | Insider misuse | An operator misuses admin APIs | All | Control plane | Attributed | Admin MFA; Record of control actions | Review of control events | KILL_SWITCH_CHANGED, POLICY_PUBLISHED | Authorisation-matrix test |
| TM-15 | Oracle leakage | Runtime reads ground truth | Benchmark validity | Benchmark → runtime | Impossible | Network plus credential isolation | `oracle_access_total` | — | REQ-ENV-002 |
| TM-16 | Benchmark leakage into prompts or code | Builders see held-out cases | Validity | Process | Prevented | Separate private repository (OD-16); sealed runner; static scan for case IDs in the core and model repositories | Scan | — | CI scan |
| TM-17 | Forged internal object (ASI07) | Fakes an Intent Object or confirmation on the internal hop | Execution plane | Model → core | Rejected | mTLS; HMAC on confirmations and grants; core re-gates intents | Signature failures | SECURITY_EVENT | EC-X09 |
| TM-18 | Cascading failure (ASI08) | Dependency down; retries amplify | Availability; duplicates | Execution | Fail closed | Circuit breakers; bounded retries; recovery only via Trust | Circuit state | CIRCUIT_STATE_CHANGED | EC-E08 |
| TM-19 | Human–agent trust exploitation (ASI09) | Persuasive false reassurance | Customer trust | Explanation | Blocked | Facts contract; claim validator | `EXPLANATION_BLOCKED` | EXPLANATION_BLOCKED | REQ-EXP-002 corpus |
| TM-20 | Code execution (ASI05) | A model asks to run code or a query | Host | Plan → tool | Impossible | No such capability; no eval or SQL from strings | Registry property test | — | INV-05 test |
| TM-21 | Speech spoofing (an injected audio prompt) | A replayed or synthetic voice | Session | Voice → Gateway | No authority from voice | Identity from the session, never from voice; confirmation in app | — | — | EC-X08 variant |
| TM-22 | Webhook spoofing to the partner | A fake `outcome.updated` | The partner's customers | Core → partner | Rejected by the partner | Signature; timestamp; replay window | Partner-side check | — | REQ-API-006 |
| TM-23 | Forged or stale evidence | An attacker or a buggy source supplies an altered payload, an unknown source or a forged authority class | Decision correctness | Tool output → context | Rejected as UNKNOWN; decision falls back to escalate or refresh | Source identity check; payload hash; authority class only from pack descriptors; freshness from `read_at` | Hash mismatches; unknown-source counter | SECURITY_EVENT | EC-X16 |
| TM-24 | Malicious or replayed inbound webhook | Forged, replayed or reordered event from the enterprise side | State integrity | Enterprise → Noema | Rejected or deduplicated; never changes a fact by itself | Per-source authentication; inbox deduplication; re-read before any change | Inbox rejects | SECURITY_EVENT | EC-X17 |
| TM-25 | Callback server-side request forgery | A callback URL pointing inside the network | Internal network | Core → partner | Registration refused | REQ-SEC-009 | Proxy denials | CALLBACK_FAILED | SSRF test set |
| TM-26 | Partial compromise of one component | One service or credential is taken over | Everything that component touches | Any | The blast radius stays inside that component's privileges | Per-power DB roles; separate credentials; grants needed for every write; Record append-only | Role-permission tests; anomaly alerts | — | Permission matrix; evil-provider run |
| TM-27 | Race between check and write | An operator or second request changes the target after Trust read it | Correctness | Execution → target | Write rejected; grant void; Trust re-runs | Conditional writes with version tokens | `REJECTED_STALE_VERSION` count | RECEIPT | US-19, EC-K01 |

Owner: Security reviewer (SR), a role held by the Founder and the Technical Co-Founder (DEC-2026-10-16 E2).
