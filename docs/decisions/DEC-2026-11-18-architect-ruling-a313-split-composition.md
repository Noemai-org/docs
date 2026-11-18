# DEC-2026-11-18 · Architect ruling A313: the composition is split by lane (interim)

| | |
|---|---|
| **Status** | **Interim.** Decided by the Principal Architect, relayed to the Repo Steward on 18 Nov 2026, who commits it; recorded by the Repo Steward. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 18 November 2026 |
| **Owner** | Principal Architect (the ruling); Founder and Technical Co-Founder (the merge) |
| **Decides** | One ruling, A313 (§1). |
| **Closes** | The wait of C1 and C2 on EL for the wiring of `cmd/core` (A286: "EL is the bottleneck for wiring"). |
| **Supersedes** | Extends and in part replaces **A286**: A286 gave C2 one file, `cmd/core/wire_understanding.go`, and left the Trust adapter, the worker, the route and SSE with EL; A313 gives every lane its own file and moves the route mounts to C1 (§2). |
| **Amends** | The path allowlists of the task cards concerned, for the named files only (REQ-AGT-002). Nothing in the SoT, the PERD or the plan. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 18 November 2026
- Closes: the wiring wait named above
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: A313
- Decision: §1
- Rationale and evidence: the Architect's message of 18 Nov 2026, relayed to the Steward
- Affected requirement IDs / SoT sections: REQ-AGT-002 (allowlists), AGENT-19 (modules meet through contracts); the tasks STM-03, STM-04, UND-04, ENV-04 and EDG-01 touch the files
- Migration notes: none
- Supersedes: see the Supersedes row above

## 1. The ruling, exactly as given

| Ruling | Text | Supersedes or changes |
|---|---|---|
| **A313** (interim) | **Split the composition.** Each lane owns its own wiring file, so nobody blocks anybody: `wire_understanding.go`: C2. `wire_investigations.go`: C1 (the reader adapter plus the route mounts). `wire_trust.go` and `wire_worker.go`: EL. EL's last small PR calls them from `main.go`. | Extends **A286** (C2's `wire_understanding.go` and EL's review). Amends the allowlists below. |

## 2. What it means, and what the Steward did where it is silent

| File (`services/core/cmd/core/`) | Owner | Holds |
|---|---|---|
| `wire_understanding.go` | C2 | C2's adapters (the Interpreter port, noema#661, and the Reconciler, noema#663), as A286 ruled |
| `wire_investigations.go` | C1 | the reader adapter and the route mounts |
| `wire_trust.go` | EL | the Trust adapter |
| `wire_worker.go` | EL | the Temporal worker (STM-04) |
| `main.go` | EL | one last small pull request that calls the four files |

- **Allowlists.** Each owner's pull request may touch its file or files; nobody else's file and `main.go` stay with EL until the last pull request. A reviewer holds a pull request to the allowlist of its card plus this record (REQ-AGT-002).
- **Who reviews.** A286 said EL reviews C2's wiring file; A313 does not change that. The Steward reads C1's and EL's files by the same rule only if asked.
- **The route moves.** A286 left "the route" with EL; A313 gives "the route mounts" to C1, inside `wire_investigations.go`. The Steward records the move as ruled.
- **SSE is not named by A313.** A296 sends EL's SSE rewrite against a Feed interface; which file mounts it is not ruled. The Steward does not assign it: EL or the Architect names the file (the likely reading, `wire_investigations.go` beside the route mounts, is not the Steward's to pick).
- **Order.** The four files are independent; the call from `main.go` is the last step and EL's. Until it lands, the files compile and are tested on their own and the composition root does not use them.
- **No plan row changes.** The work sits under STM-03, STM-04, UND-04, ENV-04 and EDG-01. If a lane needs its own row, the owner asks.
- **Next free ruling: A314.**

## 3. The Steward's ledger

| Block | Numbers | Next free |
|---|---|---|
| Earlier records | A41 to A312 (A306 to A312 in docs#202) | |
| This record | A313 | **A314** |
