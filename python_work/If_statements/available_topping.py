#!/usr/bin/env python3
"""This program checks if a topping is available"""

available_toppings = ['mushrooms', 'olives', 'green peppers',
                    'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding {}.".format(requested_topping))
    else:
        print("Sorry, we don't have {}.".format(requested_topping))
        
print("\nfinished making pizza")