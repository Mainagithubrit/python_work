#!/usr/bin/python3
"""Store programming vocabularies and meanings"""

words = {
    'Methods': 'Functions used for specific tasks',
    'Integers': 'This is a datatype that is used as numbers',
    'Variables': 'This is a datatype that is used to store objects',
    'List': 'This is a list of deferent datatypes',
    'Tuples': 'This is an unchangeable list',
    'Dictionary': 'This is a list with key-value pairs',
    'Loop': 'This is a statements that goes through a task a few number of times',
    'If statements': 'This are conditional statements to check a condition',
}

for key, value in words.items():
    print("\n{}, {}".format(key, value))