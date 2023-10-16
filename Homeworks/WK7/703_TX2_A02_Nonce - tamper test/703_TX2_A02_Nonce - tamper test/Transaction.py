from gzip import READ
from operator import truediv
from optparse import AmbiguousOptionError
import math

REWARD_VALUE = 25.0
NORMAL = 0
REWARD = 1

from Signature import *

class Tx:
    def __init__(self, type = NORMAL):
        
        self.type = type
        self.inputs = []
        self.outputs = []
        self.sigs = []
        self.reqd = []

    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))

    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))

    def add_reqd(self, addr):
        self.reqd.append(addr)

    def sign(self, private):
        message = self.__gather()
        newsig = sign(message, private)
        self.sigs.append(newsig)
               
    def is_valid(self):

        if self.type == REWARD:
            if len(self.inputs)!=0 and len(self.outputs)!=1:
                return False
            return True
        
        else:
            total_in = 0
            total_out = 0
            message = self.__gather()
            for addr,amount in self.inputs:
                found = False
                for s in self.sigs:
                    if verify(message, s, addr):
                        found = True
                if not found:
                    # print ("No good sig found for " + str(message))
                    return False
                if amount < 0:
                    return False
                total_in = total_in + amount
            for addr in self.reqd:
                found = False
                for s in self.sigs:
                    if verify(message, s, addr):
                        found = True
                if not found:
                    return False
            for addr,amount in self.outputs:
                if amount < 0:
                    return False
                total_out = total_out + amount     
            return total_out <= total_in

    def __gather(self):
        data=[]
        data.append(self.inputs)
        data.append(self.outputs)
        data.append(self.reqd)
        return data

    def __repr__(self):

        repr_str = "INPUTS:\n"
        for addr, amt in self.inputs:
            repr_str = repr_str + str(amt) + "from" + str(addr) + "\n"

        repr_str += "OUTPUTS:\n"
        for addr, amt in self.outputs:
            repr_str = repr_str + str(amt) + "to" + str(addr) + "\n"

        repr_str += "EXTRA REQUIRED SIGNATURES:\n"     
        for req_sig in self.reqd:
            repr_str = repr_str + str(req_sig) + "\n"

        repr_str += "SIGNATURES:\n"     
        for sig in self.sigs:
            repr_str = repr_str + str(sig) + "\n"

        repr_str += "END\n"
        
        return repr_str
    
    def total_input(self):
        return math.fsum(amount for _, amount in self.inputs) if self.type == NORMAL else REWARD_VALUE

    def total_output(self):
        return math.fsum(amount for _, amount in self.outputs)