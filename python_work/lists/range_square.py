#!/usr/bin/env python3
"""This function squares a list of numbers in the range of 1 to 10"""
squares = []
for value in range(1, 11):
    # square = value **2
    # squares.append(square)
    squares.append(value ** 2)
    
print(squares)