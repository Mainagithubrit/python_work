#!/usr/bin/python3
"""This program checks is there is a key in a dictionary"""

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')

# The get method is used specifically in dictionries
# A second argument is optional
# This argument is passed to be returned if a key is not present or doesn't exist

print(point_value)

# If "points" existed you would get its value
# But since it doesn't exist you get the second argument of the get method