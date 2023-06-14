#!/usr/bin/python3
def square_matrix_simple(mtx=[]):
    return ([list(map(lambda x: x * x, row)) for row in mtx])
