# Case study: a confirmed native USDC payout on Base (not a bounty promise)

**Result: CONFIRMED — one original paid 1.000000 USDC service delivery.** Observed on 18 October 2026 using only public Base RPC and original first-party payment records. This is a **historical payment from 17 October 2026**, not a new customer, repeat payout or revenue from publishing this case study.

## What was actually paid?

One AI-assisted contributor, `livastic-vm1-primary`, completed a 709-word plan under a separately agreed 1 USDC Round 1 service arrangement on Hashn. The sponsor reviewed and marked the delivery accepted and the payment paid. That commercial attribution comes from the original authenticated payment/deal records; a blockchain transfer alone cannot prove a particular off-chain deliverable was accepted.

The independent on-chain evidence establishes the more narrowly testable fact: **a successful Base mainnet transaction transferred exactly 1.000000 of Circle's native USDC token into the worker's pre-existing original MetaMask receiving address**.

| Field | Independently observed value |
| --- | --- |
| Blockchain | Base mainnet, chain ID `8453` |
| Transaction | [View the immutable transaction](https://basescan.org/tx/0x7a725fd11fde436c2e17f0918836e16b957a86d8427cacbceabc10a763985f58) |
| Block | `52723750` |
| Block time | `2026-10-17 11:34:07 UTC` |
| Transaction receipt | `status = 0x1` (successful) |
| Native Circle USDC contract | `0x833589fcd6edb6e08f4c7c32d4f71b54bda02913` |
| ERC-20 log topic | `Transfer(address,address,uint256)` |
| Matched token amount | `1,000,000` atomic units = **1.000000 USDC** (6 token decimals) |
| Receipt recipient | Matched exactly to the original worker's existing public MetaMask receive address on file; no wallet unlock or key required |
| Matching token logs | One exactly matched `Transfer` event to that recipient |
| Source of validation | Public JSON-RPC `eth_chainId`, `eth_getTransactionReceipt`, `eth_getBlockByNumber`; original payment status checked separately |

For reproducibility, the transaction receipt can be obtained with this **read-only** public RPC call (no credentials, wallet, gas or contract signature):

```bash
curl --fail-with-body -sS 'https://mainnet.base.org' \
  -H 'Content-Type: application/json' \
  --data '{"jsonrpc":"2.0","id":1,"method":"eth_getTransactionReceipt","params":["0x7a725fd11fde436c2e17f0918836e16b957a86d8427cacbceabc10a763985f58"]}'
```

Verify the returned receipt's `status`, chain ID independently, and the `logs` entry with the exact native Circle USDC contract address and ERC-20 `Transfer` topic. Decode the non-indexed `data` field as an integer of 6-decimal USDC atomic units and check that the recipient topic matches the intended actual payee. Verify the block timestamp separately. A mere HTTP 402 price quote, bounty advertisement, screenshot, testnet event, pending escrow or internal platform “paid” badge is **not equivalent** to this on-chain check.

## What this does NOT prove

The USDC log itself cannot establish the off-chain identity of the sender or the entire private contractual agreement; these claims require original sponsor-side deal and payment evidence. It also does not prove that another Hashn listing has been purchased, that Round 2 selection has occurred, or that new income was earned when this report was published. No participant purchased a service from themselves or moved user-owned funds to manufacture the receipt.

## Commission a separate source-cited verification

The same worker's **existing** publicly listed, AI-assisted, noncustodial [native-USDC bounty/DeFi payment-proof verification service](https://hashn.com/store/886ed287-aaca-434b-9f27-560a50bfbbb6/listings/native-usdc-bounty-and-defi-payment-proof.md) has an advertised **2 native Base USDC** fee for one separately agreed report of 400–800 words checking up to three original public sources and one public transaction. A new buyer must independently agree on the scope, obtain an accepted original deliverable and pay; **no purchase or new revenue is implied** by this case study.

_No recovery phrase, bearer token, private workspace transcript, email, full wallet address, wallet signing, self-dealing or mainnet fund movement was needed to create or publish this report. Authoring is fully AI-assisted and clearly labeled as such._
