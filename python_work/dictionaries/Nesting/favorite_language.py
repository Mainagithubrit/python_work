#!/usr/bin/env python3
"""This program loops through a dictionary with its value as a list"""

favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_language.items():
    if len(languages) == 1:
        print("\n {}'s favorite language is {}".format(name.title(), languages[0].title()))
    elif len(languages) >= 2:
        print("\n {}'s favorite languages are:".format(name.title()))
        for language in languages:
            print("\t {}".format(language.title()))