# Tushe — synthetic enterprise environment

Tushe provides the synthetic enterprise environment the Noema POC is built and benchmarked against (SoT §36).

| Document | Version | Status | Notes |
|---|---|---|---|
| [Technical Requirements & Acceptance Specification](Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md) | 1.0 | Issued to Tushe — frozen | 85 requirements (73 P0, 12 P1); acceptance tests AT-01 to AT-20; 20-scenario readiness pack |
| [Original export](source/) | 1.0 | Unchanged source | Kept for provenance |
| [Requested changes v1.0 → v1.1](tushe-spec-delta-v1.1.md) | 1.1 (draft) | **Superseded by v1.2. Never sent to Tushe** | Kept for the record of what was drafted |
| [Changes v1.0 → v1.2](tushe-spec-delta-v1.2.md) | 1.2 | Records the exchange of 13 Oct 2026 (the PDF is the record) | The amended AT-01, AT-03 and AT-15 conditions, requests R1 to R13 with dates, and what was withdrawn (DEC-2026-10-16 E10) |
| [Tushe correspondence](responses/README.md) | — | Frozen records | Tushe's draft response of 7 Oct 2026 (received 8 Oct); Noema's response of 13 Oct 2026, as sent (PDF) |
| [Acceptance](acceptance/README.md) | — | Worksheet sent 13 Oct 2026 (PDF); not yet signed | The worksheet for the joint session; AT-01 to AT-20 |

**What governs Tushe semantics** (DEC-2026-10-16 E10): the specification v1.0; Tushe's response of 7 Oct 2026; [DEC-2026-10-12](../../decisions/DEC-2026-10-12-tushe-environment-scope.md); delta v1.2; and the signed worksheet. Nobody infers endpoint semantics from memory or from one observed response.

**Rules**
- Issued versions are never edited. Changes go into a delta file (`tushe-spec-delta-vX.Y.md`) and become a new version only when re-issued to Tushe. Files on the frozen list (`tools/frozen-files.sha256`) are never edited.
- This folder holds only what Tushe is meant to see. Internal strategy, benchmark design and the hidden test set never go here.
- Readiness is reached when every P0 requirement is met or formally waived, AT-01 to AT-20 pass in a joint session, and the 20-scenario pack runs reproducibly (spec §25). That is the Tushe half of the exit of POC Phase A (G0-T). G0 passes only when G0-T and the Noema half (G0-N) both pass (DEC-2026-10-16 E4; SoT §36, §40).

**Issue record**
- Date the specification v1.0 was issued to Tushe: _to be confirmed by the founder_
- Tushe's response to §24 (Supported / Requires extension / Not supported): received as a working draft, dated 7 Oct 2026 (received 8 Oct); see [`responses/`](responses/README.md)
- Noema's response and the acceptance worksheet: sent to Tushe on 13 Oct 2026 (PDF records; time not recorded)
- Joint session: planned for Fri 16 Oct 2026, 18:00–20:30 WAT, and **postponed**. Tushe has not confirmed a new date. The Tushe half of G0 (G0-T) takes place on the date Tushe confirms
- Agreed exceptions: _none yet_ (the worksheet is unsigned)
