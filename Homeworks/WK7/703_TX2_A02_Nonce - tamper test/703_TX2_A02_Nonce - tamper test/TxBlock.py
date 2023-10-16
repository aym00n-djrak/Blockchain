import math
import secrets
from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

import random

REWARD_VALUE = 25.0
leading_zeros = 2
next_char_limit = 50
NORMAL = 0

class TxBlock (CBlock):

    def __init__(self, previousBlock):
        self.nonce = secrets.randbelow(2**256)
        super(TxBlock, self).__init__([], previousBlock)

    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(bytes(str(self.data), 'utf8'))
        digest.update(bytes(str(self.previousHash), 'utf8'))
        digest.update(bytes(str(self.nonce), 'utf8'))
        return digest.finalize()

    def addTx(self, Tx_in):
        self.data.append(Tx_in)

    def __count_totals1(self):
        total_in = 0
        total_out = 0
        for tx in self.data:
            for addr, amt in tx.inputs:
                total_in = total_in + amt if tx.type == NORMAL else total_in + REWARD_VALUE 
            for addr, amt in tx.outputs:
                total_out = total_out + amt
        return total_in , total_out

    def __count_totals(self):
        return math.fsum(tx.total_input() for tx in self.data), math.fsum(tx.total_output() for tx in self.data)


    def is_valid(self):

        if not super(TxBlock, self).is_valid():
            return False

        for tx in self.data:
            if not tx.is_valid():
                return False

        if self.blockHash and not self.good_nonce():
             return False
        
        total_in, total_out = self.__count_totals()

        return total_in >= total_out


    def good_nonce(self):
        return self.blockHash == self.computeHash() 

    def find_nonce(self):
        digest = self.computeHash()
        while not (digest.startswith(b'0' * leading_zeros) and digest[leading_zeros] <= next_char_limit):
            self.nonce = secrets.randbelow(2**256)
            digest = self.computeHash()
        self.blockHash = digest
        return self.nonce