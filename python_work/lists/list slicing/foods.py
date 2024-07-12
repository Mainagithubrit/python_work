#!/usr/bin/env python3
"""this program copies a list"""
my_foods = ['ugali', 'nyama', 'chapo', 'mayai']
friend_foods = my_foods[:3]

my_foods.append("smokie")
friend_foods.append('frozen yorghurt')

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favourite foods are:")
for food in friend_foods:
    print(food)
 # This slicing [2:] means you will slice 0, 1 index
 # This slicing [:3] means you will slice the 3 index

