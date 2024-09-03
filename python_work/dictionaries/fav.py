#!/usr/bin/python3
"""This program loops through a dictionary and prints its values"""

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for name in favorite_language.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_language[name].title()
        print("\t{}, I see you love {}!".format(name.title(), language))