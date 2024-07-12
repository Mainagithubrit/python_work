#!/usr/bin/env python3
"""This program slices through a list of foods"""

skip = '\n'
foods = ['ugali', 'kienyeji', 'chapo', 'guacomoli']
cp_foods = foods[:]

print(skip)
print('My favorite pizzas are:')
foods.append('mayai')
for food in foods:
    print(food)


print(skip)

print('My friend’s favorite pizzas are:')
cp_foods.append('sweet potato')
for food in cp_foods:
    print(food)

