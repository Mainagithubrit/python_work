#!/usr/bin/env python3
"""This changes the color, speed, and points of the first three alien dictionaries"""

# making an empty list to store the aliens
aliens = []

# Making a fleet of aliens
for alien_num in range(12):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# shows the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print(...)