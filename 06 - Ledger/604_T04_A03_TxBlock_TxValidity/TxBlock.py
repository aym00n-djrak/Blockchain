#!/usr/bin/env python3
"""Transactions -> Ledger (Transaction and Blocks): Tutorial 4

The goal of this tutorial is to learn how a blockchain for the transactions is implemented.
In this scenario the implementation of the block is minimal. Each block contains only his
own hash value, transaction data and the hash value of previous block. Check the provided 
code in both files, Signature.py, Transaction.py and Blockchain.py. then, 
rebuild the Block module to satisfy our testing scenario.   

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this exercise located in same folder.

To test run 'TxBlock_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * Check previous tutorials for more information on this topic
"""
from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from Transaction import Tx


class TxBlock(CBlock):
    # TODO 1: Initialize the block
    # Each block contains a list for the data and a hash value to previous block
    def __init__(self, previousBlock):
        self.data = []
        self.previousBlockHash = previousBlock.computeHash() if previousBlock else None
        self.prev_block_hash = previousBlock.computeHash() if previousBlock else None

    # TODO 2: Append the transaction to the data list
    def addTx(self, Tx_in):
        self.data.append(Tx_in)

    # TODO 3: Check the validity of each transaction in the data list
    # Expected return value is true or false
    def is_valid(self):
        # Check if the previous block hash is correct
        if self.previousBlockHash:
            if self.previousBlockHash != self.prev_block_hash:
                return False

        # Check the validity of each transaction in the block
        for tx in self.data:
            if not tx.is_valid():
                return False

        return True
