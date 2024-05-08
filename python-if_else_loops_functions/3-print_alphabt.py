#!/usr/bin/python3
"""
Prints all lowercase letters of the alphabet except for 'q' and 'e'.
"""
for i in range(97, 123):
    if i != 113 and i != 101:
        print("{}" .format(chr(i)), end='')
