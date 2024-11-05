#!/usr/bin/env python3
"""This is a program that makes sandwiches"""

sandwich_orders = ['ham', 'chicken', 'bacon', 'hot dog']

finished_sandwiches = []

while sandwich_orders:

    my_sandwich = sandwich_orders.pop()
    print("Making a {} sandwich for you!!".format(my_sandwich.title()))

    finished_sandwiches.append(my_sandwich)

print('\nThis are all the sandwiches that have been made: ')
for sandwich in finished_sandwiches:
    print(sandwich)

print(finished_sandwiches)
