#!/usr/bin/python3
def complex_delete(dict, value):
    tempo = dict.copy()
    for k, v in tempo.items():
        if value == v:
            dict.pop(k)
    return dict
