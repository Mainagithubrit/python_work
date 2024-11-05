#!/usr/bin/env python3
"""This is a program that makes sandwiches"""

sandwich_orders = ['pastrami', 'ham', 'chicken','pastrami', 'bacon', 'hot dog','pastrami']

finished_sandwiches = []

print("\nThe Deli has run out of Pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:

        my_sandwich = sandwich_orders.pop()
        print("Making a {} sandwich for you!!".format(my_sandwich.title()))

        finished_sandwiches.append(my_sandwich)

print('\nThis are all the sandwiches that have been made: ')

for sandwich in finished_sandwiches:
    print(sandwich)

print(finished_sandwiches)

