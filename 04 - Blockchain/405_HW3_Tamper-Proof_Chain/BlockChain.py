#!/usr/bin/env python3
"""Block Integrity -> Tamper Proof Chain: Homework

The goal of this homework is to extend the behavior of a block to created a chain and securely link  
them together using cryptography. In general, each block is used to hold a batch of transactions. In addition a cryptographic 
hash of the previous block in the chain and some other needed values for computation. 
In this homework each block will hold:
    * a string message (data)
    * its own block hash value
    * hash value of the previous block
    * nonce value which will be incremented when a block is mined

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this exercise located in same folder.

To test run 'Blockchain_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on this topic:
    https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/
"""
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class CBlock:
    # TODO 1: Initialize the values of a block
    # Make sure you distinguish between the genesis block and other blocks
    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        self.nonce = 0
        if previousBlock:
            self.previousHash = previousBlock.computeHash()
        else:
            self.previousHash = None
        self.blockHash = None

    # TODO 2: Compute the cryptographic hash of the current block.
    # Be sure which values must be considered to compute the hash properly. // data, previousHash, nounce
    # return the digest value
    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(bytes(str(self.data), "utf-8"))
        if self.previousHash:
            digest.update(bytes(str(self.previousHash), "utf-8"))
        digest.update(bytes(str(self.nonce), "utf-8"))
        return digest.finalize()

    # TODO 3: Mine the current value of a block
    # Calculates a digest based on required values from the block, such as:
    # data, previousHash, nonce
    # Make sure to compute the hash value of the current block and store it properly // done
    def mine(self, leading_zeros):
        target_prefix = "0" * leading_zeros
        while True:
            self.nonce += 1
            self.blockHash = self.computeHash()
            if self.blockHash.hex()[:leading_zeros] == target_prefix:
                break

    # TODO 4: Check if the current block contains valid hash digest values
    # Make sure to distinguish between the genesis block and other blocks
    # Make sure to compare both hash digest values:
    # The computed digest of the current block
    # The stored digest of the previous block
    # return the result of all comparisons as a boolean value // done
    def is_valid_hash(self):
        if self.previousBlock == None:
            return self.previousHash == None
        return self.blockHash == self.computeHash()
