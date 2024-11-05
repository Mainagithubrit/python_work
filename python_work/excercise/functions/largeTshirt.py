#!/usr/bin/env python3
"""Updating Tshirt.py for all shirts to be large"""

def make_shirt(message='i love python', size='Large'):
    """A function that prints size of T-shirt and message to be printed"""
    print("\nThis T-shirt is {}".format(size))
    print("The message to be printed is {}".format(message.title()))

make_shirt()
make_shirt(size='medium')
