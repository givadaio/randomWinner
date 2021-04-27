#!/usr/bin/env python3

import json
import requests
import sys

TOKEN = "BLOCKFROST API TOKEN"

headers = {"project_id": TOKEN}

def getDelegators(pool_id):

    url = f"https://cardano-mainnet.blockfrost.io/api/v0/pools/{pool_id}/delegators"

    resp = requests.get(url, headers=headers)
    return json.loads(resp.text)

def getStakeAmount(accounts, pool_id, epoch):
    amounts = {}

    for account in accounts:
        address = account['address']
        url = f"https://cardano-mainnet.blockfrost.io/api/v0/accounts/{address}/history"

        resp = requests.get(url, headers=headers)
        history = json.loads(resp.text)

        for snapshot in history:
            if snapshot["active_epoch"] == epoch:
                if snapshot["pool_id"] == pool_id:
                    amounts[address] = int(int(snapshot["amount"])/1000000)

    return amounts

if __name__ == "__main__":
    pool_id = sys.argv[1]
    epoch = int(sys.argv[2])
    accounts = getDelegators(pool_id)
    
    amounts = getStakeAmount(accounts, pool_id, epoch)

    print(json.dumps(amounts, sort_keys=True, indent=4))
