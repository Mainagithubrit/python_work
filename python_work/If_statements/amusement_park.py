#!/usr/bin/env python3
"""Tests for age group of a person"""
age = 66

""""

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("You admission cost is $40")

"""


# A simple way of doing the same code on top

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
    
print("Your admission cost is ${}.".format(price))