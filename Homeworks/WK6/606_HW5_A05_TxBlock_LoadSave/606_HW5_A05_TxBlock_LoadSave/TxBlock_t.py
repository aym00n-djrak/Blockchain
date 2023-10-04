#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for TxBlock.py is correct.
In this test scenario 6 blocks will be created (1 genesis and 5 child blocks). 
A total of 8 transactions will be created. 
Tempering the data on block b1 by adding a valid transaction to it should be detected. 
In addition, Transaction should be printed formmated and human-readable. You shoud add a method
to transaction file to represent a transaction in the desired format.

For the correct format check the 'output.txt' file.
"""

from BlockChain import CBlock
from Signature import generate_keys, sign, verify
import pickle
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

# from Transaction import Tx

from TxBlock import *       


if __name__ == "__main__":
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()
    mara_prv, mara_pbc = generate_keys()

    # Valid Blocks
    ####################
    # Create 2 valid transactions Tx1 and Tx2
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 1)
    Tx1.add_output(rose_pbc, 1)
    Tx1.sign(alex_prv)

    Tx2 = Tx()
    Tx2.add_input(mike_pbc,1.1)
    Tx2.add_output(rose_pbc, 1)
    Tx2.sign(mike_prv)

    # Add Tx1 and Tx2 to the first block (genesis block)
    root = TxBlock(None)
    root.addTx(Tx1)
    root.addTx(Tx2)

    # Create 2 more valid transactions Tx3 and Tx4
    Tx3 = Tx()
    Tx3.add_input(rose_pbc,1.1)
    Tx3.add_output(alex_pbc, 1)
    Tx3.sign(rose_prv)
    
    Tx4 = Tx()
    Tx4.add_input(mike_pbc,1)
    Tx4.add_output(mara_pbc, 1)
    Tx4.add_reqd(rose_pbc)
    Tx4.sign(mike_prv)
    Tx4.sign(rose_prv)

    # Add Tx3 and Tx4 to the second block (the child of the genesis block)
    B1 = TxBlock(root)
    B1.addTx(Tx3)
    B1.addTx(Tx4)

    # Save the block B1 on the disk
    savefile = open("block.dat", "wb")
    pickle.dump(B1, savefile)
    savefile.close()

    # Creat new valid transaction Tx5
    Tx5 = Tx()
    Tx5.add_input(rose_pbc, 2.3)
    Tx5.add_output(mike_pbc, 2.3)
    Tx5.sign(rose_prv)
    # Create a new block (a child of the block B1), and the transaction Tx5 to the block
    B2 = TxBlock(B1)
    B2.addTx(Tx5)

    # Load the block B1 from the disk
    loadfile = open("block.dat" ,"rb")
    load_B1 = pickle.load(loadfile)
    loadfile.close()

    for b in [root, B1, B2, load_B1]:
        if b.is_valid():
            print ("Success! Valid block is verified.")
        else:
            print ("Error! Valid block is not verified.")

    # Invalid Blocks
    ######################
    # Creat an invalid transaction Tx6 
    Tx6 = Tx()
    Tx6.add_input(mara_pbc, 2.0)
    Tx6.add_output(rose_pbc, 15.3)
    Tx6.sign(mara_prv)
    B3 = TxBlock(B2)
    B3.addTx(Tx6)

    # Creat an invalid transaction Tx7
    Tx7 = Tx()
    Tx7.add_input(rose_pbc, 2.3)
    Tx7.add_output(mike_pbc, 2.3)
    Tx7.sign(mike_prv)
    B4 = TxBlock(B3)
    B4.addTx(Tx7)

    # Creat an invalid transaction Tx8
    Tx8 = Tx()
    Tx8.add_input(mike_pbc, 0.9)
    Tx8.add_output(mara_pbc, 0.8)
    Tx8.add_reqd(rose_pbc)
    Tx8.sign(mike_prv)
    B5 = TxBlock(B4)
    B5.addTx(Tx8)

    # Tamper the block before B1 by adding a valid transaction to it
    # This will make the block B1 (the block after the tampered block) invlaid
    B1.previousBlock.addTx(Tx4)

    for b in [B1, B3, B4, B5]:
        if b.is_valid():
            print("Error! Invalid block is verified.")
        else:
            print("Success! Invalid blocks is detected.")
    
    print('Tx4\n', Tx4)
    print('Tx5\n', Tx5)
