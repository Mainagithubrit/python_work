#!/usr/bin/env python3
"""a pytgon script that contains a list of places"""

places = ['zimbambe', 'south africa', 'Egypt', 'Morocco']

print(places)

print(sorted(places))

print("\nMy list is still in its original form")
print(places)

print(sorted(places, reverse=True))

print("\nMy list is still in its original form")
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

print("\n")

print(places)
places.sort()
print(places)

print("\n")

print(places)
places.sort(reverse=True)
print(places)
