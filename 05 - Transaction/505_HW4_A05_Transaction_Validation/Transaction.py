#!/usr/bin/env python3
"""
Transaction Class 

The goal of this exercise is to learn how to complete transaction class.
A transaction is composed of a list of Inputs and a list of outputs, and few methods.
add_input() and add_output(), and sign() are already completed in the previous tutorials and exercise.
In this hoemwork, we will add another method is_valid() to the class. With this method, we can
validate a transaction. 

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this tutorial located in same folder.

To test run 'Transactions_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
"""
# 1085367 Rémy JOVANOVIC 1085377 Olgierd KRZYŻANIAK

from Signature import verify, sign as sign_data


class Tx:
    inputs = None
    outputs = None
    sigs = None
    reqd = None

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

    # TODO 1: Complete the method
    # We would like to have another method to add extra required signature if needded (e.g. escrow)
    # with this method, we can specify other required signature to the transaction by adding the
    # public key of the required signature
    # If this signature is needed, later we can check if the transaction is also signed by that person/party.
    def add_reqd(self, addr):
        self.reqd.append(addr)

    def sign(self, private_key):
        data_to_sign = self.__collect_data()
        signature = sign_data(data_to_sign, private_key)
        self.sigs.append(signature)

    def __collect_data(self):
        data_to_sign = [self.inputs, self.outputs, self.reqd]
        return data_to_sign

    # TODO 2: Complete the method
    # This method is used to validate a transaction.
    # To validate a transaction, we must check few important things:
    #   1 -  Every entery in inputs need to be signed by the relevant sender, and
    #   2 -  If an extra required signature is needed, the signature need to be verified too, and
    #   3 -  The total amount of outputs must not exceed the total amount of inputs.
    def is_valid(self):
        data = self.__collect_data()

        # Check if every entry in inputs is signed by the relevant sender
        for from_addr, amount in self.inputs:
            if not any(verify(data, sig, from_addr) for sig in self.sigs):
                return False

        # If extra required signatures are needed, verify them
        for addr in self.reqd:
            if not any(verify(data, sig, addr) for sig in self.sigs):
                return False

        # Calculate the total input and output amounts
        total_input = sum(amount for _, amount in self.inputs)
        total_output = sum(amount for _, amount in self.outputs)
        # print(total_input, total_output)

        # Check if total output amount does not exceed the total input amounta and both values are positive
        if total_output > total_input:
            return False

        if any(amount <= 0 for _, amount in self.inputs) or any(
            amount <= 0 for _, amount in self.outputs
        ):
            return False

        return True
