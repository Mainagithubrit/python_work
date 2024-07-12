#!/usr/bin/env python3
"""this code prints a message for every item on a list"""
names = ['mukami', 'peter', 'juliee', 'njoro']
for name in names:
    message = 'God bless you'
    way = '{}, {}'.format(name.title(), message)
    print(way)
