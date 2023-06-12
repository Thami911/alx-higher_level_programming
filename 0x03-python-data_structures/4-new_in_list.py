#!/usr/bin/python3
def new_in_list(my_list, idx, element):
      tep_list = my_list[:]
    if 0 <= idx < len(my_list):
        tep_list[idx] = element
        return(tep_list)
    return(my_list)
