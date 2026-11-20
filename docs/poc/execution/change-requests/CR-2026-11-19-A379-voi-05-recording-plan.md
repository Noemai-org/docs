# Change request: CR-2026-11-19-A379-voi-05-recording-plan

- Change ID: CR-2026-11-19-A379-voi-05-recording-plan
- Requester: Founders (A379, in DEC-2026-11-19-founder-intron-data-terms-a377-a379), relayed to the Repo Steward
- REQ IDs affected: REQ-VOI-004 (unchanged; VOI-05 implements it). Task VOI-05. No requirement is added or removed.
- Behaviour before: plan v1.24, VOI-05: "Voice subset recording plan: consent form, speaker mix, accents, noise conditions; raw audio storage, access and deletion rules"; done when "Plan signed by FND; storage path has restricted access and a retention timer". The draft in noema#201 asked for the Founder's signature, a consent text after legal review and a counsel review; noema#294 carried those as Founder items.
- Behaviour after: plan v1.25, VOI-05: the recording plan covers speaker mix, accents, noise conditions and devices, and the raw audio storage, access and deletion rules, with the Integrator account's retention set to zero days. The consent form for people outside the team, the counsel review and the Founder's signature are removed (A379; A378: counsel blocks nothing). Done when: plan written; storage path has restricted access and a retention timer; the Integrator account's retention is zero days; raw audio never in the repository or CI artifacts (REQ-VOI-004). The Founders keep the right to hold Intron to its written commitments (A377).
- Safety and security impact: none of the Tier 0 gates, thresholds or TTLs change. REQ-VOI-004 stands: raw audio never in the repository or in CI artifacts, only in the bench Environment's private store, deleted per the plan. Synthetic audio stays labelled SYNTHETIC. Masking before any provider call stays (AGENTS §10). The change removes a process step (consent form, counsel); it is the Founders' decision.
- Tests added or changed: none (documentation).
- Schedule and dependency impact: VOI-05 no longer waits on the Founder's signature; VOI-06 (Needs VOI-05) can start when the plan is written. VOI-06's and VOI-08's "consent" wording and the demo pre-flight's "consent forms in hand for any live voice" are not changed here: A379 names VOI-05 only (the Founders or the Architect say if they change).
- SoT or PERD text changes: none. The PERD's REQ-VOI-004 acceptance criteria stand.
- Decision owner: Founders
- Decision record: DEC-2026-11-19-founder-intron-data-terms-a377-a379 (A377 to A379)
- Migration and rollback: none. Applied as `NOEMA_POC_4WEEK_PLAN_v1.25.md`, with `tasks.csv` and the task table regenerated from it (VOI-05's row and done-when text only). Roll back by deleting v1.25 and regenerating from v1.24.
