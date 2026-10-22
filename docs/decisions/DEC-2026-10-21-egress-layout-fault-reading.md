# DEC-2026-10-21 · `tushe_egress` members, the model service layout, IMPOSSIBLE_STATE and the REQ-ENV-004 example

| | |
|---|---|
| **Status** | Accepted by the requesting Founder on 21 October 2026 (instructions given in a working session, in the words quoted in §1; they count once this record is merged). The other Founder confirms by approving the pull request that adds it |
| **Date** | 21 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | OD-P-62, OD-P-63, OD-P-64 |
| **Amends** | PERD §65.1, §64.2, §37.1 and REQ-ENV-004 (PERD v1.13) |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the requesting Founder (see the table above)
- Date: 21 October 2026
- Closes: OD-P-62, OD-P-63, OD-P-64
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2, from noema#48, noema#51, noema#44 and the committed PERD text
- Affected requirement IDs / SoT sections: PERD §65.1, §64.2, §37.1, REQ-ENV-004; cites REQ-ENV-005, REQ-CTX-006. No SoT change. The requirement count stays 153
- Migration notes: PERD v1.13 is a new file; v1.12 stays unchanged. The `noema` Compose files already match D1 (the connection matrix in noema#51 shows both members); no `noema` change follows from this record
- Supersedes: DEC-2026-10-21-compose-topology D1 in one respect only: it said the relay alone is a member of `tushe_egress`; this record adds the hostility proxy

---

## 1. The decisions

| | Decision |
|---|---|
| D1 | **`tushe_egress` carries both the hostility proxy and the webhook relay.** "Relay only" is removed. (OD-P-62; the Founder: "tushe_egress carries both the hostility proxy and the webhook relay.") |
| D2 | **The candidate client lives under `services/model/noema_model/evidence/`** in the PERD §64.2 layout. (The Founder: "Record that the candidate client lives under services/model/noema_model/evidence/ in the PERD §64.2 layout.") |
| D3 | **IMPOSSIBLE_STATE is produced by the hostility proxy.** The §37.1 effect table moves it out of "State changes (fault controller only)". (OD-P-63; the Founder: keep the committed text unless REQ-ENV-005 says otherwise, and change the docs if it does. It does: see §2.) |
| D4 | **The REQ-ENV-004 example is the §37.1 plan:** a `mock-case` fault inside a `TUSHE` plan is the reading the fault-plan schema took. (OD-P-64.) |

## 2. Rationale and evidence

**D1.** The connection matrix printed by the `compose` job of noema#51 (run 39643867540) shows `hostility-proxy` on `bench_net`, `tushe_egress` and `tushe_net`, and `webhook-relay` on `tushe_egress` and `tushe_net`, with `tushe_egress` the only route out of each and none for the core. The proxy needs a route out because the §65.1 `tushe_net` row has the core reach the hosted Tushe API only through it; Docker cannot allowlist hosts, so the proxy's route table is the allowlist (noema#51).

**D2.** The as-built model service has a Python package root `services/model/noema_model/` (noema `main`); the v1.12 layout listed the modules directly under `services/model/`. The candidate client is the model service's caller of the core's `POST /internal/v1/evidence/candidates` (REQ-CTX-006; contracts `candidates-request.v1.json` and `candidates-response.v1.json`).

**D3.** The Founder's condition was met by the committed text itself. PERD v1.12 §37.1 lists IMPOSSIBLE_STATE under "State changes (fault controller only)", but REQ-ENV-005 says: "The proxy is the primary source for transport faults, stale reads, event-delivery faults ... impossible-data fixtures (labelled synthetic) and timestamp shifts for time cases (labelled synthetic)." DEC-2026-10-12 D4 says the same ("Impossible data (for example, a credit with no debit) | Noema hostility proxy, labelled synthetic. This replaces Tushe scenario 19, which Tushe has rightly refused to fake"), and the fault-plan schema (noema#44) reads it that way. The PERD contradicted itself, and a decision record outranks a PERD table, so the table is corrected. §37.2 names no owner and is unchanged. **Session B was asked to quote REQ-ENV-005 in noema#51; its reply is not part of this record.**

**D4.** The PERD §37.1 example already holds a `mock-case` fault and a `mock-switch` fault in a plan whose `source` is `TUSHE`. The fault-plan schema (noema#44) fixes the reading: `source` names who produces the plan's faults on Tushe and the proxy; a fault whose `target` is `mock-case` is always produced by `mock-case`; a `MOCK_CASE` plan holds `mock-case` faults only. The schema's fixture `perd_example.json` is the same plan.

## 3. Agent decisions

1. **Numbering.** The Founder's list called the IMPOSSIBLE_STATE entry OD-P-63 and the REQ-ENV-004 example OD-P-64; my first draft of docs#55 had them the other way round. The entries are renumbered to the Founder's numbering (docs#55 was unmerged).
2. D3 is applied on the strength of the committed PERD text, which I read myself, without waiting for Session B's quote, because the quote is the same text. If Session B's quote differs, the Founders should say so before this merges.
3. The `ci`, `bench` and `netcheck` profiles for the proxy are as built in noema#51; the relay's profiles are as built in noema#48.

## 4. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted by the requesting Founder (one Founder) | 21 October 2026 | Instructions in a working session, written here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
