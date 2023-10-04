#!/usr/bin/env python3
"""Transactions -> Ledger (Transaction Blockchain): Tutorial 1

The goal of this tutorial is to learn how custom data structures can be de-/serialized 
before storage and transference. In addition, you will learn how an application will fail 
if serialization is not applied before storing an object in a file.
Any data structure needs to be serialized as a byte stream before storing it 
in a file or transferring it through the network. Pickle module supports such an operation. 
However, it has limited support for data structures to be serialized automatically.
Custom data structures such as asymmetric keys and transactions are not supported natively. 
They need to be serialized before storage. Pickle will throw an exception if it 
does not support the data structure. Some third-party modules such as Cryptography provide 
such serialization functions. Only some objects are needed for storage or transference 
should be serialized. For instance, we might need only to serialize public keys and 
leave private keys not serialized. Depending on your implementation scenario, 
you might also check JSON serialization functions. 

In this scenario we try to store a custom data structure into a file without serialization. 
Pickle will fail to store the byte stream into the file as it does not recognize the object. 
Your task is to try different Pickle.dump() calls and check the output. 

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this exercise located in same folder.

To test run 'TxFile_test_a.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on this topic:
    https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/
    https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/#cryptography.hazmat.primitives.serialization.load_pem_public_key
"""
from Signature import *
from Transaction import *
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
        print("Fail! Tx is invalid")

    # Opening a file to store a transaction data
    savefile = open("tx.dat", "wb")

    # TODO 1: Try different dump() calls by uncommenting it
    # Make sure you uncomment other dump calls before trying a new one
    # Application should stop here as it fails to serialize our custom data structure (transaction)
    pickle.dump(Tx1, savefile)
    pickle.dump(Tx1.inputs[0][0], savefile)
    pickle.dump(alex_pbc, savefile)

    savefile.close()

    loadfile = open("tx.dat", "rb")
    newTx = pickle.load(loadfile)

    if newTx.is_valid():
        print("Sucess! Loaded tx is valid")
    loadfile.close()
