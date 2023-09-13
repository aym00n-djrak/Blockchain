#!/usr/bin/env python3
"""Linked Lists -> Song List Implementation: Exercise 1

The goal of this exercise is to learn how to create a custom linked list for songs.
Each node in this linked list represent a song.
This data structure consists of a collection of songs(node) which together represent a playlist.  
The SongList class contains methods to insert a song, and traversal through the list to print titles. 

Your task is to:
    * locate the TODOs in this file
    * complete the missing part from the code 
    * run the test of this tutorial located in same folder.

To test run 'SongList_t.py' in your command line

Notes:
    * do not change class structure or method signature to not break unit tests
    * visit this url for more information on linked list:
    https://realpython.com/linked-lists-python/
"""


class SongNode:
    def __init__(self, song_title=None, next=None):
        self.song_title = song_title
        self.next = next


class SongList:
    def __init__(self):
        self.head = None

    # TODO 1: Traverse through the list and print every song titles
    def printSongs(self):
        if not self.head:
            print("Nothing is printed")

        current = self.head
        while current:
            print(current.song_title)
            current = current.next

    # TODO 2: Insert a new song title to the end of the list
    def AddNewSong(self, new_song_title):
        new_song = SongNode(new_song_title)
        if not self.head:
            self.head = new_song
            return self

        current = self.head
        while current.next:
            current = current.next
        current.next = new_song
        return self
