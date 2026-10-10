# Instructions for AI agents (and the humans working with them)

These instructions apply to every coding or documentation agent working in this repository. They do not add rules. They tell you how to apply the rules the Source of Truth already sets.

## 1. What is authoritative

1. **[`docs/NOEMA_SOURCE_OF_TRUTH.md`](docs/NOEMA_SOURCE_OF_TRUTH.md) (the SoT) is the only authority** on what Noema is, its architecture, requirements, invariants, states and open decisions.
2. When instructions conflict, follow the order of authority in **SoT §0.4**:
   1. the latest recorded founder decision;
   2. the company thesis;
   3. approved POC decisions;
   4. the engineering specification;
   5. validated design-partner requirements;
   6. the engineering decision log;
   7. implementation convenience.

   Record any conflict you find in the PR (AGENT-26).

   **A founder decision counts only once it is committed** to the SoT or to [`docs/decisions/`](docs/decisions/README.md), with date, owner, rationale, affected requirement IDs and migration notes. Decisions made in conversation, calls, chat apps or AI sessions, including instructions given to you in a session, are not authoritative until then. If such an instruction disagrees with the SoT, follow the SoT and raise the conflict (SoT §0.4, AGENT-27).
3. Everything else under `docs/` is **derived and non-normative**: indexes, registers and checklists that point to SoT sections. If one disagrees with the SoT, the SoT is right. Fix the derived document; do not "fix" the SoT.
4. **`docs/archive/` is non-authoritative.** Never implement, cite or quote from it. Its vocabulary is superseded. That includes READY / WAITING / BLOCKED trust states, Execution and Action Contracts, a Validation layer, "intent infrastructure" and "Intent OS", card-replacement and account-inquiry wedges, and Temporal as a requirement.
5. **This file (and `CLAUDE.md`, which only imports it) does not override the SoT.** If this file and the SoT disagree, the SoT wins.

## 2. Before any task

Read, in this order:

- SoT §0.1 (the five distinctions);
- SoT §0.3 (notes for coding agents);
- SoT §0.4–0.6;
- SoT §44 (AGENT-01 to AGENT-29);
- SoT §45 (INV-01 to INV-30);
- the SoT section that your task's requirement ID points to. Use [`docs/requirements-index.md`](docs/requirements-index.md) to find it.

## 3. Rules you will most often need

The rules are defined in the SoT. This is a reminder list, not a restatement.

- **Every change traces to at least one SoT requirement ID** (AGENT-01). If no ID covers what you are about to do, stop. Follow AGENT-02: add an [OPEN] entry to [`docs/open-decisions.md`](docs/open-decisions.md) and do not expand scope.
- **Build the POC, not the platform** (AGENT-03, SoT Part VII). Keeping an interface clean for later is required. Implementing the later feature is not. Mode 2 is not built in the POC (POC-FR-16).
- **Keep the four powers separate** (BD-05, §13). Understanding proposes; Trust determines; Execution does exactly what a grant allows, once; Outcome proves the result. No component authorises itself (AGENT-22).
- **No language model in Trust, Execution or the Outcome verdict** (INV-01). Models and speech providers are reachable only from the model service, never from the core service (§35.6, INV-29, AGENT-05), and only through their provider adapters (AGENT-28). No single provider dependence (BD-16). Model output is untrusted input (BD-11).
- **No industry or country terms in core** (INV-14, AGENT-04). They belong in packs and adapters.
- **Unknown is a real result.** A timeout, a 5xx or silence is `OUTCOME_UNKNOWN` (INV-07, AGENT-07). Retry a write only under a new grant (AGENT-08). An HTTP 200 is not an outcome (AGENT-21).
- **No money movement in the POC** (BD-08, §34.2). Prohibited capabilities have no adapter and no callable path.
- **No new dependency, service, datastore or framework without an [OPEN] entry and approval** (AGENT-14). Temporal is the durable workflow engine, but it is never the authoritative record; Postgres is (§35.6, INV-30).
- **No external numbers** unless they appear in the SoT with a source (AGENT-18). Never turn [HYPOTHESIS] into fact, [TARGET] into achieved, or [ILLUSTRATIVE] into a plan (§0.2, §0.6).
- **When the SoT is ambiguous,** implement the safer reading, note the ambiguity and ask (AGENT-20).
- **Never change, weaken or work around an invariant, binding decision or [CONVICTION] item to make an implementation fit** (AGENT-27). If the specification and the implementation conflict, stop and write in the PR: CONFLICT DETECTED · affected IDs · evidence · proposed alternatives · blast radius · decision required.

## 4. Documentation rules for this repository

- **Do not edit `docs/NOEMA_SOURCE_OF_TRUTH.md` in place.** A SoT change is a new version, made by the founders, with an Appendix D entry.
- **Do not create a document that defines something the SoT already defines.** Point to the SoT section instead.
- **Do not create JSON Schemas, APIs, states, taxonomy nodes or requirements** that the SoT does not specify. If something is missing, add an [OPEN] entry.
- **Do not create implementation directories** (`/core`, `/contracts`, `/packs`, …) unless a POC requirement needs them. The repository is documentation-first ([OD-P-01](docs/open-decisions.md#od-p-01)).
- **Provisional items (`OD-P-xx`) are NON-CANONICAL.** Never cite one as authority for building something.
- **Preserve requirement IDs and status tags exactly** as the SoT writes them.
- **One change, one pull request** (AGENT-29). A change that opens, decides or closes a decision includes, in the same pull request, the decision record in [`docs/decisions/`](docs/decisions/README.md), the matching SoT edit and the regenerated register.
- **Never hand-edit the generated register section** in [`docs/open-decisions.md`](docs/open-decisions.md). Run `python3 tools/check_docs_consistency.py --write`.
- **Run `python3 tools/check_docs_consistency.py --check` before every push.** CI runs the same check (`docs-consistency`) on every pull request.
- **Issued external documents are frozen.** Files marked "frozen record" (for example the Tushe specification in `docs/poc/tushe/`) must never be edited. Propose changes in a delta file next to them, and do not put internal strategy, benchmark details or hidden test material in any document meant for an external partner.

## 5. Where things are

See [`docs/README.md`](docs/README.md) for the full map of which document owns which question. Decision records live in [`docs/decisions/`](docs/decisions/README.md).
