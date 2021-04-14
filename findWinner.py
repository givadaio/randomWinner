#!/usr/bin/env python3

# Courtesy of givada

import argparse
import json
import random

def getDelegatorList(delegatorFile):

    delegatorList = []

    with open(delegatorFile, 'r') as f:
        rawJson = f.read()

        delegators = json.loads(rawJson)

        for address, stake in delegators.items():
            stake = int(stake)
            entries = [address] * stake
            delegatorList += entries

    return delegatorList
            

def findWinner(blockNumber, delegatorList):
    random.seed(blockNumber)

    listEntry = random.randint(0, len(delegatorList)-1)
    print(f"[*] randomEntry: {listEntry}")

    return delegatorList[listEntry]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--blockNumber", required=True, help="The winning block number")
    parser.add_argument("--delegator-file", required=True, help="A json file containing a list of delegators and their live stake")

    args = parser.parse_args()

    delegatorList = getDelegatorList(args.delegator_file)

    winner = findWinner(args.blockNumber, delegatorList)
    print(f"~*~*~*~* We have a winner: {winner}")



