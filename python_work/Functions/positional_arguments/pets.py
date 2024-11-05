#!/usr/bin/env python3
"""A function that shows which kind of animal a pet is"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a {}".format(animal_type))
    print("My {}'s name is {}".format(animal_type, pet_name.title()))

describe_pet('dog', 'betha')
describe_pet('dog', 'lia')
