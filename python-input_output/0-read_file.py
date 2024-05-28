#!/usr/bin/python3
"""This function opens and read a given file."""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        print(file.read())
