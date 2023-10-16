from BlockChain import CBlock
from Signature import generate_keys, sign, verify
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

import random

REWARD_VALUE = 25.0
leading_zeros = 2
next_char_limit = 20

class TxBlock (CBlock):

    def __init__(self, previousBlock):
        self.nonce = "A random nonce"
        super(TxBlock, self).__init__([], previousBlock)

    def addTx(self, Tx_in):
        self.data.append(Tx_in)

    def __count_totals(self):
        total_in = 0
        total_out = 0
        for tx in self.data:
            for addr, amt in tx.inputs:
                total_in = total_in + amt
            for addr, amt in tx.outputs:
                total_out = total_out + amt
        return total_in, total_out

    def is_valid(self):
        if not super(TxBlock, self).is_valid():
            return False
        for tx in self.data:
            if not tx.is_valid():
                return False
        
        total_in, total_out = self.__count_totals()
        
        Tx_Balance = round(total_out - total_in, 10)
        
        if  Tx_Balance > REWARD_VALUE:
            return False
        return True

    def good_nonce(self):
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(bytes(str(self.data), 'utf8'))
        digest.update(bytes(str(self.previousHash), 'utf8'))
        digest.update(bytes(str(self.nonce), 'utf8'))
        
        hash_result = digest.finalize()
        zeros = bytes('0' * leading_zeros, 'utf8')
        
        if hash_result[:leading_zeros] == zeros:
            return True
        return False

 

    def find_nonce(self):
        self.nonce = 0
        while not self.good_nonce():
            self.nonce += 1
            print(f'trying nonce: {self.nonce}', end='\r')
        
        print('\n')
        return True