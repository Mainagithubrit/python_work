#!/usr/bin/env python3
"""A dictionary that stores favorite language"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print("{}'s favorite language is {}.".format(name.title(), language.title()))