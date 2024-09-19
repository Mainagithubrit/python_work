#!/usr/bin/env python3
"""This program creates a list inside a dictionary"""

pizza = { 
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
        }

# summarizing the order
print("You ordered a {}-crust pizza " 
    "with the following toppings: ".format(pizza['crust']))

for topping in pizza["toppings"]:
    print("\t" + topping)