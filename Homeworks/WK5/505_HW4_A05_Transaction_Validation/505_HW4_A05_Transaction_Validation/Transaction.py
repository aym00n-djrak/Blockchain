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

from Signature import *


class Tx:
    inputs = None
    outputs = None
    sigs = None
    reqd = None

    # TODO 1: Complete the method
    # These three methods are already done in the previous tutorials
    # you can copy and paste the previous codes here
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

    # TODO 2: Complete the method
    # We would like to have another method to add extra required signature if needded (e.g. escrow)
    # with this method, we can specify other required signature to the transaction by adding the
    # public key of the required signature
    # If this signature is needed, later we can check if the transaction is also signed by that person/party.
    def add_reqd(self, addr):
        self.reqd.append(addr)

    # TODO 3: Complete the method
    # This method is also already done in the previous tutorials.
    # you can copy and paste the previous codes here

    def gather(self):
        data = []
        data.append(self.inputs)
        data.append(self.outputs)
        data.append(self.reqd)
        return data

    def sign(self, private):
        data = self.gather()
        self.sigs.append(sign(data, private))

    # TODO 4: Complete the method
    # This method is used to validate a transaction.
    # To validate a transaction, we must check few important things:
    #   1 -  Every entery in inputs need to be signed by the relevant sender, and
    #   2 -  If an extra required signature is needed, the signature need to be verified too, and
    #   3 -  The total amount of outputs must not exceed the total amount of inputs.


    def is_valid(self):

        # Obtenir la somme des montants d'entrée et de sortie
        total_in = sum([amount for addr, amount in self.inputs])
        total_out = sum([amount for addr, amount in self.outputs])

        # Vérifier que la somme des montants de sortie ne dépasse pas la somme des montants d'entrée
        if total_out > total_in:
            return False
        
        # Vérification pour s'assurer que toutes les entrées et les sorties sont positives.
        if any(amount < 0 for _, amount in self.inputs) or any(amount < 0 for _, amount in self.outputs):
            return False

        # Vérifier si chaque entrée est signée par l'expéditeur approprié.
        data = self.gather()
        for i, (addr, amount) in enumerate(self.inputs):
            if not verify(data, self.sigs[i], addr):
                return False
        
        # Vérification pour s'assurer que toutes les entrées et les sorties sont positives.
        for addr, amount in self.inputs:
            if amount < 0:
                return False
                
        for addr, amount in self.outputs:
            if amount < 0:
                return False

        # Vérifier les signatures requises.
        if self.reqd:
            for addr in self.reqd:
                if not any(verify(data, sig, addr) for sig in self.sigs):
                    return False

        return True

