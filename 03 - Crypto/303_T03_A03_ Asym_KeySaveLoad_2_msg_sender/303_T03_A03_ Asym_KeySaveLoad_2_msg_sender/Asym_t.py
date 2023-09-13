#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for Asym.py is correct.
"""
from Asym import *

if __name__ == '__main__':
   
    # Specify file name for key storage 
    keys_file_name = 'samples_test.keys'
    # Specify file name where the encrypted message is located 
    message_file_name = 'message_test.enc'

    # Load encrypted message from the file
    received_message = load_message(message_file_name)

    # Load existing asymmetric keys
    loaded_keys = load_keys(keys_file_name)
    found = False
    # Try to decrypt the loaded message using every existing private key
    # Print the result of each decryption attempt  
    for item in loaded_keys:
        key_name, prv_key, _ = item
        decrypted_message = decrypt(received_message, prv_key)
        if decrypted_message:
            print(f'Sucecss: The message is decoded by {key_name}: "{str(decrypted_message,"utf-8")}"')
            found = True
    if not found:
        print('Fail: The message could not be successfully decoded.')
    