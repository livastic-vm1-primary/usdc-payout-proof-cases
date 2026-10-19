#!/usr/bin/env python3
"""Offline receipt provenance arithmetic; no network, credentials or transfers."""
import json, re, sys
from decimal import Decimal
from pathlib import Path

CANONICAL_TOKEN = "0x833589fcd6edb6e08f4c7c32d4f71b54bda02913"
TRANS = re.compile(r"0x[a-fA-F0-9]{64}$")
ADDR = re.compile(r"0x[a-fA-F0-9]{40}$")

def reconcile(records):
    if not isinstance(records, list):
        raise ValueError("expected list")
    seen = set()
    total = Decimal("0")
    attributed = Decimal("0")
    for item in records:
        if item.get("chainId") != 8453 or item.get("token", "").lower() != CANONICAL_TOKEN:
            raise ValueError("wrong Base mainnet chain/token")
        if not TRANS.fullmatch(item.get("txHash", "")) or not ADDR.fullmatch(item.get("recipient","")):
            raise ValueError("invalid public receipt transaction/recipient")
        index = item.get("logIndex")
        if index is not None and (type(index) is not int or index < 0):
            raise ValueError("invalid logIndex")
        k = (item["txHash"].lower(), index)
        if k in seen:
            raise ValueError("double counted same receipt")
        seen.add(k)
        amount = item.get("amountUSDC", "")
        if not isinstance(amount, str) or not re.fullmatch(r"(?:0|[1-9][0-9]*)\.[0-9]{6}", amount):
            raise ValueError("USDC amount must have exact six decimals")
        x = Decimal(amount)
        if x <= 0 or not (item.get("finalityVerified") is True):
            raise ValueError("not a positive finalized native USDC receipt")
        total += x
        if item.get("purchaseAndDeliveryVerified") is True:
            attributed += x
        elif item.get("purchaseAndDeliveryVerified") is not False:
            raise ValueError("missing deliberate revenue attribution flag")
    return {
        "distinctIncomingEvents": len(seen),
        "grossFinalizedReceivedUSDC": format(total, ".6f"),
        "externallyAttributedCompletedWorkOrSalesUSDC": format(attributed, ".6f"),
        "finalizedButDeliveryUnattributedUSDC": format(total - attributed, ".6f"),
        "fiatCashedOutUSD": "0",
        "afterCostProfitUSD": None,
        "onlineVerificationPerformed": False,
    }

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("base_usdc_received_20261020.json")
    data = json.loads(path.read_text(encoding="utf-8"))
    print(json.dumps(reconcile(data), indent=2))

if __name__=="__main__":
    main()
