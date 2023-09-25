#!/usr/bin/env python3
"""
Transaction Class - Definition of Input and Output

The goal of this tutorial is to learn how to create a simple class for transactions.
A transaction is composed of a list of Inputs and a list of outputs, and few methods.

    Inputs: There are one or more inputs in a transactions which indicates the senders and the 
        amount from each sender.
    Outputs:There are one or more outputs in a transactions which indicates the receivers and the 
        amount to each receiver.

    Note: Senders and Recievers are addressed by their public keys.

    add_input() and add_output() should add inputs and outputs to a transaction.


Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this tutorial located in same folder.

To test run 'Transactions_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
"""


class Tx:

    # TODO 1: Complete the method
    # In this method, you should initialize the variables for inputs and ouputs 
    # of a transaction. 
    # Inputs and Ouputs should be defined as list, where a list of senders (and the sending amount), 
    # and a list of receivers (and the receiving amount) are stored.
    def __init__(self):
        self.inputs = []
        self.outputs = []


    # TODO 2: Complete the method
    # This method should add a new sender and the associated amount to the list of inputs
    # An input is a list of senders (from_addr) and the amount sent by each sender (amount)
    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))


    # TODO 3: Complete the method
    # This method should add a new receiver and the associated amount to the list of outputs
    # An output is a list of receivers (to_addr) and the amount recived by each receiver (amount)
    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))
