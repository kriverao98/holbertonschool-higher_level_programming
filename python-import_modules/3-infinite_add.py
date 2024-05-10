#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)
    sum = 0
    for i in range(argc):
        sum += int(argv[i])
    print("{}".format(sum))
