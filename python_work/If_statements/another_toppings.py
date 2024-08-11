#!/usr/bin/env python3
"""This code loops through a list and prints a
message if topping is out of stock"""

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding {}.".format(requested_topping))
        
print("\nfinished making pizza!")