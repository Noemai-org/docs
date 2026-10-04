# Requested additions to the Noema × Tushe specification (v1.2)

These requirements add to the *Noema × Tushe Synthetic Enterprise Environment: Technical Requirements & Acceptance Specification v1.0*. Each one is needed for Noema's proof-of-concept tests.

## 1. Version tokens on case resources

- Every read of a case resource returns a version token (for example an ETag or a version number).
- Case update and create-with-deduplication accept an expected version (for example `If-Match` or an `expected_version` field).
- If the stored version differs from the expected version, the service rejects the request with a distinct error, separate from validation and authorisation errors, and applies no change.

## 2. Lookup by idempotency key

- Case creation accepts a client-supplied idempotency key.
- The case service supports looking up a case by that key, so a client can find out whether a request whose response was lost actually created a case.

## 3. Additional fault families

The fault controller can produce each of the following, reproducibly from a scenario ID and seed:

- rate limiting: HTTP 429 with and without a `Retry-After` header, and burst throttling;
- pagination and partial pages;
- schema drift: added, renamed or missing fields, and unknown enum values;
- responses that arrive just before or just after the client's timeout;
- clock skew between the logical services (for example ledger, switch and settlement reporting different times for the same event).

## 4. Delayed settlement events under the virtual clock

- Settlement updates can be scheduled to occur after a configurable delay measured on the controllable virtual clock, so that tests can advance the clock and observe a pending settlement become settled, failed or reversed.
- The corresponding settlement events are emitted at the scheduled virtual time.
