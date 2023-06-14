#!/usr/bin/python3
def simple_delete(dict, key=""):
    if key in dict:
        del dict[key]
    return (dict)
