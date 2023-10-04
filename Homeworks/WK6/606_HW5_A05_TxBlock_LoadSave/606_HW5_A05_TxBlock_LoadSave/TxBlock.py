#!/usr/bin/env python3
"""Transactions -> Ledger (Block Validation): Exercise 

The goal of this exercise is to learn how a blockchain for the transactions is implemented.
In this scenario the implementation of the block is extended with a validation function for the block. 
Each block contains his own hash value, transaction data and the hash value of previous block. 
Check the provided code in both files, Signature.py, Transaction.py and Blockchain.py. 
In Blockchain.py the is_valid() method is provided to check the validity of the block, 
rebuild the Block module to satisfy our testing scenario. 
The testing scenario here covers tempering the data of one block. 
This tempering should be detectable.   

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this exercise located in same folder.

To test run 'TxBlock_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * Check previous tutorials for more information on this topic
"""

##1085367 Rémy JOVANOVIC 1085377 Olgierd KRZYŻANIAK

from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from Transaction import Tx

class TxBlock (CBlock):
    
    # TODO 1: Initialize the block
    # Each block contains a list for the data and a hash value to previous block
    def __init__(self, previousBlock):
        super().__init__([], previousBlock)
    
    # TODO 2: Append the transaction to the data list
    def addTx(self, Tx_in):
        self.data.append(Tx_in)
    
    # TODO 3: Check the validity of each transaction in the data list 
    # and check the validity of other blocks in the chain to make the cchain tamper-proof
    # Expected return value is true or false
    def is_valid(self):
        # Check the block's own validity using the base class's is_valid method
        if not super().is_valid():
            return False

        # Check the validity of each transaction in the current block's data list
        for tx in self.data:
            if not tx.is_valid():
                return False

        return True