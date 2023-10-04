#!/usr/bin/env python3
"""
This test case will verify if the provided exercise solution by a student for Blockchain.py is correct.
"""
from Blockchain import *

class anotherClass:
    string = None
    num = 1264378

    def __init__(self, mystring):
        self.string = mystring
    def __repr__(self):
        return self.string    + str(self.num)

if __name__ == '__main__':

    # Instantiate the genesis block 
    root  = CBlock(b'I am root', None)
    
    # Instantiate another block 
    B1 = CBlock('I am a child!', root)
    
    # Check if blocks are correctly linked  
    if root.computeHash() == B1.previousHash:
        print("Success! B1 hash matches")
    else:
        print("Fail! B1 hash does not match")
    if B1.previousBlock.computeHash() == B1.previousHash:
        print("Success! B1 hash matches")
    else:
        print("Fail! B1 hash does not match")

    # Add more blocks to the chain
    B2 = CBlock('I am a brother', root)        
    B3 = CBlock(b'I contiain bytes', B1)
    B4 = CBlock(12354, B3)
    B5 = CBlock(anotherClass('Hi there!'), B4)
    B6 = CBlock("child of B5", B5)

    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4'), (B5, 'B5')]:
        if b.previousBlock.computeHash() == b.previousHash:
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")

    #Check if tampered blocks can be detected
    B4.data = 12345
    if B5.previousBlock.computeHash() == B5.previousHash:
        print("Fail! Couldn't detect a tamper")
    else:
        print("Success! Tampering is detected")
    
    B5.data.num = 23678
    if B6.previousBlock.computeHash() == B6.previousHash:
        print("Fail! Couldn't detect a tamper")
    else:
        print("Success! Tampering is detected")