# DEC-2026-11-19 · Architect corrections: A371 and A345 S4, and the rulings not yet received

| | |
|---|---|
| **Status** | **Interim.** Given by the Principal Architect, relayed to the Repo Steward on 19 Nov 2026, who commits it. Counts once a Founder who did not author this pull request approves and merges it (A111; AGENTS §2, item 3). |
| **Date** | 19 November 2026 |
| **Owner** | Principal Architect (the corrections); Founder and Technical Co-Founder (the merge) |
| **Decides** | Two corrections, in the Steward's instruction "Correct A371 (reconstruction route audit-only; ops use the panel route) and A345 S4 (at-risk value from the pack via trustlimits; NOEMA_TRUST_AT_RISK_BPS withdrawn)". |
| **Supersedes** | **The first correction changes A371.** **The second changes A345 S4** and withdraws the setting `NOEMA_TRUST_AT_RISK_BPS` that A356 lists. Otherwise nothing. |
| **Amends** | The Compose bench settings table of A356 (`DEC-2026-11-19-architect-rulings-a341-a357`): `NOEMA_TRUST_AT_RISK_BPS` (2500) is withdrawn. The records named above are merged and are not edited; this record says what changed. |
| **Authority order applied** | SoT → decision records → PERD → plan |

**Record fields (decisions README template).**

- Status: Interim; counts on merge by a non-author Founder (A111)
- Date: 19 November 2026
- Owner: Principal Architect; Founder; Technical Co-Founder
- Decides: the two corrections
- Decision: §1
- Rationale and evidence: the Steward's instruction of 19 Nov 2026 as received. The Architect's reasoning was not in it.
- Affected requirement IDs / SoT sections: PERD §39.4; AGENT-16 (no default in code), INV-14 (no industry terms in core); A110, A345, A356, A370
- Supersedes: see the Supersedes row above
- Migration notes: none

## 1. The corrections, as given

1. **A371 corrected:** the reconstruction route is audit-only; ops use the panel route.
2. **A345 S4 corrected:** the at-risk value comes from the pack via `trustlimits`; `NOEMA_TRUST_AT_RISK_BPS` is withdrawn.

*What each changes (the Steward's reading of the records as merged):*

- **A371** in the record as the Steward holds it is "A371, wiring order. The conflicts and the final `main.go` follow the lane files in A313. No new rule." It says nothing about a reconstruction route. The route sentence is in **A370** ("Reconstruction route: PERD 39.4 and A110 win. The route is audit-only. Ops see the investigation view.") in `DEC-2026-11-19-architect-rulings-a362-a376`. The correction says "ops use the panel route"; A370 says "ops see the investigation view". The Steward does not decide which words the Architect meant: it records the correction as given and asks (§3).
- **A345 S4** (in `DEC-2026-11-19-architect-rulings-a341-a357`) gave the at-risk value as the setting `NOEMA_TRUST_AT_RISK_BPS`, and A356's table lists it at 2500. The correction takes the value from the pack, via `trustlimits`, as pack data (INV-14, AGENT-16); the setting is withdrawn.

## 2. The rulings not yet received

The Steward's instruction says "Record A358-A392" and "Record A393-A400 (the answers above)" and names A380 to A383 ("Record A380-A383"). **The text of none of these was in what the Steward received.** The Steward records none of them, and invents none.

| Block | Numbers | Status |
|---|---|---|
| `DEC-2026-11-19-architect-rulings-a362-a376` | A362 (heading only), A363 to A376 | Recorded |
| Founder decision, Intron's data terms | A377 to A379 | Recorded, verbatim |
| `DEC-2026-11-19-architect-rulings-a384-a388` | A384 to A388 | Recorded |
| Not received | A358 to A361, A380 to A383, A389 to A392, A393 to A400 | **Text needed from the Architect** |
| Next free | A401 | |

When the Architect sends the text, the Steward records it, exactly as given, in the next record.

## 3. Questions for the Architect

1. **A371:** the correction names A371, but the route sentence is A370. Is the correction to A370's route sentence, and does "the panel route" replace "the investigation view"?
2. **A345 S4:** what is the pack's field and where does `trustlimits` read it? The Steward writes no pack field name (the fintech pack has no `routes` field either, DEBT-53).
3. **Text of A358 to A361, A380 to A383, A389 to A392 and A393 to A400.**
