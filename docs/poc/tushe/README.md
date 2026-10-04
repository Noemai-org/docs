# Tushe — synthetic enterprise environment

Tushe provides the synthetic enterprise environment the Noema POC is built and benchmarked against (SoT §36).

| Document | Version | Status | Notes |
|---|---|---|---|
| [Technical Requirements & Acceptance Specification](Noema_Tushe_Synthetic_Enterprise_Environment_Spec_v1.0.md) | 1.0 | Issued to Tushe — frozen | 85 requirements (73 P0, 12 P1); acceptance tests AT-01 to AT-20; 20-scenario readiness pack |
| [Original export](source/) | 1.0 | Unchanged source | Kept for provenance |

**Rules**
- Issued versions are never edited. Changes go into a delta file (`tushe-spec-delta-vX.Y.md`) and become a new version only when re-issued to Tushe.
- This folder holds only what Tushe is meant to see. Internal strategy, benchmark design and the hidden test set never go here.
- Readiness is reached when every P0 requirement is met or formally waived, AT-01 to AT-20 pass in a joint session, and the 20-scenario pack runs reproducibly (spec §25). That is the exit of POC Phase A (SoT §36, §40).

**Issue record**
- Date issued to Tushe: _to be confirmed by the founder_
- Tushe's response to §24 (Supported / Requires extension / Not supported): _pending_
- Agreed exceptions: _none yet_
