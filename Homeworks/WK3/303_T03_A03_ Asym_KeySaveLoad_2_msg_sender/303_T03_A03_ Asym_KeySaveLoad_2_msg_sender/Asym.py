#!/usr/bin/env python3
"""Asymmetric Cryptography -> Message Receive: Tutorial 3

The goal of this tutorial is to learn how to read a decrypted message from a file.
In previous tutorial you have learned how to store and load asymmetric keys. 
When a user receives a messages it is normally encrypted. 
To simplify the implementation we assume the received encrypted message is stored in 
a file called *message_test.enc*. Asymmetric keys are stored in the file *samples_test.keys*.

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
# from tkinter.messagebox import NO
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

def save_keys(keys_file_name, keys_list):
    keys_ser_list = []
    for item in keys_list:
        key_name, private_key, public_key = item
    
        prv_ser = private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()  
                    )
        pbc_ser = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
        
        keys_ser_list.append((key_name, prv_ser, pbc_ser))
    
    savefile = open(keys_file_name, "wb")
    pickle.dump(keys_ser_list, savefile)
    savefile.close()

def load_keys(keys_file_name):
    loadfile = open(keys_file_name, "rb")
    keys_list_ser = pickle.load(loadfile)
    loadfile.close()

    keys_list = []
    for item in keys_list_ser:
        key_name, private_key_ser, public_key_ser = item
        private_key = serialization.load_pem_private_key(private_key_ser,password=None)
        public_key = serialization.load_pem_public_key(public_key_ser)

        keys_list.append((key_name, private_key, public_key))
    return keys_list

# TODO 1: Load message from a given file and return it
# Make sure of passing proper arguments to open a file in read mode
def load_message(file_name):
    return None
