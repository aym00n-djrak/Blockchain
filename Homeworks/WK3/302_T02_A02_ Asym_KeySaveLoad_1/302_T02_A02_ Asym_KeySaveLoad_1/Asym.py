#!/usr/bin/env python3
"""Asymmetric Cryptography -> Key Management: Tutorial 2

The goal of this tutorial is to learn how to load and store asymmetric keys on the disk.
In previous tutorial you have learned how to generate keys and use them directly to encrypt/decrypt a message, 
but in many cases generated keys are stored on and loaded from a disk when they are needed for a specific application.
As a part of the loading and saving process keys are de-/serialized. 
It is optionally possible to encrypted before saving using a password. In our example no passwords are needed. 
Stored keys in the file system are encoded using PEM encapsulation format. 
This format has BEGIN {format} and END {format} markers to separate keys. 
Stored keys are located in a subdirectory called *storage*

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this tutorial located in same folder.

To test run 'Asym_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit these urls for more information on this topic:
    https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/
    https://docs.python.org/3/library/pickle.html
"""
from tkinter.messagebox import NO
from cryptography.exceptions import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import pickle

def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt(message, key):
    try:
        ciphertext = key.encrypt(message,
                                padding.OAEP(
                                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                    algorithm=hashes.SHA256(),
                                    label=None))
        return ciphertext
    except:
        return False

def decrypt(ciphertext, key):
    try:
        plaintext = key.decrypt(
                                ciphertext,
                                padding.OAEP(
                                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                    algorithm=hashes.SHA256(),
                                    label=None))
        return plaintext
    except:
        return False

# TODO 1: Store the list of keys into a given file.
# Make sure of proper PEM encoding before serialization
def save_keys(keys_file_name, keys_list):
    pass

# TODO2: Load all private and public keys from a given file and return those keys as a list
# Make sure of proper PEM decoding when deserializing
def load_keys(keys_file_name):
    return None
