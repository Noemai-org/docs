# DEC-2026-10-21 · Compose topology: the `tushe_egress` network and the benchmark runner's route to the core API

| | |
|---|---|
| **Status** | Accepted by the requesting Founder on 21 October 2026 (an instruction given in a working session: "confirm the tushe_egress network ... or amend PERD §65.1" and "decide which network gives the benchmark runner a route to the core API"; it counts once this record is merged). The other Founder confirms by approving the pull request that adds it |
| **Date** | 21 October 2026 |
| **Owner** | Founder and Technical Co-Founder |
| **Closes** | None |
| **Amends** | PERD §65.1 (PERD v1.12) |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).** The table above gives Status, Date, Owner, Closes, Amends and the authority order; the template headings it lacks point to the sections below.

- Status: Accepted by the requesting Founder (see the table above)
- Date: 21 October 2026
- Closes: none
- Owner: Founder and Technical Co-Founder
- Decision: the table in §1
- Rationale and evidence: §2, from noema `sB/t4-webhook-relay` (noema#48) and `sC/t4-runner` (noema#49)
- Affected requirement IDs / SoT sections: PERD §65.1; REQ-ENV-002, REQ-API-008. No SoT change. The requirement count stays 153
- Migration notes: PERD v1.12 is a new file; v1.11 stays unchanged. The `noema` Compose files follow: noema#48 already declares `tushe_egress`; the runner service is added by Session C with the memberships in §1
- Supersedes: None. It names a network the PERD lacked and gives the runner a membership; it loosens no invariant

---

## 1. The decision

| | Decision |
|---|---|
| D1 | **`tushe_egress` is confirmed and written into PERD §65.1.** Members: the webhook relay only, in the Compose profiles `relay`, `ci` and `netcheck`. It is not Docker-internal, only so Docker can publish the relay's port to the host. The relay dials nothing. The core, the model and `mock-case` are not on it |
| D2 | **The benchmark runner's route to the core API is `edge_net`.** In the `bench` profile the runner is a member of `bench_net` and `edge_net`. It calls the public API (`/v1/...`) as a partner application, which is client traffic, and `edge_net` is the client network of §65.1. No new network is created and the core gains no membership |
| D3 | `bench_net` stays unreachable from core and model. The runner publishes and listens on no port, so its two memberships give nothing on `edge_net` a path into `bench_net` |

## 2. Rationale and evidence

**D1.** PERD §65.1 listed no `tushe_egress`; noema#48 (Session B) adds it, and its netcheck matrix (`deploy/compose/netcheck/matrix.py`) writes the memberships and the egress expectations out independently of the Compose file. That matrix shows: the relay on `tushe_net` and `tushe_egress`; every other service with no non-internal network except the model (`provider_egress`) and the UI (`ui_publish_net`); the core's route to an outside address expected to be refused; and the model and the UI forbidden from reaching the relay. The relay holds one secret (the webhook signing secret) and refuses to start with any other credential. The same pattern as `ui_publish_net` (DEC-2026-10-18): a network whose only member needs a published port. The PERD said the relay lives outside Compose; that stays true for a real deployment, and the Compose container is for local and CI runs.

**D2.** PERD §65.1 puts the runner on `bench_net` and has it call the public API as a partner app, but names no network giving it a route to the core's edge (noema#49, item 5). Options weighed:

| Option | Result |
|---|---|
| Runner also on `edge_net` | Chosen. The partner traffic is client traffic by the PERD's own definition; no change to the core's networks; `edge_net` is internal, so no route out is added |
| A new `bench_api_net` shared by runner and core | Rejected: the core gains a membership that exists only for tests, and a topology difference between profiles |
| Core joins `bench_net` | Rejected: it breaks "unreachable from core and model" and would put the core next to the oracle and the truth endpoints |

The cost is that the model also sits on `edge_net` (the voice WebSocket) and so shares a network with the runner. That is why D3 requires the runner to listen on nothing, and why the netcheck matrix must prove it.

## 3. What follows in `noema` (not done by this record)

- Session C adds the runner service to Compose in the `bench` profile on `bench_net` and `edge_net`, publishing no port.
- The netcheck matrix gains: `"benchmark-runner": {"bench_net", "edge_net"}`; the runner reaches the core's edge port; the runner reaches the oracle and the `mock-case` truth endpoint on `bench_net`; the core and the model cannot reach the runner or `bench_net`; the runner has no route to an outside address.

## 4. Agent decisions

1. D2 is a choice among three options made at the Founder's direction, with the reasoning above; the Founders may reverse it.
2. The decision is stated for the `bench` profile only. The runner does not exist in `dev`, `ci` or `demo`.

## 5. Sign-off

| Role | Decision | Date | How recorded |
|---|---|---|---|
| Founders | Accepted by the requesting Founder (one Founder) | 21 October 2026 | Instruction in a working session, written here |
| Technical Co-Founder | Pending | | Approval of the pull request that adds this record |
