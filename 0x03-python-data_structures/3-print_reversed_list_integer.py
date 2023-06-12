#!/usr/bin/python3
def print_reversed_list_integer(all_list=[]):
    if all_list is None:
        return
    for x in reversed(all_list):
        print('{:d}'.format(x))
