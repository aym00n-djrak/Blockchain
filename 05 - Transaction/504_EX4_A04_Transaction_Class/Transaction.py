#!/usr/bin/env python3
"""
Transaction Class 

The goal of this exercise is to learn how to complete transaction class.
A transaction is composed of a list of Inputs and a list of outputs, and few methods.
add_input and add_output are already completed in the previous tutorials.
In this exercise, we will add a sign method to the class. With this method, we can
sign a transaction. 

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this tutorial located in same folder.

To test run 'Transactions_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
"""
# 1085367 Rémy JOVANOVIC 1085377 Olgierd KRZYŻANIAK

from Signature import sign as sign_data


class Tx:
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.sigs = []
        self.reqd = (
            []
        )  # A placeholder for any other extra required signature (e.g. escrow)

    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))

    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))

    # TODO: Complete the method
    # In this method:
    #   1 - You should collect all data of the transaction, and then
    #   2 - Sign data and add it to the variable sigs
    #
    # It is good idea to create a seperate private or protected method to collect all data of
    # transaction before signing it.
    def sign(self, private_key):
        data_to_sign = self.__collect_data()
        signature = sign_data(data_to_sign, private_key)
        self.sigs.append(signature)

    def __collect_data(self):
        data_to_sign = [self.inputs, self.outputs, self.reqd]
        return data_to_sign
