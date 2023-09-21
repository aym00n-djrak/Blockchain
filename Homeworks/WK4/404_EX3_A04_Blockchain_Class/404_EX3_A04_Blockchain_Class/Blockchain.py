#!/usr/bin/env python3
"""Block Integrity -> Blockchain Data Structure: Exercise 1

The goal of this exercise is to learn how a simple blockchain can be created and securely linked 
together using cryptography. In general, each block is used to hold a batch of transactions. In addition a cryptographic 
hash of the previous block in the chain and some other needed values for computation. 
For the simplicity of this exercise each block will hold a string message (data) and hash of the previous block (previousBlock).  
The computeHash() method should compute the cryptographic hash of the current block. 
Be sure which values must be considered to compute the hash properly.

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
    previousHash = None
    previousBlock = None
    data = None
    
    # TODO 1: Initialize a block
    # Make sure you initialize the genesis block and transaction blocks differently
    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        if self.previousBlock:
            self.previousHash = self.previousBlock.computeHash()
        else:
            self.previousHash = None
    
    # TODO 2: Compute the hash of a the current block
    # Make sure you include all required data
    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256())
        if type(self.data) != bytes:
            data_string = str(self.data).encode('utf-8')
        else:
            data_string = self.data
        digest.update(data_string)
        if self.previousBlock:
            digest.update(self.previousHash.encode('utf-8'))
        return digest.finalize().hex()