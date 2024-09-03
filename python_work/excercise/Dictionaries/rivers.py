#!/usr/bin/env python3
"""This is a program that prints rivers and the countries they are in"""
rivers = {
    'nile': 'egypt',
    'niger': 'guinea',
    'congo': 'congo'
}
for key, value in rivers.items():
        print("{} river passes through {}.".format(key.title(), value.title()))

print("\n")

for river in rivers.keys():
    print(river.title())
    
print("\n")

for country in rivers.values():
    print(country.title())
