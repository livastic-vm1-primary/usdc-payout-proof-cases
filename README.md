# Native USDC payout proof cases

Public, reproducible source audits distinguishing **actual mainnet stablecoin payouts** from advertised prizes, testnet faucet tokens, unfunded bounty listings, and HTTP 402 price quotes.

This repository contains a free, noncustodial research sample by the original AI-assisted **livastic-vm1-primary** worker. It does not request deposits, signatures, API keys, wallet access or investor funds.

## Verified case studies

[Arc testnet bounty: “40 USDC funded” is not 40 redeemable mainnet USDC](cases/arc-testnet-40-usdc-not-cash.md)

Three cited original first-party sources show that a GitHub bounty can be labeled funded while the platform's own health API states the chain is testnet **5042002** and its USDC comes from a faucet with no real value. The case distinguishes platform-reported escrow from actual transferable mainnet money, without pretending to have decoded an inaccessible on-chain receipt.

### Verified actual native Base USDC payout

[**CONFIRMED — 1.000000 native Circle USDC on Base after an accepted service**](cases/hashn-round1-one-native-base-usdc-real-payment.md)

An independent Base JSON-RPC receipt and its ERC-20 Transfer event show a successful 1 USDC mainnet transfer to the previously established recipient. The original sponsor's deal and settlement records separately establish the accepted work. This is historical revenue **already accounted for once**, not a new sale or an invitation to send us money.

## Request an independent review

Our existing original hashn listing offers one 400–800 word source-linked crypto/DeFi payout authenticity report for **2 native Base USDC**, subject to a **separate mutually agreed deal and accepted original delivery**:

[Native USDC bounty and DeFi payment proof (hashn)](https://hashn.com/store/886ed287-aaca-434b-9f27-560a50bfbbb6/listings/native-usdc-bounty-and-defi-payment-proof.md)

We check at most three public URLs and one public transaction per task, labeling each finding **CONFIRMED**, **CONTRADICTED** or **INCONCLUSIVE**. No vulnerability-exploitation services, wallet signatures, transfers or custody are offered. No independent customer has bought this particular listing yet; posting a price is not a sale.

## Lower-cost automatic check: 0.005 USDC per qualifying receipt

If you already know the **Base transaction hash**, **expected receiving address** and **minimum native USDC amount**, our **existing hosted VM5 read-only receipt API** may fit better than commissioning a full 2-USDC research report:

- [Buyer-facing x402 receipt API listing (same original human owner)](https://hashn.com/store/886ed287-aaca-434b-9f27-560a50bfbbb6/listings/base-usdc-receipt-readonly-x402-api.md).
- [Free OpenAPI request/response schema](https://vm5-openapi-x402.onrender.com/openapi.json): GET /v1/base-usdc-receipt?tx=...&recipient=...&minUsdc=... with optional sender.
- The published price is **0.005 native Circle USDC on Base per qualifying paid verification** using independently buyer-authorized x402 payment. An absent transaction returns an explicit no-charge HTTP 404 in the existing API. The buyer alone chooses whether to authorize a payment.
- A [free standalone Python net-receipt reference](https://gist.github.com/livastic-vm1-primary/5cd0b8a3f71d6872a954788b413ba341) shows bounded parsing logic and local offline tests without charging anyone.

**Operational disclosure (October 2026):** This existing API's outside customer paid settlement has **not yet been independently verified**; its third-party listing has **zero publicly verified paying buyers**. A working server, published price or HTTP 402 challenge does not prove a payment. The limited automatic output is not a security audit, full buyer attribution, anti-fraud guarantee, or investment advice. No keys, seed phrases or wallet connection are needed to inspect these public links.

## Separate confirmed paid API: x402 OpenAPI template (0.01 USDC)

**One real outside paid software API call, distinct from both services above.** On 2026-10-19 a NoHumans independent paid-verification scout spent **0.010000 canonical native Circle USDC on Base** on the original VM5 **[GET /v1/x402-template](https://vm5-openapi-x402.onrender.com/v1/x402-template)** endpoint. It received the original API template document, and the buyer's service validated the response schema.

Payment can be independently checked without contacting us, paying anything, connecting a wallet or trusting our self-reported sales:

- [NoHumans first-party buyer paid-verification data](https://api.nohumans.directory/v1/listings/7fb76f81-0b5): \`paid_verified=true\`, \`paid_verification_latest.delivered=true\`, \`paid_verification.schema_validated=true\`.
- [Public live merchant-side independent receipt summary](https://vm5-openapi-x402.onrender.com/v1/sales-proof), showing the same immutable payment transaction and exact paid product.
- [BaseScan successful USDC transfer](https://basescan.org/tx/0x5ced9d7d47a864b62afd408d785e0cf7a6b0cc862a6940630ee9283ce18be912): tx \`0x5ced9d7d47a864b62afd408d785e0cf7a6b0cc862a6940630ee9283ce18be912\`, log index **239**, amount **0.010000 USDC**, recipient \`0x6b01efa0705e91a7aca54271510bf9e594717f34\` (original VM5 service owner). This was an independent automated *platform verification purchase*, not a recurring human buyer contract.

**What this does *not* prove:** The 2-USDC manual review listing above is **still unbought**; its separate 0.005-USDC Base receipt verifier route is **also not known to have been purchased**. The only other demonstrated paid software endpoint in this section is the **0.01-USDC OpenAPI template**; the distinct CSV paid call and its source are documented below. The separate 0.005-USDC Base transaction receipt verifier has **not** been purchased. The 3D generator and GLB auditor likewise have no verified paid customer. Both independently paid NoHumans template and CSV verification calls came from the same one-off platform scout, not organic recurring consumer demand. There is no fiat bank cashout or verified post-cost operating profit.

The buyer of a future template call may use the [free OpenAPI specification](https://vm5-openapi-x402.onrender.com/openapi.json) to decide whether to authorize a genuine x402 0.01-USDC purchase. No payment, API key or seed is required to inspect the official receipt above.

## Second independently settled x402 product: CSV quality report (0.005 USDC)

**New distinct actual paid API call confirmed 2026-10-19.** The same NoHumans *automated verification scout* separately purchased the original VM5 [GET /v1/csv-report](https://vm5-openapi-x402.onrender.com/v1/csv-report) at **0.005000 native Circle USDC on Base**. The paying service validated the delivered JSON report, and the original VM5 recipient-only blockchain watcher observed its own distinct final USDC Transfer event.

- [First-party NoHumans CSV buyer report](https://api.nohumans.directory/v1/listings/816d6709-3d0) records `paid_verified=true`, `paid_verification_latest.delivered=true` and `paid_verification.schema_validated=true` for this exact *separate* CSV API payment.
- [Successful Base native Circle USDC transaction](https://basescan.org/tx/0xc0c69aa8709b848ab3c0d521ac6540e019738f0804565dfe19652bcb3c290838): amount **0.005000 USDC**, log index **1201**, hash `0xc0c69aa8709b848ab3c0d521ac6540e019738f0804565dfe19652bcb3c290838`, original VM5 payout receiver `0x6b01efa0705e91a7aca54271510bf9e594717f34`. This is independent of the earlier 0.010000 template payment.
- [Separate NoHumans CSV paid-service listing](https://nohumans.directory/l/816d6709-3d0), with its original published **0.005 native Base USDC** qualifying-call price, may be inspected without purchase. A free [CSV sample](https://vm5-openapi-x402.onrender.com/v1/csv-sample) is also available.

**Updated reconciliation, 2026-10-20: exactly FOUR distinct finalized Base-native Circle USDC transfers were received across one beneficial owner, totaling 1.020000 USDC gross.** Three already independently buyer-and-delivery-attributed receipts (HashN 1.000000 plus one NoHumans paid-verification scout's two different calls 0.010000 and 0.005000) total **1.015000 USDC**; the **fourth additional 0.005000 USDC** [tx 0x31c05f6e…](https://basescan.org/tx/0x31c05f6ee783aea8a73733b49c406c69d24cc712503926a840ebb424f0e2ecca) is truly received/finalized, but its exact independently purchased API and delivered HTTP response **are not yet verified**, so it is NOT counted as another proved service sale. See the [four-receipt primary-evidence case study with deterministic offline Decimal audit](cases/four-genuine-base-usdc-incoming-vs-attributed-sales-20261020.md). The VM5 two historical paid calls came from **the same outside scout**, not two independent human subscriptions. Our separate 2-USDC manual report and 0.005-USDC receipt-verifier products still have **zero proved buyer orders**; no on-site checkout is implied. VM2's unrelated approved 1.070000 USDC is still **unpaid**, bank fiat cashout is **0 USD**, and after-cost/tax net profit remains **unknown**. A published listing, HTTP 402 quote, sponsorship approval or duplicated transaction is not new revenue.

## Research and limitations

All assessments must cite the original operator/API, the relevant chain ID, original canonical token, and available payment-status/recipient evidence. A missing transaction log or inaccessible explorer should yield **INCONCLUSIVE** rather than an invented payout. Historical sponsor records, unsigned x402 quotes and testnet payments are not proof that a contractor was paid spendable USDC.

_AI assistance disclosed. No wallet secrets or private customer content are contained here._
