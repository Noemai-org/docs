# DEC-2026-10-22 · IMPOSSIBLE_STATE in §37.2, and the result for a candidate request with no time window

| | |
|---|---|
| **Status** | Accepted by the requesting Founder on 22 October 2026 (instructions given in a working session, in the words quoted in §1; they count once this record is merged). The other Founder confirms by approving the pull request that adds it |
| **Date** | 22 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None |
| **Amends** | PERD §37.2 and REQ-AMB-002 (PERD v1.14) |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the requesting Founder (see the table above)
- Date: 22 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2
- Affected requirement IDs / SoT sections: PERD §37.2, REQ-AMB-002; cites REQ-ENV-005, REQ-CTX-006, §20.3. No SoT change. The requirement count stays 153
- Migration notes: PERD v1.14 is a new file; v1.13 stays unchanged. No `noema` change follows: Session D's pipeline already reports `NO_TRANSACTION_MATCH` (noema `main`, `services/model/tests/test_pipeline.py`)
- Supersedes: None

---

## 1. The decisions

| | Decision |
|---|---|
| D1 | **IMPOSSIBLE_STATE belongs to the hostility proxy** (REQ-ENV-005 and DEC-2026-10-12 D4). PERD §37.2 names the proxy as the producer of the impossible-state fixtures, to match the §37.1 table corrected in v1.13 |
| D2 | **The result for a candidate request with no time window is `NO_TRANSACTION_MATCH`.** The PERD is the authority; `NO_CANDIDATES` is not a PERD code |

## 2. Rationale and evidence

**D1.** REQ-ENV-005: "The proxy is the primary source for ... impossible-data fixtures (labelled synthetic)". DEC-2026-10-12 D4: "Impossible data ... | Noema hostility proxy, labelled synthetic". PERD v1.13 §37.1 already lists IMPOSSIBLE_STATE as a proxy effect; §37.2 named no producer and now does.

**D2.** A search of PERD v1.13 finds `NO_CANDIDATES` nowhere and `NO_TRANSACTION_MATCH` in four places: the ambiguity-flag table of §20.3 ("`NO_TRANSACTION_MATCH` | Yes | CLARIFY (widen) then ESCALATE (handoff)"), REQ-AMB-002 ("An empty set raises `NO_TRANSACTION_MATCH`"), the ambiguity-handling table ("No candidates | NO_TRANSACTION_MATCH | CLARIFY (widen window or ask amount), then handoff") and edge case EC-A12. REQ-CTX-006 lists `time_window` as an input of the candidate request, and the contract `candidates-request.v1.json` requires it, so a request with no window cannot be made; the pipeline sends none and reports the flag of an empty set. Session D's model service uses an internal state named `NO_CANDIDATES` (`ResolutionState`) and emits the flag `NO_TRANSACTION_MATCH`, so no code outside the service differs from the PERD.

## 3. Agent decisions

1. That a request with no window gives the same flag as an empty set follows the Founder's instruction to record the PERD's code; the PERD does not separately describe the no-window case. The Founders may prefer an input error instead.
2. Session D's report that the Founders decided a `counterparty_surface` that is empty or over 64 characters is refused with `INPUT_INVALID` was not part of the instruction, and is not recorded here.

## 4. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted by the requesting Founder (one Founder) | 22 October 2026 | Instructions in a working session, written here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
