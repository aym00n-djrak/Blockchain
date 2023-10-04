#!/usr/bin/env python3
"""Block Integrity -> File Comparison: Tutorial 3

The goal of this tutorial is to learn how a cryptographic hash function can be applied on files.
This technique is called 'compare-by-Hash'. Instead of comparing files byte-by-byte, we compare their hashes. 
In case they differ, then the files are certainly different. 
This technique can be useful when file comparison is needed over the network. Instead of sending
a large file we sending a small hash digest. Another use case is to check if a file has been tampered.
This technique calculates a digest and does not alter the original file. 
  
Your task is to:
    * locate the TODOs in this file
    * complete the code and compare the hash of the original file with other received files
    * find out which file is not tampered and is exaclty equal to the original file

To test run 'FileComparison.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on this topic:
    https://home.cs.colorado.edu/~jrblack/papers/cbh.html
"""
from cryptography.hazmat.primitives import hashes
from os import listdir
from os.path import isfile, join


path = 'files'

with  open(path + '/original.png', 'rb') as original_file:
    content = original_file.read()

# TODO 1: Find the hash of the original file
# use SHA256() hash function

original_hash = hashes.Hash(hashes.SHA256())
original_hash.update(content)
original_hash = original_hash.finalize()

file_list = [f for f in listdir(path + '/received/') if isfile(join(path + '/received/', f))]

# TODO 2: Find the hash of the received files using the same hash function in a loop
# and compare them with the hash of original file
# find out which file is not tampered? 

for f in file_list:
    with  open(path + '/received/' + f, 'rb') as copy_file:
        content = copy_file.read()
        
    hash = hashes.Hash(hashes.SHA256())
    hash.update(content)
    hash = hash.finalize()

    if hash == original_hash:
        print(f, 'is original!')
    else:
        print(f, 'is tampered!')