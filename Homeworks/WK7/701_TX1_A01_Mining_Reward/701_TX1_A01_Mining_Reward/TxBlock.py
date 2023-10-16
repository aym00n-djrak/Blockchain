from BlockChain import CBlock
from Signature import generate_keys, sign, verify


class TxBlock (CBlock):

    def __init__(self, previousBlock):
        super(TxBlock, self).__init__([], previousBlock)
    
    def addTx(self, Tx_in):
        self.data.append(Tx_in)
    
    def is_valid(self):
        if not super(TxBlock, self).is_valid():
            return False
        for tx in self.data:
            if not tx.is_valid():
                return False
        return True