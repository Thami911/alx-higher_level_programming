#!/usr/bin/python3
def replace_in_list(a_list, ids, elems):
    if 0 <= ids < len(a_list):
        a_list[ids] = elems
    return(a_list)
