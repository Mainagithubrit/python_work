#!/usr/bin/env python3
"""This program loops through a dictionary in a sorted order"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in sorted(favorite_languages.keys()):
    print("{}, thank you for taking the poll".format(name.title()))