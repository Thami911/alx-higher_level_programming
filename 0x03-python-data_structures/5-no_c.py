#!/usr/bin/python3
def no_c(a_string):
    create_str = ""
    for i in a_string:
        if (i != 'c') and (i != 'C'):
            create_str += i
    return (create_str)
