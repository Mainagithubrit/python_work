#!/usr/bin/env python3
"""This program checks if a person is a baby,
toddler, kid, teenager, adult or elder"""

age = 17

if age < 2:
    print("\nYou are a Baby!\n")
elif age >= 2 and age < 4:
    print("\nYou are a Toddler!\n")
elif age >= 4 and age < 13:
    print("\nYou are a kid!\n")
elif age >= 13 and age < 20:
    print("\nYou are a Teenager!\n")
elif age >= 20 and age < 65:
    print("\nYou are an Adult!\n")
else:
    print("\nYou are an Elder!\n")