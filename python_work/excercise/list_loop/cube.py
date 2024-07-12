#!/usr/bin/env python3
"""This code creates a list of numbers cubed to the power of three"""
cube = [num ** 3 for num in range(1,11)]
print(cube)

# This code does the same thing as the first one
"""cube = []
for num in range(1,11):
 cube.append(num ** 3)
print(cube)"""