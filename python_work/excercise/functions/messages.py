#!/usr/bin/env python3

def show_messages(text):
    """A function that prints short messages"""
    for txt in text:
        print("\n{}!!!".format(txt.title()))
    return txt

text = ["Jesus loves me", "Because he died for me", "long may he reign"]

show_messages(text)
