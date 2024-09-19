#!/usr/bin/env python3
"""This program loops through a dictionary within dictionary"""
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print("\n Username: {}".format(username))
    full_name = "{} {}".format(user_info['first'], user_info['last'])
    location = user_info['location']
    
    print("\tFullname: {}".format(full_name.title()))
    print("\tLocation: {}".format(location.title()))   