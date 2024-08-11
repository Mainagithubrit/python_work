#!/usr/bin/env python3
"""This code checks the color of a dead alien"""
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")
else:
    print("You have failed!")
    
print("\n")  
"""This one fails the test"""

print(alien_color)
if alien_color == "red":
    print("You have earned 5 points!")
else:
    print("You have failed!")