#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        print(c, "is lower")
        return True
    else:
        print(c, "is upper")
        return False
    