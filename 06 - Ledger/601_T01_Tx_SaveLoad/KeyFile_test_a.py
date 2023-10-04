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

Many serialization formats support multiple different types of asymmetric keys 
and will return an instance of the appropriate type. You should check that 
the returned key matches the type your application expects when using these methods.

In this scenario we generate a asymmetric keys. Use the private to sign a message. 
Your task is to de-/serialize public key of alex before storing to and when loading from a file. 

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this exercise located in same folder.

To test run 'KeyFile_test_a.py' in your command line

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
    alex_prv, alex_pbc = generate_keys()

    sample_message = b"a test message"
    sig = sign(sample_message, alex_prv)
    print(verify(sample_message, sig, alex_pbc))

    savefile = open("key.dat", "wb")

    # TODO 1: Serialize the public key to bytes
    # Use PEM encoding

    pickle.dump(alex_pbc, savefile)
    savefile.close()

    loadfile = open("key.dat", "rb")
    new_pbc = pickle.load(loadfile)

    # TODO 2: Deserialize a public key from PEM encoded data
    # Load using one of the function that supports asymmetric public key-loading

    loadfile.close()
    print(verify(sample_message, sig, new_pbc))
