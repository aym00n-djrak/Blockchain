#!/usr/bin/env python3
"""
Transaction Class - Definition of Input and Output

This is just a copy of the previous tutorial. If you have already completed the previous tutorial,
simply copy and paste the code of transaction class, here.

Check the test file. It includes signing and verification of transactions
using this new defined transaction class. 
"""

from Signature import *


class Tx:
    def __init__(self):
        self.inputs = []
        self.outputs = []

    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))

    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))
