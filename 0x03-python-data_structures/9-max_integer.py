#!/usr/bin/python3
def max_integer(mylist=[]):
    if len(mylist) == 0:
        return ("None")
    v = mylist[0]
    for i in mylist:
        if i > v:
            v = i
    return (v)
