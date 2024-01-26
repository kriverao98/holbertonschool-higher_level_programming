#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    print("{} arguments.".format(argc))
    if argc > 0:
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))