#!/usr/bin/env python3
"""This program prints a list of animals"""
animals = ['Tiger', 'Lion', 'Jaguar']
for animal in animals:
    animal1 = 'The {} is the largest of the big cat'.format(animals[0].lower())

    animal2 ='The {} is the second largest of the big cat'.format(animals[1].lower())
   
    animal3 = 'The {} is the third largest of the big cat'.format(animals[2].lower())
    print("\n")
    print(animal1)
    print(animal2)
    print(animal3)
    
    print("\n")
    
    print("These animals are the big cats")