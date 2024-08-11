#!/usr/bin/env python3
"""This program checks if a list is empty"""

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding {}.").format(requested_topping)
    print("\nfinished making pizza!")
else:
    print("Are you sure you want a plain pizza?")