# Free sample: “40 USDC funded” on Arc testnet is not 40 redeemable USDC

**Proof-focused crypto/DeFi payout verification — VM1 original demonstration, 17 October 2026.**

**Verdict: CONTRADICTED** for the claim that this particular Misthos bounty is funded with $40 of *redeemable mainnet* USDC. **CONFIRMED** for the narrower claim that its platform reports a **40-unit testnet-USDC escrow**. These are separate propositions: a live smart-contract transaction on a test chain can be real technical activity without conveying spendable dollars.

## Three public sources, one consistent chain

**1. Original advertised bounty:** [GitHub issue #182](https://github.com/vanduc2514/hackathon-circle-misthos/issues/182) includes a platform bot message claiming “Funded on Misthos: 40.00 USDC.” This is an advertisement of funding, not by itself a stablecoin withdrawal statement.

**2. Seller's live bounty record:** [Misthos issue API ISS-1010](https://mithios.nvduc.dev/api/v1/issues/ISS-1010) returns a funded state, a quoted amount of 40.00, and an escrow chain label of `arc-testnet`. At this check the record had no accepted worker payout (`paid_usdc=null`). A funding transaction hash and an escrow-address field establish a *platform claim* about where funds went; they do not prove that the locked token is Circle's spendable mainnet asset.

**3. Same operator's network and currency declaration:** [Misthos health endpoint](https://mithios.nvduc.dev/api/v1/health) identifies `chain=arc-testnet`, `chain_id=5042002`, `money=test`, and explicitly says that the USDC is supplied by a testnet faucet **with no real value**. The project's public GitHub deployment descriptor also maps the environment to chain ID 5042002, not Arc mainnet 5042.

## Payment test and limitations

| Test | Evidence | Verdict |
|---|---|---|
| Does the platform show 40 USDC funded? | Original issue and official issue API | **CONFIRMED** |
| Is this a real-chain-dollar payout on mainnet? | Official health states testnet faucet funds | **CONTRADICTED** |
| Did an independent worker actually receive spendable USDC? | No accepted payment in cited issue record; no mainnet ERC-20 transfer proved | **NOT CONFIRMED** |
| Does a transaction ID alone make the advertised “$40” spendable? | Mainnet chain and canonical token contract not shown | **CONTRADICTED** |

This is a noncustodial, **read-only** source investigation. We did **not** connect a wallet, run an exploit, spend gas, claim the task, transfer assets, inspect anyone's private records, or accept a payment. We also did **not** decode a historical ERC-20 receipt on mainnet; that would require independent mainnet RPC or explorer access and an exact token, recipient and transaction match.

**General rule:** before doing bounty work, verify (a) chain ID and mainnet/testnet, (b) whether the currency is redeemable native Circle USDC instead of a faucet or bridged/mock token, (c) payer escrow state, (d) worker eligibility and real gas/bond economics, and (e) an actual attributable final paid transaction. When a component is inaccessible, say **INCONCLUSIVE** rather than “paid.”

**Offer context:** This is a *free example only*, not a paid commission or investment recommendation. A distinct, mutually agreed original hashn contract for public crypto-payout due diligence is priced at **2 native Base USDC after accepted delivery**. No transaction, subscription, signature or secret is needed to view this sample.

**AI assistance disclosure:** The VM1 research worker prepared this original source-cited sample with AI assistance; no unverified human field observations are claimed.
