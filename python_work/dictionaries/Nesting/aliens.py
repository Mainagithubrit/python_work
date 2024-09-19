#!/usr/bin/env python3
"""Storing a fleet of aliens in a list,
which are constantly being generated,
each alien is a dictionary"""

# an empty list to store aliens
aliens = []

# making a fleet of aliens
for alien_num in range(12):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Make the first 5 aliens
for alien in aliens[:5]:
    print(alien)
    
print("...")

# showing the number of aliens that have been created
print("Total number of aliens: {}".format(len(aliens)))
