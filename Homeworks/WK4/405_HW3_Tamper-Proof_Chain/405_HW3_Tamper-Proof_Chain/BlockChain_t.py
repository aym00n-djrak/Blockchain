#!/usr/bin/env python3
"""
This test case will verify if the provided homework solution by a student for Blockchain.py is correct.
"""
from BlockChain import *
leading_zero = 4

dataG = 'Root'
data1 = 'It is B1'
data2 = 'It is B2'
data3 = 'It is B3'
data4 = 'It is B4'
data5 = 'It is B5'

if __name__ == '__main__':

    # Instantiate different blocks to be added to the chain 
    Gn = CBlock(dataG, None)
    B1 = CBlock(data1, Gn)
    B2 = CBlock(data2, B1)
    B3 = CBlock(data3, B2)
    B4 = CBlock(data4, B3)

    print('\n--- Blocks are created --- Hashes and Nonces should not match!')

    # Check if hashes and nonces of each block are valid
    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        if b.is_valid_hash():
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")

    # Mine each block
    for b, name in [(Gn, 'Gn'), (B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        print(f'\nMining {name} ...')
        b.mine(leading_zero)

    print('\n--- Blocks are mined --- Hashes and Nonces must match!')
    # Check if hashes and nonces of each block are valid
    # Check if block are linked correctly
    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        if b.is_valid_hash():
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")

    # Temper the value of a blok
    data3t = 'It is B3t'
    B3.data = data3t

    print('\n--- Block3 is tampered --- Hashes and Nonces of blocks after B3 should not match!')
    # Check if tempering of block B3 can be detected. 
    # Hashes and Nonces of its block must not match
    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        if b.is_valid_hash():
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")

    # Mine the blockchain again
    for b, name in [(Gn, 'Gn'), (B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        print(f'\nMining {name} ...')
        b.mine(leading_zero)

    print('\n--- Blocks are mined again --- Hashes and Nonces must match again!')
    # Mine the blockchain again
    # Hashes and Nonces must match again
    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        if b.is_valid_hash():
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")