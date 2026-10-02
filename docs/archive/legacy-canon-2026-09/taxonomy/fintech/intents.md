> **ARCHIVED — NON-AUTHORITATIVE.** This document predates `docs/NOEMA_SOURCE_OF_TRUTH.md` (v1.1) and is superseded by it. It is kept only as historical reasoning. Its vocabulary and decisions (for example READY / WAITING / BLOCKED trust states, Execution or Action Contracts, a separate Validation layer, "intent infrastructure" or "Intent OS" framing, and card-replacement or account-inquiry wedges) are not current. Do not implement, cite or quote from it. See `docs/archive/README.md`.

Intents

Status: Foundational
Version: 0.1
Domain: Taxonomy / Fintech
Canonical Path: taxonomy/fintech/intents.md

⸻

1. Definition

A Fintech Intent is a canonical classification of an Actor objective involving financial services, financial accounts, financial instruments, payments, transfers, money movement, credit, savings, investments, or related financial operations.

The Fintech Intent Taxonomy provides the domain-specific vocabulary through which Noema represents financial objectives without conflating:

* what the Actor wants,
* what financial resource or instrument is involved,
* what Action may eventually be required,
* whether the Actor is authorized,
* whether the Intent is trusted,
* whether execution is permitted,
* and what actually occurred.

The taxonomy therefore classifies financial Intent semantics, not execution procedures.

The canonical distinction remains:

Actor
  ↓
Intent
  ↓
Fintech Intent Classification
  ↓
Validation
  ↓
Trust
  ↓
Action Graph
  ↓
Action Contracts
  ↓
Execution
  ↓
Outcome

⸻

2. Purpose

The Fintech Intent Taxonomy exists to provide a stable semantic vocabulary for financial objectives expressed by Actors.

It enables Noema to distinguish between materially different objectives such as:

TRANSFER_FUNDS
PAY_MERCHANT
SEND_MONEY
WITHDRAW_FUNDS
DEPOSIT_FUNDS
OPEN_ACCOUNT
CLOSE_ACCOUNT
FREEZE_CARD
REPLACE_CARD
DISPUTE_TRANSACTION
REQUEST_CREDIT
REPAY_CREDIT

The taxonomy is not an execution API.

It does not specify:

* which provider must be used,
* which capability must execute an Intent,
* whether the Actor is authorized,
* whether a transaction should be approved,
* how a transaction is technically processed,
* or whether execution will succeed.

⸻

3. Core Principle

The taxonomy classifies what the Actor intends to accomplish in the financial domain.

It does not prescribe how the objective must be accomplished.

For example:

Intent:
"Send ₦100,000 to my supplier."

may classify as:

TRANSFER_FUNDS

The eventual Action Graph may contain:

Resolve Recipient
      ↓
Verify Source Account
      ↓
Validate Transfer
      ↓
Request Transfer
      ↓
Verify Transfer Outcome

The taxonomy therefore remains independent of the operational realization.

⸻

4. Intent Taxonomy Boundary

The Fintech Intent Taxonomy sits within the broader Noema Intent model.

General Intent
      │
      └── Domain = FINTECH
              │
              ├── Money Movement
              ├── Payments
              ├── Accounts
              ├── Cards
              ├── Credit
              ├── Savings
              ├── Investments
              ├── Transactions
              ├── Fees
              ├── Limits
              ├── Disputes
              └── Financial Information

The taxonomy provides classification.

The canonical Intent object remains defined by the Intent ontology.

⸻

5. Intent vs Action

A fintech Intent must not be reduced to an Action.

For example:

Intent:
Replace my expired card.

may require:

CHECK_CARD_STATUS
CHECK_REPLACEMENT_ELIGIBILITY
CREATE_REPLACEMENT_REQUEST
VERIFY_REPLACEMENT

The Intent is:

REPLACE_CARD

The Actions are implementation-level operations required to fulfill it.

Therefore:

Fintech Intent ≠ Action

⸻

6. Intent vs Transaction

A financial Intent is not necessarily a financial transaction.

For example:

"What transactions happened on my account?"

is an information-retrieval Intent.

It does not itself create a transaction.

Similarly:

"Can I transfer ₦1,000,000?"

may represent an eligibility or information Intent rather than an instruction to execute a transfer.

Therefore:

Intent ≠ Transaction

⸻

7. Intent vs Authorization

A classified Intent does not establish authorization.

For example:

Intent:
TRANSFER_FUNDS

does not establish:

Actor authorized = TRUE

Authorization remains a Trust and policy concern.

Therefore:

TRANSFER_FUNDS
      ≠
AUTHORIZED_TRANSFER

⸻

8. Intent vs Outcome

The taxonomy represents desired objectives.

It does not represent what happened.

For example:

Intent:
TRANSFER_FUNDS

may result in:

Outcome:
COMPLETED

or:

Outcome:
FAILED

or:

Outcome:
UNKNOWN

The Outcome Taxonomy remains separate.

⸻

9. Top-Level Fintech Intent Families

The canonical domain taxonomy is organized into the following families:

1. Money Movement
2. Payments
3. Accounts
4. Cards
5. Transactions
6. Credit
7. Savings
8. Investments
9. Fees and Charges
10. Limits and Controls
11. Disputes and Recovery
12. Financial Information
13. Foreign Exchange
14. Compliance and Verification
15. Beneficiaries and Recipients
16. Financial Preferences and Instructions

The taxonomy may expand as additional domain requirements are established.

⸻

10. Money Movement

Money Movement Intents concern the movement of monetary value between financial resources, accounts, wallets, or recipients.

Core Intent classes include:

TRANSFER_FUNDS
SEND_MONEY
RECEIVE_MONEY
DEPOSIT_FUNDS
WITHDRAW_FUNDS
MOVE_FUNDS
SCHEDULE_TRANSFER
CANCEL_TRANSFER

⸻

10.1 TRANSFER_FUNDS

The Actor wants to move funds from one financial resource to another.

Example:

Transfer ₦500,000 from my current account to my savings account.

Canonical classification:

intent = TRANSFER_FUNDS

Relevant semantic fields may include:

source
destination
amount
currency
timing
purpose
constraints

⸻

10.2 SEND_MONEY

The Actor wants to send money to another Actor or recipient.

Example:

Send ₦50,000 to John.

Canonical classification:

intent = SEND_MONEY

Recipient resolution may be required before the Intent becomes resolved.

⸻

10.3 RECEIVE_MONEY

The Actor wants to receive funds.

Example:

I want to receive payment from my customer.

The Intent may require:

recipient_account
sender_reference
amount
currency
payment_method

depending on the expression.

⸻

10.4 DEPOSIT_FUNDS

The Actor wants to place funds into an account or financial resource.

Example:

Deposit ₦100,000 into my savings account.

⸻

10.5 WITHDRAW_FUNDS

The Actor wants to remove funds from an account or financial resource.

Example:

Withdraw ₦50,000 from my account.

Withdrawal may require additional semantic resolution concerning:

* source account,
* withdrawal mechanism,
* amount,
* currency,
* destination.

⸻

10.6 MOVE_FUNDS

A generalized Intent for moving funds where the precise operational transfer mechanism is not yet established.

Example:

Move some money into my savings.

The Intent may remain partially resolved until:

amount
source
destination

are established.

⸻

10.7 SCHEDULE_TRANSFER

The Actor wants a transfer to occur at a specified future time or according to a recurrence.

Example:

Transfer ₦100,000 to my landlord every month.

Temporal semantics must remain explicit.

⸻

10.8 CANCEL_TRANSFER

The Actor wants to cancel a transfer that has not reached an irreversible state.

Example:

Cancel the transfer I just made.

The relevant transfer must be resolved before execution can proceed.

⸻

11. Payments

Payment Intents concern the settlement of an obligation or purchase through a financial instrument or payment mechanism.

Core classes include:

MAKE_PAYMENT
PAY_MERCHANT
PAY_BILL
PAY_INVOICE
PAY_SUBSCRIPTION
REQUEST_PAYMENT
REFUND_PAYMENT

⸻

11.1 MAKE_PAYMENT

The Actor wants to make a payment.

Example:

Pay ₦20,000 for the service.

⸻

11.2 PAY_MERCHANT

The Actor wants to pay a merchant for goods or services.

Example:

Pay the restaurant ₦25,000.

⸻

11.3 PAY_BILL

The Actor wants to settle a bill.

Example:

Pay my electricity bill.

Relevant semantic fields may include:

biller
account_reference
amount
currency
payment_date

⸻

11.4 PAY_INVOICE

The Actor wants to settle a specific invoice.

Example:

Pay invoice INV-2048.

The invoice reference should be resolved before execution.

⸻

11.5 PAY_SUBSCRIPTION

The Actor wants to make a subscription payment.

Example:

Pay my monthly software subscription.

⸻

11.6 REQUEST_PAYMENT

The Actor wants another party to make a payment to them.

Example:

Request ₦100,000 from John.

This differs from:

SEND_MONEY

because the desired direction of value is reversed.

⸻

11.7 REFUND_PAYMENT

The Actor wants a payment refunded.

Example:

Refund the payment for order 123.

The original payment must be identifiable.

⸻

12. Account Intents

Account Intents concern creation, modification, closure, access, and management of financial accounts.

Core classes include:

OPEN_ACCOUNT
CLOSE_ACCOUNT
UPDATE_ACCOUNT
VIEW_ACCOUNT
SELECT_ACCOUNT
LINK_ACCOUNT
UNLINK_ACCOUNT
FREEZE_ACCOUNT
UNFREEZE_ACCOUNT

⸻

12.1 OPEN_ACCOUNT

The Actor wants to create a financial account.

Example:

Open a savings account for me.

⸻

12.2 CLOSE_ACCOUNT

The Actor wants to close an account.

Example:

Close my old current account.

The target account must be resolved.

Closure may also require downstream conditions such as:

* outstanding balance resolution,
* pending transactions,
* linked services,
* regulatory requirements.

These are execution concerns rather than taxonomy semantics.

⸻

12.3 UPDATE_ACCOUNT

The Actor wants to modify account information or configuration.

Example:

Change the address on my account.

The specific field may require additional semantic resolution.

⸻

12.4 VIEW_ACCOUNT

The Actor wants information about an account.

Example:

Show me my current account balance.

⸻

12.5 FREEZE_ACCOUNT

The Actor wants an account temporarily restricted.

Example:

Freeze my account.

⸻

12.6 UNFREEZE_ACCOUNT

The Actor wants an account restriction removed.

Example:

Unfreeze my account.

⸻

13. Card Intents

Card Intents concern payment cards and associated lifecycle operations.

Core classes include:

REQUEST_CARD
ACTIVATE_CARD
FREEZE_CARD
UNFREEZE_CARD
REPLACE_CARD
CANCEL_CARD
UPDATE_CARD
VIEW_CARD
REQUEST_CARD_PIN
CHANGE_CARD_PIN

⸻

13.1 REQUEST_CARD

The Actor wants a new card.

Example:

Send me a new debit card.

⸻

13.2 ACTIVATE_CARD

The Actor wants to activate a card.

Example:

Activate my new card.

⸻

13.3 FREEZE_CARD

The Actor wants a card temporarily prevented from use.

Example:

Freeze my card.

⸻

13.4 UNFREEZE_CARD

The Actor wants a previously frozen card restored to usable status.

Example:

Unfreeze my card.

⸻

13.5 REPLACE_CARD

The Actor wants an existing card replaced.

Possible reasons include:

EXPIRED
LOST
STOLEN
DAMAGED
COMPROMISED
EXPIRING
OTHER

The reason may be an Intent parameter rather than a distinct Intent class.

⸻

13.6 CANCEL_CARD

The Actor wants a card permanently cancelled.

This must remain distinct from temporary freezing.

FREEZE_CARD ≠ CANCEL_CARD

⸻

14. Transaction Intents

Transaction Intents concern transactions that have already occurred or are being queried.

Core classes include:

VIEW_TRANSACTION
SEARCH_TRANSACTIONS
EXPLAIN_TRANSACTION
VERIFY_TRANSACTION
DISPUTE_TRANSACTION
CANCEL_TRANSACTION

⸻

14.1 VIEW_TRANSACTION

The Actor wants to inspect a specific transaction.

Example:

Show me the transaction from yesterday.

⸻

14.2 SEARCH_TRANSACTIONS

The Actor wants to find transactions matching criteria.

Example:

Show all payments to Amazon this month.

⸻

14.3 EXPLAIN_TRANSACTION

The Actor wants an explanation or interpretation of a transaction.

Example:

What is this ₦15,000 charge?

This does not imply that the transaction is unauthorized.

⸻

14.4 VERIFY_TRANSACTION

The Actor wants to establish whether a transaction occurred or has a particular status.

Example:

Did the transfer go through?

⸻

14.5 DISPUTE_TRANSACTION

The Actor wants to challenge a transaction.

Example:

I don’t recognize this transaction.

The semantic classification should not itself assert fraud or unauthorized activity.

⸻

14.6 CANCEL_TRANSACTION

The Actor wants to cancel an existing transaction where cancellation is semantically applicable.

The actual ability to cancel depends on transaction state and external system authority.

⸻

15. Credit Intents

Credit Intents concern borrowing, credit facilities, repayment, and credit-related information.

Core classes include:

REQUEST_CREDIT
APPLY_FOR_LOAN
CHECK_CREDIT_ELIGIBILITY
VIEW_CREDIT
REPAY_CREDIT
SCHEDULE_REPAYMENT
MODIFY_REPAYMENT
CLOSE_CREDIT

⸻

15.1 REQUEST_CREDIT

The Actor wants access to credit.

Example:

I need ₦2 million in credit.

⸻

15.2 APPLY_FOR_LOAN

The Actor wants to submit a loan application.

Example:

Apply for a personal loan for me.

Application is an Intent.

Approval is not implied.

⸻

15.3 CHECK_CREDIT_ELIGIBILITY

The Actor wants to know whether they may qualify for a credit product.

Example:

Am I eligible for a ₦5 million loan?

This is distinct from:

APPLY_FOR_LOAN

⸻

15.4 VIEW_CREDIT

The Actor wants information about an existing credit facility.

Example:

How much do I still owe?

⸻

15.5 REPAY_CREDIT

The Actor wants to make a repayment.

Example:

Pay ₦100,000 toward my loan.

⸻

15.6 SCHEDULE_REPAYMENT

The Actor wants repayment to occur at a specified future time or recurrence.

⸻

16. Savings Intents

Savings Intents concern saving, allocating, or managing funds for savings objectives.

Core classes include:

CREATE_SAVINGS
CONTRIBUTE_TO_SAVINGS
WITHDRAW_FROM_SAVINGS
VIEW_SAVINGS
SET_SAVINGS_TARGET
MODIFY_SAVINGS_TARGET

⸻

16.1 CREATE_SAVINGS

The Actor wants to create a savings arrangement or account.

⸻

16.2 CONTRIBUTE_TO_SAVINGS

The Actor wants to allocate funds toward savings.

Example:

Put ₦50,000 into my savings goal.

⸻

16.3 WITHDRAW_FROM_SAVINGS

The Actor wants to remove funds from savings.

⸻

16.4 SET_SAVINGS_TARGET

The Actor wants to establish a savings objective.

Example:

I want to save ₦2 million for a house deposit.

This may create an Intent concerning a financial objective rather than immediately executing a transaction.

⸻

17. Investment Intents

Investment Intents concern acquiring, selling, holding, or obtaining information about investment assets.

Core classes include:

BUY_ASSET
SELL_ASSET
HOLD_ASSET
VIEW_INVESTMENT
VIEW_PORTFOLIO
REBALANCE_PORTFOLIO
TRANSFER_ASSET

⸻

17.1 BUY_ASSET

The Actor wants to acquire an investment asset.

Example:

Buy ₦500,000 worth of the fund.

⸻

17.2 SELL_ASSET

The Actor wants to dispose of an investment position.

Example:

Sell my shares in the fund.

⸻

17.3 VIEW_INVESTMENT

The Actor wants information about an investment.

⸻

17.4 VIEW_PORTFOLIO

The Actor wants information about their investment portfolio.

⸻

17.5 REBALANCE_PORTFOLIO

The Actor wants portfolio holdings adjusted toward a specified allocation.

The Intent expresses the desired portfolio state.

The resulting Action Graph determines how the change could be operationally realized.

⸻

18. Fees and Charges

Fee-related Intents concern understanding, disputing, or managing financial charges.

Core classes include:

VIEW_FEES
EXPLAIN_FEE
DISPUTE_FEE
REQUEST_FEE_WAIVER

⸻

18.1 VIEW_FEES

Example:

What fees have I been charged this month?

⸻

18.2 EXPLAIN_FEE

Example:

Why was I charged this ₦2,000 fee?

⸻

18.3 DISPUTE_FEE

Example:

I want to dispute this fee.

⸻

18.4 REQUEST_FEE_WAIVER

Example:

Can you waive this fee?

A request for a waiver does not imply that the waiver will be granted.

⸻

19. Limits and Controls

These Intents concern financial limits and operational controls.

Core classes include:

VIEW_LIMIT
REQUEST_LIMIT_CHANGE
SET_TRANSACTION_LIMIT
MODIFY_TRANSACTION_LIMIT

Example:

Increase my transfer limit.

The Intent represents the requested change.

It does not establish whether the change is permitted.

⸻

20. Disputes and Recovery

Dispute and recovery Intents concern contested or problematic financial events.

Core classes include:

DISPUTE_TRANSACTION
REPORT_UNAUTHORIZED_TRANSACTION
REPORT_FRAUD
REQUEST_REFUND
REQUEST_CHARGEBACK
RECOVER_FUNDS

⸻

20.1 REPORT_UNAUTHORIZED_TRANSACTION

The Actor reports that they do not recognize or authorize a transaction.

The taxonomy records the Actor’s claim.

It does not independently establish whether the transaction was unauthorized.

⸻

20.2 REPORT_FRAUD

The Actor reports suspected fraudulent financial activity.

The Intent records the Actor’s objective to report the activity.

Noema must not convert the Actor’s allegation into an independently established fact.

⸻

20.3 REQUEST_REFUND

The Actor requests return of funds.

⸻

20.4 REQUEST_CHARGEBACK

The Actor requests initiation of a chargeback process where such a mechanism exists.

⸻

20.5 RECOVER_FUNDS

The Actor wants funds recovered after a financial problem.

This may require clarification concerning:

* transaction,
* amount,
* recipient,
* reason,
* desired recovery mechanism.

⸻

21. Financial Information

Financial Information Intents concern obtaining information rather than changing financial state.

Core classes include:

VIEW_BALANCE
VIEW_STATEMENT
VIEW_TRANSACTION
VIEW_ACCOUNT_DETAILS
VIEW_PAYMENT_STATUS
VIEW_TRANSFER_STATUS
VIEW_EXCHANGE_RATE
VIEW_FEES
VIEW_LIMITS

These Intents generally do not imply a state-changing Action.

⸻

22. Foreign Exchange

Foreign Exchange Intents concern conversion between currencies.

Core classes include:

EXCHANGE_CURRENCY
CHECK_EXCHANGE_RATE
REQUEST_FX_QUOTE

⸻

22.1 EXCHANGE_CURRENCY

Example:

Convert $1,000 to naira.

⸻

22.2 CHECK_EXCHANGE_RATE

Example:

What is today’s USD/NGN exchange rate?

This is informational.

⸻

22.3 REQUEST_FX_QUOTE

Example:

Give me a quote for converting $5,000 to naira.

A quote request does not itself constitute an instruction to execute the conversion.

⸻

23. Compliance and Verification

Some financial objectives concern verification rather than movement of money.

Core classes include:

VERIFY_IDENTITY
COMPLETE_KYC
UPDATE_KYC_INFORMATION
VERIFY_ACCOUNT
VERIFY_SOURCE_OF_FUNDS
PROVIDE_FINANCIAL_DOCUMENT

These Intents must remain distinct from authorization.

For example:

VERIFY_IDENTITY

does not mean:

AUTHORIZED_FOR_ALL_ACTIONS

⸻

24. Beneficiary and Recipient Intents

Financial operations frequently depend on recipients or beneficiaries.

Core classes include:

ADD_BENEFICIARY
REMOVE_BENEFICIARY
UPDATE_BENEFICIARY
VIEW_BENEFICIARY
SELECT_BENEFICIARY

These may support other Intents without being semantically identical to them.

For example:

ADD_BENEFICIARY

is distinct from:

TRANSFER_FUNDS

even if adding the beneficiary is a prerequisite for executing the transfer.

⸻

25. Financial Preferences and Instructions

Some financial Intents establish preferences rather than immediate transactions.

Examples include:

SET_PAYMENT_PREFERENCE
SET_TRANSFER_PREFERENCE
SET_NOTIFICATION_PREFERENCE
SET_SAVINGS_PREFERENCE
SET_ACCOUNT_PREFERENCE

A preference may influence future Action Graph construction but must not silently create authorization for future execution.

⸻

26. Intent Parameters

A fintech Intent may contain domain-specific parameters.

Conceptually:

Intent {
    intent_type
    actor
    subject
    target
    amount
    currency
    source
    destination
    recipient
    instrument
    timing
    constraints
    purpose
    context
    provenance
}

Not every Intent requires every field.

Missing fields must remain explicitly unresolved where they are semantically necessary.

⸻

27. Amount

Financial amounts should be represented explicitly.

For example:

amount:
    value = 50000
    currency = NGN

Noema must not rely on ambiguous natural-language representations once the amount becomes canonical.

⸻

28. Currency

Currency should be explicit where material.

For example:

currency = NGN

An omitted currency may remain unresolved unless an applicable deterministic rule establishes it.

A model’s assumption must not silently become canonical currency information.

⸻

29. Source

Where funds are being moved, the source financial resource may be required.

Example:

source = account_123

If multiple accounts are possible and no deterministic rule resolves the source, clarification may be required.

⸻

30. Destination

The destination identifies where value should be directed.

It may be:

* account,
* wallet,
* card,
* merchant,
* beneficiary,
* financial institution,
* investment position,
* other supported financial resource.

Destination identity must be resolved before consequential execution where required.

⸻

31. Recipient

A recipient is a semantic entity to whom value is intended to be delivered.

Recipient resolution may use:

* explicit Actor identification,
* authoritative references,
* prior conversation context,
* beneficiary records,
* permitted external evidence.

Ambiguity must remain explicit.

⸻

32. Timing

Financial Intent may contain temporal requirements.

Examples:

immediately
tomorrow
Friday
monthly
every 30 days
before 18:00

The canonical Intent should represent temporal semantics explicitly rather than preserving them only as natural language.

⸻

33. Constraints

An Actor may specify constraints.

Examples:

amount <= ₦100,000
currency = NGN
execute_after = 09:00
recipient = beneficiary_123
do_not_use = credit

Constraints form part of Intent semantics and must be preserved through downstream planning.

⸻

34. Purpose

Some financial operations include a stated purpose.

Example:

Transfer ₦200,000 to John for rent.

The purpose may be represented as semantic information.

It should not automatically be treated as verified external fact.

⸻

35. Composite Fintech Intents

A single expression may contain multiple financial objectives.

Example:

Close my old account, transfer the remaining balance to my new account, and send me confirmation.

Possible Intent components:

CLOSE_ACCOUNT
TRANSFER_FUNDS
REQUEST_CONFIRMATION

The relationship between the components must preserve:

* ordering,
* dependencies,
* atomicity,
* partial-execution semantics,
* shared constraints.

The taxonomy does not determine those relationships; the Intent and Action Graph models do.

⸻

36. Informational vs State-Changing Intents

Fintech Intents should distinguish between objectives that seek information and objectives that seek financial state changes.

Informational

VIEW_BALANCE
VIEW_TRANSACTION
CHECK_EXCHANGE_RATE
VIEW_FEES
CHECK_CREDIT_ELIGIBILITY

State-changing

TRANSFER_FUNDS
PAY_BILL
OPEN_ACCOUNT
CLOSE_ACCOUNT
REPLACE_CARD
REPAY_CREDIT
BUY_ASSET

This distinction may influence downstream Trust and Action Graph requirements.

It does not itself establish risk or authorization.

⸻

37. Read vs Write Semantics

A useful secondary classification is:

READ
WRITE
CONTROL
GOVERNANCE

Examples:

VIEW_BALANCE        → READ
TRANSFER_FUNDS     → WRITE
FREEZE_CARD        → CONTROL
REQUEST_FEE_WAIVER → GOVERNANCE

This classification is supplementary.

It must not replace the canonical Intent identity.

⸻

38. Intent Specificity

The taxonomy should prefer the most specific canonical Intent that is actually established.

For example:

"Move money."

may initially resolve to:

MOVE_FUNDS

while:

"Transfer ₦50,000 from my current account to my savings account."

may resolve to:

TRANSFER_FUNDS

Specificity must be established from semantics rather than guessed.

⸻

39. Ambiguous Intent

If an expression supports multiple materially different fintech interpretations, the Intent remains ambiguous.

Example:

Pay John.

Possible interpretations:

SEND_MONEY
PAY_INVOICE
PAY_BILL

The system must not select a materially different Intent merely because one is statistically more likely.

Clarification or authoritative context may be required.

⸻

40. Unknown Intent

If Noema cannot establish which financial objective the Actor intended, the semantic state should remain:

UNKNOWN

Unknown must not become a canonical Intent merely because a model produced a plausible label.

⸻

41. Unsupported Intent

If the Actor expresses a financial objective for which the canonical taxonomy has no supported representation, the Intent may be:

UNSUPPORTED

The system should not force the expression into an unrelated Intent class merely to continue processing.

Taxonomy expansion may subsequently introduce a canonical class.

⸻

42. Intent Aliases

Natural-language expressions may map to the same canonical Intent.

For example:

"Send money"
"Transfer money"
"Move ₦50,000 to John"
"Pay John ₦50,000"

may, depending on semantic context, map to related but not necessarily identical canonical classes.

Aliases must therefore be contextual rather than purely lexical.

The canonical taxonomy identifier remains authoritative.

⸻

43. Canonical Identifiers

Each Intent class should have a stable machine-readable identifier.

Examples:

TRANSFER_FUNDS
SEND_MONEY
PAY_MERCHANT
OPEN_ACCOUNT
CLOSE_ACCOUNT
FREEZE_CARD
REPLACE_CARD
DISPUTE_TRANSACTION
REQUEST_CREDIT
REPAY_CREDIT
BUY_ASSET
SELL_ASSET

Human-readable descriptions may evolve.

Canonical identifiers should remain stable unless a formal taxonomy revision changes their semantics.

⸻

44. Intent Versioning

The taxonomy itself is versioned independently from individual Intent versions.

For example:

Taxonomy:
fintech-intents v0.1
Intent:
intent_123 v4

A taxonomy change must not silently mutate the semantic history of previously established Intents.

⸻

45. Taxonomy Evolution

New Intent classes may be introduced when:

1. a materially distinct objective exists,
2. existing classes cannot represent it without semantic distortion,
3. the distinction has architectural significance,
4. the new class has a clear definition,
5. its relationship to existing classes is documented.

Taxonomy growth should not produce unnecessary fragmentation.

⸻

46. Intent Classification Invariants

Invariant 1

A fintech Intent represents an Actor’s financial objective.

Invariant 2

Intent classification does not establish authorization.

Invariant 3

Intent classification does not establish Trust.

Invariant 4

Intent classification does not guarantee execution.

Invariant 5

Intent classification does not represent execution outcome.

Invariant 6

A model-generated classification is not automatically canonical.

Invariant 7

Material ambiguity must remain explicit.

Invariant 8

Unknown information must not silently become known information.

Invariant 9

Financial amounts and currencies must be explicit where semantically required.

Invariant 10

Recipient, source, and destination identity must not be guessed when materially ambiguous.

Invariant 11

Informational and state-changing objectives should remain distinguishable.

Invariant 12

Intent taxonomy must remain separate from Action Graph structure.

Invariant 13

Intent taxonomy must remain separate from Action Contract semantics.

Invariant 14

Intent taxonomy must remain separate from external financial-system state.

Invariant 15

An Intent class must not imply that the requested financial operation is permitted.

⸻

47. Canonical Classification Flow

The canonical fintech classification process is:

Actor Expression
       ↓
Interpretation
       ↓
Candidate Fintech Intent
       ↓
Semantic Resolution
       ↓
Fintech Intent Classification
       ↓
Canonical Intent
       ↓
Validation
       ↓
Trust
       ↓
Action Graph

Where ambiguity remains:

Candidate Intent
       ↓
Ambiguity
       ↓
Clarification
       ↓
Resolution

⸻

48. Relationship to Trust

A fintech Intent may have significant financial consequences.

However, the taxonomy itself does not determine whether the Intent should proceed.

For example:

Intent:
TRANSFER_FUNDS

may enter Trust evaluation involving:

* Actor identity,
* authorization,
* policy,
* risk,
* limits,
* approvals,
* transaction context,
* capability availability.

The Intent taxonomy merely establishes the semantic objective.

⸻

49. Relationship to Action Graph

Once a fintech Intent is sufficiently resolved, it may be realized through an Action Graph.

Example:

Intent:
TRANSFER_FUNDS
        ↓
Action Graph:
Resolve Source
      ↓
Resolve Destination
      ↓
Validate Transfer
      ↓
Check Required Approval
      ↓
Execute Transfer
      ↓
Verify Outcome

The graph is not encoded in the taxonomy.

⸻

50. Relationship to Outcome Taxonomy

A single fintech Intent can result in multiple operational outcomes.

Example:

Intent:
TRANSFER_FUNDS

may produce:

COMPLETED
FAILED
BLOCKED
WAITING
PARTIALLY_COMPLETED
UNKNOWN

The Outcome Taxonomy records the execution result.

The Fintech Intent Taxonomy records the Actor’s objective.

⸻

51. Canonical Fintech Intent Registry

The initial registry is:

Money Movement

TRANSFER_FUNDS
SEND_MONEY
RECEIVE_MONEY
DEPOSIT_FUNDS
WITHDRAW_FUNDS
MOVE_FUNDS
SCHEDULE_TRANSFER
CANCEL_TRANSFER

Payments

MAKE_PAYMENT
PAY_MERCHANT
PAY_BILL
PAY_INVOICE
PAY_SUBSCRIPTION
REQUEST_PAYMENT
REFUND_PAYMENT

Accounts

OPEN_ACCOUNT
CLOSE_ACCOUNT
UPDATE_ACCOUNT
VIEW_ACCOUNT
SELECT_ACCOUNT
LINK_ACCOUNT
UNLINK_ACCOUNT
FREEZE_ACCOUNT
UNFREEZE_ACCOUNT

Cards

REQUEST_CARD
ACTIVATE_CARD
FREEZE_CARD
UNFREEZE_CARD
REPLACE_CARD
CANCEL_CARD
UPDATE_CARD
VIEW_CARD
REQUEST_CARD_PIN
CHANGE_CARD_PIN

Transactions

VIEW_TRANSACTION
SEARCH_TRANSACTIONS
EXPLAIN_TRANSACTION
VERIFY_TRANSACTION
DISPUTE_TRANSACTION
CANCEL_TRANSACTION

Credit

REQUEST_CREDIT
APPLY_FOR_LOAN
CHECK_CREDIT_ELIGIBILITY
VIEW_CREDIT
REPAY_CREDIT
SCHEDULE_REPAYMENT
MODIFY_REPAYMENT
CLOSE_CREDIT

Savings

CREATE_SAVINGS
CONTRIBUTE_TO_SAVINGS
WITHDRAW_FROM_SAVINGS
VIEW_SAVINGS
SET_SAVINGS_TARGET
MODIFY_SAVINGS_TARGET

Investments

BUY_ASSET
SELL_ASSET
HOLD_ASSET
VIEW_INVESTMENT
VIEW_PORTFOLIO
REBALANCE_PORTFOLIO
TRANSFER_ASSET

Fees

VIEW_FEES
EXPLAIN_FEE
DISPUTE_FEE
REQUEST_FEE_WAIVER

Limits

VIEW_LIMIT
REQUEST_LIMIT_CHANGE
SET_TRANSACTION_LIMIT
MODIFY_TRANSACTION_LIMIT

Disputes and Recovery

DISPUTE_TRANSACTION
REPORT_UNAUTHORIZED_TRANSACTION
REPORT_FRAUD
REQUEST_REFUND
REQUEST_CHARGEBACK
RECOVER_FUNDS

Financial Information

VIEW_BALANCE
VIEW_STATEMENT
VIEW_ACCOUNT_DETAILS
VIEW_PAYMENT_STATUS
VIEW_TRANSFER_STATUS
VIEW_EXCHANGE_RATE
VIEW_FEES
VIEW_LIMITS

Foreign Exchange

EXCHANGE_CURRENCY
CHECK_EXCHANGE_RATE
REQUEST_FX_QUOTE

Compliance and Verification

VERIFY_IDENTITY
COMPLETE_KYC
UPDATE_KYC_INFORMATION
VERIFY_ACCOUNT
VERIFY_SOURCE_OF_FUNDS
PROVIDE_FINANCIAL_DOCUMENT

Beneficiaries

ADD_BENEFICIARY
REMOVE_BENEFICIARY
UPDATE_BENEFICIARY
VIEW_BENEFICIARY
SELECT_BENEFICIARY

Preferences

SET_PAYMENT_PREFERENCE
SET_TRANSFER_PREFERENCE
SET_NOTIFICATION_PREFERENCE
SET_SAVINGS_PREFERENCE
SET_ACCOUNT_PREFERENCE

⸻

52. Canonical Mental Model

The Fintech Intent Taxonomy can be reduced to five questions:

1. What financial objective does the Actor express?
2. What financial subject, resource, recipient, or instrument does it concern?
3. What semantic information is required to establish the objective?
4. Is the objective sufficiently resolved to become canonical Intent?
5. What downstream Trust and execution processes must evaluate it?

Therefore:

Financial Expression
        ↓
Financial Objective
        ↓
Intent Classification
        ↓
Semantic Resolution
        ↓
Canonical Fintech Intent
        ↓
Validation
        ↓
Trust
        ↓
Action Graph
        ↓
Execution
        ↓
Outcome

⸻

53. Final Definition

The Fintech Intent Taxonomy is Noema’s canonical domain vocabulary for representing Actor objectives involving money, payments, accounts, cards, credit, savings, investments, transactions, financial controls, disputes, and related financial operations.

Its central invariant is:

A fintech Intent describes what the Actor seeks to accomplish financially; it does not establish authorization, Trust, execution authority, business-state ownership, or execution outcome.

The canonical boundary remains:

Actor Expression
      ↓
Interpretation
      ↓
Fintech Intent
      ↓
Validation
      ↓
Trust
      ↓
Action Graph
      ↓
Action Contracts
      ↓
Execution
      ↓
Outcome

The taxonomy therefore provides Noema with a stable financial semantic layer while preserving the architectural separation between meaning, validity, authority, execution, and outcome.