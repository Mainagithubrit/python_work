#!/usr/bin/env python3
"""a program that uses while loop to remove repeated instances in a list"""

pets = ['dog', 'cat', 'goldfish', 'cat', 'rabbit', 'cat' ]
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
