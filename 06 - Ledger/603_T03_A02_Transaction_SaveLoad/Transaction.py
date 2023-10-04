#!/usr/bin/env python3
"""Transactions -> Ledger (Transaction Save and Load): Tutorial 3

The goal of this tutorial is to learn how storing and loading a transaction from and to
a file system works. For this purpose you need to check the provided code in both files, Signatue.py and Transaction_t.py. 
then, rebuild the transaction module to satisfy our testing scenario.   

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this exercise located in same folder.

To test run 'Transaction_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * Check previous tutorials for more information on this topic:
"""
from Signature import *


class Tx:
    # TODO 1: Create and assign an empty list for each of those variables:
    # input, output, sigs and reqd.
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.sigs = []
        self.reqd = []

    # TODO 2: Append a new value to the input list
    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))

    # TODO 3: Append a new value to the output list
    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))

    # TODO 4: Append a new value to the reqd list
    def add_reqd(self, addr):
        self.reqd.append(addr)

    # TODO 5: Sign a message and append the signature to sign list
    def sign(self, private):
        message = self.__gather()
        newsig = sign(message, private)
        self.sigs.append(newsig)

    def __gather(self):
        data = []
        data.append(self.inputs)
        data.append(self.outputs)
        data.append(self.reqd)
        return data

    # TODO 6: Iterate through the different lists and verify if provided values and signatures are valid
    def is_valid(self):
        total_in = 0
        total_out = 0
        message = self.__gather()
        for addr, amount in self.inputs:
            found = False
            for s in self.sigs:
                if verify(message, s, addr):
                    found = True
            if not found:
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
        for addr, amount in self.outputs:
            if amount < 0:
                return False
            total_out = total_out + amount
        if total_out > total_in:
            return False
        return True
