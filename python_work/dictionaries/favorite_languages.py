#!/usr/bin/python3
"""A dictionary with the same information"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print("Sarah's favorite language is {}".format(language))