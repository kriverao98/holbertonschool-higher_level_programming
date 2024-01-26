#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    if argc == 0:
        print("0 aguments.")
    else:
        print("{} arguments:".format(argc))
        for i, arg in enumerate(argv, start=1):
            print("{}: {}".format(i, arg))
