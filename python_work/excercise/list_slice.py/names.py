#!/usr/bin/env python3
"""This program uses slice to slice through a list"""

cars = ['hilux', 'swift', 'cullinan', 'compressor', 'escalade', 'yukon']

cars_slice = cars[0:3]
print('The first three items in the list are:')
for car in cars_slice:
    print(car)
    
skip = '\n'
print(skip)

cars_slice = cars[2:5]
print('Three items from the middle of the list are:')
for car in cars_slice:
    print(car)
    
print(skip)

cars_slice = cars[3:]
print('The last three items in the list are:')
for car in cars_slice:
    print(car)
