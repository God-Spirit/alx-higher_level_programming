#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for a, v in sorted(a_dictionary.items()):
        print('{}: {}'.format(a, v))
