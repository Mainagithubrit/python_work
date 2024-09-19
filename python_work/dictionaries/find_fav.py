#!/usr/bin/env python3
"""This program finds if a person in a dictionary has polled"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')