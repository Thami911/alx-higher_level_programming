#!/usr/bin/python3
def delete_at(mylist=[], ids=0):
    if 0 <= ids < len(mylist):
        del(mylist[ids])
    return(mylist)
