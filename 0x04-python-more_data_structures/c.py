#!/usr/bin/python

def search_replace(my_list, search, replace):
    for x in my_list:
        if x == search:
            list.append(replace)
        else:
            list.append(x)
            return my_list
