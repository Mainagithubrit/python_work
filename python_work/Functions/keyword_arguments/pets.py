#!/usr/bin/env python3
"""This function uses keyword arguments"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a {}.".format(animal_type))
    print("My {}'s name is {}.".format(animal_type, pet_name))

describe_pet(animal_type='dog', pet_name='betha')
