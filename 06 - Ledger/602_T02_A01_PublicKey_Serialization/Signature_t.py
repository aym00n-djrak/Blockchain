#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for Signature.py is correct.
"""
from Signature import *

if __name__ == '__main__':
# Generating asymmetric keys for both alex and mike
    # returned public key of both mike and alex should be serialized
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()

    alex_message = b'pay 10 euro to bob'


# Verification of a signature using public key:

    # It should be correct because Alex is signing it and we verifying using his public key
    alex_signature = sign(alex_message, alex_prv)
    
    verified = verify(alex_message, alex_signature, alex_pbc)
    if verified:
        print('Success: Correct signature is verified')
    else:
        print('Error: Correct signature is not verified')

    # It should be correct because mike is signing it and we verifying using alex public key
    f_signature = sign(alex_message, mike_prv)
    
    verified = verify(alex_message, f_signature, alex_pbc)
    if not verified:
        print('Success: Wrong signature is not verified')
    else:
        print('Error: Wrong signature is  verified')

# Check originality of message using public key:
    # It should be original because alex is signing it and we verifying using alex public key
    correct = verify(b'pay 10 euro to bob', alex_signature, alex_pbc)
    if correct:
        print('Sucsess: Original message is verified')
    else:
        print('Error: Original message is not verified')


    # It should be tempered because alex signature of the message is different
    t_message = b'pay 100 euro to bob'
    correct = verify(t_message, alex_signature, alex_pbc)
    if not correct:
        print('Sucsess: Tampered message is detected')
    else:
        print('Error: Tampered message is not detected')