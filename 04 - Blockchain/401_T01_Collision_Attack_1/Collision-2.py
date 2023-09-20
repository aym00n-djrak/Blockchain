#!/usr/bin/env python3
"""Block Integrity -> Collision: Tutorial 1.2

The goal of this tutorial is to learn how a cryptographic hash function works. 
In addition, how a collision can occur. A hash function takes a data input and returns a fixed length of bits.  
Be aware that some hash algorithms are now known for their hash collision weaknesses. 
In this tutorial you will be able to observe collisions using blake2b digest algorithm. 
This algorithm can have different features dependent on the module your are using, such as:
    * salting, 
    * personalization
    * and tree hashing
In tutorial 1 and 2 you will work with different modules like hashlib and pyblake2. 
Both modules contain blake2b digest algorithm. 
Changing the size of the resulting digest in byte of the blake2b algorithm will reduce the chance of a collision.   

Your task is to:
    * locate the TODOs in this file
    * run this tutorial and observe the output

To test run 'Collision-2.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit these urls for more information on this topic:
    https://docs.python.org/3/library/hashlib.html
    https://pythonhosted.org/pyblake2/module.html#pyblake2.blake2b
"""
from hashlib import blake2b

# TODO 1: Read the code and understand each statement
# TODO 2: Run the code and observe the output
# TODO 3: Change or increment the size of the resulting digest in byte
# TODO 4: Rerun this program after changing the size
hash_size_in_bytes = 1

path = "files"
names_list = []
with open(path + "/names.txt", "r") as f_names:
    names_list = [name.lower() for name in f_names.read().splitlines()]

print(len(names_list))

myname = input("please enter your name: ").lower()
digest = blake2b(digest_size=hash_size_in_bytes)

digest.update(bytes(myname, "utf-8"))
hash_of_myname = digest.hexdigest()
print(hash_of_myname)

found = False
counter = 0
for name in names_list:
    digest = blake2b(digest_size=hash_size_in_bytes)
    digest.update(bytes(name, "utf-8"))
    h = digest.hexdigest()

    if h == hash_of_myname and name != myname:
        print(
            f'hash of "{name.lower()}" has collision with your name "{myname}": hash = {h}'
        )
        found = True
        counter += 1

if found:
    print(f"There are {counter} number of collision with the entered name!")
else:
    print("could not find any collision!")
