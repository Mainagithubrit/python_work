#!/usr/bin/env python3
"""Creating a default value for a parameter"""

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}".format(animal_type, pet_name.title()))

describe_pet(pet_name='betha', animal_type='cat')
