#!/usr/bin/python3
def weight_average(own_lists=[]):
    if not own_lists:
        return 0

    avg_number = 0
    size_den = 0

    for tup in own_lists:
        avg_number += tup[0] * tup[1]
        size_den += tup[1]

    return (avg_number / size_den)
