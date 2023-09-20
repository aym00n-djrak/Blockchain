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
        if self.previousBlock:
            self.previousHash = self.previousBlock.computeHash()
        else:
            self.previousHash = None       
        self.nonce = 0
        self.hash = None
        
    # TODO 2: Compute the cryptographic hash of the current block. 
    # Be sure which values must be considered to compute the hash properly.
    # return the digest value
    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())

        if type(self.data) == str:
            digest.update(self.data.encode('utf-8'))
        elif type(self.data) == bytes:
            digest.update(self.data)

        if self.previousHash:
            if type(self.previousHash) == str:
                digest.update(self.previousHash.encode('utf-8'))
            elif type(self.previousHash) == bytes:
                digest.update(self.previousHash)

        digest.update(str(self.nonce).encode('utf-8'))

        return digest.finalize().hex()
       
    # TODO 3: Mine the current value of a block
    # Calculates a digest based on required values from the block, such as:
    # data, previousHash, nonce
    # Make sure to compute the hash value of the current block and store it properly 
    def mine(self, leading_zeros):
        target = '0' * leading_zeros
        while True:
            self.nonce += 1
            self.hash = self.computeHash()
            self.previousHash = self.previousBlock.computeHash() if self.previousBlock else None
            if self.hash[:leading_zeros] == target:
                print(self.nonce)        
                break
                
    # TODO 4: Check if the current block contains valid hash digest values 
    # Make sure to distinguish between the genesis block and other blocks
    # Make sure to compare both hash digest values:
    # The computed digest of the current block
    # The stored digest of the previous block
    # return the result of all comparisons as a boolean value 
    def is_valid_hash(self):
        current_block_valid = self.hash == self.computeHash()
    
        if self.previousBlock:
            if (current_block_valid and 
                self.previousHash == self.previousBlock.hash and 
                self.previousBlock.is_valid_hash()):
                return True
            else:
                return False
        return current_block_valid

