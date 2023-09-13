#!/usr/bin/env python3
"""
This test case will verify if the provided solution by a student for SongList.py is correct.
"""
from SongList import *

# Instantiate a song list
linkedlist = SongList()
print(linkedlist)

# Instantiate some nodes with values 
linkedlist.head = SongNode("A Hard Day's Night")
second = SongNode('A Day in the Life')
third = SongNode("Strawberry Fields Forever")

# Link nodes instances 
linkedlist.head.next = second
second.next = third
third.next = None

# Traverse through the list and print each song title
linkedlist.printSongs()

# Insert more songs
linkedlist.AddNewSong("She Loves You")
linkedlist.AddNewSong("Something")
linkedlist.printSongs()