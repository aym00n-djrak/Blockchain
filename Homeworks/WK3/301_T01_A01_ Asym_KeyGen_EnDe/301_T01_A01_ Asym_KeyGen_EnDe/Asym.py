#!/usr/bin/env python3
"""Asymmetric Cryptography -> Key Generation: Tutorial 1

The goal of this tutorial is to learn how to generate and use asymmetric keys.
Additionally, you will learn how to encrypt and decrypt messages using generated private and public keys.
In this implementation the message is a string converted to a byte object.
Both methods encrypt and decrypt accept two args: a message and a key to perform its operation.

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this tutorial located in same folder.

To test run 'Asym_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on this topic:
    https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/
"""

from cryptography.exceptions import *
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


# TODO 1: Generate first a private key, then a public key. As a result return both values.
# Make sure you generate the keys in the correct order. 
# Use recommended algorithm values where possible
# Suggested key size 2048
def generate_keys():
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public = private.public_key()
    return private, public

# TODO 2: Encrypt a passed message using the provided key
# Suggested algorithm is SHA256() 
def encrypt(message, key):
    try: 
        ciphertext = key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
        return ciphertext
    except:
        return False
    
# TODO 3: Decrypt a passed message using the provided key
# Make sure using the same recommended algorithm values for encryption and decryption
# Suggested algorithm is SHA256(). 
def decrypt(ciphertext, key):
    try:
        message = key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )
        return message
    except:
        return False

