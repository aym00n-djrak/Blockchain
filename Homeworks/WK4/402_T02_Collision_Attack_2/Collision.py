#!/usr/bin/env python3
"""Block Integrity -> Collision Attack: Tutorial 2

The goal of this tutorial is to learn how a cryptographic hash function can be attacked. 
In such an attack the attacker tries to find two different messages m1 and m2 such that hash(m1) = hash(m2). 
In other words he tries to find two inputs producing the same hash value 
Changing the size of the resulting digest in byte of the blake2b algorithm will reduce the chance of a collision attack.   

Your task is to:
    * locate the TODOs in this file
    * run this tutorial and observe the output

To test run 'Collision.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
"""
from hashlib import blake2b
import random
import string

# TODO 1: Read the code and understand each statement
# TODO 2: Run the code and observe the output
# TODO 3: Change or increment the size of the resulting digest in byte
# TODO 4: Re-run this program after changing the size 
hash_size_in_bytes = 2

def gen_random_string(n):
    rnd_char = string.ascii_letters + string.digits + string.punctuation + string.punctuation

    rnd_string = ''
    for _ in range(n):
        rnd_string += random.choice(rnd_char)

    rnd_list = list(rnd_string)
    random.SystemRandom().shuffle(rnd_list)
    rnd_string = ''.join(rnd_list)

    return rnd_string


myname = input('please enter your name: ').lower()
digest = blake2b(digest_size = hash_size_in_bytes)

digest.update(bytes(myname, 'utf-8'))
hash_of_myname = digest.hexdigest()
print(hash_of_myname)

found = False
counter = 0
for _ in range(1000000):
    digest = blake2b(digest_size = hash_size_in_bytes)
    rnd_str = gen_random_string(8)
    print(rnd_str, end='\r')
    digest.update(bytes(rnd_str, 'utf-8'))
    h = digest.hexdigest()

    if h == hash_of_myname:
        print(f'hash of "{rnd_str}" has collision with your name "{myname}": hash = {h}')
        found = True
        counter += 1

if found:
    print(f'Total number of collisions = {counter}')
else:
    print('Could not find a collision!')