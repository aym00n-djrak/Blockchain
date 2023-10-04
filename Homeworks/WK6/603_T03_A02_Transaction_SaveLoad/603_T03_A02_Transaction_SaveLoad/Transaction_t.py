#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for TxBlock.py is correct.
"""
from Signature import generate_keys

from Transaction import Tx

import pickle

if __name__ == "__main__":

    # Generating asymmetric keys for multiple users
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()
    mara_prv, mara_pbc = generate_keys()

    # Creating a transaction from alex to mike and signing it with alex private key
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 1)
    Tx1.add_output(mike_pbc, 1)
    Tx1.sign(alex_prv)

    # Checking the validity of this transaction
    if Tx1.is_valid():
        print("Success! Tx is valid")
    else:
        print("Fails!")

    # Storing transaction data in a file
    # The operation should succeed this time
    savefile = open("tx.dat", "wb")
    pickle.dump(Tx1, savefile)
    savefile.close()

    # Loading transaction data from a file
    # The operation should succeed this time
    loadfile = open("tx.dat", "rb")
    newTx = pickle.load(loadfile)

    # Verifying the validity of the transaction 
    if newTx.is_valid():
        print("Sucess! Loaded tx is valid")
    else:
        print("Fails!")
    loadfile.close()
