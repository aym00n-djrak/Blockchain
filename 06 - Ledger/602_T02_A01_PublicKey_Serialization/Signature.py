#!/usr/bin/env python3
"""Transactions -> Ledger (Key Serialization): Tutorial 2

The goal of this tutorial is to learn how implement serialization mechanism into 
different method to simplify your operation. Due to the scope limitation of this tutorial 
we expect de-/serialization calls to be part of methods implementation (generate_keys() and verify()). 
In an ideal scenario It would be more convenient to implement it in a more abstract way
as a part of your custom data structure   

In this scenario we serialize only the generate public key of a user when keys are generated.
The private key remain as it is. When verifying the signature it is expected that the given public key 
should be deserialized before usage. 
It is expected that you rebuild Signature module to work with serialized keys 


Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this exercise located in same folder.

To test run 'Signature_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on this topic:
    https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/
    https://cryptography.io/en/latest/hazmat/primitives/asymmetric/serialization/#cryptography.hazmat.primitives.serialization.load_pem_public_key
"""
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization


# TODO 1: Generate first a private key, then a public key. As a result return both values.
# Make sure you generate the keys in the correct order.
# Use recommended algorithm values where possible
# Suggested key size 2048
def generate_keys():
    # Generate a private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Generate a corresponding public key
    public_key = private_key.public_key()

    # Serialize the public key before returning its value
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    return private_key, public_key_bytes


# TODO 2: Sign a passed message using the passed private key
# Signing and verifying algorithms must be the same
def sign(message, private_key):
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256(),
    )
    return signature


# TODO 3: Verify a signature for a message with the passed public key
# Signing and verifying algorithms values must be the same
# Make sure to handle exception properly if verification fails
def verify(message, signature, pbc_ser):
    # Deserialize the public key before verifying the signature of a message
    public_key = serialization.load_pem_public_key(pbc_ser)

    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )
        return True
    except InvalidSignature:
        return False
