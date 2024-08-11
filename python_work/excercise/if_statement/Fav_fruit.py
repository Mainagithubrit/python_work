#!/usr/bin/env python3
"""This code checks if a fruit is in my list"""
favorite_fruit = ['banana', 'pineapple', 'orange']

for fruit in favorite_fruit:
    if fruit == 'banana':
        print("\nI love {}".format(fruit))
    elif fruit == 'pineapple':
        print("\n{} are really sweet\n".format(fruit))
    elif fruit == 'orange':
        print("An {} contains citric acid\n".format(fruit))
    else:
        print("\nNot in my list")