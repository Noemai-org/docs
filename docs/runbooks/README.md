# Runbooks

Scaffolds for the POC operational runbooks. Each has the same headings (Purpose, When to use, Preconditions, Steps, Verification, Rollback or recovery, Owner, Source). None has steps yet: they are written when the backend skeleton exists (PERD §61.2, steps P0 and P4) and tested with the real system before any customer-facing action (SoT §39, [OD-P-04](../open-decisions.md#od-p-04)).

| Runbook | Purpose |
|---|---|
| [local-setup](local-setup.md) | Bring up the POC environment on one machine with one command. |
| [seed-and-reset](seed-and-reset.md) | Seed the synthetic environment and reset it to a known state for replay. |
| [fault-injection](fault-injection.md) | Run a deterministic fault plan against the synthetic environment. |
| [benchmark-run](benchmark-run.md) | Run the benchmark suite and produce scored results. |
| [provider-switch](provider-switch.md) | Switch the model or speech provider by configuration. |
| [kill-switch-and-rollback](kill-switch-and-rollback.md) | Disable all writes for a tenant in one step, and roll back to the previous image tags and pack and policy versions. |
| [incident-triage](incident-triage.md) | Classify a failure or incident by severity (S0–S3) and turn it into a permanent regression case. |
| [evidence-reconstruction](evidence-reconstruction.md) | Reconstruct a decision and its outcome from the Record alone. |
| [key-rotation](key-rotation.md) | Rotate the grant and confirmation HMAC key without downtime, and the separate per-tenant webhook secret. |
