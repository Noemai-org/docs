# Task cards

- A task card is required before a task starts (plan §4.1; REQ-AGT-002).
- Cards use the PERD template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Acceptance criteria are copied verbatim from the PERD REQ blocks (PERD v1.2; GOV-20 and ENV-13 from PERD v1.3; PLT-01 to PLT-04 from PERD v1.4; the ENV-13 relay wording from PERD v1.5).
- File name: `<TASK-ID>.md`, for example `ENV-08.md`.
- A card is changed only by its owner, in a PR, and says what changed and why.
- This index is generated from the card files and the plan by `python3 tools/plan_index.py --write`; CI runs `--check`. Never edit it by hand.

| Card | Task | Day (plan v1.5) |
|---|---|---|
| [GOV-19](GOV-19.md) | Founders approve, amend or reject DEC-2026-10-12 and SoT v1.4 | Mon 12 Oct |
| [PLT-01](PLT-01.md) | Create the `noema` skeleton per DEC-2026-10-13 R1 and PERD v1.5 §64.2 | Fri 16 Oct |
| [GOV-20](GOV-20.md) | Decide where the public webhook receiver runs and how it is secured | Fri 16 Oct |
| [PLT-02](PLT-02.md) | CI pipeline | Mon 19 Oct |
| [PLT-03](PLT-03.md) | `tools/lint` | Mon 19 Oct |
| [PLT-04](PLT-04.md) | Docker Compose with the six networks of PERD §65.1 and the profiles `dev`, `ci`, `bench` and `demo` | Mon 19 Oct |
| [ENV-11](ENV-11.md) | Tushe adapter mapping to PERD §34.4 payloads | Tue 20 Oct |
| [ENV-09](ENV-09.md) | Hostility proxy | Wed 21 Oct |
| [ENV-10](ENV-10.md) | Event-feed poller on Tushe `GET /v1/events` by sequence cursor, persisting into the inbox table | Wed 21 Oct |
| [ENV-08](ENV-08.md) | Build `mock-case` per REQ-ENV-008, with its fault hooks and truth endpoint, plus the core's case... | Thu 22 Oct |
| [ENV-13](ENV-13.md) | Webhook relay | Thu 22 Oct |
| [ENV-14](ENV-14.md) | G0-N, the Noema half of G0, Thu 22 Oct 17:00 | Thu 22 Oct |
| [ENV-12](ENV-12.md) | Walk through, agree and sign the acceptance worksheet with Tushe at the joint session | To be confirmed by Tushe (G0-T) |
