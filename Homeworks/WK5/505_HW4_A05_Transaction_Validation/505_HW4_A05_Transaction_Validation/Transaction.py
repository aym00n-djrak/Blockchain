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
class Tx:
    inputs = None
    outputs =None
    sigs = None
    reqd = None

    # TODO 1: Complete the method
    # These three methods are already done in the previous tutorials
    # you can copy and paste the previous codes here     
    def __init__(self):
        pass
    def add_input(self, from_addr, amount):
        pass
    def add_output(self, to_addr, amount):
        pass
    
    # TODO 2: Complete the method
    # We would like to have another method to add extra required signature if needded (e.g. escrow)
    # with this method, we can specify other required signature to the transaction by adding the 
    # public key of the required signature
    # If this signature is needed, later we can check if the transaction is also signed by that person/party.
    def add_reqd(self, addr):
        pass

    # TODO 3: Complete the method
    # This method is also already done in the previous tutorials.
    # you can copy and paste the previous codes here     
    def sign(self, private):
        pass


    # TODO 4: Complete the method
    # This method is used to validate a transaction.
    # To validate a transaction, we must check few important things:
    #   1 -  Every entery in inputs need to be signed by the relevant sender, and
    #   2 -  If an extra required signature is needed, the signature need to be verified too, and
    #   3 -  The total amount of outputs must not exceed the total amount of inputs.
    def is_valid(self):
        return False