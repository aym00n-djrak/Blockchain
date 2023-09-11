#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for Asym.py is correct.
"""
from Asym import *

if __name__ == '__main__':
    
    # Create an empty list
    keys_list = []

    # Generate asymmetric keys for several users 
    # Save all keys to the list
    alex_prv, alex_pbc = generate_keys()
    keys_list.append(('alex', alex_prv, alex_pbc))

    mike_prv, mike_pbc = generate_keys()
    keys_list.append(('mike', mike_prv, mike_pbc))

    rose_prv, rose_pbc = generate_keys()
    keys_list.append(('rose', rose_prv, rose_pbc))

    mara_prv, mara_pbc = generate_keys()
    keys_list.append(('mara', mara_prv, mara_pbc))

    john_prv, john_pbc = generate_keys()
    keys_list.append(('john', john_prv, john_pbc))

    lily_prv, lily_pbc = generate_keys()
    keys_list.append(('lily', lily_prv, lily_pbc))

    # Specify the file name for key storage
    keys_file_name = 'samples.keys'
    # Save keys to the file
    save_keys(keys_file_name, keys_list)
    # Load keys
    loaded_keys = load_keys(keys_file_name)

    plain_message = b'This is a test message!'

    # Test if a message can be encrypted/decrypted using asymmetric key combination of each user 
    for item in loaded_keys:
        key_name, prv_key, pbc_key = item
        ciphertext = encrypt(plain_message, pbc_key)
        decrypted_message = decrypt(ciphertext, prv_key)
        if decrypted_message == plain_message:
            print(f'Success: The message is correctly encrypted and decrypted by {key_name}')
        else:
            print(f'Fail: The message could not be decrypted by {key_name}')
    
