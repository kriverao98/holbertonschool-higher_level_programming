#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_printed = 0

    while True:
        try:
            for i in range(x):
                print(my_list[i], end=" ")
                elements_printed += 1

        except IndexError:
            pass
