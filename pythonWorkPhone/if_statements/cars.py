#!/usr/bin/env python3
"""This program loops through a list of cars
and prints a car name in uppercase"""

cars =['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
