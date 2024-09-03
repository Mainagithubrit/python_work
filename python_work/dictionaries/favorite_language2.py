#!/usr/bin/env python3
"""Looping through a dictionary using keys method to print the keys only"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name in favorite_languages.keys():
    print(name.title())