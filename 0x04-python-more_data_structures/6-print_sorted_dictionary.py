#!/usr/bin/python3
def print_sorted_dictionary(dict):
    for i in sorted(dict.keys()):
        print("{}: {}".format(i, dict[i]))
