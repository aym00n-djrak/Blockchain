#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for Signature.py is correct.
"""
from Signature import *

if __name__ == '__main__':
    
    # Generate asymmetric keys for two users
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()

    alex_message = b'pay 10 euro to bob'

    # Verification of a signature using public key:
    # If Alex sign it:
    alex_signature = sign(alex_message, alex_prv)
    
    verified = verify(alex_message, alex_signature, alex_pbc)
    if verified:
        print('Success: Valid signature is verified.')
    else:
        print('Fail: Valid signature is not verified.')

    # If Mike sign it:
    f_signature = sign(alex_message, mike_prv)
    
    verified = verify(alex_message, f_signature, alex_pbc)
    if verified:
        print('Fail: Invalid signature is verified.')
    else:
        print('Success: Invalid signature is not verified.')

    # Check originality of message using public key:
    received_message = b'pay 10 euro to bob'
    correct = verify(received_message, alex_signature, alex_pbc)
    if correct:
        print('Success: The received message is validated as original.')
    else:
        print('Fail: The received message is validated as tampered.')

    t_message = b'pay 100 euro to bob'
    correct = verify(t_message, alex_signature, alex_pbc)
    if correct:
        print('Fail: The tampered Message is not validated as original.')
    else:
        print('Success: The tampered Message is correctly detected.')
