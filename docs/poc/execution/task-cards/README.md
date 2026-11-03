# Task cards

- A task card is required before a task starts (plan §4.1; REQ-AGT-002).
- Cards use the PERD template: [`../../perd/templates/task-card.md`](../../perd/templates/task-card.md). Acceptance criteria are copied verbatim from the PERD REQ blocks (PERD v1.2; GOV-20 and ENV-13 from PERD v1.3; PLT-01 to PLT-04 from PERD v1.4; the ENV-13 relay wording from PERD v1.5; PCK-01, PCK-02 and UND-05 from PERD v1.6 and v1.7).
- File name: `<TASK-ID>.md`, for example `ENV-08.md`.
- A card is changed only by its owner, in a PR, and says what changed and why.
- This index is generated from the card files and the plan by `python3 tools/plan_index.py --write`; CI runs `--check`. Never edit it by hand.

| Card | Task | Day (plan v1.8) |
|---|---|---|
| [GOV-19](GOV-19.md) | Founders approve, amend or reject DEC-2026-10-12 and SoT v1.4 | Mon 12 Oct |
| [PLT-01](PLT-01.md) | Create the `noema` skeleton per DEC-2026-10-13 R1 and PERD v1.5 §64.2 | Fri 16 Oct |
| [GOV-20](GOV-20.md) | Decide where the public webhook receiver runs and how it is secured | Fri 16 Oct |
| [PLT-02](PLT-02.md) | CI pipeline | Wed 4 Nov |
| [PLT-03](PLT-03.md) | `tools/lint` | Wed 4 Nov |
| [PLT-04](PLT-04.md) | Docker Compose with the six networks of PERD §65.1 and the profiles `dev`, `ci`, `bench` and `demo` | Wed 4 Nov |
| [ENV-11](ENV-11.md) | Tushe adapter mapping to PERD §34.4 payloads | Wed 4 Nov |
| [PCK-01](PCK-01.md) | Fintech pack v1 rewritten to SoT §15.3 shapes against the CON-01 pack schema | Wed 4 Nov |
| [UND-05](UND-05.md) | Intent Compiler on the fintech pack | Wed 4 Nov |
| [ENV-09](ENV-09.md) | Hostility proxy | Wed 4 Nov |
| [ENV-10](ENV-10.md) | Event-feed poller on Tushe `GET /v1/events` by sequence cursor, persisting into the inbox table | Wed 4 Nov |
| [PCK-02](PCK-02.md) | `packcheck validate` | Wed 4 Nov |
| [ENV-08](ENV-08.md) | Build `mock-case` per REQ-ENV-008, with its fault hooks and truth endpoint, plus the core's case... | Wed 4 Nov |
| [ENV-13](ENV-13.md) | Webhook relay | Wed 4 Nov |
| [ENV-14](ENV-14.md) | G0-N, the Noema half of G0, Thu 22 Oct 17:00 | Wed 4 Nov |
| [OUT-01](OUT-01.md) | Outcome Verifier, verify-by-key scope | Mon 9 Nov |
| [ENV-12](ENV-12.md) | Walk through, agree and sign the acceptance worksheet with Tushe at the joint session | To be confirmed by Tushe (G0-T) |
| [UND-12](UND-12.md) | Async safety of the model service's blocking HTTP transports | Tue 1 Dec |
