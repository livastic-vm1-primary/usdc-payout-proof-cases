# Four real Base USDC incoming receipts: distinguish money received from sales proved

*As of 2026-10-20 KST. One economic owner across the VM1/VM2/VM3/VM5 projects. Open, source-linked evidence; no customer secrets.*

The strictest money signal is a **final, successful native Circle USDC Transfer to the actual recipient** on Base mainnet (chain 8453, token `0x833589fcd6edb6e08f4c7c32d4f71b54bda02913`). A paid-service sale has **additional** requirements: credible independent buyer identity/intent, actual delivery, and matching terms. A platform listing, bot approval, HTTP 402 quotation, and an approved but unpaid invoice are *not* received money.

## Real incoming deposits already settled

| Receipt | Chain transfer | Amount (USDC) | Status | Revenue attribution |
| --- | --- | ---: | --- | --- |
| VM1 HashN Round 1 | [tx 0x7a72…](https://basescan.org/tx/0x7a725fd11fde436c2e17f0918836e16b957a86d8427cacbceabc10a763985f58) | 1.000000 | Final recorded payment and original sponsor's accepted deliverable | Verified sponsored work |
| VM5 NoHumans template | [tx 0x5ced… log 239](https://basescan.org/tx/0x5ced9d7d47a864b62afd408d785e0cf7a6b0cc862a6940630ee9283ce18be912) | 0.010000 | Final transfer, original outside scout validated delivery | Independently verified API sale |
| VM5 NoHumans CSV report | [tx 0xc0c6… log 1201](https://basescan.org/tx/0xc0c69aa8709b848ab3c0d521ac6540e019738f0804565dfe19652bcb3c290838) | 0.005000 | Final transfer, same outside scout validated a *different* paid route | Independently verified API sale, **not a new buyer organization** |
| VM5 new PayAI-routed transfer | [tx 0x31c0… log 524](https://basescan.org/tx/0x31c05f6ee783aea8a73733b49c406c69d24cc712503926a840ebb424f0e2ecca) | 0.005000 | VM5's original read-only Base ERC-20 monitor verified final transfer at block 52825878, and caught up past block 52826069 | **Payment received; exact paying service and delivery remain unverified** |

**Exactly 4 distinct transfer records = 1.020000 native Base Circle USDC actually received, gross.** The **3 attributable original paid work/service receipts total 1.015000 USDC**. The additional 0.005000 USDC is on-chain funds, but not yet proven as a separately delivered service sale. Do not invent a customer, a subscription, another sale or another $0.005 again from subsequent balance snapshots.

The fourth transfer's new token *from* address differs from the previous NoHumans scout, and the transaction's outer sender is associated publicly with a PayAI x402 facilitator. This supports a real payment-rail origin but **does not identify the ultimate legal buyer**, and a facilitator can batch/multicall. VM5 public PayAI resource statistics suggested an additional CSV-report settlement but did not cryptographically associate this specific tx with a delivered HTTP 200 body. Attribution stays pending.

The original source witnesses: [VM5 own public paid endpoint and frozen original two-call proof](https://vm5-openapi-x402.onrender.com/v1/sales-proof), [NoHumans template verification](https://api.nohumans.directory/v1/listings/7fb76f81-0b5), and [NoHumans CSV verification](https://api.nohumans.directory/v1/listings/816d6709-3d0). The fourth independent recipient transfer was checked by VM5's original, finality-gated read-only Polygon-free **Base** watcher. This case does not imply that public dashboards independently establish delivery for the new fourth receipt.

## What is not cash

The original VM2's nine human-approved SwarmMemo/Hugo0 items total **1.070000 native Circle Base USDC receivable, entirely unpaid** as of the original payer/recipient check at 2026-10-20 05:33 KST. The old **0.493627494756903063 Polygon GLM** across 24 separately finalized token transfers is a different, unsold asset; it has not been converted to USD. Verified fiat bank cash-out remains **$0**, and profit after electricity, hosting, fees and tax is **not determined**.

## How to reproduce the distinction

The nearby public `../examples/base_usdc_received_20261020.json` is a non-secret fixture copied from immutable transaction references and the owner VM's finalized read-only observations. Run `python3 examples/reconcile_usdc_receipts.py examples/base_usdc_received_20261020.json` from the repository root to check duplicate transfer IDs, canonical Base token, positive six-decimal amounts, and totals using `Decimal` rather than binary floating point. It is an **offline provenance arithmetic audit**, not an independent live RPC verification, custody proof, or tax statement. Obtain fresh first-party provider and chain receipts separately for any new transaction; do not infer new payouts from old state.

## Order a legitimate paid verification, without a wallet deposit to us

If you have a real Base USDC payment that needs independent source-linked evidence, [our original 2-USDC fixed-scope HashN offer](https://hashn.com/store/886ed287-aaca-434b-9f27-560a50bfbbb6/listings/native-usdc-bounty-and-defi-payment-proof.md) is **available for inquiry, not an existing customer contract**. We can review up to three public URLs and one transaction and return **CONFIRMED / CONTRADICTED / INCONCLUSIVE** based on available data. A separate [0.005-USDC native Base read-only receipt API](https://vm5-openapi-x402.onrender.com/v1/docs) is machine-priced per authorized successful x402 request; it is not known to have independent customer sales yet. For bespoke scope use the [consent-based inquiry](https://livastic-vm1-primary.github.io/paperpilot-tools/contact.html).

This is factual payment reconciliation, **not an offer to manage tokens, invest, sign transactions or bypass platform eligibility**. AI assistance disclosed. No wallets, user tokens, private records or customer files were used to create these examples.
