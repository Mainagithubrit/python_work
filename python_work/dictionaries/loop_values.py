#!/usr/bin/env python3
"""This code loops through values in a dictionary"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("The following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())