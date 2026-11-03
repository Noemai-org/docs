# EXP-06 · Operator test of the evidence packet: protocol

Date: 2026-11-03 · Status: draft for the Founders (task EXP-06; owner C2 with the Founders, who supply the operators) · Derived and non-normative: the requirement is PERD REQ-EXP-004 (as amended by DEC-2026-10-31 D26). This file adds no requirement and sets no threshold.

## What this proves

That a person who works escalations can understand an escalated case, and decide the next action, from the evidence packet alone (REQ-EXP-004; US-03, US-14; SoT §18.4 rule 7). The measurement is the time to understand and every lookup the operator needed beyond the packet. Each gap becomes a packet change or a recorded decision.

## Before the first session

| Needed | Source | Owner |
|---|---|---|
| The packet exists on every escalation | EXP-05 Done (`RECORD_INVESTIGATION_EVIDENCE` attaches it; US-14 packet contains every listed element) | C2 |
| At least three operators who work escalations, from the Founders' network until a design partner exists | the Founders | Founders |
| Each operator's confidentiality terms confirmed | the Founders (outside the repositories) | Founders |
| At least five escalated cases per operator, synthetic, never from the held-out set (OD-16, REQ-AGT-004) | the benchmark generator's non-held-out cases, chosen by the Benchmark Owner agent | Benchmark Owner agent |
| The oracle answer for each case: what happened, and the next action | the case's oracle, read by the Benchmark Owner agent only | Benchmark Owner agent |
| A rendering of the packet that shows exactly the packet fields, masked (no other screen) | C2 | C2 |

The cases together cover, at least: an unknown outcome after a timeout (US-06), contradictory state (US-14), stale evidence, a pending settlement (US-17), and an ambiguous recipient. A case an operator has seen is not reused for them.

## A session (one operator, at least five cases)

1. Brief the operator in one minute: synthetic cases; they see the packet only; say aloud anything they would need to look up; there is no right pace.
2. For each case, the observer starts a timer when the packet is shown and records, without prompting:
   - **Lookups:** each fact the operator asks for or says they would look up, in their words, and why. A lookup is a gap even when the operator guesses right.
   - **Their answer:** what happened to the money or the case, and what they would do next.
   - **Confidence:** 1 (a guess) to 5 (certain).
3. The timer stops when the operator has stated both answers. The observer then compares them with the oracle: right or wrong on "what happened" and on "next action".
4. No hints. If the operator is stuck, they say so; that is recorded as a lookup of "unknown".

## The record

One file per session cycle in `docs/poc/execution/operator-tests/YYYY-MM-DD-EXP-06.md`, from [`../templates/operator-test-record.md`](../templates/operator-test-record.md): a row per case run (operator code, case ID, seconds to understand, lookups, both answers against the oracle, confidence) and a list of gaps. Operators are named O1, O2, O3; their names stay outside the repositories. No real customer data and no held-out material appears in the record.

## Turning gaps into changes

Every gap gets one line in the record's decision table, one of:

- **Packet change:** a change to REQ-EXP-004's packet contents or to the rendering, as a pull request against EXP-05 (a contract change follows AGENT-15), linked from the record.
- **Recorded decision:** why the packet stays as it is, with the owner's name and the date.

The task is Done when the record is committed with every gap decided (plan EXP-06, "Operator test record committed with changes or recorded decisions").

## What is not set here

No pass mark. PERD v1.19 and D26 give none, and a number invented here would be an external number (AGENT-18). The record reports the measured times, lookups and correctness as they are; the Founders may set a mark in a later decision record.

## Dates

EXP-06 is dated at the re-baseline (GOV-30). It starts when EXP-05 is Done on `main` and the Founders have named three operators.
